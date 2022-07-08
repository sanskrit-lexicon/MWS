#-*- coding:utf-8 -*-
"""make_change_noref.py for MW
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason,iline1,line1,new1):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason
  self.iline1 = iline1
  self.line1 = line1
  self.new1 = new1

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
 # possible change for iline1
 if change.iline1 != None:
  lnum = change.iline1 + 1
  line = change.line1
  new = change.new1
  outarr.append('%s old %s' % (lnum,line))
  outarr.append('%s new %s' % (lnum,new))
  outarr.append(';')
 
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
 return None

class LSCase(object):
 def __init__(self,ls,abbrev,metaline,iline,line,prevls):
  self.ls = ls
  self.abbrev = abbrev
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.prevls = prevls
  
def init_lscases(lines,tipd,abbrev):
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
  for m in re.finditer(r'<ls([^>]*)>([^<]*)</ls>',line):
   attrib = m.group(1)
   elt = m.group(2)
   m1 = re.search(r' +n="(.*?)"',attrib)
   if m1 != None:
    nval = m1.group(1)
    elt = nval + ' ' + elt
   # does this elt start only with 'parameters'?
   # for RV this could be digits or 'xiv'
   # BUT skip 'ib.'
   if elt == 'ib.':
    continue
   if re.search(r'^[0-9xiv]',elt):
    # a numerical ls.
    if prevls == None:
     continue
    # we have a 'numerical' ls. Associate it with prevtip
    if prevtip == None:
     # no previous tip to associate
     continue
    # only consider cases where previous tip is consistent with abbrev
    if prevtip.abbrev != abbrev:
     continue
    # we are good to go with this numerical case
    cases.append(LSCase(elt,abbrev,metaline,iline,line,prevls))
    # 07-13-2021 --
    prevls = None
    prevtip = None
    continue
   # regenerate prevtip and prevls
   if elt[0] not in tipd:
    continue
   tiplist = tipd[elt[0]]
   tip  = findtip(elt,tiplist)
   if tip == None:
    #print('tooltip abbreviation not found:',elt)
    continue
   prevtip = tip
   prevls = elt
   #if tip.abbrev != abbrev:
   # continue
   # found a match   
   #cases.append(LSCase(elt,abbrev,metaline,iline,line))
 print(len(cases),'instances of %s'%abbrev)
 return cases


def regular_ls(ls,abbrev):
 if re.search(r'^%s$'%abbrev,ls):
  return True
 if re.search(r'^%s [0-9]+, [0-9]+, [0-9]+[.]?$'%abbrev,ls):
  return True
 if re.search(r'^%s [0-9]+, [0-9]+[.]?$'%abbrev,ls):
  return True
 if re.search(r'^%s [0-9]+, [0-9]+-[0-9]+[.]?$'%abbrev,ls):
  return True
 if re.search(r'^%s [0-9]+, [0-9]+, [0-9]+-[0-9]+[.]?$'%abbrev,ls):
  return True
 return False

def old_refactor_1(ls,abbrev):
 """ ls == one or more of X,Y,Z. 
 """
 parts = []
 rest = ls
 while True:
  rest = rest.strip()  # remove spaces at end
  m = re.search(r'^([0-9]+)[ ,]+([0-9]+)[ ,]+([0-9]+)[.] *(.*)$',rest)
  if m == None:
   break
  part = '<ls n="%s">%s, %s, %s.</ls>' %(abbrev,m.group(1),m.group(2),m.group(3))
  parts.append(part)
  rest = m.group(4)
 if len(parts) == 0:
  return "<ls>%s</ls>" %ls
 new1 = ' '.join(parts)
 rest = rest.strip()
 if rest == '':
  return new1
 new2 = '<ls>%s</ls>' % rest
 newls = '%s %s' %(new1,new2)
 return newls

def old_refactor_2(ls,abbrev,lsprev):
 """ ls == one or more of X,Y,Z. 
 """
 
 # parse lsprev
 m = re.search(r'%s ([0-9]+)[ ,]+([0-9]+)[ ,]+([0-9]+)[.]?$' %abbrev,lsprev)
 if not m:
  #print('refactor_2 ERROR:',lsprev)
  #exit(1)
  return "<ls>%s</ls>" %ls
 x1 = m.group(1)
 x2 = m.group(2)
 x3 = m.group(3)
 parts = []
 rest = ls
 while True:
  rest = rest.strip()  # remove spaces at end
  m = re.search(r'^([0-9]+)[ ,]+([0-9]+)[.] *(.*)$',rest)
  if m == None:
   # don't require . at end
   m = re.search(r'^([0-9]+)[ ,]+([0-9]+)( *)$',rest)
  if m == None:
   break
  part = '<ls n="%s %s,">%s, %s.</ls>' %(abbrev,x1,m.group(1),m.group(2))
  parts.append(part)
  rest = m.group(3)
 if len(parts) == 0:
  return "<ls>%s</ls>" %ls
 new1 = ' '.join(parts)
 rest = rest.strip()
 if rest == '':
  return new1
 new2 = '<ls>%s</ls>' % rest
 newls = '%s %s' %(new1,new2)
 return newls

def refactor_1(ls,abbrev):
 """ 
 """
 m = re.search(r'^([xiv]+), ([0-9]+), ([0-9]+)\.?$',ls)
 if not m:
  # this generate
  return None
 newls = '<ls n="%s">%s</ls>' %(abbrev,ls)
 return newls
 while True:
  rest = rest.strip()  # remove spaces at end
  m = re.search(r'^([0-9]+)[ ,]+([0-9]+)[ ,]+([0-9]+)[.] *(.*)$',rest)
  if m == None:
   break
  part = '<ls n="%s">%s, %s, %s.</ls>' %(abbrev,m.group(1),m.group(2),m.group(3))
  parts.append(part)
  rest = m.group(4)
 if len(parts) == 0:
  return "<ls>%s</ls>" %ls
 new1 = ' '.join(parts)
 rest = rest.strip()
 if rest == '':
  return new1
 new2 = '<ls>%s</ls>' % rest
 newls = '%s %s' %(new1,new2)
 return newls

def write_lscases_noref(fileout,cases,abbrev,option):
 f = codecs.open(fileout,"w","utf-8")
 n = 0
 nchg = 0
 prevline = None
 previline = None
 for lscase in cases:
  outarr = []
  n = n + 1
  outarr.append(r'; -------------------------------------------------------')
  metaline = re.sub(r'<k2>.*$','',lscase.metaline)
  outarr.append('; %s' % metaline)
  oldls = lscase.ls
  prevls = lscase.prevls
  outarr.append('; %s : prev=%s' % (oldls,prevls))
  iline = lscase.iline
  lnum = iline + 1
  line = lscase.line
  if previline == iline:
   # in case we change same line more than once
   line = prevline
  outarr.append('%s old %s' %(lnum,line))
  oldlsfull = "<ls>%s</ls>" % oldls
  if option == '1':
   newlsfull = refactor_1(oldls,abbrev)
  elif option == 'man':
   newlsfull = '*****<xls n="%s">%s</ls>' % (abbrev,oldls)
  else:
   print('write_lscases_noref ERROR. Unknown option:',option)
   exit(1)
  if newlsfull == None:
   continue
  newline = line.replace(oldlsfull,newlsfull)
  nchg = nchg + 1
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))

  for out in outarr:
   f.write(out+'\n')
  previline = iline
  prevline = newline
 print(nchg,'cases written to',fileout)
 f.close()

def write_lscases_irreg(fileout,cases,abbrev):
 f = codecs.open(fileout,"w","utf-8")
 n = 0
 for lscase in cases:
  outarr = []
  if regular_ls(lscase.ls,abbrev):
   continue
  n = n + 1
  outarr.append(r'; ------------------------------------------------------=')
  meta = re.sub(r'<k2>.*$','',lscase.metaline)
  outarr.append('; %s' % meta)
  outarr.append('; %s' %lscase.ls)
  outarr.append('%s old %s' %(lscase.iline+1,lscase.line))
  outarr.append(';')
  outarr.append('%s new %s' %(lscase.iline+1,lscase.line))
  #newline = lscase.line.replace(lscase.ls,newls)
  #outarr.append('%s new %s' %(lscase.iline+1,newline))
  #outarr.append(';')
  for out in outarr:
   f.write(out+'\n')
 print(n,'irregular cases written to',fileout)
 f.close()

if __name__=="__main__":
 abbrev = sys.argv[1]  # used to filter abbreviation.
 option = sys.argv[2]
 filein = sys.argv[3] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[4] # pwgbib_input.txt
 fileout = sys.argv[5] # possible change transactions
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 #test(tipd,tips)
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 lscases = init_lscases(lines,tipd,abbrev) # also, updates tip.changes
 print(len(lscases),'cases',abbrev)
 #exit(1)
 #write_lscases(fileout,lscases,abbrev)
 #write_lscases_1(fileout,lscases,abbrev)
 #write_lscases_0(fileout,lscases,abbrev)
 write_lscases_noref(fileout,lscases,abbrev,option)
  
