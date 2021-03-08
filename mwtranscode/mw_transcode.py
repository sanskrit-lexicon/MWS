#-*- coding:utf-8 -*-
"""mw_transcode.py
 
 
"""
from __future__ import print_function
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir('transcoder')

slp1chars = {}
def update_slp1chars(x,y,tranin,tranout):
 if not ((tranin == 'roman') and (tranout == 'slp1')):
  return
 m = re.search(r"^[a-zA-Z|~/\\^— √°'+.,;=?\[\]\(\)!-]*$",y)
 if m == None:
  print(iline+1,x,y)
 return
 
def convert(line,tranin,tranout):
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

def convert_metaline(line,tranin,tranout):
 # '<k1>X<k2>Y'
 m = re.search('<k1>([^<]+)<k2>([^<]+)',line)
 x = m.group(0)  # entire match
 k1 = m.group(1)
 k2 = m.group(2)
 #k1a =transcoder.transcoder_processString(k1,tranin,tranout)
 #k2a =transcoder.transcoder_processString(k2,tranin,tranout)
 k1a = transcode(k1,tranin,tranout)
 k2a = transcode(k2,tranin,tranout)
 y = '<k1>%s<k2>%s' %(k1a,k2a)
 lineout = line.replace(x,y)
 if False and (tranin == 'slp1') and (tranout == 'deva'):
  if '/' in k2:
   print_unicode(k2,k2a)
 if (tranin in ['roman','roman1']) and (tranout == 'slp1'):
  # transcoding inversion problem for three lines
  exceptions = [
   ('<L>116525.7<',
    '<L>116525.7<pc>588,2<k1>paramahaMsopanizadhfdaya<k2>parama/—haMsopanizad-hfdaya<e>4'
   ),
   ('<L>139372<',
    '<L>139372<pc>704,3<k1>prAghAra<k2>prAg—hAra<e>3'
   ),
   ('<L>139373<',
    '<L>139373<pc>704,3<k1>prAghoma<k2>prAg—homa<e>3'
   )
  ]
  for start,correction in exceptions:
   if lineout.startswith(start):
    lineout = correction
    print('manual correction:',lineout)
    break
 return lineout

def test():
 tranin = 'roman'
 tranout = 'slp1'
 tests = [
  'ā́',
  'ā-pyā́yana',
  'ā́-bhūti',
 ]
 for x in tests:
  y = transcode(x,tranin,tranout)
  print('%s -> %s'%(x,y))
 exit(1)
def test1():
 with codecs.open("temp.txt","w","utf-8") as f:
  x = 'A^'
  y = transcode(x,'slp1','roman')
  f.write(y+'\n')
  z = transcode(y,'roman','slp1')
  f.write(z+'\n')
 print('write to temp.txt')
 exit(1)
 
if __name__=="__main__":
 #test()
 #test1()
 tranin = sys.argv[1]
 tranout = sys.argv[2]
 filein = sys.argv[3] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[4] # 
 
 with codecs.open(filein,"r","utf-8") as f:
  with codecs.open(fileout,"w","utf-8") as fout:
   inentry = False
   for iline,line in enumerate(f):
    line = line.rstrip('\r\n')
    if inentry:
     # inentry = True
     if line.startswith('<LEND>'):
      lineout = line
      inentry = False
     elif line.startswith('<L>'):  # error
      print('Error 1. Not expecting <L>')
      print("line # ",iline+1)
      print(line)
      exit(1)
     else:
      # keep looking for <LEND
      lineout = convert(line,tranin,tranout)
    else:
     # inentry = False
     if line.startswith('<L>'):
      lineout = convert_metaline(line,tranin,tranout)
      inentry = True
     elif line.startswith('<LEND>'): # error
      print('Error 2. Not expecting <LEND>')
      print("line # ",iline+1)
      print(line)
      exit(1)
     else:
      # line outside of <L>...<LEND>
      lineout = line
    fout.write(lineout+'\n')
    if False: # True:
     if iline > 1000:
      print('quit at iline=',iline)
      break
