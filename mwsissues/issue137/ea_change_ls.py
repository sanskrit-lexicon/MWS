#-*- coding:utf-8 -*-
"""ea_change_ls.py
 
"""
import sys,re,codecs
import unicodedata
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
def change(lines):
 data = [
  (r'â', r'ā'),
  (r'ê', r'e'),
  (r'î', r'ī'),
  (r'ô', r'o'),
  (r'û', r'ū'),
  (r'ṉ', r'ṃ'),
 ]

 def f(m):
  x = m.group(0)
  for old,new in data:
   x = x.replace(old,new)
  return x

 newlines = []
 for line in lines:
  newline = re.sub(r'<ls.*?</ls>',f,line)
  newlines.append(newline)
 return newlines

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in lines:
    f.write(out+'\n')
 print(len(lines),"lines written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  tooltip
 fileout = sys.argv[2] # changed tooltip
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 newlines = change(lines) 
 write(fileout,newlines)

 
