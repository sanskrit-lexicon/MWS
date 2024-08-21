#-*- coding:utf-8 -*-
""" remove_tru_hui.py
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

class LGROUP:
 def __init__(self,Lbody):
  self.Ls = [Lbody]
  self.entries = []
  self.k2s = []
  self.homs = []
  self.k2homs = []
  self.k2ab = None
  self.newmeta = None
  
def get_k2homs(k2s,homs):
 arr = []
 for i,k2 in enumerate(k2s):
  hom = homs[i]
  if hom == None:
   x = k2
   arr.append(x)
   continue
  x = '%s. %s' %(hom,k2)
  arr.append(x)
 return arr

def init_Lgroups_cdsl(entries):
 ientries_lbody = []
 n = 0
 for ientry,entry in enumerate(entries):
  text = ' '.join(entry.datalines)
  m = re.search(r'{{Lbody=(.*?)}}',text)
  if m != None:
   Lbody = m.group(1)
   ientries_lbody.append((ientry,Lbody))
 print('init_groups_cdsl finds %s Lbody entries' % len(ientries_lbody))
 #
 groupsd = {}
 groups = []
 for i,temp in enumerate(ientries_lbody):
  ientry,Lbody = temp
  if Lbody not in groupsd:
   group = LGROUP(Lbody)
   groups.append(group)
   groupsd[Lbody] = group
  group = groupsd[Lbody]
  entry = entries[ientry]
  L = entry.metad['L']
  group.Ls.append(L)
 #
 # compute additional attributes of Lgroup objects
 for group in groups:
  for L in group.Ls:
   entry = digentry.Entry.Ldict[L]
   group.entries.append(entry)
   k2 = entry.metad['k2']
   group.k2s.append(k2)
   if 'h' in entry.metad:
    hom = entry.metad['h']
    m = re.search(r'^[0-9]+$',hom)
    if not m:  # non-numeric hom!
     print('WARNING: non-numeric hom: metaline=\n%s' % entry.metaline)
   else:
    hom = None
   group.homs.append(hom)
  # generate revised k2
  group.k2homs = get_k2homs(group.k2s,group.homs)
  group.k2ab = ','.join(group.k2homs)
  # new metaline
  entry0 = group.entries[0]
  meta = entry0.metaline
  metad = entry0.metad
  if 'e' in metad: # mw
   eval = metad['e']
   newe = '<e>%s' % eval
  else:
   newe = ''
  meta1 = re.sub(r'<k2>.*$','',meta)  # so L,pc,k1 remain in meta1
  newk2 = group.k2ab
  meta2 = '%s<k2>%s%s' %(meta1,newk2,newe)  #
  group.newmeta = meta2
  
 if True: # dbg
  for igroup,group in enumerate(groups):
   if igroup > 5:
    break
   print('groupLs %04d: %s' % (igroup+1,group.Ls))
   print('  newmeta=',group.newmeta)
 return groups

def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs,blankflag=False)
 
def make_entries_ab(entries,Lgroups):
 for Lgroup in Lgroups:
  for i,L in enumerate(Lgroup.Ls):
   entry = Lgroup.entries[i]
   entry.group = Lgroup
   if i != 0:
    entry.groupskip = True
    continue
   # revised metaline for first entry in group
   entry.metaline = Lgroup.newmeta
   if L == '21': print(L,'newmeta=',entry.metaline)
   # extra
   Ls = ','.join(Lgroup.Ls)
   datalines = entry.datalines
   lastline = datalines[-1]
   Ls1 = '{{%s}}' % Ls
   lastline = lastline + Ls1
   datalines[-1] = lastline
   
 newentries = []
 icase = 0
 for entry in entries:
  if not(hasattr(entry,'groupskip')):
   newentries.append(entry)
  else:
   icase = icase + 1
   if icase < 5:
    print('case %s groupskip=%s: %s' %(icase, entry.groupskip,entry.metaline))
 return newentries

def change_lines(lines):
 newlines = []
 nchange = 0
 # the initial 'x' is temporary markup in temp_mw_9.txt
 regex_raw = r'<x?info hui="([0-9]+)"/>'
 regex = re.compile(regex_raw)
 for line in lines:
  newline = re.sub(regex,'',line)
  newlines.append(newline)
  if newline != line:
   nchange = nchange + 1
 print('change_line: %s lines changed' % nchange)
 return newlines
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # revised xxx/
 lines = read_lines(filein)
 newlines = change_lines(lines)
 write_lines(fileout,newlines)

