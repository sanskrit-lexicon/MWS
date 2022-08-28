#-*- coding:utf-8 -*-
"""make_change_info.py
 
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

if __name__=="__main__":
 filein = sys.argv[1] #  digitization
 fileout = sys.argv[2] # change file
 entries = digentry.init(filein)
 changes = init_changes(entries)
 #
 write_changes(fileout,changes)



 
