
import sys,re,codecs

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')
 print(len(lines),"written to",fileout)
 
def test(lines):
 punct = {}
 for line in lines:
  m = re.search(r'([a-zA-Z])$',line)
  if not m:
   c = line[-1] # last char   
   if c not in punct:
    punct[c] = 0
   punct[c] = punct[c] + 1
 keys = sorted(punct.keys())
 for c in keys:
  print(c,punct[c])
 exit(1)
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2] # alphabetic
 fileout1 = sys.argv[3] # hy
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip('\r\n') for line in f]
 print(len(lines),"lines from",filein)
 #test(lines)
 dkeep = {}
 keep = []
 dother = {}
 other = []
 #ending_punct = ('.',',',';','?')
 for line in lines:
  m = re.search(r'^([a-zA-Z]+)[.,;:?!]?$',line)
  if m:
   word = m.group(1)
   if word not in dkeep:
    dkeep[word] = True
    keep.append(word)
  else:
   word = line
   if word not in dother:
    dother[word] = True
    other.append(word)
 print(len(keep),len(other))
 write(fileout,keep)
 write(fileout1,other)

 
