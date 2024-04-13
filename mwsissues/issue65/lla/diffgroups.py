#-*- coding:utf-8 -*-
""" diffgroups.py
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

def is_rearQ(grouplines):
 if is_simpleQ(grouplines):
  return False
 if is_delQ(grouplines):
  return False
 for line in grouplines:
  if line.startswith(';; matter rearranged'):
   return True
 return False

def get_nondelgroups(groups):
 ans = []
 for grouplines in groups:
  # grouplines is a list of lines
  if not is_delQ(grouplines):
   ans.append(grouplines)
 return ans

def get_langs_from_group(grouplines,src):
 ans = []
 for line in grouplines:
  if not line.startswith(src):
   continue
  id1,lnum1,langstr1 = line.split('\t')
  langs = re.findall(r'<lang>.*?</lang>',langstr1)
  for lang in langs:
   ans.append(lang)
 return ans

def get_groups_diff(groups):
 ans = []
 for grouplines in groups:
  langs_cdsl = get_langs_from_group(grouplines,'(CDSL):')
  langs_ab   = get_langs_from_group(grouplines,'(AB):')
  if langs_cdsl != langs_ab:
   ans.append(grouplines)
 return ans

if __name__=="__main__":
 filein = sys.argv[1] # lla2
 fileout = sys.argv[2] # complex diffs matching option
 lines = read_lines(filein)
 groups = list(get_linegroups(lines))
 print(len(groups),"groups")
 #
 groups1 = get_nondelgroups(groups)
 print(len(groups1),"groups marked as non-deleted (in AB version)")
 #
 groups2 = get_groups_diff(groups1)
 write_recs(fileout,groups2)
 # del_nums = get_cdsl_lnums(groups1)
 # write_lines(fileout1,del_nums)
