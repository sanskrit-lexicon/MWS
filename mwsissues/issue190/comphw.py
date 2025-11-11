# coding=utf-8
""" comphw.py

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

def make_outarr(hwd):
 outarr = []
 for k1 in hwd:
  val = hwd[k1]
  olds = val['<']
  news = val['>']
  # out = f'{k1} : old:{len(olds)} new:{len(news)}'
  out = f'{k1} : old:{len(olds)} {olds}  new:{len(news)} {news}'
  outarr.append(out)
 return outarr
if __name__ == "__main__":
 filediff = sys.argv[1]  # diif_lost.txt
 fileout = sys.argv[2]
 lostlines = read_lines(filediff)
 hwd = init_hw(lostlines)
 outarr = make_outarr(hwd)
 write_lines(fileout,outarr)
 
