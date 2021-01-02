#-*- coding:utf-8 -*-
"""undorenum.py
 One-time program to undo the renumbering of
 changes_9_Andhrabharati.txt
 python undorenum.py changes_9.txt changes_9_Andhrabharati_edit.txt changes_9_Andhrabharati_norenum.txt
 

"""
from __future__ import print_function
import sys, re,codecs

def generate_cases(lines):
 """ 
 """
 nlines = len(lines)
 def linetypeF(iline):
  flag1 =  lines[iline] == '; ------------------------------------------------------------'
  case = 0
  if not flag1:
   return case
  iline1 = iline + 1
  if not (iline1 < nlines):
   return case
  m = re.search(r'^; Case ([0-9][0-9][0-9][0-9])[.]',lines[iline1])
  if not m:
   return case
  case = int(m.group(1))
  return case

 items = []
 for iline,line in enumerate(lines):
  if iline == 0:
   case = linetypeF(iline)
   if not (0 < case):
    print('generate_items ERROR 1',line)
    exit(1)
   items = [line]
  elif linetypeF(iline)>0:
   yield items
   items=[line]
  else:
   items.append(line)
 # last time
 yield items

def convert_totab(lines):
 groups = []
 flag = False
 group = []
 for line in lines:
  if line.startswith('<L>'):
   flag = True
   group = [line]
  elif line.startswith('<LEND>'):
   group.append(line)
   groups.append(group)
   group = []
   flag = False
  elif flag:
   group.append(line)
  else:
   group = [line]
   groups.append(group)
 # 
 outlines = []
 suppflag = False
 for group in groups:
  if len(group) == 1:
   line = group[0]
   suppflag = (line == '; SUPPLEMENT')
   if suppflag:
    continue  # don't include in output    
  else:
   line = '\t'.join(group)
   if suppflag:
    line = re.sub('<L>','<Ls>',line)
   suppflag = False
  outlines.append(line)    
 return outlines

def convert_fromtab(lines):
 outlines = []
 for line in lines:
  if re.search(r'^ *$',line):
   # skip blank lines
   continue
  if not line.startswith('<L'):
   outlines.append(line)
   continue
  m = re.search('^<L(.*?)>',line)
  a = m.group(1)
  line1 = re.sub(r'^<L(.*?)>','<L>',line)
  lines1 = line1.split('\t')
  if a != '':
   outlines.append('; SUPPLEMENT %s'%a)
  outlines = outlines + lines1
 return outlines

def get_Lcodes(tablines):
 a = []
 for iline,line in enumerate(tablines):
  m = re.search(r'^<L.*?>(.*?)<',line)
  if m:
   aval = (iline,m.group(1))
   a.append(aval)
 return a

def matchlineStat(tabline,atabline):
 if tabline == atabline:
  return 1.0
 tabline1 = re.sub(r'^<L>.*?<','',tabline)
 atabline1 = re.sub(r'^<L>.*?<','',atabline)
 words = re.split(r'[\t ]',tabline1)
 awords = re.split(r'[\t ]',atabline1)
 setwords = set(words)
 asetwords = set(awords)
 isect = setwords.intersection(asetwords)
 nisect = len(isect)
 nwords = len(setwords)
 nawords = len(asetwords)
 xwords = float(nwords)
 xawords = float(nawords)
 xavgwords = (xwords + xawords)/2.0
 xisect = float(nisect)
 x = xisect / xavgwords
 return x
 print('words=',words)
 print('awords=',awords)
 print('isect words=',list(isect))
 print('# words: ',nisect,nwords,nawords)
 print('check:',x)

def matchlineP(tabline,atabline):
 if tabline == atabline:
  return True
 # are they approximately equal?
 tabline1 = re.sub(r'^<L>.*?<','',tabline)
 atabline1 = re.sub(r'^<L>.*?<','',atabline)
 words = re.split(r'[\t ]',tabline1)
 awords = re.split(r'[\t ]',atabline1)
 setwords = set(words)
 asetwords = set(awords)
 isect = setwords.intersection(asetwords)
 nisect = len(isect)
 nwords = len(setwords)
 nawords = len(asetwords)
 xwords = float(nwords)
 xawords = float(nawords)
 xavgwords = (xwords + xawords)/2.0
 xisect = float(nisect)
 x = xisect / xavgwords
 print('words=',words)
 print('awords=',awords)
 print('isect words=',list(isect))
 print('# words: ',nisect,nwords,nawords)
 print('check:',x)

 exit(1)

def match_tabline(tabline,alcodes,atablines):
 xbest = -1.0
 jbest = 0
 for idx_alcode,alcode in enumerate(alcodes):
  jline,Lnuma = alcode
  atabline = atablines[jline]
  x = matchlineStat(tabline,atabline)
  if x > xbest:
   xbest = x
   jbest = idx_alcode
 
 return xbest,jbest
def compare_case(tablines,atablines):
 lcodes = get_Lcodes(tablines)
 alcodes = get_Lcodes(atablines)
 assert len(lcodes) == len(alcodes)
 ans = []
 for idx,lcode in enumerate(lcodes):
  iline,Lnum = lcode
  tabline = tablines[iline]
  xbest,aidx = match_tabline(tabline,alcodes,atablines)
  ans.append(aidx)
 assert len(set(ans)) == len(alcodes)
 return ans
 #assert len(ans) = len(alcodes)
 
def compare_cases(cases,acases):
 ncases = len(cases)
 assert ncases == len(acases)
 nprob = 0
 nsame = 0
 ndiff = 0
 new_acases = []
 for icase,lines in enumerate(cases):
  alines = acases[icase]
  lcodes = get_Lcodes(lines)
  alcodes = get_Lcodes(alines)
  if len(lcodes) != len(alcodes):
   print('compare_cases WARNING',icase+1,len(lcodes),' != ',len(alcodes))
   nprob = nprob + 1
  aperm = compare_case(lines,alines) # permutation of indexes in alcodes
  invperm = list(range(0,len(aperm)))  # inverse of permutation aperm
  for icode in aperm:
   jcode = aperm[icode]
   invperm[jcode] = icode
  #print(aperm,invperm)
  new_alines = []  # make a copy of new_alines
  for line in alines:
   new_alines.append(line)
  for jcode,icode in enumerate(invperm):
   alcode = alcodes[jcode]
   lcode = lcodes[icode]
   iline,iL = lcode
   jline,jL = alcode
   aline = alines[jline]  # original from Andhrabharati
   # replace first instance of >jL< with >iL<
   new_aline = aline.replace('>'+jL+'<','>'+iL+'<',1)
   # replace also in alines array
   new_alines[jline] = new_aline
  # replace acases
  new_acases.append(new_alines)
  continue
  if True:
   if aperm == list(range(len(alcodes))):
    print('Case %s: no changes' % (icase+1,))
    nsame = nsame + 1
    continue
   ndiff = ndiff + 1
   for icode,lcode in enumerate(lcodes):
    iline,iL = lcode
    jcode = aperm[icode]
    alcode = alcodes[jcode]
    jline,jL = alcode
    #if (icode != jcode):
    print('Case %s: %s (%s)  <--> %s (%s)'%(icase+1,icode,iL,jcode,jL))
   #exit(1)
 #print('compare_case: nprob=',nprob)
 #print(nsame,'Cases involve no renumbering')
 #print(ndiff,'Cases involve renumbering')
 return new_acases

def adjust_acase(new,old):
 """ lists of lines of equal length.
  Note number of differences
  if non-zero,  modify line new[1]
 """
 n = len(new)
 ndiff = 0
 assert n == len(old)
 for iline,line in enumerate(new):
  if old[iline] != line:
   ndiff = ndiff + 1
 if ndiff > 0:
  i = 1 # 2nd line of new
  line = new[i]
  line1 =  line + ' REORDER %s' %ndiff
  new[i] = line1
  return True
 else:
  return False  # no differences

if __name__=="__main__": 
 filein = sys.argv[1]  # changes_9
 filein1 = sys.argv[2] # changes_9_Andhrabharati
 fileout = sys.argv[3]
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
  tablines = convert_totab(lines)
  cases = list(generate_cases(tablines))
  print(len(cases),"cases from",filein)

 with codecs.open(filein1,"r","utf-8") as f:
  atablines = [x.rstrip('\r\n') for x in f]
  acases = list(generate_cases(atablines))
  print(len(acases),"cases from",filein1)

 new_acases = compare_cases(cases,acases)
 new_alines = []
 ndiff_cases = 0
 for icase,new_acase in enumerate(new_acases):
  acase = acases[icase]
  flag = adjust_acase(new_acase,acase)
  new_alines = new_alines + new_acase
  if flag:
   ndiff_cases = ndiff_cases + 1
 print(ndiff_cases,'Cases have reorderings')
 assert len(new_alines) == len(atablines)
 with codecs.open(fileout,"w","utf-8") as f:
  ndiff = 0
  for iline,line in enumerate(new_alines):
   f.write(line+'\n')
   if line != atablines[iline]:
    ndiff = ndiff + 1
 print(len(new_alines),'written to',fileout)
 print(ndiff,'differences from',filein1)
