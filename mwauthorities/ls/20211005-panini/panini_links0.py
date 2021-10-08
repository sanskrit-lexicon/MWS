#-*- coding:utf-8 -*-
"""panini_links0.py
 
 
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
  self.marks = []
  self.ilines = []  # entry.datalines[iline] for marks
  #self.marked = False # from a filter of markup associated with verbs
  #self.verb = None  # value of verb attribute root|genuineroot|pre|gati|nom
  #self.parse = None  # string value of parse attribute (for pre/gati
  #self.cps  = None  # string value of cp attribute
  
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

# example: <ls>Pāṇ. 6-4, 107</ls>
regexraw1 = r'<ls>Pāṇ[.](.*?)</ls>'
regex1 = re.compile(regexraw1)
regexraw2 = r'^ +([0-9]+)-([0-9]+), *([0-9]+)'
# example ' 6-4, 107'
regex2 = re.compile(regexraw2)

def mark_entries(entries):
 regexraw = r'(<ls n="Pāṇ[.][^"]*">.*?</ls>)|(<ls>Pāṇ[.].*?</ls>)'
 regex = re.compile(regexraw)
 
 for entry in entries:
  marks = []
  for iline,line in enumerate(entry.datalines):
   for m in re.finditer(regex,line) :
    entry.marks.append(m.group(0))
    entry.ilines.append(iline)
    
def write(fileout,entries,option=None):
 n = 0
 n1 = 0
 nok = 0
 flagcount = {'Y':0, 'N':0, 'X':0}
 with codecs.open(fileout,"w","utf-8") as f:
  for entry in entries:
   marks = entry.marks
   if marks == []:
    continue
   n = n + 1
   L = entry.metad['L']
   k1 = entry.metad['k1']
   for imark,mark in enumerate(marks):
    n1 = n1 + 1
    out = '%s %s %s' %(k1,L,mark)
    f.write(out + '\n')
 print(n1,"references written to",fileout)

if __name__=="__main__": 
 dictlo = 'mw'
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[2] #
 fileoutN = sys.argv[3]
 entries = init_entries(filein)
 mark_entries(entries)
 write(fileout,entries)
 #write(fileoutN,entries,option='N')
