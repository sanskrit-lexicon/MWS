"""removeHom.py April 6, 2015
 Read a version of monier.xml, and remove un-needed homonym codes.
 Essentially, homonym codes appearing in head (<h>) when
 category (<H..>) tag-name ends in A,B,C  (e.g. <H2B>).
 There is no change required to the DTD
"""
import sys, re,codecs

def removeHom(filein,fileout):
 fout = codecs.open(fileout,"w",'utf-8')
 f = codecs.open(filein,"r",'utf-8')
 n = 0 # number of lines read
 nchg = 0 # Number of lines changed
 for line in f:
  n = n + 1
  m = re.search(r'<H[^>]*[ABC]><h>.*?<hom>.*</h>',line)
  if not m:
   fout.write(line)
   continue
  lineout = re.sub('</key2><hom>.*?</hom>','</key2>',line)
  if line == lineout: 
   print "Unexpected @ line",n
   print line.encode('utf-8')
  else:
   nchg = nchg + 1
  fout.write(lineout)
 fout.close()
 f.close()
 print n,"lines from",filein
 print n,"lines to",fileout
 print nchg,"lines changed"
if __name__=="__main__": 
 filein = sys.argv[1] #  monier.xml
 fileout = sys.argv[2] # monier_X.xml
 removeHom(filein,fileout)
