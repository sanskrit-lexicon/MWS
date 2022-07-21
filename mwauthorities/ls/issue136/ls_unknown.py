#-*- coding:utf-8 -*-
"""ls_unknown.py
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

class Case(object):
 def __init__(self,metaline,iline,line,match,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.match = match  
  self.newline = newline
  
def init_cases(lines,tipd,option):
 cases = []
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
   if tip != None:
    # this program only interested in UNKNOWN tip abbreviations.
    # Unless tip in None, we have no further interest in this ls.
    continue
   if option == '1':
    m1 = re.search(r'<ls>(.*?[^.])</ls>',lstxt)
    if m1 == None:
     continue
    elt = m1.group(1)
    eltnew = elt+'.'  # add missing period
    if eltnew[0] in tipd:
     tiplist = tipd[eltnew[0]]
     tip = findtip(eltnew,tiplist)
     if tip == None:
      continue
     newtxt = '<ls>%s</ls>' % eltnew
     newline = line.replace(lstxt,newtxt)
     cases.append(Case(metaline,iline,line,lstxt,newline))
     if False:
      print(metaline,lstxt)
   elif option == '2':
    if ' ' in lstxt:
     continue
    if not lstxt.endswith('.</ls>'):
     # end with period
     continue
    if lstxt not in dwork:
     dwork[lstxt] = 0
    dwork[lstxt] = dwork[lstxt] + 1
    newline = line.replace(lstxt,'**'+lstxt)
    cases.append(Case(metaline,iline,line,lstxt,newline))
   elif option == '3':
    newline = line.replace(lstxt,'**'+lstxt)
    cases.append(Case(metaline,iline,line,lstxt,newline))
   else:
    print('init_cases unknown option',option)
    exit(1)

 print(len(cases),'with unknown ls abbreviation')
 if False and (option == '2'):
  for lstxt in dwork:
   print(lstxt[4:-5],dwork[lstxt])
 return cases

def write_cases(fileout,cases,option):
 if option == '2':
  # sort cases alphabetically by case.match
  cases = sorted(cases, key = lambda case: case.match.lower())
  cased = {}
  for case in cases:
   match = case.match
   if match not in cased:
    cased[match] = 0
   cased[match] = cased[match] + 1
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 prevmatch = None
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' %(fileout,len(cases)))
 outarr.append('; option = %s' % option)
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  if option in ('1','2','3'):
   if option == '2':
    match = case.match
    if prevmatch != match:
     outarr.append(r'; ======================================================')
     outarr.append(r'; Begin %02d instances of %s )' %(cased[match],match) )
     outarr.append(r'; ======================================================')
    prevmatch = match
   outarr = []
   n = n + 1
   metaline = re.sub(r'<k2>.*$','',case.metaline)
   outarr.append('; %s' % metaline)
   if option != '2':
    outarr.append('; %s ' % case.match)
   #outrecs.append(outarr)
   iline = case.iline
   lnum = iline + 1
   line = case.line
   if previline == iline:
    # in case we change same line more than once
    line = prevline
   outarr.append('%s old %s' %(lnum,line))
   nchg = nchg + 1
   newline = case.newline
   if option == '2':
    pass
   else:
    outarr.append(';')
    outarr.append('%s new %s' %(lnum,newline))
    outarr.append(r'; -------------------------------------------------------')
   outrecs.append(outarr)
   previline = iline
   prevline = newline

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
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[3] # pwgbib_input.txt
 fileout = sys.argv[4] # possible change transactions
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)

 cases = init_cases(lines,tipd,option) 
 
 write_cases(fileout,cases,option)
 if option == '2':
  fileout1 = sys.argv[5]
  write_mwauth(fileout1,cases)
