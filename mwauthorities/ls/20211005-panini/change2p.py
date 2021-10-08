#-*- coding:utf-8 -*-
"""change2p.py change transactions re panini links
 
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

def init_changes(lines):
 """
 regexraw1 = r'<ls>Pāṇ[.](.*?)</ls>'
 regex1 = re.compile(regexraw1)
 #regexraw2 = r'^ +([0-9]+)-([0-9]+), *([0-9]+)'
 # example ' 6-4, 107'
 # Also, ' 6-4, 107X'  where X does not start with a digit.
 # catch example where space missing after comma
 regexraw2a = r'^ +([0-9]+)-([0-9]+), *([0-9]+)'
 regex2 = re.compile(regexraw2a)
 regexraw3 = r'<ls>Pāṇ[.]([^<]*) and (.*?)</ls>'
 regex3 = re.compile(regexraw3)
 """
 regexraw3 = r'(<ls>Pāṇ[.].*?)([ ,])+</ls>'
 regex3 = re.compile(regexraw3)

 changes = [] # array of Change objects
 metaline = None
 page = None
 def fsub(m):
  x = m.group(0)
  x1 = m.group(1)
  x2 = m.group(2)
  if x2 in [',', ', ']:
   y = x1 + '</ls>' + x2
  elif x2 == ', ':
   y = x1 + '</ls>, '
  else:
   y = x1 + '</ls>**'
  return y
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
  oldline = line  
  newline = re.sub(regex3,fsub,line)
  if newline == oldline:
   continue
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
 outarr.append('; -------------------------')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for ichange,change in enumerate(changes):
   outarr = change_out(change,ichange)
   for out in outarr:
    f.write(out+'\n')
 print(len(changes),"written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt
 fileout = sys.argv[2] # 
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes = init_changes(lines)
 write_changes(fileout,changes)
