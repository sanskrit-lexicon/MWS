# coding=utf-8
""" ad_markplus
"""
from __future__ import print_function
import sys, re,codecs

def write(fileout,adrecs):
 outrecs = []
 # title
 outarr = []
 outarr.append('; **********************************************************')
 outarr.append('; %s' % fileout)
 outarr.append('; **********************************************************')
 outrecs.append(outarr)
 for adrec in adrecs:
  k1 = adrec.k1
  k2 = adrec.k2
  k2pwg = adrec.k2pwg
  pc = adrec.pc
  k1a = k1.ljust(10)
  k2a = k2.ljust(15)
  k2pwga = k2pwg.ljust(15)
  status = adrec.newstatus
  a = [status,k1a,k2a,k2pwga,pc]
  out = '\t'.join(a)
  outarr = [out]
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 nout = len(adrecs)
 print("%s records written to %s" %(nout,fileout))

class ADrec:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  self.status,self.k1,self.k2,self.k2pwg,self.pc = line.split('\t')
  self.type = self.status.strip()
  if self.type not in ['+','x','_']:
   print('ADrec: unknown status')
   print(line)
   exit(1)
  self.k1 = self.k1.strip()
  self.k2 = self.k2.strip()
  self.k2pwg = self.k2pwg.strip()
  
def init_ad(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [ADrec(x) for x in f if not x.startswith(';')]
 print(len(recs),"accent difference records read from",filein)
 return recs

def adrecs_update_status(recs,prevplus):
 d = {}
 for adrec in prevplus:
  k1 = adrec.k1
  if k1 in d:
   print('adrecs_update_status: unexpected duplicate k1=',k1)
  d[k1] = adrec
 for adrec in recs:
  k1 = adrec.k1
  if k1 not in d:
   print('k1 not in previous',k1)
   adrec.newstatus = adrec.status
  else:
   adrec.newstatus = '+' 
  
if __name__=="__main__":
 filein1 = sys.argv[1] # ad3_rev.txt
 filein2 = sys.argv[2] # temp_ad3b_rev.txt
 fileout = sys.argv[3] # ad3_rev3b.txt
 
 adrecs = init_ad(filein1)
 adrecs1 = [r for r in adrecs if r.type == '+']

 adrecs3b = init_ad(filein2)
 # add 'newstatus' attribute to adrecs3b
 adrecs_update_status(adrecs3b,adrecs1)
 write(fileout,adrecs3b)
