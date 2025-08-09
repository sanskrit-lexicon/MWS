# coding=utf-8
""" dict_replace2.py
    revised from dict_replace.py to handle extra 'nparm' of lsfix2_ input
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

class REPL:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t')
  assert len(parts) == 5
  self.status = parts[0]
  self.nparm = int(parts[1])
  self.lnum = int(parts[2])
  self.old = parts[3]
  self.new = parts[4]
  
def repls_d(repls):
 d = {}
 for repl in repls:
  if repl.status != 'fixed':
   continue
  lnum = repl.lnum
  if lnum not in d:
   d[lnum] = []
  d[lnum].append(repl)
 lnums = d.keys()
 print(len(lnums),'lines to change')
 return d

def apply_repls(lines,replsd):
 newlines = []
 nchg = 0 # number of lines changed
 for iline,line in enumerate(lines):
  lnum = iline + 1
  if lnum not in replsd:
   newlines.append(line)
   continue
  repls = replsd[lnum]
  newline = line
  for repl in repls:
   newline = newline.replace(repl.old,repl.new)
  newlines.append(newline)
  assert newline != line
  nchg = nchg + 1
 print('apply_repls: %s lines changed' % nchg)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]  # kosha
 filein1 = sys.argv[2] # line string replacements
 fileout = sys.argv[3] # revised kosha
 lines = read_lines(filein)
 lines1 = read_lines(filein1,commentFlag=True)
 
 repls = [REPL(line) for line in lines1]
 d = repls_d(repls)  
 newlines = apply_repls(lines,d)
 write_lines(fileout,newlines)
 
