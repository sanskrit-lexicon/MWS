# coding=utf-8
""" Dhaval Patel. May 17, 2017
 parseheadline parses a text string of the repeated forms
  <key>value.
 It returns a dictionary d, so that d['key']=value.
 Note that the order of the <key>value pairs is not relevant.
"""
from __future__ import print_function
import sys
import re
# Make code python2, python3 compatible.
if sys.version_info[0] > 2:
    xrange = range

def parseheadline(headline):
	"""<L>16850<pc>292-3<k1>visarga<k2>visarga<h>1<e>2"""
	headline = headline.strip()
	splits = re.split('[<]([^>]*)[>]([^<]*)',headline)
        #print(splits)
	result = {}
	for i in xrange(len(splits)):
		if i % 3 == 1:
			result[splits[i]] = splits[i+1]
	return result
def test():
 testlines=[
  "<L>16850<pc>292-3<k1>visarga<k2>visarga<h>1<e>2",
  "<L>16850<pc>292-3<k1>visarga<k2>visarga<h>1<e>",
  "<L><pc>292-3<k1>visarga<k2>visarga<h>1<e>",
  "nokey<key>val",
  "nokeyval",
 ]
 for idx,line in enumerate(testlines):
  ntest = idx+1
  try:
   result = parseheadline(line)
  except:
   result = 'Error from parseheadline'
  # generate array of lines for output
  outarr =[]
  outarr.append("parseheadline test # %s"% ntest)
  outarr.append("headline: %s" % line)
  outarr.append("  result: %s" % result)
  outarr.append("")
  # send outarr to stdout
  for out in outarr:
   print(out.encode('utf-8'))
if __name__ == "__main__":
 test()
