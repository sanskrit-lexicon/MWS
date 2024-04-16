#-*- coding:utf-8 -*-
"""lang_to_tag.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def change_lines_gk(lines):
 newlines = []
 nchg = 0 # number of lines changed 
 for iline,line in enumerate(lines):
  newline = re.sub(r'<lang n="greek">([^<]*?)</lang>',r'<gk>\1</gk>',line)
  if newline != line:
   nchg = nchg + 1
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
 print('change_lines_gk: %s lines changed' % nchg)
 return newlines

def change_lines_arab_arab(lines):
 newlines = []
 nchg = 0 # number of lines changed 
 for iline,line in enumerate(lines):
  if '<lang ' not in line:
   newlines.append(line)
   continue
  newline = re.sub(r'<lang script="Arabic" n="Arabic">([^<]*?)</lang>',
                   r'<arab>\1</arab>',line)
  if newline != line:
   nchg = nchg + 1
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
 print('change_lines_arab_arab: %s lines changed' % nchg)
 return newlines

def change_lines_arab_other(lines):
 newlines = []
 nchg = 0 # number of lines changed 
 for iline,line in enumerate(lines):
  if '<lang ' not in line:
   newlines.append(line)
   continue
  # for arabic script of other languages than "Arabic",
  # introduce a lang attribute of 'arab' tab
  # This assumes <lang script="Arabic" n="Arabic"> has already been
  # changed to <arab>.
  newline = re.sub(r'<lang script="Arabic" n="(.*?)">([^<]*?)</lang>',
                   r'<arab lang="\1">\2</arab>',line)
  if newline != line:
   nchg = nchg + 1
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
 print('change_lines_arab_other: %s lines changed' % nchg)
 return newlines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt 
 fileout = sys.argv[2] # xxx-revised
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 newlines = change_lines_gk(lines)
 newlines1 = change_lines_arab_arab(newlines)
 newlines2 = change_lines_arab_other(newlines1)
 write_lines(fileout,newlines2)

