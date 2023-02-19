# coding=utf-8
""" 
groupcount.py
"""
from __future__ import print_function
import sys, re,codecs
import langgroup

def unused_select(entries):
 nfound = 0
 regexraw = r'<s>[^<]*\..*?</s>'
 regex = re.compile(regexraw)
 for entry in entries:
  grlines = []
  for iline,line in enumerate(entry.datalines):
   m = re.search(regex,line)
   if m != None:
    text = m.group(0)
    grlines.append((iline,line,text))
  # add attribute to the entry
  entry.grlines = grlines
  if grlines != []:
   nfound = nfound + 1
   assert len(grlines) == 1
 print('select %s entries matching "%s"' %(nfound,text))

def write(fileout,d):
 keys = d.keys()
 #keys = sorted(keys)
 outarr = []
 for i,key in enumerate(keys):
  n = d[key]
  
  outarr.append('%d %s' %(n,key))
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')
 print(len(keys),"records written to",fileout)
 
def countmsg(langgroups):
 d = {}
 print(len(langgroups),'in countmsg')
 for i,langgroup in enumerate(langgroups):
  msg = langgroup.msg
  #if i < 10:
  # print(msg)
  if msg not in d:
   d[msg] = 0
  d[msg] = d[msg] + 1
 return d
if __name__=="__main__":
 filein = sys.argv[1] # e.g., lang.string.changes.txt
 fileout = sys.argv[2] # msg coungs
 # read all the entries of the dictionary.
 langgroups = langgroup.init_langgroups(filein)
 d = countmsg(langgroups)
 write(fileout,d)
 
