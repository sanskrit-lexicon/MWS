#-*- coding:utf-8 -*-
"""tag_to_lang.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def change_lines(lines,d,tag):
 
 newlines = []
 nchg = 0 # number of lines changed
 regex = r'<%s>(.*?)</%s>' % tag
 regexa = re.compile(regex) # for efficiency
 
 for iline,line in enumerate(lines):
  """
re.findall return"
   If the pattern has one capturing group, 
     the function returns a list of strings that match that group.
   If the pattern has multiple capturing groups, 
     the function returns tuples of strings corresponding to those groups.
  """
  abs = re.findall(regexa,line)
  if abs == []:
   newlines.append(line)
   continue
  newline = line
  for x in abs:
   if x in d:
    old = '<%s>%s</%s>' % (tag,x,tag)
    new = '<lang>%s</lang>' % x
    newline = newline.replace(old,new)
    # update d
    d[x] = d[x] + 1
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
  if False: # dbg
   if newline != line:
    print('old:',line)
    print('new:',newline)
    exit()
 print('%s lines changed' % nchg)
 return newlines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)
 
def init_langtags(filein):
 lines = read_lines(filein)
 d = {}
 for line in lines:
  # <lang>X</lang>
  m = re.search(r'<lang>([^<]*)</lang>',line)
  if m == None:
   print('init_langtags error: %s' % line)
   exit(1)
  x = m.group(1)
  if x in d:
   print('init_langtags duplicate',line)
   exit(1)
  d[x] = 0  # count of instances
 print(len(lines),"lang tags read from",filein)
 return d

def write_unused_tags(fileout,d):
 outarr = []
 # write tags that are not found
 for x in d:
  val = d[x]
  if val == 0:
   y = '<lang>%s</lang>' % x
   outarr.append(y)
 write_lines(fileout,outarr)
 
if __name__=="__main__":
 oldtag = sys.argv[1]
 langtagfile = sys.argv[2]
 filein = sys.argv[3] #  xxx.txt 
 fileout = sys.argv[4] #
 filetodo = sys.argv[5]
 langtags_dict = init_langtags(langtagfile)
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 newlines = change_lines(lines,langtags_dict,oldtag
 write_lines(fileout,newlines)
 write_unused_tags(filetodo,langtags_dict,)
 
 
