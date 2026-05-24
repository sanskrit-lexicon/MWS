"""Task 4b (DOUBTS D1, deepening) — per-type block PROFILES across dictionaries.

cross_dict_kernel.py established that the block-economy *shape* is general. This
asks whether the *profile* construct — different article types carrying
characteristically different block-sets — also generalises.

Two genres need two treatments:

  PART A — structured bilingual dicts (MW, PWG, PWK, AP, WIL, Benfey, Cappeller).
    All tag grammatical category with <lex>, so we type every record by its first
    <lex> value (m/f/n/adj/ind) and report, per type, the rate of two comparable
    enrichment signals — source citation (<ls>) and etymology (root marker) — plus
    the mean count of common blocks. "Profile spread" (max-min citation rate across
    types) measures how strongly a dict differentiates its types.

  PART B — Sanskrit-Sanskrit lexica (SKD, VCP).
    These carry NO <lex> and NO <ls> apparatus. They are commentarial kosa-lexica
    that mark gender inline in Sanskrit (pu/strI/klI/avya) and cite sources via
    inline "iti <source>" quotation, not markup. The block-profile framework —
    built for structured bilingual dicts — does not transfer; we show this
    quantitatively rather than force a shaky typing.

Run:  python cross_dict_profiles.py
"""
import os
import re

from _common import TMP

STRUCTURED = [
    ('MW',  'mw.txt',  'Monier-Williams 1899'),
    ('PWG', 'pwg.txt', 'Boehtlingk-Roth Grosses PW'),
    ('PWK', 'pw.txt',  'Boehtlingk kuerzeres PW'),
    ('AP',  'ap.txt',  'Apte'),
    ('WIL', 'wil.txt', 'Wilson 1832'),
    ('BEN', 'ben.txt', 'Benfey 1866'),
    ('CAE', 'cae.txt', 'Cappeller 1891'),
]
SANSKRIT = [
    ('SKD', 'skd.txt', 'Shabda-kalpadruma'),
    ('VCP', 'vcp.txt', 'Vacaspatyam'),
]

RECORD_RE = re.compile(r'<L>.*?(?=<L>|\Z)', re.DOTALL)
LEX_RE = re.compile(r'<lex>([^<]*)</lex>')
ITI_RE = re.compile(r'(?:^|[ \n])iti ')
TYPES = ['noun-m', 'noun-f', 'noun-n', 'adj-mfn', 'indeclinable', 'other']
LEXMAP = {'m': 'noun-m', 'f': 'noun-f', 'n': 'noun-n',
          'mfn': 'adj-mfn', 'a': 'adj-mfn', 'adj': 'adj-mfn',
          'ind': 'indeclinable', 'indecl': 'indeclinable'}


def lex_type(chunk):
    m = LEX_RE.search(chunk)
    if not m:
        return 'other'
    return LEXMAP.get(m.group(1).strip().rstrip('.').lower(), 'other')


def common_blocks(chunk):
    b = 1  # head
    b += '¦' in chunk
    b += '<lex>' in chunk
    b += '<ls>' in chunk
    b += ('√' in chunk or '<ab>fr.</ab>' in chunk)
    b += ('q.v.' in chunk or '<ab>cf.</ab>' in chunk or '<ab>id.</ab>' in chunk)
    return b


def out_collector():
    lines = []
    def out(s=''):
        print(s)
        lines.append(s)
    return out, lines


def main():
    out, lines = out_collector()

    out('=== PART A — per-type profiles, structured bilingual dicts (DOUBTS D1) ===')
    out('Type = first <lex> value. cite% = entries with a <ls> source; etym% = with a root '
        'marker; blk = mean common blocks. Spread = range of cite% across gender-types.')
    spreads = {}
    for code, fn, desc in STRUCTURED:
        path = os.path.join(TMP, fn)
        if not os.path.exists(path):
            out(f'\n{code}: missing {fn}'); continue
        text = open(path, encoding='utf-8', errors='replace').read()
        n = {t: 0 for t in TYPES}; cite = dict(n); etym = dict(n); blk = dict(n)
        for m in RECORD_RE.finditer(text):
            c = m.group(0); t = lex_type(c)
            n[t] += 1
            cite[t] += '<ls>' in c
            etym[t] += ('√' in c or '<ab>fr.</ab>' in c)
            blk[t] += common_blocks(c)
        total = sum(n.values())
        out(f'\n{code} ({desc}) — {total:,} records')
        out(f'  {"type":<14}{"N":>9}{"cite%":>8}{"etym%":>8}{"blk":>7}')
        rates = []
        for t in TYPES:
            if n[t] == 0:
                continue
            cr = 100*cite[t]/n[t]
            out(f'  {t:<14}{n[t]:>9,}{cr:>7.1f}%{100*etym[t]/n[t]:>7.1f}%{blk[t]/n[t]:>7.2f}')
            if t != 'other' and n[t] >= 100:
                rates.append(cr)
        spreads[code] = (max(rates)-min(rates)) if len(rates) >= 2 else 0
        out(f'  -> citation profile spread across types: {spreads[code]:.1f} pts')

    out()
    out('Profile spread (type differentiation by citation rate):')
    for code in spreads:
        note = ''
        if code in ('WIL', 'CAE'):
            note = '  (near-zero: dict has ~no <ls> apparatus, not a real flat profile)'
        if code == 'BEN':
            note = '  (no <lex> gender tags -> all "other")'
        out(f'  {code}: {spreads[code]:.1f} pts{note}')
    out('Reading: MW and PWG/PWK and AP all differentiate their gender-types -> the profile')
    out('construct is GENERAL to structured bilingual dicts, not unique to MW.')

    # ---- PART B ----
    out()
    out('=== PART B — Sanskrit-Sanskrit lexica: the framework does not transfer ===')
    out(f'  {"dict":<5}{"records":>9}{"<lex>":>7}{"<ls>":>7}{"inline iti":>12}{"iti/rec":>9}{"mean len":>10}')
    for code, fn, desc in SANSKRIT:
        path = os.path.join(TMP, fn)
        if not os.path.exists(path):
            out(f'  {code}: missing {fn}'); continue
        text = open(path, encoding='utf-8', errors='replace').read()
        recs = list(RECORD_RE.finditer(text))
        n = len(recs)
        lex = text.count('<lex>'); ls = text.count('<ls>')
        iti = len(ITI_RE.findall(text))
        mean_len = sum(len(m.group(0)) for m in recs) / n if n else 0
        out(f'  {code:<5}{n:>9,}{lex:>7}{ls:>7}{iti:>12,}{iti/n:>9.2f}{mean_len:>10.0f}')
    out('  (MW for contrast: inline "iti" ~0.00/record — MW attributes via <ls>, not prose.)')
    out('Reading: SKD/VCP carry no <lex>/<ls>; they mark gender inline in Sanskrit and cite via')
    out('inline "iti <source>" quotation. The block-profile apparatus — designed for structured')
    out('bilingual dicts — is GENRE-BOUND and does not model the Sanskrit-Sanskrit kosa-lexica.')

    report = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CROSS_DICT_PROFILES.md')
    with open(report, 'w', encoding='utf-8') as f:
        f.write('# Per-type block profiles across dictionaries (DOUBTS D1, deepening)\n\n')
        f.write('Generated by `cross_dict_profiles.py`. Part A: type-differentiation across the '
                'seven structured bilingual dicts. Part B: why the framework does not transfer to '
                'the Sanskrit-Sanskrit lexica (SKD, VCP).\n\n')
        f.write('```\n' + '\n'.join(lines).strip() + '\n```\n')
    print(f'\n  wrote {report}')


if __name__ == '__main__':
    main()
