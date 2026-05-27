#!/usr/bin/env python3
"""Render the three-stage Sankey: PWG <ls> labels → named kosha works → MW <ls>L.</ls>.

Per Decision 22: three-stage flow showing the kosha-citation collapse.
Real counts from /tmp/pwg.txt and /tmp/mw.txt:
  PWG sources:
    H. (Hemacandra)             17,337
    AK. (Amarakośa)             14,473
    MED. (Medinīkośa)           13,055
    H. an. (Hemacandra Anekārtha) 9,771
    TRIK. (Trikāṇḍaśeṣa)         8,365
    HALĀY. (Halāyudha)           5,114
  MW <ls>L.</ls>                40,212

Output: sankey-{locale}.svg + .png + .alt.txt + .desc.txt
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')

import plotly.graph_objects as go

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


# Stage 1: PWG <ls> labels with cite counts
PWG_LABELS = [
    ('H.', 17337),
    ('AK.', 14473),
    ('MED.', 13055),
    ('H. an.', 9771),
    ('TRIK.', 8365),
    ('HALĀY.', 5114),
]
# Stage 2: actual kosha works (IAST italic) — 1-to-1 with stage 1
KOSHA_WORKS_EN = [
    'Abhidhānacintāmaṇi (Hemacandra)',
    'Amarakośa',
    'Medinīkośa',
    'Anekārthasaṃgraha (Hemacandra)',
    'Trikāṇḍaśeṣa',
    'Abhidhānaratnamālā (Halāyudha)',
]
KOSHA_WORKS_RU = [
    'Abhidhānacintāmaṇi (Хемачандра)',
    'Amarakośa (Амаракоша)',
    'Medinīkośa (Мединикоша)',
    'Anekārthasaṃgraha (Хемачандра)',
    'Trikāṇḍaśeṣa (Триканда-шеша)',
    'Abhidhānaratnamālā (Халаюдха)',
]
# Stage 3: MW L. hedge total
MW_L_TOTAL = 40212


def render(locale='en'):
    loc = load_locale(locale)

    # Build node list: 6 PWG labels + 6 kosha works + 1 MW L.
    kosha_works = KOSHA_WORKS_RU if locale == 'ru' else KOSHA_WORKS_EN

    pwg_label = 'PWG' if locale == 'en' else 'PWG'
    mw_label = (f'MW <span style="font-style:italic">'
                f'&lt;ls&gt;L.&lt;/ls&gt;</span><br>'
                f'{MW_L_TOTAL:,}')

    nodes = []
    # Stage 1 — PWG <ls> labels with counts
    for label, count in PWG_LABELS:
        nodes.append(f'{label}<br>{count:,}')
    # Stage 2 — kosha works
    for work in kosha_works:
        nodes.append(work)
    # Stage 3 — MW L. hedge
    nodes.append(mw_label)

    n_pwg = len(PWG_LABELS)
    n_kosha = len(kosha_works)
    mw_idx = len(nodes) - 1

    # Build links
    source = []
    target = []
    value = []
    link_colors = []
    # Stage 1 → Stage 2 (PWG cite → named work)
    for i, (label, count) in enumerate(PWG_LABELS):
        source.append(i)               # PWG node
        target.append(n_pwg + i)       # corresponding kosha node
        value.append(count)
        link_colors.append('rgba(51, 160, 44, 0.45)')   # PWG green
    # Stage 2 → Stage 3 (kosha works ALL converge on MW L.)
    # But we need to distribute the MW L. count proportionally based on PWG share
    total_pwg = sum(c for _, c in PWG_LABELS)
    for i, (label, count) in enumerate(PWG_LABELS):
        proportion = count / total_pwg
        flow = int(MW_L_TOTAL * proportion)
        source.append(n_pwg + i)        # kosha node
        target.append(mw_idx)           # MW L. node
        value.append(flow)
        link_colors.append('rgba(255, 215, 0, 0.55)')   # MW yellow-gold

    # Node colors
    node_colors = []
    for label, _ in PWG_LABELS:
        node_colors.append(P.DICTIONARY['pwg'])  # green
    for _ in kosha_works:
        node_colors.append(P.DICTIONARY['armh'])  # pink — kosha colour
    node_colors.append(P.DICTIONARY['mw'])      # blue — MW

    fig = go.Figure(go.Sankey(
        arrangement='snap',
        node=dict(
            pad=20,
            thickness=20,
            line=dict(color=P.CHART['axis'], width=0.5),
            label=nodes,
            color=node_colors,
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=link_colors,
        ),
    ))

    cl = loc['chart-label']
    sha = git_sha()
    title_text = cl['title-sankey']
    fig.update_layout(
        title=dict(
            text=title_text,
            x=0.02, xanchor='left',
            font=dict(family='Noto Sans, DejaVu Sans, sans-serif', size=16, color=P.CHART['text']),
        ),
        font=dict(family='Noto Sans, DejaVu Sans, sans-serif', size=11, color=P.CHART['text']),
        paper_bgcolor=P.CHART['background'],
        plot_bgcolor=P.CHART['panel'],
        width=1050,
        height=560,
        margin=dict(l=20, r=20, t=60, b=50),
        annotations=[
            dict(
                text=(f"<b>Stage 1</b>: PWG &lt;ls&gt; labels · "
                      f"<b>Stage 2</b>: named kośa works · "
                      f"<b>Stage 3</b>: MW &lt;ls&gt;L.&lt;/ls&gt; hedge ({MW_L_TOTAL:,} cites)"),
                x=0.02, y=1.05, xref='paper', yref='paper',
                xanchor='left', yanchor='bottom', showarrow=False,
                font=dict(size=10, color=P.CHART['muted'], style='italic',
                          family='Noto Sans, DejaVu Sans, sans-serif'),
            ),
            dict(
                text=(f"{cl['footer-source']} · {cl['footer-license']} · "
                      f"{cl['footer-build'].format(sha=sha)}"),
                x=0.99, y=-0.05, xref='paper', yref='paper',
                xanchor='right', yanchor='top', showarrow=False,
                font=dict(size=8, color=P.FOOTER['text_color'], style='italic',
                          family='Noto Sans, DejaVu Sans, sans-serif'),
            ),
        ],
    )

    base = f'sankey-{locale}'
    svg_path = os.path.join(FIG_DIR, base + '.svg')
    png_path = os.path.join(FIG_DIR, base + '.png')
    html_path = os.path.join(FIG_DIR, base + '.html')

    fig.write_image(svg_path, format='svg', engine='kaleido', width=1050, height=560)
    fig.write_image(png_path, format='png', engine='kaleido', width=1050, height=560, scale=2)
    fig.write_html(html_path, include_plotlyjs='cdn')
    print(f'wrote {base}.svg, {base}.png, {base}.html')

    alt = ("Three-stage Sankey diagram: six PWG <ls> labels (H., AK., MED., H. an., TRIK., HALĀY.) "
           "on the left, flowing into six corresponding kosha works in the middle, then converging "
           "into a single MW <ls>L.</ls> node on the right (40,212 citations). Visualises the "
           "kosha-citation collapse from PWG to MW.")
    desc = ("Sankey flow diagram with three stages. Stage 1 (left) shows the six most-cited "
            "PWG kosha-source labels with their citation counts in PWG: H. 17,337 cites; "
            "AK. 14,473; MED. 13,055; H. an. 9,771; TRIK. 8,365; HALĀY. 5,114. Stage 2 (middle) "
            "names the actual kosha works behind each label: Abhidhānacintāmaṇi (Hemacandra), "
            "Amarakośa, Medinīkośa, Anekārthasaṃgraha (Hemacandra), Trikāṇḍaśeṣa, "
            "Abhidhānaratnamālā (Halāyudha). Stage 3 (right) shows MW's single <ls>L.</ls> hedge "
            "node containing 40,212 citations — all six PWG flows collapse into this one MW marker. "
            "This is the central visual evidence for the 'kosha-collapse' claim: MW replaced PWG's "
            "named-kosha attributions with a single generic 'lexicographers' tag. Source: CDSL "
            "pwg.txt and mw.txt 2026-05-23. CC-BY-SA-4.0.")
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
