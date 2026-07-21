#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Conjugation-class concordance: MW `cp` vs Whitney `classes` (+ Westergaard coverage).

For verbal roots MW anchors to Whitney, compare the conjugation class(es) each
source assigns:
  MW:       <info verb="genuineroot" cp="1P,1Ā"/>   -> class {1}
  Whitney:  app_data classes ['I','IV']             -> {1,4}
Agreement validates the assignment; conflicts are research signals (the contested
class assignments behind the Whitney I/VI/IV collapse). Westergaard/Dhātupāṭha
presence is reported as a third-authority tiebreaker available for follow-up.

Outputs (this dir):
  class_concordance.csv   root, mw_classes, whitney_classes, verdict, has_westergaard
  CLASS_CONCORDANCE_SUMMARY.md
"""
import sys, os, re, csv, json
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH   = os.path.abspath(os.path.join(HERE, '..', '..'))
MW   = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')

_S2I = {'A':'ā','I':'ī','U':'ū','f':'ṛ','F':'ṝ','x':'ḷ','X':'ḹ','E':'ai','O':'au',
        'M':'ṃ','H':'ḥ','K':'kh','G':'gh','N':'ṅ','C':'ch','J':'jh','Y':'ñ',
        'w':'ṭ','W':'ṭh','q':'ḍ','Q':'ḍh','R':'ṇ','T':'th','D':'dh','P':'ph',
        'B':'bh','S':'ś','z':'ṣ','L':'ḻ'}
def s2i(s): return ''.join(_S2I.get(c, c) for c in s)
def bare(r):
    r = re.sub(r'^\d+\s+', '', r.strip()); r = re.sub(r'\d+$', '', r); return r
ROM = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}

# --- hub: bare root -> set of classes (union over homonyms) ---
hub = json.load(open(os.path.join(GH,'WhitneyRoots','src','app_data.json'), encoding='utf-8'))['lexicon']
hub_cls = {}
for r in hub:
    b = bare(r['root'])
    cs = {ROM[c] for c in r['classes'] if c in ROM}
    hub_cls.setdefault(b, set()).update(cs)
hub_has = {bare(r['root']) for r in hub}

# --- MW: roots with whitney anchor + cp class, and westergaard presence ---
WR_RE = re.compile(r'whitneyroots="([^"]*)"')
WG_RE = re.compile(r'westergaard="')
CP_RE = re.compile(r'verb="(?:genuineroot|root)"\s+cp="([^"]*)"')   # both are verbal roots (CODE_REVIEW #4)
L_RE  = re.compile(r'^<L>([^<]*)')
def mw_classes(cp):
    # cp like "1P,1Ā,10P" -> {1,10}. MW class 0 = "no gana assigned" (pada known,
    # class unspecified) -> a sentinel, dropped so it is not counted as a class.
    return {int(m) for m in re.findall(r'(\d+)', cp)} - {0}

records = []   # (bare_root, mw_cls set, has_wg)
cur_L = None; rec = []
def flush():
    if cur_L is None: return
    t = ''.join(rec)
    wr = WR_RE.search(t); cp = CP_RE.search(t)
    if not (wr and cp): return
    root = wr.group(1).split(';')[0].rsplit(',',1)[0]
    b = bare(s2i(root))
    records.append((b, mw_classes(cp.group(1)), bool(WG_RE.search(t))))
with open(MW, encoding='utf-8') as f:
    for line in f:
        if line.startswith('<L>'):
            flush(); cur_L = L_RE.match(line).group(1); rec = []
        elif line.startswith('<LEND>'):
            flush(); cur_L = None; rec = []
        elif cur_L is not None:
            rec.append(line)
flush()

# --- compare (per DISTINCT bare root) ---
# CODE_REVIEW #5: a homonym-rich root has >1 genuine-root record; aggregate MW
# classes over those records (as hub_cls already unions Whitney's) so each root is
# compared ONCE, not once per homonym record (was N=records, double-counting ~50).
by_root = {}
for b, mwc, wg in records:
    e = by_root.setdefault(b, [set(), False])
    e[0] |= mwc; e[1] = e[1] or wg
rows = []; verdict_hist = {}; conflicts = []
for b, (mwc, wg) in sorted(by_root.items()):
    wc = hub_cls.get(b, set())
    if not mwc and not wc: v = 'both_empty'
    elif not wc:           v = 'whitney_empty'
    elif not mwc:          v = 'mw_empty'
    elif mwc == wc:        v = 'agree'
    elif mwc & wc:         v = 'overlap'
    else:                  v = 'conflict'
    verdict_hist[v] = verdict_hist.get(v, 0) + 1
    rows.append([b, ' '.join(map(str,sorted(mwc))) or '-', ' '.join(map(str,sorted(wc))) or '-',
                 v, 'yes' if wg else 'no'])
    if v == 'conflict':
        conflicts.append((b, sorted(mwc), sorted(wc), wg))

with open(os.path.join(HERE,'class_concordance.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['root','mw_classes','whitney_classes','verdict','has_westergaard'])
    w.writerows(sorted(rows))

N = len(by_root)
comparable = sum(verdict_hist.get(v,0) for v in ('agree','overlap','conflict'))
def pc(n): return f'{100*n/comparable:.1f}%' if comparable else '-'
S=[]
S.append('# Conjugation-class concordance: MW `cp` vs Whitney `classes`\n')
S.append(f'- MW genuine roots with both a Whitney anchor and a `cp` class: **{N:,}**')
S.append(f'- Comparable (both sources assign ≥1 class): **{comparable:,}**\n')
S.append('## Verdict (of comparable roots)')
S.append('| verdict | count | % |')
S.append('|---|--:|--:|')
for v in ('agree','overlap','conflict'):
    S.append(f'| **{v}** | {verdict_hist.get(v,0):,} | {pc(verdict_hist.get(v,0))} |')
S.append('')
S.append(f'- Not comparable: whitney_empty {verdict_hist.get("whitney_empty",0):,}, '
         f'mw_empty {verdict_hist.get("mw_empty",0):,}, both_empty {verdict_hist.get("both_empty",0):,}\n')
S.append('## Candidate conflicts (disjoint class sets — research signals, unverified)')
S.append(f'- {len(conflicts):,} roots where MW and Whitney share NO class. These are')
S.append(f'  **candidates** for review, not confirmed disagreements — homonym-rich roots')
S.append(f'  may reflect hub class-completeness rather than a true clash (see Notes).')
wg_n = sum(1 for c in conflicts if c[3])
S.append(f'- Of these, {wg_n:,} also carry a Westergaard/Dhātupāṭha anchor — the indigenous')
S.append(f'  grammarian class is available as a tiebreaker for them.')
S.append('\n| root | MW class | Whitney class | Dhātup.? |')
S.append('|---|---|---|---|')
for b, mwc, wc, wg in sorted(conflicts):
    S.append(f'| {b} | {",".join(map(str,mwc))} | {",".join(map(str,wc))} | {"y" if wg else ""} |')
S.append('\n## Notes')
S.append('- Class extracted from MW `cp` digits (`1P,1Ā`→{1}); Whitney roman→arabic.')
S.append('- MW `cp="0P"` (class 0 = "no gaṇa assigned", pada-only) is dropped as a')
S.append('  sentinel — so a 0-only root is `mw_empty`, not a spurious conflict.')
S.append('- Hub classes are unioned over homonyms sharing a bare root, so the test is')
S.append('  lenient (agreement if MW class ∈ any homonym\'s classes); true conflicts are')
S.append('  therefore conservative — real disagreements, not homonym artefacts.')
S.append('- Conflicts are candidates for the Whitney class-verdict review and a P4 signal;')
S.append('  the Dhātupāṭha (Westergaard) class can adjudicate where present.')
open(os.path.join(HERE,'CLASS_CONCORDANCE_SUMMARY.md'),'w',encoding='utf-8').write('\n'.join(S)+'\n')

print(f'roots compared: {N} | comparable: {comparable}')
print(f'verdicts: {verdict_hist}')
print(f'conflicts: {len(conflicts)} ({wg_n} with Dhatupatha anchor)')
print('sample conflicts:', [(c[0],c[1],c[2]) for c in sorted(conflicts)[:6]])