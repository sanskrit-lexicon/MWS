#!/usr/bin/env python
"""Mechanical A/B disagreement diff for the G5 gold sample (SPEC-2 step 3).

Reads pass_a/annotations.csv (gold_blocks_A) and pass_b/annotations.csv
(gold_blocks_B), computes the per-record block-set symmetric difference, and
writes disagreements.csv: one row per (record, block) where exactly one pass
marked the block. Per-block disagreement counts go into `;`-prefixed header
comment lines, per SPEC-2's acceptance criteria.

Usage:  python make_disagreements.py
Run from review_packets/g5/.
"""
import csv
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ALL_BLOCKS = [f'F{i:02d}' for i in range(1, 19)]


def load(path, col):
    rows = {}
    with open(path, encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            blocks = frozenset(b for b in r[col].split(';') if b)
            bad = blocks - set(ALL_BLOCKS)
            if bad:
                raise SystemExit(f'{path}: {r["sample_id"]} has invalid block ids {sorted(bad)}')
            rows[r['sample_id']] = (r, blocks)
    return rows


def main():
    a = load('pass_a/annotations.csv', 'gold_blocks_A')
    b = load('pass_b/annotations.csv', 'gold_blocks_B')
    if set(a) != set(b):
        raise SystemExit(f'sample_id mismatch: only-A={sorted(set(a)-set(b))} only-B={sorted(set(b)-set(a))}')

    per_block = Counter()
    out_rows = []
    rows_with_disagreement = 0
    for sid in sorted(a):
        ra, blocks_a = a[sid]
        rb, blocks_b = b[sid]
        if (ra['L'], ra['k1']) != (rb['L'], rb['k1']):
            raise SystemExit(f'{sid}: L/k1 mismatch between passes')
        diff = blocks_a ^ blocks_b
        if diff:
            rows_with_disagreement += 1
        for blk in sorted(diff):
            per_block[blk] += 1
            out_rows.append({
                'sample_id': sid,
                'L': ra['L'],
                'k1': ra['k1'],
                'stratum': ra['stratum'],
                'block': blk,
                'in_A': 'yes' if blk in blocks_a else 'no',
                'in_B': 'yes' if blk in blocks_b else 'no',
                'adjudicated': '',
                'adjudication_note': '',
            })

    with open('disagreements.csv', 'w', encoding='utf-8', newline='') as f:
        f.write('; G5 A/B disagreements — mechanical symmetric diff of gold_blocks_A vs gold_blocks_B\n')
        f.write(f'; records compared: {len(a)}; records with >=1 disagreement: '
                f'{rows_with_disagreement}; exact-agreement records: {len(a) - rows_with_disagreement}\n')
        f.write(f'; total (record, block) disagreement rows: {len(out_rows)}\n')
        f.write('; per-block disagreement counts: '
                + ' '.join(f'{blk}={per_block[blk]}' for blk in ALL_BLOCKS if per_block[blk])
                + '\n')
        w = csv.DictWriter(f, fieldnames=['sample_id', 'L', 'k1', 'stratum', 'block',
                                          'in_A', 'in_B', 'adjudicated', 'adjudication_note'])
        w.writeheader()
        w.writerows(out_rows)

    print(f'records: {len(a)}  disagreeing records: {rows_with_disagreement}  rows: {len(out_rows)}')
    for blk in ALL_BLOCKS:
        if per_block[blk]:
            print(f'  {blk}: {per_block[blk]}')


if __name__ == '__main__':
    main()
