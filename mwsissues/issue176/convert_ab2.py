#-*- coding:utf-8 -*-
""" convert_ab2.py
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

class LGROUP1:
 def __init__(self,Lbody):
  self.Ls = [Lbody]
  self.entries = []
  self.k2s = []
  self.homs = []
  self.k2homs = []
  self.k2ab = None
  self.newmeta = None
  
def init_Lgroups_cdsl_helper1(k2s,homs):
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
   group = LGROUP1(Lbody)
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
  group.k2homs = init_Lgroups_cdsl_helper1(group.k2s,group.homs)
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
  
 if False: # dbg
  for igroup,group in enumerate(groups):
   if igroup > 5:
    break
   print('groupLs %04d: %s' % (igroup+1,group.Ls))
   print('  newmeta=',group.newmeta)
 return groups

class LGROUP2:
 def __init__(self,entry,ientry):
  self.entry = entry
  self.ientry = ientry
  self.status = False
  meta = entry.metaline
  k2 = entry.metad['k2']
  k2s = k2.split(',')
  if len(k2s) == 1:
   return  # status is False
  text = ' '.join(entry.datalines)
  m = re.search(r'{{(.*?)}}',text)
  if m == None:
   print('LGROUP2 WARNING no {{Ls}} for L=',entry.metad['L'])
   return # status is False
  Ls_txt = m.group(1)
  Ls = Ls_txt.split(',')
  if len(Ls) != len(k2s):
   print('LGROUP2 WARNING no {{Ls}} & k2s mismatch for L=',entry.metad['L'])
   return # status is False
  # Looks ok. entry is a group entry
  self.status = True
  self.Ls_txt = Ls_txt
  self.Ls = Ls
  self.k2s = k2s
  #
  # self.k2s = []
  self.homs = []
  self.k2homs = []
  self.k2ab = None

def init_Lgroups_ab(entries):
 Lgroups = []
 for ientry,entry in enumerate(entries):
  Lgroup = LGROUP2(entry,ientry)
  if Lgroup.status:
   Lgroups.append(Lgroup)
 print('init_groups_ab finds %s Lgroup entries' % len(Lgroups))
 return Lgroups
 
def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs,blankflag=False)
 
def make_entries_ab(entries,Lgroups):
 # LGROUP1 object
 for Lgroup in Lgroups:
  for i,L in enumerate(Lgroup.Ls):
   entry = Lgroup.entries[i]
   entry.group = Lgroup
   if i != 0:
    entry.groupskip = True
    continue
   # revised metaline for first entry in group
   entry.metaline = Lgroup.newmeta
   # if L == '21': print(L,'newmeta=',entry.metaline)
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
   if (icase < 5) and False: # dbg
    print('case %s groupskip=%s: %s' %(icase, entry.groupskip,entry.metaline))
 return newentries


def remove_Ls(datalines):
 ans = []
 for dataline in datalines:
  newdataline = re.sub(r'{{[0-9.,]+}}','',dataline)
  ans.append(newdataline)
 return ans

slp1_chars = "aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh" + "|~L"

def k1chk(k1,chars):
 # return list of characters in k1 but not chars
 # could use sets
 ans = []  
 for c in k1:
  if c not in chars:
   ans.append(c)
 return ans

def k2_k1_one(k2):
 # remove hom, if any
 a1 = re.sub(r'^[0-9]+\. ','',k2)
 # remove accents /,^
 # remove —-  (word parts)
 # remove '  avagraha
 # remove space (once) vAstu—yAga—viDes tattva
 # remove ° (once): bfhad—AraRya°ko/panizad
 k1 = re.sub(r"[/\^—'° -]",'',a1)  
 # check that k1 has no non-slp1 letters
 badchars = k1chk(k1,slp1_chars)
 if len(badchars) != 0:
  print('k2_k1_one:',k2,'has unexpected characters',badchars)
 return k1
 
def k2_to_k1(k2):
 # k2 could have ';' separated values
 k2as = k2.split(';')
 k1s = []
 for i,k2a in enumerate(k2as):
  k1 = k2_k1_one(k2a)
  k1s.append(k1)
  if k1 != k1s[0]:
   print('k2_to_k1: accent variant error',k2)
 # use only the first
 return k1s[0]

def make_entry_recs_cdsl(entries,Lgroups):
 # LGROUP2 object
 d = {}
 for Lgroup in Lgroups:
  entry = Lgroup.entry
  L = entry.metad['L']
  Ls = Lgroup.Ls
  assert Ls[0] == L
  if L in d:
   print('make_entries_cdsl: duplicate L',L)
   exit(1)
  d[L] = Lgroup

 newrecs = []
 icase = 0
 for entry in entries:
  L = entry.metad['L']
  if L not in d:
   # no change
   rec = write_entries_helper(entry)
   newrecs.append(rec)
   continue
  Lgroup = d[L]
  Ls = Lgroup.Ls
  k2s = Lgroup.k2s
  # from LGROUP2 constructor, we know len(Ls) == len(k2s)
  datalines = entry.datalines
  metaline = entry.metaline
  # remove the {{Ls_txt}}  from
  newdatalines = remove_Ls(datalines)
  pc = entry.metad['pc']
  e = entry.metad['e']  # for mw
  k1s = []
  metas = []
  L0 = L
  for i,L in enumerate(Ls):
   k2 = k2s[i]
   k1 = k2_to_k1(k2)
   newmeta = '<L>%s<pc>%s<k1>%s<k2>%s<e>%s' %(L,pc,k1,k2,e)
   k1s.append(k1)
   # construct new rec
   rec = []
   rec.append(newmeta)
   if i == 0:
    for temp in newdatalines:
     rec.append(temp)
   else:
    Lbodyline = '{{Lbody=%s}}' % L0
    rec.append(Lbodyline)
   rec.append('<LEND>')
   newrecs.append(rec)
 return newrecs   
    
if __name__=="__main__":
 option = sys.argv[1]
 assert option in ('cdsl,ab','ab,cdsl')
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # 
 entries = digentry.init(filein)
 Ldict = digentry.Entry.Ldict;

 if option == 'cdsl,ab':
  Lgroups = init_Lgroups_cdsl(entries)
  entries_ab = make_entries_ab(entries,Lgroups)
  write_entries(fileout,entries_ab)
  print(len(entries_ab),'new entries written to',fileout)
  exit(1)
 if option == 'ab,cdsl':
  Lgroups = init_Lgroups_ab(entries)
  newrecs = make_entry_recs_cdsl(entries,Lgroups)
  write_recs(fileout,newrecs,blankflag=False)
  print(len(newrecs),'entry records written to',fileout)
  exit(1)
