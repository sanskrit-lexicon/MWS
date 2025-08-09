# coding=utf-8
""" generate_random.py for vikramor
"""
from __future__ import print_function
import sys, re,codecs
import digentry
from make_js_index import *

def roman_to_integer(roman):
 # courtest copilot
 roman_values = {
     'I': 1, 'V': 5, 'X': 10, 'L': 50,
     'C': 100, 'D': 500, 'M': 1000
 }
 integer_value = 0
 prev_value = 0
 romanup = roman.upper()  # upcase to agree with roman_values
 for char in reversed(romanup):
  current_value = roman_values[char]
  if current_value < prev_value:
      integer_value -= current_value
  else:
      integer_value += current_value
  prev_value = current_value

 return integer_value

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)


def keyconvert_RN_pw_2_int(x):
 vals = ('Pr.','I','II','III','IV')
 for ival,val in enumerate(vals):
  if x == val:
   return ival
 print('keyconvert_RN_pw_2_int ERROR: x=',x)
 exit(1)

def get_dict_key(m,dictcode):
 if dictcode in ['mw2']:
  parm1=m.group(1)  
  parm2=m.group(2)
  key1 = roman_to_integer(parm1)
  key2 = int(parm2)
  key = (key1,key2)
  return key
 print('get_dict_key. Cannot handle dictcode %s' % dictcode)
 exit(1)
 
def init_verseentries(entries,dictcode):
 # allow roman
 d = {}
 n = 0
 dbg = False #True
 regex = get_dict_regex(dictcode)
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(regex,text):
   key = get_dict_key(m,dictcode)
   n = n + 1
   if dbg:
    L = entry.metad['L']
    print('dbg init_verseentries: L=%s, %s' %(L,m.group(0)))
   if key not in d:
    d[key] = []
   d[key].append(entry)
 keys = list(d.keys())
 if dbg:
  for key in d:
   es = d[key] # list of entries
   for e in es:
    L = e.metad['L']
    print('key=%s, L=%s' %(key,L))
 print('found %s instances in kosha' % n)
 print('found %s distinct in kosha' % len(keys))
 return d

def randomize_pagerecs(pagerecs,nrandom):
 import random
 vmin = pagerecs[0].fromv
 vmax = pagerecs[-1].tov
 ans = []
 for _ in range(nrandom):
  v = random.randint(vmin,vmax)
  ans.append(v)
 ans1 = sorted(ans)
 return ans1

class Example:
 def __init__(self,key,pagerec):
  self.key = key
  self.pagerec = pagerec
  self.entry = None
  
def unused_get_entry_for_examples(entries,examples):
 verses = [example.key for example in examples]
 dexample = {}
 for example in examples:
  dexample[example.key] = example
 regex_raw = r'<ls>Spr\. ([0-9]+)'
 regex = re.compile(regex_raw)
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(regex,text):
   versekosha = int(m.group(1))
   if versekosha in dexample:
    example = dexample[versekosha]
    example.entry = entry
    break
 for example in examples:
  verse = example.key
  entry = example.entry
  if entry == None:
   print('No entry found for verse',v)
  else:
   print(example.key, example.entry.metad['L'])
 exit(1)
 
def get_pagerec(pagerecs,key):
 for rec in pagerecs:
  if (rec.keymin <= key) and (key <= rec.keymax):
   return rec
 #print('get_pagerec ERROR: cannot find key',key)

def set_pagerec_key_helper(rec,dictcode):
 if dictcode in ('mw2',):
  anka = rec.anka
  fromv = rec.fromv
  tov = rec.tov
  rec.keymin = (anka,fromv)
  rec.keymax = (anka,tov)
 else:
  print('set_pagerec_key_helper ERROR. dictcode=',dictcode)
  exit(1)
  
def set_pagerec_key(pagerecs,dictcode):
 # set rec.keymin, rec.keymax for all records in pagerecs
 for rec in pagerecs:
  set_pagerec_key_helper(rec,dictcode)

def get_examples(verseentries,nrandom,pagerecs,dictcode):
 import random
 set_pagerec_key(pagerecs,dictcode)
 allkoshaverses = verseentries.keys()
 keyminall = pagerecs[0].keymin
 keymaxall = pagerecs[-1].keymax

 koshaverses = [key for key in allkoshaverses if
                ((keyminall <= key) and (key <= keymaxall))]
 nexamples = nrandom
 if nrandom > len(koshaverses):
  nexamples = len(koshaverses)
  print('WARNING Can only get %s examples' % len(koshaverses))
 # sample without duplicates
 exampleverses = random.sample(koshaverses,nexamples)
 examples = []
 for key in exampleverses:
  ventries = verseentries[key]
  ventry = random.choice(ventries)
  pagerec = get_pagerec(pagerecs,key)
  example = Example(key,pagerec)
  example.entry = ventry
  examples.append(example)
 return examples

def get_examples_all(verseentries,pagerecs,dictcode):
 set_pagerec_key(pagerecs,dictcode)
 allkoshaverses = verseentries.keys()
 keyminall = pagerecs[0].keymin
 keymaxall = pagerecs[-1].keymax

 koshaverses = [key for key in allkoshaverses if
                ((keyminall <= key) and (key <= keymaxall))]
 examples = []
 # exampleverses = koshaverses
 exampleverses = allkoshaverses
 nopagerec = 0
 for key in exampleverses:
  ventries = verseentries[key]
  for ventry in ventries:
   pagerec = get_pagerec(pagerecs,key)
   if pagerec == None:
    nopagerec = nopagerec + 1
   example = Example(key,pagerec)
   example.entry = ventry
   examples.append(example)
 #if nopagerec != 0:
 #print('get_examples_all: %s pagerecs not found' % nopagerec)
 return examples

def get_example_dict(dictcode):
 dicts = ('pwg','pwkvn','pw','sch','mw')
 thedict = None
 for d in dicts:
  if dictcode.startswith(d):
   thedict = d
   break
 if thedict == None:
  print('get_example_dict ERROR: %s' % dictcode)
 return thedict

def get_example_href(dictcode,pc):
 thedict = get_example_dict(dictcode)
 if thedict == None:
  return 'WARNING: href not found for %s' % dictcode
 dictup = thedict.upper()
 href = 'https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=%s&page=%s' % (dictup,pc)
 return href

def example_to_outrec(example,dictcode):
 outarr = []
 key  = example.key
 pagerec = example.pagerec
 entry = example.entry
 if pagerec == None:
  line = 'pagerec not found'
 else:
  line = pagerec.line
 outarr.append('key %s: %s' %(key,line))
 L = entry.metad['L']
 k1 = entry.metad['k1']
 pc = entry.metad['pc']
 outarr.append('L= %s, hw= %s, pc=%s' %(L,k1,pc))
 outarr.append('check: ?')
 if pagerec == None:
  href = get_example_href(dictcode,pc)
  outarr.append(href)
 outarr.append('----------------------------------------------')
 outarr.append('')
 return outarr

def example_to_outrec1(example,dictcode):
 # adjust so easier transfer to csl-corrections form
 outarr = []
 key  = example.key
 pagerec = example.pagerec
 entry = example.entry
 if pagerec == None:
  line = 'pagerec not found'
 else:
  line = pagerec.line
 outarr.append('key %s: %s' %(key,line))
 L = entry.metad['L']
 k1 = entry.metad['k1']
 pc = entry.metad['pc']
 if pagerec != None:
  outarr.append('L= %s, hw= %s, pc=%s' %(L,k1,pc))
 else:
  lsabbrev = get_dict_lsabbrev(dictcode)
  keystr = [str(i) for i in key]
  keyform = ','.join(keystr)
  oldform = '%s %s' %(lsabbrev,keyform)
  outarr.append('%s : %s : %s : ' %(L,k1,oldform))
 outarr.append('check: ?')
 if pagerec == None:
  href = get_example_href(dictcode,pc)
  outarr.append(href)
 outarr.append('----------------------------------------------')
 outarr.append('')
 return outarr

def write_examples(fileout,examples,dictcode):
 outrecs = []
 # sort examples by verse
 examples1 = sorted(examples,key = lambda e: e.key)
 for example in examples1:
  outrec = example_to_outrec1(example,dictcode)
  outrecs.append(outrec)
 #
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print('write_examples:',len(examples),"written to",fileout)

def get_dict_lsabbrev(dictcode):
 d = {
  'mw2':r'Vikr.',
   }
 if dictcode not in d:
  print('get_dict_lsabbrev Error',dictcode)
  exit(1)
 lsabbrev = d[dictcode]
 return lsabbrev
 
def get_dict_regex(dictcode):
 d = {
  # 
  'mw2':r'<ls>Vikr. ([iv]+), *([0-9]+)',
   }
 if dictcode not in d:
  print('get_dict_regex Error',dictcode)
  exit(1)
 regex_raw = d[dictcode]
 print("regex_raw =",regex_raw)
 regex = re.compile(regex_raw)
 return regex 

if __name__=="__main__":
 randomcode = sys.argv[1]
 # nrandom = int(sys.argv[1])
 dictcode = sys.argv[2]
 filein = sys.argv[3]  # xxx.txt
 filein1 = sys.argv[4] # name of index file
 fileout = sys.argv[5] # output file
 pagerecs = init_pagerecs(filein1)
 entries = digentry.init(filein)

 verseentries = init_verseentries(entries, dictcode)
 if randomcode == 'ALL':
  examples = get_examples_all(verseentries,pagerecs,dictcode)
  examples_nopagerecs = [x for x in examples if x.pagerec == None]
  write_examples(fileout,examples,dictcode)
  print(len(examples_nopagerecs),"instances of 'pagerec not found'")
  if examples_nopagerecs != []:
   if 6 < len(sys.argv):
    fileout1 = sys.argv[6]
    write_examples(fileout1,examples_nopagerecs,dictcode)
 else:
  # randomcode != ALL
  nrandom = int(randomcode)
  examples = get_examples(verseentries,nrandom,pagerecs,dictcode)
  print(len(examples),"examples found")
  write_examples(fileout,examples,dictcode)

