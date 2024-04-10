#-*- coding:utf-8 -*-
"""lang_tags_count1.txt
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)

class TagRec:
 def __init__(self,line):  
  self.langtag,count_cdsl,count_ab = line.split('\t')
  self.count_cdsl_old = int(count_cdsl)
  self.count_ab   = int(count_ab)
  self.count_cdsl = 0 # to be updated
  m = re.search(r'^<lang>(.*?)</lang>$',self.langtag)
  self.abbrev = m.group(1)
   
def init_langtags(filein):
 lines = read_lines(filein)
 recs = []
 d = {}
 for iline,line in enumerate(lines):
  if iline == 0: #labels
   continue
  rec = TagRec(line)
  recs.append(rec)
  if rec.abbrev in d:
   print('unexpected duplicate',line)
   exit(1)
  d[rec.abbrev] = rec
 print(len(lines),"lang tags read from",filein)
 return d,recs
 
def update_langtags_dict(d,lines,lnums_del_dict):
 z = [('<lang>%s</lang>' % k,k) for k in d]
 for iline,line in enumerate(lines):
  # skip metalines and empty lines
  if line.startswith(('<L>','<LEND>')):
   continue
  if line.strip() == '':   
   continue
  # skip lines in lnums_del_dict
  lnum = iline + 1
  if lnum in lnums_del_dict:
   continue
  for elt,k in z:
   nelt = line.count(elt)
   rec = d[k]
   if nelt != 0:
    #d[k] = d[k] + nelt
    rec.count_cdsl = rec.count_cdsl + nelt
 return d

def write_count(fileout,d):
 outarr = []
 title = '\t'.join(['TAG','CDSL','CDSLREV','AB','CDSLREV-AB'])
 print(title)
 outarr.append(title)
 for key in d:
  rec = d[key]
  cdslold = str(rec.count_cdsl_old)
  cdslnew = str(rec.count_cdsl)
  ab = str(rec.count_ab)
  diff = str(rec.count_cdsl - rec.count_ab)
  out = '\t'.join((rec.langtag,cdslold,cdslnew,ab,diff))
  if diff != '0':
   print(out)
  # out = '<lang>%s</lang> %s' %(key,d[key])
  outarr.append(out)
 write_lines(fileout,outarr)

def init_lnums_del(filein):
 lines = read_lines(filein)
 d = {}
 for line in lines:
  m = re.search(r'^([0-9]+) (.*)$',line)
  s = m.group(1)
  tag = m.group(2)
  lnum = int(s)
  if lnum not in d:
   d[lnum] = []
  d[lnum].append(tag)
 print(len(d.keys()),"lnums read from",filein)
 return d

if __name__=="__main__":
 langtagfile = sys.argv[1]
 filein1 = sys.argv[2] # countdiff_tags_del.txt
 filein = sys.argv[3] #  xxx.txt
 fileout = sys.argv[4] #
 langtags_dict,langtag_recs = init_langtags(langtagfile)
 lnums_del_dict = init_lnums_del(filein1)
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 update_langtags_dict(langtags_dict,lines,lnums_del_dict)
 write_count(fileout,langtags_dict)
 

