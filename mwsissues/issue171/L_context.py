#-*- coding:utf-8 -*-
""" L_context.py
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


def entry_revsup(entry):
 text = '\n'.join(entry.datalines)
 if '<info n="sup"/>' in text:
  revsup = 'sup'
 elif '<info n="rev"/>' in text:
  revsup = 'rev'
 else:
  revsup = 'xxx'
 return revsup

def unused_nonalpha(entries):
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

def write_helper(rec,entries,case):
 ientry = rec.ientry
 entry = entries[ientry]
 N = 10 # number of context lines before/after entry
 ientry = rec.ientry  
 outarr = []
 preventry = entries[ientry - 1]
 nextentry = entries[ientry + 1]
 def f(entr):
  k1 = entr.metad['k1']
  L = entr.metad['L']
  e = entr.metad['e']
  revsup = entry_revsup(entr)
  out = '%s %s %s %s' % (k1,e,L,revsup)
  return out

 outarr.append('* Case %s: %s ' % (case,f(entry)))  # ientry '*' for emacs org mode
 iprev2 = ientry - 1
 iprev1 = iprev2 - N
 for i in range(iprev1,iprev2):
  outarr.append('      %s' % f(entries[i]))
 outarr.append('prev: %s' % f(preventry)) # ientry - 1
 outarr.append(' cur: %s' % f(entry))  # ientry
 outarr.append('next: %s' % f(nextentry)) #ientry + 1
 inext = ientry + 1
 inext1 = inext + 1
 inext2 = inext + N + 1
 for i in range(inext1,inext2):
  outarr.append('      %s' % f(entries[i]))

 outarr.append('')
 return outarr

def write(fileout,recs,entries):
 outrecs = []
 for irec,rec in enumerate(recs):
  case = irec + 1
  outrec = write_helper(rec,entries,case)
  outrecs.append(outrec)
  
 write_recs(fileout,outrecs)
 print(len(outrecs),"lines written to",fileout)

class Lrec:
 def __init__(self,L):
  self.L = L
  ientry = None # filled in later
 
def get_Lrecs(filein,option):
 lines = read_lines(filein)
 recs = []
 for line in lines:
  old,new = line.split()
  if option == '1':
   L = old
  elif option == '2':
   L = new
  else:
   print('get_Lrecs ERROR: option "%s" not implemented' % option)
   exit(1)
  rec = Lrec(L)
  recs.append(rec)
 return recs

def L_ientry_dict(entries):
 d = {}
 for ientry,entry in enumerate(entries):
  L = entry.metad['L']
  if L in d:
   print('L_ientry_dict ERROR: duplicate L',L)
   exit(1)
  d[L] = ientry
 return d
def update_recs(recs,entries):
 # get ientry field for each rec
 d = L_ientry_dict(entries)
 for rec in recs:
  L = rec.L
  if L not in d:
   print('update_recs ERROR. L not found in entries:',L)
   exit(1)
  ientry = d[L]
  rec.ientry = ientry  # update rec
  
if __name__=="__main__":
 option = sys.argv[1]
 assert option in ['1','2']
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 Lfile = sys.argv[3]
 fileout = sys.argv[4] # output summary
 entries = digentry.init(filein)
 recs = get_Lrecs(Lfile,option)
 update_recs(recs,entries)
 print('dbg quits')
 write(fileout,recs,entries)


