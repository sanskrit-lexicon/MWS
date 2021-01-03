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
import re
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
                pc = meta['pc']
                k1 = meta['k1']
            if '<lang n="greek">' in lin:
                greekData = re.findall('<lang n="greek">([^<]*)</lang>', lin)
                gk = ','.join(greekData)
                print(k1 + ':' + pc + ':' + gk)
                flog.write(k1 + ':' + pc + ':' + gk + '\n')
    flog.close()


def extract_greek_AB(ABFile, logFile):
    flog = codecs.open(logFile, 'w', 'utf-8')
    with codecs.open(ABFile, 'r', 'utf-8') as fin:
        for lin in fin:
            lin = lin.rstrip()
            [hwtype, pc, k1, greekWords] = lin.split('\t')
            # aMh [2] -> aMh
            k1 = re.sub('[^A-Za-z]*', '', k1)
            # <gk>ἀ</gk>, <gk>ἀν</gk> -> ἀ,ἀν
            greekWords = greekWords.replace('<gk>', '')
            greekWords = greekWords.replace('</gk>', '')
            gk = greekWords.replace(', ', '')
            print(k1 + ':' + pc + ':' + gk)
            flog.write(k1 + ':' + pc + ':' + gk + '\n')
    flog.close()


if __name__ == "__main__":
    baseFile = os.path.join('..', '..', 'csl-orig', 'v02', 'mw', 'mw.txt')
    ABFile = 'MW_Gk_words.txt'
    outFile = 'mw1.txt'
    logFile1 = 'log_greek.txt'
    # extract_greek(baseFile, logFile1)
    logFile2 = 'log_greek_AB.txt'
    extract_greek_AB(ABFile, logFile2)
