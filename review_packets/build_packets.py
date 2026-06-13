#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Build turnkey verification packets so a Sanskritist can confirm the session's
*mechanical* findings with yes/no judgements, no lookups required (red-team M2).

Three packets:
  A. ib. resolutions  — sampled, each with its record gloss + resolved source
  B. band-3 L.→DCS    — each L.-only lemma WITH one real DCS example sentence
                        (the sense-level evidence that settles the homograph
                        question: is the corpus hit MW's word or a homograph?)
  C. class conflicts  — 32 MW-vs-Whitney disagreements, with the Dhātupāṭha
                        (Westergaard) tiebreaker reference where MW records one

Each packet → a readable .md review sheet (with a blank `Verdict:` per item) and
a .csv (blank `verdict` column) for spreadsheet entry. Analysis only.
"""
import sys, os, re, csv, sqlite3
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
GH   = os.path.abspath(os.path.join(HERE, '..', '..'))
MW   = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')
DCSF = os.path.join(GH, 'VisualDCS', 'src', 'DCS-data-2026', 'dcs_full.sqlite')

_S2I = {'A':'ā','I':'ī','U':'ū','f':'ṛ','F':'ṝ','x':'ḷ','X':'ḹ','E':'ai','O':'au',
        'M':'ṃ','H':'ḥ','K':'kh','G':'gh','N':'ṅ','C':'ch','J':'jh','Y':'ñ',
        'w':'ṭ','W':'ṭh','q':'ḍ','Q':'ḍh','R':'ṇ','T':'th','D':'dh','P':'ph',
        'B':'bh','S':'ś','z':'ṣ','L':'ḻ'}
def s2i(s): return ''.join(_S2I.get(c, c) for c in s)
TAG = re.compile(r'<[^>]+>')
def clean(t):
    t = TAG.sub('', t).replace('{','').replace('}','').replace('#','').replace('¦','| ')
    return re.sub(r'\s+',' ',t).strip()

def md_header(title, intro, cols):
    return [f'# {title}\n', intro, '', '> Fill the **Verdict** line on each item. '
            'A blank `verdict` column in the paired `.csv` is provided for spreadsheet entry.\n']

# ---------------------------------------------------------------- PACKET B
def packet_B():
    rows = list(csv.DictReader(open(os.path.join(ROOT,'lexicographer_dcs','purely_lexicographic_attested.csv'),encoding='utf-8')))
    band3 = [r for r in rows if r['dcs_freqBand']=='3']
    targets = {s2i(r['k1_slp1']): r for r in band3}     # IAST -> row
    # one DCS example sentence per lemma
    con = sqlite3.connect(DCSF)
    examples = {}
    qs = list(targets)
    for i in range(0, len(qs), 400):
        chunk = qs[i:i+400]
        ph = ','.join('?'*len(chunk))
        for lemma, sent in con.execute(
            f"SELECT t.lemma, s.text_sandhied FROM token t JOIN sentence s ON t.sentence_id=s.id "
            f"WHERE t.lemma IN ({ph}) GROUP BY t.lemma", chunk):
            examples[lemma] = sent
    con.close()
    out_csv, md = [], md_header(
        'Packet B — band-3 `<ls>L.</ls>` lemmas vs DCS (with corpus example)',
        f'{len(band3)} MW headwords whose entire attestation is the lexicographer hedge `L.`, '
        'yet which DCS attests 10–99×. For each, decide whether the **DCS example sentence uses '
        "MW's word in MW's sense** (confirm) or a **homograph** (reject).", None)
    for iast, r in sorted(targets.items()):
        ex = examples.get(iast, '—  (no DCS sentence retrieved)')
        out_csv.append([r['k1_slp1'], iast, r['mw_gloss_snippet'], ex, ''])
        md += [f'### {iast}  (`{r["k1_slp1"]}`)',
               f'- **MW (L.-only):** {r["mw_gloss_snippet"]}',
               f'- **DCS example:** {clean(ex)[:240]}',
               f'- **Confirm corpus = MW sense? (Y / homograph / unsure)** Verdict: ____\n']
    write('PACKET_B_band3', md, ['k1_slp1','iast','mw_gloss','dcs_example_sentence','verdict'], out_csv)
    return len(band3), sum(1 for v in examples.values() if v)

# ---------------------------------------------------------------- helpers for A & C: pull records from mw.txt
def load_records(want_L=None, want_k1_root=None):
    """Single pass: collect record text for given L-numbers, and the first
    genuine-root record for given k1 roots (with its westergaard ref)."""
    byL, byroot = {}, {}
    cur_L = cur_k1 = None; buf = []
    with open(MW, encoding='utf-8') as f:
        for line in f:
            if line.startswith('<L>'):
                if cur_L is not None:
                    t = ''.join(buf)
                    if want_L and cur_L in want_L and cur_L not in byL: byL[cur_L]=t
                    if want_k1_root and cur_k1 in want_k1_root and 'genuineroot' in t and cur_k1 not in byroot:
                        byroot[cur_k1]=t
                cur_L = re.match(r'^<L>([^<]*)', line).group(1)
                m = re.search(r'<k1>([^<]*)', line); cur_k1 = m.group(1) if m else None
                buf=[line]
            elif line.startswith('<LEND>'):
                t=''.join(buf)
                if want_L and cur_L in want_L and cur_L not in byL: byL[cur_L]=t
                if want_k1_root and cur_k1 in want_k1_root and 'genuineroot' in t and cur_k1 not in byroot:
                    byroot[cur_k1]=t
                cur_L=None; buf=[]
            elif cur_L is not None:
                buf.append(line)
    return byL, byroot

# ---------------------------------------------------------------- PACKET A
def packet_A():
    rows = list(csv.DictReader(open(os.path.join(ROOT,'relative_refs','ib_resolved.csv'),encoding='utf-8')))
    real = [r for r in rows if r['kind']=='real']
    same = [r for r in real if r['confidence']=='same-cluster']
    cross= [r for r in real if r['confidence']=='crossed-headword']
    sample = same[:35] + cross[:15]                      # core + the weaker class to scrutinise
    byL,_ = load_records(want_L=set(r['L_number'] for r in sample))
    out_csv, md = [], md_header(
        'Packet A — `ib.` resolution check (sample of 50)',
        '`ib.` = "ibidem". The resolver assigned each to the preceding source by document order. '
        'For each, read the gloss and decide whether the **resolved source is the one MW meant**. '
        '35 same-cluster (high-confidence) + 15 crossed-headword (the weaker class).', None)
    for r in sample:
        raw = byL.get(r['L_number'],'')
        head, _, body = raw.partition('\n')        # drop the header line
        m = re.search(r'<k1>([^<]*)', head); hw = s2i(m.group(1)) if m else '?'
        rec = clean(body)[:220] or '(continuation record — gloss in body)'
        out_csv.append([r['L_number'], hw, r['terminal_siglum'], r['confidence'], rec, ''])
        md += [f'### L{r["L_number"]} — *{hw}*  →  resolved to **{r["terminal_siglum"]}**  _({r["confidence"]})_',
               f'- {rec}',
               f'- **Is `ib.` here = {r["terminal_siglum"]}? (Y/N/unsure)** Verdict: ____\n']
    write('PACKET_A_ib', md, ['L_number','headword','resolved_to','confidence','record_gloss','verdict'], out_csv)
    return len(sample)

# ---------------------------------------------------------------- PACKET C
def packet_C():
    rows = list(csv.DictReader(open(os.path.join(ROOT,'root_crosswalk','class_concordance.csv'),encoding='utf-8')))
    conf = [r for r in rows if r['verdict']=='conflict']
    roots_slp = {}
    for r in conf:
        # reverse IAST->SLP1 is ambiguous; instead match on the SLP1 of the IAST via the crosswalk's bare root
        roots_slp[r['root']] = r
    # CODE_REVIEW #11: index every genuine-root record by bare root, keeping ALL
    # homonyms (was setdefault → first only), so the reviewer sees the homonym the
    # conflict actually sits on. (Also drops the dead load_records(set()) full scan.)
    idx = {}   # bare root -> list of (k1, record_text)
    cur_k1=None; buf=[]
    def _stash():
        if cur_k1 and 'genuineroot' in ''.join(buf):
            idx.setdefault(s2i(re.sub(r'\d+$','',cur_k1)), []).append((cur_k1, ''.join(buf)))
    with open(MW, encoding='utf-8') as f:
        for line in f:
            if line.startswith('<L>'):
                _stash(); m=re.search(r'<k1>([^<]*)',line); cur_k1=m.group(1) if m else None; buf=[line]
            elif line.startswith('<LEND>'):
                _stash(); cur_k1=None; buf=[]
            elif cur_k1 is not None: buf.append(line)
        _stash()
    def _hom(rec):
        wg = re.search(r'westergaard="[^,]*,([^,]*),', rec)
        dref = f'Dhātup. {wg.group(1)}' if wg else '(no Westergaard ref)'
        gloss = clean(rec.split('¦',1)[1])[:150] if '¦' in rec else clean(rec)[:150]
        return dref, gloss
    out_csv, md = [], md_header(
        'Packet C — MW vs Whitney conjugation-class conflicts (32)',
        'Roots where MW and Whitney assign **disjoint** conjugation classes. **All MW homonym '
        'records** are shown (the class conflict may sit on one of several), with the Dhātupāṭha '
        '(Westergaard) reference where MW records it. Decide the correct class (MW / Whitney / both / other).', None)
    for r in conf:
        homs = idx.get(r['root'], [])
        csv_homs = ' || '.join(f'{k1h}: {_hom(rec)[1]} [{_hom(rec)[0]}]' for k1h,rec in homs) or '(no MW genuineroot record)'
        out_csv.append([r['root'], r['mw_classes'], r['whitney_classes'], len(homs), csv_homs, ''])
        md += [f'### √{r["root"]}',
               f'- **MW class (union over homonyms):** {r["mw_classes"]}   **Whitney class:** {r["whitney_classes"]}']
        if homs:
            for k1h, rec in homs:
                dref, gloss = _hom(rec)
                md.append(f'  - *{s2i(k1h)}* ({dref}): {gloss}')
        else:
            md.append('  - *(no MW genuine-root record found for this bare root)*')
        md.append(f'- **Correct class? (MW / Whitney / both / other; which homonym?)** Verdict: ____\n')
    write('PACKET_C_classconflicts', md, ['root','mw_classes','whitney_classes','n_homonyms','mw_homonym_records','verdict'], out_csv)
    return len(conf)

def write(name, md_lines, csv_header, csv_rows):
    open(os.path.join(HERE,name+'.md'),'w',encoding='utf-8').write('\n'.join(md_lines)+'\n')
    with open(os.path.join(HERE,name+'.csv'),'w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(csv_header); w.writerows(csv_rows)

nb, nbex = packet_B()
na = packet_A()
nc = packet_C()
print(f'Packet B: {nb} band-3 lemmas, {nbex} with a DCS example sentence')
print(f'Packet A: {na} ib. sampled')
print(f'Packet C: {nc} class conflicts')
