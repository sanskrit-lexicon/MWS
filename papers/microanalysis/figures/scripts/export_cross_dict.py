#!/usr/bin/env python3
"""Export cross-dictionary stats to JSON for the figures + the atlas.

Recomputes the format-robust common-block populations, citation density, and
modal kernel across all nine CDSL dictionaries (reusing the audit functions in
../../analysis/), and writes figures/data/cross-dict.json — consumed by
render_cross_dict.py and by the csl-atlas cross-dictionary view.
"""
import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.normpath(os.path.join(HERE, '..'))
ANALYSIS = os.path.normpath(os.path.join(FIG_DIR, '..', 'analysis'))
sys.path.insert(0, ANALYSIS)

from cross_dict_kernel import blocks_of, RECORD_RE, COMMON_BLOCKS, DICTS  # noqa: E402
from _common import TMP  # noqa: E402

VOLUMES = {'MW': 1, 'PWG': 7, 'PWK': 1, 'AP': 1, 'WIL': 1, 'BEN': 1, 'CAE': 1, 'SKD': 1, 'VCP': 1}


def main():
    out = []
    for code, fn, desc in DICTS:
        path = os.path.join(TMP, fn)
        if not os.path.exists(path):
            print(f'skip {code}: missing {fn}')
            continue
        text = open(path, encoding='utf-8', errors='replace').read()
        pop = Counter()
        perentry = Counter()
        n = 0
        for m in RECORD_RE.finditer(text):
            bl = blocks_of(m.group(0))
            n += 1
            perentry[len(bl)] += 1
            for x in bl:
                pop[x] += 1
        ls = text.count('<ls>')
        modal = max(perentry.items(), key=lambda kv: kv[1])[0] if perentry else 0
        mean = sum(k * v for k, v in perentry.items()) / n if n else 0
        out.append({
            'code': code,
            'name': desc,
            'volumes': VOLUMES.get(code, 1),
            'genre': 'sanskrit' if code in ('SKD', 'VCP') else 'structured',
            'records': n,
            'ls_total': ls,
            'ls_per_record': round(ls / n, 3) if n else 0,
            'modal_blocks': modal,
            'mean_blocks': round(mean, 2),
            'blocks_pct': {b: round(100 * pop[b] / n, 1) if n else 0 for b in COMMON_BLOCKS},
        })
        print(f'{code}: {n:,} records, {ls/n:.2f} ls/rec, modal {modal}')

    payload = {'blocks': COMMON_BLOCKS, 'dicts': out}
    dest = os.path.join(FIG_DIR, 'data', 'cross-dict.json')
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f'\nwrote {dest}')


if __name__ == '__main__':
    main()
