#-*- coding:utf-8 -*-
""" k2_semi.py
"""
from __future__ import print_function
import sys,re,codecs

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


def change_lines(lines):
 newlines = []
 nchange = 0
 for line in lines:
  if line.startswith('<LEND>'):
   if line != '<LEND>':
    line = '<LEND>'
    nchange = nchange + 1
   newlines.append(line)
   continue
                  
  if not line.startswith('<L>'):
   newlines.append(line)
   continue
  m = re.search(r'<k2>([^<]+)',line)
  oldk2field = m.group(0) # <k2>xxx
  newk2field = oldk2field.replace(';', '; ')
  newline = line.replace(oldk2field,newk2field)
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

