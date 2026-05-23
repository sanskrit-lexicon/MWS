"""Task 4 (DOUBTS D1) — is "block economy" MW-specific or general?

The paper claims MW reuses a ~6-block kernel across 286,561 entries with a long
tail of rare enrichments ("block economy"). D1 asks whether this is just a
property of *any* single-volume scholarly dictionary.

The MW block detector keys on MW-specific encodings (<s>, <info>, etc.) and is
not portable. So here we use a deliberately FORMAT-ROBUST, tag-presence block
vocabulary that is comparable across every CDSL `<L>...<LEND>` dictionary,
regardless of language or markup:

    head  every record (definitional)            <L>...
    body  has a head|body separator              ¦
    gram  grammatical-category tag               <lex>
    cite  source-citation apparatus              <ls>
    hom   homograph marker                       <hom>
    etym  etymology marker                       √  or  <ab>fr.</ab>
    xref  cross-reference                        q.v. / <ab>cf.</ab> / <ab>id.</ab>
    hedge generic lexicographer hedge            <ls>L.</ls>
    info  machine-annotation (digitisation)      <info

We then compare, per dict, the DISTRIBUTION of blocks-per-entry (the "economy
shape": small modal kernel + long tail) and each block's population. This tests
the *shape* of block economy on a common footing; it does NOT claim the same
blocks are encoded in every digitisation (they are not — e.g. SKD/VCP carry no
<ls>, PWG uses {#..#} not <s> for headwords). Read it as a shape comparison.

Run:  python cross_dict_kernel.py
"""
import os
import re
from collections import Counter

from _common import TMP

DICTS = [
    ('MW',  'mw.txt',  'Monier-Williams 1899 (1 vol.)'),
    ('PWG', 'pwg.txt', 'Boehtlingk-Roth Grosses PW (7 vol.)'),
    ('PWK', 'pw.txt',  'Boehtlingk kuerzeres PW (1 vol.)'),
    ('AP',  'ap.txt',  'Apte practical (1 vol.)'),
    ('WIL', 'wil.txt', 'Wilson 1832 (1 vol.)'),
    ('BEN', 'ben.txt', 'Benfey 1866 (1 vol.)'),
    ('SKD', 'skd.txt', 'Shabda-kalpadruma (Skt-Skt)'),
    ('VCP', 'vcp.txt', 'Vacaspatyam (Skt-Skt)'),
]

RECORD_RE = re.compile(r'<L>.*?(?=<L>|\Z)', re.DOTALL)
COMMON_BLOCKS = ['head', 'body', 'gram', 'cite', 'hom', 'etym', 'xref', 'hedge', 'info']


def blocks_of(chunk):
    b = {'head'}
    if '¦' in chunk:
        b.add('body')
    if '<lex>' in chunk:
        b.add('gram')
    if '<ls>' in chunk:
        b.add('cite')
    if '<hom>' in chunk:
        b.add('hom')
    if '√' in chunk or '<ab>fr.</ab>' in chunk:
        b.add('etym')
    if 'q.v.' in chunk or '<ab>cf.</ab>' in chunk or '<ab>id.</ab>' in chunk:
        b.add('xref')
    if '<ls>L.</ls>' in chunk:
        b.add('hedge')
    if '<info' in chunk:
        b.add('info')
    return b


def analyse(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        text = f.read()
    pop = Counter()
    perentry = Counter()
    n = 0
    for m in RECORD_RE.finditer(text):
        bl = blocks_of(m.group(0))
        n += 1
        perentry[len(bl)] += 1
        for x in bl:
            pop[x] += 1
    return n, pop, perentry


def modal(perentry):
    return max(perentry.items(), key=lambda kv: kv[1])[0] if perentry else 0


def median(perentry, n):
    cum = 0
    for k in sorted(perentry):
        cum += perentry[k]
        if cum >= n / 2:
            return k
    return 0


def main():
    lines = []
    def out(s=''):
        print(s)
        lines.append(s)

    out('=== Block-economy SHAPE across CDSL dictionaries (DOUBTS D1) ===')
    out('Common, format-robust tag-presence block vocabulary (see script docstring).')
    out()
    results = {}
    for code, fn, desc in DICTS:
        path = os.path.join(TMP, fn)
        if not os.path.exists(path):
            out(f'{code}: missing {fn}')
            continue
        n, pop, perentry = analyse(path)
        results[code] = (n, pop, perentry, desc)

    # population table
    out(f'{"block":<7}' + ''.join(f'{c:>9}' for c in results))
    for blk in COMMON_BLOCKS:
        row = f'{blk:<7}'
        for code in results:
            n, pop, _pe, _d = results[code]
            row += f'{100*pop[blk]/n:>8.1f}%'
        out(row)

    out()
    out(f'{"dict":<5}{"records":>10}{"mean blk":>10}{"modal":>7}{"median":>8}   kernel (blocks present in >=66% of entries)')
    for code in results:
        n, pop, perentry, desc = results[code]
        meanb = sum(k*v for k, v in perentry.items()) / n
        kernel = [b for b in COMMON_BLOCKS if pop[b] / n >= 0.66]
        out(f'{code:<5}{n:>10,}{meanb:>10.2f}{modal(perentry):>7}{median(perentry, n):>8}   {", ".join(kernel)}')

    out()
    out('=== Interpretation (D1) ===')
    out('- "Block economy" = a small modal/median kernel reused across most entries,')
    out('  with a long tail of rare enrichments. Compare the modal/median columns.')
    out('- If every single-volume dict shows the same small kernel, block economy is a')
    out('  general single-volume property and MW\'s claim must be softened to "MW exhibits')
    out('  the block economy CHARACTERISTIC OF single-volume scholarly dictionaries".')
    out('- Multi-volume PWG (7 vols) is the control: if it is denser (larger kernel /')
    out('  more cites/entry), that supports economy being a single-volume constraint.')
    out('- Caveat: this is a SHAPE comparison on a common tag vocabulary, not identical')
    out('  blocks. SKD/VCP (Skt-Skt) carry no <ls>/<lex>; their low counts reflect markup,')
    out('  not necessarily editorial economy. English-format AP/WIL/BEN are the cleanest')
    out('  comparanda to MW; PWG/PWK use {#..#}/{%..%} markup (headword not in <s>).')

    report = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CROSS_DICT.md')
    with open(report, 'w', encoding='utf-8') as f:
        f.write('# Cross-dictionary block-economy shape (DOUBTS D1)\n\n')
        f.write('Generated by `cross_dict_kernel.py`. Format-robust tag-presence block '
                'vocabulary compared across every CDSL dictionary in `/tmp`. A shape '
                'comparison, not an identical-block comparison — read with the caveats.\n\n')
        f.write('```\n' + '\n'.join(lines).strip() + '\n```\n')
    print(f'\n  wrote {report}')


if __name__ == '__main__':
    main()
