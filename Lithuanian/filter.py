#-*- coding:utf-8 -*-
"""filter.py
 
 
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
  self.marked_ilines = [] # from a filter 
  
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

def mark_entries(entries):

 for entry in entries:
  marks = []
  for iline,line in enumerate(entry.datalines):
   # we have checked that at most one instance of following regex
   # occurs in any given line.
   m = re.search(r'<ab>Lit[.]</ab> <etym>.*?</etym>',line) 
   if m:
    entry.marked_ilines.append(iline)

def write(fileout,entries,fileout1):
 n = 0
 f1 = codecs.open(fileout1,"w","utf-8")  # manualByLine format
 with codecs.open(fileout,"w","utf-8") as f:  # instance format
  icase = 0
  for entry in entries:
   if entry.marked_ilines == []:
    continue
   n = n + 1
   L = entry.metad['L']
   k1 = entry.metad['k1']
   lnum1 = entry.linenum1
   for iline in entry.marked_ilines:
    lnum = lnum1 + iline
    # since lnum1 is the meta line, and datalines starts with line
    # after meta line, we need to add 1
    lnum = lnum + 1  
    line = entry.datalines[iline]
    # assume exactly one match in next
    m = re.search(r'<ab>Lit[.]</ab> <etym>(.*?)</etym>',line) 
    oldetym=m.group(1)
    out = '%s:%s:%s:' %(L,k1,oldetym)
    f.write(out + '\n')
    # manualByLine form
    icase = icase + 1
    outarr = []
    outarr.append('; Case %s : %s:%s:%s:' %(icase,L,k1,oldetym))
    outarr.append('%s old %s' %(lnum,line))
    outarr.append('%s new %s' %(lnum,line))
    outarr.append(';')
    for out in outarr:
     f1.write(out+'\n')
 f1.close()
 print(n,"records written to",fileout)
 print(icase,"records written to",fileout1)

if __name__=="__main__": 
 dictlo = sys.argv[1] # xxx
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] # 
 fileout1 = sys.argv[4] # 
 entries = init_entries(filein)
 mark_entries(entries)
 write(fileout,entries,fileout1)
