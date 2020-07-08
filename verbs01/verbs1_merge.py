#-*- coding:utf-8 -*-
"""verbs1_merge.py
  
"""
from __future__ import print_function
import sys, re,codecs

class MWVerb(object):
 d = {}  # dictionary of records via 'k1'
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  self.k1,self.Lnums,self.cat,self.cps,self.parse = line.split(':')
  if self.k1 in MWVerb.d:
   print('MWVerb WARNING: duplicate root',self.line)
  MWVerb.d[self.k1] = self
  # extra fields 
  self.dictinfo = {}

def init_mwverbs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [MWVerb(x) for x in f]
 print(len(recs),"mwverbs read from",filein)
 #recs = [r for r in recs if r.cat in ['root','genuineroot']]
 #print(len(recs),"returned from mwverbs")
 return recs

def unused_filter_mwverbs(mwrecs,option):
 return mwrecs
 recs = []
 for rec in mwrecs:
  if option == '1v':
   if has_one_vowel(rec.k1):
    recs.append(rec)
  else:
   recs.append(rec)
 return recs

def init_all_dictinfo(mwrecs,dictcodes):
 for rec in mwrecs:
  for dictcode in dictcodes:
   rec.dictinfo[dictcode] = []

class Dictverb(object):
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  m = re.search(r'L=([^,]*), k1=([^,]*), .*, mw=(.*)$',line)
  self.L,self.k1,self.mw = m.group(1),m.group(2),m.group(3)
  self.Ls = []

def init_dictverbs(filein,dictlo):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  npre = 0
  nomw = 0
  for x in f:
   if not x.startswith(';; Case'):
    continue
   rec = Dictverb(x)
   if dictlo in ['ap90']:
    if ' ' in rec.mw:
     npre = npre + 1
     continue
   if dictlo in ['bur','stc']:
    # mw=aNg,verb
    # mw=aNgIkf,preverb,aNgI+kf
    parts = rec.mw.split(',')
    #if rec.k1 == 'akz':
    # print('chk parts:',parts)
    rec.mw = parts[0]
    cat = parts[1]
    if cat == 'preverb':
     npre = npre + 1
     continue
   if rec.mw.startswith('?'):
    #print(dictlo,'No mw',rec.L,rec.k1)
    nomw = nomw + 1
    continue
   recs.append(rec)
   #if (dictlo == 'bur') and (rec.mw == 'stuB'):
   # print('init_dictverbs chk:',dictlo,rec.line)
 print('%s: %s verbs. Skip %s preverbs, %s nomw'%(dictlo,len(recs),npre,nomw))
 return recs

def joindups(dictrecs,dictlo):
 d = {}
 recs = []
 for dictrec0 in dictrecs:
  #kmw = dictrec0.mw
  L = dictrec0.L
  k1 = dictrec0.k1
  if k1 not in d:
   d[k1] = dictrec0
   recs.append(dictrec0)
  dictrec = d[k1]
  if L in dictrec.Ls:
   print('joindups: duplicate L')
   print(' rec = ',dictrec.line)
   print(' prev= ',dictrec0.line)
  else:
   dictrec.Ls.append(L)
 return recs

def init_dictinfo(mwrecs,dictlo,dictparent):
 dictup = dictlo.upper()
 if dictlo == 'pw':
  dictup = 'PWK'
 verbdir='verbs01'
 if dictlo == 'pwg':
  verbdir='verbs01a'
 filein = '%s%s/%s/%s_verb_filter_map.txt' %(dictparent,dictup,verbdir,dictlo)
 dictrecs = init_dictverbs(filein,dictlo)
 dictrecs1 = joindups(dictrecs,dictlo)

 for rec in dictrecs1:
  kmw = rec.mw
  if kmw not in MWVerb.d:
   print(dictlo,'initinfo. MW verb not found:',kmw,rec.k1,rec.Ls)
  else:
   mwrec = MWVerb.d[kmw]
   """
   if len(mwrec.dictinfo[dictlo]) != 0:
    print('init_dictinfo. Duplicate for',dictlo,kmw)
    for rec1 in mwrec.dictinfo[dictlo]:
     print('    ',rec1.line)
    exit(1)
   """
   mwrec.dictinfo[dictlo].append(rec)
   if False:
    if (dictlo == 'bur') and (kmw == 'stuB'):
     print('init_dictinfo chk:',dictlo,kmw,rec.line)
 
def write0(fileout,mwrecs,dictcodes,filter_opt):
 n = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in mwrecs:
   if not mwverb_passes_filter(rec,filter_opt):
    continue
   outarr = []
   outarr.append('mw=%s;%s' %(rec.k1,rec.Lnums))
   n1 = 0
   for dictcode in dictcodes:
    dictverbs = rec.dictinfo[dictcode]
    for dictverb in dictverbs:
     Lstr = ','.join(dictverb.Ls)
     outarr.append('%s=%s;%s' %(dictcode,dictverb.k1,Lstr))
     n1 = n1 + 1
   if n1 > 0:
     n = n + 1
     out = ':'.join(outarr) 
     f.write(out + '\n')
 print(n,"records written to",fileout)

def write1_helper_k1_L(k1,L):
  ans =  '%s;%s' %(k1,L)
  ans = k1
  return ans

def write1(fileout,mwrecs,dictcodes,filter_opt):
 # create markdown, one column for each dictionary
 n = 0
 outlines = []
 # title
 outlines.append("# Mapping of verbs to MW entries")
 outlines.append('')
 # table header (markdown)
 codes1 = ['mw'] + dictcodes
 out = ' | '.join(codes1)
 out = '| ' + out + ' |'
 outlines.append(out)
 # table underline (markdown)
 underlines = ['---' for code in codes1]
 out = ' | '.join(underlines)
 out = '| ' + out + ' |'
 outlines.append(out)
 for rec in mwrecs:
  if not mwverb_passes_filter(rec,filter_opt):
   continue
  outarr = []
  #outarr.append('mw=%s;%s' %(rec.k1,rec.Lnums))
  outarr.append(write1_helper_k1_L(rec.k1,rec.Lnums))
  n1 = 0
  for dictcode in dictcodes:
   dictverbs = rec.dictinfo[dictcode]
   #if (rec.k1 == 'stuB') and (dictcode == 'bur'):
   # print('dbg:',dictcode,rec.k1,len(dictverbs))
   if dictverbs == []:
    outarr.append('')
    continue
   a = [] 
   n1 = n1 + 1
   for dictverb in dictverbs:
    Lstr = ','.join(dictverb.Ls)
    #b = '%s;%s' %(dictverb.k1,Lstr)
    b = write1_helper_k1_L(dictverb.k1,Lstr)
    a.append(b)
   a1 = ' / '.join(a)
   outarr.append(a1)
  if n1 > 0:
    n = n + 1
    out = '| '.join(outarr)
    out = '| ' + out + ' |'
    outlines.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outlines:
   f.write(out + '\n')
 print(n,"records written to",fileout)

def write1h_helper_k1_L(k1,L):
  ans =  '%s;%s' %(k1,L)
  ans = k1
  return ans

def write1h(fileout,mwrecs,dictcodes,filter_opt):
 # create html table, one column for each dictionary
 n = 0
 outlines = []
 # title
 title = "verbs1 merge"
 temp = """
<!DOCTYPE html>
<html>
<head>
<title>%s</title>
<!-- See: https://github.com/sanskrit-lexicon/MWS/tree/master/verbs01 -->
<!-- https://css-tricks.com/position-sticky-and-table-headers/ -->
<style>
body {
  margin: 0;
  padding: 2rem;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse; 
}
table {
  text-align: center; /*left;*/
  position: relative;
  border-collapse: collapse; 
}
th, td {
  padding: 0.25rem;
}
tr:nth-child(even) {background-color: #f2f2f2;}

th {
  background: #FFE333; /*white;*/
  position: sticky;
  top: 0;
  box-shadow: 0 2px 2px -1px rgba(0, 0, 0, 0.4);
}
</style>
</head>
<body>
""" % title
 outlines = temp.splitlines() 
 outlines.append("<h2> Mapping of verbs to MW entries</h2>")
 if filter_opt == '1v':
  x = "<h3>MW verbs with one vowel</h3>"
 elif filter_opt == '2v':
  x = "<h3>MW verbs with more than one vowel</h3>"
 outlines.append(x)
 outlines.append('<br/>')
 # table header 
 outlines.append('<table>')
 outlines.append('<tr>')
 codes1 = ['mw'] + dictcodes
 a = []
 for code in codes1:
  a.append('<th>%s</th>' %code)
 outlines.append(' '.join(a))
 outlines.append('</tr>')
 for rec in mwrecs:
  if not mwverb_passes_filter(rec,filter_opt):
   continue
  outarr = []
  outarr.append(write1_helper_k1_L(rec.k1,rec.Lnums))
  n1 = 0
  for dictcode in dictcodes:
   dictverbs = rec.dictinfo[dictcode]
   #if (rec.k1 == 'stuB') and (dictcode == 'bur'):
   # print('dbg:',dictcode,rec.k1,len(dictverbs))
   if dictverbs == []:
    outarr.append('')
    continue
   a = [] 
   n1 = n1 + 1
   for dictverb in dictverbs:
    Lstr = ','.join(dictverb.Ls)
    #b = '%s;%s' %(dictverb.k1,Lstr)
    b = write1_helper_k1_L(dictverb.k1,Lstr)
    a.append(b)
   a1 = ' / '.join(a)
   outarr.append(a1)
  if n1 > 0:
    n = n + 1
    a = []
    for x in outarr:
     a.append('<td>%s</td>' % x)
    a1 = ' '.join(a)
    out = '<tr>%s</tr>'%a1
    outlines.append(out)
 outlines.append('</table>')
 outlines.append('</body>')
 outlines.append('</html>')
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outlines:
   f.write(out + '\n')
 print(n,"records written to",fileout)

def has_one_vowel(x):
 vowels = 'aAiIuUfFxXeEoO'  # Sanskrit vowels, in SLP1 transliteration
 xvowels = [c for c in x if c in vowels]
 return len(xvowels) == 1

def mwverb_passes_filter(rec,filter_opt):
 if filter_opt == '1v':
  ans = has_one_vowel(rec.k1)
 else:
  ans = True
 #print('filter:',filter_opt,rec.k1,ans)
 return ans

def write2(fileout,mwrecs,dictcodes,filter_opt):
 n = 0
 outlines = []
 for rec in mwrecs:
  if not mwverb_passes_filter(rec,filter_opt):
   continue
  k1s = [] # distinct values of rec.k1
  k1data = {}
  k1s.append(rec.k1)
  k1data[rec.k1] = []
  k1data[rec.k1].append(('mw',rec))
  n1 = 0
  for dictcode in dictcodes:
   dictverbs = rec.dictinfo[dictcode]
   for dictverb in dictverbs:
    k1 = dictverb.k1
    dictverb.Lnums = ','.join(dictverb.Ls)
    if k1 not in k1data:
     k1s.append(k1)
     k1data[k1] = []
    k1data[k1].append((dictcode,dictverb))
    n1 = n1 + 1
  if n1 == 0:
   continue
  n = n + 1 
  outarr = []
  for ik1,k1 in enumerate(k1s):
   codeverblist = k1data[k1]
   codes = []
   for code,vrec in codeverblist:
    assert vrec.k1 == k1
    codes.append(code)
   codestr = ','.join(codes)  # all the dictionary with spelling k1
   #outarr.append((k1,codestr))
   outarr.append('%s:%s' %(k1,codestr))
  outline = ' '.join(outarr) 
  outlines.append(outline)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outlines:
   f.write(out + '\n')
 print(n,"records written to",fileout)

def parse_option(s):
 parts = s.split(',')
 option = parts[0]
 if len(parts) == 1:
  filter_opt = None
 else:
  filter_opt = parts[1]
 return option,filter_opt

if __name__=="__main__": 
 optionstring = sys.argv[1]
 fileout = sys.argv[2] # verbs1_merge
 filein = sys.argv[3] # mwverbs2.txt
 dictcodes = sys.argv[4].lower().split(',')
 dictparent = sys.argv[5]
 option,filter_opt = parse_option(optionstring)
 #filter_opt = '1v'
 mwrecs = init_mwverbs(filein)
 #mwrecs = filter_mwverbs(mwrecs0,filter_opt)
 init_all_dictinfo(mwrecs,dictcodes)
 for dictcode in dictcodes:
  init_dictinfo(mwrecs,dictcode,dictparent)
 if option == '0':
  write0(fileout,mwrecs,dictcodes,filter_opt)
 elif option == '1':  # markdown output table
  write1(fileout,mwrecs,dictcodes,filter_opt)
 elif option == '1h': # html output table
  write1h(fileout,mwrecs,dictcodes,filter_opt)
 elif option == '2':
  write2(fileout,mwrecs,dictcodes,filter_opt)
 else:
  print('Invalid option:',option)
