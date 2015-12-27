#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from lxml import etree # lxml.de
import re
import codecs
import datetime
import sys

def printtimestamp():
	return datetime.datetime.now()
#xmlfilename = sys.argv[1]  # e.g., ../pw.xml
def parsefile():
	xmlfilename = '../../Cologne_localcopy/mw/mwxml/xml/mw.xml'
	print "Using xmlfile",xmlfilename
	# Function to return timestamp
	print "Parsing started at", printtimestamp()
	entries = etree.parse(xmlfilename) # Parse xml
	print "Parsing ended at", printtimestamp()
	return entries
def removecrap(word):
	repl = [('-',''),('/',''),('^',''),(' ',''),("'","")]
	for (a,b) in repl:
		word = word.replace(a,b)
	word = re.sub('[0-9]$','',word)
	return word

def scrape():
	entries = parsefile() # Fetched parse XML.
	g = codecs.open('k1k2clash.txt', 'w','utf-8') # Opened file to store
	mwk1 = entries.xpath('/mw/*/h/key1')
	mwk2 = entries.xpath('/mw/*/h/key2')
	k1 = [etree.tostring(member, method="text") for member in mwk1]
	k2 = [etree.tostring(member, method="text") for member in mwk2]
	for i in xrange(len(k2)):
		if not (k1[i].strip() == removecrap(k2[i]).strip()):
			g.write(k1[i]+':'+removecrap(k2[i])+'\n')
	g.close()
(mwk1,mwk2) = scrape()
