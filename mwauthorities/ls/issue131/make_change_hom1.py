#-*- coding:utf-8 -*-
"""make_change_hom1.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,match,line1):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.match = match  
  self.line1 = line1
  
def init_cases_hom1(lines):
 regex1 = r'<h>[0-9][a-z]'
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
  m = re.search(regex1,line)
  if m == None:
   continue
  match = m.group(0)
  line1 = lines[iline+1]
  # generate a case
  cases.append(Case(metaline,iline,line,match,line1))

 print(len(cases),'changes of %s'%regex1)
 return cases

def write_cases_hom1(fileout,cases):
 n = 0
 nchg = 0
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' %(fileout,len(cases)))
 outarr.append('; <h>[0-9][a-z]')
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  outarr = []
  n = n + 1
  outarr.append(r'; -------------------------------------------------------')
  #metaline = re.sub(r'<k2>.*$','',case.metaline)
  #outarr.append('; %s' % metaline)
  outarr.append('; %s ' % case.match)
  iline = case.iline
  lnum = iline + 1
  line = case.line
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('%s new %s' %(lnum,line))
  outarr.append(';')
  iline1 = iline + 1
  lnum1 = iline1 + 1
  line1 = case.line1
  outarr.append('%s old %s' %(lnum1,line1))
  outarr.append('%s new %s' %(lnum1,line1))
  
  nchg = nchg + 1
  outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)


if __name__=="__main__":
 # Problem with input of regexes into command line
 # python make_change_regex.py ', </ls>' '</ls>, ' temp_mw_3.txt temp.txt
 # The 2nd paramenter '</ls>, ' is not intepreted properly
 # It prints as "<C:/Program Files/Git/ls>, "
 # Thus, use an option number

 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases_hom1(lines) 
 print(len(cases),'cases')
 write_cases_hom1(fileout,cases)
  
