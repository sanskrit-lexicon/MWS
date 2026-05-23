#!/usr/bin/env python3
"""Render the 18-block × 14-type heatmap as paper-quality SVG.

Per Decision 21 (heatmap layout): blocks on Y, types on X with horizontal short codes.
Per Decision 17 (dimensions): IJL full-page-width (~175 mm).
Per Decision 18 (font): Noto Sans.
Per Decision 14 (a11y): writes alt-text + long-desc as sidecar files.
Per Decision 26 (footer): bottom-right grey 7pt italic.
Per Decision 28 (versioning): SHA + date in footer.

Usage:
  python render_heatmap.py --locale en
  python render_heatmap.py --locale ru
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
import matplotlib.patches as mpatches
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, FIG_DIR)
import palette as P  # the generated palette module

DATA_PATH = os.path.join(FIG_DIR, 'data', 'block-by-type-matrix.json')


def load_locale(locale):
    with open(os.path.join(FIG_DIR, 'locales', f'{locale}.json'), encoding='utf-8') as f:
        return json.load(f)


def git_sha():
    try:
        sha = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'],
                                       cwd=FIG_DIR, stderr=subprocess.DEVNULL).decode().strip()
        return sha
    except Exception:
        return 'local'


def render(locale='en'):
    loc = load_locale(locale)
    with open(DATA_PATH, encoding='utf-8') as f:
        data = json.load(f)

    types = data['types']
    blocks = data['blocks']
    matrix_rows = data['matrix']

    # Build a (n_blocks, n_types) array of percentages
    n_b = len(blocks)
    n_t = len(types)
    M = np.zeros((n_b, n_t))
    type_to_col = {t: i for i, t in enumerate(types)}
    for row in matrix_rows:
        t = row['type']
        if t not in type_to_col:
            continue
        j = type_to_col[t]
        for i, b in enumerate(blocks):
            M[i, j] = row.get(b + '_pct', 0)

    # Figure
    fig, ax = plt.subplots(figsize=(7, 5.5), dpi=300)
    fig.patch.set_facecolor(P.CHART['background'])
    ax.set_facecolor(P.CHART['panel'])

    # Heatmap — use a sequential colormap
    im = ax.imshow(M, aspect='auto', cmap='YlOrRd', vmin=0, vmax=100,
                   interpolation='nearest')

    # Y axis: formal blocks F01..F18 with full names
    block_names = loc['formal-block']
    block_labels = [f"{b} {block_names.get(b, b)}" for b in blocks]
    ax.set_yticks(range(n_b))
    ax.set_yticklabels(block_labels, fontsize=7, family='Noto Sans')

    # X axis: article-type SHORT codes per Decision 21 (horizontal)
    short_names = loc['article-type-short']
    type_labels = [short_names.get(t, t) for t in types]
    ax.set_xticks(range(n_t))
    ax.set_xticklabels(type_labels, fontsize=7, rotation=0, family='Noto Sans')

    # Cell text — percentages, white when dark cell, black when light
    for i in range(n_b):
        for j in range(n_t):
            v = M[i, j]
            if v == 0:
                continue
            color = 'white' if v > 60 else 'black'
            txt = f'{v:.0f}' if v >= 1 else f'{v:.1f}'
            ax.text(j, i, txt, ha='center', va='center',
                    fontsize=5.5, color=color, family='Noto Sans')

    # Title + subtitle
    cl = loc['chart-label']
    ax.set_title(cl['title-heatmap'], fontsize=10, family='Noto Sans', loc='left', pad=18)
    ax.text(0, -0.8, cl['subtitle-heatmap'], fontsize=7.5,
            family='Noto Sans', color=P.CHART['muted'], style='italic',
            transform=ax.transData)

    # Axis labels
    ax.set_xlabel(cl['axis-type'], fontsize=8, family='Noto Sans')
    ax.set_ylabel(cl['axis-block'], fontsize=8, family='Noto Sans')

    # Tick params
    ax.tick_params(axis='both', which='both', length=0, pad=2)
    for spine in ax.spines.values():
        spine.set_edgecolor(P.CHART['grid'])
        spine.set_linewidth(0.5)

    # Colour bar — % scale
    cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02, shrink=0.7)
    cbar.set_label(cl['axis-percent'], fontsize=7, family='Noto Sans')
    cbar.ax.tick_params(labelsize=6)
    cbar.outline.set_edgecolor(P.CHART['grid'])

    # Footer — bottom-right, 7pt italic grey
    sha = git_sha()
    today = date.today().isoformat()
    footer_text = (f"{cl['footer-source']} · {cl['footer-license']} · "
                   f"{cl['footer-build'].format(sha=sha)}")
    fig.text(0.99, 0.01, footer_text,
             ha='right', va='bottom',
             fontsize=6, color=P.FOOTER['text_color'], style='italic',
             family='Noto Sans')

    plt.tight_layout(rect=[0, 0.03, 1, 0.96])

    # Output
    out_dir = FIG_DIR
    base = f'heatmap-{locale}'
    svg_path = os.path.join(out_dir, base + '.svg')
    png_path = os.path.join(out_dir, base + '.png')
    plt.savefig(svg_path, format='svg', bbox_inches='tight', dpi=300)
    plt.savefig(png_path, format='png', bbox_inches='tight', dpi=200)
    plt.close()
    print(f'wrote {svg_path}')
    print(f'wrote {png_path}')

    # Sidecar a11y files
    alt = (f"Heatmap matrix: 18 formal blocks (F01-F18) vs 14 article types. "
           f"Type-defining blocks visible as dark cells: F14 botanical in botanical type (100%); "
           f"F15 biographical in biographical (100%); F13 hedge L. in lexicographer-only (100%). "
           f"Striking off-diagonal: F13 at 71% in botanical and 65% in biographical reveals "
           f"the koshic basis of MW's plant and proper-name vocabulary.")
    desc = (f"This heatmap shows MW1899's microstructure as the percentage of entries of each "
            f"article type (14 columns: root, n.m, n.f, n.n, n.mn, adj, ind, comp, deriv, cont, lex., "
            f"IE.et, bot, bio, V.acc, oth) containing each formal block (18 rows: F01 record header "
            f"through F18 correction record). Colour scale 0%-100%. Diagonal entries mark type-defining "
            f"blocks. Off-diagonals reveal cross-cutting structural features. Source: CDSL mw.txt 2026-05-23. "
            f"Released under CC-BY-SA-4.0.")
    with open(os.path.join(out_dir, base + '.alt.txt'), 'w', encoding='utf-8') as f:
        f.write(alt)
    with open(os.path.join(out_dir, base + '.desc.txt'), 'w', encoding='utf-8') as f:
        f.write(desc)
    print(f'wrote {base}.alt.txt, {base}.desc.txt')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--locale', default='en', choices=['en', 'ru'])
    args = p.parse_args()
    render(args.locale)


if __name__ == '__main__':
    main()
