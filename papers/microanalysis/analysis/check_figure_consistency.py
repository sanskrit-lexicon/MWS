#!/usr/bin/env python3
"""S11 — Cross-figure data consistency audit.

Verifies that the four Tier-1 figures + cross-dict data are internally consistent:
  - Total records: 286,561 across all sources
  - Per-type counts: article-type-counts.json == block-by-type-matrix.json
  - Cross-dict MW: records + ls_per_record + cite% internally consistent
  - MW common-block data: cite% + hedge% match known facts
  - Per-dict blocks.json record counts match expected values
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '..', 'figures', 'data'))

errors = []

def check(label, cond, detail=''):
    if cond:
        print(f'  OK   {label}')
    else:
        print(f'  FAIL {label}: {detail}')
        errors.append(label)

def load(name):
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        print(f'  MISS {name} (file not found)')
        return None
    with open(path, encoding='utf-8') as f:
        return json.load(f)


print('=== S11 Cross-figure data consistency audit ===\n')

# Load all data files
atc = load('article-type-counts.json')      # {'total': N, 'types': [{'type':..,'count':..},...]}
bbm = load('block-by-type-matrix.json')     # {'total_entries':N, 'blocks':[..], 'types':[..], 'matrix':[rows]}
bc  = load('block-counts.json')             # {'total':N, 'blocks':[{'id':'F01','count':N},...]}
crd = load('cross-dict.json')               # {'blocks':[..], 'dicts':[{'code','records','ls_per_record','blocks_pct',...}]}
mw_blk = load('mw_blocks.json')            # common-block format: total_entries, blocks_pct, matrix
print()

# ---- 1. Total record count (286,561 everywhere) ----
print('--- 1. Total record count (should be 286,561 MW records) ---')
EXPECTED_TOTAL = 286561

if atc:
    check('article-type-counts total', atc['total'] == EXPECTED_TOTAL,
          f"got {atc['total']}")
    # Types are orthogonal (compound+vedic-accented+lexicographer-only can co-exist).
    # Sum > total is expected. Verify sum is in a reasonable range [total, 2×total].
    type_sum = sum(r['count'] for r in atc['types'])
    check('article-type-counts sum-of-types in [total, 2×total] (orthogonal types)',
          atc['total'] <= type_sum <= 2 * atc['total'],
          f"sum={type_sum:,} total={atc['total']:,}")
    print(f'  INFO type counts are orthogonal: sum={type_sum:,} > total={atc["total"]:,} (entries multi-labeled)')

if bbm:
    check('block-by-type-matrix total_entries', bbm['total_entries'] == EXPECTED_TOTAL,
          f"got {bbm['total_entries']}")

if bc:
    check('block-counts total', bc['total'] == EXPECTED_TOTAL, f"got {bc['total']}")
    # F01 (head) should equal total — every record has a head block
    f01 = next((b['count'] for b in bc['blocks'] if b['id'] == 'F01'), None)
    if f01 is not None:
        check('block-counts F01 (head) == total', f01 == EXPECTED_TOTAL,
              f'F01={f01}')

if crd:
    mw_row = next((d for d in crd['dicts'] if d['code'] == 'MW'), None)
    if mw_row:
        check('cross-dict MW records', mw_row['records'] == EXPECTED_TOTAL,
              f"got {mw_row['records']}")
    else:
        print('  MISS cross-dict.json MW row not found')

if mw_blk:
    check('mw_blocks total_entries', mw_blk['total_entries'] == EXPECTED_TOTAL,
          f"got {mw_blk['total_entries']}")

# ---- 2. Per-type counts: article-type-counts vs block-by-type-matrix ----
print()
print('--- 2. Per-type counts: article-type-counts.json vs block-by-type-matrix.json ---')
if atc and bbm:
    atc_map = {r['type']: r['count'] for r in atc['types']}
    bbm_map = {r['type']: r['count'] for r in bbm['matrix']}
    all_types = set(atc_map) | set(bbm_map)
    mismatches = []
    for t in sorted(all_types):
        a = atc_map.get(t)
        b = bbm_map.get(t)
        if a != b:
            mismatches.append(f'{t}: atc={a} bbm={b}')
    check(f'all {len(all_types)} types match between atc and bbm',
          len(mismatches) == 0, '; '.join(mismatches[:5]))
    if not mismatches:
        print(f'  INFO {len(all_types)} types, total={sum(atc_map.values()):,}')

# ---- 3. Cross-dict MW consistency ----
print()
print('--- 3. cross-dict.json MW row vs known facts ---')
if crd:
    mw_row = next((d for d in crd['dicts'] if d['code'] == 'MW'), None)
    if mw_row:
        # ls_per_record = 1.089 (known from MWS DICT_PROFILE.md)
        ls = mw_row.get('ls_per_record', 0)
        check('MW ls_per_record ≈ 1.089 (±0.01)', abs(ls - 1.089) < 0.01, f'got {ls:.3f}')
        # cite% in cross-dict blocks_pct
        bp = mw_row.get('blocks_pct', {})
        if 'cite' in bp:
            check('MW blocks_pct cite > 50%', bp['cite'] > 50,
                  f"got {bp['cite']:.1f}%")
        if 'hedge' in bp:
            # Known: 40,213 L. records / 286,561 total ≈ 14.0%
            expected_hedge = 40213 / 286561 * 100
            check(f'MW blocks_pct hedge ≈ 14.0% (L. records)',
                  abs(bp['hedge'] - expected_hedge) < 1.0,
                  f"got {bp['hedge']:.1f}% expected≈{expected_hedge:.1f}%")
        # Check other dicts present
        all_codes = [d['code'] for d in crd['dicts']]
        expected_codes = {'MW', 'PWG', 'PWK', 'AP', 'WIL', 'BEN', 'CAE', 'SKD', 'VCP'}
        missing = expected_codes - set(all_codes)
        check(f'cross-dict has all 9 expected dicts', not missing,
              f'missing: {missing}')
        print(f'  INFO dicts present: {all_codes}')

# ---- 4. mw_blocks.json common-block facts ----
print()
print('--- 4. mw_blocks.json common-block internal consistency ---')
if mw_blk:
    bp = mw_blk.get('blocks_pct', {})
    # head should be 100%
    check('mw_blocks head = 100.0%', bp.get('head') == 100.0, f"got {bp.get('head')}")
    # cite should match cross-dict if both present
    if crd and mw_row and 'cite' in bp and 'cite' in mw_row.get('blocks_pct', {}):
        diff = abs(bp['cite'] - mw_row['blocks_pct']['cite'])
        check('mw_blocks cite% == cross-dict MW cite% (same computation)',
              diff < 0.2, f"mw_blocks={bp['cite']:.1f}% crd={mw_row['blocks_pct']['cite']:.1f}%")
    # hedge should be ~14%
    if 'hedge' in bp:
        expected = 40213 / 286561 * 100
        check(f'mw_blocks hedge ≈ 14.0% (L. records / total)',
              abs(bp['hedge'] - expected) < 1.0,
              f"got {bp['hedge']:.1f}%")
    # sanity: hedge < cite
    if 'hedge' in bp and 'cite' in bp:
        check('mw_blocks hedge < cite (sanity)', bp['hedge'] < bp['cite'])

# ---- 5. Per-dict blocks.json record counts ----
print()
print('--- 5. Per-dict blocks.json record counts ---')
EXPECTED_RECORDS = {
    'mw': 286561, 'pwg': 123366, 'pwk': 170556,
    'ap': 90654,  'wil': 44577,  'ben': 5186,
    'cae': 40069, 'skd': 42531,  'vcp': 50135,
}
for code, expected in EXPECTED_RECORDS.items():
    blk = load(f'{code}_blocks.json')
    if blk is None:
        continue
    actual = blk.get('total_entries', 0)
    check(f'{code}_blocks total={expected:,}', actual == expected, f'got {actual:,}')

# ---- 6. Cross-dict per-dict records match blocks.json ----
print()
print('--- 6. cross-dict.json per-dict records vs {code}_blocks.json ---')
CODE_MAP = {'MW': 'mw', 'PWG': 'pwg', 'PWK': 'pwk', 'AP': 'ap', 'WIL': 'wil',
            'BEN': 'ben', 'CAE': 'cae', 'SKD': 'skd', 'VCP': 'vcp'}
if crd:
    for row in crd['dicts']:
        code = row.get('code', '')
        file_code = CODE_MAP.get(code)
        if file_code is None:
            continue
        blk_path = os.path.join(DATA, f'{file_code}_blocks.json')
        if not os.path.exists(blk_path):
            continue
        with open(blk_path, encoding='utf-8') as f:
            blk = json.load(f)
        crd_rec = row.get('records', 0)
        blk_rec = blk.get('total_entries', 0)
        check(f'{code} records: cross-dict ({crd_rec:,}) == blocks ({blk_rec:,})',
              crd_rec == blk_rec, f'diff={crd_rec - blk_rec}')

# ---- 7. Twin block tables (PAPER.md / PAPER_RU.md) vs SPOTCHECK ----
# H1379: the EN and RU §4 block-rate tables drifted apart for weeks (seven rows,
# including a <1%-vs-2.5% category error) because nothing gated the PROSE tables,
# only the figure JSON. This section asserts (a) both twins carry the same 18 rows,
# (b) each row's value reads identically in EN and RU after notation normalisation
# (, vs . decimals, ≈ vs ~, footnote daggers), and (c) every exact decimal value
# matches the audited SPOTCHECK.md rate. An edit to one twin now fails the check.
print()
print('--- 7. Twin block tables (PAPER.md / PAPER_RU.md) vs SPOTCHECK.md ---')
import re

def parse_spotcheck():
    path = os.path.join(HERE, 'SPOTCHECK.md')
    rates = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'\s+(F\d{2}):\s+[\d,]+\s+\(\s*([\d.]+)%\)', line)
            if m:
                rates[m.group(1)] = float(m.group(2))
    return rates

def parse_twin_table(fname):
    path = os.path.normpath(os.path.join(HERE, '..', fname))
    rows = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'\|\s*(?:\*\*)?(F\d{2})\b', line)
            if not m:
                continue
            fid = m.group(1)
            cells = [c.strip() for c in line.split('|')]
            # cells[0] is empty, cells[1] the block name, cells[2] the rate
            if len(cells) > 2 and fid not in rows:
                rows[fid] = cells[2]
    return rows

def normalise(val):
    v = val.replace('**', '')
    v = re.sub(r'\\?[*†‡¶§]', '', v)   # footnote markers
    v = v.replace('≈', '~').replace(',', '.')
    v = re.sub(r'\s+', '', v)
    return v

spot = parse_spotcheck()
en_rows = parse_twin_table('PAPER.md')
ru_rows = parse_twin_table('PAPER_RU.md')

check('EN and RU block tables carry the same row set',
      set(en_rows) == set(ru_rows),
      f'EN-only: {sorted(set(en_rows) - set(ru_rows))}; RU-only: {sorted(set(ru_rows) - set(en_rows))}')

twin_mismatch = []
for fid in sorted(set(en_rows) & set(ru_rows)):
    if normalise(en_rows[fid]) != normalise(ru_rows[fid]):
        twin_mismatch.append(f'{fid}: EN "{en_rows[fid]}" vs RU "{ru_rows[fid]}"')
check(f'all {len(set(en_rows) & set(ru_rows))} twin rows agree EN vs RU',
      not twin_mismatch, '; '.join(twin_mismatch[:5]))

spot_mismatch = []
audited = 0
for fid, raw in sorted(en_rows.items()):
    v = normalise(raw)
    # only exact decimal values are gated against SPOTCHECK; rounded ints
    # (96%, 76%) and bounded values (~100%, <1%) state a coarser claim
    m = re.fullmatch(r'(\d+\.\d+)%', v)
    if not m or fid not in spot:
        continue
    audited += 1
    if abs(float(m.group(1)) - spot[fid]) > 0.05:
        spot_mismatch.append(f'{fid}: table {v} vs SPOTCHECK {spot[fid]}%')
check(f'{audited} exact decimal rows match SPOTCHECK audited rates',
      not spot_mismatch, '; '.join(spot_mismatch[:5]))

# ---- Summary ----
print()
print('=== Summary ===')
if errors:
    print(f'FAILED: {len(errors)} check(s):')
    for e in errors:
        print(f'  - {e}')
    sys.exit(1)
else:
    print('All checks passed.')
