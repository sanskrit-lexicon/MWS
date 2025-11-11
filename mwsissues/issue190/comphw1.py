# coding=utf-8
""" comphw1.py

"""
from __future__ import print_function
import sys, re, codecs

def read_lines(filein,commentFlag=False):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines1 = [x.rstrip('\r\n') for x in f]
 if commentFlag:
  # remove 'comments' - lines start with ';'
  lines = [x for x in lines1 if not x.startswith(';')]
  print(len(lines),"kept.")
  print(len(lines1),'lines read from',filein)
 else:
  lines = lines1
  print(len(lines1),'lines read from',filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def init_hw(lines):
 hwd = {}
 for line in lines:
  m = re.search(r'^([<>]) <L>(.*?)<pc>(.*?)<k1>(.*?)<',line)
  if m == None:
   continue
  kind = m.group(1)
  L = m.group(2)
  pc = m.group(3)
  k1 = m.group(4)
  if k1 not in hwd:
   hwd[k1] = {'<':[], '>':[]}
  hwd[k1][kind].append(L)
 return hwd

def make_outarr(words):
 # put a word on each line
 # words is a set
 #words1 = sorted(words) # standard ascii sort
 words1 = sorted(words, key = lambda w: w.lower())
 outarr = []
 for w in words1:
  outarr.append(w)
 return outarr

def init_wordset(filein):
 lines = read_lines(filein)
 wordset = set()
 for line in lines:
  m = re.search(r'^<L>(.*?)<pc>(.*?)<k1>(.*?)<',line)
  if m == None:
   continue
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  wordset.add(k1)
 print(f'{filein} {len(wordset)} distinct headwords')
 return wordset

if __name__ == "__main__":
 file1 = sys.argv[1]
 file2 = sys.argv[2]
 fileout = sys.argv[3]
 words_1 = init_wordset(file1)
 words_2 = init_wordset(file2)
 words_diff = words_1.difference(words_2)
 outarr = make_outarr(words_diff)
 write_lines(fileout,outarr)
 
