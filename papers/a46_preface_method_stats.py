#!/usr/bin/env python3
"""A46 stated-vs-measured statistics: recompute every mw.txt-derived figure
cited in papers/A46_mw_preface_method.md from the canonical source.

Usage:
    python a46_preface_method_stats.py [path/to/mw.txt]

Default source path assumes the standard sibling layout
(../../csl-orig/v02/mw/mw.txt relative to this file). Stdlib-only,
deterministic, re-runnable. Prints a Markdown-ready block of figures.
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

DEFAULT = Path(__file__).resolve().parents[2] / 'csl-orig' / 'v02' / 'mw' / 'mw.txt'


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    text = src.read_text(encoding='utf-8')
    lines = text.splitlines()

    records = 0
    k1_all = []
    k2_accented = 0
    k2_total = 0
    hom = 0
    e_codes = Counter()
    root_info = Counter()
    for line in lines:
        m = re.match(r'<L>([^<]+)<pc>([^<]*)<k1>([^<]*)<k2>([^<]*)', line)
        if m:
            records += 1
            k1_all.append(m.group(3))
            k2 = m.group(4)
            k2_total += 1
            # accent markers in key2: / (udatta), \ (svarita), ^
            if any(c in k2 for c in '/\\^'):
                k2_accented += 1
            e = re.search(r'<e>(\S+)', line)
            if e:
                e_codes[e.group(1)] += 1
        hom += line.count('<hom>')
        for v in re.findall(r'<info\s[^>]*verb="([^"]+)"', line):
            root_info[v.split(',')[0]] += 1

    ls_all = re.findall(r'<ls[^>]*>(.*?)</ls>', text)
    ls_total = len(ls_all)
    ls_counter = Counter(s.strip() for s in ls_all)
    ls_L = ls_counter.get('L.', 0)
    ls_MW = sum(v for k, v in ls_counter.items()
                if k == 'MW.' or k.startswith('MW.'))
    ls_W = sum(v for k, v in ls_counter.items()
               if k == 'W.' or k.startswith('W.'))
    ls_RV = sum(v for k, v in ls_counter.items()
                if k == 'RV.' or k.startswith('RV.'))
    ls_ib = ls_counter.get('ib.', 0)

    distinct_k1 = len(set(k1_all))

    print(f'source: {src} ({len(lines):,} lines)')
    print(f'records (<L>): {records:,}')
    print(f'distinct k1 headwords: {distinct_k1:,}')
    print(f'k2 with accent marks (/ \\ ^): {k2_accented:,} '
          f'({100 * k2_accented / k2_total:.1f}% of {k2_total:,})')
    print(f'<hom> homonym numbers: {hom:,}')
    print(f'<ls> citations total: {ls_total:,}')
    print(f'<ls>L.</ls> (lexicographers-only hedge): {ls_L:,} '
          f'({100 * ls_L / ls_total:.1f}%)')
    print(f'<ls> MW.* (own authority): {ls_MW:,}')
    print(f'<ls> W.* (Wilson authority): {ls_W:,}')
    print(f'<ls> RV.* (Rig-Veda): {ls_RV:,}')
    print(f'<ls>ib.</ls>: {ls_ib:,}')
    print(f'distinct <ls> sigla (verbatim strings): {len(ls_counter):,}')
    print('info verb= record kinds: '
          + ', '.join(f'{k}={v:,}' for k, v in root_info.most_common()))
    print('top-level <e> hierarchy codes: '
          + ', '.join(f'{k}={v:,}' for k, v in e_codes.most_common(8)))


if __name__ == '__main__':
    main()
