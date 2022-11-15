# coding=utf-8
""" 
hwcount.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry


def init_k1dict(entries):
 d = {}
 for entry in entries:
  k1 = entry.metad['k1']
  if k1 not in d:
   d[k1] = []
  d[k1].append(entry)
 return d


if __name__=="__main__":
 filein = sys.argv[1] # e.g., mw.txt
 # read all the entries of the dictionary.
 entries = digentry.init(filein)
 # get k1 dictionary for entries
 k1dict = init_k1dict(entries)
 # count the number of keys in k1dict
 numkeys = len(k1dict.keys())
 print(numkeys,"distinct k1 headwords in",filein)
