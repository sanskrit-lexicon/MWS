# coding=utf-8
""" 
change_6_phi.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry
import unicodedata

def select(entries):
 def make_new(oldline):
  """
  GREEK SMALL LETTER PHI 03c6 = 966
  GREEK PHI SYMBOL 03d5 = 981   <<< preferred
  """
  n966 = 0
  n981 = 0
  ans = []
  for c in oldline:
   ic = ord(c)
   if ic == 981: # ok. PHI SYMBOL
    ans.append(c)
    n981 = n981 + 1
   elif ic == 966: # change to PHI SYMBOL
    d = chr(981)
    ans.append(d)
    n966 = n966 + 1
   else: # some other characer
    ans.append(c)
  newline = ''.join(ans)
  return newline,n966,n981
 
 nfound = 02
 n966a = 0
 n981a = 0
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   newline,n966,n981 = make_new(line)
   n966a = n966a + n966
   n981a = n981a + n981
   if newline == line:
    continue
   # generate change
   entry.changes.append((iline,line,newline))
   nfound = nfound + 1

 print('select: %s lines to change' %nfound)
 print('SMALL LETTER PHI 03C6 changed %s times' % n966a)
 print('PHI SYMBOL unchanged %s times' %n981a)

def write(fileout,entries):
 outrecs = []
 for entry in entries:
  changes = entry.changes
  if changes == []:
   continue  
  outarr = []
  outarr.append('; ------------------------------------------------------')
  meta = entry.metaline
  meta = re.sub(r'<k2>.*$','',meta)
  outarr.append('; %s (%s lines changed)' % (meta,len(changes)))
  for iline,old,new in changes:   
   lnum = entry.linenum1 + iline + 1
   outarr.append('%s old %s' %(lnum,old))
   outarr.append(';')
   outarr.append('%s new %s' %(lnum,new))
   if len(changes) != 1:
    outarr.append('; ------------------------')
  outrecs.append(outarr)   
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] # e.g., mw.txt
 fileout = sys.argv[2] # text output
 # read all the entries of the dictionary.
 entries = digentry.init(filein)
 
 select(entries)
 write(fileout,entries)
