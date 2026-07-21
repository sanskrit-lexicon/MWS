#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A18 / P3 sense-level verification package (the *sense-next* step).

The lemma-level joins in ../../lexicographer_dcs/ established that ~31% of the
18,930 strict purely-lexicographic (`<ls>L.</ls>`-only) MW lemmas occur in the
DCS-2026 corpus. That is *lemma-now* evidence: the lemma occurs, but nobody has
checked whether the corpus attests THE HEDGED SENSE. This script builds the
hand-verification sample for that check (the human band-3 `L.` pass):

  - HEDGE stratum: 60 of the 174 band-3 (uncommon, 10-99 DCS tokens) strict
    purely-lexicographic lemmas, deterministically sampled. Band 3 is the
    publication core: frequent enough that attestation is not a hapax fluke,
    rare enough that homograph collision is unlikely.
  - CONTROL stratum: 20 text-cited MW senses (single-entry lemmas whose only
    <ls> citations name a primary text) that also sit in DCS band 3. Expected
    sense-match rate is high; the control measures the method's ceiling so the
    hedge stratum's rate can be read against it.

For each sampled sense: the full MW entry line(s) from csl-orig mw.txt, the
<ls> citations, and up to 4 DCS-2026 occurrences (text name, chapter ref,
sandhied sentence) so the verifier can judge: does the corpus attest MW's
sense? Output feeds the /review-sheet HTML sheet.

Inputs (all pre-existing; nothing re-derived):
  ../../lexicographer_dcs/purely_lexicographic_attested_2026.csv  (band-3 pool)
  ../../../csl-orig/v02/mw/mw.txt                                 (MW source)
  ../../../VisualDCS/src/DCS-data-2026/dcs_full.sqlite            (DCS-2026 master)

Outputs (this dir):
  sense_verify_items.json   one object per sense, for the review sheet
  sense_verify_sample.csv   flat summary table
  SAMPLE_SUMMARY.md         strata counts + method note
"""
import sys, os, re, csv, json, random, sqlite3, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
MWS  = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
GH   = os.path.abspath(os.path.join(MWS, '..'))
LEXDIR = os.path.join(MWS, 'lexicographer_dcs')
MWTXT  = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')
DB     = os.path.join(GH, 'VisualDCS', 'src', 'DCS-data-2026', 'dcs_full.sqlite')

SEED = 20260704          # fixed: sample is reproducible
N_HEDGE, N_CONTROL = 60, 20
MAX_OCC = 4              # DCS occurrences shown per lemma

# --- IAST -> SLP1 (same greedy longest-match table as ls_L_dcs2026.py) ---
_MAP = [
    ('ai','E'),('au','O'),
    ('kh','K'),('gh','G'),('ch','C'),('jh','J'),('ṭh','W'),('ḍh','Q'),
    ('th','T'),('dh','D'),('ph','P'),('bh','B'),
    ('ā','A'),('ī','I'),('ū','U'),('ṝ','F'),('ṛ','f'),('ḹ','X'),('ḷ','x'),
    ('ṅ','N'),('ñ','Y'),('ṭ','w'),('ḍ','q'),('ṇ','R'),
    ('ś','S'),('ṣ','z'),('ṃ','M'),('ḥ','H'),('ṁ','M'),('ḻ','L'),('ẖ','H'),('ḫ','H'),
    ('a','a'),('i','i'),('u','u'),('e','e'),('o','o'),
    ('k','k'),('g','g'),('c','c'),('j','j'),('t','t'),('d','d'),('n','n'),
    ('p','p'),('b','b'),('m','m'),('y','y'),('r','r'),('l','l'),('v','v'),
    ('s','s'),('h','h'),
]
def iast_to_slp1(s):
    s = unicodedata.normalize('NFC', s.strip().lower())
    out, i, n = [], 0, len(s)
    while i < n:
        for src, dst in _MAP:
            if s.startswith(src, i):
                out.append(dst); i += len(src); break
        else:
            i += 1
    return ''.join(out)

# Meta / relative sigla that do NOT count as a primary-text citation
META_LS = {'L.', 'W.', 'MW.', 'ib.', 'Cat.'}

# --- 1. parse mw.txt into k1 -> [entries] ---
print('parsing mw.txt ...')
entries = {}   # k1 -> list of dicts {L, pc, body(list of lines)}
cur = None
head_re = re.compile(r'^<L>([^<]*)<pc>([^<]*)<k1>([^<]*)<k2>')
with open(MWTXT, encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        m = head_re.match(line)
        if m:
            cur = {'L': m.group(1), 'pc': m.group(2), 'k1': m.group(3), 'body': []}
            continue
        if line.startswith('<LEND>'):
            if cur:
                entries.setdefault(cur['k1'], []).append(cur)
            cur = None
            continue
        if cur is not None:
            cur['body'].append(line)
print(f'  {sum(len(v) for v in entries.values()):,} entries, {len(entries):,} distinct k1')

LS_RE = re.compile(r'<ls[^>]*>([^<]*)</ls>')
def ls_of(body):
    out = []
    for line in body:
        out.extend(x.strip() for x in LS_RE.findall(line))
    return out

TAG_RE = re.compile(r'<[^>]+>')
def plain(body):
    txt = ' '.join(body)
    txt = txt.replace('¦', '').strip()
    return re.sub(r'\s+', ' ', TAG_RE.sub('', txt)).strip()

def raw(body):
    return '\n'.join(body)

def siglum_root(ls):
    # 'MBh. xiii, 26, 8' -> 'MBh.' ; 'Suśr.' -> 'Suśr.'
    return ls.split(',')[0].split()[0] if ls else ls

# --- 2. hedge stratum: band-3 strict purely-lexicographic, DCS-attested ---
b3 = []
with open(os.path.join(LEXDIR, 'purely_lexicographic_attested_2026.csv'), encoding='utf-8') as f:
    for row in csv.DictReader(f):
        if row['dcs2026_band'] == '3':
            b3.append(row)
b3.sort(key=lambda r: r['k1_slp1'])
rng = random.Random(SEED)
hedge = rng.sample(b3, N_HEDGE)
print(f'hedge pool band-3: {len(b3)} -> sampled {len(hedge)}')

# --- 3. DCS-2026 frequencies + slp1 -> IAST lemma map (for occurrence lookup) ---
print('DCS-2026 frequency pass ...')
con = sqlite3.connect(DB)
freq, slp2iast = {}, {}
for lemma, cnt in con.execute("SELECT lemma, COUNT(*) FROM token GROUP BY lemma"):
    if not lemma: continue
    k = iast_to_slp1(lemma)
    if not k: continue
    freq[k] = freq.get(k, 0) + cnt
    slp2iast.setdefault(k, []).append(lemma)

def band_of(n):
    if n <= 0: return None
    if n == 1: return 1
    if n < 10: return 2
    if n < 100: return 3
    if n < 1000: return 4
    return 5

# --- 4. control stratum: single-entry, text-cited-only lemmas in DCS band 3 ---
hedge_k1 = {r['k1_slp1'] for r in b3}
control_pool = []
for k1, es in entries.items():
    if k1 in hedge_k1 or len(es) != 1:
        continue
    if band_of(freq.get(k1, 0)) != 3:
        continue
    cites = ls_of(es[0]['body'])
    if not cites:
        continue
    roots = {siglum_root(c) for c in cites}
    if roots & META_LS:          # any meta citation disqualifies (clean control)
        continue
    control_pool.append(k1)
control_pool.sort()
control = rng.sample(control_pool, N_CONTROL)
print(f'control pool (single-entry, text-cited only, band 3): {len(control_pool)} -> sampled {len(control)}')

# --- 5. DCS occurrences per sampled lemma ---
def occurrences(k1):
    iasts = slp2iast.get(k1, [])
    if not iasts: return []
    q = ('SELECT t.form, t.lemma, s.text_sandhied, c.ref, x.name '
         'FROM token t JOIN sentence s ON t.sentence_id = s.id '
         'JOIN chapter c ON s.chapter_id = c.chapter_id '
         'JOIN text x ON c.text_id = x.text_id '
         f"WHERE t.lemma IN ({','.join('?' * len(iasts))}) "
         'ORDER BY t.id LIMIT ?')
    rows = con.execute(q, iasts + [MAX_OCC]).fetchall()
    return [{'form': r[0], 'dcs_lemma': r[1], 'sentence': (r[2] or '').strip(),
             'ref': r[3], 'text': r[4]} for r in rows]

items = []
def add_item(k1, stratum):
    es = entries.get(k1, [])
    body_raw = '\n---\n'.join(raw(e['body']) for e in es)
    body_plain = ' || '.join(plain(e['body']) for e in es)
    cites = []
    for e in es: cites.extend(ls_of(e['body']))
    items.append({
        'id': f'{stratum[0].upper()}{len(items)+1:03d}',
        'stratum': stratum,
        'k1_slp1': k1,
        'mw_L_ids': [e['L'] for e in es],
        'mw_pc': [e['pc'] for e in es],
        'mw_entry_raw': body_raw,
        'mw_entry_plain': body_plain,
        'ls_citations': cites,
        'dcs2026_tokens': freq.get(k1, 0),
        'dcs_occurrences': occurrences(k1),
    })

for r in hedge:   add_item(r['k1_slp1'], 'hedge')
for k1 in control: add_item(k1, 'control')
con.close()

missing = [it['k1_slp1'] for it in items if not it['mw_L_ids']]
if missing:
    print(f'WARNING: {len(missing)} sampled lemmas not found in mw.txt: {missing[:5]}')

# --- 6. outputs ---
with open(os.path.join(HERE, 'sense_verify_items.json'), 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=1)

with open(os.path.join(HERE, 'sense_verify_sample.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['id','stratum','k1_slp1','dcs2026_tokens','ls_citations','mw_gloss','n_dcs_occ_shown'])
    for it in items:
        w.writerow([it['id'], it['stratum'], it['k1_slp1'], it['dcs2026_tokens'],
                    ' | '.join(it['ls_citations']), it['mw_entry_plain'][:200],
                    len(it['dcs_occurrences'])])

n_h = sum(1 for i in items if i['stratum']=='hedge')
n_c = sum(1 for i in items if i['stratum']=='control')
occ_total = sum(len(i['dcs_occurrences']) for i in items)
with open(os.path.join(HERE, 'SAMPLE_SUMMARY.md'), 'w', encoding='utf-8') as f:
    f.write(f"""# A18 sense-verification sample — build summary

- Seed: `{SEED}` (deterministic; re-running reproduces the identical sample)
- **Hedge stratum:** {n_h} of {len(b3)} band-3 strict purely-lexicographic
  DCS-attested lemmas (`purely_lexicographic_attested_2026.csv`)
- **Control stratum:** {n_c} of {len(control_pool)} single-entry, text-cited-only
  MW lemmas in DCS band 3 (no meta sigla {sorted(META_LS)})
- DCS occurrences attached: {occ_total} (≤{MAX_OCC} per lemma, document order)
- Verifier question per item: *does the DCS context attest MW's sense?*
  yes = sense confirmed · no = homograph / different sense · unsure = defer

_Auto-generated by build_sense_verify.py._
""")

print(f'items: {len(items)} ({n_h} hedge + {n_c} control), occurrences {occ_total}')
print('wrote sense_verify_items.json / sense_verify_sample.csv / SAMPLE_SUMMARY.md')
