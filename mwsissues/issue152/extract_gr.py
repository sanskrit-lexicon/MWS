# coding=utf-8
""" 
extract_gr.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def select(entries):
 nfound = 0
 text = '<ls>Gr.'
 for entry in entries:
  grlines = []
  for line in entry.datalines:
   if text in line:
    grlines.append(line)
  # add attribute to the entry
  entry.grlines = grlines
  if grlines != []:
   nfound = nfound + 1
   assert len(grlines) == 1
 print('select %s entries matching "%s"' %(nfound,text))

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
  for line in entry.grlines:
   grtexts = re.findall(r'<ls>Gr\..*?</ls>',line)
   for grtext in grtexts:
    outarr.append('; %s' % grtext)
   outarr.append(line)
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
