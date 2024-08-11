#-*- coding:utf-8 -*-
""" nonseq.py
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

def check_entries(entries,k1dict):
 probs = [] # no match 
 for entry in entries:  
  text = ' '.join(entry.datalines)
  k1 = entry.metad['k1']
  if k1 not in k1dict:
   probs.append(entry)
   print('check_entries: k1 not found:',k1)
 return probs

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
 write_recs(fileout,outrecs) # ,blankflag=False)

def check_groups_1(groupd,entries):
 Ldict = digentry.Entry.Ldict;
 nprob = 0
 for groupkey in groupd:
  # groupkey = L1,X1;L2,X2; ...
  group = groupd[groupkey]
  ientries = group.ientries;
  Lk1s = groupkey.split(';')
  if len(ientries) != len(Lk1s):
   print(groupkey)
   print('len(ientries)=%s, len(Lk1s)=%s' %(len(ientries),len(Lk1s)))
   print()
   nprob = nprob + 1
   continue
 print('check_groups_1 finds %s problems' % nprob)

def check_groups_2(groupd,entries):
 nprob = 0
 for groupkey in groupd:
  # groupkey = L1,X1;L2,X2; ...
  group = groupd[groupkey]
  ientries = group.ientries;
  Lk1s = groupkey.split(';')
  #ientries = groupd[groupkey]
  #Lk1s = groupkey.split(';')
  if (len(ientries) != len(Lk1s)):
   print('check_groups_2 error:')
   print('  groupkey=',groupkey)
   print('  ientries=',ientries)
   exit(1)
  Ls = group.Ls
  k1s = group.k1s
  for i,Lk1 in enumerate(Lk1s):
   try:
    (L,k1) = Lk1.split(',')
   except:
    nprob = nprob + 1
    print(groupkey)
    continue
   Ls.append(L)
   k1s.append(k1)
   ientry = ientries[i] ## ok sice ientries and Lk1s have same length
   entry = entries[ientry]
   # check that L,k1 consistent with entry
   L_e = entry.metad['L']
   k1_e = entry.metad['k1']
   if L_e != L:
    nprob = nprob + 1
    print(groupkey)
    #print('L inconsistency')
    continue
   if k1_e != k1:
    nprob = nprob + 1
    print(groupkey)
 print('check_groups_2 finds %s problems' % nprob)

def check_groups_3(groups,entries):
 # for each group, check that the associated entries are sequential
 nprob = 0
 for group in groups:
  groupkey = group.key
  # groupkey = L1,X1;L2,X2; ...
  ientries = group.ientries;
  flag = True
  for i,ientry in enumerate(ientries):
   if i == 0:
    ientrydiff = 0
    #group.ientrydiffs.append(0)
   else:  # i != 0:
    ientry_prev = ientries[i-1]
    ientrydiff = ientry - (ientry_prev + 1) 
    if ientrydiff != 0:
     flag = False
     #break
   group.ientrydiffs.append(ientrydiff)
  group.seqflag = flag
  if not flag:
   nprob = nprob + 1
 print('check_groups_3 finds %s problems' % nprob)
 return nprob

def check_groups_4(groups,entries):
 # for each group, check that the associated entries all have
 # the same body
 nprob = 0
 for group in groups:
  groupkey = group.key
  # groupkey = L1,X1;L2,X2; ...
  ientries = group.ientries;
  flag = True
  body0 = None
  for i,ientry in enumerate(ientries):
   entry = entries[ientry]
   body = ' ' . join(entry.datalines)
   if i == 0:
    body0 = body
   else:  # i != 0:
    if body != body0:
     flag = False
  group.seqflag1 = flag
  if not flag:
   nprob = nprob + 1
 print('check_groups_4 finds %s problems' % nprob)
 return nprob

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
  self.ientrydiffs = []  # updated in check_groups_3
  
def init_groups(entries,option):
 assert option in ('or','and')
 Ldict = digentry.Entry.Ldict;
 regex_raw = r'<info %s="(.*?)"/>' % option
 regex = re.compile(regex_raw)
 groupd = {}
 groups = []
 n = 0
 for ientry,entry in enumerate(entries):
  text = ' '.join(entry.datalines)
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
 print('%s entries matching %s' %(n,regex_raw))
 keys = groupd.keys()
 print('%s groups' % len(keys))
 check_groups_1(groupd,entries)
 check_groups_2(groupd,entries)
 return groups

def write_problems_version1(fileout,groups,entries):
 outarr = []
 icase = 0
 for group in groups:
  if group.seqflag:
   continue
  # group entries not sequential. write the group entries
  icase1 = icase + 1
  outarr.append('* TODO (%03d) %s' % (icase1,group.key))
  for i,ientry in enumerate(group.ientries):
   entry = entries[ientry]
   ientrydiff = group.ientrydiffs[i]
   outarr.append('%s (%02d intervening)' %(entry.metaline,ientrydiff))
   for dataline in entry.datalines:
    outarr.append(dataline)
   outarr.append(entry.lend)
 write_lines(fileout,outarr)

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

def write_entries1(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries1_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs,blankflag=False)
 
def mark_problem_entries_3(groups,entries):
 for entry in entries:
  entry.group = '' # new attribute
 icase = 0
 for group in groups:
  if group.seqflag:
   continue
  # group entries not sequential. 
  icase1 = icase + 1
  icase = icase1
  ientries = group.ientries
  # begin group 
  ientry1 = ientries[0]
  entry1 = entries[ientry1]
  entry1.group = '; BEGIN case %03d: %s'  % (icase1,group.key)
  # estimate the end of group
  ientry2a = ientries[-1]
  if len(ientries) == 2:
   iextra = group.ientrydiffs[-1]
   ientry2 = ientry2a + iextra
  else:
   ientry2 = ientry2a
  entry2 = entries[ientry2]
  entry2.group = '; END case %03d: %s'  % (icase1,group.key)

def mark_problem_entries_4(groups,entries):
 for entry in entries:
  entry.group = '' # new attribute
 icase = 0
 for group in groups:
  if group.seqflag1:
   continue
  # group entries have different bodies 
  icase1 = icase + 1
  icase = icase1
  ientries = group.ientries
  # begin group 
  ientry1 = ientries[0]
  entry1 = entries[ientry1]
  entry1.group = '; BEGIN case %03d: %s'  % (icase1,group.key)
  # the end of group
  ientry2 = ientries[-1]
  entry2 = entries[ientry2]
  entry2.group = '; END case %03d: %s'  % (icase1,group.key)
 
if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # output summary
 entries = digentry.init(filein)
 Ldict = digentry.Entry.Ldict;

 groups = init_groups(entries,option)
 nprob = check_groups_3(groups,entries)
 mark_problem_entries_3(groups,entries)
 write_entries1(fileout,entries)
 exit(0)
 # check that bodies of group entries are identical
 nprob = check_groups_4(groups,entries)
 if nprob != 0:
  mark_problem_entries_4(groups,entries)
  write_entries1(fileout,entries)
 if nprob == 0:
  mark_problem_entries_4(groups,entries)
  write_entries1(fileout,entries)
  exit(0)
 
