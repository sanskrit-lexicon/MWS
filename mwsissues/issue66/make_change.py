# coding=utf-8
""" make_change.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

class Change:
 def __init__(self,metaline,lnum,old,new,oldtext,newtext):
  self.metaline = metaline
  self.lnum = lnum
  self.old = old
  self.new = new
  self.oldtext = oldtext
  self.newtext = newtext
  
def write_changes(fileout,changes):
 outrecs = []
 outarr = [] # header
 outarr.append('; ******************************************************')
 outarr.append('; %s changes' % (len(changes),))
 outarr.append('; ******************************************************')
 outrecs.append(outarr)
 for c in changes:
  outarr = []
  outarr.append('; %s' % c.metaline)
  outarr.append('; old: %s' % c.oldtext)
  outarr.append('; new: %s' % c.newtext)
  lnum = int(c.lnum)
  # change 
  outarr.append('%s old %s' %(lnum,c.old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,c.new))
  outarr.append('; ----------------------------------------------')
  outrecs.append(outarr)
 write_recs(fileout,outrecs,blankflag=False)

def make_changes_helper(line):
 """
  example 
old:
<ab>inf.</ab>with an ...
new:
<ab>inf.</ab> with an ...
 """
 m = re.search(r'(<ab[^<]*)(.)</ab>([a-zA-Z])',line)
 if m == None:
  return None
 a = m.group(1)
 c1 = m.group(2) # last char before </ab>
 c2 = m.group(3) # char after </ab>
 if c2 == ' ':
  return None
 if c1 == '°':
  return None
 oldtext = m.group(0)
 newtext = '%s%s</ab> %s' % (a,c1,c2)
 newline = line.replace(oldtext,newtext)
 return (newline,oldtext,newtext)

def make_changes(lines):
 changes = []
 metaline = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   metaline = line
  if line.startswith('<LEND>'):
   metaline = None
   continue
  if metaline == None:
   continue
  temp = make_changes_helper(line)
  if temp == None:
   continue
  # make a change
  (newline,oldtext,newtext) = temp
  lnum = iline + 1
  change = Change(metaline,lnum,line,newline,oldtext,newtext)
  changes.append(change)
 print(len(changes),"changes")
 return changes

if __name__=="__main__":
 filein = sys.argv[1]  # mw.txt
 fileout = sys.argv[2]  # change file 
 lines = read_lines(filein)
 changes = make_changes(lines)
 write_changes(fileout,changes)
 

