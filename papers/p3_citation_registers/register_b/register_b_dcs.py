#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Register-B corpus test — the indigenous (iti) register vs DCS.

P3's Register A is MW's tagged <ls> apparatus; its lexicographer-only sub-register
is the <ls>L.</ls> hedge, ~31% corpus-recoverable (the lexicographer_dcs result).
Register B is the indigenous in-prose `iti <source>` quotative of the
Sanskrit-Sanskrit dictionaries SKD (Śabdakalpadruma) and VCP (Vācaspatya), which
carry ~0 <ls> tags.

Two questions, parallel to the Register-A test:
 1. Is Register B constitutively lexicographic? — what share of its `iti`
    citations target a known kośa / nighaṇṭu (a *lexicon*) rather than a text.
 2. Is that lexical vocabulary corpus-grounded? — what share of SKD/VCP headwords
    occur in DCS, vs MW's general lemma inventory and MW's L.-only subset (31%).

Headwords (<k1>) and DCS-2021 lemma keys are both SLP1 -> direct join.

Outputs (this dir):
  register_b_summary.csv      per dict: records, headwords, lexicon-cited %, DCS %
  REGISTER_B_SUMMARY.md
"""
import sys, os, re, csv, json
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH   = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
ORIG = os.path.join(GH, 'csl-orig', 'v02')
DCS  = os.path.join(GH, 'VisualDCS', 'dcs_lemma_summary.json')

L_RE  = re.compile(r'^<L>')
K1_RE = re.compile(r'<k1>([^<]*)')
ITI_RE = re.compile(r' iti ([a-zA-Zā-ṣĀ-Ṣ-￿]+)')

# Known Sanskrit kośas / nighaṇṭus cited via `iti` in SKD/VCP (SLP1, transparent list).
# Conservative: named lexical authorities only; commentators / vernacular glosses
# ('BAzA', 'kecit', 'ca') are NOT counted as lexicon sources.
KOSA = {
 'rAjanirGaRwaH','medinI','hemacandraH','hema','SabdaratnAvalI','kavikalpadrumaH',
 'trikARqaSezaH','jawADaraH','SabdacandrikA','ratnamAlA','SabdamAlA','hArAvalI',
 'halAyuDaH','rAjavallaBaH','SabdaratnA','amaraH','amara','viSvaH','viSvaprakASaH',
 'SASvataH','vEjayantI','nAnArTaH','nAnArTArRavaH','SabdArTacintAmaRiH','BAvaprakASaH',
 'DaraRiH','SabdaratnAkaraH','ajayaH','rAjanirGaRwe','medinyAm','hEmaH','viSvamedinyOH',
}

with open(DCS, encoding='utf-8') as f:
    dcs = json.load(f)['lemmas']
def _att(k):
    e = dcs.get(k); return bool(e and e.get('attested'))
def attested(k):
    # SKD cites headwords in nominative-singular form (aMSaH, aMSakaM, aMSuH); DCS
    # lemmas are bare stems. Try the citation form AND de-inflected stem candidates.
    # (Validated: this leaves bare-stem dicts like VCP unchanged, +0.0 pts.)
    if _att(k): return True
    if k.endswith('H') and _att(k[:-1]): return True       # visarga: aMSuH->aMSu
    if k.endswith('M') and _att(k[:-1]): return True       # anusvara neut: aMSakaM->aMSaka
    if k.endswith('aH') and _att(k[:-2]+'a'): return True
    return False

def analyse(path):
    """Return (records, distinct_headwords, lex_cited_hw, attested_hw,
               attested_lexcited_hw, iti_total, iti_to_kosa)."""
    heads = {}           # k1 -> {'lex':bool}
    iti_total = iti_kosa = 0
    cur_k1 = None; body = []
    def flush():
        nonlocal iti_total, iti_kosa
        if cur_k1 is None: return
        text = ''.join(body)
        srcs = ITI_RE.findall(text)
        iti_total += len(srcs)
        is_lex = False
        for s in srcs:
            if s in KOSA:
                iti_kosa += 1; is_lex = True
        d = heads.setdefault(cur_k1, {'lex': False})
        if is_lex: d['lex'] = True
    with open(path, encoding='utf-8') as f:
        for line in f:
            if L_RE.match(line):
                flush()
                m = K1_RE.search(line); cur_k1 = m.group(1) if m else None
                body = []
            elif line.startswith('<LEND>'):
                flush(); cur_k1 = None; body = []
            elif cur_k1 is not None:
                body.append(line)
        flush()
    n_records = sum(1 for _ in open(path, encoding='utf-8') if _.startswith('<L>'))
    hw = list(heads)
    att = [k for k in hw if attested(k)]
    lex_hw = [k for k,v in heads.items() if v['lex']]
    att_lex = [k for k in lex_hw if attested(k)]
    return dict(records=n_records, hw=len(hw), att=len(att), lex_hw=len(lex_hw),
                att_lex=len(att_lex), iti_total=iti_total, iti_kosa=iti_kosa)

# --- MW comparison: distinct k1 DCS-attestation (general inventory) ---
mw_hw = set()
with open(os.path.join(ORIG,'mw','mw.txt'), encoding='utf-8') as f:
    for line in f:
        if line.startswith('<L>'):
            m = K1_RE.search(line)
            if m: mw_hw.add(m.group(1))
mw_att = sum(1 for k in mw_hw if attested(k))

res = {}
for d in ('skd','vcp'):
    p = os.path.join(ORIG, d, d+'.txt')
    if os.path.exists(p):
        res[d] = analyse(p)

# --- write ---
with open(os.path.join(HERE,'register_b_summary.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f)
    w.writerow(['dict','records','headwords','iti_total','iti_to_kosa','iti_kosa_pct',
                'headwords_lexicon_cited','dcs_attested_hw','dcs_pct','dcs_pct_lexcited'])
    for d,r in res.items():
        w.writerow([d.upper(), r['records'], r['hw'], r['iti_total'], r['iti_kosa'],
                    f"{100*r['iti_kosa']/r['iti_total']:.1f}" if r['iti_total'] else '',
                    r['lex_hw'], r['att'], f"{100*r['att']/r['hw']:.1f}" if r['hw'] else '',
                    f"{100*r['att_lex']/r['lex_hw']:.1f}" if r['lex_hw'] else ''])

def pct(a,b): return f"{100*a/b:.1f}%" if b else "—"
S=[]
S.append('# Register-B corpus test — the indigenous `iti` register vs DCS\n')
S.append('Parallel to the Register-A (`<ls>L.</ls>`→DCS) result. SKD/VCP headwords and')
S.append('DCS-2021 lemma keys are both SLP1. **Lemma-level, lemma-now.**\n')
S.append('## 1. Register B is constitutively lexicographic (the headline)')
S.append(f'- **SKD**: of {res["skd"]["iti_total"]:,} `iti` citations, **{pct(res["skd"]["iti_kosa"],res["skd"]["iti_total"])}** '
         f'target a named kośa / nighaṇṭu in the (conservative) lexicon list')
S.append(f'  (`rājanighaṇṭu`, `medinī`, `hemacandra`, `śabdaratnāvalī`, `kavikalpadruma`, …)')
S.append(f'  — a floor, since the long tail of lexical sources is unclassified.')
S.append('')
S.append('Where MW marks lexicographer-only material with an *exceptional* hedge')
S.append('(`<ls>L.</ls>`, 13% of citations), the indigenous register cites lexicons by')
S.append('**default**. The `L.` hedge is Register A\'s way of flagging, as exceptional, what')
S.append('is the constitutive norm of Register B. (VCP\'s `iti`-source vocabulary differs')
S.append('from SKD\'s; the SKD-derived kośa list does not measure it — VCP\'s lexical share')
S.append('is left open, not zero.)\n')
S.append('## 2. Is that lexical vocabulary corpus-grounded?')
S.append('Yes — about half of it is. SKD headwords are cited in nominative-singular form')
S.append('(`aMSaH`, `aMSakaM`), so a stem-aware match is required; the de-inflected figure')
S.append('is the real one (the same de-inflection leaves bare-stem VCP unchanged, a +0.0-pt')
S.append('control).')
S.append('')
S.append('| inventory | headwords | DCS-attested | rate |')
S.append('|---|--:|--:|--:|')
for d,r in res.items():
    S.append(f'| {d.upper()} — all headwords (stem-aware) | {r["hw"]:,} | {r["att"]:,} | **{pct(r["att"],r["hw"])}** |')
S.append(f'| *context:* MW — all headwords | {len(mw_hw):,} | {mw_att:,} | {pct(mw_att,len(mw_hw))} |')
S.append(f'| *context:* MW — `L.`-only lemmas (DCS-2021) | 18,930 | 5,871 | 31.0% |')
S.append('')
S.append('So the indigenous lexical inventory is **not** a closed self-referential universe:')
S.append('~half of SKD and VCP headwords occur in dated texts. The constitutively-lexical')
S.append('*citation style* (§1) does **not** imply a corpus-detached *vocabulary*.')
S.append('\n## Caveats')
S.append('- **MW is context, not a benchmark.** MW\'s rate (28.2%) is over 194k headwords —')
S.append('  ~4× the indigenous inventories — and is diluted by its compound-heavy')
S.append('  macrostructure; the lower number reflects inventory composition, not weaker')
S.append('  grounding. Do not read "indigenous > MW".')
S.append('- Lemma-level; a headword counts as attested for *any* corpus sense (homograph')
S.append('  exposure).')
S.append('- **The SKD figure is approximate (±).** The visarga/anusvāra stem-recovery can')
S.append('  over- or under-strip; the VCP-unchanged control validates the *direction* of')
S.append('  the correction, not the *precision* of SKD\'s 50.3% — read it as ~50%, not exact.')
S.append('- **The kośa/text binary is soft-edged.** Some `iti` sources blur the line — e.g.')
S.append('  `Bhāvaprakāśa` is a medical *text* carrying a nighaṇṭu section — so 46.7% is a')
S.append('  floor with a fuzzy boundary, not a sharp count.')
S.append('- VCP lexical-share unmeasured (kośa list is SKD-specific). The nine-dict register')
S.append('  comparison is the atlas CITATION_REGISTERS work, not this memo.')
open(os.path.join(HERE,'REGISTER_B_SUMMARY.md'),'w',encoding='utf-8').write('\n'.join(S)+'\n')

print(f'MW headwords {len(mw_hw)}, DCS-attested {mw_att} ({pct(mw_att,len(mw_hw))})')
for d,r in res.items():
    print(f'{d.upper()}: records {r["records"]}, hw {r["hw"]}, iti {r["iti_total"]} '
          f'(kośa {pct(r["iti_kosa"],r["iti_total"])}), DCS-hw {pct(r["att"],r["hw"])}, '
          f'lex-cited-hw {r["lex_hw"]} DCS {pct(r["att_lex"],r["lex_hw"])}')