#!/usr/bin/env python3
"""Deterministic G5 stratified sampler for MW (mw.txt).

Pinned algorithm (must be byte-identical for Pass A and Pass B to draw the
same 200 records independently -- see G5_GOLD_SAMPLE_SPEC.md sampling
addendum). Do not change ordering, seed, or stratum predicate order after
this is merged to master.
"""
import re
import sys
import random
import csv

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

SEED = 20260702  # pinned: date this addendum was ratified (DDMMYYYY->YYYYMMDD ISO form used as int)
SRC_COMMIT = "392ed6bdda9c624c2a18e5730a61719fdacf645c"  # csl-orig, v02/mw/mw.txt, 2026-06-27
MW_PATH = "../csl-orig/v02/mw/mw.txt"

STRATA = [
    # (name, target_n, predicate)
]

def parse_records(path):
    records = []
    with open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')
    cur = []
    for line in lines:
        if line.startswith('<L>'):
            if cur:
                records.append('\n'.join(cur))
            cur = [line]
        elif line.strip() == '<LEND>':
            cur.append(line)
            records.append('\n'.join(cur))
            cur = []
        else:
            if cur:
                cur.append(line)
    if cur:
        records.append('\n'.join(cur))
    return records


def field(text, tag):
    m = re.search(r'<%s>([^<]*)' % tag, text)
    return m.group(1) if m else ''


def get_L(text):
    m = re.search(r'<L>([^<]*)', text)
    return m.group(1) if m else ''


def get_pc(text):
    m = re.search(r'<pc>([^<]*)', text)
    return m.group(1) if m else ''


def get_e(text):
    m = re.search(r'<e>([^\n<]*)', text)
    return m.group(1) if m else ''


def is_continuation(e):
    return bool(re.search(r'[0-9](\.[0-9]+)?[A-Za-z]$', e.strip())) or bool(re.search(r'^[0-9]+[A-Za-z]', e.strip()))


def is_kernel_common(text, e):
    has_lex = '<lex>' in text or '<lex ' in text
    has_s = bool(re.search(r'<s>[^<]', text))
    has_ls = '<ls>' in text
    has_info = '<info' in text
    enrich = any(t in text for t in ['<hom>', '<lang>', '<bot>', '<bio>', '<s1>', '<etym>',
                                       '<chg', 'verb="genuineroot"', 'verb="root"', 'verb="gati"',
                                       'verb="nom"', 'verb="pre"', '<ab>cl.</ab>', 'phwchild=',
                                       'phwparent=', '<div n=', '<pcol>', '√'])
    return has_lex and has_s and has_ls and has_info and not enrich and not is_continuation(e)


def is_root_verbal(text):
    return ('<ab>cl.</ab>' in text or 'verb="genuineroot"' in text or 'verb="root"' in text
            or 'verb="gati"' in text or 'verb="nom"' in text or 'verb="pre"' in text
            or '<ab>P.</ab>' in text or '<ab>Ā.</ab>' in text)


def is_hedge_ls(text):
    return '<ls>L.</ls>' in text


def is_botanical_bio(text):
    return '<bot>' in text or '<bio>' in text or '<s1>' in text


def is_crossref_phw(text):
    return ('<ab>id.</ab>' in text or 'type="phw"' in text or 'phwchild=' in text
            or 'phwparent=' in text or '<pcol>' in text)


def is_correction_edge(text):
    return '<chg' in text or 'n="rev"' in text or '<listinfo n="rev"' in text


def main():
    records = parse_records(MW_PATH)
    print(f"Parsed {len(records)} records from {MW_PATH}", file=sys.stderr)

    parsed = []
    for text in records:
        L = get_L(text)
        if not L:
            continue
        parsed.append({
            'L': L,
            'k1': field(text, 'k1'),
            'pc': get_pc(text),
            'e': get_e(text),
            'text': text,
        })

    assigned = {}  # L -> stratum
    order = []

    def take(name, target, predicate, pool_source):
        rng = random.Random(SEED ^ hash(name) & 0xffffffff)
        candidates = [r for r in pool_source if r['L'] not in assigned and predicate(r)]
        candidates.sort(key=lambda r: r['L'])
        rng.shuffle(candidates)
        picked = candidates[:target]
        for r in picked:
            assigned[r['L']] = name
            order.append((name, r))
        print(f"{name}: {len(picked)}/{target} (pool {len(candidates)})", file=sys.stderr)

    take('kernel_common', 40, lambda r: is_kernel_common(r['text'], r['e']), parsed)
    take('root_verbal', 25, lambda r: is_root_verbal(r['text']), parsed)
    take('continuation', 25, lambda r: is_continuation(r['e']), parsed)
    take('hedge_ls', 25, lambda r: is_hedge_ls(r['text']), parsed)
    take('botanical_bio', 25, lambda r: is_botanical_bio(r['text']), parsed)
    take('crossref_phw', 20, lambda r: is_crossref_phw(r['text']), parsed)
    take('correction_edge', 15, lambda r: is_correction_edge(r['text']), parsed)
    take('random_residual', 25, lambda r: True, parsed)

    print(f"TOTAL: {len(order)}", file=sys.stderr)

    rng = random.Random(SEED)
    rng.shuffle(order)

    rows = []
    for i, (stratum, r) in enumerate(order, start=1):
        excerpt = re.sub(r'\s+', ' ', r['text']).strip()
        if len(excerpt) > 220:
            excerpt = excerpt[:217] + '...'
        rows.append({
            'sample_id': f'G5-{i:03d}',
            'stratum': stratum,
            'L': r['L'],
            'k1': r['k1'],
            'pc': r['pc'],
            'record_excerpt': excerpt,
            'detected_blocks': '',
            'gold_blocks_A': '',
            'gold_blocks_B': '',
            'adjudicated_blocks': '',
            'false_positive_blocks': '',
            'false_negative_blocks': '',
            'notes': '',
        })

    with open('G5_gold_sample_skeleton.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    with open('sample_full_text.tsv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['sample_id', 'L', 'full_text'])
        for i, (stratum, r) in enumerate(order, start=1):
            w.writerow([f'G5-{i:03d}', r['L'], r['text'].replace('\t', ' ').replace('\n', ' | ')])

    print("Wrote G5_gold_sample_skeleton.csv and sample_full_text.tsv", file=sys.stderr)


if __name__ == '__main__':
    main()
