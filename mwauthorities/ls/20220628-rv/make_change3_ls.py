#-*- coding:utf-8 -*-
"""make_change2_ls.py
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
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
  self.lsarr = []
  
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

class Change(object):
 def __init__(self,metaline,lnum,old,new):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new

def make_number_change(lsold,lsabbr,n1,n2):
 # 1)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+,) ([0-9]+[.]?)</ls>$',lsold)
 if m:
  a1 = m.group(1)
  a2 = m.group(2)
  a3 = m.group(3)
  lsnew = '<ls n="%s">%s %s %s</ls>' %(lsabbr,a1,a2,a3)
  return lsnew
 # 2)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>$',lsold)
 if m:
  a1 = m.group(1)
  a2 = m.group(2)
  a3 = m.group(3)
  a4 = m.group(4)
  lsnew = '<ls n="%s">%s %s %s %s</ls>' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 3)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+[.]?)</ls>$',lsold)
 if m:
  a1 = n1 
  a2 = m.group(1)
  a3 = m.group(2)
  lsnew = '<ls n="%s %s,">%s %s</ls>' %(lsabbr,a1,a2,a3)
  return lsnew
 # 3a)
 m = re.search(r'^<ls>([0-9]+[.]?)</ls>$',lsold)
 if m:
  a1 = n1
  a2 = n2
  assert (n1 != None) and (n2 != None)
  a3 = m.group(1)
  lsnew = '<ls n="%s %s, %s,">%s</ls>' %(lsabbr,a1,a2,a3)
  return lsnew
 # 3b)
 m = re.search(r'^<ls>([0-9]+[.]?) ((fgg?\.)|(v\. l\.))</ls>$',lsold)
 if m:
  a1 = n1
  a2 = n2
  assert (n1 != None) and (n2 != None)
  a3 = m.group(1) 
  a4 = m.group(2) # ((fgg?\.)|(v\. l\.))
  lsnew = '<ls n="%s %s, %s,">%s %s</ls>' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 4)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>$',lsold)
 if m:
  a1 = n1
  a2 = m.group(1)
  a3 = m.group(2)
  a4 = m.group(3) # ((fgg?\.)|(v\. l\.))
  lsnew = '<ls n="%s %s,">%s %s %s</ls>' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 5)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+,) ([0-9]+[.]) ([0-9].*$)',lsold)
 if m:
  a1 = m.group(1)
  a2 = m.group(2)
  a3 = m.group(3)
  a4 = m.group(4)
  lsnew = '<ls n="%s">%s %s %s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 6)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+[.]) ([0-9].*$)',lsold)
 if m:
  a1 = n1
  assert n1 != None
  a2 = m.group(1)
  a3 = m.group(2)
  a4 = m.group(3)
  lsnew = '<ls n="%s %s,">%s %s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 7)
 m = re.search(r'^<ls>([0-9]+[.]) ([0-9].*$)',lsold)
 if m:
  a1 = n1
  a2 = n2
  assert (n1 != None) and (n2 != None)
  a3 = m.group(1)
  a4 = m.group(2)
  lsnew = '<ls n="%s %s, %s,">%s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4)
  return lsnew
 # 8)
 m = re.search(r'^<ls>([0-9]+[.]) ((fgg?\.)|(v\. l\.)) ([0-9].*$)',lsold)
 if m:
  a1 = n1
  a2 = n2
  a3 = m.group(1)
  a4 = m.group(2) # groups 3,4 are the subgroups (fgg?\.) and (v\. l\.)
  a5 = m.group(5) # ([0-9].*$)
  if False:
   print('lsold=',lsold)
   for i in [1,2,3,4,5]:
    print('m.group(%s)=%s' %(i,m.group(i)))
   exit(1)
  lsnew = '<ls n="%s %s, %s,">%s %s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4,a5)
  return lsnew
 # 9)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.)) ([0-9].*$)',lsold)
 if m:
  a1 = n1
  a2 = m.group(1)
  a3 = m.group(2)
  a4 = m.group(3) # ((fgg?\.)|(v\. l\.))
  a5 = m.group(6) # ([0-9].*$)
  lsnew = '<ls n="%s %s,">%s %s %s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4,a5)
  return lsnew
 # 10)
 m = re.search(r'^<ls>([0-9]+,) ([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.)) ([0-9].*$)',lsold)
 if m:
  a1 = m.group(1)
  a2 = m.group(2)
  a3 = m.group(3)
  a4 = m.group(4)  # ((fgg?\.)|(v\. l\.))
  # group 5 : (fgg?\.)
  # group 6 : (fgg?\.)
  a5 = m.group(7)  # ([0-9].*$)
  lsnew = '<ls n="%s">%s %s %s %s</ls> <ls>%s' %(lsabbr,a1,a2,a3,a4,a5)
  return lsnew
 return None

def write_debug(lnum,metaline,prevls,lsold,line):
 # generate message to fdbg output
 metaline1 = re.sub(r'<k2>.*$','',metaline)
 #metaline1 = '%s   %s' %(prevls,metaline1)
 outarr = []
 outarr.append('; ---------------------------')
 outarr.append('; %s' %metaline1)
 outarr.append('; prev = %s' % prevls)
 outarr.append('; todo = %s' % lsold)
 outarr.append('%s old %s' %(lnum,line))
 outarr.append(';')
 outarr.append('%s new %s' %(lnum,line))
 for out in outarr:
  fdbg.write(out+'\n')
  
def generate_changes(entries,lsabbr):
 # works for LS whose citations take 3 parameters
 # nmiss = number of candidate changes that make_number_change
 #         did not handle
 nmiss = 0
 # ndefer = number of additional changes on a line that are deferred
 #          since we only make 1 change per line
 ndefer = 0
 regexes = [
  r'<ls>%s ([0-9]+), ([0-9]+), ([0-9]+)' %lsabbr,
  r'<ls n="%s">([0-9]+), ([0-9]+), ([0-9]+)' %lsabbr,
  r'<ls n="%s ([0-9]+),">([0-9]+), ([0-9]+)' %lsabbr,
  r'<ls n="%s ([0-9]+), ([0-9]+),">([0-9]+)' %lsabbr,
  ]
 for entry in entries:
  metaline = entry.metaline
  prevlsname = None
  n1 = None
  n2 = None
  prevls = None
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1+iline+1
   linechanged = False  # to control only one change per line
   # iterate over every possible ls
   for m in re.finditer(r'<ls(.*?)>(.*?)</ls>',line):
    lsold = m.group(0)
    attrib = m.group(1)
    data = m.group(2)
    isnumeric = (attrib == '') and re.search(r'^[0-9]',data)
    if isnumeric:
     
     if prevls == None:  # isnumeric case 1
      # there is no previous matching ls to generate a change
      continue
     # Try to generate a change to this numeric ls
     lsnew = make_number_change(lsold,lsabbr,n1,n2)
     if False: # dbg
      if lsold =='<ls>3, 29, 13. 1, 140, 8.</ls>':
       print("dbg: lsold = '%s',  n1=%s,n2=%s, lsnew='%s'" %(lsold,n1,n2,lsnew))
     if lsnew == None:  # isnumeric case 2
      # our change logic fails for this case.
      # write a message to debug file
      write_debug(lnum,metaline,prevls,lsold,line)
      # and increment nmiss
      nmiss = nmiss + 1
      continue # with next finditer
     if linechanged:  # isnumeric case 3
      ndefer = ndefer + 1
      continue # with next finditer
     # isnumeric case 4
     # lsnew != None and linechanged == False
     #   Yield a change and update linechanged
     newline = line.replace(lsold,lsnew)
     metaline1 = re.sub(r'<k2>.*$','',metaline)
     metaline1 = '%s   %s' %(prevls,metaline1)
     change = Change(metaline1,lnum,line,newline)
     yield change
     linechanged = True
     continue # with next finditer
    # END OF isnumeric
    # Deal with nonnumeric
    # Reset prevls parameters
    # three cases
    # <ls>MBH. n1, n2
    # <ls n="MBH.">n1, n2
    # <ls n="MBH. n1,">n2
    prevlsname = None
    prevls = None
    n1 = None
    for regex in regexes:
     m1 = re.search(regex,lsold)
     if m1 != None:
      prevlsname = lsabbr
      n1 = m1.group(1)
      n2 = m1.group(2)
      prevls = lsold
      break # for regex
    # end of code within finditer
   # fall through to next finditer
  # fall through to next line in entry
 print(nmiss,'changes not yet done. See',filedbg)
 print(ndefer,'changes deferred')

def write_changes(fileout,changes):
 outrecs = []
 for change in changes:
  outarr = []
  outarr.append('; -------------------------------------')
  outarr.append('; ' + change.metaline)
  outarr.append('%s old %s' %(change.lnum,change.old))
  outarr.append('; ')
  outarr.append('%s new %s' %(change.lnum,change.new))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

if __name__=="__main__":
 lsabbr = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[3] # change_X
 filedbg = 'tempdbg.txt'
 fdbg = codecs.open(filedbg,"w","utf-8")
 entries = init_entries(filein)
 changes = generate_changes(entries,lsabbr)
 write_changes(fileout,changes)
