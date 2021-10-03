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


if __name__ == "__main__":
	with codecs.open('ab_lang.tsv', 'r', 'utf-8') as csvfile:
		abreader = csv.reader(csvfile, delimiter='\t')
		for row in abreader:
			linenum = row[0]
			hw = row[1]
			abdata = row[2]
			colognedata = row[4]
			print(hw)
