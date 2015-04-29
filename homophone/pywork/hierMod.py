"""hierMod.py April 6, 2015
 Read a version of monier.xml, and alter some H-codes
 The logic does not involve the <hom> tag.
 The DTD is changed
"""
import sys, re,codecs

class Counter(dict):
 def __init__(self):
  self.d = {}
 def update(self,l):
  for x in l:
   if not (x in self.d):
    self.d[x]=0
   self.d[x] = self.d[x] + 1


def hierMod(filein,fileout):
 fout = codecs.open(fileout,"w",'utf-8')
 f = codecs.open(filein,"r",'utf-8')
 n = 0 # number of lines read
 nchg = 0 # Number of lines changed
 chgCounter = Counter() # categories changed
 mainEnt = 'a'  
 enc = []  # list of encountered non-main keys
 for line in f:
  n = n + 1
  m = re.search(r'<(H[^>]*)>.*?<key1>(.*?)</key1>',line)
  if not m:
   fout.write(line)
   continue
  cat = m.group(1)
  keyH = m.group(2)
  if cat.endswith('A'): # no change
   fout.write(line)
   continue
  if cat == 'HPW': # no change
   # HPW is probably not present in more recent monier.xml
   fout.write(line)
   continue
  if len(cat) == 2:  # Hx
   # (a) reset state variables
   mainEnt = keyH
   enc = []
   # (b) no change
   fout.write(line)
   continue
  # Now, cat is of form <Hxy> (but not HPW) (actually y is B or C)
  if keyH == mainEnt:
   # key same as primary key (mainEnt). 
   # (a) alter line. Change <Hxy>-><Hxya> and </Hxy>-></Hxya>
   lineout = re.sub(r'<(/?)(%s)>' % cat,r'<\1\2a>',line)
   fout.write(lineout)
   # (b) update counters
   nchg = nchg + 1
   chgCounter.update([cat])
   continue
  # key differs from primary key (mainEnt)
  if keyH in enc:
   # have encountered keyH before
   # (a) alter line. Change <Hxy>-><Hxya> and </Hxy>-></Hxya>
   lineout = re.sub(r'<(/?)(%s)>' % cat,r'<\1\2a>',line)
   fout.write(lineout)
   # (b) update counters
   nchg = nchg + 1
   chgCounter.update([cat])
   continue
  # have not encountered keyH
  enc.append(keyH)
  fout.write(line)
 fout.close()
 f.close()
 print n,"lines from",filein
 print n,"lines to",fileout
 print nchg,"lines changed"
 for cat in chgCounter.d.keys():
  print cat, chgCounter.d[cat]
if __name__=="__main__": 
 filein = sys.argv[1] #  monier.xml
 fileout = sys.argv[2] # monier_X.xml
 hierMod(filein,fileout)
