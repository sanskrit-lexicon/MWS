# coding=utf-8
""" 
unicode_test.py
"""
from __future__ import print_function
import sys, re,codecs
import unicodedata

def make_outarr(line):
 outarr = []
 outarr.append(line)
 if line.startswith(';'):
  return outarr
 for c in line:
  name = unicodedata.name(c)
  ic = ord(c)
  out = '     %s %04x %s' %(c,ic,name)
  outarr.append(out)
 return outarr

def write(fileout,lines):
 outrecs = []
 for line in lines:
  outarr = make_outarr(line)                    
  outrecs.append(outarr)   
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)


   
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt
 fileout = sys.argv[2] #
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 write(fileout,lines)
 
