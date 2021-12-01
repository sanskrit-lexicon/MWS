
import sys,re,codecs
import enchant

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')
 print(len(lines),"written to",fileout)
 
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2] # english US
 fileout1 = sys.argv[3] # not english US but english GB
 fileout2 = sys.argv[4] # neither of above.
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip('\r\n') for line in f]
 print(len(lines),"lines from",filein)

 US = enchant.Dict('en_US')
 GB = enchant.Dict('en_GB')
 
 #den_US = {}
 en_US = []
 #den_GB = {}
 en_GB = []
 #dother = {}
 other = []
 for line in lines:
  word,count = line.split(' ')
  if US.check(word):
   en_US.append(line)
  elif GB.check(word):
   en_GB.append(line)
  else:
   other.append(line)
 print(len(en_US),len(en_GB),len(other))
 write(fileout,en_US)
 write(fileout1,en_GB)
 write(fileout2,other)

 
