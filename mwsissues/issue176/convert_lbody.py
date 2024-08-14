#-*- coding:utf-8 -*-
""" convert_lbody.py
"""
from __future__ import print_function
import sys,re,codecs,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import digentry
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

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

def write_entries_helper(entry):
 outarr = []
 outarr.append(entry.metaline)
 for line in entry.datalines:
  outarr.append(line)
 outarr.append(entry.lend)
 return outarr

def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs,blankflag=False) # no blank line

class Group:
 def __init__(self,key):
  self.key = key  # L1,X1;L2,X2; ...
  self.ientries = []
  self.Lk1s = key.split(';')
  self.Ls = []
  self.k1s = []
  for Lk1 in self.Lk1s:
   try:
    (L,k1) = Lk1.split(',')
    self.Ls.append(L)
    self.k1s.append(k1)
   except:
    print('Group error:',key)
    exit(1)
  self.seqflag = None  # Are group entries sequential
  self.seqflag1 = None # Are bodylines same in groups?
  self.seqflag5 = None # <h>[a-z]
  self.seqflag6 = None # Are metaline-<e> the same in group?
  self.ientrydiffs = []  # updated in check_groups_3
  
def init_groups(entries):
 regexes_raw = []
 regexes = []
 for option in ('or','and'):
  regex_raw = r'<info %s="(.*?)"/>' % option
  regex = re.compile(regex_raw)
  regexes_raw.append(regex_raw)
  regexes.append(regex)
  
 groupd = {}
 groups = []
 n = 0
 for ientry,entry in enumerate(entries):
  text = ' '.join(entry.datalines)
  for regex in regexes:
   for m in re.finditer(regex,text):
    n = n + 1
    data = m.group(1)  # L1,X1;L2,X2; ...
    if data not in groupd:
     group = Group(data)
     groupd[data] = group
     groups.append(group)
    else:
     group = groupd[data]
    group.ientries.append(ientry)

 print('%s entries matching %s' %(n,regexes_raw))
 keys = groupd.keys()
 print('%s groups' % len(keys))
 #check_groups_1(groupd,entries)
 #check_groups_2(groupd,entries)
 return groups

def write_entries1_helper(entry):
 outarr = []
 g = entry.group
 if g.startswith('; BEGIN'):
  outarr.append('') # blank line
  outarr.append(g)
 outarr.append(entry.metaline)
 for line in entry.datalines:
  outarr.append(line)
 outarr.append(entry.lend)
 if g.startswith('; END'):
  outarr.append(g)
  outarr.append('') # blank line
 return outarr

def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs,blankflag=False)
 
def revise_entries(groups,entries):
 for group in groups:
  ientries = group.ientries
  # begin group 
  ientry0 = ientries[0]
  entry0 = entries[ientry0]
  L0 = entry0.metad['L']
  for ientry in ientries[1:]:
   entry = entries[ientry]
   # change entry.datalines
   newdataline = '{{Lbody=%s}}' % L0
   entry.datalines = [newdataline]
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # output with errors marked.
 entries = digentry.init(filein)
 Ldict = digentry.Entry.Ldict;

 groups = init_groups(entries) # get both or/and
 revise_entries(groups,entries)
 write_entries(fileout,entries)
 
