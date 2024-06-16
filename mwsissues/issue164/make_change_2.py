#-*- coding:utf-8 -*-
"""change1a.py 
 
"""
from __future__ import print_function
import sys, re,codecs
import digentry
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec canno t encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,iline,old,new):
  self.iline = iline
  self.old = old
  self.new = new

def change6(line):
 # Compar. exclude occcurrences in <ab>X</ab>,
 parts = re.split(r'(<ab>.*?</ab>)|(Compar[.])',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'Compar.':
   newpart = '<ab>Compar.</ab>'
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   

def change5(line):
 # Comm. exclude occcurrences in <ab>X</ab>,
 parts = re.split(r'(<ab>.*?</ab>)|(Comm[.])',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'Comm.':
   newpart = '<ab>Comm.</ab>'
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   

def change4(line):
 # Cf. exclude occcurrences in <ab>X</ab>,
 parts = re.split(r'(<ab>.*?</ab>)|(Cf[.])',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'Cf.':
   newpart = '<ab>Cf.</ab>'
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   

def change3(line):
 # Caus. exclude occcurrences in <ab>X</ab>,
 parts = re.split(r'(<ab>.*?</ab>)|(Caus[.])',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'Caus.':
   newpart = '<ab>Caus.</ab>'
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   


def change2(line):
 # A.D exclude occcurrences in <ab>X</ab>, 'A°</ab>'
 parts = re.split(r'(<ab>.*?</ab>)|(A[.]D[.])|(A[.]D.)',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part == 'A.D.':
   newpart = '<ab>A.D.</ab>'
  elif part.startswith('A.D'):
   newpart = '<ab>A.D.</ab>**'  # ** needs to be checked
  elif part.startswith('<ab>'):
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   

def change1(line):
 # A°  exclude occcurrences in <s>X</s>, 'A°</ab>'
 parts = re.split(r'(<s>.*?</s>)|(A°</ab>)|(A°)',line)
 newparts = []
 for part in parts:
  if part == 'A°':
   newpart = '** %s **'%part
  elif part == None:
   continue
  elif part.startswith('<s>'):
   newpart = part
  elif part == 'A°</ab>':
   newpart = part
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline   

def change_director(option):
 fname = 'change'+option
 if fname in globals(): #locals():
  fun = globals()[fname]
  return fun
 else:
  print('ERROR: no function ',fname)
  exit(1)

def change_2(line):
 def f(m):
  sold = m.group(0)
  a,v,b = m.group(1),m.group(2),m.group(3)
  if v in 'aiufeo':
   w = v.upper()
  else:
   w = v.lower()
  snew1 = '<s>%s%s%s</s>' % (a,v,b)
  snew2 = '<s>%s%s%s</s>' % (a,w,b)
  snew = '%s or %s' %(snew1,snew2)
  #ans = '[[%s--]]%s' % (sold,snew) # [[x]] for debuggin
  ans = snew
  return ans
 def g(m):
  sall = m.group(0)
  ans = re.sub(r'<s>(.*?)([aAiIuUfFeEoO])<shortlong/>(.*?)</s>',f,sall)
  return ans
 newline = re.sub(r'<s>.*?</s>',g,line)
 return newline

def init_entry_changes(entry):
 changes = [] # array of Change objects
 for iline,line in enumerate(entry.datalines):
  newline = change_2(line)
  if newline == line:
   continue
  change = Change(iline,line,newline)
  changes.append(change)
 return changes

def change_entry_out(entry):
 outarr = []
 if entry.changes == []:
  return outarr
 metaline = entry.metaline
 linenum1 = entry.linenum1
 outarr.append('; **************************************************')
 outarr.append('; %s' % metaline)
 for ichange,change in enumerate(entry.changes):
  iline = change.iline
  old = change.old
  new = change
  lnum = linenum1 + iline + 1
  outarr.append('%s old %s' % (lnum,change.old))
  outarr.append(';')
  outarr.append('%s new %s' % (lnum,change.new))
  outarr.append('; --------------------------------------------------')
 return outarr

def write_changes(fileout,entries):
 outrecs = []
 for entry in entries:
  outarr = change_entry_out(entry)
  if outarr != []:
   outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs)," changes written to",fileout)


if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # change transactions
 n = 0
 entries = digentry.init(filein)
 for entry in entries:
  entry.changes = init_entry_changes(entry)
 write_changes(fileout,entries)

