# -*- coding: utf-8 -*-
"""ad_cpd_non.py
"""
import codecs, re, sys
from collections import defaultdict

class ADrec:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  self.status,self.k1,self.k2,self.k2pwg,self.pc = line.split('\t')
  self.type = self.status.strip()
  if not self.type.startswith('+'):
   print('ADrec: unknown status')
   print(line)
   exit(1)
  else:
   self.type = '+'
  self.k1 = self.k1.strip()
  self.k2 = self.k2.strip()
  self.k2pwg = self.k2pwg.strip()
  

def write(fileout,lines1,lines2):
 fout = codecs.open(fileout, 'w', 'utf-8')
 n = 0
 for line in lines1:
  fout.write(line+'\n')
  n = n + 1
 for line in lines2:
  fout.write(line+'\n')
  n = n + 1
 fout.close()
 print(n,"lines written to",fileout)

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"read from",filein)
 return lines

def adjust1(lines):
 ans = []
 for line in lines:
  if line.startswith(';'):
   ans.append(line)
  else:
   newline = '+\t'+line
   ans.append(newline)
 return ans

def adjust2(lines):
 ans = []
 for line in lines:
  if line.startswith(';'):
   ans.append(line)
  else:
   # replace initial '++' with '+'
   newline = re.sub(r'^[+]+','+',line)  
   ans.append(newline)
 return ans

def check(lines):
 nprob = 0
 for line in lines:
  if not line.startswith(';'):
   rec = ADrec(line)  # program will exit if not valid ADrec object
 
if __name__ == "__main__":
 filein1 = sys.argv[1]
 filein2 = sys.argv[2]
 fileout = sys.argv[3]

 lines1 = read_lines(filein1)
 lines2 = read_lines(filein2)
 lines1a = adjust1(lines1)
 lines2a = adjust2(lines2)
 check(lines1a)
 check(lines2a)
 write(fileout,lines1a,lines2a)
 
 #print('Prepare HTML in ', out_html)
 #write_diff_to_html(out_tsv, out_html, dict1, dict2)
 
