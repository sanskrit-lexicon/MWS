# -*- coding: utf-8 -*-
"""find_accent_diff3a
"""
import codecs
import re
import sys
import csv
from collections import defaultdict
import parseheadline

def prepare_dict_mw(filein):
 fin = codecs.open(filein, 'r', 'utf-8')
 result = defaultdict(list)
 for lin in fin:
  if lin.startswith('<L>'):
   meta = parseheadline.parseheadline(lin)
   k1 = meta['k1']
   # revised k2 syntax allows comma-separated list
   k2s = meta['k2'].split(',')
   for k2 in k2s:
    if re.search(r'[—-]',k2):
     # skip entry with 'compound' markup
     continue
    # require an accent
    if not re.search('[\/^]', k2):
     continue
    if (k2 not in result[k1]):
     result[k1].append(k2)    
 fin.close()
 print('prepare_dict_mw:',len(result.keys()))
 return result

def prepare_dict_pw(filein):
 fin = codecs.open(filein, 'r', 'utf-8')
 result = defaultdict(list)
 for lin in fin:
  if lin.startswith('<L>'):
   meta = parseheadline.parseheadline(lin)
   k1 = meta['k1']
   k2 = meta['k2']
   # require an accent
   if not re.search('[\/^]', k2):
    continue
   if (k2 not in result[k1]):
    result[k1].append(k2)    
 fin.close()
 print('prepare_dict_pw:',len(result.keys()))
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

def old_write_diff_to_tsv(d1, d2, d1pc,file_tsv):
 fout = codecs.open(file_tsv, 'w', 'utf-8')
 ndiff = 0
 for key in d1:
  if key in d2:
   if set(d1[key]) != set(d2[key]):
    ndiff = ndiff + 1
    
    a = [key, ','.join(d1[key]), ','.join(d2[key]), ';'.join(d1pc[key])]
    out = '\t'.join(a)
    fout.write(out+'\n')
    #fout.write(key + '\t' +  + '\t' + ','.join(d2[key]) + '\n')
 print(ndiff,'differences written to',file_tsv)
 fout.close()

def write_diff_to_tsv(d1k2, d2a, d1pc,file_tsv):
 # print only those where there is a difference
 fout = codecs.open(file_tsv, 'w', 'utf-8')
 nf = 0 # number not found
 n = 0 # keys in d2a
 neq = 0 # count keys where d1k2s = d2k2s
 nout = 0
 for key in d2a:
  n = n + 1
  if key not in d1k2:
   # exclude
   nf = nf + 1
   continue
  d2k2s = d2a[key]
  d1k2s = d1k2[key]
  if set(d1k2s) == set(d2k2s):
   neq = neq + 1
   continue
  d1pcs = d1pc[key]
  d1k2txt = ' '.join(d1k2s)
  d1pctxt = ' '.join(d1pcs)
  d2k2txt = ' '.join(d2k2s)
  keya = key.ljust(10)
  d1k2txta = d1k2txt.ljust(15)
  d2k2txta = d2k2txt.ljust(15)
  status = '_'
  a = [status,keya,d1k2txta,d2k2txta,d1pctxt]
  out = '\t'.join(a)
  nout = nout + 1
  fout.write(out+'\n')
 print('write: n=%s, nf = %s, neq=%s, nout=%s' %(n,nf,neq,nout))
 fout.close()

def old_get_k1k2(filein):
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
 assert ('mw' in filedict1 ) and ('pw' in filedict2)
 print("Prepare dict from ", filedict1)
 d1 = prepare_dict_mw(filedict1)
 dpage = k1pc(filedict1)
 print("Prepare dict from ", filedict2)
 d2 = prepare_dict_pw(filedict2)

 # d2a the cases of d2 occuring in d1
 d2a = {}
 for k1 in d2:
  # k1 is for pwg.
  k1mw = k1.replace('vant','vat')  # the mw spelling
  if k1mw in d1:
   d2a[k1] = d2[k1]
 #d1k2 = get_k1k2(filedict1) # key is k1, value is list of k2s.
 print('d2a count:',len(d2a.keys()))
 d1k2 = d1

 print('Write difference to ', out_tsv)
 write_diff_to_tsv(d1k2, d2a, dpage, out_tsv)
 
 #print('Prepare HTML in ', out_html)
 #write_diff_to_html(out_tsv, out_html, dict1, dict2)
 
