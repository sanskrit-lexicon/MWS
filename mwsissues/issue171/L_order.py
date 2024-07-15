#-*- coding:utf-8 -*-
""" L_order.py
"""
from __future__ import print_function
import sys,re,codecs
import digentry
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 nout = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
    nout = nout + 1
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
    nout = nout + 1
 if printflag:
  print(len(outrecs),"records (%s lines) written to" % nout,fileout)

def write_entries_helper(entry):
 outarr = []
 outarr.append(entry.metaline)
 for line in entry.datalines:
  outarr.append(line)
 outarr.append(entry.lend)
 return outarr

def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
  
 write_recs(fileout,outrecs,blankflag=False)
 #print(len(outrecs),"entries written to",fileout)

def sort_entries(entries):
 entries1 = sorted(entries,key = lambda e: float(e.metad['L']))
 return entries1

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # xxx.txt reorder by L
 entries = digentry.init(filein)
 entries1 = sort_entries(entries)

 write_entries(fileout,entries1)


