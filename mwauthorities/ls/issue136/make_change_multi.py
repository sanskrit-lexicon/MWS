#-*- coding:utf-8 -*-
"""make_change_multi.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,iline,old,new):
  self.metaline = metaline
  self.iline = iline
  self.old = old
  self.new = new

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 try:
  ident = change.metaline
 except:
  print('ERROR:',change.iline,change.old)
  exit(1)
 if ident == None:
  ident = change.page
 outarr.append('; ' + ident)
 
 # change for iline
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')

 # dummy next line
 return outarr

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
  #print('findtip error:',ls)
  #exit(1)
 return None

class LSCase(object):
 def __init__(self,ls,abbrev,metaline,iline,line,prevls):
  self.ls = ls
  self.abbrev = abbrev
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.prevls = prevls

def calc_regex(abbrev,option):
 # for re.sub(r1,r2,line)
 if option == '1':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+) and ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3</ls> and <ls n="\1 \2,">\4</ls>'
  return r1,r2raw
 elif option == '2':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+) and ([xivcl]+), ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3</ls> and <ls n="\1">\4, \5</ls>'
  return r1,r2raw
 elif option == '3a':
  r1raw = r' and</ls> '
  r1 = re.compile(r1raw)
  r2raw = r'</ls> and '
  return r1,r2raw
 elif option == '3b':
  r1raw = r' and</ls>; <ls'
  r1 = re.compile(r1raw)
  r2raw = r'</ls> and <ls'
  return r1,r2raw
 
 elif option == '4a':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+), ([0-9]+) and ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3, \4</ls> and <ls n="\1 \2, \3,">\5</ls>'
  return r1,r2raw
 
 elif option == '4b':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+), ([0-9]+) and ([0-9]+), ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3, \4</ls> and <ls n="\1 \2,">\5, \6</ls>'
  return r1,r2raw

 elif option == '4c':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+), ([0-9]+) and ([xivcl]+), ([0-9]+), ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3, \4</ls> and <ls n="\1">\5, \6, \7</ls>'
  return r1,r2raw

 elif option == '5':
  r1raw = r'<ls>(%s) ([0-9]+) and ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2</ls> and <ls n="\1">\3</ls>'
  return r1,r2raw

 elif option == '6':
  r1raw = r'<ls>(%s) ([^<]+) and ([^<]+)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2</ls> and <ls n="\1">\3</ls>'
  return r1,r2raw

 elif option == '7':
  r1raw = r' <ab>seq.</ab></ls>' 
  r1 = re.compile(r1raw)
  r2raw = r'</ls> <ab>seq.</ab>'
  return r1,r2raw
 elif option == '7a':
  r1raw = r';</ls>' 
  r1 = re.compile(r1raw)
  r2raw = r'</ls>;'
  return r1,r2raw

 elif option == '7b':
  r1raw = r',</ls>' 
  r1 = re.compile(r1raw)
  r2raw = r'</ls>,'
  return r1,r2raw

 elif option == '8':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+); ([xivcl]+), ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3</ls>; <ls n="\1">\4, \5</ls>'
  return r1,r2raw

 elif option == '8a':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+), ([0-9]+); ([xivcl]+), ([0-9]+), ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3, \4</ls>; <ls n="\1">\5, \6, \7</ls>'
  return r1,r2raw

 elif option == '8b':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+); ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3</ls>; <ls n="\1 \2,">\4</ls>'
  return r1,r2raw

 elif option == '8c':
  r1raw = r'<ls>(%s) ([0-9]+); ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2</ls>; <ls n="\1">\3</ls>'
  return r1,r2raw

 elif option == '8d':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+); ([xivcl]+), ([0-9]+); ([xivcl]+), ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3</ls>; <ls n="\1">\4, \5</ls>; <ls n="\1">\6, \7</ls>'
  return r1,r2raw

 elif option == '8e':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+), ([0-9]+); ([0-9]+), ([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3, \4</ls>; <ls n="\1 \2,">\5, \6</ls>'
  return r1,r2raw

 elif option == '8f':
  r1raw = r'<ls>(%s) ([xivcl]+), ([0-9]+), ([0-9]+); *([0-9]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2, \3, \4</ls>; <ls n="\1 \2, \3,">\5</ls>'
  return r1,r2raw

 elif option == '8g':
  r1raw = r'<ls>(%s) ([xivcl]+); *([xivcl]+\.?)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2</ls>; <ls n="\1">\3</ls>'
  return r1,r2raw

 elif option == '9':
  r1raw = r'<ls>(%s) ([^<]+) *; *([^<]+)</ls>' % abbrev
  r1 = re.compile(r1raw)
  r2raw = r'<ls>\1 \2</ls>; <ls n="\1">\3</ls>'
  return r1,r2raw

 else:
  print('calc_regex ERROR. unknown option:',option)
  exit(1)
  
def init_lscases(lines,tipd,abbrev,option,ilines):
 # lines can be modified.
 regex1,regex2 = calc_regex(abbrev,option)
 cases = []
 metaline = None
 imetaline1 = None
 page = None
 prevls = None
 prevtip = None
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   continue
  if line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  if iline not in ilines:
   continue
  newline = re.sub(regex1,regex2,line)
  if newline == line:
   continue
  change = Change(metaline,iline,line,newline)
  cases.append(change)
  # in case a subsequent abbreviation also changes this line
  lines[iline] = newline  
 #print(len(cases),"lines changed")
 return cases

def write_lscases_all(fileout,cases_all,option):
 outrecs = []
 ntot = 0
 # title showing fileout
 outarr = []
 outarr.append(r'; *****************************************************')
 outarr.append(r'; %s' % fileout)
 outarr.append(r'; *****************************************************')
 outrecs.append(outarr)
 for abbrev,option,cases in cases_all:
  ntot = ntot + len(cases)
  # title for these changes
  outarr = []
  outarr.append(r'; =====================================================')
  outarr.append(r'; %s option=%s (%s)' %(abbrev,option,len(cases)))
  outarr.append(r'; =====================================================')
  outrecs.append(outarr) 
  for icase,case in enumerate(cases):
   outarr = change_out(case,icase)
   outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 
 print(ntot,'cases written to',fileout)
 f.close()


if __name__=="__main__":
 #abbrev = sys.argv[1]  # Could be used to filter abbreviation.
 option = sys.argv[1]
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[3] # pwgbib_input.txt
 fileout = sys.argv[4] # possible change transactions
 tips0 = init_tooltip(filetip)
 #tips0 = tips0[0:50]
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)

 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 # for efficiency, construct a dictionary indexed by known ls abbreviations.
 # abbrevd[ls] is a set containing the ilines with an instance of this
 # ls abbreviation
 # of lines that contain a given ls abbreviation
 abbrevd = {} 
 for iline,line in enumerate(lines):
  lsall = re.findall(r'<ls>.*?</ls>',line)
  for lstag in lsall:
   ls = lstag[4:-5] # remove <ls> and </ls>
   if ls == '':
    continue  # aberrant case
   if ls[0] not in tipd:
    continue # temporary
   tiplist = tipd[ls[0]]
   tip = findtip(ls,tiplist)
   if tip == None:
    continue
   abbrev = tip.abbrev
   if abbrev not in abbrevd:
    abbrevd[abbrev] = set()
   abbrevd[abbrev].add(iline)
 lscases_all = []
 for tip in tips0:
  abbrev = tip.abbrev
  if abbrev not in abbrevd:
   continue
  ilines = abbrevd[abbrev]
  lscasesa = init_lscases(lines,tipd,abbrev,option,ilines)
  if lscasesa != []:
   lscases_all.append((abbrev,option,lscasesa))
   print(abbrev,len(lscasesa))
 #print(len(lscases),'cases')
 write_lscases_all(fileout,lscases_all,option)
  
