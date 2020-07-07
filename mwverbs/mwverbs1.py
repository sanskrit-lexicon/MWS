#-*- coding:utf-8 -*-
"""mwverbs1.py
 
 
"""
from __future__ import print_function
import sys, re,codecs

class MWVerb(object):
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  self.k1,self.L,self.cat,self.cps,self.parse = line.split(':')
  if self.cat in ['root','genuineroot','nom']:
   self.cat1 = 'verb'
  elif self.cat in ['pre','gati']:
   self.cat1 = 'preverb'
  else: 
   print('MWVerb unexpected category',line)
  self.used = False

def init_mwverbs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [MWVerb(x) for x in f]
 print(len(recs),"mwverbs read from",filein)
 #recs = [r for r in recs if r.cat in ['root','genuineroot']]
 #print(len(recs),"returned from mwverbs")
 return recs

def merge_mwrecs(mwrecs):
 d = {}
 keys = []
 for mwverb in mwrecs:
  root = mwverb.k1
  if root not in d:
   d[root] = []
   keys.append(root)
  d[root].append(mwverb)

 recs = []
 for key in keys: 
  mwreclist = d[key]
  if len(mwreclist) == 1:
   recs.append(mwreclist)
   continue
  list1 = [mwrec for mwrec in mwreclist if mwrec.cat1 == 'verb']
  list2 = [mwrec for mwrec in mwreclist if mwrec.cat1 == 'preverb']
  if list1 != []:
   recs.append(list1)
  if list2 != []:
   recs.append(list2)
 print(len(recs),"distinct roots in mw")
 return recs

def check1a(mwreclist):
 cats = [r.cat1 for r in mwreclist]
 if len(set(cats)) != 1:
  mwrec = mwreclist[0]
  print('check1a:',mwrec.k1,cats)
  return
 cat1 = mwreclist[0].cat1
 parses = [r.parse for r in mwreclist]
 if cat1 == 'verb':
  if set(parses) != set(''):
   print('check1a - parses')
   for mwrec in mwreclist:
    print('  ',mwrec.line)

def check1a(mwreclist):
 cats = [r.cat1 for r in mwreclist]
 if len(set(cats)) != 1:
  mwrec = mwreclist[0]
  print('check1a:',mwrec.k1,cats)

def check1(mwreclists):
 for mwreclist in mwreclists:
  if len(mwreclist) == 1:
   continue
  check1a(mwreclist)

def write(fileout,mwreclists):
 n = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for mwreclist in mwreclists:
   mwrec0 = mwreclist[0]
   k1 = mwrec0.k1
   cat1 = mwrec0.cat1
   L = '&'.join([mwrec.L for mwrec in mwreclist])
   cps = ','.join([mwrec.cps for mwrec in mwreclist if mwrec.cps != ''])
   parses = [mwrec.parse for mwrec in mwreclist if mwrec.parse != '']
   parses_unique = []
   for p in parses:
    if p not in parses_unique:
     parses_unique.append(p)
   parse = ','.join(parses_unique)
   parts = [k1,L,cat1,cps,parse]
   out = ':'.join(parts)
   f.write(out + '\n')
   n = n + 1
 print(n,"records written to",fileout)


if __name__=="__main__": 
 filein = sys.argv[1] # mwverbs.txt
 fileout = sys.argv[2] # mwverbs1.txt
 mwrecs = init_mwverbs(filein)
 mwreclists = merge_mwrecs(mwrecs)
 check1(mwreclists)
 write(fileout,mwreclists)
