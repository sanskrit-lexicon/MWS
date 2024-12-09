# coding=utf-8
""" link_prelim2.py for 'BhP.' in MW
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_recs(fileout,recs):
 outarr = []
 for rec in recs:
  # rec is an array, convert to strings
  rec1 = []
  for x in rec:
   y = str(x)
   rec1.append(y)
  out = '\t'.join(rec1)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def get_all_regexes(X):
 regexraws = [
  r'<ls>%s.*?</ls>' % X,
  r'<ls n="%s.*?</ls>' % X
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def get_partitions(regexes,allrecs):
 matches = []
 imatches = []
 counts = {}
 for iregex,regex in enumerate(regexes):
  a,ia = match_recs(allrecs,regex)
  matches.append(a)
  imatches.append(ia)
  counts[iregex] = len(ia)
 return matches,imatches,counts

def print_regex_counts(title,regexraws,counts):
 outarr = []
 outarr.append(title)
 nregex = len(regexraws)
 ntot = 0
 for i in range(nregex):
  raw = regexraws[i]
  raw1 = raw.replace('\\','')
  n = counts[i]
  outarr.append('%5d %s' %(n,raw1))
  ntot = ntot + n
 outarr.append('%5d Total' %ntot)
 outarr.append('')
 #
 for out in outarr:
  print(out)
 
def findall_ls_entries(entries,regexes):
 nregex = len(regexes)
 recs = []
 counts = {}
 for i in range(nregex):
  counts[i] = 0
 dups = [] # lines with duplicate ls
 for ientry,entry in enumerate(entries):
  #text = ' '.join(entry.datalines)
  L = entry.metad['L'] # the entry id
  k1 = entry.metad['k1'] # the entry id
  linenum1 = entry.linenum1
  for idx,line in enumerate(entry.datalines):
   lnum = linenum1 + idx + 1
   d = {}
   vals = []
   dupflag = False
   counts_line = {}
   for iregex,regex in enumerate(regexes):
    a = re.findall(regex,line)
    for x in a:
     val = (L,k1,lnum,x)
     vals.append(val)
     if iregex not in counts_line:
      counts_line[iregex] = 0
     counts_line[iregex] = counts_line[iregex] + 1
     if val in d:
      dupflag = True
      break
     d[val] = True
    if dupflag:
     dups.append(lnum)
     continue
   for val in vals:
    recs.append(val)
   for iregex in counts_line:
    counts[iregex] = counts[iregex] + counts_line[iregex]
 print('findall_ls_entries: number of lines with duplicates=',len(dups))
 return recs,counts 

def get_standard_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "(\.| fg\.| fgg\.|\. fg\.|\. fgg\.)?"
 regexraws = [
  r'<ls>%s</ls>' % X,
  r'<ls>%s %s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s</ls>' %(X,d1,d2,d3,Y),
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def get_partition_regexes(X):
 regexraws = [
  r'<ls>%s</ls>' % X,
  r'<ls>%s [0-9]' % X,
  r'<ls>%s [e]' % X,
  r'<ls>%s [^0-9e]' % X,
  
  r'<ls n="%s">' % X,
  r'<ls n="%s [0-9]' % X,
  r'<ls n="%s [e]' % X,
  r'<ls n="%s [^0-9e]' % X,
  r'<ls>%s\)' % X  # erroneous paren
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def match_recs(recs,regex):
 # recs is array of (lnum,ls)
 recs1 = []
 irecs1 = []
 for irec,rec in enumerate(recs):
  ientry,lnum,ls = rec
  if re.search(regex,ls):
   irecs1.append(irec)
   recs1 = irecs1
 return recs1,irecs1
  
def check_disjoint(ab):
 # ab is a list of lists
 for i,a in enumerate(ab):
  for j,b in enumerate(ab):
   if j<=i:
    continue
   aset = set(a)
   bset = set(b)
   if not aset.isdisjoint(bset):
    cset = aset.intersection(bset)
    c = list(cset)
    print('%s is in group %s AND in group %s' %(c[0],i+1,j+1))
    exit(1)
 print('%s groups are pairwise disjoint' % len(ab))
 
def check_undetected(recs,matches,imatches):
 # matches and imatches are lists of lists.
 iall = set(range(0,len(recs)))
 union = set()
 for a in imatches: 
  for i in a:
   union.add(i)
 d = iall.difference(union)
 ans = []
 for i in d:
  rec = recs[i]
  ans.append(rec)

 #print('dbg:',ans[0:5])
 return ans

def get_filter_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "( fg\.| fgg\.|\. fg\.|\. fgg\.|\.)?"
 
 regexraws = [
  # r'<ls>%s</ls>' % X,
  r'<ls>%s %s,%s,%s%s ' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s ' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s ' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s ' %(X,d1,d2,d3,Y),
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 fileout = sys.argv[2] # 
 entries = digentry.init(filein)
 X = r'BhP\.'
 allregs,allregsraw = get_all_regexes(X)
 allrecs,allcounts = findall_ls_entries(entries,allregs)
 print_regex_counts('TITLE1',allregsraw,allcounts)
 write_recs(fileout,allrecs)
