# coding=utf-8
""" 
change_3a.py   etym text in ': Others [Spelling Error]'
"""
from __future__ import print_function
import sys, re,codecs
import digentry
import langgroup

def etyminfo(langgroups):
 for i,langgroup in enumerate(langgroups):
  a = []
  for m in re.finditer(r'<etym>(.*?)</etym>',langgroup.old):
   a.append(m.group(1))
  b = []
  for m in re.finditer(r'<etym>(.*?)</etym>',langgroup.new):
   b.append(m.group(1))
  langgroup.oldetym = a
  langgroup.newetym = b
  na = len(a)
  nb = len(b)
  if True:
   if len(a) != len(b):
    print(langgroup.lnum, '# old etym = %s, # new etym = %s' %(len(a),len(b)))

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
    #for m in re.finditer(r'<etym>(.*?)</etym>',langgroup.old):
    for m in re.finditer(r'<etym>(.*?)</etym>',line):
     c.append(m.group(1))
    langgroup.entryetym = c

def make_new(oldline,newetyms):
 # check same number of <etym>X</etym> in oldline as in newetyms
 oldetyms = re.findall(r'(<etym>.*?</etym>)',oldline)
 if len(newetyms) != len(oldetyms):
  return None  # error condition that caller must handle
 parts = re.split(r'(<etym>.*?</etym>)',oldline)
 newparts = []
 iety = 0
 for part in parts:
  if not part.startswith('<etym>'):
   newpart = part
  else:
   newpart = '<etym>%s</etym>' %newetyms[iety]
   iety = iety + 1
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline

def make_outarr(entry):
 outarr = []
 outarr = []
 outarr.append('; ------------------------------------------------------')
 meta = entry.metaline
 meta = re.sub(r'<k2>.*$','',meta)
 outarr.append('; %s' % meta)
 langgroup = entry.langgroup
 iline = langgroup.iline
 if iline == None:
  outarr.append('; PROBLEM')
  return outarr
 a = langgroup.oldetym
 b = langgroup.newetym
 c = langgroup.entryetym
 na = len(a)
 nb = len(b)
 nc = len(c)
 # only deal with cases with same number of etym items
 if (na!=nb) or (na!=nc):
  outarr.append('; SKIPPED')
  return outarr
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
 new = make_new(old,b)
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
  outarr.append('; etym %s %s' %(i+1,eshow))
 if new == None:
  outarr.append('; PROBLEM')
  new = old
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
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
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
 # consider only the '
 langgroups = [x for x in langgroups_all if x.msg == 'Others'
               and x.comment.startswith('[Spelling Error]')]
 print(len(langgroups),"Others [Spelling Errors]")
 
 etyminfo(langgroups)
 entrygroups(langgroups,entries)
 select(entries)
 write(fileout,entries)
