#-*- coding:utf-8 -*-
"""mwverb.py
 
 
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  #  extra attributes
  self.marked = False # from a filter of markup associated with verbs
  self.verb = None  # value of verb attribute root|genuineroot|pre|gati|nom
  self.parse = None  # string value of parse attribute (for pre/gati
  self.cps  = None  # string value of cp attribute
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

def mark_entries_verb(entries):
 infokeys = ['verb','cp','parse']
 for entry in entries:
  marks = []
  for iline,line in enumerate(entry.datalines):
   m = re.search(r'<info +(verb=.*?)/>',line) # empty element
   if not m:
    continue 
   s = m.group(1) # 
   for i,key in enumerate(infokeys):
    regex=r'%s="(.*?)"' %key
    m = re.search(regex,s)
    if m:
     marks.append(m.group(1))
    else:
     marks.append('')
   if marks[0] == '':
    continue  # require the 'verb' attribute. Otherse are optional    
  if len(marks) > 0:
   entry.marked = True
   entry.verb,entry.cps,entry.parse = marks

def write(fileout,entries):
 n = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for entry in entries:
   if not entry.marked:
    continue
   n = n + 1
   L = entry.metad['L']
   k1 = entry.metad['k1']
   outarr = []
   outarr.append(k1)
   outarr.append(L)
   #out = '%s:%s' %(k1,L)
   #outarr.append(outarr)
   outarr.append(entry.verb)
   outarr.append(entry.cps)
   outarr.append(entry.parse)
   out = ':'.join(outarr)
   f.write(out + '\n')
 print(n,"records written to",fileout)

if __name__=="__main__": 
 dictlo = sys.argv[1] # xxx
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] # 
 entries = init_entries(filein)
 mark_entries_verb(entries)
 write(fileout,entries)
