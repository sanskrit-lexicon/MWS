#-*- coding:utf-8 -*-
"""make_change_regex.py 
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
  
def init_cases(lines,regex):
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
  elif line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   #continue
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  m = re.search(regex,line)
  if m != None:
   # generate a case
   match = m.group(0)
   cases.append(Case(metaline,iline,line,match))

 print(len(cases),'instances of %s'%regex)
 return cases

def write_cases_regex(fileout,cases,regex):
 n = 0
 nchg = 0
 prevline = None
 previline = None
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
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  outarr.append('; %s' % metaline)
  outarr.append('; %s ' % case.match)
  iline = case.iline
  lnum = iline + 1
  line = case.line
  if previline == iline:
   # in case we change same line more than once
   line = prevline
  outarr.append('%s old %s' %(lnum,line))
  matchmark = '***** %s *****' %case.match
  newline = line.replace(case.match,matchmark)
  nchg = nchg + 1
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)
  previline = iline
  prevline = newline

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)

if __name__=="__main__":
 regex = sys.argv[1]  # search for record matching regex
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases(lines,regex) 
 print(len(cases),'cases')
 write_cases_regex(fileout,cases,regex)
  
