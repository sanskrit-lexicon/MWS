#-*- coding:utf-8 -*-
"""make_change_abbrev.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Abc(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split('\t')
  assert len(parts) in [2,3]
  self.old = parts[0]
  self.new = parts[1]
  if len(parts) == 3:
   self.note = parts[2]
  else:
   self.note = None
  self.cases = []
  self.regex = self.old.replace('.','[.]')
  self.regex = r'\b' + self.regex
def init_abcs(filein):
 d = {}
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   rec = Abc(line)
   n = rec.old
   if n in d:
    print('init_abcs: duplicate lnum',n)
   d[n] = rec
   recs.append(rec)
 print(len(recs),'records read from',filein)   
 return recs,d

class Abbrev(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  parts = line.split('\t')
  self.abbrev = parts[0]
  self.data = parts[1]
  
def init_abbrevs(filein):
 d = {}
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   rec = Abbrev(line)
   n = rec.abbrev
   if n in d:
    print('init_abbrevs: duplicate lnum',n)
   d[n] = rec
   recs.append(rec)
 print(len(recs),'records read from',filein)   
 return recs,d

def check_abcs(abcs,abbrevsd):
 for rec in abcs:
  m = re.search(r'<ab>(.*?)</ab>',rec.new)
  if m == None:
   print('not an abbreviation',rec.new)
   rec.abbrev = None
   continue
  abbrev = m.group(1)
  if abbrev in abbrevsd:
   abbrevrec = abbrevsd[abbrev]
   data = abbrevrec.data
   print(abbrev,'found abbrev' ,data)
   rec.abbrev = abbrevrec
   
class Case(object):
 def __init__(self,metaline,iline,line,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.newline = newline

def compute_newpart(part,abcs):
 #abcs0 = abcs[:3]
 for abc in abcs:
  old = abc.old
  regex = abc.regex
  new = abc.new
  #newpart = part.replace(old,new)
  newpart = re.sub(regex,new,part)
  if newpart != part:
   return newpart,abc  # apply first change 
 return part,None # no changes apply

def compute_newline(line,abcs,iline):
 parts = re.split(r'(<ls[^<]*</ls>)|(<ab[^<]*?</ab>)|(<s>.*?</s>)|(<s1.*?</s1>)|(<pcol.*?</pcol>)',line)
 newparts = []
 abcnew = None
 for part in parts:
  if part == None:
   continue
  if part.startswith(('<ls','<ab','<s>','<s1','<pcol')):
   newpart = part
  else:
   newpart,abc = compute_newpart(part,abcs)
   if abc != None:
    if abcnew == None:
     abcnew = abc
    else:
     print('duplicate',abcnew.old, abc.old,iline+1) # not sure what to do
     print(line,'\n')
     
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline,abcnew

def init_cases(lines,abcs):
 cases = []
 metaline = None
 imetaline1 = None
 page = None
 prevls = None
 ncases = 0
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  elif line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   continue
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   continue
  newline,abc = compute_newline(line,abcs,iline)
  if newline == line:
   continue
  if abc == None:
   print('error. line=',line)
   print('newline    =',newline)
   exit(1)
  # generate a case
  case = Case(metaline,iline,line,newline)
  abc.cases.append(case)
  ncases = ncases + 1
 print(ncases,'lines changed')
 return cases

def write_changes(fileout,abcs):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s' % fileout)
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for abc in abcs:
  outarr = []
  n = n + 1
  cases = abc.cases
  outarr.append(r'; -------------------------------------------------------')
  outarr.append(r'; %s -> %s  (%s lines)' % (abc.old,abc.new,len(cases)))
  outarr.append(r'; -------------------------------------------------------')
  for case in cases:
   metaline = re.sub(r'<k2>.*$','',case.metaline)
   outarr.append('; %s' % metaline)
   iline = case.iline
   lnum = iline + 1
   line = case.line
   outarr.append('%s old %s' %(lnum,line))
   nchg = nchg + 1
   newline = case.newline
   outarr.append(';')
   outarr.append('%s new %s' %(lnum,newline))
   outarr.append('; ------------------------------')
  outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(nchg,'cases written to',fileout)

interpret_option = {
  '1': (r'<ls>RTL\.</ls> p\. *([0-9]+\.?)', r'<ls>RTL. p. \1</ls>'),
  '1a': (r' Jain\b', r' <ns>Jain</ns>'),
 }
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2] # Suggested abbreviations to be marked
 filein2 = sys.argv[3] # mwab_input == known abbreviations
 fileout = sys.argv[4] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 abcs,abcs_d = init_abcs(filein1)
 abbrevs,abbrevs_d = init_abbrevs(filein2)
 check_abcs(abcs,abbrevs_d)
 init_cases(lines,abcs)
 write_changes(fileout,abcs)
 
  
