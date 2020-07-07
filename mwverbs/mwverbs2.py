#-*- coding:utf-8 -*-
"""mwverbs2.py
  
"""
from __future__ import print_function
import sys, re,codecs

class MWVerb(object):
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  self.k1,self.Lnums0,self.cat,self.cps0,self.parse = line.split(':')
  self.L = self.Lnums0.replace('&',',')
  self.cps = self.cps0.replace('P','a')
  self.cps = self.cps.replace('Ā','m')
  
def init_mwverbs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [MWVerb(x) for x in f]
 print(len(recs),"mwverbs read from",filein)
 #recs = [r for r in recs if r.cat in ['root','genuineroot']]
 #print(len(recs),"returned from mwverbs")
 return recs


def write(fileout,mwrecs):
 n = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in mwrecs:
   parts = [rec.k1,rec.L,rec.cat,rec.cps,rec.parse]
   out = ':'.join(parts)
   f.write(out + '\n')
   n = n + 1
 print(n,"records written to",fileout)


if __name__=="__main__": 
 filein = sys.argv[1] # mwverbs.txt
 fileout = sys.argv[2] # mwverbs1.txt
 mwrecs = init_mwverbs(filein)
 write(fileout,mwrecs)
