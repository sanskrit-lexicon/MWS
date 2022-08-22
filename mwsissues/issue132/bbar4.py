#-*- coding:utf-8 -*-
"""bbar4.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,match):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.match = match  
  #self.newline = newline

class Rec:
 def __init__(self,imetaline,metaline,line,info):
  self.imetaline = imetaline
  self.metaline = metaline
  self.line = line
  self.info = info
  infoLs = []
  infok1s = []
  infoparts = info.split(';')
  for infopart in infoparts:
   try:
    infoL,infok1 = infopart.split(',')
   except:
    print('Rec error info parse:',metaline)
    continue
   infoLs.append(infoL)
   infok1s.append(infok1)
  self.infoLs = infoLs
  self.infok1s = infok1s
  self.infoparts = infoparts
  
  
def init_cases(lines):
 """ broken bar character
   should occur once in line following metaline
   should occur 0 times in other entry lines.
 """
 nmeta = 0  # number of metalines
 nhead = 0  # number of headlines
 cases = []
 metaline = None
 imetaline = None
 # -----------------------------------------
 # initialize dictionary.
 # key is L, value is a Rec object.
 # L values are keys when the headline contains an <info or/and="X"/> item.
 # -----------------------------------------
 d = {} 
 for iline,line in enumerate(lines):
  line = line.rstrip('\r\n')
  if line == '':
   continue
  elif line.startswith('<L>'):
   metaline = line
   imetaline = iline
   nmeta = nmeta+1
   ndata = 0
   continue
  elif line == '<LEND>':
   if ndata == 0:
    print('empty entry:',metaline)
   metaline = None
   imetaline = None
   ndata = None
   continue
  if metaline == None:
   continue # not in an entry
  ndata = ndata + 1 
  if imetaline == None:
   # unexpected
   print('init_cases error at line #',iline+1)
   print(line)
   exit(1)
  m = re.search(r'<info (or|and)="(.*?)"/>',line)
  if iline != imetaline+1:
   # headline is the line after metaline
   # assume <info or/and> markup occurs ONLY in headline
   if m != None:
    print('Error at line# %s: unexpected info or/ans' % (iline+1,))
   continue
  if m == None:
   continue
  info = m.group(2)
  m = re.search(r'<L>(.*?)<pc>',metaline)
  L = m.group(1)
  if L in d:
   # should not happen!
   print('init_cases Error multiple info',metaline)
   rec1 = d[L]
   print('rec1 = %s' %(rec1.metaline))
   exit(1)
   continue
  d[L] = Rec(imetaline,metaline,line,info)
 # -----------------------------------------
 # Now, use d to search for inconsistencies
 # -----------------------------------------
 for L0 in d:
  rec0 = d[L0]
  info0 = rec0.info
  for L1 in rec0.infoLs:
   if L1 not in d:
    match = 'Error 1: L0=%s, L1=%s' %(L0,L1)
    imetaline = rec0.imetaline;
    metaline = rec0.metaline
    iline = imetaline+1
    line = rec0.line
    case = Case(metaline,iline,line,match)
    cases.append(case)
    continue
   rec1 = d[L1]
   info1 = rec1.info
   if info0 != info1:
    imetaline = rec1.imetaline;
    metaline = rec1.metaline
    iline = imetaline+1
    line = rec1.line
    match = 'Error 2: L0=%s, L1=%s' %(L0,L1)
    case = Case(metaline,iline,line,match)
    cases.append(case)
    continue
    
 return cases

def write_cases(fileout,cases):
 n = 0
 nchg = 0
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s ' %fileout)
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  outarr = []
  n = n + 1
  outarr.append(r'; -------------------------------------------------------')
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  outarr.append('; %s' % metaline)
  outarr.append('; %s ' % case.match)
  iline = case.iline
  lnum = iline + 1
  line = case.line
  outarr.append('%s old %s' %(lnum,line))
  newline = line  # change to be manual
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)



if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases(lines) 
 print(len(cases),'cases')
 write_cases(fileout,cases)
  
