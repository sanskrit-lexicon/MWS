# coding=utf-8
""" 
extract.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def select(entries):
 nfound = 0
 regexraw = r'<s>[^<]*\..*?</s>'
 regex = re.compile(regexraw)
 for entry in entries:
  grlines = []
  for iline,line in enumerate(entry.datalines):
   for m in re.finditer(r'<ls>(.*?)</ls>',line):
    x = m.group(1)
    if x.startswith(('Gr.','Gram.')):
     grlines.append(x)
     nfound = nfound + 1
  # add attribute to the entry
  entry.grlines = grlines
 print('select %s instances'%nfound)

def write(fileout,entries):
 outrecs = []
 for entry in entries:
  grlines = entry.grlines
  if grlines == []:
   continue
  outarr = []
  outarr.append('; ------------------------------------------------------')
  meta = entry.metaline
  meta = re.sub(r'<k2>.*$','',meta)
  outarr.append('; %s' % meta)
  for text in entry.grlines:
   outarr.append('%s ::: ?' % text)
  outrecs.append(outarr)   
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
if __name__=="__main__":
 filein = sys.argv[1] # e.g., mw.txt
 fileout = sys.argv[2] # text output
 # read all the entries of the dictionary.
 entries = digentry.init(filein)
 
 select(entries)
 write(fileout,entries)
