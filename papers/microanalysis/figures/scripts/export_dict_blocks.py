#!/usr/bin/env python3
"""S5 — Per-dict block-matrix JSON export using the common-block vocabulary.

Extends the cross_dict_kernel block-detection pipeline to produce per-type
block-frequency matrices for each CDSL dict (analogous to what export_data.py
produces for MW with the full F01-F18 taxonomy, but using the 9-block
format-robust common vocabulary so results are comparable across dicts).

Run:  python export_dict_blocks.py [CODE ...]

Examples:
  python export_dict_blocks.py          # all dicts
  python export_dict_blocks.py PWG PWK  # specific dicts

Output:  ../data/{CODE}_blocks.json  for each processed dict.

Dict-specific notes (also in analysis/CROSS_DICT_PROFILES.md §Adjustments):
  PWG/PWK: use <lex>a.</lex> for adjectives (not mfn.); handled via LEXMAP.
  AP/WIL/CAE: also use <lex>a.</lex> for adjectival entries.
  SKD/VCP: no <lex> tags; all entries typed as "other"; no <ls>; cite=0%.
  BEN:     no <lex> tags; all entries typed as "other".
  MW:      uses <lex>mfn.</lex>; also mf(n.). Both handled.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.normpath(os.path.join(HERE, '..'))
DATA_DIR = os.path.join(FIG_DIR, 'data')
ANALYSIS = os.path.normpath(os.path.join(FIG_DIR, '..', 'analysis'))
sys.path.insert(0, ANALYSIS)

from cross_dict_kernel import blocks_of, RECORD_RE, COMMON_BLOCKS, DICTS  # noqa: E402
from _common import TMP  # noqa: E402

# Type order for output (common across all dicts)
TYPE_ORDER = ['noun-m', 'noun-f', 'noun-n', 'adj-mfn', 'indeclinable', 'other']

# Dicts where <lex> is absent — all entries fall into "other"
NO_LEX_DICTS = {'SKD', 'VCP', 'BEN'}

# Mapping from raw <lex> content (after rstrip('.').lower()) to type.
# Covers MW (mfn, mf(n.)), PWG/PWK/AP/WIL/CAE (a, adj, indecl).
LEXMAP = {
    'm': 'noun-m',
    'f': 'noun-f',
    'n': 'noun-n',
    'mfn': 'adj-mfn',
    'mf(n.)': 'adj-mfn',
    'mf(n)': 'adj-mfn',
    'a': 'adj-mfn',       # PWG/PWK/AP/WIL/CAE convention for adjectives
    'adj': 'adj-mfn',
    'ind': 'indeclinable',
    'indecl': 'indeclinable',
}

LEX_RE = re.compile(r'<lex>([^<]+)</lex>')


def classify_lex(chunk):
    """Return the primary grammatical type from the first <lex> tag."""
    m = LEX_RE.search(chunk)
    if not m:
        return 'other'
    raw = m.group(1).strip().rstrip('.').lower()
    return LEXMAP.get(raw, 'other')


def process_dict(code, filename):
    path = os.path.join(TMP, filename)
    if not os.path.exists(path):
        print(f'  {code}: {filename} not found in {TMP} — skip')
        return None
    text = open(path, encoding='utf-8', errors='replace').read()

    per_type_blocks = defaultdict(lambda: Counter())   # type -> Counter(block)
    per_type_count = Counter()                          # type -> N entries
    n = 0
    for m in RECORD_RE.finditer(text):
        chunk = m.group(0)
        t = 'other' if code in NO_LEX_DICTS else classify_lex(chunk)
        bl = blocks_of(chunk)
        n += 1
        per_type_count[t] += 1
        for b in bl:
            per_type_blocks[t][b] += 1

    # Build matrix rows
    matrix = []
    for t in TYPE_ORDER:
        cnt = per_type_count[t]
        if cnt == 0:
            continue
        row = {'type': t, 'count': cnt}
        for b in COMMON_BLOCKS:
            row[b] = per_type_blocks[t][b]
            row[b + '_pct'] = round(100.0 * per_type_blocks[t][b] / cnt, 2)
        matrix.append(row)

    # Overall block totals (= sum across all records)
    overall_blocks = Counter()
    for t_rows in per_type_blocks.values():
        for b, v in t_rows.items():
            overall_blocks[b] += v
    overall_pct = {b: round(100.0 * overall_blocks[b] / n, 1) if n else 0.0
                   for b in COMMON_BLOCKS}

    return {
        'code': code,
        'name': next(desc for c, fn, desc in DICTS if c == code),
        'total_entries': n,
        'blocks': COMMON_BLOCKS,
        'types': TYPE_ORDER,
        'blocks_pct': overall_pct,
        'matrix': matrix,
    }


def main(targets=None):
    to_run = [(c, fn, d) for c, fn, d in DICTS if (targets is None or c in targets)]
    if not to_run:
        print(f'No matching dicts for: {targets}')
        return
    for code, filename, _ in to_run:
        print(f'Processing {code} ({filename})...')
        result = process_dict(code, filename)
        if result is None:
            continue
        dest = os.path.join(DATA_DIR, f'{code.lower()}_blocks.json')
        with open(dest, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        types_present = [r['type'] for r in result['matrix']]
        adj_count = next((r['count'] for r in result['matrix'] if r['type'] == 'adj-mfn'), 0)
        print(f'  {result["total_entries"]:,} entries, types: {types_present}')
        if adj_count:
            print(f'  adj-mfn: {adj_count:,}')
        print(f'  wrote {dest}')


if __name__ == '__main__':
    args = [a.upper() for a in sys.argv[1:]] or None
    main(args)
