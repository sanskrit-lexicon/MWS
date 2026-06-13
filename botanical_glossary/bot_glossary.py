#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MW botanical glossary export (issue #74) — FAIR dataset.

The legacy botbio/mw_bot.txt is only a binomial frequency count. This builds the
useful artefact: a per-headword Sanskrit <-> Linnaean glossary with provenance
and corpus attestation, cross-linked to the <ls>L.</ls> finding.

For every <bot>...</bot> in mw.txt we capture:
  - the Sanskrit headword (k1, SLP1 + IAST)
  - the Linnaean binomial (raw + canonicalised Genus-species)
  - provenance: L-number, page,column
  - the sense's citation, and whether it is lexicographer-only (<ls>L.</ls>)
  - DCS-2021 attestation of the headword (band)

Novel cross-link: botanical names MW marked lexicographers-only that the modern
corpus nonetheless attests (intersection of #74 and the L./DCS pilot).

Outputs (this dir):
  mw_botanical_glossary.csv     one row per (headword, binomial) occurrence
  species_to_sanskrit.json      canonical species -> sorted Sanskrit synonyms
  BOTANICAL_SUMMARY.md
"""
import sys, os, re, csv, json
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH   = os.path.abspath(os.path.join(HERE, '..', '..'))
MW   = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')
DCS  = os.path.join(GH, 'VisualDCS', 'dcs_lemma_summary.json')

BOT_RE = re.compile(r'<bot>([^<]*)</bot>')
LS_RE  = re.compile(r'<ls(?:\s[^>]*)?>(.*?)</ls>')
K1_RE  = re.compile(r'<k1>([^<]*)')
PC_RE  = re.compile(r'<pc>([^<]*)')
L_RE   = re.compile(r'^<L>([^<]*)')
BAND   = {1:'hapax(1)',2:'rare(2-9)',3:'uncommon(10-99)',4:'common(100-999)',5:'very-common(1000+)'}

# --- SLP1 -> IAST (k1 has no accents, single-char map is exact) ---
_S2I = {'A':'ā','I':'ī','U':'ū','f':'ṛ','F':'ṝ','x':'ḷ','X':'ḹ','E':'ai','O':'au',
        'M':'ṃ','H':'ḥ','K':'kh','G':'gh','N':'ṅ','C':'ch','J':'jh','Y':'ñ',
        'w':'ṭ','W':'ṭh','q':'ḍ','Q':'ḍh','R':'ṇ','T':'th','D':'dh','P':'ph',
        'B':'bh','S':'ś','z':'ṣ','L':'ḻ'}
def slp1_to_iast(s):
    return ''.join(_S2I.get(c, c) for c in s)

def canon_binomial(b):
    """Genus capitalised, epithet(s) lowercase; trim notes/punctuation."""
    b = b.strip().strip('.,;')
    b = re.sub(r'\s+', ' ', b)
    if not b:
        return ''
    parts = b.split(' ')
    out = [parts[0][:1].upper() + parts[0][1:].lower()]
    out += [p.lower() for p in parts[1:]]
    return ' '.join(out)

# --- DCS-2021 attestation (SLP1 keyed) ---
with open(DCS, encoding='utf-8') as f:
    dcs = json.load(f)['lemmas']
def dcs_band(k):
    e = dcs.get(k)
    return e['freqBand'] if e and e.get('attested') else None

# --- parse mw.txt, one record at a time ---
rows = []
k1_kind = {}      # k1 -> {'bot':bool, 'nonbot':bool}  (does the lemma have non-plant senses?)
cur_L = cur_k1 = cur_pc = None
rec = []
def flush():
    if cur_L is None:
        return
    text = ''.join(rec)
    bots = BOT_RE.findall(text)
    if cur_k1 is not None:
        d = k1_kind.setdefault(cur_k1, {'bot':False,'nonbot':False})
        if bots: d['bot'] = True
        else:    d['nonbot'] = True
    if not bots:
        return
    lss = LS_RE.findall(text)
    L_only = (len(lss) > 0 and all(x.strip() == 'L.' for x in lss))
    cite = '; '.join(lss) if lss else ''
    band = dcs_band(cur_k1) if cur_k1 else None
    iast = slp1_to_iast(cur_k1) if cur_k1 else ''
    for raw in bots:
        canon = canon_binomial(raw)
        rows.append([cur_k1, iast, canon, raw.strip(), cur_L, cur_pc or '',
                     cite, 'yes' if L_only else 'no',
                     band or '', BAND.get(band, '') if band else ''])

with open(MW, encoding='utf-8') as f:
    for line in f:
        if line.startswith('<L>'):
            flush()
            cur_L = L_RE.match(line).group(1)
            m = K1_RE.search(line); cur_k1 = m.group(1) if m else None
            p = PC_RE.search(line); cur_pc = p.group(1) if p else None
            rec = []
        elif line.startswith('<LEND>'):
            flush(); cur_L = None; rec = []
        elif cur_L is not None:
            rec.append(line)
flush()

# --- write glossary CSV ---
with open(os.path.join(HERE, 'mw_botanical_glossary.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['k1_slp1','k1_iast','species_canonical','species_raw','L_number',
                'page_col','sense_citation','lexicographer_only','dcs_band','dcs_band_label'])
    w.writerows(rows)

# --- species -> sanskrit synonym rings ---
species = {}
for r in rows:
    sp = r[2]
    if sp:
        species.setdefault(sp, set()).add(r[1])  # IAST headword
species_json = {sp: sorted(v) for sp, v in sorted(species.items())}
with open(os.path.join(HERE, 'species_to_sanskrit.json'), 'w', encoding='utf-8') as f:
    json.dump(species_json, f, ensure_ascii=False, indent=1)

# --- stats ---
n_occ = len(rows)
heads = set(r[0] for r in rows)
n_species = len(species)
L_rows = [r for r in rows if r[7] == 'yes']
L_heads = set(r[0] for r in L_rows)
L_attested = set(r[0] for r in L_rows if r[8] != '')
# botanical-only headwords: lemma whose every record is a plant sense (no homograph)
bot_only = {k for k,d in k1_kind.items() if d['bot'] and not d['nonbot']}
# clean novel slice: L.-only plant sense, headword is botanical-only, DCS-attested
clean = [r for r in L_rows if r[0] in bot_only and r[8] != '']
clean_heads = set(r[0] for r in clean)
top_syn = sorted(species_json.items(), key=lambda kv: -len(kv[1]))[:12]

S = []
S.append('# MW botanical glossary (#74) — summary\n')
S.append(f'- `<bot>` occurrences: **{n_occ:,}**')
S.append(f'- Distinct Sanskrit headwords with a botanical sense: **{len(heads):,}**')
S.append(f'- Distinct canonical species (binomials): **{n_species:,}**')
S.append(f'- DCS-attested headwords (any band): {sum(1 for r in rows if r[8]!=""):,} occurrences\n')
S.append('## Cross-link with the `<ls>L.</ls>` finding')
S.append(f'- Botanical senses marked **lexicographer-only**: {len(L_rows):,} occurrences,')
S.append(f'  {len(L_heads):,} distinct headwords ({100*len(L_heads)/len(heads):.0f}% of botanical headwords).')
S.append(f'- Naive lemma-level join: {len(L_attested):,} of those headwords are DCS-attested —')
S.append(f'  **but most high-band hits are homograph collisions** (`kṛṣṇa`, `indra`, `kāla`')
S.append(f'  are common words with a rare *plant* sense marked L.; the corpus frequency is')
S.append(f'  the non-plant sense). Lemma attestation does NOT confirm the botanical sense here.')
S.append(f'- **Honest subset — botanical-only headwords** (lemma whose *every* sense is a')
S.append(f'  plant, so no homograph): {len(bot_only):,} such headwords; of these,')
S.append(f'  **{len(clean_heads):,} are both L.-only and DCS-attested** — clean confirmations')
S.append(f'  of plant vocabulary MW had only from kośas that the corpus nonetheless attests.\n')
S.append('## Biggest synonym rings (one species, many Sanskrit names)')
S.append('| species | # Sanskrit synonyms |')
S.append('|---|--:|')
for sp, syns in top_syn:
    S.append(f'| *{sp}* | {len(syns)} |')
S.append('\n## Files')
S.append('- `mw_botanical_glossary.csv` — per-occurrence: headword (SLP1+IAST), species')
S.append('  (canonical+raw), L-number, page, citation, lexicographer-only flag, DCS band.')
S.append('- `species_to_sanskrit.json` — canonical species → sorted Sanskrit synonym ring.')
S.append('\n## Notes')
S.append('- Canonicalisation: Genus capitalised, epithet lowercase, notes/punctuation')
S.append('  trimmed — folds `Abrus Precatorius`/`Abrus precatorius` into one species.')
S.append('- Headword IAST via exact SLP1→IAST (k1 carries no accents).')
S.append('- DCS attestation is lemma-level (DCS-2021 summary). Re-run against DCS-2026')
S.append('  for fuller coverage (see ../lexicographer_dcs/).')
S.append('- Supersedes the frequency-only `botbio/mw_bot.txt`; this is the FAIR export.')
open(os.path.join(HERE, 'BOTANICAL_SUMMARY.md'), 'w', encoding='utf-8').write('\n'.join(S) + '\n')

print(f'<bot> occurrences: {n_occ}')
print(f'distinct headwords: {len(heads)}; distinct species: {n_species}')
print(f'L.-only botanical: {len(L_rows)} occ / {len(L_heads)} heads; of those DCS-attested heads: {len(L_attested)}')
print(f'top synonym ring: {top_syn[0][0]} = {len(top_syn[0][1])} names')