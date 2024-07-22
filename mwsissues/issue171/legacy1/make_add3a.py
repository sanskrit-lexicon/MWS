# coding=utf-8
""" make_add3a.py
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

class EntryX:
 def __init__(self,line):
  m = re.search(r'^<H([1-4][ABC]?)><h>(.*?)</h><body>(.*?)</body><tail>(.*?)</tail></H\1>$',line)
  if m == None:
   self.status = False
  else:
   self.status = True
  if not self.status:
   return
  self.e = m.group(1)
  self.h = m.group(2)
  self.body = m.group(3)
  self.tail = m.group(4)
  # parse head
  m = re.search(r'^<hc3>.*?</hc3><key1>(.*?)</key1><hc1>1</hc1><key2>(.*?)</key2>$',self.h)
  if m == None:
   self.status = False
   return
  self.k1 = m.group(1)
  self.k2 = m.group(2)
  # parse tail
  m = re.search(r'^<pc>(.*?)</pc><L>(.*?)</L>$',self.tail)
  if m == None:
   self.status = False
   return
  self.pc = m.group(1)
  self.L = m.group(2)

def write_problems(notlines):
 fileout = 'temp_make_add3a_prob.txt'
 write_lines(fileout,notlines)
 exit(1)

def make_entries(lines):
 entries = []
 nnot = 0  # number of non-standard lines
 notlines = []
 for line in lines:
  rec = EntryX(line)
  if not rec.status:
   nnot = nnot + 1
   notlines.append(line)
   continue
  entries.append(rec)
 print(nnot,"non-standard lines")
 if nnot != 4:
  write_problems(notlines)
 return entries

def write_entries_helper(rec):
 outarr = []
 # metaline
 metaline = '<L>%s<pc>%s<k1>%s<k2>%s<e>%s' % (
              rec.L,rec.pc,rec.k1,rec.k2,rec.e)
 outarr.append(metaline)
 outarr.append(rec.body)
 outarr.append('<LEND>')
 return outarr

def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
 #
 write_recs(fileout,outrecs)
 
if __name__=="__main__":
 filein = sys.argv[1]  # mw.txt
 fileout = sys.argv[2]  # change file 
 lines = read_lines(filein)
 entries = make_entries(lines)
 write_entries(fileout,entries)
 
 
