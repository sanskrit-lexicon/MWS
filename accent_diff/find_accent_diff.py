# -*- coding: utf-8 -*-
"""Find out cases where csl-orig/v02/mw.txt differs in the headword accent from csl-orig/v02/pwg.txt

Usage - python3 find_accent_diff.py dict1 dict2 logtsv loghtml
		python3 find_accent_diff.py mw pwg log.tsv log.html
"""
import codecs
import re
import sys
import csv
from collections import defaultdict
import parseheadline


def prepare_dict(dict1):
	filein = '../../../cologne/csl-orig/v02/' + dict1 + '/' + dict1 + '.txt'
	fin = codecs.open(filein, 'r', 'utf-8')
	result = defaultdict(list)
	for lin in fin:
		if lin.startswith('<L>'):
			meta = parseheadline.parseheadline(lin)
			k1 = meta['k1']
			k2 = meta['k2']
			k1 = k1.replace('—', '')
			k1 = k1.replace('-', '')
			k2 = k2.replace('—', '')
			k2 = k2.replace('-', '')
			if re.search('[\/^]', k2):
				if k2 not in result[k1]:
					result[k1].append(k2)
	fin.close()
	return result


def write_diff_to_tsv(d1, d2, file_tsv):
	fout = codecs.open(file_tsv, 'w', 'utf-8')
	for key in d1:
		if key in d2:
			if d1[key] != d2[key]:
				print(key, d1[key], d2[key])
				fout.write(key + '\t' + ','.join(d1[key]) + '\t' + ','.join(d2[key]) + '\n')
	fout.close()


def write_diff_to_html(file_tsv, file_html, dict1, dict2):
	fin = codecs.open(file_tsv, 'r', 'utf-8')
	reader = csv.reader(fin, delimiter='\t')
	fout = codecs.open(file_html, 'w', 'utf-8')
	fout.write('<html><body><table>')
	fout.write('<tr><th>key</th><th>' + dict1 + '</th><th>' + dict2 + '</th></tr>')
	for row in reader:
		(key, d1, d2) = row
		fout.write('<tr><td>' + key + '</td><td><a target="_blank" href="https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=' + dict1.upper() + '&key=' + key + '">' + d1 + '</a></td><td><a target="_blank" href="https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=' + dict2.upper() + '&key=' + key + '">' + d2 + '</a></td></tr>\n')
	fout.write('</table></body></html>')
	fin.close()
	fout.close()
# https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=PWG&key=rAma

if __name__ == "__main__":
	dict1 = sys.argv[1]
	dict2 = sys.argv[2]
	out_tsv = sys.argv[3]
	out_html = sys.argv[4]
	"""
	print("Prepare dict from ", filein1)
	d1 = prepare_dict(dict1)
	print("Prepare dict from ", filein2)
	d2 = prepare_dict(filein2)
	print('Write difference to ', out_tsv)
	write_diff_to_tsv(d1, d2, out_tsv)
	"""
	print('Prepare HTML in ', out_html)
	write_diff_to_html(out_tsv, out_html, dict1, dict2)
	