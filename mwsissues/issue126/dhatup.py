#-*- coding:utf-8 -*-
"""dhatup.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,dhatups):
  self.metaline = metaline
  self.dhatups = dhatups
  
def init_cases(lines):
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
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  instances = []
  for m in re.finditer(r'<ls>(Dhāt.*?)</ls>',line):
   instances.append(m.group(1))
  for m in re.finditer(r'<ls n="(Dhāt.*?)">(.*?)</ls>',line):
   instances.append(m.group(1) + ' ' + m.group(2))
  if instances != []:
   # generate a case
   cases.append(Case(metaline,instances))

 print(len(cases),"dhatupada cases")
 return cases

def write_cases(fileout,cases):
 n = 0
 outrecs = []
 nprob = 0
 for case in cases:
  outarr = []
  n = n + 1
  #outarr.append(r'; -------------------------------------------------------')
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  #outarr.append('; %s' % metaline)
  for x in case.dhatups:
   if re.search(r'^Dhāt[up]*\. [ixv]+, [0-9]+\.?$',x):
    y = x
   elif re.search(r'^Dhāt[up]*\.$',x):
    y = x
   elif re.search(r'^Dhāt[up]*\. [ixv]+, [0-9]+\.? f\.$',x):
    y = x
   else:
    y = x + ' ?'
    nprob = nprob + 1
   out = '%s : %s' %(metaline,y)
   outarr.append(out)
  outrecs.append(outarr)
 print(nprob,"cases with non-standard form")
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
  
