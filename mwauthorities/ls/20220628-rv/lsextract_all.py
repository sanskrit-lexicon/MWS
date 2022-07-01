#-*- coding:utf-8 -*-
"""lsextract_all.py -- summary stats for MW
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

def init_changes(lines,tipd):
 changes = [] # array of Change objects
 metaline = None
 imetaline1 = None
 page = None
 for iline,line in enumerate(lines):
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
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
   continue
  if line.startswith('[Page'):
   page = line
   continue
  reason=''
  newline = ls_questionmark(line,tipd)
  if newline == line:
   continue
  # generate a change
  # look at previous line(s) for last '<ls>X</ls>' and derive source
  found = None
  if found == None:
   iline1 = None
   line1 = None
   newline1 = None
   reason = ''
   #print('manual check:',iline+1,line)
  else:
   newline1 = line1 # re.sub(r'#} *$',' …#}',line1)
  change = Change(metaline,page,iline,line,newline,reason,iline1,line1,newline1)
  changes.append(change)
 print(len(changes),'potential changes found')
 return changes

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

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
   for ichange,change in enumerate(changes):
    outarr = change_out(change,ichange)
    for out in outarr:
     f.write(out+'\n')
 print(len(changes),"possible changes written to",fileout)

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
 def __init__(self,ls,abbrev,metaline,iline,line):
  self.ls = ls
  self.abbrev = abbrev
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.parmstr = ls[len(abbrev):].strip()
  if self.parmstr == '':
   self.nparms = 0
  else:
   self.nparms = len(self.parmstr.split(' '))
  self.len = len(self.parmstr)
  #if ls == abbrev:
  # print(ls,"'%s'" %self.parmstr,self.nparms)
  # exit(1)
  
def count_tips(lines,tipd,numbertip,unknowntip):
 #
 lsentries = []  # list of 'entry' with ls of given abbrev
 metaline = None
 imetaline1 = None
 page = None
 for iline,line in enumerate(lines):
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   entry = [] # list of LSCase appearing in this entry
   continue
  if line == '<LEND>':
   if len(entry)>0:
    lsentries.append(entry)
    # 
   metaline = None
   imetaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  for m in re.finditer(r'<ls([^>]*)>([^<]*)</ls>',line):
   attrib = m.group(1)
   elt = m.group(2)
   if len(elt) == 0:
    print('empty ls at line %s: %s' %(iline+1,line))
    continue
   m1 = re.search(r' +n="(.*?)"',attrib)
   if m1 != None:
    nval = m1.group(1)
    elt = nval + ' ' + elt
   if re.search(r'^[0-9]',elt): # number
    tip = numbertip
   elif elt[0] not in tipd:
    tip = unknowntip
   else:
    tiplist = tipd[elt[0]]
    tip  = findtip(elt,tiplist)
    if tip == None:
     tip = unknowntip
   # found a match
   
   tip.total = tip.total + 1
   if False: # debug
    if iline == 21943:
     print("DBG: ",tip.abbrev)
   #lscase = LSCase(elt,abbrev,metaline,iline,line)
   #entry.append(lscase)
 
 #print(len(lsentries),'entries with ls for  %s'%abbrev)
 #return lsentries

def unused_write_lscases(fileout,cases,abbrev):
 parmsd = {}  # 
 mparm = 0
 nparms = []
 for ls in cases:
  n = ls.nparms
  if n not in parmsd:
   parmsd[n] = []
  parmsd[n].append(ls)
  if n > mparm:
   mparm = n
  if n not in nparms:
   nparms.append(n)
   
 nparms.sort()
 print(nparms)
 for n in nparms:
  casesn = parmsd[n]
  print("%s cases with %s parms" %(len(casesn),n))
 print('ok so far')
 f = codecs.open(fileout,"w","utf-8")
 n0 = 4
 for n in nparms:
  casesn = parmsd[n]
  if n != n0:
   continue 
  f.write(';-----------------------------------------------------------\n')
  f.write(';  %s %s instances with %s parameters\n' %(len(casesn),abbrev,n))
  f.write(';-----------------------------------------------------------\n')
  
  for lscase in casesn:
   outarr = []
   if n == n0:
    outarr.append('; %s' %lscase.metaline)
    outarr.append('; %s' %lscase.ls)
    newls = re.sub(r'(%s [0-9]+, [0-9]+, [0-9]+[.]) ' % abbrev,
                   r'\1</ls> <ls n="%s">' % abbrev,lscase.ls)
    if newls != lscase.ls:
     outarr.append('%s old %s' %(lscase.iline+1,lscase.line))
     newline = lscase.line.replace(lscase.ls,newls)
     outarr.append('%s new %s' %(lscase.iline+1,newline))
    else:
     outarr.append('; %s old %s' %(lscase.iline+1,lscase.line))
    outarr.append(';')
   else:
    outarr.append('; %s' %lscase.ls)
   for out in outarr:
     f.write(out+'\n')
 f.close()

def write_tips(tips0,numbertip,unknowntip):
 outrecs = []
 outrecs.append('')  # for totals
 tips = sorted(tips0,key = lambda tip: tip.total,reverse=True)
 def tipformat(tip):
  text = tip.tip
  text = re.sub(r'^.*? = ','',text)
  text = text.replace('[Cologne Addition]','')
  text = text[0:40]
  return '%05d\t%s\t%s' %(tip.total,tip.abbrev,text)
 outrecs.append(tipformat(numbertip))
 outrecs.append(tipformat(unknowntip))
 tot = 0
 tot = tot + numbertip.total
 tot = tot + unknowntip.total
 for tip in tips:
  outrecs.append(tipformat(tip))
  tot = tot + tip.total
 #
 import datetime
 x = datetime.datetime.now()
 date = x.strftime("%Y-%m-%d")
 outrecs[0] = '%05d\t%s\tAs of %s' %(tot,'ALL',date)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outrecs:
   f.write(out+'\n')
 print("write_tips Output in ",fileout)
 
def write_lsentries(fileout,lsentries,abbrev):
 f = codecs.open(fileout,"w","utf-8")
 n0 = 0
 ntot = 0
 for lscases in lsentries:
  # lscases is a non-empty list of LSCase objects
  metaline = lscases[0].metaline
  n = len(lscases)
  ntot = ntot + n
  f.write(';-----------------------------------------------------------\n')
  x = re.sub(r'<k2>.*$','',metaline)
  f.write('; %s {%s %s}\n' %(x,abbrev,n))
  #f.write(';-----------------------------------------------------------\n')
  
  for lscase in lscases:
   f.write(lscase.ls + '\n')
  #f.write(';-----------------------------------------------------------\n')
 f.close()
 print(ntot,'= number of %s ls references'%abbrev)
if __name__=="__main__":
 
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filetip = sys.argv[2] # pwgbib_input.txt
 fileout = sys.argv[3] # output summary
 tips0 = init_tooltip(filetip)
 tips = sorted(tips0,key = lambda tip: len(tip.abbrev),reverse=True)
 tipd = dfirstchar(tips)
 # dummy for number
 numbertip = Tooltip("9.1\tNUMBER\tnumber\tls starts with number")
 # dummy for unknown
 unknowntip = Tooltip("9.2\tUNKNOWN\tunknown\tls is unknown")
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 count_tips(lines,tipd,numbertip,unknowntip) # also, updates tip.changes
 write_tips(tips0,numbertip,unknowntip)
 exit(1)
 write_lsentries(fileout,lsentries,abbrev)
 
