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
import csv
from collections import defaultdict
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
            k1 = re.sub(r'\[[0-9a-z]*\]$', '', k1)
            k1 = k1.rstrip()
            # <gk>ἀ</gk>, <gk>ἀν</gk> -> ἀ,ἀν
            greekWords = greekWords.replace('<gk>', '')
            greekWords = greekWords.replace('</gk>', '')
            gk = re.sub('[ ]*', '', greekWords)
            print(k1 + ':' + pc + ':' + gk)
            flog.write(k1 + ':' + pc + ':' + gk + '\n')
    flog.close()


def link_to_text(hw):
    return '[' + hw + '](https://sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/getword.php?key=' + hw + ')'

def link_to_pdf(pc):
    return '[' + pc + '](https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=MW&page=' + pc + ')'

def compare_both_logs(logFile1, logFile2, diffMd):
    set1 = set()
    fdiff = codecs.open(diffMd, 'w', 'utf-8')
    fdiff.write('|headword|pagecolumn|cologne|andhrabharati|\n')
    fdiff.write('|---|---|---|---|\n')
    with codecs.open(logFile1, 'r', 'utf-8') as fin1:
        log1Reader = csv.reader(fin1, delimiter=':')
        for row in log1Reader:
            set1.add(tuple(row))
    set2 = set()
    with codecs.open(logFile2, 'r', 'utf-8') as fin2:
        log1Reader = csv.reader(fin2, delimiter=':')
        for row in log1Reader:
            set2.add(tuple(row))
    diff1 = set1 - set2
    diff2 = set2 - set1

    result = []
    for [a, b, c] in diff1:
        result.append([a, b, c, ''])
    for [a, b, c] in diff2:
        result.append([a, b, '', c])
    result.sort()
    for [a, b, c, d] in result:
        print(a + '\t' + b + '\t' + c + '\t' + d)
        fdiff.write('|' + link_to_text(a) + '|' + link_to_text(b) + '|' + c + '|' + d + '|\n')
    fdiff.close()


if __name__ == "__main__":
    baseFile = os.path.join('..', '..', 'csl-orig', 'v02', 'mw', 'mw.txt')
    ABFile = 'MW_Gk_words.txt'
    outFile = 'mw1.txt'
    logFile1 = 'log_greek.txt'
    extract_greek(baseFile, logFile1)
    logFile2 = 'log_greek_AB.txt'
    extract_greek_AB(ABFile, logFile2)
    diffMd = 'greek_diff.md'
    compare_both_logs(logFile1, logFile2, diffMd)
