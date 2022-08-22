#-*- coding:utf-8 -*-
"""bbar1a.py 
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
  
def init_cases(lines):
 """ broken bar character
   should occur once in line following metaline
   should occur 0 times in other entry lines.
 """
 nmeta = 0  # number of metalines
 nhead = 0  # number of headlines
 n1 = 0  # number of headlines with exactly 1 broken bar
 n2 = 0  # number of headlines with > 1 broken bar
 n3 = 0  # number of headlines with 0 broken bar
 n4 = 0  # number of non-headlines with 1 or more broken bars 
 cases = []
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
  #elif line.startswith('[Page'):
  # page = line
  # continue
  if metaline == None:
   continue # not in an entry
  ndata = ndata + 1 
  nbbar = len(re.findall(r'¦',line))
  if imetaline == None:
   # unexpected
   print('init_cases error at line #',iline+1)
   print(line)
   exit(1)
  if iline == imetaline+1:
   # headline
   nhead = nhead + 1
   if nbbar == 1:
    n1 = n1 + 1
   elif nbbar > 1:
    n2 = n2 + 1
    case = Case(metaline,iline,line,'> 1 broken bar in headline')
    cases.append(case)
   elif nbbar == 0:
    n3 = n3 + 1
    case = Case(metaline,iline,line,'no broken bar in headline')
    cases.append(case)
  else:
   if nbbar != 0:
    n4 = n4 + 1
    case = Case(metaline,iline,line,'broken bar in non-headline')
    cases.append(case)

 print(nmeta,"metalines")
 print(nhead,"headlines")
 print(n1,"headlines with 1 ¦")
 print(n2,"headlines with > 1 ¦")
 print(n3,"headlines with 0 ¦")
 print(n4,"non-headlines with 1 or more ¦")
 return cases

def write_cases(fileout,cases):
 n = 0
 nchg = 0
 prevline = None
 previline = None
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
  previline = iline
  prevline = newline

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
 cases = init_cases(lines) 
 #print(len(cases),'cases')
 write_cases(fileout,cases)
  
