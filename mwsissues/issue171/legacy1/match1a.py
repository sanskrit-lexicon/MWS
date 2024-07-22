#-*- coding:utf-8 -*-
""" match1a.py
"""
from __future__ import print_function
import sys,re,codecs,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import digentry
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

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

slp_from = "aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh"
slp_to =   "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw"
slp_from_to = str.maketrans(slp_from,slp_to)

# We can tell if string x is less than string y:
#  x.translate(slp_from_to) < y.translate(slp_from_to)

def comparek1_version1(prevk1,k1,nextk1):
 # return true only when prevk1 < k1 < nextk1
 if not (prevk1.translate(slp_from_to) < k1.translate(slp_from_to)):
  return False
 if not (k1.translate(slp_from_to) < nextk1.translate(slp_from_to)):
  return False
 return True

def comparek1(prevk1,k1,nextk1):
 # return true only when prevk1 < k1 < nextk1
 if prevk1.translate(slp_from_to) > k1.translate(slp_from_to):
  return False
 if k1.translate(slp_from_to) > nextk1.translate(slp_from_to):
  return False
 return True

def compentry(x1,x2,x3):
 k1 = x1.metad['k1']
 k2 = x2.metad['k1']
 k3 = x3.metad['k1']
 if k1.translate(slp_from_to) > k2.translate(slp_from_to):
  return False
 if k2.translate(slp_from_to) > k3.translate(slp_from_to):
  return False
 # further require same 'e' values
 e1 = x1.metad['e']
 e2 = x2.metad['e']
 e3 = x3.metad['e']
 if e1 != e2:
  return False
 if e2 != e3:
  return False
 return True

def compare_2_entries(x1,x2):
 k1 = x1.metad['k1']
 k2 = x2.metad['k1']
 if k1.translate(slp_from_to) < k2.translate(slp_from_to):
  return '<'
 if k1.translate(slp_from_to) == k2.translate(slp_from_to):
  return '='
 return '>'
 
class Misorder(object):
 def __init__(self,preventry,entry,nextentry,ientry):
  self.preventry = preventry
  self.entry = entry
  self.nextentry = nextentry
  self.ientry = ientry
  

def entry_revsup(entry):
 text = '\n'.join(entry.datalines)
 if '<info n="sup"/>' in text:
  revsup = 'sup'
 elif '<info n="rev"/>' in text:
  revsup = 'rev'
 else:
  revsup = 'xxx'
 return revsup

def nonalpha(entries):
 nsup = 0
 recs = [] # returned
 
 for ientry,entry in enumerate(entries):
  # require entry to be a 'sup'
  revsup = entry_revsup(entry)
  if revsup != 'sup':
   continue
  nsup = nsup + 1
  # compare k1s - no error checking needed since first/last entries not sup
  preventry = entries[ientry - 1]  
  nextentry = entries[ientry + 1]
  k1 = entry.metad['k1']
  prevk1 = preventry.metad['k1']
  nextk1 = nextentry.metad['k1']
  if comparek1(prevk1,k1,nextk1):
   # properly ordered
   continue
  # improperly ordered
  # Further require the same e's
  if preventry.metad['e']  != entry.metad['e']:
   continue
  if entry.metad['e'] != nextentry.metad['e']:
   continue
  # Further require this common 'e' to be a digit 1-4
  if len(entry.metad['e']) != 1:
   continue
  recs.append(Misorder(preventry,entry,nextentry,ientry))
 print('nonalpha nsup = ',nsup)
 print('# misordered = ', len(recs))
 return recs

def write_misorder_helper(rec,entries):
 preventry = rec.preventry
 entry = rec.entry
 nextentry = rec.nextentry
 ientry = rec.ientry  
 outarr = []
 def f(entr):
  k1 = entr.metad['k1']
  L = entr.metad['L']
  e = entr.metad['e']
  revsup = entry_revsup(entr)
  out = '%s %s %s %s' % (k1,e,L,revsup)
  return out

 outarr.append('* %s -> ?' % f(entry))  # ientry '*' for emacs org mode
 iprev2 = ientry - 1
 iprev1 = iprev2 - 10
 for i in range(iprev1,iprev2):
  outarr.append('      %s' % f(entries[i]))
 outarr.append('prev: %s' % f(preventry)) # ientry - 1
 outarr.append(' cur: %s' % f(entry))  # ientry
 outarr.append('next: %s' % f(nextentry)) #ientry + 1
 inext = ientry + 1
 inext1 = inext + 1
 inext2 = inext + 10 + 1
 for i in range(inext1,inext2):
  outarr.append('      %s' % f(entries[i]))

 outarr.append('')
 return outarr

def write_misorder(fileout,recs,entries):
 outrecs = []
 for rec in recs:
  outrec = write_misorder_helper(rec,entries)
  outrecs.append(outrec) 
 write_recs(fileout,outrecs)
 print(len(outrecs),"lines written to",fileout)

def make_k1dict(entries):
 d = {}
 for entry in entries:
  k1 = entry.metad['k1']
  if k1 not in d:
   d[k1] = [] # list of entries with given k1
  d[k1].append(entry)
 return d

def get_revsup(entry):
 text = '\n' . join(entry.datalines)
 if '<info n="rev"' in text:
  return "rev"
 if '<info n="sup"/>' in text:
  return "sup"
 return None

def check1a_entries(entries,k1dict):
 probs = [] # no match 
 for entry in entries:  # mw.txt
  revsup = get_revsup(entry)
  if revsup == None:
   continue
  k1 = entry.metad['k1']
  if k1 not in k1dict:
   probs.append(entry)
 #print(len(probs),'supplement entries unknown k1')
 return probs

def write_entries_helper(entry):
 outarr = []
 outarr.append(entry.metaline)
 for line in entry.datalines:
  outarr.append(line)
 outarr.append(entry.lend)
 return outarr

def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs) # ,blankflag=False)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2] # add3a.txt
 fileout = sys.argv[3] # output summary
 entries = digentry.init(filein)
 Ldict = digentry.Entry.Ldict;
 digentry.Entry.Ldict = {}
 entries1 = digentry.init(filein1)
 k1dict = make_k1dict(entries1)
 print(len(k1dict),'distinct k1 from',filein1)
 problems1 = check1a_entries(entries,k1dict)
 write_entries(fileout,problems1)

