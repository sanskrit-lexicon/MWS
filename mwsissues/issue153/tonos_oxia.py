# coding=utf-8
""" 
tonos_oxia.py
"""
from __future__ import print_function
import sys, re,codecs
import unicodedata

def write(fileout,d):
 keys = d.keys()
 keys = sorted(keys)
 outarr = []
 outarr.append('; Greek characters in mw.txt with tonos or oxia accent')
 for c in keys:
  ic = ord(c)
  name = unicodedata.name(c)
  out = '%s %s %04x %s' %(d[c],c,ic,name)
  outarr.append(out)
 
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')
 print(len(outarr),"records written to",fileout)

def count_tonos_oxia(lines):
 d = {}
 for line in lines:
  for m in re.finditer(r'<lang n="greek">(.*?)</lang>',line):
   text = m.group(1)
   for c in line:
    name = unicodedata.name(c)
    name = name.lower()
    if ('tonos' in name) or ('oxia' in name):
     if c not in d:
      d[c] = 0
     d[c] = d[c] + 1
 return d     
   
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt
 fileout = sys.argv[2] #
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 d = count_tonos_oxia(lines)
 write(fileout,d)
 
