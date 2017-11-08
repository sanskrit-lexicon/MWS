# coding=utf-8
""" filter_simple.py
    
"""
import sys,re,codecs


def filter_abbrev(inlines):
 """ find right angle char without preceding left angle char """
 counter = {}
 ntot=0
 for idx,line in enumerate(inlines):
  results = re.findall(r'<ab>(.*?)</ab>',line)
  for result in results:
   if result not in counter:
    counter[result]=0
   counter[result] = counter[result] + 1
   ntot = ntot + 1
 nkeys = len(counter.keys())
 print ntot,"instances of <ab> tag"
 print nkeys,"distinct abbreviations"
 return counter
 
if __name__=="__main__":
 filein = sys.argv[1]  # xxxwithmeta1.txt
 fileout = sys.argv[2] # results
 with codecs.open(filein,"r","utf-8") as f:
  inlines = [x.rstrip('\r\n') for x in f]
  print len(inlines),"lines read from",filein
 counter = filter_abbrev(inlines)
 keys = counter.keys()
 keys = sorted(keys,key = lambda x: x.lower())
 with codecs.open(fileout,"w","utf-8") as fout:
  for key in keys:
   fout.write('%s %s\n' %(key,counter[key]))
 print len(keys),"lines written to",fileout
