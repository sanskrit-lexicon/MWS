# coding=utf-8
""" 
make_change.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def k2_to_k1(k2):
 # Is this complete?
 k1 = re.sub(r'[^aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|~]','',k2)
 return k1

class Change:
 def __init__(self,iline,metaline,info):
  self.iline = iline
  self.metaline = metaline
  self.info = info #
  
def make_changes(infos,Ldict):
 changes = []
 for info in infos:
  parts = info.split('\t')
  Lpc,k1,k2,k1a = parts
  m = re.search(r'<L>(.*?)<pc>.*?$',Lpc)
  if m == None:
   print('make_changes problem 1:%s',info)
   exit(1)
  L = m.group(1)
  if L not in Ldict:
   print('make_changes problem 2:%s',info)
   exit(1)
  iline,metaline = Ldict[L]
  change = Change(iline,metaline,info)
  changes.append(change)
 return changes

def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  iline,metaline,info = change.iline,change.metaline,change.info
  outarr = []
  lnum = iline + 1
  outarr.append('%s old %s' %(lnum,metaline))
  outarr.append('; info: %s' % info)
  outarr.append('%s new %s' %(lnum,metaline))
  outarr.append('; ---------------------------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)
  
def make_Ldict(lines):
 d = {}
 for iline,line in enumerate(lines):
  if not line.startswith('<L>'):
   continue
  m = re.search(r'<L>(.*?)<pc>',line)
  L = m.group(1)
  assert L not in d
  d[L] = (iline,line)
 return d

if __name__=="__main__":
 filein = sys.argv[1] # e.g., mw.txt
 filein1 = sys.argv[2] # one of the 'diffs_' files
 fileout = sys.argv[3] # text output
 # read all the entries of the dictionary.
 lines = read_lines(filein)
 print(len(lines),"read from",filein)
 lines1 = read_lines(filein1)
 Ldict = make_Ldict(lines)

 changes = make_changes(lines1,Ldict)
 write_changes(fileout,changes)

