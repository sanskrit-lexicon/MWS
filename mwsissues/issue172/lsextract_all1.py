#-*- coding:utf-8 -*-
"""lsextract_all1.py -- summary stats for MW, including 'empty' or not 'empty'
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
  try:
   self.code,self.abbrev,self.tipmain,self.tipcat = line.split('\t')
  except:
   print('Tooltip error:\n%s' %line)
   parts=line.split('\t')
   exit(1)
  self.total = 0  # total = titular + nontitular
  self.titular = 0  # count of 'empty' eg. <ls>C</ls>  (C = code)
  self.nontitular = 0 # non-empty 
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
  #for m in re.finditer(r'<ls([^>]*)>([^<]*)</ls>',line):
  # allow abbreviations within <ls>
  for m in re.finditer(r'<ls([^>]*)>(.*?)</ls>',line):
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
   if re.search(r'^[0-9]',elt): # number
    tip = numbertip
   elif elt[0] not in tipd:
    tip = unknowntip
   else:
    tiplist = tipd[elt[0]]
    tip  = findtip(elt,tiplist)
    if tip == None:
     tip = unknowntip
   # found a match update counts
   tip.total = tip.total + 1
   #if lstxt == '<ls>RV.</ls>': # dbg
   # print('check: elt=%s, code=%s' %(elt,tip.code))
   # exit(1)
   if elt == tip.abbrev:
    tip.titular = tip.titular + 1
   else:
    tip.nontitular = tip.nontitular + 1
   if tip == unknowntip:
    metaline = re.sub(r'<k2>.*$','',metaline)
    print('unknown tip at %s' % metaline)
    print('lstxt = %s, elt="%s"' %(lstxt, elt))
    print()

def tipformat_0(tip):
 text = tip.tip
 text = re.sub(r'^.*? = ','',text)
 text = text.replace('[Cologne Addition]','')
 text = text[0:40]
 return '%05d\t%s\t%s' %(tip.total,tip.abbrev,text)

def tipformat(tip):
 parts = [tip.code,tip.abbrev,tip.tipmain,tip.tipcat]
 text = ' :: '.join(parts)
 #return '%05d\t%s' %(tip.total,text)
 return '%05d,%d,%d\t%s' %(tip.total,tip.titular,tip.nontitular,text)

def write_tips(tips0,numbertip,unknowntip):
 outrecs = []
 outrecs.append('')  # for totals
 tips = sorted(tips0,key = lambda tip: tip.total,reverse=True)
 outrecs.append(tipformat(numbertip))
 outrecs.append(tipformat(unknowntip))
 tot = 0
 tot = tot + numbertip.total
 tot = tot + unknowntip.total
 tot_titular = 0
 tot_nontitular = 0
 for tip in tips:
  outrecs.append(tipformat(tip))
  tot = tot + tip.total
  tot_titular = tot_titular + tip.titular
  tot_nontitular = tot_nontitular + tip.nontitular
 #
 import datetime
 x = datetime.datetime.now()
 date = x.strftime("%Y-%m-%d")
 tot_str = '%d,%d,%d\t%s\tAs of %s' %(tot,tot_titular,tot_nontitular,'ALL,TITULAR,NONTITULAR',date)
 outrecs[0] = tot_str
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outrecs:
   f.write(out+'\n')
 print(len(outrecs),"lines written to",fileout)
 print(tot_str)
 tot_titular_str = '%05d\t%s' %(tot_titular,'TITULAR')
 tot_nontitular_str = '%05d\t%s' %(tot_nontitular,'NONTITULAR')
 print(tot_titular_str)
 print(tot_nontitular_str)
 

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

