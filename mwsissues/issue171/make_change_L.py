# coding=utf-8
""" make_change_L.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

class Change:
 def __init__(self,metaline,lnum,newmeta):
  self.metaline = metaline
  self.lnum = lnum
  self.newmeta = newmeta
  
def write_changes(fileout,changes):
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s changes' % (len(changes),))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in changes:
  outarr = []
#  outarr.append('; %s' % c.metaline)
#  outarr.append('; old: %s' % c.metaline)
#  outarr.append('; new: %s' % c.new)
  lnum = int(c.lnum)
  # change 
  outarr.append('%s old %s' %(lnum,c.metaline))
  outarr.append('%s new %s' %(lnum,c.newmeta))
  outarr.append(';')
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)

def make_dict(linesL,globald):
 d = {}
 for line in linesL:
  Lold,Lnew = line.split()
  ## check form
  m = re.search(r'^[0-9.]+$',Lold)
  if m == None:
   print('make_dict ERROR Lold',Lold)
   exit(1)
  m = re.search(r'^[0-9.]+$',Lnew)
  if m == None:
   print('make_dict ERROR Lnew',Lnew)
   exit(1)
  # check no duplicates in Lold
  if Lold in d:
   print('make_dict ERROR Duplicate Lold',Lold)
   exit(1)
  # check that Lold is in globald and Lnew is NOT in globald
  if Lold not in globald:
   print('make_dict ERROR Lold not in global dict',Lold,Lnew)
   exit(1)
  if Lnew in globald:
   print('make_dict ERROR Lnew is in global dict',Lold,Lnew)
   exit(1)
  # update d
  d[Lold] = Lnew
 # check that no Lnew is in d. This could complicate things
 for Lold in d:
  Lnew = d[Lold]
  if Lnew in d:
   print('make_dict ERROR: Lnew found in d: Lold, Lnew = ',Lold,Lnew)
   exit(1)
 return d

def make_global_dict(lines):
 d = {}
 for iline,line in enumerate(lines):
  m = re.search(r'<L>(.*?)<',line)
  if m == None:
   continue
  # metaline
  L = m.group(1)
  # check for dups
  if L in d:
   print('make_global_dict: Duplicate L=',L)
   exit(1)
  d[L] = L  # metaline
 return d

def make_changes(lines,linesL):
 dglobaldict = make_global_dict(lines)
 # Each line of linesL has form 'LOLD LNEW'
 # construct a dictionary d[LOLD] = LNEW
 d = make_dict(linesL,dglobaldict)
 changes = []
 metaline = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
  if line.startswith('<LEND>'):
   metaline = None
   continue
  if metaline == None:
   continue
  m = re.search(r'<L>(.*?)<',metaline)
  assert m != None
  L = m.group(1)
  if L not in d:
   continue
  # construct Change object
  Lnew = d[L]
  xold = m.group(0)  # <L>X<'
  xnew = '<L>%s<' % Lnew
  newmeta = metaline.replace(xold,xnew)
  lnum = iline + 1
  change = Change(metaline,lnum,newmeta)
  changes.append(change)
  # reset metaline to None, so only one change per entry
  metaline = None
 print(len(changes),"changes")
 return changes

if __name__=="__main__":
 filein = sys.argv[1]  # mw.txt
 filein1 = sys.argv[2] # Lold Lnew
 fileout = sys.argv[3]  # change file 
 lines = read_lines(filein)
 lines1 = read_lines(filein1)
 changes = make_changes(lines,lines1)
 write_changes(fileout,changes)
 

