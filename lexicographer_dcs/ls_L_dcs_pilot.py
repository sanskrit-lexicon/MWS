#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
<ls>L.</ls> -> DCS corpus verification pilot.

MW marks 40,212 senses <ls>L.</ls> = "lexicographers only" (attested only in
indigenous kośas, no text witness MW knew of). Modern corpora (DCS, Oliver
Hellwig) may now attest some of these words. This pilot tests the cleanest,
most defensible claim at the LEMMA level:

  A "purely-lexicographic lemma" = an MW headword (k1) where EVERY <ls> across
  all its records is literally "L." (and there is >=1 such <ls>). MW had no
  text witness for this word at all. If DCS attests the lemma, the corpus
  refutes the "lexicographers only" status -> a hedge that corpus evidence can re-examine.

Join is direct: MW <k1> and DCS lemmas are both SLP1, no transcoding.

Inputs (relative to GitHub/):
  csl-orig/v02/mw/mw.txt
  VisualDCS/dcs_lemma_summary.json   (DCS-2021, 83,239 lemmas, SLP1)
Outputs (this dir):
  purely_lexicographic_attested.csv  (review-candidates: lemma, band, gloss)
  purely_lexicographic_unattested.csv
  SUMMARY.md (headline numbers)
"""
import sys, os, re, json, csv
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH   = os.path.abspath(os.path.join(HERE, '..', '..'))
MW   = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')
DCS  = os.path.join(GH, 'VisualDCS', 'dcs_lemma_summary.json')

LS_RE   = re.compile(r'<ls(?:\s[^>]*)?>(.*?)</ls>')
K1_RE   = re.compile(r'<k1>([^<]*)')
TAG_RE  = re.compile(r'<[^>]+>')
BAND = {1:'hapax(1)',2:'rare(2-9)',3:'uncommon(10-99)',4:'common(100-999)',5:'very-common(1000+)'}

def gloss_snippet(text):
    """First bar-delimited gloss, tags stripped, trimmed."""
    if '¦' in text:
        text = text.split('¦', 1)[1]
    text = TAG_RE.sub('', text)
    text = text.replace('{', '').replace('}', '').replace('#', '')
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:90]

# --- pass 1: aggregate per k1, record-by-record ---
# agg[k1] = [L_count, nonL_count, uncited_gloss_records]
# uncited_gloss_records = records that HAVE a ¦ gloss but NO <ls> at all.
# These are either (a) common senses MW left uncited (e.g. anta 'end'), or
# (b) cross-ref stubs ('See p. ...'). Either way their presence means the
# lemma is NOT genuinely "known only from lexicons" -> excludes from strict.
agg = {}
snippet = {}
cur_k1 = None
rec_text = []
def flush(k1, text):
    if k1 is None:
        return
    joined = ''.join(text)
    lss = LS_RE.findall(joined)
    L  = sum(1 for x in lss if x.strip() == 'L.')
    nL = len(lss) - L
    has_gloss = '¦' in joined
    a = agg.setdefault(k1, [0, 0, 0])
    a[0] += L; a[1] += nL
    if has_gloss and not lss:
        a[2] += 1
    if k1 not in snippet and has_gloss:
        snippet[k1] = gloss_snippet(joined)

with open(MW, encoding='utf-8') as f:
    for line in f:
        if line.startswith('<L>'):
            flush(cur_k1, rec_text)
            m = K1_RE.search(line)
            cur_k1 = m.group(1) if m else None
            rec_text = []
        elif line.startswith('<LEND>'):
            flush(cur_k1, rec_text)
            cur_k1 = None
            rec_text = []
        elif cur_k1 is not None:
            rec_text.append(line)
    flush(cur_k1, rec_text)

# --- classify ---
# broad  : every <ls> is L. (coarse; contaminated by uncited-common-sense words)
# strict : every <ls> is L. AND no uncited gloss record AND no cross-ref stub
#          -> genuinely "MW knew this word only from kośas"
broad      = {k:v for k,v in agg.items() if v[0] > 0 and v[1] == 0}
purely_lex = {k:v for k,v in agg.items() if v[0] > 0 and v[1] == 0 and v[2] == 0}
partial    = {k:v for k,v in agg.items() if v[0] > 0 and v[1] > 0}

# --- DCS lemma index ---
with open(DCS, encoding='utf-8') as f:
    dcs = json.load(f)
dcs_lem = dcs['lemmas']
def dcs_band(k):
    e = dcs_lem.get(k)
    return e['freqBand'] if e and e.get('attested') else None

attested, unattested = [], []
band_hist = {1:0,2:0,3:0,4:0,5:0}
for k, (Lc, _nL, _u) in sorted(purely_lex.items()):
    b = dcs_band(k)
    row = (k, Lc, b if b else '', BAND.get(b,'') if b else '', snippet.get(k,''))
    if b:
        attested.append(row); band_hist[b]+=1
    else:
        unattested.append(row)

# --- write CSVs ---
def write_csv(name, rows):
    with open(os.path.join(HERE, name), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['k1_slp1','L_sense_count','dcs_freqBand','dcs_band_label','mw_gloss_snippet'])
        w.writerows(rows)
write_csv('purely_lexicographic_attested.csv', attested)
write_csv('purely_lexicographic_unattested.csv', unattested)

# --- summary ---
np, na = len(purely_lex), len(attested)
pct = 100*na/np if np else 0
lines = []
lines.append('# `<ls>L.</ls>` -> DCS verification pilot — results\n')
lines.append(f'- Total MW headwords (k1) with >=1 `<ls>`: **{sum(1 for v in agg.values() if v[0]+v[1]>0):,}**')
lines.append(f'- Broad "every `<ls>` is L." (coarse, contaminated): {len(broad):,}')
lines.append(f'- **Strict purely-lexicographic lemmas** (every `<ls>` is `L.`, AND no uncited gloss/stub — genuinely known only from kośas): **{np:,}**')
lines.append(f'- Partially-hedged lemmas (both `L.` and real citations): {len(partial):,}')
lines.append(f'- DCS corpus index (DCS-2021, summary generated {dcs.get("generatedAt","?")}): {dcs["lemmaCount"]:,} attested lemmas')
lines.append(f'  *(provenance stamp — re-running against a different DCS summary will change the figures below)*\n')
lines.append(f'## Headline')
lines.append(f'- **{na:,} of {np:,} purely-lexicographic lemmas ({pct:.1f}%) are ATTESTED in DCS.**')
lines.append(f'  These are candidates for review: words MW marked lexicographer-only that')
lines.append(f'  nonetheless occur in dated texts.\n')
lines.append('| DCS freq band | purely-lex lemmas attested |')
lines.append('|---|--:|')
for b in (5,4,3,2,1):
    lines.append(f'| {b} {BAND[b]} | {band_hist[b]:,} |')
lines.append(f'\n- Unattested in DCS (genuinely corpus-absent, hedge stands): {len(unattested):,}')
lines.append('\n## Interpretation')
lines.append('- An attested strict purely-lexicographic lemma is a **clean** refutation:')
lines.append('  MW cited *no* text, yet the word occurs in the corpus.')
lines.append('- **Strongest tier = bands 2-3** (rare/uncommon). These are typically plant,')
lines.append('  medical and technical terms MW had only from nighaṇṭus/kośas that DCS now')
lines.append('  attests (e.g. `SAlaparRI` Desmodium, `BfNgaja` Agallochum, `viqaNga`')
lines.append('  Embelia). Frequency 10-99 in dated texts is solid, non-accidental evidence.')
lines.append('- **Band 1 (hapax)** is weak: single corpus occurrences may be DCS lemmatizer')
lines.append('  artefacts. Spot-check, do not auto-apply.')
lines.append('- **Band 4-5 caveat: homograph collision.** A handful of top-band hits are')
lines.append('  short strings (`tA`="Lakṣmī") that collide with a high-frequency *grammatical*')
lines.append('  DCS lemma, not the MW sense. Top-band single/double-letter lemmas need manual')
lines.append('  disambiguation before use.')
lines.append('- **Method note:** a coarse "every `<ls>` is L." test over-counts: common words')
lines.append('  (`anta` "end", `anila` "wind") leave their main sense *uncited* and carry')
lines.append('  one minor L. subsense, so they look purely-lexicographic. The strict filter')
lines.append('  excludes any lemma with an uncited gloss or cross-ref stub, which removes')
lines.append(f'  these (broad {len(broad):,} -> strict {np:,}). This is the key methodological')
lines.append('  lesson for sense-level work in P3.')
lines.append('- This is **lemma-level** (lemma-now). It does not yet verify the specific')
lines.append('  *sense* MW hedged (sense-next needs sense-tagged corpus). For purely-lex')
lines.append('  lemmas the distinction collapses: MW had no witness for the word at all.')
lines.append('- Partially-hedged lemmas are deliberately excluded: there the lemma is')
lines.append('  already text-attested in other senses, so DCS presence cannot refute the')
lines.append('  specific `L.` sense without sense-level data.')
lines.append('\n_Generated by `ls_L_dcs_pilot.py`. DCS: Oliver Hellwig, DCS-2021 snapshot, CC BY._')
with open(os.path.join(HERE, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print(f'purely-lex lemmas: {np}')
print(f'  attested in DCS: {na} ({pct:.1f}%)')
print(f'  band hist (5..1): {[band_hist[b] for b in (5,4,3,2,1)]}')
print(f'partially-hedged:  {len(partial)}')
print('wrote: purely_lexicographic_attested.csv, _unattested.csv, SUMMARY.md')
