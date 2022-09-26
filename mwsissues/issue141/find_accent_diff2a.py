# -*- coding: utf-8 -*-
"""find_accent_diff2a.py
"""
import codecs
import re
import sys
import csv
from collections import defaultdict
import parseheadline

def prepare_dict(filein,option):
 fin = codecs.open(filein, 'r', 'utf-8')
 result = defaultdict(list)
 for lin in fin:
  if lin.startswith('<L>'):
   meta = parseheadline.parseheadline(lin)
   k1 = meta['k1']
   k2 = meta['k2']
   # Ignore hyphenated differences
   k2 = k2.replace('-', '')
   k2 = k2.replace('—', '')
   if option == '0':
    # any accent
    if re.search('[\/^]', k2) and (k2 not in result[k1]):
     result[k1].append(k2)
   elif option == '1':
    if ('^' in k2) and (k2 not in result[k1]):
     result[k1].append(k2)    
   else:
    print('prepare_dict unknown option:',option)
    exit(1)
 fin.close()
 return result

def k1pc(filein):

 fin = codecs.open(filein, 'r', 'utf-8')
 result = defaultdict(list)
 for lin in fin:
  if lin.startswith('<L>'):
   meta = parseheadline.parseheadline(lin)
   pc = meta['pc']
   k1 = meta['k1']   
   if pc not in result[k1]:
    result[k1].append(pc)
 fin.close()
 return result

def write_diff_to_tsv(d1k2, d2a, d1pc,file_tsv):
 fout = codecs.open(file_tsv, 'w', 'utf-8')
 nf = 0 # number not found
 n = 0 # keys in d2a
 for key in d2a:
  n = n + 1
  if key in d1k2:
   d1k2txt = ','.join(d1k2[key])
   d1pctxt = ','.join(d1pc[key])
  else:
   d1k2txt = 'NF' # not found
   d1pctxt = 'NF'
   nf = nf + 1
  d2k2txt = ','.join(d2a[key])
  a = [key,d1k2txt,d2k2txt,d1pctxt]
  out = '\t'.join(a)
  fout.write(out+'\n')
 print('%s records printed, %s not found in mw' %(n,nf))

 fout.close()

def get_k1k2(filein):
 fin = codecs.open(filein, 'r', 'utf-8')
 result = defaultdict(list)
 for lin in fin:
  if lin.startswith('<L>'):
   meta = parseheadline.parseheadline(lin)
   k1 = meta['k1']
   k2 = meta['k2']
   # Ignore hyphenated differences
   k2 = k2.replace('-', '')
   k2 = k2.replace('—', '')
   if k2 not in result[k1]:
    result[k1].append(k2)
 fin.close()
 return result
 
if __name__ == "__main__":
 filedict1 = sys.argv[1]
 filedict2 = sys.argv[2]
 out_tsv = sys.argv[3]

 print("Prepare dict from ", filedict1)
 d1 = prepare_dict(filedict1,'0') # any accent
 d1pc = k1pc(filedict1)
 print("Prepare dict from ", filedict2)
 d2 = prepare_dict(filedict2,'1')  # svarita only for pwg

 # We have already examined d1 and d2.
 # remove from d2 all cases in d1
 d2a = {}
 for k1 in d2:
  # k1 is for pwg.
  k1mw = k1.replace('vant','vat')  # the mw spelling
  if 'vant' in k1mw:
   k1mw = k
  if k1mw not in d1:
   d2a[k1] = d2[k1]
 d1k2 = get_k1k2(filedict1) # key is k1, value is list of k2s.
 
 print('Write difference to ', out_tsv)
 write_diff_to_tsv(d1k2, d2a, d1pc, out_tsv)
 
