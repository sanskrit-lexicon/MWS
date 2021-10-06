#-*- coding:utf-8 -*-
"""change1b.py change transactions for those lines containing one of
   several strings read at run time.
 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec canno t encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason

def init_changes(lines,stringrecs):
 changes = [] # array of Change objects
 metaline = None
 page = None
 for iline,line in enumerate(lines):
  line = line.rstrip('\r\n')
  if line.startswith('<L>'):
   metaline = line
   continue
  if line == '<LEND>':
   metaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  found = False
  for rec in stringrecs:
   if rec.string in line:
    found = True
    break
  if not found:
   continue
  rec.count = rec.count + 1
  oldline = line
  newline = oldline
  reason = None
  change = Change(metaline,page,iline,oldline,newline,reason)
  changes.append(change)
 print(len(changes),'potential changes found')
 return changes

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 ident = change.metaline
 if ident == None:
  ident = change.page
 if ident == None:
  ident = 'None'
 outarr.append('; ' + ident)
 lnum = change.iline + 1
 outarr.append('%s old %s' % (lnum,change.old))
 outarr.append(';')
 outarr.append('%s new %s' % (lnum,change.new))
 outarr.append(';')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for ichange,change in enumerate(changes):
   outarr = change_out(change,ichange)
   for out in outarr:
    f.write(out+'\n')
 print(len(changes),"written to",fileout)

class String(object):
 def __init__(self,s):
  s = s.rstrip('\r\n')
  self.string = s
  self.count = 0  # number of line instances in xxx.txt

def init_findrecs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [String(x) for x in f]
 print(len(recs),'Strings from',filein)
 return recs

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt
 filein1 = sys.argv[2] # list of strings
 fileout = sys.argv[3] # 
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 findrecs = init_findrecs(filein1)
 changes = init_changes(lines,findrecs)
 write_changes(fileout,changes)
 # check for strings not found
 n = 0
 for rec in findrecs:
  if rec.count == 0:
   n = n + 1
   print('NOT FOUND: ',rec.string)
 if n == 0:
  print('All strings from %s found in %s'%(filein1,filein))
 else:
  print(n,'strings from %s NOT found'%filein1)
  
