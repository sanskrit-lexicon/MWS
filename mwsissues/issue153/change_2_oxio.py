# coding=utf-8
""" 
extract_gr.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def select(entries):
 #omicron_tonos = 'ό'  # u+03cc
 #omicron_oxia = 'ό'    # u+1f79
 tonos_oxias = [
  ('ό' , 'ό'),  # omicron
  ('ΐ' , 'ΐ'),  # IOTA WITH DIALYTIKA
  ('ά' , 'ά'), # alpha
  ('έ' , 'έ'),  # epsilon
  ('ή', 'ή'),   # eta
  ('ί', 'ί'),   # iota
  ('ύ', 'ύ'),   # upsilon
  ('ώ', 'ώ'),   # omega
  
  ]
 # change tonos to oxia.
 nfound = 0
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   newline = line
   for tonos,oxia in tonos_oxias:
    newline = newline.replace(tonos,oxia)
   if newline == line:
    continue
   # generate change
   entry.changes.append((iline,line,newline))
   nfound = nfound + 1

 print('select: %s lines to change' %nfound)

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
