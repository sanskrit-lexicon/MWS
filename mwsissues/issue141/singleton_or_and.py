# coding=utf-8
""" singleton_or_and.py 
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def write_1(fileout,entries):
 # this display is primarily informational
 outrecs = []
 # title
 outarr = []
 outarr.append('; **********************************************************')
 outarr.append('; %s' % fileout)
 outarr.append('; **********************************************************')
 outrecs.append(outarr)
 nprob = 0
 for entry in entries:
  metaline = entry.metaline
  headline = entry.datalines[0]
  outarr = []
  outarr.append('%s' % metaline)
  head1 = re.sub(r' *¦.*$','',headline)
  outarr.append('%s' % head1)
  head2 = re.sub(r'<srs/>','',head1)
  head2 = re.sub(r'°','',head2)
  m = re.search(r'<s>([^<]+)</s>.*?<s>([^<]+)</s>',head2)
  if m == None:
   nprob = nprob + 1
   out = '; PROBLEM:' 
   outarr.append(out)
   lnum = entry.linenum1+1
   outarr.append('%s old %s' %(lnum,headline))
   outarr.append(';')
   outarr.append('%s new %s' %(lnum,headline))
  else:
   out = '%s,%s' % (m.group(1),m.grooup(2))
   outarr.append(out)
  outarr.append(';')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print("%s entries written to %s" %(len(entries),fileout))
 print(nprob,'Problems parsing headline')

def write_2(fileout,entries):
 # this display changes metaline at k2
 outrecs = []
 # title
 outarr = []
 outarr.append('; **********************************************************')
 outarr.append('; %s' % fileout)
 outarr.append('; **********************************************************')
 outrecs.append(outarr)
 ntodo = 0 
 for entry in entries:
  metaline = entry.metaline
  headline = entry.datalines[0]
  outarr = []
  #outarr.append('%s' % metaline)
  head1 = re.sub(r' *¦.*$','',headline)
  outarr.append('; %s' % head1)
  head2 = re.sub(r'<srs/>','',head1)
  head2 = re.sub(r'°','',head2)
  m = re.search(r'<s>([^<]+)</s>.*?<s>([^<]+)</s>',head2)
  if m == None:
   print('ERROR: PROBLEM Unexpected')
   exit(1)
  newk2 = '%s,%s' %(m.group(1),m.group(2))
  # check completness of newk2
  k1 = entry.metad['k1']
  flag = True
  headk2s = (m.group(1),m.group(2))
  for x in headk2s:
   k1x = re.sub(r'[/\^]','',x) # remove accent
   k1y = re.sub(r'[-—]','',k1x)
   if k1 != k1y:
    flag = False
  if not flag:
   # print warning
   outarr.append('; TODO: k1y %s  !== k1 %s' % (k1y,k1) )
   ntodo = ntodo + 1
  lnum = entry.linenum1
  newmeta = re.sub(r'<k2>.*?<','<k2>%s<' %newk2,metaline)
  outarr.append('%s old %s' %(lnum,metaline))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newmeta))
  outarr.append('; --------------------------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print("%s changes written to %s" %(len(entries),fileout))
 if ntodo != 0:
  print(ntodo,'TODO cases')
def get_singletons(entries):
 ans = []
 regexesraw = [
  r'<info or="[^;"]+"/>',
  r'<info and="[^;"]+"/>',
  ]
 regexes = [re.compile(regex) for regex in regexesraw]
 for entry in entries:
  headline = entry.datalines[0]
  found = False
  for regex in regexes:
   if re.search(regex,headline):
    found = True
  if not found:
   continue
  ans.append(entry)
 print(len(ans),'singleton or/and entries')
 return ans
if __name__=="__main__":
 option = sys.argv[1]
 assert option in ['1','2']
 filein = sys.argv[2] # mw.txt
 fileout = sys.argv[3] # changes.txt
 mwentries = digentry.init(filein)
 sentries = get_singletons(mwentries)
 if option == '1':
  write_1(fileout,sentries)
 elif option == '2':
  write_2(fileout,sentries)
  
