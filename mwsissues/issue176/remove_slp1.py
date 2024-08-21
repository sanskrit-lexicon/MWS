#-*- coding:utf-8 -*-
""" remove_slp1.py
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

def change_line_s1(line):
 # s1 tag can have only one attribute 'slp1', which is optional
 regex = r'<s1( slp1="[^>]*?")>([^<]*?)</s1>'
 replacements = []
 for m in re.finditer(regex,line):
  old = m.group(0)
  attr = m.group(1)
  txt = m.group(2)
  new = '<s1>%s</s1>' % txt
  replacements.append((old,new))
 if replacements == []:
  return line,replacements
 # generate new line
 newline = line
 oldarr = []
 for old,new in replacements:
  newline = newline.replace(old,new)
  oldarr.append(old)
 return newline,oldarr

def change_lines_s1(lines):
 newlines = []
 arr = []
 nchange = 0
 for line in lines:
  newline,a = change_line_s1(line)
  newlines.append(newline)
  for old in a:
   arr.append(old)
  if newline != line:
   nchange = nchange + 1
 print('change_line_s1: %s lines changed' % nchange)
 return newlines,arr

def change_line_ab_slp1(line):
 # example:
 # old: <ab n="Pitṛ" slp1="pitf">P°</ab>
 # new: <s1 n="Pitṛ">P°</s1>
 regex = r'<ab( n="[^>]*?")( slp1="[^>]*?")>(.*?)</ab>'
 replacements = []
 for m in re.finditer(regex,line):
  old = m.group(0)
  attr_n = m.group(1)
  attr_slp1 = m.group(2)
  txt = m.group(3)
  new = '<s1%s>%s</s1>' % (attr_n,txt)
  replacements.append((old,new))
 if replacements == []:
  return line,replacements
 # generate new line
 newline = line
 oldarr = []
 for old,new in replacements:
  newline = newline.replace(old,new)
  oldarr.append(old)
 return newline,oldarr

def change_lines_ab_slp1(lines):
 newlines = []
 arr = []
 nchange = 0
 for line in lines:
  newline,a = change_line_ab_slp1(line)
  newlines.append(newline)
  for old in a:
   arr.append(old)
  if newline != line:
   nchange = nchange + 1
 print('change_line_ab_slp1: %s lines changed' % nchange)
 return newlines,arr


if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx/
 fileout1 = sys.argv[3]  # instances of slp1 attribute in <s1> tag
 fileout2 = sys.argv[4]  # instances of slp1 attribute in <ab> tag
 
 lines = read_lines(filein)
 newlines_1,arr1 = change_lines_s1(lines)
 newlines_2,arr2 = change_lines_ab_slp1(newlines_1)
 
 newlines = newlines_2
 write_lines(fileout,newlines)
 write_lines(fileout1,arr1)
 write_lines(fileout2,arr2)
 
