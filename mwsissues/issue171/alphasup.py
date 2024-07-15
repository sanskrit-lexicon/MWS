#-*- coding:utf-8 -*-
""" alphasup.py
"""
from __future__ import print_function
import sys,re,codecs
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

class Misorder(object):
 def __init__(self,preventry,entry,nextentry):
  self.preventry = preventry
  self.entry = entry
  self.nextentry = nextentry

def nonalpha(entries):
 nsup = 0
 recs = [] # returned
 
 for ientry,entry in enumerate(entries):
  # require entry to be a 'sup'
  text = '\n'.join(entry.datalines)
  if '<info n="sup"/>' not in text:
   continue
  nsup = nsup + 1
  # compare k1s - no error checking needed since first/last entries not sup
  preventry = entries[ientry - 1]  
  nextentry = entries[ientry + 1]
  k1 = entry.metad['k1']
  prevk1 = preventry.metad['k1']
  nextk1 = nextentry.metad['k1']
  if comparek1(prevk1,k1,nextk1):
  #if compentry(preventry,entry,nextentry):
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
  recs.append(Misorder(preventry,entry,nextentry))
 print('nonalpha nsup = ',nsup)
 print('# misordered = ', len(recs))
 return recs

def write_misorder_helper(rec):
 preventry = rec.preventry
 entry = rec.entry
 nextentry = rec.nextentry
 outarr = []
 def f(entr):
  k1 = entr.metad['k1']
  L = entr.metad['L']
  e = entr.metad['e']
  out = '%s %s %s' % (k1,e,L)
  return out
 
 #x = f(preventry)
 #print(x)
 outarr.append('prev: %s' % f(preventry))
 outarr.append(' cur: %s' % f(entry))
 outarr.append('next: %s' % f(nextentry))
 outarr.append('')
 return outarr

def write_misorder(fileout,recs):
 outrecs = []
 for rec in recs:
  outrec = write_misorder_helper(rec)
  outrecs.append(outrec)
  
 write_recs(fileout,outrecs)
 print(len(outrecs),"lines written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # output summary
 entries = digentry.init(filein)

 recs = nonalpha(entries)

 write_misorder(fileout,recs)


