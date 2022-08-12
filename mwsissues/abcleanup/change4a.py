#-*- coding:utf-8 -*-
"""change4a.py 
 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec canno t encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason


def default_changes(base):
 changes = (
  ('(%s '%base,  '(<ab>%s.</ab> '%base),
  ('(%s.'%base,  '(<ab>%s.</ab>'%base),
  ('(%s,'%base,  '(<ab>%s.</ab>'%base),
  ('(%s:'%base,  '(<ab>%s.</ab>'%base),

  (' %s '%base,  ' <ab>%s.</ab> '%base),
  (' %s.'%base,  ' <ab>%s.</ab>'%base),
  (' %s,'%base,  ' <ab>%s.</ab>'%base),
  (' %s:'%base,  ' <ab>%s.</ab>'%base),
  
  ('[%s '%base,  '[<ab>%s.</ab> '%base),
  ('[%s.'%base,  '[<ab>%s.</ab>'%base),
  ('[%s,'%base,  '[<ab>%s.</ab>'%base),
  ('[%s:'%base,  '[<ab>%s.</ab>'%base),

 )
 return changes

def change1(line):
 base = 'cf'
 newline = newline_default(line,base)
 return newline

def change2(line):
 base = 'sc'
 newline = newline_default(line,base)
 return newline

def change3(line):
 base = 'aor'
 newline = newline_default(line,base)
 return newline

def change4(line):
 base = 'subj'
 newline = newline_default(line,base)
 return newline

def change5(line):
 base = 'abstr'
 newline = newline_default(line,base)
 return newline

def change6(line):
 base = 'gram'
 newline = newline_default(line,base)
 return newline

def change7(line):
 base = 'irreg'
 newline = newline_default(line,base)
 return newline

def change8(line):
 base = 'q.v.'
 changes = (
  (' q.v.',' <ab>q.v.</ab>'),
  (' qq.v.',' <ab>qq.v.</ab>'),
  ('[q.v.' ,'[<ab>q.v.</ab>'),
  ('(q.v.' ,'(<ab>q.v.</ab>'),
 )
 newline = newline_default(line,base,changes=changes)
 return newline

def change9(line):
 changes = (
  ('<ls>A.</ls>D.', '<ab>A.D.</ab>'),
 )
 newline = line
 for old,new in changes:
  newline = newline.replace(old,new)
 return newline

def change10(line):
 base = 'acc'
 newline = newline_default(line,base)
 return newline

def change11(line):
 base = 'comp'
 newline = newline_default(line,base)
 return newline

def newline_default(line,base,changes=None):
 if changes == None:
  changes = default_changes(base)
 if base not in line:
  return line
 dbg = line.startswith('<s>a/pya</s>')
 dbg = False
 #dbg = '(cf <s>an-agArin</s>)' in line
 parts = re.split(r'(<.*?>)',line)
 tagstack = []
 tag = None
 newparts = []
 for part in parts:
  if part.startswith('<'):
   newpart = part
   if part.endswith('/>'): # empty tag
    pass
   elif part.startswith('</'): # closing tag
    etag = part[2:-1]
    if (tagstack != []) and (etag == tagstack[-1]):
    #if etag == tag:
     tag = tagstack.pop()
    else:
     # error
     #print('change1 ERROR closing tag',etag,tag)
     #print('line=',line)
     return None
   else:
    # new opening tag
    m = re.search(r'<([^ >]*)',part)
    tag = m.group(1)
    tagstack.append(tag)
  elif tagstack != []:
   # text within a tag. skip entirely
   newpart = part
  else:
   newpart = part
   for old,new in changes:
    newpart = newpart.replace(old,new)
  if newpart != part:
   print('"%s"' %newpart)
  newparts.append(newpart)
  if dbg: print('part   =',part,'\n   newpart=',newpart,"\n   tagstack=",tagstack,tag)
 newline = ''.join(newparts)
 return newline   

def change_director(option):
 fname = 'change'+option
 if fname in globals(): #locals():
  fun = globals()[fname]
  return fun
 else:
  print('ERROR: no function ',fname)
  exit(1)
 
def init_changes(lines,opption):
 changes = [] # array of Change objects
 changefun = change_director(option) # function associated with option
 metaline = None
 page = None
 for iline,line in enumerate(lines):
  line = line.rstrip('\r\n')
  if line.startswith('<L>'):
   metaline = line
   continue
  if line == '<LEND>':
   metaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  if metaline == None:
   continue
  oldline = line
  # generate change
  newline = changefun(line)
  if newline == None: # error
   print('ERROR:',iline+1,"\n",line)
   exit(1)
  if newline == oldline:
   continue
  reason = None
  change = Change(metaline,page,iline,oldline,newline,reason)
  changes.append(change)
 print(len(changes),'potential changes found')
 return changes

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 ident = change.metaline
 if ident == None:
  ident = change.page
 outarr.append('; ' + ident)
 lnum = change.iline + 1
 outarr.append('%s old %s' % (lnum,change.old))
 outarr.append(';')
 outarr.append('%s new %s' % (lnum,change.new))
 outarr.append(';')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for ichange,change in enumerate(changes):
   outarr = change_out(change,ichange)
   for out in outarr:
    f.write(out+'\n')
 print(len(changes),"written to",fileout)


if __name__=="__main__":
 option  = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # change transactions
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes = init_changes(lines,option)
 write_changes(fileout,changes)

