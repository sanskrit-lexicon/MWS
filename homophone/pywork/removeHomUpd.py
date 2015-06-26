"""removeHomUpd.py June 16, 2015
 Read a version of monier.xml, and generate update records
 Based on removeHom.py
"""
import sys, re,codecs

def removeHomUpd(filein,fileout,fileout1):
 fout = codecs.open(fileout,"w",'utf-8')
 fout1 = codecs.open(fileout1,"w",'utf-8')
 f = codecs.open(filein,"r",'utf-8')
 n = 0 # number of lines read
 nchg = 0 # Number of lines changed
 for line in f:
  line = line.rstrip('\r\n')
  n = n + 1
  m = re.search(r'<H[^>]*[ABC]><h>.*?<hom>.*</h>',line)
  if not m:
   #nothing to do
   continue
  lineout = re.sub('</key2><hom>.*?</hom>','</key2>',line)
  if line == lineout: 
   # internal consistency check
   print "Unexpected @ line",n
   print line.encode('utf-8')
   continue
  # generate outputs
  nchg = nchg + 1
  m = re.search(r'<key1>(.*?)</key1>.*<L.*?>(.*?)</L>',line)
  if not m:
   print "INTERNAL ERROR"
   print line.encode('utf-8')
   continue
  key1 = m.group(1)
  L = m.group(2)
  # generate update record from lineout
  fout.write("Update\n")
  fout.write("<L>%s</L>\n" % L)
  fout.write("%s\n" % lineout)
  # generate old/new record pair in 2nd output
  fout1.write("Case %d: L=%s, key1=%s\n" %(nchg,L,key1))
  fout1.write("old:\n%s\n" % line)
  fout1.write("\nnew:\n%s\n" % lineout)
  fout1.write("\n%s\n" %('-'*72))
  if False and (nchg == 50): 
   print "breaking after 50 cases"
   break
 fout.close()
 fout1.close()
 f.close()
 print n,"lines from",filein
 print nchg,"changes written to",fileout
if __name__=="__main__": 
 filein = sys.argv[1] #  monier.xml
 fileout = sys.argv[2] # updlogs/log_20150616-01.txt
 fileout1 = sys.argv[3] # updlogs/notes_20150616.txt
 removeHomUpd(filein,fileout,fileout1)
