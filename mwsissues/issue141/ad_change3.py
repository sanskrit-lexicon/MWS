# coding=utf-8
""" ad_change3.py (revised)
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Change(object):
 def __init__(self,oldmeta,newmeta,lnummeta, oldhead,newhead,lnumhead,comment):
  self.oldmeta = oldmeta
  self.newmeta = newmeta
  self.lnummeta = lnummeta
  self.oldhead = oldhead
  self.newhead = newhead
  self.lnumhead = lnumhead
  self.comment = comment

def make_changes_1(adrecs):
 # add 'changes' attribute to each adrec
 for adrec in adrecs:
  changes = []
  for entry in adrec.entries:
   metaline = entry.metaline
   lnummeta = entry.linenum1
   oldk2 = entry.metad['k2']
   newk2 = oldk2.replace('/','^')
   oldmeta = metaline
   newmeta = oldmeta.replace(oldk2,newk2)
   #
   headline = entry.datalines[0] # first line after meta line
   lnumhead = lnummeta + 1
   oldhead = headline
   newhead = oldhead.replace(oldk2,newk2)
   # maybe oldk2 not a substring of headline.  Mark such with a '**'
   if newhead == oldhead:
    newhead = '**'+oldhead
   comment = adrec.line
   change = Change(oldmeta,newmeta,lnummeta, oldhead,newhead,lnumhead,comment)
   changes.append(change)
  adrec.changes = changes


def write_changes(fileout,adrecs):
 outrecs = []
 # title
 outarr = []
 outarr.append('; **********************************************************')
 outarr.append('; %s' % fileout)
 outarr.append('; **********************************************************')
 outrecs.append(outarr)
 nout = 0  # number of entries to change
 for adrec in adrecs:
  # title for this subsection of changes
  changes = adrec.changes
  nchanges = len(changes)
  nout = nout + nchanges
  outarr = []
  outarr.append('; ----------------------------------------------------------')
  outarr.append('; %s' % adrec.line)
  outarr.append('; %s entries to change' % nchanges)
  outarr.append('; ----------------------------------------------------------')
  outrecs.append(outarr)
  # section for each change
  for change in changes:
   outarr = []
   outarr.append('; ..................................')
   #outarr.append('; %s' % change.comment)
   outarr.append('%s old %s' %(change.lnummeta,change.oldmeta))
   outarr.append('%s new %s' %(change.lnummeta,change.newmeta))
   outarr.append(';')
   #
   outarr.append('%s old %s' %(change.lnumhead,change.oldhead))
   outarr.append(';')
   outarr.append('%s new %s' %(change.lnumhead,change.newhead))
   outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print("changes for %s entries written to %s" %(nout,fileout))

class ADrec:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  self.status,self.k1,self.k2,self.k2pwg,self.pc = line.split('\t')
  self.type = self.status.strip()
  if self.type not in ['+','x']:
   print('ADrec: unknown status')
   print(line)
   exit(1)
  self.k1 = self.k1.strip()
  self.k2 = self.k2.strip()
  self.k2pwg = self.k2pwg.strip()
  
def init_ad(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = [ADrec(x) for x in f if not x.startswith(';')]
 print(len(recs),"accent difference records read from",filein)
 return recs

def init_k1dict(entries):
 d = {}
 for entry in entries:
  k1 = entry.metad['k1']
  if k1 not in d:
   d[k1] = []
  d[k1].append(entry)
 return d

def attach_entries(adrecs1,k1dictmw):
 for adrec in adrecs1:
  k1 = adrec.k1
  adrec.entries = k1dictmw[k1]
  
if __name__=="__main__":
 option = sys.argv[1]
 assert option in ['+','x']
 filein1 = sys.argv[2] # ad1.txt
 filein2 = sys.argv[3] # mw.txt
 fileout = sys.argv[4] # changes.txt
 adrecs = init_ad(filein1)
 adrecs1 = [r for r in adrecs if r.type == option]
 print(len(adrecs1),"records for option",option)
 mwentries = digentry.init(filein2)
 # get k1 dictionary for mwentries
 k1dictmw = init_k1dict(mwentries)
 # attach entries
 attach_entries(adrecs1,k1dictmw)
 if option == 'x':
  make_changes_1(adrecs1) # add changes attribute
  write_changes(fileout,adrecs1)
 else:
  print('main: unknown option')
 
