# -*- coding: utf-8 -*-
"""Place greek text to its proper place in mw.txt

Author - drdhaval2785@gmail.com
Date - 03 January 2021

Usage - python3 place_greek_text.py

Input files -
1. mw.txt
2. MW_Gk_words.txt

Output files -
1. mw1.txt having greek text placed at their respective place.
2. log_greek.txt having details about headword, lnum and lines changed.
"""
import os
import codecs
from parseheadline import parseheadline


def extract_greek(baseFile, logFile):
    flog = codecs.open(logFile, 'w', 'utf-8')
    with codecs.open(baseFile, 'r', 'utf-8') as fin:
        lnum = ''
        pc = ''
        k1 = ''
        for lin in fin:
            if lin.startswith('<L>'):
                meta = parseheadline(lin)
                lnum = meta['L']
                pc = meta['pc']
                k1 = meta['k1']
            if '<lang n="greek">' in lin:
                print(';' + k1 + ':' + lnum + ':' + pc)
                print(lin)
                flog.write(';' + k1 + ':' + lnum + ':' + pc + '\n')
                flog.write(lin)
    flog.close()


if __name__ == "__main__":
    baseFile = os.path.join('..', '..', 'csl-orig', 'v02', 'mw', 'mw.txt')
    greekFile = 'MW_Gk_words.txt'
    outFile = 'mw1.txt'
    logFile = 'log_greek.txt'
    extract_greek(baseFile, logFile)
