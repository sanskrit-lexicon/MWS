# coding=utf-8
""" 
k2_k1_diffs.py
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

def get_diffs_1(lines):
 ans = []
 for line in lines:
  if not line.startswith('<L>'):
   continue
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>(.*?)<',line)
  if m == None:
   print('metaline invalid format:\n%s' % line)
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  k2 = m.group(4)
  k1a = k2_to_k1(k2)
  if k1 == k1a:
   continue
  Lpc = '<L>%s<pc>%s' %(L,pc)  
  a = (Lpc,k1,k2,k1a)
  b = '\t'.join(a)
  ans.append(b)
 return ans

def get_diffs_2(lines):
 ans = []
 for line in lines:
  if not line.startswith('<L>'):
   continue
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>(.*?)<',line)
  if m == None:
   print('metaline invalid format:\n%s' % line)
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  k2 = m.group(4)
  k2s = k2.split(',')  # list of alternate k2s
  k2ok = True
  for k2a in k2s:
   k1a = k2_to_k1(k2a)
   if k1 != k1a:
    k2ok = False
  if k2ok:
   continue
  Lpc = '<L>%s<pc>%s' %(L,pc)  
  a = (Lpc,k1,k2,k1a)
  b = '\t'.join(a)
  ans.append(b)
 return ans

def get_diffs_3(lines):
 ans = []
 for line in lines:
  if not line.startswith('<L>'):
   continue
  # only difference from get_diffs_2
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>(.*?)<[eh]>',line)
  if m == None:
   print('metaline invalid format:\n%s' % line)
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  k2 = m.group(4)
  k2s = k2.split(',')  # list of alternate k2s
  k2ok = True
  for k2a in k2s:
   k1a = k2_to_k1(k2a)
   if k1 != k1a:
    k2ok = False
  if k2ok:
   continue
  Lpc = '<L>%s<pc>%s' %(L,pc)  
  a = (Lpc,k1,k2,k1a)
  b = '\t'.join(a)
  ans.append(b)
 return ans

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # e.g., mw.txt
 fileout = sys.argv[3] # text output
 # read all the entries of the dictionary.
 lines = read_lines(filein)
 print(len(lines),"read from",filein)
 if option == '1':
  diffs = get_diffs_1(lines)
 elif option == '2':
  diffs = get_diffs_2(lines)
 elif option == '3':
  diffs = get_diffs_3(lines)
 else:
  print('Unknown option:',option)
  exit(1)
 write_lines(fileout,diffs)
