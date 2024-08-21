#-*- coding:utf-8 -*-
""" remove_and_or.py
"""
from __future__ import print_function
import sys,re,codecs,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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
 
def change_lines(lines):
 newlines = []
 nchange = 0
 regex1_raw = r'<info or=".*?"/>'
 regex2_raw = r'<info and=".*?"/>'
 regex1,regex2 = (re.compile(regex1_raw),re.compile(regex2_raw))
 count1 = 0
 count2 = 0
 for line in lines:
  newline1 = re.sub(regex1,'',line)
  if newline1 != line:
   count1 = count1 + 1
  newline = re.sub(regex2,'',newline1)
  if newline != newline1:
   count2 = count2 + 1
  newlines.append(newline)
 print('remove %s instances of %s' %(count1,regex1_raw))
 print('remove %s instances of %s' %(count2,regex2_raw))
 return newlines
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] #
 lines = read_lines(filein)
 newlines = change_lines(lines)
 write_lines(fileout,newlines)

