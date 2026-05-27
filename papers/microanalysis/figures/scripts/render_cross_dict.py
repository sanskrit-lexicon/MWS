#!/usr/bin/env python3
"""Render the cross-dictionary comparison figures from data/cross-dict.json.

Two figures (EN; RU deferred until the locale is reviewed, per DOUBTS D11):
  cross-dict-density-en.*  — source-citation density (<ls> per record), 9 dicts.
  cross-dict-blocks-en.*   — common-block population heatmap, 9 blocks x 9 dicts.

Conventions match render_heatmap.py: Noto Sans, palette module, footer with
SHA + date (Decisions 14/18/26/28), plus .alt.txt / .desc.txt sidecars.
"""
import json
import os
import subprocess
import sys
from datetime import date

sys.stdout.reconfigure(encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, FIG_DIR)
import palette as P  # noqa: E402

DATA = os.path.join(FIG_DIR, 'data', 'cross-dict.json')
# code -> palette colour (palette.DICTIONARY lacks ben/cae; add them)
DICT_COLOR = {
    'MW': P.DICTIONARY['mw'], 'PWG': P.DICTIONARY['pwg'], 'PWK': P.DICTIONARY['pw'],
    'AP': P.DICTIONARY['ap'], 'WIL': P.DICTIONARY['wil'], 'BEN': '#17becf',
    'CAE': '#8c564b', 'SKD': P.DICTIONARY['skd'], 'VCP': P.DICTIONARY['vcp'],
}
BLOCK_LABEL = {'head': 'head', 'body': 'body (¦)', 'gram': 'gram (<lex>)',
               'cite': 'cite (<ls>)', 'hom': 'homograph', 'etym': 'etymology',
               'xref': 'cross-ref', 'hedge': 'L. hedge', 'info': 'info (digit.)'}


def git_sha():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'],
                                       cwd=FIG_DIR, stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return 'local'


def footer(fig):
    fig.text(0.99, 0.01,
             f"Source: CDSL 2026-05-24 · CC-BY-SA-4.0 · build {git_sha()}",
             ha='right', va='bottom', fontsize=6,
             color=P.FOOTER['text_color'], style='italic', family='Noto Sans')


def sidecar(base, alt, desc):
    with open(os.path.join(FIG_DIR, base + '.alt.txt'), 'w', encoding='utf-8') as f:
        f.write(alt)
    with open(os.path.join(FIG_DIR, base + '.desc.txt'), 'w', encoding='utf-8') as f:
        f.write(desc)


def save(fig, base):
    svg = os.path.join(FIG_DIR, base + '.svg')
    png = os.path.join(FIG_DIR, base + '.png')
    fig.savefig(svg, format='svg', bbox_inches='tight')
    fig.savefig(png, format='png', bbox_inches='tight', dpi=200)
    plt.close(fig)
    print(f'wrote {base}.svg / .png')


def render_density(data):
    dicts = sorted(data['dicts'], key=lambda d: d['ls_per_record'], reverse=True)
    codes = [d['code'] for d in dicts]
    vals = [d['ls_per_record'] for d in dicts]
    colors = [DICT_COLOR[c] for c in codes]

    fig, ax = plt.subplots(figsize=(7, 4), dpi=300)
    fig.patch.set_facecolor(P.CHART['background'])
    ax.set_facecolor(P.CHART['panel'])
    bars = ax.bar(range(len(codes)), vals, color=colors, edgecolor=P.CHART['grid'], linewidth=0.5)
    for i, d in enumerate(dicts):
        ax.text(i, d['ls_per_record'] + 0.08, f"{d['ls_per_record']:.2f}",
                ha='center', va='bottom', fontsize=6.5, family='Noto Sans', color=P.CHART['text'])
        if d['volumes'] > 1:
            ax.text(i, d['ls_per_record'] + 0.30, f"{d['volumes']} vol.",
                    ha='center', va='bottom', fontsize=6, family='Noto Sans',
                    color=P.CHART['accent'], style='italic')
    ax.set_xticks(range(len(codes)))
    ax.set_xticklabels(codes, fontsize=8, family='Noto Sans')
    ax.set_ylabel('<ls> source citations per record', fontsize=8, family='Noto Sans')
    ax.set_title('Source-citation density across nine CDSL dictionaries',
                 fontsize=10, family='Noto Sans', loc='left', pad=10)
    ax.tick_params(axis='both', length=0)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_edgecolor(P.CHART['grid'])
    ax.margins(y=0.18)
    footer(fig)
    fig.tight_layout(rect=[0, 0.03, 1, 1])
    save(fig, 'cross-dict-density-en')
    sidecar('cross-dict-density-en',
            "Bar chart of source-citation density (<ls> tags per record) for nine CDSL dictionaries. "
            "PWG (7 volumes) is densest at 4.63; Benfey 2.84; MW 1.09; AP 0.69; PWK 0.51; "
            "WIL 0.01; Cappeller, SKD and VCP ~0. The multi-volume PWG is roughly 4x denser per "
            "entry than the single-volume MW, illustrating block economy as a single-volume constraint.",
            "Source-citation density per record across nine CDSL dictionaries, sorted descending. "
            "Multi-volume PWG leads; single-volume bilingual dicts (MW, AP, PWK, Benfey) are far lower; "
            "WIL/Cappeller carry almost no <ls> apparatus and the Sanskrit-Sanskrit lexica SKD/VCP none. "
            "Source: CDSL 2026-05-24, CC-BY-SA-4.0.")


def render_blocks(data):
    blocks = data['blocks']
    dicts = data['dicts']
    codes = [d['code'] for d in dicts]
    M = np.array([[d['blocks_pct'][b] for d in dicts] for b in blocks])

    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    fig.patch.set_facecolor(P.CHART['background'])
    ax.set_facecolor(P.CHART['panel'])
    im = ax.imshow(M, aspect='auto', cmap='YlOrRd', vmin=0, vmax=100, interpolation='nearest')
    ax.set_xticks(range(len(codes)))
    ax.set_xticklabels(codes, fontsize=8, family='Noto Sans')
    ax.set_yticks(range(len(blocks)))
    ax.set_yticklabels([BLOCK_LABEL[b] for b in blocks], fontsize=7.5, family='Noto Sans')
    for i in range(len(blocks)):
        for j in range(len(codes)):
            v = M[i, j]
            if v < 0.5:
                continue
            ax.text(j, i, f'{v:.0f}', ha='center', va='center', fontsize=6,
                    color='white' if v > 60 else 'black', family='Noto Sans')
    ax.set_title('Common-block population across nine CDSL dictionaries',
                 fontsize=10, family='Noto Sans', loc='left', pad=10)
    ax.set_xlabel('Dictionary', fontsize=8, family='Noto Sans')
    ax.tick_params(axis='both', length=0, pad=2)
    for s in ax.spines.values():
        s.set_edgecolor(P.CHART['grid'])
        s.set_linewidth(0.5)
    cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02, shrink=0.7)
    cbar.set_label('% of entries', fontsize=7, family='Noto Sans')
    cbar.ax.tick_params(labelsize=6)
    footer(fig)
    fig.tight_layout(rect=[0, 0.03, 1, 1])
    save(fig, 'cross-dict-blocks-en')
    sidecar('cross-dict-blocks-en',
            "Heatmap of nine format-robust common blocks (rows) by nine CDSL dictionaries (columns), "
            "as percentage of entries. The L.-hedge row is lit only for MW (14%); the info row only "
            "for MW (96%); citation is near-universal in PWG (94%) but absent in SKD/VCP/CAE. Every "
            "dict shares the head and body blocks; structural richness drops sharply in the "
            "Sanskrit-Sanskrit lexica (SKD, VCP).",
            "Common-block population matrix: rows are head, body, grammar, citation, homograph, "
            "etymology, cross-reference, L.-hedge, and info (digitisation); columns are MW, PWG, PWK, "
            "AP, WIL, Benfey, Cappeller, SKD, VCP. Colour 0-100% of entries. The L.-hedge and info "
            "blocks are MW-only; SKD/VCP show only head+body, marking their different genre. "
            "Source: CDSL 2026-05-24, CC-BY-SA-4.0.")


def main():
    with open(DATA, encoding='utf-8') as f:
        data = json.load(f)
    render_density(data)
    render_blocks(data)


if __name__ == '__main__':
    main()
