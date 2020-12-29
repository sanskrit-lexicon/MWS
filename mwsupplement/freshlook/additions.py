#-*- coding:utf-8 -*-
"""additions.py
 
 
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  #  extra attributes
  self.marked = False # from a filter of markup associated with verbs
  self.verb = None  # value of verb attribute root|genuineroot|pre|gati|nom
  self.parse = None  # string value of parse attribute (for pre/gati
  self.cps  = None  # string value of cp attribute
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

def mark_entries(entries,d):
 nsup = 0
 n1 = 0 # addition: <e>1234
 n1a = 0 # additions with unique k1
 n1b = 0 # additions with non-unique k1
 n2 = 0 # change: <e>1A, etc
 changes = []
 additions = []
 for ientry,entry in enumerate(entries):
  marks = []
  for iline,line in enumerate(entry.datalines):
   m = re.search(r'<info +n="sup"/>',line) # empty element
   if not m:
    continue 
   L = entry.metad['L']
   k1 = entry.metad['k1']
   nsup = nsup + 1
   e = entry.metad['e']  # always there. He
   if e in '1234':
    n1 = n1 + 1
    additions.append(ientry)
    a = d[k1]  # entries with this k1
    if len(a) == 1:
     # this entry is the only one
     n1a = n1a + 1
    else:
     # there are other entries with this headword
     n1b = n1b + 1
   elif re.search(r'^[1-4][A-E]$',e):
    n2 = n2 + 1
    changes.append(ientry)
   else:
    print('unknown e:"%s"'%e,L,k1)
   continue
  if len(marks) > 0:
   entry.marked = True
   entry.verb,entry.cps,entry.parse = marks
 print(nsup,"records marked")
 print(n1,"additions;",n2,"changes")
 print(n1a,"Strict additions", n1b,"other additions")
 return additions

def init_entry_keys(entries):
 # get dictionary by k1
 # d[k1] = list of entry indices whose headword is k1
 d = {}
 for ientry,entry in enumerate(entries):
  k1 = entry.metad['k1']
  if k1 not in d:
   d[k1] = []
  d[k1].append(ientry)
 return d

def get_parent(entries,ientry):
 jentry = ientry
 while True:
  entry = entries[jentry]
  e = entry.metad['e']  # always there. He
  if e in '1234':
   break
  jentry = jentry-1
  if jentry < 0:
   entry = entries[ientry]
   L = entry.metad['L']
   k1 = entry.metad['k1']
   print('get_parent ERROR',ientry,k1,L)
   exit(1)
 return jentry

def analyze(changes,entries,d):
 dparents = {}
 for ichange,change in enumerate(changes):
  ientry0 = change 
  entry0 = entries[ientry0]
  iparent = get_parent(entries,ientry0)
  entry = entries[iparent]
  L0 = entry0.metad['L']
  k0 = entry0.metad['k1']
  Lp = entry.metad['L']
  kp = entry.metad['k1']
  if iparent not in dparents:
   dparents[iparent] = []
  dparents[iparent].append(ichange)
  #print(ichange+1,L0,k0,'<',Lp,kp)
 return dparents

def print_dparents(dparents,changes,entries):
 iparents = sorted(dparents.keys())
 distrib = {}
 for icase,iparent in enumerate(iparents):
  entry = entries[iparent]
  Lp = entry.metad['L']
  kp = entry.metad['k1']
  a = []
  changelist = dparents[iparent]
  nc = len(changelist)
  if nc not in distrib:
   distrib[nc] = 0
  distrib[nc] = distrib[nc] + 1
  for ichange in changelist:
   change = changes[ichange]
   ientry0 = change 
   entry0 = entries[ientry0]
   L0 = entry0.metad['L']
   k0 = entry0.metad['k1']
   a.append('(%s,%s)' %((L0,k0)))
  p = '(%s,%s)' %(Lp,kp)
  b = ' '.join(a)
  out = 'Case %03d: %s > %s'%(icase+1,p,b)
  #print(out)
 print('distribution statistics')
 for nc in sorted(distrib.keys()):
  val = distrib[nc]
  print(nc,'instances with',val,'sup changes of same parent')

def get_children(entries,ientry):
 # return jentry, so 
 # entries[ientry:jentry] contain parent and all children
 # Assume ientry is a parent (e in '1234')
 jentry = ientry
 while True:
  jentry = jentry + 1
  entry = entries[jentry]
  e = entry.metad['e']  # always there. He
  if e in '1234':
   break
 return jentry

def filterCodeFlag(filterCode,a,nkp,entries):
 if filterCode == '0':
  return True
 if filterCode == '1':
  return (nkp == 1)

 if filterCode == '2':
  #return not ((nentries == 1) and (nkp == 1))
  return not (nkp == 1)
 print('filterCodeFlag ERROR: unknown filter code',filterCode)
 exit(1)

 print('filterCodeFlag ERROR: unknown filter code',filterCode)
 exit(1)

def  write_addition_cases(fileout,additions,entries,filterCode,dk):
 outcases = []
 ncase = 0
 parents = []
 for iadd in additions:
  entry = entries[iadd]
  kp = entry.metad['k1']
  kplist = dk[kp]
  a = []
  for ientry in kplist:
   #entryp = entries(ientry)
   #if entryp.metad['e'].not
   iparent = get_parent(entries,ientry)
   if iparent not in a:
    a.append(iparent)
  parents.append((kplist,a))
  if len(kplist) > 1:
   Lp = entry.metad['L']
   #print(iadd,kp,Lp,kplist,a)
 # There are many cases where there is:
 #  a supplement parent with also a supplement child.
 # These have already been considred in the 'changes' analysis.
 # We don't want to include them here.
 parents1 = []
 for icase,x in enumerate(parents):
  kplist,a = x
  for iparent in a:
   iparent1 = get_children(entries,iparent)
   # we know the parent is a supplement record
   if iparent1 == (iparent + 1):
    parents1.append(x)
   continue
   # another test
   childsuppflag = False
   for ientry in range(iparent,iparent1):
    entry = entries[ientry]
    for line in entry.datalines:
     if not re.search(r'<info +n="sup"/>',line):
      continue
     # we have a supplement entry. Is it a child entry
     if (entry.metad['e'] not in '1234'):
      childsuppflag = True
      break # for line
    if childsuppflag:
     continue  # this entry family already considered with changes
    # parent is supplement, but there are no child-supplements
    parents1.append(x)
 # we still have 'duplicates' --- for example
 #  an Hx which is a supplement and an Hy which is not a supplement.
 parents2 = []
 np1 = len(parents1)
 for i1 in range(0,np1):
  x1 = parents1[i1]
  if x1 not in parents2:
   parents2.append(x1)

 print (len(parents),"parents")
 print(len(parents1),"parents1")
 print(len(parents2),"parents2")
 for icase,x in enumerate(parents2):
  kplist,a = x
  nkp = len(kplist)
  flag = filterCodeFlag(filterCode,a,nkp,entries)
  if not flag:
   continue
  ncase = ncase + 1
  outarr = ['; ------------------------------------------------------------']
  #outarr.append('; Case %04d. L=%s, key=%s. %s entries, %s headwords' %(ncase,Lp,kp,nentries,nkp))
  outarr.append('; Case %04d.' %ncase)
  outarr.append('; ------------------------------------------------------------')
  for iparent in a:
   iparent1 = get_children(entries,iparent)
   entry = entries[iparent]
   Lp = entry.metad['L']
   kp = entry.metad['k1']
   nentries = iparent1 - iparent
   outarr.append('; PARENT: %s, %s, %s'%(Lp,kp,nentries))
   for ientry in range(iparent,iparent1):
    entry = entries[ientry]
    metalines = [entry.metaline]
    for line in entry.datalines:
     if re.search(r'<info +n="sup"/>',line):
      metalines = ['; SUPPLEMENT',entry.metaline]
      break
    entrylines = metalines + entry.datalines + [entry.lend]
    outarr = outarr + entrylines
  outcases.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outcases:
   for out in outarr:
    f.write(out+'\n')
 print(ncase,"Cases written to",fileout)

if __name__=="__main__": 
 dictlo = 'mw'
 filterCode = sys.argv[1] # xxx
 filterCodes = ['0','1','2','3','4','8','9']
 if filterCode not in filterCodes:
  print('filterCode Error: known values=',filterCodes)
  exit(1)

 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] #  changes
 entries = init_entries(filein)
 dk = init_entry_keys(entries)
 additions = mark_entries(entries,dk)
 #dparents = analyze(changes,entries,dk)
 #print_dparents(dparents,changes,entries)
 
 write_addition_cases(fileout,additions,entries,filterCode,dk)

