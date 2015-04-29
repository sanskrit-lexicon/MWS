"""extract_keys_a.py April 8, 2015
 Conversion of extract_keys_a.php to Python
 Read extract_keys.txt, and construct extract_keys_a.txt.
 
"""
import sys, re,codecs

def extract_keys_a(filein,fileout):
 fout = codecs.open(fileout,"w",'utf-8')
 f = codecs.open(filein,"r",'utf-8')
 n = 0 # number of lines read
 # state variables
 key0 = ''  # previous key
 outarr=[]
 for line in f:
  n = n + 1
  if n > 1000000: #50:
   print "Debug breaking"
   break
  line = line.rstrip('\r\n')
  # A small number of keys have non-SLP characters. We remove these
  line1 = line
  line = re.sub(r'[^a-zA-Z0-9,.|]','',line)
  if line != line1:
   print "WARNING: Characters in key: %s (change to %s)" %(line1,line)
  (key,hcode,lnum) = re.split(',',line)
  if key0 == '': #First time through  
   key0 = key
   hcode0 = hcode
   L1 = lnum
   L2 = lnum
   keyhash = {}
   keyhash[key0]=hcode0
   continue
  # Special handling for hcode=X[ABC]
  if re.search(r'[ABC]$',hcode):
   L2 = lnum
   if not (key in keyhash):
    keyhash[key]=hcode
   continue
  # otherwise, put records into outarr
  # First, sort keyhash by key
  keys = keyhash.keys() # list of keys
  sorted_keys = sorted(keys) #  Why sort?
  for key1 in sorted_keys:
   out = "%s,%s,%s,%s" % (key1,keyhash[key1],L1,L2)
   outarr.append(out)
  # reset state variables
  key0 = key
  hcode0 = hcode
  L1 = lnum
  L2 = lnum
  keyhash={}
  keyhash[key0]=hcode0
 # done with input
 f.close()
 # loop done.  Process last one
 keys = keyhash.keys() # list of keys
 sorted_keys = sorted(keys) # Why sort?
 for key1 in sorted_keys:
  out = "%s,%s,%s,%s" % (key1,keyhash[key1],L1,L2)
  outarr.append(out)
 #--- output phase
 for out in outarr:
  fout.write("%s\n" % out)
 fout.close()
 # summary messages
 print n,"records in",filein
 print len(outarr),"records written to",fileout

if __name__=="__main__": 
 filein = sys.argv[1] #  extract_keys.txt
 fileout = sys.argv[2] # extract_keys_a.txt
 extract_keys_a(filein,fileout)
