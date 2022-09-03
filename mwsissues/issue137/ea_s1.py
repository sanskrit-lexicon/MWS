#-*- coding:utf-8 -*-
"""ea_s1.py
 
"""
import sys,re,codecs
import unicodedata

sys.stdout.reconfigure(encoding='utf-8') 
def check_ea(lines):
 asdict = {}
 s1dict = {}
 metaline = None
 page = None
 regex_split = re.compile(r'<s1 slp1="(.*?)">(.*?)</s1>')
 #nls = 0
 for iline,line in enumerate(lines):
  if iline == 0: # %***This File is E:\\APTE.ALL, Last update 11.09.06 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  if line.startswith('<L>'):
   metaline = line
   #imetaline1 = iline+1
   #continue
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   continue
  elif line.startswith('[Page'):
   page = line
   continue
  if metaline == None:
   # only examines lines within entries, including metaline
   continue
  for m in re.finditer(regex_split,line):
   s1txt = m.group(2)
   words = s1txt.split(' ')
   for word in words:
    for c in word:
     if ord(c) > 127:
      if c not in asdict:
       asdict[c] = 0
      asdict[c] = asdict[c] + 1
      if word not in s1dict:
       s1dict[word] = 0
      s1dict[word] = s1dict[word]+1
 
 return asdict,s1dict

def write_ea(fileout,eadict):
 keys = eadict.keys()
 keys = sorted(keys)
 
 with codecs.open(fileout,"w","utf-8") as f:
   for key in keys:
    out = "%s  (\\u%04x) %5d := %s" %(key,ord(key),eadict[key],unicodedata.name(key))
    f.write(out+'\n')
   
 print(len(keys),"extended ascii counts written to",fileout)

def write_s1(fileout,s1dict):
 keys = s1dict.keys()
 keys = sorted(keys)
 
 with codecs.open(fileout,"w","utf-8") as f:
   for key in keys:
    out = "%s %s" %(key,s1dict[key])
    f.write(out+'\n')
   
 print(len(keys),"extended ascii words written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout1 = sys.argv[2] # extended ascii characters
 fileout2 = sys.argv[3] # ls words with extended ascii characters
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 eacounts,s1counts = check_ea(lines) # 
 write_ea(fileout1,eacounts)
 write_s1(fileout2,s1counts)
 
