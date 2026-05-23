#!/usr/bin/env python3
"""Render article-type treemap.

286,561 entries by article type as a squarified treemap.
Per Decision 17 (full-page-width), Decision 18 (Noto Sans),
Decision 21 (use article-type colours from palette).
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import squarify

HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, FIG_DIR)
import palette as P


def load_locale(locale):
    with open(os.path.join(FIG_DIR, 'locales', f'{locale}.json'), encoding='utf-8') as f:
        return json.load(f)


def git_sha():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'],
                                        cwd=FIG_DIR, stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return 'local'


def render(locale='en'):
    loc = load_locale(locale)
    with open(os.path.join(FIG_DIR, 'data', 'article-type-counts.json'), encoding='utf-8') as f:
        data = json.load(f)

    types = sorted(data['types'], key=lambda r: -r['count'])
    total = data['total']

    sizes = [t['count'] for t in types]
    type_names = loc['article-type']
    labels = []
    for t in types:
        name = type_names.get(t['type'], t['type'])
        pct = 100 * t['count'] / total
        if pct >= 3.0:
            labels.append(f"{name}\n{t['count']:,}\n({pct:.1f}%)")
        elif pct >= 1.0:
            labels.append(f"{name}\n{t['count']:,}")
        else:
            labels.append('')

    colors = [P.ARTICLE_TYPE.get(t['type'].replace('-', '_'), '#888888') for t in types]

    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    fig.patch.set_facecolor(P.CHART['background'])
    ax.set_facecolor(P.CHART['panel'])

    squarify.plot(sizes=sizes, label=labels, color=colors,
                  text_kwargs={'fontsize': 8, 'color': 'black', 'family': 'Noto Sans'},
                  edgecolor=P.CHART['background'], linewidth=2,
                  ax=ax, alpha=0.92)
    ax.axis('off')

    cl = loc['chart-label']
    fig.suptitle(cl['title-treemap'], fontsize=11, family='Noto Sans', x=0.02, ha='left', y=0.97)

    # Subtitle: each type has its overlapping property — note that
    note = ("Note: types overlap (an entry can be both noun_m AND vedic_accented). "
            "Sizes are membership counts; total is non-additive.")
    fig.text(0.02, 0.93, note, fontsize=7, color=P.CHART['muted'], style='italic',
             family='Noto Sans')

    # Footer
    sha = git_sha()
    footer_text = (f"{cl['footer-source']} · {cl['footer-license']} · "
                   f"{cl['footer-build'].format(sha=sha)}")
    fig.text(0.99, 0.01, footer_text, ha='right', va='bottom',
             fontsize=6, color=P.FOOTER['text_color'], style='italic',
             family='Noto Sans')

    plt.tight_layout(rect=[0, 0.03, 1, 0.92])

    base = f'treemap-{locale}'
    plt.savefig(os.path.join(FIG_DIR, base + '.svg'), format='svg', bbox_inches='tight', dpi=300)
    plt.savefig(os.path.join(FIG_DIR, base + '.png'), format='png', bbox_inches='tight', dpi=200)
    plt.close()
    print(f'wrote {base}.svg, {base}.png')

    alt = (f"Treemap of MW1899: 286,561 entries arranged by article type as proportional rectangles. "
           f"Compound sub-entries dominate at ~44%; derived forms ~25%; vedic-accented ~16%; "
           f"lexicographer-only ~13%; smaller types tail off. Types overlap (an entry can be both "
           f"noun_m and vedic_accented).")
    desc = (f"Squarified treemap visualising the composition of MW1899's 286,561 records by article type. "
            f"Largest tile: compound sub-entries (126,360, 44.1%). Second: derived forms (72,119, 25.2%). "
            f"Vedic-accented (47,598, 16.6%), lexicographer-only (38,414, 13.4%). Smaller tiles include "
            f"masculine nouns (19,204), other types. Note that types are not mutually exclusive — an entry "
            f"can be classified into multiple types; sizes are membership counts, not exclusive partitions. "
            f"Source: CDSL mw.txt 2026-05-23. CC-BY-SA-4.0.")
    with open(os.path.join(FIG_DIR, base + '.alt.txt'), 'w', encoding='utf-8') as f:
        f.write(alt)
    with open(os.path.join(FIG_DIR, base + '.desc.txt'), 'w', encoding='utf-8') as f:
        f.write(desc)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--locale', default='en', choices=['en', 'ru'])
    args = p.parse_args()
    render(args.locale)


if __name__ == '__main__':
    main()
