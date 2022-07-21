#-*- coding:utf-8 -*-
"""make_mwauth_entries.py
   inputs:
    -  a first code (xx.xx)  which should not overlap codes 
          already in mwauth.txt
    -  a list of ls abbreviations (in a file, one per line)
   constructs prototype lines for mwauth.txt and
    writes to the output file.
"""
import sys,re,codecs

def init_auths(abbrevs,firstcode):
 outarr = []
 code = float(firstcode)
 for a in abbrevs:
  code = code + .01
  atype = 'ti'
  tip = '<expandNorm><ti>Unknown reference</ti> [Cologne Addition]</expandNorm>'
  out = '%5.2f\t%s\t%s\t%s\t%s' %(code,a,a,atype,tip)
  outarr.append(out)
 return outarr
if __name__=="__main__":
 firstcode = sys.argv[1]
 if not re.search(r'^[0-9][0-9][.][0-9][0-9]$', firstcode):
  print('Invalid first code:',firstcode)
  exit(1)
 filein = sys.argv[2] # ls abbreviations
 fileout = sys.argv[3] # 
 with codecs.open(filein,"r","utf-8") as f:
  abbrevs = [x.rstrip('\r\n') for x in f]
 outarr = init_auths(abbrevs,firstcode)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
    f.write(out+'\n')
 print(len(outarr),'Records written to',fileout)
 
