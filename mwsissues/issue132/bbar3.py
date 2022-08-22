#-*- coding:utf-8 -*-
"""bbar3.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,imetaline,headline,iline,line):
  self.metaline = metaline
  self.imetaline = imetaline
  self.headline = headline # imetaline+1
  self.iline = iline  # non-headline with <info and/or="X"/>
  self.line = line
  
def init_cases(lines):
 cases = []
 metaline = None
 imetaline = None
 for iline,line in enumerate(lines):
  #if iline == 0: 
  # continue  # 
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
  if iline == (imetaline + 1):
   iheadline = iline
   headline = line
   continue
  # in entry, not the metaline, not the headline
  # if this line specifies and or/and group, then generate a case
  if re.search(r'<info (or|and)="',line):
   case = Case(metaline,imetaline,headline,iline,line)
   cases.append(case)
 return cases
  
def write_cases_helper(case):
 outarr = []
 meta = case.metaline
 meta = re.sub(r'<k2>.*$','',meta)
 outarr.append('; %s' % meta)
 #
 ilinehead = case.imetaline+1
 oldheadline = case.headline
 iline = case.iline
 oldline  = case.line
 m = re.search(r'<info (or|and)=".*?"/>',oldline)
 info = m.group(0)
 #
 newheadline = oldheadline + info
 newline = oldline.replace(info,'')
 # change to headline
 lnum = ilinehead + 1
 old = oldheadline
 new = newheadline
 outarr.append('%s old %s' %(lnum,old))
 outarr.append(';')
 outarr.append('%s new %s' %(lnum,new))
 outarr.append('; ....................')
 # change to line
 lnum = iline + 1
 old = oldline
 new = newline
 outarr.append('%s old %s' %(lnum,old))
 outarr.append(';')
 outarr.append('%s new %s' %(lnum,new))
 outarr.append('; ------------------------------------------------------')
 return outarr

def write_cases(fileout,cases):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s' % fileout)
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  outarr = write_cases_helper(case)
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
 #print(len(cases),"cases found")
 write_cases(fileout,cases)
  
