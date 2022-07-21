#-*- coding:utf-8 -*-
"""ls_abbrev_instances.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Tooltip(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  # pwg has code, abbrevUpper, abbrevLower,tip
  try:
   self.code,self.abbrev,self.tipmain,self.tipcat = line.split('\t')
  except:
   print('Tooltip error:\n%s' %line)
   parts=line.split('\t')
   exit(1)
  self.total = 0
  self.tip = '%s (%s)' %(self.tipmain,self.tipcat)
  
def init_tooltip(filein):
 with codecs.open(filein,"r","utf-8") as f:
  ans = [Tooltip(x) for x in f]
 print(len(ans),'tooltips from',filein)
 return ans

def dfirstchar(tooltips_sorted):
 d = {}
 for tip in tooltips_sorted:
  c = tip.abbrev[0]
  if c not in d:
   d[c] = []
  d[c].append(tip)
 return d

def findtip(ls,tiplist):
 for tip in tiplist:
  if ls.startswith(tip.abbrev):
   return tip
 return None

class Instance(object):
 def __init__(self,abbrev):
  self.abbrev = abbrev
  self.cases = [] # list of Case objects
  
class Case(object):
 def __init__(self,metaline,iline,line,match,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.match = match  
  self.newline = newline
  
def init_cases(lines,tipd,abbrevlist):
 abbrevdict = {}
 for abbrev in abbrevlist:
  abbrevdict[abbrev] = []
 metaline = None
 imetaline1 = None
 page = None
 prevls = None
 dwork = {} 
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  elif line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   #continue
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  # xx
  for m in re.finditer(r'<ls([^>]*)>([^<]*)</ls>',line):
   lstxt = m.group(0)
   attrib = m.group(1)
   elt = m.group(2)
   if len(elt) == 0:
    print('empty ls at line %s: %s' %(iline+1,line))
    continue
   m1 = re.search(r' +n="(.*?)"',attrib)
   if m1 != None:
    nval = m1.group(1)
    elt = nval + ' ' + elt
   if elt[0] not in tipd:
    tip = None
   else:
    tiplist = tipd[elt[0]]
    tip  = findtip(elt,tiplist)
   if tip == None:
    print('Unexpected unknown ls abbreviation: %s' %lstxt)
    continue
   tipabbrev = tip.abbrev
   if tipabbrev not in abbrevdict:
    # only interested in the given abbreviations
    continue
   newline = line.replace(lstxt,'**'+lstxt)
   case = Case(metaline,iline,line,lstxt,newline)
   abbrevdict[tipabbrev].append(case)
 return abbrevdict

def write_cases(fileout,abbrevdict,abbrevlist):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 prevmatch = None
 outrecs = []
 for abbrev in abbrevlist:
  cases = abbrevdict[abbrev]
  ncases = len(cases)
  outarr = []
  outarr.append('; ======================================================')
  outarr.append('; %s %s instances' % (abbrev,ncases))
  outarr.append('; ======================================================')
  for icase,case in enumerate(cases):
   metaline = re.sub(r'<k2>.*$','',case.metaline)
   outarr.append('; %s (instance %s of %s)' % (metaline,icase+1,abbrev))
   iline = case.iline
   lnum = iline + 1
   newline = case.newline
   outarr.append('%s new %s' %(lnum,newline))
   if (icase+1) != ncases:
    outarr.append('; ----------------------------')
  outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)

def write_mwauth(fileout,cases):
 """ write records in format of mwauth
 """
 cases = sorted(cases, key = lambda case: case.match.lower())
 outarr = []
 prevcode = 90.00
 prevabbrev = None
 inewcase = 0

 for case in cases:
  abbrev = case.match[4:-5]
  if abbrev == prevabbrev:
   continue
  prevabbrev= abbrev
  curcode = prevcode + 0.01
  prevcode = curcode
  a = abbrev
  atype = 'ti'
  tip = '<expandNorm><ti>Unknown reference</ti> [Cologne Addition]</expandNorm>'
  out = '%5.2f\t%s\t%s\t%s\t%s' %(prevcode,a,a,atype,tip)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
    f.write(out+'\n')
 print(len(outarr),'Records written to',fileout)
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2] # list of abbreviations
 filetip = sys.argv[3] # ls tooltip file
 fileout = sys.argv[4] # instances of abbreviations
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 with codecs.open(filein1,"r","utf-8") as f:
  abbrevlist = [x.rstrip('\r\n') for x in f]
  print(len(abbrevlist),"abbreviations in",filein1)
 # tooltips
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)

 abbrevdict = init_cases(lines,tipd,abbrevlist) 
 
 write_cases(fileout,abbrevdict,abbrevlist)
