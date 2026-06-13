#!/usr/bin/env python3
"""Build a 200-entry stratified GOLD-STANDARD validation sample for the MW
block detector (PAPER.md D6 / Limitation 1; upgrades the random 100-record
SPOTCHECK to a stratified, double-annotated, precision/recall-scored sample).

It reuses the SAME detector under test — detect_blocks / classify_type imported
from figures/scripts/export_data.py — so the sample validates the live code, not
a copy. The record regex mirrors export_data.main().

Stratified by PRIMARY article type (round-robin draw) so every type, including
rare ones (root, botanical, biographical), is covered and no common type
(compound) dominates. Deterministic (SEED).

Emits:
  GOLD_SAMPLE.json  — double-keyed annotation packet (2 annotators, A and B);
                      each marks only the detector's false +/- per entry.
  GOLD_SAMPLE.md    — human worksheet grouped by stratum.

Score it later with gold_score.py once annotators fill the packet.

Usage: python gold_sample.py
"""
import json
import os
import re
import sys
import random
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', 'figures', 'scripts')))
from export_data import detect_blocks, classify_type  # the detector under test

SEED = 2026
TARGET = 200
BLOCK_ORDER = [f'F{i:02d}' for i in range(1, 19)]
BLOCK_NAMES = {
    'F01': 'record header', 'F02': 'display headword', 'F03': 'homophone disambiguator',
    'F04': 'grammatical category', 'F05': 'verb inflection class', 'F06': 'etymology root marker',
    'F07': 'IE cognate', 'F08': 'inflection form', 'F09': 'editorial commentary',
    'F10': 'sense gloss', 'F11': 'sense division', 'F12': 'source citation',
    'F13': 'hedge marker (L.)', 'F14': 'botanical name', 'F15': 'biographical content',
    'F16': 'cross-reference', 'F17': 'machine annotation', 'F18': 'correction record',
}
# Mirror of export_data.main()'s record pattern (kept in sync by hand).
RECORD_RE = re.compile(
    r'<L>([0-9.]+)<pc>([^<]*)<k1>([^<\r\n]*?)<k2>([^<\r\n]*?)(?:<h>([^<]*))?<e>([^\r\n]+?)\r?\n(.*?)\r?\n<LEND>',
    re.DOTALL,
)


def find_mw_txt():
    candidates = [
        os.environ.get('MW_TXT'),
        r'C:/Users/user/AppData/Local/Temp/mw.txt',
        os.path.join(HERE, '..', '..', '..', '..', 'csl-orig', 'v02', 'mw', 'mw.txt'),
        os.path.join(HERE, '..', '..', '..', '..', '..', 'csl-orig', 'v02', 'mw', 'mw.txt'),
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return os.path.normpath(c)
    raise SystemExit('mw.txt not found; set MW_TXT or place csl-orig as a sibling repo.')


def main():
    path = find_mw_txt()
    print(f'Loading {path} ...')
    with open(path, encoding='utf-8') as f:
        text = f.read()

    by_type = defaultdict(list)
    n = 0
    for m in RECORD_RE.finditer(text):
        lnum, pc, k1, k2, h, ecode, body = m.groups()
        ecode = ecode.strip()
        types = classify_type(body, k2, ecode)
        blocks = sorted(detect_blocks(body))
        primary = types[0]  # classify_type priority order: root > compound > ... > other
        by_type[primary].append({
            'lnum': lnum, 'k2': k2, 'ecode': ecode, 'stratum': primary,
            'body': body.strip(),
            'machine': {'blocks': blocks, 'types': types},
        })
        n += 1
    print(f'Parsed {n:,} entries across {len(by_type)} primary strata.')

    # Round-robin draw across strata for a balanced, rare-type-covering sample.
    rng = random.Random(SEED)
    strata = sorted(by_type)
    pools = {t: rng.sample(by_type[t], len(by_type[t])) for t in strata}
    idx = {t: 0 for t in strata}
    picked = []
    while len(picked) < TARGET and any(idx[t] < len(pools[t]) for t in strata):
        for t in strata:
            if len(picked) >= TARGET:
                break
            if idx[t] < len(pools[t]):
                picked.append(pools[t][idx[t]])
                idx[t] += 1
    picked.sort(key=lambda e: (e['stratum'], float(e['lnum'])))

    def empty_annotator():
        return {'annotator': '', 'falsePositives': [], 'falseNegatives': [], 'note': ''}

    items = []
    for e in picked:
        items.append({
            'reviewId': f"gold:mw:L{e['lnum']}",
            'lnum': e['lnum'], 'k2': e['k2'], 'ecode': e['ecode'], 'stratum': e['stratum'],
            'body': e['body'],
            'machine': e['machine'],
            'annotations': {'A': empty_annotator(), 'B': empty_annotator()},
        })

    stratum_counts = defaultdict(int)
    for it in items:
        stratum_counts[it['stratum']] += 1

    packet = {
        'schemaVersion': '1.0.0',
        'license': 'CC-BY-SA-4.0',
        'queue': 'mw-block-gold-standard',
        'claim': 'A 200-entry stratified gold-standard sample for human validation of the MW block detector.',
        'evidenceLabel': 'derived',
        'reviewStatus': 'needs-review',
        'seed': SEED,
        'sourcePath': os.path.basename(path),
        'detector': 'papers/microanalysis/figures/scripts/export_data.py:detect_blocks',
        'annotationProtocol': (
            'Two annotators (A, B) independently review each entry against its raw body. '
            'For each, record only the detector errors: falsePositives = detected blocks that '
            'are NOT genuinely present; falseNegatives = blocks genuinely present that the '
            'detector MISSED. Ground truth = (machine.blocks - falsePositives) + falseNegatives. '
            'Set annotator to your id when done. Score with gold_score.py.'
        ),
        'blockNames': BLOCK_NAMES,
        'recordCount': len(items),
        'stratumCounts': dict(sorted(stratum_counts.items())),
        'totalEntries': n,
        'items': items,
    }
    out_json = os.path.join(HERE, 'GOLD_SAMPLE.json')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(packet, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'  wrote {os.path.relpath(out_json, HERE)} ({len(items)} entries)')

    # Human worksheet.
    lines = [
        '# MW block detector — gold-standard worksheet',
        '',
        f'200-entry stratified sample (seed={SEED}). For each entry, mark the detector errors:',
        '`FP:` detected blocks not actually present; `FN:` present blocks the detector missed.',
        'Record decisions in `GOLD_SAMPLE.json` (annotations.A / annotations.B), then run `gold_score.py`.',
        '',
        '| stratum | entries |', '|---|---:|',
    ]
    for t, c in sorted(stratum_counts.items()):
        lines.append(f'| {t} | {c} |')
    lines.append('')
    current = None
    for it in items:
        if it['stratum'] != current:
            current = it['stratum']
            lines.append(f'\n## {current}\n')
        blocks = ' '.join(f"{b}({BLOCK_NAMES[b]})" for b in it['machine']['blocks'])
        lines.append(f"### L{it['lnum']}  k2=`{it['k2']}`  e={it['ecode']}")
        lines.append(f"- detected blocks: {blocks}")
        lines.append(f"- detected types: {' '.join(it['machine']['types'])}")
        lines.append(f"- body: `{it['body']}`")
        lines.append(f"- FP: ___   FN: ___")
        lines.append('')
    out_md = os.path.join(HERE, 'GOLD_SAMPLE.md')
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  wrote {os.path.relpath(out_md, HERE)}')


if __name__ == '__main__':
    main()
