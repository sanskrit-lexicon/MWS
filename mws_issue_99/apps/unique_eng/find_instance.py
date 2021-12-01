""" check_instance.py
"""
import sys,re,codecs
from parseheadline import parseheadline

class Entry(object):
 Ldict = {}
 k1dict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  # ===== additional attributes for Entry objects
  self.L = self.metad['L']
  self.k1 = self.metad['k1']
  self.pc = self.metad['pc']
  if self.k1 not in self.k1dict:
   self.k1dict[self.k1] = []  # a list of entries with given k1
  self.k1dict[self.k1].append(self)
  
  #  extra attributes
  self.topcatname = None # kind of or/and group  (por,or,pand,and)
  self.sval = None  # <s>(.*?)</s>
  self.sval1 = None # sval, without accents, etc.
  # kindmatch is True when topcatname is por/or and <info or='''>
  #   or similarly with and.
  # kindmatch is False with topcatname is por/or and <info and='''>
  #   or similarly with and
  # kindmatch is None when there is no <info or/and=...>
  self.kindmatch = None
  self.orand_iline = None  # iline value for '<info or="'
  self.orand_kind = None
  self.orand_data = None
  
def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

class WordCount(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  line = line.strip()
  self.word,self.count = line.split(' ')
  self.entries = []  # list of Entry objects containing word
  self.identdict = {}

tagregexes = [
    '<ab.*?</ab>', '<s>.*?</s>', '<ls.*?</ls>', '<info.*?/>',
 '<bot>.*?</bot>','<hom>.*?</hom>', '<etym>.*?</etym>', '<lang.*?</lang>',
 '<lex.*?</lex>','<s1.*?</s1>',
    ]
regexes = [re.compile(r) for r in tagregexes]

def remove_markup(text):
 for r in regexes:
  text = re.sub(r,' ',text)  # replace with space
 return text
"""
def entry_text(entry):
 textlines = entry.datalines
 text = ' '.join(textlines)  # not sure of joining with space.
 text = remove_markup(
 for r in regexes:
  text = re.sub(r,' ',text)  # replace with space
 return text
"""

def words_in_entries(wordrecs,entries):
 dword = {}
 for rec in wordrecs:
  dword[rec.word] = rec
 #
 for ientry,entry in enumerate(entries):
  for iline,line in enumerate(entry.datalines):
   text = remove_markup(line)
   linewords = re.split(r'\b',text)
   for w in linewords:
    if w in dword:
     rec = dword[w]
     e = (entry,iline)
     ident = (ientry,iline)
     if ident not in rec.identdict:
     #if e not in rec.entries:
      rec.entries.append(e)
      rec.identdict[ident] = True

def write_found(fileout,wordrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  nout = 0
  for rec in wordrecs:
    n = len(rec.entries)
    if n == 0:
     continue
    nout = nout + n
    outarr = []
    outarr.append('; -------------------------------------------')
    outarr.append('; %s %s' %(rec.word,rec.count))
    for entry,iline in rec.entries:
     line = entry.datalines[iline]
     lnum = entry.linenum1 + iline + 1
     meta = re.sub(r'<k2>.*$','',entry.metaline)
     outarr.append('; %s' %meta)
     out = '%s old %s' %(lnum,line)
     outarr.append(out)
     outarr.append(';')
    n = len(rec.entries)
    for out in outarr:
     f.write(out+'\n')
 print(nout,"written to",fileout)

def write_notfound(fileout,wordrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  nout = 0
  for rec in wordrecs:
    n = len(rec.entries)
    if n == 0:
     out = rec.word
     f.write(out+'\n')
     nout = nout + 1
 print(nout,"written to",fileout)

if __name__ == "__main__":
 filein = sys.argv[1]  # list of words with frequencies
 filein1 = sys.argv[2] # mw.txt or other cologne dictionary from csl-orig
 fileout = sys.argv[3] # lines of mw.txt containing instances of words.

 with codecs.open(filein,"r","utf-8") as f:
  words = [WordCount(line) for line in f]
 print(len(words),"words from",filein)
 entries = init_entries(filein1)
 words_in_entries(words,entries)
 write_found(fileout,words)
 
