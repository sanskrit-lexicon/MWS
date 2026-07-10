#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3-way verbal-root crosswalk: MW <-> Whitney hub <-> DCS corpus.

Thin MWS-side consumer of the canonical join in
WhitneyRoots/scripts/root_triangulation.py (SHARED_CODE.md §16) — this script no
longer re-scans mw.txt or re-implements the hub/DCS join; it imports the shared
module and re-emits MWS's own output files unchanged so downstream consumers
(ROOT_CROSSWALK_SUMMARY.md readers, class_concordance.py) see the same shape.

Outputs (this dir):
  root_crosswalk.csv     whitney_id, root, in_MW, mw_L, mw_classes, dcs_status, dcs_freq
  mw_whitney_unmatched.csv   MW anchors that match no hub root (candidate errors)
  ROOT_CROSSWALK_SUMMARY.md
"""
import sys
import os
import csv

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH = os.path.abspath(os.path.join(HERE, '..', '..'))
WR_SCRIPTS = os.path.join(GH, 'WhitneyRoots', 'scripts')
sys.path.insert(0, WR_SCRIPTS)
from root_triangulation import triangulate  # noqa: E402  (SHARED_CODE.md §16)

rows, summary, mw_unmatched = triangulate()

with open(os.path.join(HERE, 'root_crosswalk.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['whitney_id', 'root', 'in_MW', 'mw_L', 'mw_classes', 'dcs_status', 'dcs_freq'])
    for r in rows:
        w.writerow([r['whitney_id'], r['root'], r['in_MW'], r['mw_L'], r['mw_classes'],
                    r['dcs_status'], r['dcs_freq']])

with open(os.path.join(HERE, 'mw_whitney_unmatched.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['mw_root_iast_bare', 'mw_L', 'whitney_page'])
    w.writerows(mw_unmatched)

NH = summary['n_hub']
in_mw, in_dcs, in_both = summary['in_mw'], summary['in_dcs'], summary['in_both']

# H500 regression lock (SHARED_CODE.md §17): the pre-refactor coverage stat, asserted so a
# silently-different join in root_triangulation.py doesn't slip past a re-run unnoticed.
# If MW/DCS/hub data legitimately changed, update these constants after reviewing the diff.
assert NH == 935 and in_mw == 809 and in_dcs == 590 and in_both == 550, (
    f'coverage stat drifted from the H500 baseline: hub={NH} in_MW={in_mw} in_DCS={in_dcs} in_both={in_both}')
S = []
S.append('# 3-way verbal-root crosswalk: MW ↔ Whitney ↔ DCS\n')
S.append('## MW side')
S.append(f"- MW verbal-root records (`verb=\"genuineroot\"` or `\"root\"`): **{summary['n_mw_genuine']:,}**")
S.append(f"- …with a Whitney anchor (`<info whitneyroots>`): {summary['n_mw_anchored']:,}")
S.append(f"- …with a Westergaard anchor (`<info westergaard>`): {summary['n_westergaard']:,}")
S.append(f"- Distinct MW-anchored roots matched to the hub: {summary['n_mw_anchored'] - summary['n_unmatched']:,};")
S.append(f"  **unmatched (candidate anchor errors): {summary['n_unmatched']:,}** → `mw_whitney_unmatched.csv`\n")
S.append('## Coverage of the 935-root Whitney hub')
S.append(f'- Attested in **MW**: **{in_mw:,}** ({100*in_mw/NH:.1f}%)')
S.append(f'- Attested in **DCS** corpus: **{in_dcs:,}** ({100*in_dcs/NH:.1f}%)')
S.append(f'- **In BOTH MW and DCS (triangulated by bare-root match): {in_both:,}** ({100*in_both/NH:.1f}%)')
S.append(f'- MW+Whitney but **DCS-absent** (grammarian/lexical roots): {in_mw-in_both:,}')
S.append(f'- DCS+Whitney but **MW-unanchored** (anchoring gap to close): {in_dcs-in_both:,}')
S.append(f'- In neither MW nor DCS: {NH-(in_mw+in_dcs-in_both):,}\n')
S.append('## Why it matters')
S.append('- The triangulated roots (MW gloss + Whitney grammar + DCS frequency) are the')
S.append('  ready core of the grammar-corpus-dict crosswalk: a root you can define,')
S.append('  conjugate, and frequency-rank at once. **Caveat:** the join is on the')
S.append('  homonym-collapsed bare root, so "in all three" does not assert the three')
S.append('  sources mean the *same* homonym — homonym-level alignment is a later step.')
S.append('- Roots in Whitney+DCS but NOT anchored in MW are the gap to close (add the')
S.append('  `<info whitneyroots>` anchor); roots in MW+Whitney but DCS-unmatched are')
S.append('  corpus-absent (lexical/grammarian roots) — a P3/P4 signal.')
S.append('\n## Notes')
S.append('- Join is on homonym-normalised root string (MW `akz1`/`akz2` ↔ hub `1 akṣ`).')
S.append('- The number in `whitneyroots="root,N"` is Whitney\'s 1885 root-appendix page')
S.append('  (max 210, many roots share a page), NOT a root id — decoded here.')
S.append('- `mw_whitney_unmatched.csv` are MW anchors with no hub root after')
S.append('  normalisation: either MW-side typos or roots absent from the hub.')
S.append('- MW side is read from the canonical `csl-orig/v02/mw/mw_roots.tsv`')
S.append('  (SHARED_CODE.md §11); the join itself lives in')
S.append('  `WhitneyRoots/scripts/root_triangulation.py` (SHARED_CODE.md §16) — this')
S.append('  script is a thin MWS-side consumer, not a second implementation.')
open(os.path.join(HERE, 'ROOT_CROSSWALK_SUMMARY.md'), 'w', encoding='utf-8').write('\n'.join(S) + '\n')

print(f"MW genuine roots {summary['n_mw_genuine']} | whitney-anchored {summary['n_mw_anchored']} "
      f"| westergaard {summary['n_westergaard']}")
print(f'hub {NH}: in_MW {in_mw}, in_DCS {in_dcs}, in_both {in_both}')
print(f"MW anchors unmatched to hub: {summary['n_unmatched']}")
