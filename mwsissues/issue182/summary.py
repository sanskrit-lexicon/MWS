# coding=utf-8
""" summary.py for 'BhP.' 
"""
from __future__ import print_function
import sys, re,codecs
import digentry  
from roman_int import roman_to_int,int_to_Roman

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines_simple(fileout,outarr,printFlag=True):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    #if out == None:
    # out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

def write_recs_1_standard(fileout,recs):
 # recs is list of Inrec objects
 outarr = []
 for rec in recs:
  if rec.status != 'STANDARD':
   continue
  ireg = rec.ireg
  m = rec.m
  if ireg == 0:
   parms = (0,0,0)
  else:
   parms = (rec.d1,rec.d2,rec.d3)
  parmstr = '(%s,%s,%s)' % parms
  rec1 = (rec.L,rec.k1,rec.lnum,rec.ls,parmstr)
  out = '\t'.join(rec1)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_recs_1_nonstandard(fileout,recs):
 # recs is list of Inrec objects
 outarr = []
 for rec in recs:
  if rec.status != 'TODO':
   continue
  rec1 = (rec.L,rec.k1,rec.lnum,rec.ls)
  out = '\t'.join(rec1)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_recs_2(fileout,recs):
 # recs is list of Inrec objects
 outarr = []
 recs1 = [rec for rec in recs if rec.status == 'STANDARD']
 # establish
 d = {}
 for rec in recs1:
  ireg = rec.ireg
  if ireg == 0:
   key = (0,0,0)
  else:
   key = (roman_to_int(rec.d1.upper()),rec.d2,rec.d3)
  if key not in d:
   d[key] = []
  d[key].append(rec)
 keys = d.keys()
 keys1 = sorted(keys)
 for key in keys1:
  n = len(d[key])
  (d1int,d2,d3) = key
  d1up = int_to_Roman(d1int)
  d1lo = d1up.lower()
  key1 = (d1lo,d2,d3)
  parmstr = '(%s,%s,%s)' % key1
  out = '%s\t%s' %(parmstr,n)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)


def check_standarda(ls,sregs):
 used = []
 for ireg,sreg in enumerate(sregs):
  m = re.search(sreg,ls)
  if m:
   used.append((m,ireg))
 flag = (len(used) == 1)
 if flag:
  m,ireg = used[0]
 else:
  m,ireg = None,-1
 return flag,m,ireg

def get_all_regexes(X):
 regexraws = [
  r'<ls>%s.*?</ls>' % X,
  r'<ls n="%s.*?</ls>' % X
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def findall_ls_entries(entries,regexes):
 nregex = len(regexes)
 recs = []
 counts = {}
 for i in range(nregex):
  counts[i] = 0
 dups = [] # lines with duplicate ls
 dupok = '<ls>%s</ls>' % X1  # BhP.
 print('dupok = ',dupok)

 for ientry,entry in enumerate(entries):
  #text = ' '.join(entry.datalines)
  L = entry.metad['L'] # the entry id
  k1 = entry.metad['k1'] # the entry id
  linenum1 = entry.linenum1
  for idx,line in enumerate(entry.datalines):
   lnum = linenum1 + idx + 1
   d = {}
   vals = []
   dupflag = False
   counts_line = {}
   for iregex,regex in enumerate(regexes):
    a = re.findall(regex,line)
    for x in a:
     val = (L,k1,lnum,x)
     vals.append(val)
     if iregex not in counts_line:
      counts_line[iregex] = 0
     counts_line[iregex] = counts_line[iregex] + 1
     if (val in d) and (x != dupok):
      dupflag = True
      if True: # debug
       print('val=%s, x = %s, d[val]=%s' % (val,x,d[val]))
       exit(1)
      break
     d[val] = True
    if dupflag:
     dups.append((lnum,val))
     continue
   for val in vals:
    (L,k1,lnum,x) = val
    rec = Inrec(L,k1,str(lnum),x)
    recs.append(rec)
   for iregex in counts_line:
    counts[iregex] = counts[iregex] + counts_line[iregex]
 print('%s instances of ls' % len(recs))
 print('findall_ls_entries: number of lines with duplicates=',len(dups))
 for dup in dups:
  lnum,val = dup
  (L,k1,lnum1,x) = val
  assert lnum == lnum1
  print('duplicate: L=%s, k1=%s, lnum=%s, ls=%s' %(L,k1,lnum,x))
 return recs,counts 

def get_standard_regexes(X):
 d1 = "([ivx]+)"  # peculiar to MW
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional f. OR optional ff.
 #Y = "(\.| f\.| ff\.|\. f\.|\. ff\.)?"
 # MW may omit the period before f, ff
 Y = "(\.| f\.| ff\.|\. f\.|\. ff\.| f\.| ff\.)?"
 regexraws = [
  r'<ls>%s</ls>' % X,
  r'<ls>%s %s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s</ls>' %(X,d1,d2,d3,Y),
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

class Inrec:
 def __init__(self,L,k1,lnum,ls):
  #self.line = line
  #parts = line.split('\t')
  #self.parts = parts
  self.L = L
  self.k1 = k1
  self.lnum = lnum # string,
  self.ilnum = int(self.lnum)
  self.ls = ls
  self.status = 'TODO'
  self.m = None
  self.ireg = None
  self.d1 = None
  self.d2 = None
  self.d3 = None

def classify(allrecs):
 sregs, sregraws = get_standard_regexes(X)
 for irec,rec in enumerate(allrecs):
  flag,m,ireg = check_standarda(rec.ls,sregs)
  if not flag:
   assert rec.status == 'TODO'
   continue
  # rec is standard
  rec.status = 'STANDARD'
  rec.m = m
  rec.ireg = ireg
  if ireg != 0:
   #rec.d1 = int(m.group(1))
   rec.d1 = m.group(1)
   rec.d2 = int(m.group(2))
   rec.d3 = int(m.group(3))

if __name__ == "__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # pwg.txt
 X = r'BhP\.' # global variable
 X1 = 'BhP.'  # global variable
 entries = digentry.init(filein)
 allregs,allregsraw = get_all_regexes(X)
 # allrecs is list of Inrec objects
 allrecs,allcounts = findall_ls_entries(entries,allregs)
 classify(allrecs)
 if option == '1':
  fileout = sys.argv[3]
  fileout1 = sys.argv[4]
  write_recs_1_standard(fileout,allrecs)
  write_recs_1_nonstandard(fileout1,allrecs)
 elif option == '2':
  fileout = sys.argv[3]
  write_recs_2(fileout,allrecs)
 else:
  print('unknown option',option)

