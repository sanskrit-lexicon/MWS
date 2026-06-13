#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
3-way verbal-root crosswalk: MW <-> Whitney hub <-> DCS corpus.

MW anchors ~795 of its verbal roots to Whitney's root list via
<info whitneyroots="root,page"/> (page = Whitney's 1885 root-appendix page, not
the root id). The WhitneyRoots repo is the hub (935 roots) and already carries the
Whitney<->DCS join (src/dcs_freq.json). This joins the MW side on root string
(homonym-normalised) to produce, per Whitney root, whether it is attested in MW
and in DCS — the grammar-corpus-dict crosswalk the roadmap describes.

Outputs (this dir):
  root_crosswalk.csv     whitney_id, root, in_MW, mw_L, mw_classes, dcs_status, dcs_freq
  mw_whitney_unmatched.csv   MW anchors that match no hub root (candidate errors)
  ROOT_CROSSWALK_SUMMARY.md
"""
import sys, os, re, csv, json
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH   = os.path.abspath(os.path.join(HERE, '..', '..'))
MW   = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')
WR   = os.path.join(GH, 'WhitneyRoots', 'src')

_S2I = {'A':'ā','I':'ī','U':'ū','f':'ṛ','F':'ṝ','x':'ḷ','X':'ḹ','E':'ai','O':'au',
        'M':'ṃ','H':'ḥ','K':'kh','G':'gh','N':'ṅ','C':'ch','J':'jh','Y':'ñ',
        'w':'ṭ','W':'ṭh','q':'ḍ','Q':'ḍh','R':'ṇ','T':'th','D':'dh','P':'ph',
        'B':'bh','S':'ś','z':'ṣ','L':'ḻ'}
def s2i(s):   return ''.join(_S2I.get(c, c) for c in s)
def bare(r):  # strip homonym markers: leading "1 " (hub) or trailing digit (MW)
    r = re.sub(r'^\d+\s+', '', r.strip())
    r = re.sub(r'\d+$', '', r)
    return r

# --- hub ---
hub = json.load(open(os.path.join(WR,'..','src','app_data.json'), encoding='utf-8'))['lexicon']
dcs = json.load(open(os.path.join(WR,'dcs_freq.json'), encoding='utf-8'))['entries']
bare2ids = {}
hub_by_id = {}
for r in hub:
    b = bare(r['root'])
    hub_by_id[r['id']] = {'root': r['root'], 'bare': b}
    bare2ids.setdefault(b, []).append(r['id'])

# --- parse MW roots ---
L_RE = re.compile(r'^<L>([^<]*)')
WR_RE = re.compile(r'whitneyroots="([^"]*)"')
WG_RE = re.compile(r'westergaard="([^"]*)"')
VB_RE = re.compile(r'<info verb="([^"]*)"(?:\s+cp="([^"]*)")?')

genuine = set()                # L of genuine-root records
mw_anchor_bare = {}            # bare IAST root -> (mw_L, page, cp)
mw_unmatched = []
has_wr = set(); has_wg = set()
cur_L = None; rec = []
def flush():
    if cur_L is None: return
    t = ''.join(rec)
    vb = VB_RE.search(t)
    cp = ''
    if vb:
        if vb.group(1) == 'genuineroot':
            genuine.add(cur_L)
        cp = vb.group(2) or ''
    for v in WR_RE.findall(t):
        has_wr.add(cur_L)
        for part in v.split(';'):
            root = part.rsplit(',', 1)[0]
            page = part.rsplit(',', 1)[1] if ',' in part else ''
            b = bare(s2i(root))
            mw_anchor_bare.setdefault(b, (cur_L, page, cp))
    if WG_RE.search(t):
        has_wg.add(cur_L)

with open(MW, encoding='utf-8') as f:
    for line in f:
        if line.startswith('<L>'):
            flush(); cur_L = L_RE.match(line).group(1); rec = []
        elif line.startswith('<LEND>'):
            flush(); cur_L = None; rec = []
        elif cur_L is not None:
            rec.append(line)
flush()

# match MW anchors to hub
matched_bares = set()
for b in mw_anchor_bare:
    if b in bare2ids:
        matched_bares.add(b)
    else:
        mw_unmatched.append((b, mw_anchor_bare[b][0], mw_anchor_bare[b][1]))

# --- per-Whitney-root crosswalk ---
rows = []
in_mw = in_dcs = in_both = 0
for r in hub:
    hid = r['id']; b = hub_by_id[hid]['bare']
    mw = mw_anchor_bare.get(b)
    d = dcs.get(hid, {})
    dstat = d.get('dcs_status', ''); dfreq = d.get('total', '')
    mwflag = 'yes' if mw else 'no'
    dflag = (dstat == 'matched')
    if mw: in_mw += 1
    if dflag: in_dcs += 1
    if mw and dflag: in_both += 1
    rows.append([hid, r['root'], mwflag, mw[0] if mw else '', mw[2] if mw else '',
                 dstat, dfreq])

with open(os.path.join(HERE,'root_crosswalk.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['whitney_id','root','in_MW','mw_L','mw_classes','dcs_status','dcs_freq'])
    w.writerows(rows)
with open(os.path.join(HERE,'mw_whitney_unmatched.csv'),'w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['mw_root_iast_bare','mw_L','whitney_page']); w.writerows(mw_unmatched)

NH = len(hub)
S=[]
S.append('# 3-way verbal-root crosswalk: MW ↔ Whitney ↔ DCS\n')
S.append('## MW side')
S.append(f'- MW genuine-root records (`verb="genuineroot"`): **{len(genuine):,}**')
S.append(f'- …with a Whitney anchor (`<info whitneyroots>`): {len(has_wr):,}')
S.append(f'- …with a Westergaard anchor (`<info westergaard>`): {len(has_wg):,}')
S.append(f'- Distinct MW-anchored roots matched to the hub: {len(matched_bares):,};')
S.append(f'  **unmatched (candidate anchor errors): {len(mw_unmatched):,}** → `mw_whitney_unmatched.csv`\n')
S.append('## Coverage of the 935-root Whitney hub')
S.append(f'- Attested in **MW**: **{in_mw:,}** ({100*in_mw/NH:.1f}%)')
S.append(f'- Attested in **DCS** corpus: **{in_dcs:,}** ({100*in_dcs/NH:.1f}%)')
S.append(f'- **In BOTH MW and DCS (fully triangulated): {in_both:,}** ({100*in_both/NH:.1f}%)')
S.append(f'- MW+Whitney but **DCS-absent** (grammarian/lexical roots): {in_mw-in_both:,}')
S.append(f'- DCS+Whitney but **MW-unanchored** (anchoring gap to close): {in_dcs-in_both:,}')
S.append(f'- In neither MW nor DCS: {NH-(in_mw+in_dcs-in_both):,}\n')
S.append('## Why it matters')
S.append('- The fully-triangulated roots (MW gloss + Whitney grammar + DCS frequency)')
S.append('  are the ready core of the grammar-corpus-dict crosswalk: a root you can')
S.append('  define, conjugate, and frequency-rank at once.')
S.append('- Roots in Whitney+DCS but NOT anchored in MW are the gap to close (add the')
S.append('  `<info whitneyroots>` anchor); roots in MW+Whitney but DCS-unmatched are')
S.append('  corpus-absent (lexical/grammarian roots) — a P3/P4 signal.')
S.append('\n## Notes')
S.append('- Join is on homonym-normalised root string (MW `akz1`/`akz2` ↔ hub `1 akṣ`).')
S.append('- The number in `whitneyroots="root,N"` is Whitney\'s 1885 root-appendix page')
S.append('  (max 210, many roots share a page), NOT a root id — decoded here.')
S.append('- `mw_whitney_unmatched.csv` are MW anchors with no hub root after')
S.append('  normalisation: either MW-side typos or roots absent from the hub.')
open(os.path.join(HERE,'ROOT_CROSSWALK_SUMMARY.md'),'w',encoding='utf-8').write('\n'.join(S)+'\n')

print(f'MW genuine roots {len(genuine)} | whitney-anchored {len(has_wr)} | westergaard {len(has_wg)}')
print(f'hub {NH}: in_MW {in_mw}, in_DCS {in_dcs}, in_both {in_both}')
print(f'MW anchors unmatched to hub: {len(mw_unmatched)}')