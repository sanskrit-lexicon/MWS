#-*- coding:utf-8 -*-
"""make_change_3tab.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,newline,oldtext,newtext,note):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.newline = newline
  self.old = oldtext
  self.new = newtext
  self.note = note
  
class Orphan(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split('\t')
  assert len(parts) in [3,4]
  m = re.search(r'^ *\(([0-9]+)\): *$',parts[0])
  if m == None:
   print('Orphan format error\n',line,'"%s"' % parts[0])
   exit(1)
  self.lnum = int(m.group(1))
  self.old = parts[1]
  self.new = parts[2]
  if len(parts) == 4:
   self.note = parts[3]
  else:
   self.note = None
  self.nused = 0
  
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
  orec.nused = orec.nused + 1
  oldtext = orec.old
  newtext = orec.new
  newline = line.replace(oldtext,newtext)
  note = orec.note
  # generate a case
  cases.append(Case(metaline,iline,line,newline,oldtext,newtext,note))

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
  outarr.append('; %s' % case.old)
  outarr.append('; %s' % case.new)
  if case.note != None:
   outarr.append('; NOTE: %s' % case.note)
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
 write_cases(fileout,cases)
 # check all cases used
 nprob = 0
 for rec in orphans:
  if rec.nused != 1:
   print('problem',rec.lnum,rec.nused)
   nprob = nprob + 1
 print(nprob,'problems noted')
 
