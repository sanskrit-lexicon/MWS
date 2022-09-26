# -*- coding: utf-8 -*-
"""find_accent_diff1
"""
import codecs
import re
import sys
import csv
from collections import defaultdict
import parseheadline

def prepare_dict(filein,option):
 #filein = '../../../cologne/csl-orig/v02/' + dict1 + '/' + dict1 + '.txt'
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

def write_diff_to_tsv(d1, d2, d1pc,file_tsv):
 fout = codecs.open(file_tsv, 'w', 'utf-8')
 ndiff = 0
 for key in d1:
  if key in d2:
   if set(d1[key]) != set(d2[key]):
    ndiff = ndiff + 1    
    a = [key, ','.join(d1[key]), ','.join(d2[key]), ','.join(d1pc[key])]
    out = '\t'.join(a)
    fout.write(out+'\n')
    #fout.write(key + '\t' +  + '\t' + ','.join(d2[key]) + '\n')
 print(ndiff,'differences written to',file_tsv)
 fout.close()


def write_diff_to_html(file_tsv, file_html, dict1, dict2):
 fin = codecs.open(file_tsv, 'r', 'utf-8')
 reader = csv.reader(fin, delimiter='\t')
 fout = codecs.open(file_html, 'w', 'utf-8')
 fout.write('<html><body><table>')
 fout.write('<tr><th>key</th><th>' + dict1 + '</th><th>' + dict2 + '</th></tr>')
 for row in reader:
  (key, d1, d2) = row
  fout.write('<tr><td>' + key + '</td><td><a target="_blank" href="https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=' + dict1.upper() + '&key=' + key + '">' + d1 + '</a></td><td><a target="_blank" href="https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=' + dict2.upper() + '&key=' + key + '">' + d2 + '</a></td></tr>\n')
 fout.write('</table></body></html>')
 fin.close()
 fout.close()
# https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=PWG&key=rAma

if __name__ == "__main__":
 option1,option2= sys.argv[1].split(',')  # 
 filedict1 = sys.argv[2]
 filedict2 = sys.argv[3]
 out_tsv = sys.argv[4]

 print("Prepare dict from ", filedict1)
 d1 = prepare_dict(filedict1,option1)
 dpage = k1pc(filedict1)
 print("Prepare dict from ", filedict2)
 d2 = prepare_dict(filedict2,option2)

 print('Write difference to ', out_tsv)
 write_diff_to_tsv(d1, d2, dpage, out_tsv)
 
 #print('Prepare HTML in ', out_html)
 #write_diff_to_html(out_tsv, out_html, dict1, dict2)
 
