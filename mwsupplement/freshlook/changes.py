#-*- coding:utf-8 -*-
"""changes.py
 
 
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
 def is_supplement(self):
  for iline,line in enumerate(self.datalines):
   if re.search(r'<info +n="sup"/>',line):
    return True
  return False

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
 return changes

def mwtextform(line):
 x = re.sub(r'<ls[^>]*>.*?</ls>',' ',line)
 x = re.sub(r'<lang[^>]*>.*?</lang>',' ',x)
 x = re.sub(r'<s>(.*?)</s>',r'{@\1@}',x)
 parts = re.split(r'<.*?>',x)
 newparts = []
 for part in parts:
  if part.startswith('<'):
   newparts.append(' ')
  else:
   newparts.append(part)
 newline = ''.join(newparts)
 newline = newline.replace('&c.',' ')
 newline = re.sub(r'; +;',';',newline)
 newline = re.sub(r' +',' ',newline)
 newline = newline.strip()
 return newline

def write(fileout,entries):
 n = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for entry in entries:
   if not entry.marked:
    continue
   if entry.verb not in ['root','genuineroot','nom']:
    continue
   n = n + 1
   L = entry.metad['L']
   k1 = entry.metad['k1']
   """
   out = '%s,%s'%(k1,s)
   
   outarr = []
   outarr.append(k1)
   outarr.append(L)
   #out = '%s:%s' %(k1,L)
   #outarr.append(outarr)
   outarr.append(entry.verb)
   outarr.append(entry.cps)
   outarr.append(entry.parse)
   out = ':'.join(outarr)
   """
   outarr = []
   for iline,line in enumerate(entry.datalines):
    if iline == 0:
     x,y = line.split('¦')
     x = re.sub(r'<s>.*?</s>',' ',x)
     line = x+y
    line1 = mwtextform(line)
    if line1 != '':
     outarr.append(line1)
   out = ' '.join(outarr)
   out = re.sub(r' +',' ',out)
   out = '{@%s@},%s:%s'%(k1,L,out)
   f.write(out + '\n')
   #for out in outarr:
   # f.write(out + '\n')
 print(n,"records written to",fileout)

def init_entry_keys(entries):
 # get dictionary by k1
 # d[k1] = list of entries whose headword is k1
 d = {}
 for entry in entries:
  k1 = entry.metad['k1']
  if k1 not in d:
   d[k1] = []
  d[k1].append(entry)
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

def filterCodeFlag(filterCode,nentries,nchanges):
 if filterCode == '0':
  return True
 if filterCode == '1':
  return (nentries == nchanges)
  #return (nentries == 2) and (nchanges == 2)

 if filterCode == '2':
  return (nentries == 2) and (nchanges == 1)
 if filterCode == '3':
  return (nentries == 3) and (nentries != nchanges)
 if filterCode == '4':
  return (nentries == 4) and (nentries != nchanges)
 if filterCode == '8':
  return (nentries > 4) and (nchanges == 1)
 if filterCode == '9':
  return (nentries > 4) and (nchanges > 1) and (nentries != nchanges)
 print('filterCodeFlag ERROR: unknown filter code',filterCode)
 exit(1)

def  write_change_cases(fileout,dparents,changes,entries,filterCode):
 iparents = sorted(dparents.keys())
 outcases = []
 ncase = 0
 for icase,iparent in enumerate(iparents):
  iparent1 = get_children(entries,iparent)
  entry = entries[iparent]
  Lp = entry.metad['L']
  kp = entry.metad['k1']
  nentries = iparent1 - iparent
  changelist = dparents[iparent]
  nchanges = len(changelist)
  if entry.is_supplement():  # parent is supplement
   nchanges = nchanges + 1
  flag = filterCodeFlag(filterCode,nentries,nchanges)
  if not flag:
   continue
  ncase = ncase + 1
  outarr = ['; ------------------------------------------------------------']
  outarr.append('; Case %04d. L=%s, key=%s. %s entries, %s supplement entries' %(ncase,Lp,kp,nentries,nchanges))
  outarr.append('; ------------------------------------------------------------')
  for ientry in range(iparent,iparent1):
   #for ichange in changelist:
   # change = changes[ichange]
   # ientry0 = change 
   entry = entries[ientry]
   metalines = [entry.metaline]
   # could have metaline not in changes
   suppflag = False
   for line in entry.datalines:
    if re.search(r'<info +n="sup"/>',line):
     suppflag = True
     break
   if suppflag:
    metalines = ['; SUPPLEMENT',entry.metaline]
    #metalines = ['%s  ; %s' %(entry.metaline,'SUPPLEMENT')]
    #metaline = '%s  ; %s' %(metaline,'SUPPLEMENT')
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
 changes = mark_entries(entries,dk)
 dparents = analyze(changes,entries,dk)
 print_dparents(dparents,changes,entries)
 
 write_change_cases(fileout,dparents,changes,entries,filterCode)

