"""Task 2 (DOUBTS D7) — significance tests + confidence intervals.

For every (article-type, block) cell we build a per-entry 2x2 table
(type vs rest) x (block present vs absent), and report:
  - the within-type percentage with a Wilson 95% CI,
  - the baseline rate in all other entries,
  - a chi-square p-value (Fisher exact when any expected cell < 5),
  - whether the enrichment/suppression is significant at alpha = 0.05.

It then audits the specific headline contrasts the paper makes, including the
D7 example (F08 in noun_m vs noun_f, a direct pairwise test).

Run:  python significance.py
"""
import math
import os
from collections import Counter, defaultdict

from scipy import stats

from _common import iter_mw, detect_blocks, classify_type, BLOCK_ORDER, TYPE_ORDER

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA = 0.05


def wilson(k, nn, z=1.96):
    if nn == 0:
        return (0.0, 0.0)
    p = k / nn
    denom = 1 + z * z / nn
    centre = p + z * z / (2 * nn)
    adj = z * math.sqrt(p * (1 - p) / nn + z * z / (4 * nn * nn))
    return ((centre - adj) / denom, (centre + adj) / denom)


def pval_2x2(a, b, c, d):
    """p-value for [[a,b],[c,d]]; Fisher when any expected < 5, else chi2 (Yates)."""
    table = [[a, b], [c, d]]
    tot = a + b + c + d
    if tot == 0:
        return 1.0, 'na'
    row1, row2 = a + b, c + d
    col1, col2 = a + c, b + d
    expected = [row1 * col1 / tot, row1 * col2 / tot, row2 * col1 / tot, row2 * col2 / tot]
    if min(expected) < 5:
        _, p = stats.fisher_exact(table)
        return p, 'fisher'
    _, p, _, _ = stats.chi2_contingency(table, correction=True)
    return p, 'chi2'


def main():
    print('Loading + classifying...')
    type_count = Counter()
    block_total = Counter()
    matrix = defaultdict(Counter)
    n = 0
    for r in iter_mw():
        blocks = detect_blocks(r['body'])
        types = classify_type(r['body'], r['k2'], r['ecode'])
        n += 1
        for b in blocks:
            block_total[b] += 1
        for t in types:
            type_count[t] += 1
            for b in blocks:
                matrix[t][b] += 1
    print(f'  {n:,} records')

    present_types = [t for t in TYPE_ORDER if type_count[t] > 0]

    rows = []  # (type, block, k, row_t, pct, lo, hi, base_pct, diff, p, test, sig)
    for t in present_types:
        row_t = type_count[t]
        for b in BLOCK_ORDER:
            a = matrix[t][b]
            b_cell = row_t - a
            c = block_total[b] - a
            d = (n - row_t) - c
            pct = 100 * a / row_t if row_t else 0
            lo, hi = wilson(a, row_t)
            base = 100 * c / (c + d) if (c + d) else 0
            p, test = pval_2x2(a, b_cell, c, d)
            sig = p < ALPHA
            rows.append((t, b, a, row_t, pct, 100*lo, 100*hi, base, pct - base, p, test, sig))

    # ---- report ----
    lines = []
    def out(s=''):
        print(s)
        lines.append(s)

    out('=== Per (type, block) enrichment vs baseline ===')
    out(f'{"type":<18}{"blk":<5}{"k":>8}{"N":>8}{"pct":>7}{"  95% CI":>16}{"base":>7}{"diff":>8}{"p":>11}{"  test":>8}{" sig":>5}')
    for (t, b, a, row_t, pct, lo, hi, base, diff, p, test, sig) in rows:
        # only print cells that are non-trivial: pct>=5 or it's a documented kernel/enrichment
        if pct < 1 and base < 1:
            continue
        out(f'{t:<18}{b:<5}{a:>8,}{row_t:>8,}{pct:>6.1f}%{f"[{lo:.1f},{hi:.1f}]":>16}{base:>6.1f}%{diff:>+7.1f}{p:>11.2e}{test:>8}{" *" if sig else "  ":>5}')

    # ---- headline-claim audit ----
    out()
    out('=== Headline-claim audit ===')

    def cell(t, b):
        a = matrix[t][b]; row_t = type_count[t]
        c = block_total[b] - a; d = (n - row_t) - c
        pct = 100*a/row_t if row_t else 0
        lo, hi = wilson(a, row_t)
        base = 100*c/(c+d) if (c+d) else 0
        p, test = pval_2x2(a, row_t-a, c, d)
        return a, row_t, pct, 100*lo, 100*hi, base, p, test

    claims = [
        ('root', 'F09', 'F09 commentary high in roots vs baseline'),
        ('root', 'F05', 'F05 verb-class ~definitional in roots'),
        ('etymological-ie', 'F07', 'F07 IE cognate definitional in etymological'),
        ('botanical', 'F13', 'F13 hedge ~72% in botanical'),
        ('biographical', 'F13', 'F13 hedge ~65% in biographical'),
        ('lexicographer-only', 'F13', 'F13 hedge 100% in lexicographer-only'),
        ('continuation', 'F02', 'F02 display suppressed in continuation'),
    ]
    for t, b, label in claims:
        a, row_t, pct, lo, hi, base, p, test = cell(t, b)
        verdict = 'SIGNIFICANT' if p < ALPHA else 'n.s.'
        out(f'  {label}')
        out(f'    {b} in {t}: {pct:.1f}% [{lo:.1f},{hi:.1f}]  (N={row_t:,}; baseline {base:.1f}%)  p={p:.2e} [{test}] -> {verdict}')

    # D7 pairwise: F08 in noun_m vs noun_f
    out()
    out('  D7 pairwise — F08 inflection: noun_m vs noun_f')
    am, nm = matrix['noun-m']['F08'], type_count['noun-m']
    af, nf = matrix['noun-f']['F08'], type_count['noun-f']
    pm, pf = 100*am/nm, 100*af/nf
    p, test = pval_2x2(am, nm-am, af, nf-af)
    lom, him = wilson(am, nm); lof, hif = wilson(af, nf)
    out(f'    noun_m F08: {pm:.1f}% [{100*lom:.1f},{100*him:.1f}] (N={nm:,})')
    out(f'    noun_f F08: {pf:.1f}% [{100*lof:.1f},{100*hif:.1f}] (N={nf:,})')
    out(f'    difference {pm-pf:+.1f} pts; p={p:.2e} [{test}] -> '
        f'{"SIGNIFICANT" if p < ALPHA else "n.s. (D7 confirmed: small diff not significant)"}')

    sig_count = sum(1 for r in rows if r[-1])
    out()
    out(f'Cells tested: {len(rows)}; significant at a=0.05: {sig_count}')

    report = os.path.join(HERE, 'SIGNIFICANCE.md')
    with open(report, 'w', encoding='utf-8') as f:
        f.write('# Significance tests + confidence intervals (DOUBTS D7)\n\n')
        f.write('Generated by `significance.py`. 2x2 per (type, block): type-vs-rest x '
                'present-vs-absent. Fisher exact when any expected cell < 5, else '
                'chi-square with Yates correction. Wilson 95% CIs on within-type rates.\n\n')
        f.write('```\n' + '\n'.join(lines).strip() + '\n```\n')
    print(f'\n  wrote {report}')


if __name__ == '__main__':
    main()
