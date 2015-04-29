"""newHom.py April 6, 2015
 
 
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

class ExtractKey(object):
 """ 
 """
 def __init__(self,key,cats,lnums):
  (self.key,self.cats,self.lnums) = (key,cats,lnums)
  # These next to be filled in during reading of old monier
  self.mwhoms = []
  self.mwlnums= []
  self.newhoms = []
 def __repr__(self):
  catstr = ' '.join(self.cats)
  lnumstr = ' '.join(self.lnums)
  mwhomstr = ' '.join(self.mwhoms)
  mwlnumstr = ' '.join(self.mwlnums)
  out = "%s %s %s : %s : %s" % (self.key,catstr,lnumstr,mwhomstr,mwlnumstr)
  return out
 def toString1(self):
  catstr = ' '.join(self.cats)
  lnumstr = ' '.join(self.lnums)
  mwhomstr = ' '.join(self.mwhoms)
  mwlnumstr = ' '.join(self.mwlnums)
  out = "%s %s  %s" % (self.key,mwlnumstr,mwhomstr)
  return out  
 def check(self):
  if len(self.mwhoms) != len(self.mwlnums):
   return 1
  if len(self.mwlnums) != len(self.lnums):
   return 2
  # Note: the next check is NOT expected to be true.
  # For instance, akzarA, which appears as an H1B under akzara.
  # From extract_keys (self.lnums), we get the FULL RANGE FOR akzara (i.e., first
  # lnum is that of akzara), while for mwlnums, we get the first akzarA lnum
  # e.g. lnumstr = 577 662, mwlnumstr = 582 662
  return 0
  for j in xrange(0,len(self.mwlnums)):
   if self.lnums[j] != self.mwlnums[j]:
    return 3
  return 0
 def _finduniq(self):
  """ count number of distinct non-0 hom values"""
  used = {}
  for hom in self.mwhoms:
   if hom == '0':
    continue
   used[hom]=True
  ans = len(used.keys())
  return ans

 def calc(self,printFlag=True):
  """ construct newhoms array
  """
  if printFlag:
   print self.toString1()
  actHoms = self._finduniq()
  reqHoms = len(self.mwlnums)
  if actHoms == reqHoms:
   # This may be suspect, as it depends on some ill-specified
   # property of the extract_keys_b.txt construction.
   # Pawan's code assumes that in this case there is no change
   # required for these homonyms, so that's what this version
   # of python code mimics
   self.newhoms = self.mwhoms
   return
  # There needs to be adjustment for some homs.  The rest of
  # this function provides the adjustments.
  imwhoms = [int(x) for x in self.mwhoms] #hom values as integers
  maxHom = max(imwhoms) # largest hom value (could be 0)
  pHom="abcdefghijklmnopqrstuvwxyz"  # Used when constructing a new hom value
  # construct counter for all hom values, including '0'
  totalHom = Counter()
  for hom in self.mwhoms:
   totalHom.update([hom])
  # numHom is individual counter for each hom value
  # initialized to 0
  numHom = {}
  for hom in totalHom.d.keys():
   numHom[hom]=0
  # homNew is the array of new homs, parallel to mwhoms
  homNew = []
  for hom in self.mwhoms:
   repl = hom # initialize replacement
   if hom == '0':
    k = numHom[hom] # current count
    repl = pHom[k] 
    numHom[hom] = k+1
   elif totalHom.d[hom] > 1:
    k = numHom[hom] # current count
    repl = "%s%s" %(hom,pHom[k])
    numHom[hom] = k+1
   homNew.append(repl)
  self.newhoms = homNew
  if printFlag:
   out1 = self.toString1()
   out = "%s -----%s" %(out1,' '.join(homNew))
   # Try to detect errors in monier.xml markup of <hom>
   if maxHom == 0:
    err=False
   elif maxHom == 1:
    err = True  # shouldn't have just 1 numbered homonym
   elif sorted([h for h in imwhoms if h != 0]) != range(1,maxHom+1):
    err=True
   else:
    err=False
   if err:
    out = "%s CHK ERR" % out
   print out

def init_ExtractKey(filekeys):
 f = codecs.open(filekeys,"r",'utf-8')
 keyrecs=[]
 keydict = {}
 for line in f:
  line=line.rstrip('\r\n')
  # sample = aMSaka	5	H2,39,39;H2,40,43
  # separator = tab
  (key,ndummy,struct) = re.split('\t',line)
  struct_parts = re.split(';',struct)
  if len(struct_parts) == 1:
   # only keep cases with more than one part
   continue
  cats = []
  lnums = []
  for part in struct_parts:
   (cat,l1,l2) = re.split(r',',part)
   cats.append(cat)
   lnums.append(l1)
  keyrec = ExtractKey(key,cats,lnums)
  keyrecs.append(keyrec)
  if key in keydict:
   print key,"Duplicate key in",filekeys
  keydict[key]=keyrec
 f.close()
 return (keyrecs,keydict)

class MWrec(object):
 def __init__(self,line,keydict):
  line = line.rstrip('\r\n')
  self.line = line
  m = re.search(r'^<(H.*?)>.*?<key1>(.*?)</key1>.*<L[^>]*>(.*?)</L>',line)
  if not m:
   # xml boilerplate
   self.entryFlag = False # Not of further interest
   return
  self.entryFlag = True
  self.cat = m.group(1)
  self.key = m.group(2)
  self.lnum = m.group(3)
  m = re.search(r'</key2><hom>(.*?)</hom>',line)
  if m:
   self.hom = m.group(1)
  else:
   self.hom = '0'
  if self.cat.endswith('A') or (len(self.cat) == 4) or (not (self.key in keydict)):
   # 2nd condition excludes those like H1Ba
   self.interestFlag = False # not of further interest
   return
  self.interestFlag = True
  self.keyrec = keydict[self.key]
  self.keyrecIndex = len(self.keyrec.mwhoms)
  self.keyrec.mwhoms.append(self.hom)
  self.keyrec.mwlnums.append(self.lnum)

def check_keyrecs(keyrecs):
 """ These are odd cases, which need to be checked
     separately . 
 """
 #print 'Skipping check_keyrecs'
 return  # comment this out to generate 'check_keyrecs.txt' sysout
 nerr=0
 for keyrec in keyrecs:
  ichk = keyrec.check()
  if ichk!=0:
   print 'ERR',ichk,'keyrec=',keyrec
   nerr = nerr + 1
 print nerr," internal errors found in keyrecs"
 exit(1)

def newHom(filekeys,filein,fileout1,fileout):
 # get potential cases from filekeys (extract_keys_b.txt)
 (keyrecs,keydict) = init_ExtractKey(filekeys)
 #print len(keyrecs),"potential 'hom' cases from",filekeys
 print "Cases to check are ..%s" % len(keyrecs)
 # read old version of mw, and update some keyrec fields
 with codecs.open(filein,"r","utf-8") as f:
  mwrecs = [MWrec(line,keydict) for line in f]
 #print len(mwrecs),"lines read from",filein
 check_keyrecs(keyrecs)
 # Construct rational homs from keyrecs
 for keyrec in keyrecs:
  keyrec.calc(printFlag=True)
  #newhom_calc(keyrec,fout1)
 # Write debug messages to fileout1 (mod_hom.txt)
 fout1 = codecs.open(fileout1,"w","utf-8")
 for keyrec in keyrecs:
  newhoms = keyrec.newhoms
  mwhoms = keyrec.mwhoms
  mwlnums = keyrec.mwlnums
  for i in xrange(0,len(newhoms)):
   if newhoms[i] != mwhoms[i]:
    fout1.write("%s %s\n" % (mwlnums[i],newhoms[i]))
 fout1.close()
 # write new version of monier (monier_pg3.xml)
 fout = codecs.open(fileout,"w",'utf-8')
 for mwrec in mwrecs:
  line = mwrec.line
  if (not mwrec.entryFlag):
   pass
  elif (not mwrec.interestFlag):
   pass
  else:
   keyrec = mwrec.keyrec
   ikeyrec = mwrec.keyrecIndex
   mwhom = keyrec.mwhoms[ikeyrec]
   newhom = keyrec.newhoms[ikeyrec]
   if mwhom == newhom:  # line unchanged
    pass
   elif mwhom == '0': # insert new hom into line
    line = re.sub('</key2>','</key2><hom>%s</hom>' % newhom,line)
   else: # modify existing hom in line
    line = re.sub('</key2><hom>.*?</hom>','</key2><hom>%s</hom>' % newhom,line)
  fout.write("%s\n" % line)
 fout.close()
 return
 # unused code----------------------------------------
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
 filekeys = sys.argv[1] #  extract_keys_b
 filein = sys.argv[2] #  monier_pg2a.xml
 fileout1 = sys.argv[3] # mod_hom.txt
 fileout = sys.argv[4] # monier_pg3.xml
 
 newHom(filekeys,filein,fileout1,fileout)
