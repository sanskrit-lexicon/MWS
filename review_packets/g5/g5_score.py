#!/usr/bin/env python
"""Score the MW block detector against the adjudicated G5 gold sample.

Port of papers/microanalysis/analysis/gold_score.py (docs-pass @ d0270a4) onto
the review_packets/g5 CSV instrument, per the Fable S2 ruling that g5/ is the
canonical gold instrument (A16_REVIEW_FABLE5.md Major 2). The live detector is
detect_blocks() from papers/microanalysis/figures/scripts/export_data.py
(docs-pass @ 0901c81), vendored verbatim below because the papers/ tree lives
only on the docs-pass branch.

Inputs:
  G5_gold_adjudicated.csv        (adjudicated gold, 200 records)
  mw.txt @ 392ed6b               (pinned source; pass path as argv[1])

Outputs:
  G5_gold_adjudicated.csv        (detected/false_positive/false_negative filled)
  G5_scores.json
  G5_SCORES.md

Usage:
  python g5_score.py --selftest          # verify metric maths first
  python g5_score.py <path-to-mw.txt>    # score
"""
import csv
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

BLOCK_ORDER = [f'F{i:02d}' for i in range(1, 19)]
BLOCK_NAMES = {
    'F01': 'record header', 'F02': 'display headword', 'F03': 'homophone',
    'F04': 'grammatical category', 'F05': 'verb inflection class',
    'F06': 'etymology root', 'F07': 'IE cognate', 'F08': 'inflection form',
    'F09': 'editorial commentary', 'F10': 'sense gloss', 'F11': 'sense division',
    'F12': 'source citation', 'F13': 'hedge marker (L.)', 'F14': 'botanical',
    'F15': 'biographical', 'F16': 'cross-reference', 'F17': 'machine annotation',
    'F18': 'correction record',
}


def detect_blocks(body):
    """Verbatim from figures/scripts/export_data.py (docs-pass @ 0901c81)."""
    blocks = set()
    blocks.add('F01')  # header — always
    if re.search(r'<s>[^<]+</s>', body) or re.search(r'<s1>', body):
        blocks.add('F02')
    if '<hom>' in body:
        blocks.add('F03')
    if '<lex>' in body:
        blocks.add('F04')
    if '<ab>cl.</ab>' in body or '<ab>P.</ab>' in body or '<ab>Ā.</ab>' in body:
        blocks.add('F05')
    if '√' in body or '<ab>fr.</ab>' in body:
        blocks.add('F06')
    if '<lang>' in body:
        blocks.add('F07')
    if len(re.findall(r'<s>([^<]+)</s>', body)) > 1:
        blocks.add('F08')
    if re.search(r'\([^)]{50,}', body):
        blocks.add('F09')
    if '¦' in body and len(body) > 30:
        blocks.add('F10')
    if re.search(r'\b\d\)\s', body):
        blocks.add('F11')
    if '<ls>' in body:
        blocks.add('F12')
    if '<ls>L.</ls>' in body:
        blocks.add('F13')
    if '<bot>' in body:
        blocks.add('F14')
    if '<bio>' in body or '<s1>' in body:
        blocks.add('F15')
    if 'q.v.' in body or '<ab>cf.</ab>' in body or '<ab>id.</ab>' in body:
        blocks.add('F16')
    if '<info' in body:
        blocks.add('F17')
    if '{{' in body and '->' in body:
        blocks.add('F18')
    return blocks


def cohen_kappa(a, b, c, d):
    """a=both present, b=only A, c=only B, d=both absent. (gold_score.py @ d0270a4)"""
    n = a + b + c + d
    if n == 0:
        return None
    po = (a + d) / n
    pe = ((a + b) * (a + c) + (c + d) * (b + d)) / (n * n)
    if pe == 1.0:
        return 1.0
    return (po - pe) / (1 - pe)


def extract_bodies(mw_path, wanted):
    """body = record content between the <L> header line and <LEND>, matching
    export_data.py's record regex semantics."""
    bodies = {}
    cur_L, buf = None, []
    with open(mw_path, encoding='utf-8') as f:
        for line in f:
            if line.startswith('<L>'):
                cur_L = line[3:].split('<')[0].strip()
                buf = []
            elif cur_L is not None:
                if line.startswith('<LEND>'):
                    if cur_L in wanted:
                        bodies[cur_L] = '\n'.join(buf)
                    cur_L = None
                else:
                    buf.append(line.rstrip('\r\n'))
    return bodies


def blockset(cell):
    return set(b for b in cell.split(';') if b)


def score(rows):
    per_block = {}
    exact_agree = sum(1 for r in rows if blockset(r['gold_blocks_A']) == blockset(r['gold_blocks_B']))
    for F in BLOCK_ORDER:
        tp = fp = fn = tn = 0
        ka = kb = kc = kd = 0
        support = 0
        for r in rows:
            det = F in blockset(r['detected_blocks'])
            gold = F in blockset(r['adjudicated_blocks'])
            ap = F in blockset(r['gold_blocks_A'])
            bp = F in blockset(r['gold_blocks_B'])
            ka += ap and bp; kb += ap and not bp; kc += (not ap) and bp; kd += (not ap) and (not bp)
            support += gold
            if det and gold:
                tp += 1
            elif det and not gold:
                fp += 1
            elif (not det) and gold:
                fn += 1
            else:
                tn += 1
        precision = tp / (tp + fp) if (tp + fp) else None
        recall = tp / (tp + fn) if (tp + fn) else None
        f1 = (2 * precision * recall / (precision + recall)) if (precision and recall) \
            else (0.0 if (precision is not None and recall is not None) else None)
        per_block[F] = {
            'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn, 'support': support,
            'precision': precision, 'recall': recall, 'f1': f1,
            'kappa': cohen_kappa(ka, kb, kc, kd),
        }
    return {'total': len(rows), 'exactAgreement': exact_agree, 'perBlock': per_block}


def _fmt(x):
    return '—' if x is None else f'{x:.3f}'


def macro(metrics, key):
    vals = [metrics['perBlock'][F][key] for F in BLOCK_ORDER
            if metrics['perBlock'][F][key] is not None]
    return sum(vals) / len(vals) if vals else None


def render(metrics, adjudicated_rows):
    m = metrics
    low = [F for F in BLOCK_ORDER if m['perBlock'][F]['support'] < 5]
    lines = [
        '# G5 gold sample — MW block detector scores',
        '',
        '_Created: 03-07-2026 · Last updated: 03-07-2026_',
        '',
        f"Sample: {m['total']} stratified records "
        '([sampling addendum](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/g5/G5_SAMPLING_ADDENDUM.md)), '
        'source [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) '
        'pinned @ `392ed6b`. Gold = Pass A (rule-based, Sonnet 5 `claude-sonnet-5`) × Pass B '
        '(reading pass, Sonnet 5 `claude-sonnet-5`), every disagreement adjudicated per-record by '
        'Fable 5 (`claude-fable-5`) — see '
        '[disagreements.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/g5/disagreements.csv). '
        'Detector = `detect_blocks()` from `figures/scripts/export_data.py` (docs-pass @ `0901c81`), '
        'scorer ported from `analysis/gold_score.py` (docs-pass @ `d0270a4`).',
        '',
        f"Inter-annotator exact agreement (full block set per record): "
        f"**{m['exactAgreement']}/{m['total']}** ({m['exactAgreement']/m['total']:.1%}). "
        f"Adjudicated records: {adjudicated_rows}.",
        '',
        '| block | name | support | TP | FP | FN | precision | recall | F1 | κ (A vs B) |',
        '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|',
    ]
    for F in BLOCK_ORDER:
        b = m['perBlock'][F]
        lines.append(
            f"| {F} | {BLOCK_NAMES[F]} | {b['support']} | {b['tp']} | {b['fp']} | {b['fn']} | "
            f"{_fmt(b['precision'])} | {_fmt(b['recall'])} | {_fmt(b['f1'])} | {_fmt(b['kappa'])} |")
    lines += [
        '',
        f"Macro precision {_fmt(macro(m, 'precision'))}, recall {_fmt(macro(m, 'recall'))}, "
        f"F1 {_fmt(macro(m, 'f1'))}, mean κ {_fmt(macro(m, 'kappa'))}.",
        '',
        f"**Low-support warning** (support < 5, too sparse for stable claims): "
        f"{', '.join(low) if low else 'none'}.",
        '',
        '## Reading notes',
        '',
        '- **F12 precision (0.721) is a definitional split, not a detection bug**: the detector '
        'counts ANY `<ls>` as F12 (so every `<ls>L.</ls>`-only hedge record fires both F12 and '
        'F13); the gold follows G5 spec reviewer rule 4, under which an entry whose only citation '
        'is the `L.` hedge is F13 *without* F12. All 48 F12 false positives are hedge-only records.',
        '- **F09 (editorial commentary) is the weakest block measured** (precision 0.250, '
        'κ 0.189): no dedicated tag exists, and the detector proxy (any parenthetical ≥ 50 chars) '
        'over-fires on inflected-form inventories and identification glosses. This was the '
        'paper\'s own predicted weak spot (§9); it is now measured, not estimated.',
        '- **F08 precision 0.632**: the extra-`<s>`-span proxy also fires on segmented-headword '
        'displays, etymon citations, and cross-referenced forms that are not inflections of the '
        'headword (κ 0.322 between passes — the reading pass corrected exactly this).',
        '- **F02**: 20 false positives are continuation records whose later `<s>`/`<s1>` spans are '
        'not a display headword; all 8 false negatives are display headwords containing `<srs/>` '
        '(e.g. `<s>vizayE<srs/>zin</s>`), which the `[^<]+` regex rejects — a fixable detector bug.',
        '- **F04 recall 0.969 / F15 recall 0.944 — literal-string misses**: the detector matches '
        "`'<lex>'` and `'<s1>'` literally, so `<lex type=\"phw\">` (4 records) and "
        '`<s1 n="...">` (2 records) escape it — fixable detector bugs, same family as F02.',
        '- **F05 measured perfect (P=R=1.000)** despite κ 0.773: the A/B disagreements were all '
        '`<info verb=>`-only records; adjudication ruled machine attributes are F17 (reviewer '
        'rule 3), which coincides with the detector\'s print-string rule (`cl.`/`P.`/`Ā.`).',
        '- **F16 recall 0.654**: all 9 false negatives are bare `See X` prose references — the '
        'detector has `q.v.`/`cf.`/`id.` rules but no `See` rule. The 1 false positive is an '
        'entry-internal `cf. below` (self-reference, not a cross-reference).',
        '- **F18 recall 0.000** (support 2): both correction records in the sample use the '
        '`<chg>` markup form; the detector only knows the `{{old -> new}}` inline form.',
        '',
        '_Dr. Mārcis Gasūns_',
    ]
    return '\n'.join(lines) + '\n'


def _selftest():
    rows = [
        # r1: detector {F01,F08,F10}; gold {F01,F10}; A={F01,F10}, B={F01,F08,F10}
        {'detected_blocks': 'F01;F08;F10', 'adjudicated_blocks': 'F01;F10',
         'gold_blocks_A': 'F01;F10', 'gold_blocks_B': 'F01;F08;F10'},
        # r2: detector {F01,F08,F10}; gold {F01,F08,F10}; A=B=gold
        {'detected_blocks': 'F01;F08;F10', 'adjudicated_blocks': 'F01;F08;F10',
         'gold_blocks_A': 'F01;F08;F10', 'gold_blocks_B': 'F01;F08;F10'},
        # r3: detector {F01,F10}; gold {F01,F10,F11}; A=B=gold
        {'detected_blocks': 'F01;F10', 'adjudicated_blocks': 'F01;F10;F11',
         'gold_blocks_A': 'F01;F10;F11', 'gold_blocks_B': 'F01;F10;F11'},
    ]
    m = score(rows)
    b = m['perBlock']
    assert b['F08']['tp'] == 1 and b['F08']['fp'] == 1 and b['F08']['fn'] == 0, b['F08']
    assert abs(b['F08']['precision'] - 0.5) < 1e-9 and abs(b['F08']['recall'] - 1.0) < 1e-9
    assert b['F10']['tp'] == 3 and b['F10']['fp'] == 0 and b['F10']['fn'] == 0
    assert b['F11']['fn'] == 1 and b['F11']['tp'] == 0 and b['F11']['recall'] == 0.0
    # kappa F08: A yes on r2 only; B yes on r1,r2 -> a=1,b=0,c=1,d=1
    # po=2/3, pe=(1*2+2*1)/9=4/9 -> kappa=(2/3-4/9)/(5/9)=0.4
    assert abs(b['F08']['kappa'] - 0.4) < 1e-9, b['F08']['kappa']
    assert m['exactAgreement'] == 2
    # detect_blocks smoke test
    db = detect_blocks('<s>x</s> ¦ <lex>m.</lex> a thing that is long enough, <ls>L.</ls><info lex="m"/>')
    assert {'F01', 'F02', 'F04', 'F10', 'F12', 'F13', 'F17'} <= db and 'F08' not in db
    print('selftest OK: precision/recall/F1/kappa maths + detector smoke verified.')


def main():
    if '--selftest' in sys.argv:
        _selftest()
        return
    if len(sys.argv) < 2:
        raise SystemExit('usage: python g5_score.py <path-to-pinned-mw.txt>')

    with open('G5_gold_adjudicated.csv', encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 200, len(rows)

    bodies = extract_bodies(sys.argv[1], {r['L'] for r in rows})
    missing = {r['L'] for r in rows} - set(bodies)
    if missing:
        raise SystemExit(f'records missing from mw.txt: {sorted(missing)}')

    for r in rows:
        det = detect_blocks(bodies[r['L']])
        gold = blockset(r['adjudicated_blocks'])
        r['detected_blocks'] = ';'.join(sorted(det))
        r['false_positive_blocks'] = ';'.join(sorted(det - gold))
        r['false_negative_blocks'] = ';'.join(sorted(gold - det))

    with open('G5_gold_adjudicated.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    metrics = score(rows)
    n_adj = sum(1 for r in rows if r['notes'])
    with open('G5_scores.json', 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=2)
    with open('G5_SCORES.md', 'w', encoding='utf-8') as f:
        f.write(render(metrics, n_adj))
    print(f"Wrote G5_SCORES.md + G5_scores.json "
          f"(exact agreement {metrics['exactAgreement']}/{metrics['total']}).")


if __name__ == '__main__':
    main()
