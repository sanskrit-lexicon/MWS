#-*- coding:utf-8 -*-
"""mw_svarita_missed.py
 
"""
from __future__ import print_function
import sys, re,codecs
import digentry

class Change(object):
 def __init__(self,entry,data2):
  self.entry = entry
  self.data2 = data2
  
def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  entry = change.entry
  data = change.data2
  assert len(data) == 2
  iline1,infos1 = data[0]
  iline2,infos2 = data[1]
  lnum0 = entry.linenum1
  metaline = entry.metaline
  metaline = re.sub(r'<k2>.*$','',metaline)
  line1 = entry.datalines[iline1]
  line2 = entry.datalines[iline2]
  if iline1 != 0:
   print('WRITE ANOMALY', metaline,iline1)
   exit(1)
  # so there is <info> in first line
  info1 = ''.join(infos1)
  info2 = ''.join(infos2)
  if False:
   print(metaline)
   print(line1)
   print(infos1)
   print(info1)
   exit(1)
  m = re.search(r'<info (or|and|orsl)=',info1)
  if m:
   #print('line 1 contains',info1)
   #exit(1)
   # put info2 into line1, and remove from line2
   newline1 = line1 + info2
   newline2 = re.sub(r'<info .*?/>','',line2)
  else:
   # put info1 into line2, and remove from line1 
   newline2 = line2 + info1
   newline1 = re.sub(r'<info .*?/>','',line1)
  # generate the change lines in outarr
  outarr = []
  outarr.append('; =====================================================')
  outarr.append('; %s' % metaline)
  lnum1 = lnum0 + iline1 + 1
  outarr.append('%s old %s' %(lnum1,line1))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum1,newline1))
  outarr.append('; ......................')

  lnum2 = lnum0 + iline2 + 1
  outarr.append('%s old %s' %(lnum2,line2))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum2,newline2))
  outarr.append('; ......................')
  
  outrecs.append(outarr)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for line in outarr:
    f.write(line+'\n')
 print(len(outrecs),"records written to",fileout)

def init_changes(entries):
 changes = []
 n1 = 0
 n2 = 0
 n1a = 0
 for entry in entries:
  metaline = entry.metaline
  lnum0 = entry.linenum1
  data = []
  for iline,line in enumerate(entry.datalines):
   infos = re.findall(r'<info .*?/>',line)
   if infos != []:
    data.append((iline,infos))
  if data == []: # no info statements
   continue
  meta = re.sub(r'<k2>.*$','',metaline)
  ndata = len(data)
  if ndata > 2:
   print(meta,ndata,'more than 2 <info> lines')
   continue
  if ndata == 1:
   n1 = n1 + 1
   iline,infos = data[0]
   if iline == (len(entry.datalines) - 1):
    n1a = n1a + 1
   else:
    print(meta,'info not on last line')
   itemp,infotemps = data[0]
   infotemp = ''.join(infotemps)
   if ('<info orsl=' in infotemp) and (itemp != 0):
    print('orsl anomaly',metaline)
   continue # no further interest
  elif ndata == 2:
   n2 = n2 + 1
   change = Change(entry,data)
   changes.append(change)
  else:
   print('ANOMALY: %s, ndata=%s' %(meta,ndata))
 print(n1,"entries have exactly 1 line with <info")
 print('n1a=',n1a)
 print(n2,"entries have exactly 2 line with <info")
 print(len(changes),'Change records generated')
 return changes

def k2accent(entries,accentname):
 # return subset of entries where k2 appears with accent
 ans = [] # list of entries returned
 regexes = {
  'svarita': r'\^',
  }
 regex = regexes[accentname]
 for entry in entries:
  k2 = entry.metad['k2']
  if re.search(regex,k2):
   ans.append(entry)
 return ans

def init_k1dict(entries):
 d = {}
 for entry in entries:
  k1 = entry.metad['k1']
  if k1 not in d:
   d[k1] = []
  d[k1].append(entry)
 return d

def compare_k2(a,b):
 # a,b are two k2 values.
 # are they the same?
 # start with simple comparison
 return a == b

def confirm_accent(mwentries,k1dictpw):
 for entry in mwentries:
  k1 = entry.metad['k1']
  if k1 not in k1dictpw:
   entry.pwentries = []
  else:
   entry.pwentries = k1dictpw[k1]
   k2 = entry.metad['k2']
   for pwentry in entry.pwentries:
    pwk2 = pwentry.metad['k2']
    pwentry.status = compare_k2(k2,pwk2) # new attribute

def write(fileout,mwentries):
 outrecs = []
 for entry in mwentries:
  pwentries = entry.pwentries  # pw entries with same k1 as entry
  outarr = []
  outarr.append('; ----------------------------------------------------')
  outarr.append(entry.metaline)
  if pwentries == []:
   outarr.append('NONE')
  else:
   for pwentry in pwentries:
    status = pwentry.status
    if status:
     outarr.append('OK:   %s' %pwentry.metaline)
    else:
     outarr.append('TODO: %s' %pwentry.metaline)
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(mwentries),"records written to",fileout)
 
if __name__=="__main__":
 filein1 = sys.argv[1] #  mw digitization
 filein2 = sys.argv[2] #  pwg or pw digitization
 fileout = sys.argv[3] #  metaline for cases to examine.
 mwentries = digentry.init(filein1)
 # re-initialize Ldict from digentry
 digentry.Entry.Ldict = {}
 pwentries = digentry.init(filein2)
 Ldictpw = digentry.Entry.Ldict
 accentname = 'svarita'
 pwentries1 = k2accent(pwentries,accentname)
 print(len(pwentries1),'records in pwentries1')
 exit(1)
 # get k1 dictionary for pwentries
 k1dictpw = init_k1dict(pwentries)
 print(len(mwentries1),'mw entries with',accentname)
 confirm_accent(mwentries1,k1dictpw)
 
 write(fileok,mwentries1)



 
