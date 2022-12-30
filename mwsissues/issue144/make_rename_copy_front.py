import sys,re,codecs
import os

def makesh(vol,voldata,dirout='pdfpages'):
 ans = []
 dirin = voldata['dirin']
 filepatin = voldata['filepat']
 #dirout = 'pdfpages'
 filepatout = 'rgorr_%s.#.pdf' % vol
 # title page (optional)
 if voldata['pagetitle'] != None:
  N = voldata['pagetitle']['N']
  X = voldata['pagetitle']['X']
  filein = filepatin.replace('#','%s' % N)
  pathin = '%s/%s' % (dirin,filein)
  fileout = filepatout.replace('#',X)
  pathout = '%s/%s' %(dirout,fileout)
  pathinq = "'%s'" %pathin
  sh = "cp %s %s" %(pathinq,pathout)
  ans.append(sh)
 #
 N1 = voldata['N1']
 N2 = voldata['N2']
 Xdiff = voldata['Xdiff']
 for N in range(N1,N2+1):
  XN = N - Xdiff
  X = '%03d' % XN
  filein = filepatin.replace('#','%s' % N)
  pathin = '%s/%s' % (dirin,filein)
  fileout = filepatout.replace('#',X)
  pathout = '%s/%s' %(dirout,fileout)
  # quote  pathin since there is a space
  pathinq = "'%s'" %pathin
  sh = "cp %s %s" %(pathinq,pathout)
  ans.append(sh)
 return ans 

def write_script(fileout,frontnames,dirin,dirout):
 with codecs.open(fileout,"w","utf-8") as f:
   for name in frontnames:
    oldfile = '%s/%s.pdf' %(dirin,name)
    newfile = '%s/%s.pdf' %(dirout,name)
    out = 'cp %s %s' %(oldfile,newfile)
    f.write(out+'\n')
 print(len(frontnames),"lines written to",fileout)

def read_frontnames(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for x in f:
   x =  x.rstrip('\r\n')  # the filename, absent .pdf
   recs.append(x)
 print(len(recs),"read from",filein)  # 36, as expected
 return recs

if __name__ == "__main__":
 filein = sys.argv[1] # frontfiles.txt
 fileout = sys.argv[2] # output script
 dirin = sys.argv[3] # location of old files
 dirout = sys.argv[4] # target directory of copy
 frontnames = read_frontnames(filein)
 write_script(fileout,frontnames,dirin,dirout)
 
 
