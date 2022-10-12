# coding=utf-8
""" ad_change4b.py 
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

def make_changes_0(adrecs):
 # Remove accent in metaline and headline
 ntodo = 0  # number marked with **
 for adrec in adrecs:
  changes = []
  for ientry,entry in enumerate(adrec.entries):
   if ientry == 0:
    comment = adrec.line
   else:
    comment = None
   metaline = entry.metaline
   lnummeta = entry.linenum1
   headline = entry.datalines[0] # first line after meta line
   lnumhead = lnummeta + 1
   oldhead = headline
   oldmeta = metaline
   oldk2str = entry.metad['k2']
   # allow comma-separated list for metaline k2
   oldk2s = oldk2str.split(',')
   flag = False  # true when change to be constructed
   if len(oldk2s) != 1:
    print('make_change_0: error multiple k2:',metaline)
    exit(1)
   accents = re.findall(r'[/\^]',oldk2str)
   if len(accents) == 0:
    oldmeta = ';'+oldmeta
    oldhead = ';'+oldhead
    newmeta = None
    newhead = None
   elif len(accents) != 1:
    print('error multiple accents',metaline)
    exit(1)
   else:
    # For this option, remove the accents
    oldk2 = oldk2s[0]
    newk2 = re.sub(r'[/\^]','',oldk2)
    newmeta = oldmeta.replace(oldk2,newk2)
    #
    if headline.startswith('¦'):
     newhead = None
    else:
     newhead = oldhead.replace(oldk2,newk2)
     if newhead == oldhead:
      newhead = '**' + newhead
      ntodo = ntodo + 1
   change = Change(oldmeta,newmeta,lnummeta,oldhead,newhead,lnumhead,comment)
   changes.append(change)
  adrec.changes = changes

def make_changes_p(adrecs):
 # use pwg k
 ntodo = 0  # number marked with **
 for adrec in adrecs:
  changes = []
  for ientry,entry in enumerate(adrec.entries):
   if ientry == 0:
    comment = adrec.line
   else:
    comment = None
   metaline = entry.metaline
   lnummeta = entry.linenum1
   headline = entry.datalines[0] # first line after meta line
   lnumhead = lnummeta + 1
   oldhead = headline
   oldmeta = metaline
   oldk2str = entry.metad['k2']
   # allow comma-separated list for metaline k2
   oldk2s = oldk2str.split(',')
   flag = False  # true when change to be constructed
   if len(oldk2s) != 1:
    print('make_change_0: error multiple k2:',metaline)
    exit(1)
   accents = re.findall(r'[/\^]',oldk2str)
   if len(accents) == 0:
    oldmeta = ';'+oldmeta
    oldhead = ';'+oldhead
    newmeta = None
    newhead = None
   elif len(accents) != 1:
    print('error multiple accents',metaline)
    exit(1)
   else:
    # For this option, remove the mw accent, then
    # try to insert the pwg accent. Often this may fail.
    k2pwg = adrec.k2pwg
    oldk2 = oldk2s[0]
    # first, remove the accents from oldk2
    newk2 = re.sub(r'[/\^]','',oldk2)
    m = re.search(r'(..)([/\^])',k2pwg)
    if m == None:
     newmeta = '**'+oldmeta
    else:
     preaccent = m.group(1)
     accent = m.group(2)
     preaccentmws = re.findall(preaccent,newk2)
     if len(preaccentmws) != 1:
      newmeta = '**'+oldmeta
     else:
      preaccentmw = preaccentmws[0]
      newk2 = newk2.replace(preaccent,preaccent + accent)
      newmeta = oldmeta.replace(oldk2,newk2)
    #
    if headline.startswith('¦'):
     newhead = None
    else:
     newhead = oldhead.replace(oldk2,newk2)
     if newhead == oldhead:
      newhead = '**' + newhead
      ntodo = ntodo + 1
   change = Change(oldmeta,newmeta,lnummeta,oldhead,newhead,lnumhead,comment)
   changes.append(change)
  adrec.changes = changes

def make_changes_x(adrecs):
 # Prepare prototype changes for metaline and headline
 ntodo = 0  
 for adrec in adrecs:
  changes = []
  for ientry,entry in enumerate(adrec.entries):
   if ientry == 0:
    comment = adrec.line
   else:
    comment = None
   metaline = entry.metaline
   lnummeta = entry.linenum1
   headline = entry.datalines[0] # first line after meta line
   lnumhead = lnummeta + 1
   oldhead = headline
   oldmeta = metaline
   oldk2str = entry.metad['k2']
   # allow comma-separated list for metaline k2
   oldk2s = oldk2str.split(',')
   flag = False  # true when change to be constructed
   accents = re.findall(r'[/\^]',oldk2str)
   if len(accents) == 0:
    oldmeta = ';'+oldmeta
    oldhead = ';'+oldhead
    newmeta = None
    newhead = None
   else:
    newmeta = oldmeta
    if headline.startswith('¦'):
     newhead = None
    else:
     newhead = oldhead
   change = Change(oldmeta,newmeta,lnummeta,oldhead,newhead,lnumhead,comment)
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
   if change.newmeta == None:
    outarr.append('; %s old %s' %(change.lnummeta,change.oldmeta))
    #outarr.append('%s new %s' %(change.lnummeta,change.newmeta))
    outarr.append('; %s old %s' %(change.lnumhead,change.oldhead))
    outrecs.append(outarr)
    continue
   if change.oldmeta.startswith(';'):
    oldmeta = change.oldmeta[1:] # drop the ;
    outarr.append('; %s old %s' %(change.lnummeta,oldmeta))
   else:  
    outarr.append('%s old %s' %(change.lnummeta,change.oldmeta))
    outarr.append('%s new %s' %(change.lnummeta,change.newmeta))
    outarr.append(';')
   if change.newhead == None:
    outarr.append(';%s old %s' %(change.lnumhead,change.oldhead))
    outrecs.append(outarr)
    continue
   if change.newhead.startswith('**'):
    nchk = nchk + 1
    outarr.append(';')
    outarr.append('%s old %s' %(change.lnumhead,change.oldhead))
    outarr.append(';')
    outarr.append('%s new %s' %(change.lnumhead,change.newhead))
    outrecs.append(outarr)
   else:
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
  if self.type not in ['+','x','0','p']:
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
 filein1 = sys.argv[2] # ad4a_rev1
 filein2 = sys.argv[3] # mw.txt
 fileout = sys.argv[4] # changes.txt
 adrecs = init_ad(filein1)
 adrecs1 = [r for r in adrecs if r.status == option ]
 print(len(adrecs1),"adrecs with status",option)
 mwentries = digentry.init(filein2)
 # get k1 dictionary for mwentries
 k1dictmw = init_k1dict(mwentries)
 # attach entries
 attach_entries(adrecs1,k1dictmw)
 
 if option == '0':
  make_changes_0(adrecs1)
 elif option == 'p':
  make_changes_p(adrecs1)
 elif option == 'x':
  make_changes_x(adrecs1)
 else:
  print('unknown option')
  exit(1)
 write_changes(fileout,adrecs1)

