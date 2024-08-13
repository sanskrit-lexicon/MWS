#-*- coding:utf-8 -*-
""" dumpgroups_div.py
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
 return groups

def write_groups(fileout,groups,entries):
 for entry in entries:
  entry.group = '' # new attribute
 outrecs = []
 icase = 0
 for igroup,group in enumerate(groups):
  ientries = group.ientries
  ientry0 = ientries[0]
  entry0 = entries[ientry0] # first entry
  # consider only those groups with '<div n="P"/>'
  text = ' '.join(entry0.datalines)
  if not '<div n="P"/>' in text:
   continue  # skip this group
  icase = icase + 1
  outarr = []
  outarr.append('; **********************************************')
  outarr.append('; and/or group with divs %04d: %s'  % (icase,group.key))
  outarr.append('; **********************************************')
  # write entry0
  outarr.append(entry0.metaline)
  for iline,line in enumerate(entry0.datalines):
   if (iline == 0) and ('<div n="P"/>' not in line):
    line = re.sub(r'¦.*$', '¦ ...',line)
   elif (iline == 0):
    pass
   elif ('<div n="P"/>' not in line):
    continue
   # output the line
   outarr.append(line)
  outarr.append(entry0.lend)
  # a spacing line
  outarr.append(';')
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)


if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # output with errors marked.
 entries = digentry.init(filein)
 groups = init_groups(entries) # get both or/and
 write_groups(fileout,groups,entries)

