# coding=utf-8
""" ad_change4a1.py 
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

def make_changes_4a0(adrecs):
 # add 'changes' attribute to each adrec
 for adrec in adrecs:
  changes = []
  for entry in adrec.entries:
   metaline = entry.metaline
   lnummeta = entry.linenum1
   oldk2str = entry.metad['k2']
   # allow comma-separated list for metaline k2
   oldk2s = oldk2str.split(',')
   flag = False  # true when change to be constructed
   if len(oldk2s) != 1:
    flag = True
   accents = re.findall(r'[/\^]',oldk2str)
   if len(accents) not in [0,1,2]:
    flag = True
   if not flag:
    continue
   # For this option, all changes will be manual
   oldk2 = oldk2str
   newk2 = oldk2
   oldmeta = metaline
   newmeta = oldmeta.replace(oldk2,newk2)
   #
   headline = entry.datalines[0] # first line after meta line
   lnumhead = lnummeta + 1
   oldhead = headline
   newhead = oldhead.replace(oldk2,newk2)
   # maybe oldk2 not a substring of headline.  Mark such with a '**'
   #if newhead == oldhead:
   # newhead = '**'+oldhead
   comment = adrec.line
   change = Change(oldmeta,newmeta,lnummeta, oldhead,newhead,lnumhead,comment)
   changes.append(change)
  adrec.changes = changes


def make_changes_4a1(adrecs):
 # add 'changes' attribute to each adrec
 ntodo = 0
 for adrec in adrecs:
  changes = []
  for entry in adrec.entries:
   metaline = entry.metaline
   lnummeta = entry.linenum1
   oldk2str = entry.metad['k2']
   # allow comma-separated list for metaline k2
   oldk2s = oldk2str.split(',')
   # but this logic requires only 1 k2
   if len(oldk2s) != 1:
    print('make_changes_1 skipping multiple k2:',oldk2str)
    continue
   oldk2 = oldk2s[0]
   accents = re.findall(r'[/\^]',oldk2)
   if len(accents) in [0,1]:
    # this particular entry has either no accents in k2
    # or 1 accent in k2.
    # in either case, we make no change here
    # the case of 1 accent may require a change, if the accent occurs
    # before a samAsa break. This will be dealt with in another
    # change program. For this program, we skip
    continue
   if len(accents) != 2:
    print('Wrong number of accents',oldk2)
    continue
   if accents[0] != '/':
    print('first accent not udatta',oldk2)
    continue
   # remove FIRST accent.
   newk2 = oldk2.replace(accents[0],'',1) 
   #newk2 = oldk2.replace('/','^')
   #newk2 = oldk2
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
    ntodo = ntodo + 1
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
 nchk = 0  # number requiring further manual work
 for adrec in adrecs:
  # title for this subsection of changes
  changes = adrec.changes
  nchanges = len(changes)
  if nchanges == 0:
   continue # skip output when there are no actual changes
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
   if change.newhead.startswith('**¦'):
    outarr.append(';%s old %s' %(change.lnumhead,change.oldhead))
   else:
    if change.newhead.startswith('**'):
     nchk = nchk + 1
    outarr.append(';')
    outarr.append('%s old %s' %(change.lnumhead,change.oldhead))
    outarr.append(';')
    outarr.append('%s new %s' %(change.lnumhead,change.newhead))
   outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print("changes for %s entries written to %s" %(nout,fileout))
 print('make_changes_4a1:', nchk,'changes marked "**" - manual check required')

class ADrec:
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  self.status,self.k1,self.k2,self.k2pwg,self.pc = line.split('\t')
  self.type = self.status.strip()
  if self.type not in ['+','x','_']:
   print('ADrec: unknown status')
   print(line)
   exit(1)
  self.k1 = self.k1.strip()
  self.k2str = self.k2.strip()  # space-separated list
  self.k2s = self.k2str.split(' ')
  self.k2pwgstr = self.k2pwg.strip()  # space-separated list
  self.k2pwgs = self.k2pwgstr.split(' ')
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

def filter_multi_accent(k2str):
 k2s = k2str.split(' ')
 multi_flag = False
 for k2 in k2s:
  m = re.search(r'[/\^].*[/\^]',k2)
  if m != None:
   multi_flag = True
 return multi_flag
if __name__=="__main__":
 option = sys.argv[1]  
 filein1 = sys.argv[2] # temp_ad4a
 filein2 = sys.argv[3] # mw.txt
 fileout = sys.argv[4] # changes.txt
 adrecs = init_ad(filein1)
 adrecs1 = [r for r in adrecs if filter_multi_accent(r.k2) ]
 print(len(adrecs1),"AD records have multi accents")
 mwentries = digentry.init(filein2)
 # get k1 dictionary for mwentries
 k1dictmw = init_k1dict(mwentries)
 # attach entries
 attach_entries(adrecs1,k1dictmw)
 if option == '4a0':
  make_changes_4a0(adrecs1) # add changes attribute
 elif option == '4a1':
  make_changes_4a1(adrecs1) # add changes attribute
 else:
  print('unknown option')
  exit(1)
 write_changes(fileout,adrecs1)

