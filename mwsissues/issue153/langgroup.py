# coding=utf-8
""" 
langgroup.py  parses lang.string.changes
"""
from __future__ import print_function
import sys, re,codecs

class LangGroup(object):
 def __init__(self,lnum,msg,comment,old,new):
  self.lnum = lnum
  self.msg = msg
  self.comment = comment
  self.old = old
  self.new = new

def groupgen(lines):
 group = []
 for iline,line in enumerate(lines):
  # ignore lines starting with ;
  if line.startswith(';'):
   continue
  group.append(line)
  if line.startswith('=='):
   # checks
   m = re.search(r'^\(([0-9]+)\): (.*$)',group[0])
   if m == None:
    print('msg problem 1 at line',iline+1)
    exit()
   msg_lnum = m.group(1)
   msg_raw = m.group(2)
   if msg_raw == 'NO Error':
    msg_text = msg_raw
    msg_comment = ''
   else:
    m1 = re.search(r'^(.*?) (\[.*$)',msg_raw)
    if m1 == None:
     print('msg problem 1 at line',iline+1)
     exit(1)
    msg_text = m1.group(1)
    msg_comment = m1.group(2)
   m = re.search(r'^OLD\t(.*)$',group[1])
   if m == None:
    print('msg problem 2 at line',iline+1)
    exit()
   old = m.group(1)
   m = re.search(r'^NEW\t(.*)$',group[3])
   if m == None:
    print('msg problem 3 at line',iline+1)
    print(group[3])
    exit()
   new = m.group(1)
   rec = LangGroup(msg_lnum,msg_text,msg_comment,old,new)
   if False: # dbg
    if iline < 50:
     print('groupgen: lnum=%s, msg=%s, comment=%s' % (msg_lnum,msg_text,msg_comment))
   yield rec
   group = []
   
def init_langgroups(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Group objects
 n = 0
 for rec in groupgen(lines):
  recs.append(rec)
  n = n + 1
  if False: # dbg
   if n < 10:
    print('init_langgroups: lnum=%s, msg=%s' % (rec.lnum,rec.msg))
 print(len(recs),"LangGroups read from",filein)
 return recs
