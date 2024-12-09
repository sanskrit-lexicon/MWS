# coding=utf-8
""" link_prepare.py for MW (BhP)
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"read from",filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def unused_change_1(line):
 # ", 3" -> ",3"
 try:
  newline = re.sub(r', ([0-9])', r',\1',line)
 except:
  print('error1: %s' % line)
  exit(1)
 return newline

def change_remove_space(line):
 # ", 3" -> ",3"
 # only in <lsX</ls>
 def replace(m):
  old = m.group(0)
  new = re.sub(r', ([0-9])', r',\1',old)
  return new
 newline = re.sub('<ls.*?</ls>',replace,line)
 return newline

def change_restore_space(line):
 # ",3" -> ", 3" 
 # only in <lsX</ls>
 def replace(m):
  old = m.group(0)
  new = re.sub(r',([0-9])', r', \1',old)
  return new
 newline = re.sub('<ls.*?</ls>',replace,line)
 return newline

def change(lines,option):
 newlines = []
 n = 0
 if option == '1':
  changeline = change_remove_space
 elif option == '2':
  changeline = change_restore_space
 else:
  print('ERROR: unknown option',option)
  exit(1)
 for line in lines:
  newline = line
  newline = changeline(newline)
  newlines.append(newline)
  if newline != line:
   n = n + 1
 print('%s lines changed' % n)
 return newlines
 
if __name__=="__main__":
 option = sys.argv[1]  
 filein = sys.argv[2]  # xxx.txt
 fileout = sys.argv[3] #
 lines = read_lines(filein)
 lines1 = change(lines,option)
 write_lines(fileout,lines1)
