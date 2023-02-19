# coding=utf-8
""" 
change_1chk.py   Greek text
"""
from __future__ import print_function
import sys, re,codecs
import digentry
import langgroup

def greekinfo(langgroups):
 for i,langgroup in enumerate(langgroups):
  a = []
  for m in re.finditer(r'<lang n="greek">(.*?)</lang>',langgroup.old):
   a.append(m.group(1))
  b = []
  for m in re.finditer(r'<gk>(.*?)</gk>',langgroup.new):
   b.append(m.group(1))
  langgroup.oldgreek = a
  langgroup.newgreek = b
  na = len(a)
  nb = len(b)
  if True:
   if len(a) != len(b):
    print(langgroup.lnum, '# old greek = %s, # new greek = %s' %(len(a),len(b)))

def select(entries):
 nfound = 0
 for entry in entries:
  langgroup = entry.langgroup
  if langgroup == None:
   continue
  langgroup.iline = None
  lnumg = int(langgroup.lnum)
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1 + iline + 1
   if lnum == lnumg:
    langgroup.iline = iline
    c = []
    for m in re.finditer(r'<lang n="greek">(.*?)</lang>',line):
     c.append(m.group(1))
    langgroup.entrygreek = c

def make_outarr(entry):
 outarr = []
 outarr = []
 outarr.append('; ------------------------------------------------------')
 meta = entry.metaline
 meta = re.sub(r'<k2>.*$','',meta)
 langgroup = entry.langgroup
 iline = langgroup.iline
 if iline == None:
  outarr.append('; PROBLEM')
  return outarr
 a = langgroup.oldgreek
 b = langgroup.newgreek
 c = langgroup.entrygreek
 if b == c:
  status = 'OK'
 else:
  status = 'CHK'
 outarr.append('; %s  status=%s' % (meta,status))
 
 na = len(a)
 nb = len(b)
 nc = len(c)
 n = max(na,nb,nc)
 dar = []
 for i in range(n):
  d = ["None","None","None","None","None"]
  if i < na:
   d[0] = a[i]
  if i < nb:
   d[1] = b[i]
  if i < nc:
   d[2] = c[i]
  if (i<na) and (i<nb):
   if a[i] == b[i]:
    d[3] = 'EQ'
   else:
    d[3] = '->'
  if (i<nb) and (i<nc):
   if b[i] == c[i]:
    d[4] = 'EQ'
   else:
    d[4] = '<-'
  dar.append(d)
  
 lnum = entry.linenum1 + iline + 1
 old = entry.datalines[iline]
 new = old
 outarr.append('%s old %s' %(lnum,old))
 outarr.append(';')
 for i in range(n):
  d = dar[i]
  e = []
  e.append(d[0].ljust(10))
  e.append(d[3].ljust(5)) 
  e.append(d[1].ljust(10))
  e.append(d[4].ljust(5))
  e.append(d[2].ljust(10))
  eshow = ' '.join(e)           
  outarr.append('; greek %s %s' %(i+1,eshow))
 outarr.append('%s new %s' %(lnum,new))
 return outarr

def write(fileout,entries):
 outrecs = []
 for entry in entries:
  langgroup = entry.langgroup
  if langgroup == None:
   continue
  outarr = make_outarr(entry)                    
  outrecs.append(outarr)   
 with codecs.open(fileout,"w","utf-8") as f:
  nstat = 0
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
    if 'status=CHK' in out:
     nstat = nstat + 1
 print(len(outrecs),"written to",fileout)
 print(nstat,"records to check")
 
def entrygroups(langgroups,entries):
 ## initialize langgroup attribute for entries
 for entry in entries:
  entry.langgroup = None
 ## assume langgroups sorted by lnum
 nentries = len(entries)
 ientry0 = 0
 for langgroup in langgroups:
  lnum = int(langgroup.lnum)
  ientry = ientry0
  jentry = None
  while ientry < nentries:
   entry = entries[ientry]
   if entry.linenum1 <= lnum <= entry.linenum2:
    entry.langgroup = langgroup
    jentry = ientry
    break
   else:
    ientry = ientry + 1
  if jentry == None:
   print('entrygroups problem at lnum=',lnum)
  else:
   ientry0 = jentry

   
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt
 filein1 = sys.argv[2] # e.g., lang.string.changes.txt
 fileout = sys.argv[3] # prototype change transactions
 # read all the entries of the dictionary.
 entries = digentry.init(filein)
 # read the lang file
 langgroups_all = langgroup.init_langgroups(filein1)
 # consider only the 'msg=Greek' groups
 langgroups = [x for x in langgroups_all if x.msg == 'Greek']
 print(len(langgroups),"Greek")
 greekinfo(langgroups)
 entrygroups(langgroups,entries)
 select(entries)
 write(fileout,entries)
