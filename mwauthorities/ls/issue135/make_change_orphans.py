#-*- coding:utf-8 -*-
"""make_change_orphans.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,newline,comment):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.newline = newline
  self.comment = comment

class Orphan(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  m = re.search(r'^ *\(([0-9]+)\): +(.*)$',line)
  if m == None:
   print('Orphan format error\n',line)
   exit(1)
  self.lnum = int(m.group(1))
  self.text = m.group(2)

def init_orphans(filein):
 d = {}
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   rec = Orphan(line)
   n = rec.lnum
   if n in d:
    print('init_orphans: duplicate lnum',n)
   d[n] = rec
   recs.append(rec)
 print(len(recs),'records read from',filein)   
 return recs,d
def compute_newpart(part,changedata):
 for idata,data in enumerate(changedata):
  old,new = data
  newpart = part.replace(old,new)
  if newpart != part:
   return newpart,idata  # apply first change 
 return part,-1 # no changes apply

def compute_newline(line,changedata):
 parts = re.split(r'(<ls[^<]*</ls>)',line)
 newparts = []
 idxnew = -1
 for part in parts:
  if part.startswith('<ls'):
   newpart,idx = compute_newpart(part,changedata)
   if idx != -1:
    # part was changed
    if False: # dbg
     change = changedata[idx]
     print(change)
    if idxnew != -1:
     # hard to handle multiple changes in a line
     print('compute_newline multiple:',line)
    idxnew = idx
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline,idxnew

def init_cases(lines,orphand):
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
   continue 
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  lnum = iline+1
  if lnum not in orphand:
   continue
  orec = orphand[lnum]
  text = orec.text
  if text in line:
   newline = line.replace(text,'**'+text)
   comment = ' ' + text
  else:
   newline = line
   comment = '?? ' + text
  # generate a case
  cases.append(Case(metaline,iline,line,newline,comment))

 print(len(cases),'found in init_cases')
 return cases

def write_cases(fileout,cases):
 n = 0
 nchg = 0
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' % (fileout,len(cases)))
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  outarr = []
  n = n + 1
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  outarr.append('; %s' % metaline)
  outarr.append('; %s' % case.comment)
  iline = case.iline
  lnum = iline + 1
  line = case.line
  newline = case.newline
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append(r'; -------------------------------------------------------')
  outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'changes written to',fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2]
 fileout = sys.argv[3] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 orphans,orphand = init_orphans(filein1)

 cases = init_cases(lines,orphand) 
 #print(len(cases),'cases')
 write_cases(fileout,cases)
  
