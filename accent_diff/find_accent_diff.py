# -*- coding: utf-8 -*-
"""Find out cases where csl-orig/v02/mw.txt differs in the headword accent from csl-orig/v02/pwg.txt

Usage - python3 find_accent_diff.py dict1 dict2 logfile
		python3 find_accent_diff.py ../../../cologne/csl-orig/v02/mw/mw.txt ../../../cologne/csl-orig/v02/pwg/pwg.txt log.html
"""
import codecs
import re
import sys
from collections import defaultdict
import parseheadline


def prepare_dict(filein):
	fin = codecs.open(filein, 'r', 'utf-8')
	result = defaultdict(list)
	for lin in fin:
		if lin.startswith('<L>'):
			meta = parseheadline.parseheadline(lin)
			k1 = meta['k1']
			k2 = meta['k2']
			k1 = k1.replace('—', '')
			k2 = k2.replace('—', '')
			if re.search('[\/^]', k2):
				if k2 not in result[k1]:
					result[k1].append(k2)
	return result


if __name__ == "__main__":
	filein1 = sys.argv[1]
	filein2 = sys.argv[2]
	fileout = sys.argv[3]
	fout = codecs.open(fileout, 'w', 'utf-8')
	print("Prepare dict from ", filein1)
	d1 = prepare_dict(filein1)
	print("Prepare dict from ", filein2)
	d2 = prepare_dict(filein2)
	for key in d1:
		if key in d2:
			if d1[key] != d2[key]:
				print(key, d1[key], d2[key])
				fout.write(key + '\t' + ','.join(d1[key]) + '\t' + ','.join(d2[key]) + '\n')
