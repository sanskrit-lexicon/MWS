#-*- coding:utf-8 -*-
"""make_change_deleted.py
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

class Change:
 def __init__(self,metaline,lnum,line,lnum_recs):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.comments = lnum_recs[0:-1] # array of strings

def prev_metaline(lines,iline):
 while iline > 0:
  line = lines[iline]
  if line.startswith('<L>'):
   return line
  iline = iline - 1
 print('prev_metaline not found. iline=',iline)
 exit(1)
 
def make_changes(lines,groups):
 changes = []
 for grouplines in groups:
  for groupline in grouplines:
   if not groupline.startswith('(CDSL):'):
    continue
   id1,lnum1,langstr1 = groupline.split('\t')
   lnum = int(lnum1)
   iline = lnum - 1
   line = lines[iline]
   metaline = prev_metaline(lines,iline)
   lnum_recs = grouplines
   change = Change(metaline,lnum,line,lnum_recs)
   changes.append(change)
 return changes

def write_changes(fileout,changes):
 outrecs = []
 for c in changes:
  outarr = []
  # '*' for org-mode
  outarr.append('* TODO ; %s' % c.metaline)
  for comment in c.comments:
   if not comment.startswith(';'):
    comment = ';' + comment
   outarr.append(comment)
  # In this program, we comment out the changes!
  # editing may reverse a few
  outarr.append('; %s old %s' % (c.lnum,c.line))
  outarr.append(';')
  outarr.append('; %s new %s' % (c.lnum,c.line))
  outarr.append('; --------------------------------------------------')
  outrecs.append(outarr)
 write_recs(fileout,outrecs)

def get_linegroups(lines):
 grouplines = []
 for iline,line in enumerate(lines):
  grouplines.append(line)
  if line.startswith('='):
   yield grouplines
   grouplines = []
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt
 filein1 = sys.argv[2] #  lla2_deletediff.txt
 fileout = sys.argv[3] # change file
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 lines1 = read_lines(filein1)
 groups = list(get_linegroups(lines1))
 print(len(groups),"groups")
 changes = make_changes(lines,groups)
 write_changes(fileout,changes)
