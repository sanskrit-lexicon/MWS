# This Python file uses the following encoding: utf-8
"""
Usage:
python issue_632.py
"""
from __future__ import print_function
import re
import codecs
import sys
import os
import csv


def read_mw_devanagari():
	filein = os.path.join('..', '..', 'csl-devanagari', 'v02', 'mw', 'mw.txt')
	fin = codecs.open(filein, 'r', 'utf-8')
	data = fin.read()
	fin.close()
	return data.split('\n')


def adjust_abdata(abdata):
	abdata = abdata.replace('á', 'á')
	abdata = abdata.replace('é', 'é')
	abdata = abdata.replace('û', 'û')
	abdata = abdata.replace('î', 'î')
	abdata = abdata.replace('a0', 'ä')
	abdata = abdata.replace('e0', 'ë')
	abdata = abdata.replace('ē', 'ē')
	abdata = abdata.replace('<auml/>', 'ä')
	abdata = abdata.replace('<uuml/>', 'ö')
	return abdata

if __name__ == "__main__":
	mwdata = read_mw_devanagari()
	with codecs.open('ab_lang1.tsv', 'r', 'utf-8') as csvfile:
		abreader = csv.reader(csvfile, delimiter='\t')
		for row in abreader:
			m = re.search('Line ([0-9]+):', row[0])
			linenum = int(m.group(1)) - 1
			hw = row[1]
			abdata = row[4]
			abdata = adjust_abdata(abdata)
			ablangs = re.findall('<lang.*?>(.*?)</lang>', abdata)
			colognedata = mwdata[linenum]
			col1 = re.sub('<lang.*?>', '<lang>', colognedata)
			col1 = re.sub('<etym>(.*?)</etym>', '<lang>\g<1></lang>', col1)
			colognelangs = re.findall('<lang.*?>(.*?)</lang>', col1)
			if ablangs != colognelangs:
				print(linenum)
				print([x for x in ablangs if x not in colognelangs])
				print([x for x in colognelangs if x not in ablangs])
				print(abdata)
				print(colognedata)
				print()
