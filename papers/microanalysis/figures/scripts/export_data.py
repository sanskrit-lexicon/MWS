#!/usr/bin/env python3
"""Export microanalysis data to JSON for figures + microsite.

Generates:
  data/article-type-counts.json
  data/block-counts.json
  data/block-by-type-matrix.json
  data/fullness-distribution.json
  data/avg-fullness-by-type.json
  data/dict-totals.json
  data/source-coverage.json   (Option F)
  data/source-totals.json
"""
import json
import re
import os
import sys
from collections import Counter, defaultdict
sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.normpath(os.path.join(HERE, '..'))
DATA_DIR = os.path.join(FIG_DIR, 'data')
TMP = r'C:/Users/user/AppData/Local/Temp'


def classify_type(body, k2, ecode):
    has_compound_marker = ('—' in k2) or ('-' in k2)
    has_genuineroot = 'genuineroot' in body
    lex = {
        'noun-m': '<lex>m.</lex>' in body,
        'noun-f': '<lex>f.</lex>' in body,
        'noun-n': '<lex>n.</lex>' in body,
        'adjective-mfn': '<lex>mfn.</lex>' in body,
        'indeclinable': '<lex>ind.</lex>' in body,
        'noun-mn': '<lex>mn.</lex>' in body,
    }
    types = []
    if has_genuineroot:
        types.append('root')
    if has_compound_marker and ecode.startswith('3'):
        types.append('compound')
    if ecode.startswith('1A'):
        types.append('continuation')
    if ecode.startswith('2'):
        types.append('derived')
    for k, v in lex.items():
        if v and not types:
            types.append(k)
            break
    if '<bot>' in body:
        types.append('botanical')
    if '<bio>' in body:
        types.append('biographical')
    if '<lang>' in body:
        types.append('etymological-ie')
    if '/' in k2:
        types.append('vedic-accented')

    ls_in_body = re.findall(r'<ls>([^<]+)</ls>', body)
    if ls_in_body and all(s.strip().rstrip(',.;:') == 'L' for s in ls_in_body):
        types.append('lexicographer-only')

    if not types:
        types.append('other')
    return types


def detect_blocks(body):
    blocks = set()
    blocks.add('F01')  # header — always
    if re.search(r'<s>[^<]+</s>', body) or re.search(r'<s1>', body):
        blocks.add('F02')
    if '<hom>' in body:
        blocks.add('F03')
    if '<lex>' in body:
        blocks.add('F04')
    if '<ab>cl.</ab>' in body or '<ab>P.</ab>' in body or '<ab>Ā.</ab>' in body:
        blocks.add('F05')
    if '√' in body or '<ab>fr.</ab>' in body:
        blocks.add('F06')
    if '<lang>' in body:
        blocks.add('F07')
    if len(re.findall(r'<s>([^<]+)</s>', body)) > 1:
        blocks.add('F08')
    if re.search(r'\([^)]{50,}', body):
        blocks.add('F09')
    if '¦' in body and len(body) > 30:
        blocks.add('F10')
    if re.search(r'\b\d\)\s', body):
        blocks.add('F11')
    if '<ls>' in body:
        blocks.add('F12')
    if '<ls>L.</ls>' in body:
        blocks.add('F13')
    if '<bot>' in body:
        blocks.add('F14')
    if '<bio>' in body or '<s1>' in body:
        blocks.add('F15')
    if 'q.v.' in body or '<ab>cf.</ab>' in body or '<ab>id.</ab>' in body:
        blocks.add('F16')
    if '<info' in body:
        blocks.add('F17')
    if '{{' in body and '->' in body:
        blocks.add('F18')
    return blocks


def main():
    print('Loading mw.txt...')
    with open(os.path.join(TMP, 'mw.txt'), encoding='utf-8') as f:
        text = f.read()

    pattern = re.compile(
        r'<L>([0-9.]+)<pc>([^<]*)<k1>([^<\r\n]*?)<k2>([^<\r\n]*?)(?:<h>([^<]*))?<e>([^\r\n]+?)\r?\n(.*?)\r?\n<LEND>',
        re.DOTALL
    )

    type_order = ['root', 'noun-m', 'noun-f', 'noun-n', 'noun-mn', 'adjective-mfn',
                  'indeclinable', 'compound', 'derived', 'continuation',
                  'lexicographer-only', 'etymological-ie', 'botanical',
                  'biographical', 'vedic-accented', 'other']
    block_order = [f'F{i:02d}' for i in range(1, 19)]

    type_counts = Counter()
    block_counts = Counter()
    matrix = defaultdict(lambda: Counter())  # type -> Counter of blocks
    fullness_dist = Counter()
    type_total_blocks = defaultdict(int)
    type_entry_counts = defaultdict(int)

    n_entries = 0
    for m in pattern.finditer(text):
        lnum, pc, k1, k2, h, ecode, body = m.groups()
        ecode = ecode.strip()
        types = classify_type(body, k2, ecode)
        blocks = detect_blocks(body)
        n_entries += 1
        fullness_dist[len(blocks)] += 1
        for t in types:
            type_counts[t] += 1
            type_total_blocks[t] += len(blocks)
            type_entry_counts[t] += 1
            for b in blocks:
                matrix[t][b] += 1
        for b in blocks:
            block_counts[b] += 1

    print(f'Parsed {n_entries:,} entries')

    # Write JSON files
    article_type_data = [
        {'type': t, 'count': type_counts.get(t, 0)} for t in type_order if type_counts.get(t, 0) > 0
    ]
    with open(os.path.join(DATA_DIR, 'article-type-counts.json'), 'w', encoding='utf-8') as f:
        json.dump({'total': n_entries, 'types': article_type_data}, f, indent=2, ensure_ascii=False)
    print('  wrote data/article-type-counts.json')

    with open(os.path.join(DATA_DIR, 'block-counts.json'), 'w', encoding='utf-8') as f:
        json.dump({'total': n_entries, 'blocks': [{'id': b, 'count': block_counts.get(b, 0)} for b in block_order]},
                  f, indent=2, ensure_ascii=False)
    print('  wrote data/block-counts.json')

    matrix_data = []
    for t in type_order:
        if type_counts.get(t, 0) == 0:
            continue
        row = {'type': t, 'count': type_counts[t]}
        for b in block_order:
            row[b] = matrix[t].get(b, 0)
            row[b + '_pct'] = round(100 * matrix[t].get(b, 0) / type_counts[t], 2) if type_counts[t] else 0
        matrix_data.append(row)
    with open(os.path.join(DATA_DIR, 'block-by-type-matrix.json'), 'w', encoding='utf-8') as f:
        json.dump({'total_entries': n_entries, 'blocks': block_order, 'types': type_order, 'matrix': matrix_data},
                  f, indent=2, ensure_ascii=False)
    print('  wrote data/block-by-type-matrix.json')

    fullness_data = [{'blocks': n, 'count': c} for n, c in sorted(fullness_dist.items())]
    with open(os.path.join(DATA_DIR, 'fullness-distribution.json'), 'w', encoding='utf-8') as f:
        json.dump({'total': n_entries, 'distribution': fullness_data}, f, indent=2, ensure_ascii=False)
    print('  wrote data/fullness-distribution.json')

    avg_fullness = []
    for t in type_order:
        if type_entry_counts.get(t, 0) > 0:
            avg_fullness.append({
                'type': t,
                'count': type_entry_counts[t],
                'avg_blocks': round(type_total_blocks[t] / type_entry_counts[t], 2)
            })
    with open(os.path.join(DATA_DIR, 'avg-fullness-by-type.json'), 'w', encoding='utf-8') as f:
        json.dump(avg_fullness, f, indent=2, ensure_ascii=False)
    print('  wrote data/avg-fullness-by-type.json')


if __name__ == '__main__':
    main()
