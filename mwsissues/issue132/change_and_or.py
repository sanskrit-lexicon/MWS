#-*- coding:utf-8 -*-
"""change_and_or.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,match,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.match = match  
  self.newline = newline
  
def init_cases(lines,groupd):
 metaline = None
 imetaline = None
 page = None
 prevls = None
 ndata = 0 # number of lines between <L> and <LEND>
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  elif line.startswith('<L>'):
   metaline = line
   imetaline = iline
   continue
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   continue
  if metaline == None:
   continue # not in an entry
  if iline != (imetaline + 1):
   continue
  m = re.search(r'^<L>(.*?)<pc>',metaline)
  L = m.group(1)
  if L not in groupd:
   continue
  group = groupd[L]
  entry = group.entriesd[L] # gri
  entry.mwmetaline = metaline
  entry.mwheadline = line
  entry.imetaline = imetaline  

def write_groups_helper(group):
 outarr = []
 gtype = group.entries[0].gtype
 outarr.append('; %s words in "%s" group' %(len(group.entries),gtype))
 for entry in group.entries:
  meta = entry.mwmetaline
  meta = re.sub(r'<k2>.*$','',meta)
  outarr.append('; %s' % meta)
 # construct the info element to be appended to each headline
 infoparts = []
 for entry in group.entries:
  assert gtype == entry.gtype
  L = entry.L
  m = re.search(r'<k1>(.*?)<k2>',entry.mwmetaline)
  if m == None:
   print('write_groups_helper ERROR:',entry.mwmetaline)
   exit(1)
  k1 = m.group(1)
  infopart = '%s,%s' %(L,k1)
  infoparts.append(infopart)
 infostr = ';'.join(infoparts)
 info = '<info %s="%s"/>' %(gtype,infostr)
 # construct changes
 for entry in group.entries:
  L = entry.L
  outarr.append('; .......')
  iline = entry.imetaline+1
  lnum = iline + 1 # lnum of mwheadline
  old = entry.mwheadline
  new = '%s%s' %(old,info)  # append info
  outarr.append('%s old %s' %(lnum,old))
  outarr.append('%s new %s' %(lnum,new))
  if False and (L == "185441"): # dbg
   print("old=",old  + "\n")
   print("info=",info  + "\n")
   print("new=",new  + "\n")
 outarr.append('; ------------------------------------------------------')
 return outarr

def write_groups(fileout,groups):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' %(fileout,len(groups)))
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for group in groups:  
  outarr = write_groups_helper(group)
  outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(groups),'groups written to',fileout)

class GroupEntry:
 def __init__(self,L,metaline,headline,gtype):
  self.L = L
  self.metaline = metaline
  self.headline = headline
  self.gtype = gtype
  # next filled in later in init_cases
  self.mwmetaline = None
  self.imetaline = None
  self.mwheadline = None
class Group:
 d = {}
 def __init__(self,lines):
  entriesd = {}
  entries = []
  metaline = None
  for iline,line in enumerate(lines):
   if (iline % 2) == 0:
    # metaline
    metaline = line
    assert line.startswith('<L>')  # is it really a metaline
   else:
    headline = line
    if metaline == None:
     print('Group error')
     exit(1)
    m = re.search(r'<info ([^ ]*?)$',headline)
    gtype = m.group(1)
    m = re.search(r'^<L>(.*?)<pc>',metaline)
    L = m.group(1)
    entry = GroupEntry(L,metaline,headline,gtype)
    entriesd[L] = entry
    entries.append(entry)
    
  self.entries = entries
  self.entriesd = entriesd
  for entry in self.entries:
   L = entry.L
   if L in Group.d:
    print('Group duplicate L',L)
   Group.d[L] = self
  
def generate_groups(f):
 # entries 'split' by the line 'GROUP'
 grouplines = []
 igroup = 0
 for line in f:
  line = line.rstrip('\r\n')
  if line == '':
   pass
  elif line == '<LEND>':
   pass
  elif line == 'GROUP':
   igroup = igroup+1
   #print(igroup,"group",grouplines[0][0:10])
   yield Group(grouplines)
   # reinit for next group
   grouplines = []
  else:
   grouplines.append(line)
 if grouplines != []:
  igroup = igroup+1
  #print(igroup,"last group",grouplines[0][0:10])
  # last group
  yield Group(grouplines)
  
def init_groups(filein):
 with codecs.open(filein,"r","utf-8") as f:
  groups = list(generate_groups(f))
 print(len(groups),"groups from",filein)
 return groups

if __name__=="__main__":
 filegrp = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # possible change transactions
 groups = init_groups(filegrp)
 groupd = Group.d 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 init_cases(lines,groupd) # modifies groups
 write_groups(fileout,groups)
  
