#-*- coding:utf-8 -*-
""" revise_lla.py
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

def write_groups(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for line in outarr:
    f.write(line+'\n')  
 print(len(outrecs),"group records written to",fileout)

def get_linegroups(lines):
 grouplines = []
 for iline,line in enumerate(lines):
  grouplines.append(line)
  if line.startswith('='):
   yield grouplines
   grouplines = []
 
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

def unused_revise_lla(groups,tuples):
 # new
 groups_revised = []
 for igroup,grouplines in enumerate(groups):
  tuple = tuples[igroup]
  lnum,langs_revised = tuple
  langstr_revised = ', '.join(langs_revised)
  id1,lnum1,langstr1 = grouplines[0].split('\t')
  if str(lnum) != lnum1:
   print('ERROR: lnum=%s, lnum1=%s' %(lnum,lnum1))
   print(langstr_revised)
   print(langstr1)
   exit(1)
  assert id1 == '(CDSL):'
  new_groupline = '\t'.join([id1,lnum1,langstr_revised])
  grouplines_revised = []
  for i,groupline in enumerate(grouplines):
   if i == 0:
    grouplines_revised.append(new_groupline)
   else:
    grouplines_revised.append(grouplines[i])
  groups_revised.append(grouplines_revised)
 return groups_revised

def revise_lla(lines,tuples):
 dtuple = {}
 for t in tuples:
  lnum,langs_revised = t
  lnumstr = str(lnum)
  dtuple[lnumstr] = t
 #
 newlines = []
 lnum_prev = 0
 for line in lines:
  if not line.startswith('(CDSL):'):
   newlines.append(line)
   continue
  id1,lnum1,langstr1 = line.split('\t')
  if lnum1 not in dtuple:
   langstr_revised = '----------'  # ref lla1, 63845
   lnum = int(lnum1)
  else:
   tuple = dtuple[lnum1]
   lnum,langs_revised = tuple
   langstr_revised = ', '.join(langs_revised)
  assert id1 == '(CDSL):'
  if str(lnum) != lnum1:
   print('ERROR: lnum=%s, lnum1=%s' %(lnum,lnum1))
   print(langstr_revised)
   print(langstr1)
   exit(1)
  newline = '\t'.join([id1,lnum1,langstr_revised])
  newlines.append(newline)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt
 filein1 = sys.argv[2] # llaX.txt
 fileout = sys.argv[3] # llaY.txt
 lines = read_lines(filein) # xxx.txt
 print(len(lines),"read from",filein)
 lines1 = read_lines(filein1)
 print(len(lines1),"read from",filein1)
 # groups = list(get_linegroups(lines1))
 # print(len(groups),"groups")
 tuples = get_lnum_lang(lines)
 lines2 = revise_lla(lines1,tuples)
 write_lines(fileout,lines2)

