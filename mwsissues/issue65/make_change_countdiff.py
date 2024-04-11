#-*- coding:utf-8 -*-
"""make_change_countdiff.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)

def write_recs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for line in outarr:
    f.write(line+'\n')  
 print(len(outrecs),"change records written to",fileout)

class TagDiff:
 def __init__(self,linegroup):
  self.tagline,self.otherlines = linegroup
  self.langtag,count_cdsl,count_ab = self.tagline.split('\t')
  self.count_cdsl = int(count_cdsl)
  self.count_ab   = int(count_ab)
  m = re.search(r'^<lang>(.*?)</lang>$',self.langtag)
  self.abbrev = m.group(1)
  self.chg_line = None
  self.del_line = None
  self.chg_lnums = []
  self.del_lnums = []
  for line in self.otherlines:
   if ('deleted in AB version' in line) and (self.del_line == None):
    self.del_line = line
    self.del_lnums = [int(x) for x in re.findall(r'[0-9]+',self.del_line)]
   elif self.chg_line == None:
    self.chg_line = line
    self.chg_lnums =  [int(x) for x in re.findall(r'[0-9]+',self.chg_line)]
   else:
    print('TagDiff problem')
    print(self.tagline)
    for x in self.otherlines:
     print(x)
    exit(1)
    
def get_linegroups(lines):
 langline = None
 for iline,line in enumerate(lines):
  if line.startswith('<lang>'):
   if iline != 0:
    yield (langline,grouplines)
   langline = line
   grouplines = []
   continue
  if line.startswith(';;'):
   grouplines.append(line)
 yield (langline,grouplines) # last group
 
def init_diffrecs(filein):
 lines = read_lines(filein)
 linegroups = list(get_linegroups(lines))
 print(len(linegroups),"groups found in",filein)
 recs = []
 for linegroup in linegroups:
  rec = TagDiff(linegroup)
  recs.append(rec)
 return recs

class Change:
 def __init__(self,metaline,lnum,line,lnum_recs):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  a = []
  for rec in lnum_recs:
   a.append('; %s' % rec.langtag)
   if rec.chg_line != None:
    b = rec.chg_line
    a.append(b)
   """
   if rec.del_line != None:
    b = rec.del_line
    a.append(b)
   """
  self.comments = a
 
def make_changes(lines,d):
 changes = []
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
  lnum = iline + 1
  if lnum in d:
   lnum_recs = d[lnum]
   change = Change(metaline,lnum,line,lnum_recs)
   changes.append(change)
 return changes

def get_lnums_chg(recs):
 d = {}
 ndup = 0
 lnums = []
 for rec in recs:
  # reclnums = rec.chg_lnums + rec.del_lnums
  reclnums = rec.chg_lnums
  for lnum in reclnums:
   if lnum not in d:
    d[lnum] = []
    lnums.append(lnum)
   else:
    ndup = ndup + 1
   d[lnum].append(rec)
 print(len(lnums),"distinct lnums found, excluding AB deletes")
 print(ndup,"lnums found more than once")
 return d

def get_lnums_del(recs):
 d = {}
 ndup = 0
 lnums = []
 for rec in recs:
  reclnums = rec.del_lnums
  for lnum in reclnums:
   if lnum not in d:
    d[lnum] = []
    lnums.append(lnum)
   else:
    ndup = ndup + 1
   d[lnum].append(rec)
 print(len(lnums),"distinct lnums found from AB deletes")
 print(ndup,"lnums found more than once")
 return d

def write_changes(fileout,changes):
 outrecs = []
 for c in changes:
  outarr = []
  # '*' for org-mode
  outarr.append('* TODO ; %s' % c.metaline)
  for comment in c.comments:
   outarr.append(comment)
  outarr.append('%s old %s' % (c.lnum,c.line))
  outarr.append(';')
  outarr.append('%s new %s' % (c.lnum,c.line))
  outarr.append('; --------------------------------------------------')
  outrecs.append(outarr)
 write_recs(fileout,outrecs)

def write_tags_del(fileout,d):
 outarr = []
 for lnum in d:
  recs_del = d[lnum]
  for rec in recs_del:
   outarr.append('%s %s' %(lnum,rec.langtag))
 write_lines(fileout,outarr)
 print(len(outarr),"items written to",fileout)

def write_lnums_del(fileout,d):
 deletes = d.keys()
 deletes = sorted(deletes)
 outarr = [str(delete) for delete in deletes]
 write_lines(fileout,outarr)

def check_del(d1,d2):
 n = 0
 for lnum in d1:
  if lnum in d2:
   n = n + 1
   print('%s in both chg and del' % lnum)
 print(n,"lnums in both chg and del") # expect n = 0
 
if __name__=="__main__":
 filetagdiff = sys.argv[1]  # 
 filein = sys.argv[2] #  xxx.txt 
 fileout = sys.argv[3] #
 fileout1 = sys.argv[4]
 fileout2 = sys.argv[5]
 diffrecs = init_diffrecs(filetagdiff)
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 lnums_chg_dict = get_lnums_chg(diffrecs)
 changes = make_changes(lines,lnums_chg_dict)
 write_changes(fileout,changes)
 # Handle lines delete in AB version of MW.
 lnums_del_dict = get_lnums_del(diffrecs)
 write_tags_del(fileout1,lnums_del_dict)
 # check the lnums_chg_dict and lnums_del_dict are disjoint re lnum
 check_del(lnums_chg_dict,lnums_del_dict)
 # 04-10-2024  just the lnums AB marked as delete
 write_lnums_del(fileout2,lnums_del_dict)
 
