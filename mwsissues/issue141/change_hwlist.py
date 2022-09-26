# coding=utf-8
""" change_hwlist.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

class Change(object):
 def __init__(self,oldmeta,newmeta,lnummeta, oldhead,newhead,lnumhead):
  self.oldmeta = oldmeta
  self.newmeta = newmeta
  self.lnummeta = lnummeta
  self.oldhead = oldhead
  self.newhead = newhead
  self.lnumhead = lnumhead

def make_changes(hwlist,k1dict):
 # 'simple'
 # apply change '/' to '^' in metaline and headline of
 # all entries with given headword.
 ans = []
 for hw in hwlist:
  if hw not in k1dict:
   print('headword not found: "%s"' %hw)
   continue
  hwentries = k1dict[hw]
  hwchanges = []
  for entry in hwentries:
   metaline = entry.metaline
   lnummeta = entry.linenum1
   oldmeta = metaline
   newmeta = oldmeta
   #
   headline = entry.datalines[0] # first line after meta line
   lnumhead = lnummeta + 1
   oldhead = headline
   newhead = oldhead
   change = Change(oldmeta,newmeta,lnummeta, oldhead,newhead,lnumhead)
   hwchanges.append(change)
  ans.append((hw,hwchanges))
 return ans

def write_changes(fileout,hwchanges,hwlist):
 outrecs = []
 # title
 outarr = []
 outarr.append('; **********************************************************')
 outarr.append('; metaline, headline changes for headwords:')
 s = ', '.join(hwlist)
 outarr.append('; %s' % s)
 outarr.append('; **********************************************************')
 outrecs.append(outarr)
 for hw,changes in hwchanges:
  outarr = []
  outarr.append('; ==========================================================')
  outarr.append('; changes for %s: %s entries' % (hw,len(changes)))
  outarr.append('; ==========================================================')
  for change in changes:
   outarr.append('; ----------------------------------------------------------')
   outarr.append('%s old %s' %(change.lnummeta,change.oldmeta))
   outarr.append('%s new %s' %(change.lnummeta,change.newmeta))
   outarr.append(';')
   #
   outarr.append('%s old %s' %(change.lnumhead,change.oldhead))
   outarr.append(';')
   outarr.append('%s new %s' %(change.lnumhead,change.newhead))
  outarr.append(';')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  nout = 0
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
    nout = nout + 1
 print(nout,"change forms written to",fileout)
   
def init_k1dict(entries):
 d = {}
 for entry in entries:
  k1 = entry.metad['k1']
  if k1 not in d:
   d[k1] = []
  d[k1].append(entry)
 return d
 
if __name__=="__main__":
 option = sys.argv[1]
 hwlist = option.split(',')
 print('getting metaline and headline for entries of %s headwords' % len(hwlist))
 filein = sys.argv[2] # mw.txt
 fileout = sys.argv[3] # changes.txt
 entries = digentry.init(filein)
 # get k1 dictionary for entries
 k1dict = init_k1dict(entries)
 hwchanges = make_changes(hwlist,k1dict)
 write_changes(fileout,hwchanges,hwlist)
 
