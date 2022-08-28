#-*- coding:utf-8 -*-
"""make_oldnew1_range.py
"""
import sys,re,codecs
if __name__=="__main__":
 lnum1 = int(sys.argv[1])
 lnum2 = int(sys.argv[2])
 if lnum2 == 0: # for just one line
  lnum2 = lnum1
 filein = sys.argv[3] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[4] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 iline1 = lnum1 - 1
 iline2 = lnum2 - 1
 with codecs.open(fileout,"w","utf-8") as f:
  
  for iline,line in enumerate(lines):
   if line.startswith('<L>'):
    meta = re.sub(r'<k2>.*$','',line)
   if iline1<=iline<=iline2:
    outarr = []
    lnum = iline+1
    if iline == iline1:
     outarr.append('; %s' %meta)
    outarr.append('%s old %s' %(lnum,line))
    outarr.append(';')
    outarr.append('%s new %s' %(lnum,line))
    outarr.append(';')
    for out in outarr:
     f.write(out+'\n')
 print('output written to',fileout)

  
