#!/usr/bin/env python3
"""Score the MW block detector against the gold-standard sample.

Reads GOLD_SAMPLE.json (filled in by two annotators) and reports, per formal
block: detector precision / recall / F1 against the adjudicated gold, plus
Cohen's kappa for inter-annotator agreement. Adjudicated gold = the block calls
on which both annotators agree (disagreements are reported and excluded from
P/R until a human adjudicates).

Ground truth per annotator per entry = (machine.blocks - falsePositives) + falseNegatives.

Usage:
  python gold_score.py            # score GOLD_SAMPLE.json -> GOLD_STANDARD_SCORES.md
  python gold_score.py --selftest # verify the metric maths on a synthetic packet
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
BLOCK_ORDER = [f'F{i:02d}' for i in range(1, 19)]


def truth_set(item, key):
    ann = item['annotations'][key]
    if not ann.get('annotator'):
        return None
    machine = set(item['machine']['blocks'])
    return (machine - set(ann.get('falsePositives', []))) | set(ann.get('falseNegatives', []))


def cohen_kappa(a, b, c, d):
    """a=both present, b=only A, c=only B, d=both absent."""
    n = a + b + c + d
    if n == 0:
        return None
    po = (a + d) / n
    pe = ((a + b) * (a + c) + (c + d) * (b + d)) / (n * n)
    if pe == 1.0:
        return 1.0
    return (po - pe) / (1 - pe)


def score(packet):
    items = packet['items']
    annotated = [it for it in items if it['annotations']['A'].get('annotator') or it['annotations']['B'].get('annotator')]
    both = [it for it in items if it['annotations']['A'].get('annotator') and it['annotations']['B'].get('annotator')]

    per_block = {}
    for F in BLOCK_ORDER:
        tp = fp = fn = disagree = 0
        ka = kb = kc = kd = 0  # kappa confusion over `both`-annotated items
        for it in annotated:
            ta, tb = truth_set(it, 'A'), truth_set(it, 'B')
            machine_pres = F in it['machine']['blocks']
            if ta is not None and tb is not None:
                ap, bp = F in ta, F in tb
                ka += ap and bp; kb += ap and not bp; kc += (not ap) and bp; kd += (not ap) and (not bp)
                if ap != bp:
                    disagree += 1
                    continue
                truth_pres = ap
            else:
                truth_pres = F in (ta if ta is not None else tb)
            if machine_pres and truth_pres:
                tp += 1
            elif machine_pres and not truth_pres:
                fp += 1
            elif (not machine_pres) and truth_pres:
                fn += 1
        precision = tp / (tp + fp) if (tp + fp) else None
        recall = tp / (tp + fn) if (tp + fn) else None
        f1 = (2 * precision * recall / (precision + recall)) if (precision and recall) else (0.0 if (precision is not None and recall is not None) else None)
        per_block[F] = {
            'tp': tp, 'fp': fp, 'fn': fn, 'disagree': disagree,
            'precision': precision, 'recall': recall, 'f1': f1,
            'kappa': cohen_kappa(ka, kb, kc, kd) if both else None,
        }
    return {
        'annotatedCount': len(annotated),
        'bothCount': len(both),
        'total': len(items),
        'perBlock': per_block,
    }


def _fmt(x):
    return '—' if x is None else f'{x:.3f}'


def render(packet, metrics):
    names = packet.get('blockNames', {})
    lines = [
        '# MW block detector — gold-standard scores',
        '',
        f"Sample: {metrics['total']} stratified entries (seed {packet.get('seed')}). "
        f"Annotated: {metrics['annotatedCount']} (both annotators: {metrics['bothCount']}).",
        '',
        'Precision/recall are the detector against the adjudicated gold (blocks both '
        'annotators agree on); `disagree` counts block calls where A and B differ '
        '(excluded from P/R pending adjudication). `kappa` is Cohen\'s κ for '
        'inter-annotator agreement on that block.',
        '',
        '| block | name | TP | FP | FN | disagree | precision | recall | F1 | κ |',
        '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|',
    ]
    for F in BLOCK_ORDER:
        b = metrics['perBlock'][F]
        lines.append(
            f"| {F} | {names.get(F, '')} | {b['tp']} | {b['fp']} | {b['fn']} | {b['disagree']} | "
            f"{_fmt(b['precision'])} | {_fmt(b['recall'])} | {_fmt(b['f1'])} | {_fmt(b['kappa'])} |"
        )
    if metrics['annotatedCount'] == 0:
        lines += ['', '_No annotations yet: fill `annotations.A` / `annotations.B` in '
                  '`GOLD_SAMPLE.json` and re-run. The table above is the empty harness._']
    else:
        # macro averages over blocks that have a defined metric
        def macro(metric):
            vals = [metrics['perBlock'][F][metric] for F in BLOCK_ORDER if metrics['perBlock'][F][metric] is not None]
            return sum(vals) / len(vals) if vals else None
        lines += ['', f"Macro precision {_fmt(macro('precision'))}, recall {_fmt(macro('recall'))}, "
                  f"F1 {_fmt(macro('f1'))}, mean κ {_fmt(macro('kappa'))}.",
                  '', 'The F08, F09 (documented over-counts) and F11 (under-count) rows are the '
                  'ones PAPER.md §9 / SPOTCHECK predicted; this measures them rather than estimating.']
    return '\n'.join(lines) + '\n'


def _selftest():
    # 2 items, 2 annotators. machine = {F08, F10}. Construct known FP/FN.
    def item(lnum, machine, a_fp, a_fn, b_fp, b_fn):
        return {
            'reviewId': f'gold:mw:L{lnum}', 'lnum': lnum, 'machine': {'blocks': machine, 'types': []},
            'annotations': {
                'A': {'annotator': 'x', 'falsePositives': a_fp, 'falseNegatives': a_fn, 'note': ''},
                'B': {'annotator': 'y', 'falsePositives': b_fp, 'falseNegatives': b_fn, 'note': ''},
            },
        }
    packet = {'items': [
        # item1: both agree F08 is a false positive; both agree F11 was missed (FN)
        item('1', ['F08', 'F10'], ['F08'], ['F11'], ['F08'], ['F11']),
        # item2: both agree machine correct (F08, F10 present, nothing else)
        item('2', ['F08', 'F10'], [], [], [], []),
    ]}
    m = score(packet)['perBlock']
    # F08: machine present in both; truth: item1 absent (FP), item2 present (TP) -> tp=1, fp=1
    assert m['F08']['tp'] == 1 and m['F08']['fp'] == 1 and m['F08']['fn'] == 0, m['F08']
    assert abs(m['F08']['precision'] - 0.5) < 1e-9 and abs(m['F08']['recall'] - 1.0) < 1e-9
    # F10: machine present both, truth present both -> tp=2
    assert m['F10']['tp'] == 2 and m['F10']['fp'] == 0 and m['F10']['fn'] == 0
    # F11: machine absent both, truth present in item1 (FN) -> fn=1, recall 0
    assert m['F11']['fn'] == 1 and m['F11']['tp'] == 0, m['F11']
    assert m['F11']['recall'] == 0.0
    # kappa F08: both annotators agree on both items (present item2, absent item1) -> perfect
    assert m['F08']['kappa'] == 1.0, m['F08']['kappa']
    print('selftest OK: precision/recall/F1/kappa maths verified.')


def main():
    if '--selftest' in sys.argv:
        _selftest()
        return
    src = os.path.join(HERE, 'GOLD_SAMPLE.json')
    if not os.path.exists(src):
        raise SystemExit('GOLD_SAMPLE.json not found; run gold_sample.py first.')
    with open(src, encoding='utf-8') as f:
        packet = json.load(f)
    metrics = score(packet)
    out = os.path.join(HERE, 'GOLD_STANDARD_SCORES.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(render(packet, metrics))
    print(f"Wrote {os.path.relpath(out, HERE)} "
          f"({metrics['annotatedCount']}/{metrics['total']} annotated).")


if __name__ == '__main__':
    main()
