#-*- coding:utf-8 -*-
"""ls_abnormal.py
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

def lsnormal(lselt,abbrev):
 ls0 = lselt
 if not ls0.startswith(abbrev):
  print('lsnormal problem: lselt = %s, abbrev = %s' %(lselt,abbrev))
  exit(1)
 if re.search(r'^Śak. [0-9]+ [a-d]\.?$',lselt):
  return True
 if ls0 == abbrev:
  return True  #<ls>MBh.</ls>
 ls = ls0[len(abbrev):] # strip the abbreviation
 # remove ending f., ff.
 ls = re.sub(r' ff?\.$','',ls)
 # remove ' n. d' (27 matches for "<ls[^<]* n\. [0-9]+\."
 ls = re.sub(r' n\. [0-9]+\.?','',ls)
 ls = re.sub(r' note [0-9]+\.?','',ls)
 
 # remove periods and commas
 ls = re.sub(r'[.,]','',ls)
 # remove spaces at end
 ls = ls.strip()
 # split on space
 words = ls.split(' ')
 # check each word to have typical form
 flag = True
 for word in words:
  if re.search(r'^[0-9]+$',word):
   continue # known form
  if re.search(r'^[ivxlc]+$',word):
   continue # known form
  if re.search(r'^[0-9]+/[0-9]+$',word):
   continue # known form
  if word in ['p','pp']: # revision 1
   # RTL. pp. 77 periods were removed above.
   continue # known form
  if word in ['n','note']: #revision 2
   continue # known form
  if word in ['a/b']: #revision 3
   continue # known form
  if word in ['14/v','14c/v']: # revision 4
   continue # known form   
  if word in ['vol']: # revision 5
   continue # known form   
  if word in ['Introd']: # revision 6
   continue # known form   
  # unexpected form
  flag = False
  break
 return flag

def init_cases(lines,tipd):
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
   if tip == None:
    #  we don't expect this to occur
    print('%s UNKNOWN ABBREV: %s' %(metaline,lstxt))
    continue
   abbrev = tip.abbrev
   flag = lsnormal(elt,abbrev)
   if flag:
    continue
   #newtxt = '**<ls>%s</ls>' % eltnew
   newline = line.replace(lstxt,'**'+lstxt)
   cases.append(Case(metaline,iline,line,lstxt,newline))

 print(len(cases),'abnormal ls cases')
 return cases

def write_cases(fileout,cases):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 prevmatch = None
 # section title
 for case in cases:
   outarr = []
   n = n + 1
   metaline = re.sub(r'<k2>.*$','',case.metaline)
   outarr.append('; %s' % metaline)
   outarr.append('; %s ' % case.match)
   iline = case.iline
   lnum = iline + 1
   line = case.line
   if previline == iline:
    # in case we change same line more than once
    line = prevline
   outarr.append('%s old %s' %(lnum,line))
   nchg = nchg + 1
   newline = case.newline
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
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[2] # tooltips
 fileout = sys.argv[3] # possible change transactions
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)

 cases = init_cases(lines,tipd) 
 
 write_cases(fileout,cases)
