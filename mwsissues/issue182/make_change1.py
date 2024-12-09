# coding=utf-8
""" make_change1.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_changes(fileout,changes):
 outrecs = []
 for c in changes:
  outarr = []
  outarr.append('; -----------------------------------------------------')
  outarr.append('; %s' %c.metaline)
  for rep in c.replacements:
   #outarr.append('; prevls:%s' % rep.prevls)
   outarr.append('; oldls :%s' % rep.old)
   outarr.append('; newls :%s' % rep.new)
  outarr.append('%s old %s' % (c.lnum,c.oldline))
  outarr.append(';')
  outarr.append('%s new %s' % (c.lnum,c.newline))
  outrecs.append(outarr)
 write_outrecs(fileout,outrecs)

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_outarr(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

class Change:
 def __init__(self,oldline,newline,metaline,replacements,lnum):
  # a -> b
  self.oldline = oldline
  self.newline = newline
  self.lnum = int(lnum)
  self.metaline = metaline
  self.replacements = replacements
  
class Replacement:
 def __init__(self,line):
  self.line = line
  L,k1,lnumstr,old,new = line.split('\t')
  lnum = int(lnumstr)
  self.L = L
  self.k1 = k1
  self.lnum = int(lnumstr)
  self.old = old
  self.new = new
  self.count = 0
  
def init_replacements(filein):
 lines = read_lines(filein)
 reps = []
 d = {}
 ndup = 0
 for line in lines:
  rep = Replacement(line)
  dupkey = (rep.lnum,rep.old)
  if dupkey in d:
   #print('init_replacements skipping duplicate',old)
   ndup = ndup + 1
   continue
  reps.append(rep)
  d[dupkey] = rep
 print(ndup,'duplicates noted')
 print("%s replacements read from %s" %(len(reps),filein))
 return reps,d

def get_newline(lnum,line,drec):
 dbg = (lnum == 114532)
 dbg = False
 if dbg: print('get_newline: %s,%s' %(lnum,line))
 lsarr = re.findall(r'<ls.*?</ls>',line)
 replacements = []
 for ls in lsarr:
  dreckey = (lnum,ls)
  if dreckey not in drec:
   continue
  replacements.append(drec[dreckey])
  drec[dreckey].count = drec[dreckey].count + 1
 if dbg: print('%s replacements' %len(replacements))
 #if dbg: exit(1)
 if replacements == []:
  return line,replacements
 # generate newline
 newline = line
 for rep in replacements:
  old = rep.old
  new = rep.new
  newline = newline.replace(old,new)
 return newline,replacements

def make_changes(entries,repsd):
 #print('enter make_changes',len(entries))
 changes = []
 for ientry,e in enumerate(entries):
  for iline,line in enumerate(e.datalines):
   lnum = e.linenum1 + iline + 1
   #if iline < 10: print('iline=%s, lnum=%s' %(iline,lnum))
   #if lnum == 114532: print('make_changes at lnum=114532')
   newline,replacements = get_newline(lnum,line,repsd)
   if newline == line:
    continue
   metaline = e.metaline
   change = Change(line,newline,metaline,replacements,lnum)
   changes.append(change)
 return changes

def check_reps(reps):
 n = 0 # total count of rep.count
 for rep in reps:
  n = n + rep.count
  if rep.count == 0:
   print('not used:',rep.old)
 print(n,'count of replacements')
 
if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 filein1 = sys.argv[2] # link_expand_?
 fileout = sys.argv[3] # change transactions
 reps,repsd = init_replacements(filein1)
 entries = digentry.init(filein)

 changes = make_changes(entries,repsd)
 print(len(changes),"lines changes")
 check_reps(reps)
 write_changes(fileout,changes)

