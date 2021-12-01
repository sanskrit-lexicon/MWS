
import sys,re,codecs
def has_arabic(line):
 maxchar = max(line)
 if u'\u0600' <= maxchar <= u'\u06ff':  # Arabic code block
  return True
 else:
  return False
def has_nonascii(line):
 maxchar = max(line)
 if chr(127) <= maxchar :  
  return True
 else:
  return False

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')
 print(len(lines),"written to",fileout)
 
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2] # ascii
 fileout_arabic = sys.argv[3]
 fileout_nonascii = sys.argv[4]
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip('\r\n') for line in f]
 print(len(lines),"lines from",filein)
 arabic = []
 nonascii = []
 english = []
 for line in lines:
  line = line.strip()  # lines have preceding space
  if has_arabic(line):
   arabic.append(line)
  elif has_nonascii(line):
   nonascii.append(line)
  else:
   english.append(line)
 print(len(arabic),len(nonascii),len(english))
 write(fileout,english)
 write(fileout_arabic,arabic)
 write(fileout_nonascii,nonascii)
 
