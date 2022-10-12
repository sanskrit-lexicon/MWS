# -*- coding: utf-8 -*-
"""find_accent_diff5a
"""
import codecs
import re
import sys
import csv
from collections import defaultdict
import parseheadline

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

def ad_known(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [ADrec(x) for x in f if not x.startswith(';')]
 print(len(recs),"ADrecs read from",filein)
 return recs

def ad_known_dict(filein):
 recs = ad_known(filein)
 d = {}
 for rec in recs:
  k1 = rec.k1
  if k1 in d:
   print('ad_known_dict duplicate',k1)
  d[k1] = rec
 return d

def get_all_k1k2(filein):
 fin = codecs.open(filein, 'r', 'utf-8')
 result = defaultdict(list)
 for lin in fin:
  if lin.startswith('<L>'):
   meta = parseheadline.parseheadline(lin)
   k1 = meta['k1']  
   k2s = meta['k2'].split(',') # allow comma-separated values
   for k2 in k2s:
    if k2 not in result[k1]:
     result[k1].append(k2)
 fin.close()
 print(len(result.keys()),"get_all_k1k2",filein)
 if False:
  print('get_all_k1k2 check begin')
  keys = list(result.keys())
  for k1 in keys[0:2]:
   print(' k1=',k1)
   for k2 in result[k1]:
    print('  k2=',k2)
  print('get_all_k1k2 check end')
 return result
def filter_unaccented(result):
 # For a given k1, if any k2 has an accent, then exclude the k1
 #keep only those k2 containing an accent character.
 # If there are no such k2, then do not include this k1 in result.
 ans = {}
 for k1 in result:
  k2arr = result[k1]
  keep = []
  for k2 in k2arr:
   if re.search('[\/^]', k2):
    keep.append(k2)
  if keep == []:  
   ans[k1] = keep
 print(len(ans.keys()),'filter_accented')
 return ans

def filter_exclude_dash(result):
 # EXCLUDE cases where ALL k2s have a '-'
 # i.e. INCLUDE cases where some k2 does NOT have a '-'
 
 ans = {}
 for k1 in result:
  k2arr = result[k1]
  a = [k2 for k2 in k2arr if re.search(r'[—-]',k2)]
  if a != k2arr:
   ans[k1] = k2arr
 print(len(ans.keys()),'filter_exclude_dash')
 return ans

def filter_remove_dash(result):
 # Also, exclude single quote '  (slp1 for anusvAra. example da/S'oRi
 ans = {}
 for k1 in result:
  k2arr = result[k1]
  # remove '-' from each k2
  newk2s = []
  for k2 in k2arr:
   k2a = re.sub(r"[—'-]",'',k2)
   # undo this change.
   # allow avagraha to remain in mwk2, since it appears in pwg.
   #k2a = re.sub(r"[—-]",'',k2)
   if k2a not in newk2s:
    newk2s.append(k2a)
  ans[k1] = newk2s
 return ans

def prepare_dict_mw(filein):
 result = get_all_k1k2(filein)
 #result1 = filter_unaccented(result)
 result1 = result
 #result2 = filter_exclude_dash(result1)
 result2 = result1
 result3 = filter_remove_dash(result2)
 print('prepare_dict_mw:',len(result3.keys()))
 return result3

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
   # remove avagraha, if any
   k2 = k2.replace("'","");
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

def write_diff_to_tsv(d1k2, d2a, d1pc,file_tsv):
 # print only those where there is a difference
 fout = codecs.open(file_tsv, 'w', 'utf-8')
 nf = 0 # number not found
 n = 0 # keys in d2a
 neq1 = 0 # count keys where d1k2s = d2k2s
 neq2 = 0 # count keys where d1k2s = d2k2s + key(no accent)
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
   neq1 = neq1 + 1
   continue
  # We also count as equal when
  # d1k2s (mw) has only 1 additional, non-accented, member compared to 
  # d2k2s (pwg)
  a = [key]
  b = d2k2s + a
  if set(b) == set(d1k2s):
   neq2 = neq2 + 1
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
 neq = neq1 + neq2
 print('write: n=%s, nf = %s, neq=%s, nout=%s' %(n,nf,neq,nout))
 print('neq1 = %s, neq2 = %s' %(neq1,neq2))
 fout.close()

def remove_known(dall,dknown):
 d = {}
 n = 0
 for k1 in dall:
  if k1 not in dknown:
   d[k1] = dall[k1]
   n = n + 1
 print(n,"records returned by remove_known")
 return d
if __name__ == "__main__":
 fileknown = sys.argv[1]
 filedict1 = sys.argv[2]
 filedict2 = sys.argv[3]
 out_tsv = sys.argv[4]
 assert ('mw' in filedict1 ) and ('pw' in filedict2)
 adknownd = ad_known_dict(fileknown)
 print("Prepare dict from ", filedict1)
 d1 = prepare_dict_mw(filedict1)
 dpage = k1pc(filedict1)
 print("Prepare dict from ", filedict2)
 d2 = prepare_dict_pw(filedict2)
 d2notknown = remove_known(d2,adknownd)
 
 # d2a the cases of d2 occuring in d1
 d2a = {}
 for k1 in d2notknown:
  # k1 is for pwg.
  k1mw = k1.replace('vant','vat')  # the mw spelling
  if k1mw in d1:
   d2a[k1] = d2notknown[k1]
 #d1k2 = get_k1k2(filedict1) # key is k1, value is list of k2s.
 print('d2a count:',len(d2a.keys()))
 d1k2 = d1

 print('Write difference to ', out_tsv)
 write_diff_to_tsv(d1k2, d2a, dpage, out_tsv)
 
 #print('Prepare HTML in ', out_html)
 #write_diff_to_html(out_tsv, out_html, dict1, dict2)
 
