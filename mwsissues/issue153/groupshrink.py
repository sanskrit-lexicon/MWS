# coding=utf-8
""" 
groupshrink.py
"""
from __future__ import print_function
import sys, re,codecs
import langgroup

def write(fileout,langgroups):
 outarr = []
 for g in langgroups:
  lines = g.lines
  for line in lines:
   outarr.append(line)
  
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')
 print(len(langgroups),"records written to",fileout)
 
def shrink_1(langgroups):
 ans = []
 print(len(langgroups),'in countmsg')
 for i,langgroup in enumerate(langgroups):
  if langgroup.msg in ['NO Error','Greek']:
   continue
  ans.append(langgroup)
 return ans

def shrink_2(langgroups):
 ans = []
 print(len(langgroups),'in countmsg')
 for i,x in enumerate(langgroups):
  if x.msg in ['NO Error','Greek']:
   continue
  if ((x.msg == 'Others') and
      (x.comment.startswith('[Spelling Error]')) ):
   continue             
  ans.append(x)
 return ans

def shrink_3(langgroups):
 ans = []
 for i,x in enumerate(langgroups):
  if x.msg in ['NO Error','Greek']:
   continue
  if ((x.msg == 'Others') and
      (x.comment.startswith('[Spelling Error]')) ):
   continue
  if '<lang>Prākṛt</lang>' in x.new:
   continue
  if '<lang>Bengālī</lang>' in x.new:
   continue
  if '<lang>Beng.</lang>' in x.new:
   continue
  ans.append(x)
 return ans

def shrink_4(langgroups):
 ans = []
 for i,x in enumerate(langgroups):
  if x.msg in ['NO Error','Greek']:
   continue
  if ((x.msg == 'Others') and
      (x.comment.startswith('[Spelling Error]')) ):
   continue
  if '<lang>Prākṛt</lang>' in x.new:
   continue
  if '<lang>Bengālī</lang>' in x.new:
   continue
  if '<lang>Beng.</lang>' in x.new:
   continue
  if '<lang>Pāli</lang>' in x.new:
   continue
  ans.append(x)
 return ans

def shrink_5(langgroups):
 ans = []
 for i,x in enumerate(langgroups):
  if x.msg in ['NO Error','Greek']:
   continue
  if ((x.msg == 'Others') and
      (x.comment.startswith('[Spelling Error]')) ):
   continue
  if '<lang>Prākṛt</lang>' in x.new:
   continue
  if '<lang>Bengālī</lang>' in x.new:
   continue
  if '<lang>Beng.</lang>' in x.new:
   continue
  if '<lang>Pāli</lang>' in x.new:
   continue
  if '<lang>Persian</lang>' in x.new:
   continue
  ans.append(x)
 return ans

def shrink_6(langgroups):
 ans = []
 for i,x in enumerate(langgroups):
  if x.msg in ['NO Error','Greek']:
   continue
  if ((x.msg == 'Others') and
      (x.comment.startswith('[Spelling Error]')) ):
   continue
  if '<lang>Prākṛt</lang>' in x.new:
   continue
  if '<lang>Bengālī</lang>' in x.new:
   continue
  if '<lang>Beng.</lang>' in x.new:
   continue
  if '<lang>Pāli</lang>' in x.new:
   continue
  if '<lang>Persian</lang>' in x.new:
   continue
  if '<lang>Eng.</lang>' in x.new:
   continue
  if '<lang>English</lang>' in x.new:
   continue
  ans.append(x)
 return ans

def shrink_7(langgroups):
 ans = []
 for i,x in enumerate(langgroups):
  if x.msg in ['NO Error','Greek']:
   continue
  if ((x.msg == 'Others') and
      (x.comment.startswith('[Spelling Error]')) ):
   continue
  if '<lang>Prākṛt</lang>' in x.new:
   continue
  if '<lang>Bengālī</lang>' in x.new:
   continue
  if '<lang>Beng.</lang>' in x.new:
   continue
  if '<lang>Pāli</lang>' in x.new:
   continue
  if '<lang>Persian</lang>' in x.new:
   continue
  if '<lang>Eng.</lang>' in x.new:
   continue
  if '<lang>English</lang>' in x.new:
   continue
  # 7
  if (x.msg == 'Misc.') and ('Tag' in x.comment):
   continue
  ans.append(x)
 return ans

if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # e.g., lang.string.changes.txt
 fileout = sys.argv[3] # 
 # read all the entries of the dictionary.
 langgroups = langgroup.init_langgroups(filein)
 if option == '1':
  langgroups1 = shrink_1(langgroups)
 elif option == '2':
  langgroups1 = shrink_2(langgroups)
 elif option == '3':
  langgroups1 = shrink_3(langgroups)
 elif option == '4':
  langgroups1 = shrink_4(langgroups)
 elif option == '5':
  langgroups1 = shrink_5(langgroups)
 elif option == '6':
  langgroups1 = shrink_6(langgroups)
 elif option == '7':
  langgroups1 = shrink_7(langgroups)
 else:
  print('groupshrink.py  option error',option)
  exit(1)
 write(fileout,langgroups1)
 
