#-*- coding:utf-8 -*-
"""filter_ab.py
 
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

def init_changes(lines,word):
 changes = [] # array of Change objects
 metaline = None
 page = None
 word1 = word.replace('.','[.]')
 regexraw = r"[^<>:./—°\"-]\b%s\b[^°<\"-]" %word1
 #print("regexraw=",regexraw)
 regex = re.compile(regexraw)
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
  if metaline == None:
   continue
  oldline = line
  # generate change
  m = re.search(regex,line)
  if m == None:
   continue
  newline = oldline
  reason = None
  change = Change(metaline,page,iline,oldline,newline,reason)
  changes.append(change)
 #print(len(changes),'potential changes found')
 return changes

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 ident = change.metaline
 if ident == None:
  ident = change.page
 #outarr.append('; ' + ident)
 lnum = change.iline + 1
 outarr.append('%s old %s' % (lnum,change.old))
 outarr.append(';')
 outarr.append('%s new %s' % (lnum,change.new))
 outarr.append('; --')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for ichange,change in enumerate(changes):
   outarr = change_out(change,ichange)
   for out in outarr:
    f.write(out+'\n')
 print(len(changes),"written to",fileout)


if __name__=="__main__":
 wordsopt = sys.argv[1] # comma delimited list of words
 
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # change transactions
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 words = wordsopt.split(',')
 outrecs = []
 a = []
 for word in words:
  changes = init_changes(lines,word)
  a.append((word,changes))
  print(word,len(changes))
 outrecs = []
 for word,changes in a:
  outarr = []
  outarr.append('; -------------------------------------------------------')
  outarr.append('; %s (%s)' %(word,len(changes)))
  outarr.append('; -------------------------------------------------------')
  for ichange,change in enumerate(changes):
   outarr = outarr + change_out(change,ichange)
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print('potential changes written to',fileout)
 #write_changes(fileout,changes)

