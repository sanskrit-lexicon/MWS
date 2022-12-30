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

def write_script(fileout,colornames,mwfilesd,dirout):
 with codecs.open(fileout,"w","utf-8") as f:
   #n = len(shfile)
   #f.write('echo "copying %s files from vol%s"\n' %(n,vol))
   for (page4str,oldfile) in colornames:
    newfile = mwfilesd[page4str]
    out = 'cp %s %s/%s' %(oldfile,dirout,newfile)
    f.write(out+'\n')
 print(len(colornames),"lines written to",fileout)

def read_main_filenames(filein):
 with codecs.open(filein,"r","utf-8") as f:
  d = {}
  for x in f:
   x =  x.rstrip('\r\n')  # the filename, absent .pdf
   m = re.search(r'^mw([0-9][0-9][0-9][0-9])-',x)
   if m == None:
    m = re.search(r'^mw([0-9][0-9][0-9][0-9])$',x)
   if m == None:
    print('read_main_filenames skipping:',x)
    continue
   page4str = m.group(1)
   newfile = x + '.pdf'
   d[page4str] = newfile
 keys = d.keys()
 print(len(keys),"read from",filein)  # 1333, as expected
 return d

def read_colornames(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = []
  for x in f:
   x =  x.rstrip('\r\n')  # the filename, absent .pdf
   # 'mwcolorpages/MW-main (coloured) 109.pdf'
   m = re.search(r'^(mwcolorpages/MW-main \(coloured\)) ([0-9]+)[.](pdf)$',x)
   if m == None:
    print('read_colornames problem:',x)
    exit(1)
   pfx = m.group(1)
   filename = "'" + x + "'" # single quote since spaces in x
   ipage = int(m.group(2))
   page4str = '%04d' % ipage
   sfx = m.group(3) # pdf
   rec = (page4str,filename)
   recs.append(rec)
 
 print(len(recs),"read from",filein)  # 1333, as expected
 return recs

if __name__ == "__main__":
 filein = sys.argv[1] # mwfiles.txt
 filein1 = sys.argv[2] # mwcolornames.txt
 fileout = sys.argv[3] # output script
 dirout = sys.argv[4] # target directory of copy
 mwfilesd = read_main_filenames(filein)
 colornames = read_colornames(filein1) # (page,pathname)
 write_script(fileout,colornames,mwfilesd,dirout)
 
 
