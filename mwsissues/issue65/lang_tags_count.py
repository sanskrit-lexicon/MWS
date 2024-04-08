#-*- coding:utf-8 -*-
"""lang_tags_count.txt
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

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
 
def update_langtags_dict(d,lines):
 z = [('<lang>%s</lang>' % k,k) for k in d]
 for iline,line in enumerate(lines):
  # skip metalines and empty lines
  if line.startswith(('<L>','<LEND>')):
   continue
  if line.strip() == '':   
   continue
  for elt,k in z:
   nelt = line.count(elt)
   if nelt != 0:
    d[k] = d[k] + nelt
 return d

def write_count(fileout,d):
 outarr = []
 for key in d:
  out = '<lang>%s</lang> %s' %(key,d[key])
  outarr.append(out)
 write_lines(fileout,outarr)
 
if __name__=="__main__":
 langtagfile = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt 
 fileout = sys.argv[3] #
 langtags_dict = init_langtags(langtagfile)
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 update_langtags_dict(langtags_dict,lines)
 write_count(fileout,langtags_dict)
 

