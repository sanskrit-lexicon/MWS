#!/usr/bin/env python3
"""Pass A codebook annotator for G5.

Independently derived from G5_GOLD_SAMPLE_SPEC.md's F01-F18 definitions and
MWS/DATA_DICTIONARY.md's tag inventory -- NOT from papers/microanalysis/analysis/.
Produces a first-pass mechanical reading of each record's block set; borderline
records (F13 hedge-vs-citation, F16 boundary, F09 commentary, F08 forms) are
then hand-reviewed and may be overridden -- see CODEBOOK_A.md and the notes
column for which rows were touched by hand.
"""
import re
import sys
import csv

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


def annotate(text):
    blocks = set()
    blocks.add('F01')  # record header: always present by construction

    body = text.split('¦', 1)
    head = body[0]
    gloss = body[1] if len(body) > 1 else ''

    if re.search(r'<s>[^<]', head) or re.search(r'<s1>[^<]', head):
        blocks.add('F02')
    if '<hom>' in text:
        blocks.add('F03')
    if '<lex>' in text or '<lex ' in text:
        blocks.add('F04')
    if ('<ab>cl.</ab>' in text or '<ab>P.</ab>' in text or '<ab>Ā.</ab>' in text
            or re.search(r'verb="(genuineroot|root|gati|nom|pre)"', text)):
        blocks.add('F05')
    if '√' in text or '<etym>' in text:
        blocks.add('F06')
    if '<lang>' in text or '<gk>' in text:
        blocks.add('F07')
    s_count_head = len(re.findall(r'<s>[^<]', head))
    if 'lexcat=' in text or s_count_head > 1 or re.search(r'<ab>(Caus|Desid|Intens)\.</ab>', text):
        blocks.add('F08')
    if '<div n="vp"' in text or re.search(r'<ab>(cf|prob|fr)\.</ab>', text):
        blocks.add('F09')
    if gloss.strip() or '<div n="to"' in text:
        blocks.add('F10')
    if re.search(r'<div n="(P|p|1)"', text):
        blocks.add('F11')
    ls_tags = re.findall(r'<ls>([^<]*)</ls>', text)
    non_hedge_ls = [t for t in ls_tags if t.strip() != 'L.']
    hedge_ls = [t for t in ls_tags if t.strip() == 'L.']
    # F12/F13 are independent booleans, not mutually exclusive: a record can
    # carry a named-text citation for one sense AND the L. hedge for another
    # (rule 4 disambiguates what <ls>L.</ls> itself means, not whether F12
    # can co-occur elsewhere in the same record).
    if non_hedge_ls:
        blocks.add('F12')
    if hedge_ls:
        blocks.add('F13')
    if '<bot>' in text:
        blocks.add('F14')
    if '<bio>' in text or ('<s1>' in text and '<bot>' not in text):
        blocks.add('F15')
    if ('<ab>id.</ab>' in text or 'type="phw"' in text or '<pcol>' in text
            or ('phwchild=' in text or 'phwparent=' in text)):
        blocks.add('F16')
    if '<info' in text:
        blocks.add('F17')
    if '<chg' in text:
        blocks.add('F18')

    return blocks


MW_PATH = '../../../../csl-orig/v02/mw/mw.txt'


def load_mw_records_by_L(path):
    by_L = {}
    with open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')
    cur = []
    for line in lines:
        if line.startswith('<L>'):
            if cur:
                text = '\n'.join(cur)
                by_L[re.match(r'<L>([^<]*)', cur[0]).group(1)] = text
            cur = [line]
        elif line.strip() == '<LEND>':
            cur.append(line)
            text = '\n'.join(cur)
            by_L[re.match(r'<L>([^<]*)', cur[0]).group(1)] = text
            cur = []
        else:
            if cur:
                cur.append(line)
    return by_L


def main():
    rows = []
    with open('../G5_gold_sample_skeleton.csv', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    full_text = load_mw_records_by_L(MW_PATH)

    for row in rows:
        text = full_text[row['L']]
        blocks = annotate(text)
        row['gold_blocks_A'] = ';'.join(sorted(blocks, key=lambda b: int(b[1:])))

    with open('annotations.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"Annotated {len(rows)} rows", file=sys.stderr)


if __name__ == '__main__':
    main()
