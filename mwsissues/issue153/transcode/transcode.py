#-*- coding:utf-8 -*-
""" transcode.py
 
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('./')

slp1chars = {}
def update_slp1chars(x,y,tranin,tranout):
 if not ((tranin == 'roman') and (tranout == 'slp1')):
  return
 regex = "^[a-zA-Z|~/\\^— √°'+.,;=?\[\]\(\)!‘’〈〉{}‒-]*$"
 m = re.search(regex,y)
 if m == None:
  import string
  lowups = string.ascii_lowercase + string.ascii_uppercase
  others = r"~/|~\^— √°'+.,;=?[]()!‘’〈〉{}‒-]"
  goodchars = lowups + others
  badchars = [c for c in y if c not in goodchars]
  
  print('Unexpected character(s) in line #%s' % (iline+1,))
  badchars1 = ' '.join(badchars)
  print('%s unexpected chars=%s' %(len(badchars),badchars1))
  print(' x=',x)
  print(' y=',y)
 return
 
def convert(line,tranin,tranout,iline):
 # convert text  in '<s>X</s>'
 tagname = 's'
 def f(m):
  x = m.group(1)
  parts = re.split(r'(<.*?>)',x)
  newparts = []
  for part in parts:
   if part == None:
    newpart = ''
   elif part.startswith('<'):
    newpart = part
   else:
    #newpart = transcoder.transcoder_processString(part,tranin,tranout)
    newpart = transcode(part,tranin,tranout)
   newparts.append(newpart)
  y = ''.join(newparts)
  return '<s>%s</s>' % y

 regex = '<s>(.*?)</s>'
 #lineout = transcoder.transcoder_processElements(line,tranin,tranout,tagname)
 lineout = re.sub(regex,f,line)
 return lineout

def print_unicode(x,u):
 """ Sample output:
x= a/MSa—BU/
0905 | अ | DEVANAGARI LETTER A
0951 | ॑ | DEVANAGARI STRESS SIGN UDATTA
0902 | ं | DEVANAGARI SIGN ANUSVARA
0936 | श | DEVANAGARI LETTER SHA
2014 | — | EM DASH
092D | भ | DEVANAGARI LETTER BHA
0942 | ू | DEVANAGARI VOWEL SIGN UU
0951 | ॑ | DEVANAGARI STRESS SIGN UDATTA
 """
 import unicodedata
 outarr = []
 for c in u:
  name = unicodedata.name(c)
  icode = ord(c)
  a = f"{icode:04X} | {c} | {name}"
  outarr.append(a)
 print('x=',x)
 for out in outarr:
  print(out)
 print()

def transcode(x,tranin,tranout):
 y = transcoder.transcoder_processString(x,tranin,tranout)
 #if True and (('|' in x) or ('Q' in x)):
 if False and ('~' in x):  # for debugging.
  print_unicode(x,y)
 update_slp1chars(x,y,tranin,tranout)
 return y


if __name__=="__main__":
 tranin = sys.argv[1]
 tranout = sys.argv[2]
 filein = sys.argv[3] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[4] # 
 
 with codecs.open(filein,"r","utf-8") as f:
  with codecs.open(fileout,"w","utf-8") as fout:
   nchg = 0
   n = 0
   for iline,line in enumerate(f):
    n = n + 1
    line = line.rstrip('\r\n')
    lineout = convert(line,tranin,tranout,iline)
    if lineout != line:
     nchg = nchg + 1
    fout.write(lineout+'\n')
 print(n,"lines written to",fileout)
 print(nchg,"lines changed")
 
