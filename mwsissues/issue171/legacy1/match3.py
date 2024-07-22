#-*- coding:utf-8 -*-
""" match3.py
"""
from __future__ import print_function
import sys,re,codecs,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import digentry
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

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

def make_k1dict(entries):
 d = {}
 for entry in entries:
  k1 = entry.metad['k1']
  if k1 not in d:
   d[k1] = [] # list of entries with given k1
  d[k1].append(entry)
 return d

def check_entries(entries,k1dict):
 probs = [] # no match 
 for entry in entries:  
  text = ' '.join(entry.datalines)
  k1 = entry.metad['k1']
  if k1 not in k1dict:
   probs.append(entry)
 return probs

def write_entries_helper(entry):
 outarr = []
 outarr.append(entry.metaline)
 for line in entry.datalines:
  outarr.append(line)
 outarr.append(entry.lend)
 return outarr

def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs) # ,blankflag=False)

def get_revsup(entry):
 # an mw entry
 text = ' '.join(entry.datalines)
 if '<info n="sup"' in text:
  return 'S'
 elif '<info n="rev"' in text:
  return 'R'
 else:
  return None
 
def get_mwsupentries(entries):
 ans = []
 for entry in entries:
  text = ' '.join(entry.datalines)
  if '<info n="sup"' in text:
   ans.append(entry)
  elif '<info n="rev"' in text:
   ans.append(entry)
 return ans

def get_supentries(entries):
 ans = []
 for entry in entries:
  text = ' '.join(entry.datalines)
  if '(in <ab>comp.</ab>' in text:
   continue
  else:
   ans.append(entry)
 return ans

def write_problems(problems):
 outarr = []
 for i,p in enumerate(problems):
  # p is an entry
  outarr.append('%02d %s' %(i+1,p.metaline))
 return outarr

def compare_dicts(mwdict,supdict):
 mwkeys = set(mwdict.keys())
 supkeys = set(supdict.keys())
 samekeys = (mwkeys == supkeys)
 print('mwkeys same as supkeys?:',samekeys)
 assert samekeys
 print('# of distinct sup keys=',len(mwkeys)) # same as len(supkeys)
 # keys with different number
 keys = mwkeys 
 for k1 in keys:
  mwnum = len(mwdict[k1])
  supnum = len(supdict[k1])
  if mwnum != supnum:
   print('%s #mw = %s, #sup = %s' %(k1,mwnum,supnum))


def write_entries_both_helper(mwsupentries,supentries):
 outarr = []
 for i,m in enumerate(mwsupentries):
  s = supentries[i]
  # i, m
  m_k1 = m.metad['k1'].ljust(15)
  s_k1 = s.metad['k1'].ljust(15)
  m_pc = m.metad['pc']
  s_pc = s.metad['pc']
  m_L = m.metad['L'].ljust(9)
  s_L = s.metad['L'].ljust(9)
  m_e = m.metad['e'].ljust(2)
  s_e = s.metad['e'].ljust(2)
  revsup = get_revsup(m)
  assert revsup in ['R','S']
  mwout = '%s %s %s %s %s' %(m_k1,m_L,m_e,revsup,m_pc)
  supout = '%s %s %s %s' %(s_k1,s_L,s_e,s_pc)
  mwout1 = mwout.ljust(40)
  out = '%s :: %s' %(mwout1,supout)
  outarr.append(out)
 return outarr

def write_entries_both(fileout,mwsupentries,supentries):
 outarr = write_entries_both_helper(mwsupentries,supentries)
 write_lines(fileout,outarr)


def write_entries_difflib_helper(mwsupentries,supentries):
 import difflib
 d = difflib.Differ()
 mw = [e.metad['k1'] for e in mwsupentries]
 sup = [e.metad['k1'] for e in supentries]

 mwtxt = '\n'.join(mw)
 suptxt = '\n'.join(sup)
 mwtxt1 = mwtxt.splitlines(keepends=True)
 suptxt1 = suptxt.splitlines(keepends=True)
 results = list(d.compare(mwtxt1,suptxt1))
 # results is list of strings.
 outarr = []
 for line in results:
  if line.startswith('?'):  # junk?
   pass
  else:
   outarr.append(line.rstrip('\r\n'))
 return outarr

def write_entries_difflib(fileout,mwsupentries,supentries):
 outarr = write_entries_difflib_helper(mwsupentries,supentries)
 write_lines(fileout,outarr)

def write_entries_3_helper(mwsupentries,supentries):
 a = write_entries_both_helper(mwsupentries,supentries)
 a1 = []
 a2 = []
 for x in a:
  x1,x2 = x.split('::')
  x1 = x1.strip()
  x2 = x2.strip()
  a1.append(x1)
  a2.append(x2)
 n = len(a1)
 assert n == len(a2)
 b = write_entries_difflib_helper(mwsupentries,supentries)
 i1 = -1
 i2 = -1
 c = []
 for i,x in enumerate(b):
  if x.startswith('  '):
   i1 = i1 + 1
   i2 = i2 + 1
   try:
    y1 = a1[i1]
    y2 = a2[i2]
    #y = a1[i1] + ' :: ' + a2[i2]
   except:
    y = 'write_entries_3_helper ERROR 1:"%s"' % x
    print(y)
    exit(1)
   #c.append(y)
  elif x.startswith('+ '):
   i2 = i2 + 1
   y1 = 'xxx'
   y2 = a2[i2]
   y = 'xxx ' + ' :: ' + a2[i2]
   #c.append(y)
  elif x.startswith('- '):
   i1 = i1 + 1
   if i1 < n:
    y1 = a1[i1]
    y2 = 'yyy'
    #y = a1[i1] + ' :: ' + 'yyy'
   else:
    y = 'write_entries_3_helper ERROR 2:"%s"' % x
    exit(1)
   #c.append(y)
  #elif x.startswith('?'):
  # # junk?
  # continue
  else:
   print('write_entries_3_helper ERROR 2: error at line %s:\n%s' % (i+1,x))
   exit(1)
  y = y1.ljust(40) + ' :: ' + y2
  c.append(y)
 return c
 
def write_entries_3(fileout,mwsupentries,supentries):
 outarr = write_entries_3_helper(mwsupentries,supentries)
 write_lines(fileout,outarr)
 
def test_difflib():
 import difflib
 d = difflib.Differ()
 mwlist = 'akabara,akabbara,akarizyat,akarRIya,akarmikA,akali,akalita,akalmaza,akalmAza,akalya,akavara,akasyavid,akAmasaMjYapana,akAyikA,akAla,akAlaka,akAlakOmudI,akAvaNka'

 suplist = 'akabara,akabbara,akavara,akarizyat,akarRIya,akarmikA,akali,akalita,akalmaza,akalmAza,akalya,akasyavid,akAmasaMjYapana,akAyikA,akAla,akAlakOmudI,akAlaka,akAvaNka'

 mw = mwlist.split(',')
 sup = suplist.split(',')

 mwtxt = '\n'.join(mw)
 suptxt = '\n'.join(sup)
 mwtxt1 = mwtxt.splitlines(keepends=True)
 suptxt1 = suptxt.splitlines(keepends=True)
 results = list(d.compare(mwtxt1,suptxt1))
 for line in results:
  print(line.rstrip('\r\n'))
 exit(1)

 
if __name__=="__main__":
 #test_difflib()
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[3] # add3c.txt
 fileout = sys.argv[4] # output summary
 entries = digentry.init(filein)
 mwsupentries = get_mwsupentries(entries)
 mwdict = make_k1dict(mwsupentries)
 Ldict = digentry.Entry.Ldict;
 #print(len(mwdict),'distinct supplement k1 from',filein)
 digentry.Entry.Ldict = {}
 entries = digentry.init(filein1)
 supentries = get_supentries(entries)
 
 supdict = make_k1dict(supentries)
 problems1 = check_entries(supentries,mwdict)
 print(len(problems1),' problems1')
 problems2 = check_entries(mwsupentries,supdict)
 print(len(problems2),' problems2')

 print(len(mwsupentries),"suprev entries in mw body")
 print(len(supentries),"suprev entries in mw supplement")
 assert len(mwsupentries) == len(supentries)
 #write_entries(fileout,problems1)
 outarr1 = write_problems(problems1)
 outarr2 = write_problems(problems2)
 outarr = outarr1 + outarr2
 #write_lines(fileout,outarr)
 #
 compare_dicts(mwdict,supdict)
 if option == '1':
  write_entries_both(fileout,mwsupentries,supentries)
 elif option == '2':
  write_entries_difflib(fileout,mwsupentries,supentries)
 elif option == '3':
  write_entries_3(fileout,mwsupentries,supentries)
 else:
  print('no output: unknown option')
 
