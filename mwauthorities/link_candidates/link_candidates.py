#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W1 layer (a): enumerate live <ls> abbreviations with NO authority record, and
propose a mechanical match to an existing canonical authority.

Approach (avoids decoding the legacy digit-encoding in linkmwauthorities_init.txt):
  - distinct bare <ls> abbreviations from live mw.txt are IAST;
  - transcode each IAST -> SLP1 (the canonical authority keys are already SLP1);
  - "covered" = SLP1 keys of authority records (mwauthorities_init.txt col1)
    UNION the canonical column of the link file (col3);
  - an abbreviation whose SLP1 form is not covered is a CANDIDATE unlinked siglum;
  - for each, propose the closest canonical key (difflib) as a mechanical match.

This is a REVIEW CANDIDATE generator. It writes link_candidates.csv only; it does
NOT touch any authority file. The transcode-membership test has a known
false-positive mode (a linked siglum whose live spelling != its canonical key),
so the script self-validates against the top-frequency (certainly-linked) sigla
and reports that rate.

Outputs (this dir):
  link_candidates.csv   unlinked siglum, count, SLP1, suggested canonical, score, confidence
  LINK_CANDIDATES_SUMMARY.md
"""
import sys, os, re, csv, difflib, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH   = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
MW   = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')
AUTH = os.path.join(HERE, '..', 'mwauthorities_init.txt')
LINK = os.path.join(HERE, '..', 'linkmwauthorities_init.txt')

# --- IAST -> SLP1 (lowercases first; IAST case is orthographic, SLP1 case is phonemic) ---
_MAP = [
    ('ai','E'),('au','O'),
    ('kh','K'),('gh','G'),('ch','C'),('jh','J'),('ṭh','W'),('ḍh','Q'),
    ('th','T'),('dh','D'),('ph','P'),('bh','B'),
    ('ā','A'),('ī','I'),('ū','U'),('ṝ','F'),('ṛ','f'),('ḹ','X'),('ḷ','x'),
    ('ṅ','N'),('ñ','Y'),('ṭ','w'),('ḍ','q'),('ṇ','R'),
    ('ś','S'),('ṣ','z'),('ṃ','M'),('ḥ','H'),('ṁ','M'),('ḻ','L'),
    ('a','a'),('i','i'),('u','u'),('e','e'),('o','o'),
    ('k','k'),('g','g'),('c','c'),('j','j'),('t','t'),('d','d'),('n','n'),
    ('p','p'),('b','b'),('m','m'),('y','y'),('r','r'),('l','l'),('v','v'),
    ('s','s'),('h','h'),
]
def iast_to_slp1(s):
    s = unicodedata.normalize('NFC', s).lower()
    out, i, n = [], 0, len(s)
    while i < n:
        for src, dst in _MAP:
            if s.startswith(src, i):
                out.append(dst); i += len(src); break
        else:
            i += 1   # drop periods, spaces, parentheses, digits
    return ''.join(out)

LS_RE = re.compile(r'<ls(?:\s[^>]*)?>([^<]*)</ls>')
def bare(siglum):
    """Reduce a citation to its base work siglum: drop scholiast/edition
    qualifiers and the trailing locator, so 'R. (B.)' and 'Yājñ., Sch.' fold to
    the base work (which may already be linked)."""
    s = siglum.strip()
    s = re.sub(r',?\s*(Sch\.|Comm\.|Scholiast|Gframm?\.|Caus\.).*$', '', s)
    s = re.sub(r'\s*\([^)]*\)\s*$', '', s)                       # trailing (B.), (C.)
    s = re.sub(r'\s+p\.?$', '', s)                               # trailing ' p'
    s = re.split(r'[ ,]+[ivxlcdm0-9]', s, maxsplit=1)[0]         # locator
    return s.strip()

# --- live <ls> bare abbreviation frequencies ---
# Noise filter: a real siglum is a Capitalised work abbreviation. Roman-numeral
# locators (vi, iii, x) and stray lowercase fragments start lowercase -> dropped.
counts = {}
META = {'L.','ib.','MW.','W.','Cat.','id.'}
ROMAN = re.compile(r'^[IiVvXxLlCcDdMm]+\.?$')
def is_siglum(b):
    if not b or b in META: return False
    if not b[:1].isupper(): return False        # works are Capitalised (incl. Ā, Ś)
    if ROMAN.match(b): return False              # roman numeral locator (V., XI. ...)
    return True
with open(MW, encoding='utf-8') as f:
    for line in f:
        for siglum in LS_RE.findall(line):
            b = bare(siglum)
            if is_siglum(b):
                counts[b] = counts.get(b, 0) + 1

# --- covered sets ---
# col1_text = live text spellings already linked (verbatim for ASCII sigla like RV.)
# canon_slp = SLP1 canonical keys (auth col1 + link col3) for diacritic sigla
col1_text = set()
canon_slp = set()
with open(AUTH, encoding='utf-8') as f:
    for line in f:
        if '\t' in line:
            canon_slp.add(line.split('\t')[0].strip())
with open(LINK, encoding='utf-8') as f:
    for line in f:
        parts = line.rstrip('\n').split('\t')
        if parts and parts[0].strip():
            col1_text.add(parts[0].strip())
        if len(parts) >= 3:
            canon_slp.add(parts[2].strip())

# --- classify each live siglum (dual check) ---
rows = []
for sig, c in counts.items():
    slp = iast_to_slp1(sig)
    linked = (sig in col1_text) or (slp in canon_slp)
    rows.append((sig, c, slp, linked))
covered = canon_slp  # for the difflib suggestion pool

unlinked = [r for r in rows if not r[3]]
linked   = [r for r in rows if r[3]]

# --- self-validation: of the top-40 sigla by count, how many flagged unlinked? ---
top = sorted(rows, key=lambda r:-r[1])[:40]
top_unlinked = [r for r in top if not r[3]]

# --- mechanical match for each unlinked siglum ---
cov_list = sorted(covered)
def suggest(slp):
    m = difflib.get_close_matches(slp, cov_list, n=1, cutoff=0.7)
    if not m:
        return '', 0.0
    return m[0], round(difflib.SequenceMatcher(None, slp, m[0]).ratio(), 2)

cand = []
for sig, c, slp, _ in sorted(unlinked, key=lambda r:-r[1]):
    s, score = suggest(slp)
    if score >= 0.9:   conf = 'high'
    elif score >= 0.8: conf = 'medium'
    elif s:            conf = 'low'
    else:              conf = 'no-match (new work?)'
    cand.append([sig, c, slp, s, score, conf])

with open(os.path.join(HERE,'link_candidates.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['ls_siglum','citation_count','slp1','suggested_canonical','match_score','confidence'])
    w.writerows(cand)

from collections import Counter
conf_hist = Counter(r[5] for r in cand)
S=[]
S.append('# W1 (a) — unlinked `<ls>` siglum candidates\n')
S.append('Review candidates only — **nothing is written to any authority file.**\n')
S.append('## Counts')
S.append(f'- Distinct live `<ls>` bare abbreviations (meta excluded): **{len(rows):,}**')
S.append(f'- Already covered by an authority record / link: {len(linked):,}')
S.append(f'- **Candidate unlinked: {len(unlinked):,}**\n')
S.append('## Self-validation (false-positive check)')
S.append(f'The linked-check is dual: a siglum counts as linked if its spelling is in the')
S.append(f'link file col1 verbatim (ASCII sigla like `RV.`) OR its SLP1 transcription is a')
S.append(f'known canonical key (diacritic sigla like `Pāṇ.`→`pAR`).')
if not top_unlinked:
    S.append(f'- Of the 40 highest-frequency sigla (certainly real and linked), **0 are')
    S.append(f'  flagged unlinked** — the check produces no false positives at the high-')
    S.append(f'  frequency end, so the candidates below are genuine gaps, not mismatches.\n')
else:
    S.append(f'- Of the 40 highest-frequency sigla, **{len(top_unlinked)} are flagged unlinked**')
    S.append(f'  — likely transcode/spelling mismatches (false positives) to discount:')
    for sig,c,slp,_ in top_unlinked[:12]:
        s,score=suggest(slp)
        S.append(f'  - `{sig}` ({c:,}) → `{slp}` → nearest `{s}` ({score})')
    S.append('')
S.append('## Match confidence (of the candidates)')
S.append('| confidence | count | meaning |')
S.append('|---|--:|---|')
S.append(f'| high (≥0.90) | {conf_hist.get("high",0)} | near-certain spelling variant of an existing record |')
S.append(f'| medium (0.80–0.89) | {conf_hist.get("medium",0)} | probable variant — quick human confirm |')
S.append(f'| low (0.70–0.79) | {conf_hist.get("low",0)} | weak — needs judgment |')
S.append(f'| no-match | {conf_hist.get("no-match (new work?)",0)} | no close record — candidate NEW authority |')
S.append('\n## How to use')
S.append('- `link_candidates.csv` is sorted by citation count. The **high**-confidence')
S.append('  rows are the mechanical wins (a spelling variant that should point to an')
S.append('  existing canonical record); **no-match** rows are candidate new authorities.')
S.append('- A maintainer reviews, then the accepted rows are added to')
S.append('  `linkmwauthorities_init.txt` via the normal authority workflow. Not automated.')
open(os.path.join(HERE,'LINK_CANDIDATES_SUMMARY.md'),'w',encoding='utf-8').write('\n'.join(S)+'\n')

print(f'distinct sigla: {len(rows)} | linked: {len(linked)} | candidate unlinked: {len(unlinked)}')
print(f'top-40 false positives: {len(top_unlinked)}')
print(f'confidence: {dict(conf_hist)}')