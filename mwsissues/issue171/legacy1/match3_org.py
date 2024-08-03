#-*- coding:utf-8 -*-
""" match3_org.py
"""
from __future__ import print_function
import sys,re,codecs,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import digentry

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
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

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

def write_entries_org_helper(entry):
 # Emacs org-mode
 outarr = []
 # entry.revsup is either R, S, or '' (empty string)
 flag = entry.revsup
 assert flag in ('R','S','')
 # possibly modify meta
 meta = entry.metaline
 if flag in ('R','S'):
  meta = meta.replace('<L>','* TODO %s <L>' % flag)
 #else:
 # meta = meta.replace('<L>','* <L>')
 outarr.append(meta)
 # no change to datalines
 for line in entry.datalines:
  outarr.append(line)
 # possibly modify lend
 lend = entry.lend
 if flag in ('R','S'):
  lend = '* <LEND>'
  pass
 outarr.append(lend)
 return outarr

def write_entries_org(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_org_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs,blankflag=False)

def mark_revsup(entries):
 # add 'revsup' attribute to each entry
 for entry in entries:
  text = ' '.join(entry.datalines)
  if '<info n="sup"' in text:
   entry.revsup = 'S'
  elif '<info n="rev"' in text:
   entry.revsup = 'R'
  else:
   entry.revsup = ''  # neither rev nor sup. Normal 'body' entry
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # output summary
 entries = digentry.init(filein)
 mark_revsup(entries)
 write_entries_org(fileout,entries) 
