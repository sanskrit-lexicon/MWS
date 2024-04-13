#-*- coding:utf-8 -*-
""" deleted_diff.py
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
 print(len(outrecs),"records written to",fileout)
 
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
 grouplines = []
 for iline,line in enumerate(lines):
  grouplines.append(line)
  if line.startswith('='):
   yield grouplines
   grouplines = []
 
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

def get_cdsl_lnums(groups):
 d = {}
 lnums = []
 for grouplines in groups:
  for line in grouplines:
   if not line.startswith('(CDSL):'):
    continue
   id1,lnum1,langstr1 = line.split('\t')
   assert lnum1 not in d
   d[lnum1] = True
   lnums.append(lnum1)
 return lnums

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

def get_lnum_lang(lines):
 ans = []
 for iline,line in enumerate(lines):
  langs = re.findall(r'<lang>.*?</lang>',line)
  if langs == []:
   continue
  lnum = iline + 1
  a = (lnum,langs)
  ans.append(a)
 return ans

def write_tuples(fileout,tuples):
 outarr = []
 for t in tuples:
  lnum,langs = t
  langout = ', '.join(langs)
  lnumout = '%s' % lnum
  tout = ['(CDSL):',lnumout,langout]
  out = '\t'.join(tout)
  outarr.append(out)
 write_lines(fileout,outarr)

def is_simpleQ(grouplines):
 id1,lnum1,langstr1 = grouplines[0].split('\t')
 id2,lnum2,langstr2 = grouplines[1].split('\t')
 if id1 != '(CDSL):':
  return False
 if id2 != '(AB):':
  return False
 if lnum1 != lnum2:
  return False
 for line in grouplines[2:-1]:
  if not line.startswith(';;'):
   return False
  if line.startswith(';; deleted'):
   return False
 # it must be simple!
 return True

def is_delQ(grouplines):
 if is_simpleQ(grouplines):
  return False
 for line in grouplines:
  if line.startswith(';; deleted'):
   return True
 return False

def get_delgroups(groups):
 ans = []
 for grouplines in groups:
  # grouplines is a list of lines
  if is_delQ(grouplines):
   ans.append(grouplines)
 return ans

def get_simplediffs(groups):
 ans = []
 for grouplines in groups:
  id1,lnum1,langstr1 = grouplines[0].split('\t')
  id2,lnum2,langstr2 = grouplines[1].split('\t')
  assert id1 == '(CDSL):'
  assert id2 == '(AB):'
  assert lnum1 == lnum2
  if langstr1 != langstr2:
   ans.append(grouplines)
 return ans

if __name__=="__main__":
 filein = sys.argv[1] # lla2
 fileout = sys.argv[2] # complex diffs matching option
 fileout1 = sys.argv[3] # lnums of deleted
 lines = read_lines(filein)
 groups = list(get_linegroups(lines))
 print(len(groups),"groups")
 #
 groups1 = get_delgroups(groups)
 print(len(groups1),"groups marked as deleted (in AB version)")
 #
 #simplediffs = get_simplediffs(complexgroups)
 #print(len(simplediffs),"")
 #
 write_recs(fileout,groups1)
 del_nums = get_cdsl_lnums(groups1)
 write_lines(fileout1,del_nums)
