#-*- coding:utf-8 -*-
"""change3a.py 
 
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

def change6(line):
 # Compar. exclude occcurrences in <ab>X</ab>,
 parts = re.split(r'(<ab>.*?</ab>)|(Compar[.])',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'Compar.':
   newpart = '<ab>Compar.</ab>'
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   

def change5(line):
 # Comm. exclude occcurrences in <ab>X</ab>,
 parts = re.split(r'(<ab>.*?</ab>)|(Comm[.])',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'Comm.':
   newpart = '<ab>Comm.</ab>'
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   

def change4(line):
 # Cf. exclude occcurrences in <ab>X</ab>,
 parts = re.split(r'(<ab>.*?</ab>)|(Cf[.])',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'Cf.':
   newpart = '<ab>Cf.</ab>'
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   

def change3(line):
 # Caus. exclude occcurrences in <ab>X</ab>,
 parts = re.split(r'(<ab>.*?</ab>)|(Caus[.])',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'Caus.':
   newpart = '<ab>Caus.</ab>'
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   


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

def newline_default(line):
 #changes = default_changes(base)
 #if base not in line:
 # return line
 changes = []
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
 
def init_changes(lines):
 changes = [] # array of Change objects
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
  newline = newline_default(line)
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
 #outarr.append('; ' + ident)
 lnum = change.iline + 1
 outarr.append('%s old %s' % (lnum,change.old))
 #outarr.append(';')
 #outarr.append('%s new %s' % (lnum,change.new))
 #outarr.append(';')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for ichange,change in enumerate(changes):
   outarr = change_out(change,ichange)
   for out in outarr:
    f.write(out+'\n')
 print(len(changes),"written to",fileout)


if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # change transactions
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes = init_changes(lines)
 write_changes(fileout,changes)

