#-*- coding:utf-8 -*-
"""make_change_hom2.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,metahom,headhom):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.metahom = metahom
  self.headhom = headhom
  
def init_cases_hom2(lines,option):
 assert option in ['num','letter']
 if option == 'num':
  metaregex = r'<h>([0-9])<'
  headregex = r'^<hom>([0-9])\.</hom>.*¦'
 elif option == 'letter':
  metaregex = r'<h>([a-z])<'
  #headregex = r'^<s>.*?</s> <hom>([a-z])</hom>.*¦'
  headregex = r'<hom>([a-z])</hom>.*¦'
 cases = []
 metaline = None
 imetaline1 = None
 page = None
 prevls = None
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if not line.startswith('<L>'):
   continue
  metaline = line
  headline = lines[iline+1] # line after metaline
  #
  metahom = None  # hom code in metaline
  headhom = None  # hom code in header
  m = re.search(metaregex,metaline)
  if m != None:
   metahom = m.group(1)
  m = re.search(headregex,headline)
  if m != None:
   headhom = m.group(1)
  if metahom == headhom:
   # consistency between metaline and headline
   continue
  # metaline and headline inconsistent.
  # for option=letter, exclude 'or' and 'and' cases
  if option == 'letter':
   if re.search(r'<info or="',headline):
    continue
   if re.search(r'<info and="',headline):
    continue
   
  # generate a case
  cases.append(Case(metaline,iline,headline,metahom,headhom))

 print(len(cases),'cases to examine')
 return cases

def write_cases_hom2(fileout,cases):
 n = 0
 nchg = 0
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' %(fileout,len(cases)))
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  outarr = []
  n = n + 1
  outarr.append(r'; -------------------------------------------------------')
  #metaline = re.sub(r'<k2>.*$','',case.metaline)
  #outarr.append('; %s' % metaline)
  outarr.append('; %s != %s ' % (case.metahom,case.headhom))
  iline = case.iline
  lnum = iline + 1
  line = case.metaline
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('%s new %s' %(lnum,line))
  outarr.append(';')
  # header line
  iline = case.iline + 1
  lnum = iline + 1
  line = case.line
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,line))

  nchg = nchg + 1
  outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)


if __name__=="__main__":
 option = sys.argv[1]
 assert option in ['num','letter']
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases_hom2(lines,option) 
 print(len(cases),'cases')
 write_cases_hom2(fileout,cases)
  
