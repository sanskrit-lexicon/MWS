#-*- coding:utf-8 -*-
""" remove_tru_hui.py
"""
from __future__ import print_function
import sys,re,codecs,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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

def change_lines(lines):
 newlines = []
 nchange = 0
 # the initial 'x' is temporary markup in temp_mw_9.txt
 regex_raw = r'<x?info hui="([0-9]+)"/>'
 regex = re.compile(regex_raw)
 for line in lines:
  newline = re.sub(regex,'',line)
  newlines.append(newline)
  if newline != line:
   nchange = nchange + 1
 print('change_line: %s lines changed' % nchange)
 return newlines
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx/
 lines = read_lines(filein)
 newlines = change_lines(lines)
 write_lines(fileout,newlines)

