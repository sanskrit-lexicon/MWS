#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_correction_example.py — README before/after panel (H7720), one-off.

Renders docs/assets/correction-example.svg. The two entry strings — the only
text carrying IAST diacritics (u-macron) — are converted to vector paths from
Arial glyph outlines via fontTools, so the panel has no font dependency where
diacritics would drift. All other labels are plain ASCII <text>.

Real record: csl-corrections batch_20240616 case 688 — MW L=165450 (mud),
old "(aor. amumudat)" -> new "(aor. amūmudat)", printed page/column from the
source metaline <pc>822,2. One-off asset: the committed SVG is the deliverable
(re-run needs macOS system Arial via fonttools).

Usage: python3 docs/assets/src/make_correction_example.py
"""
import os
import re
import sys

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(HERE, "docs", "assets", "correction-example.svg")
REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"

INK = "#111827"
MUTED = "#6b7280"
BLUE = "#0f4c81"
BLUE_BG = "#eff6ff"
GRAY_CARD = "#f9fafb"
RULE = "#d1d5db"
ORANGE = "#c2410c"
FONT = "Helvetica, Arial, sans-serif"

NUM = re.compile(r"\d+\.\d+")


def rounded(d):
    return NUM.sub(lambda m: f"{float(m.group(0)):.1f}", d)


def draw_entry_paths(font, s, x, y, size, fill, out):
    """Convert s to glyph-outline paths at baseline (x, y); return char spans."""
    cmap, upm, gs, hmtx = font["cmap"] if "cmap" in font else (None,), font["head"].unitsPerEm, font.getGlyphSet(), font["hmtx"]
    cmap = font.getBestCmap()
    spans = []
    for i, ch in enumerate(s):
        gname = cmap[ord(ch)]
        adv = hmtx[gname][0] * size / upm
        pen = SVGPathPen(gs)
        gs[gname].draw(TransformPen(pen, Transform(size / upm, 0, 0, -size / upm, x, y)))
        d = rounded(pen.getCommands())
        if d.strip():
            out.append(f'    <path d="{d}" fill="{fill}"/>')
        spans.append((i, x, adv))
        x += adv
    return spans


def text_el(s, x, y, size, fill, weight="normal", anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    esc = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'  <text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}"{a}>{esc}</text>'


def main():
    font = TTFont(REGULAR)
    el = []
    el.append(text_el("One real correction, before and after", 12, 26, 15, INK, "bold"))
    el.append(text_el("mud (MW L=165450) - printed page 822, column 2 (source metaline <pc>822,2)", 12, 46, 11, MUTED))

    # Card A: as digitised (entry text as paths)
    el.append(f'  <rect x="12" y="60" width="288" height="72" rx="6" fill="{GRAY_CARD}" stroke="{RULE}" stroke-width="1.5"/>')
    el.append(text_el("AS DIGITISED", 24, 80, 10, MUTED, "bold"))
    spans_a = draw_entry_paths(font, "(aor. amumudat)", 24, 118, 19, INK, el)
    _, cx, adv = spans_a[8]  # the 'u' that should be a u-macron
    el.append(f'  <line x1="{cx + 1:.1f}" y1="124" x2="{cx + adv - 1:.1f}" y2="124" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="3 2"/>')

    # Arrow
    el.append(f'  <line x1="312" y1="96" x2="336" y2="96" stroke="{MUTED}" stroke-width="1.5"/>')
    el.append(f'  <path d="M336 92 L344 96 L336 100 Z" fill="{MUTED}"/>')

    # Card B: corrected (entry text as paths; u-macron included)
    el.append(f'  <rect x="356" y="60" width="292" height="72" rx="6" fill="{BLUE_BG}" stroke="{BLUE}" stroke-width="1.5"/>')
    el.append(text_el("CORRECTED", 368, 80, 10, BLUE, "bold"))
    spans_b = draw_entry_paths(font, "(aor. am\u016Bmudat)", 368, 118, 19, INK, el)
    _, cx, adv = spans_b[8]  # the u-macron
    el.append(f'  <line x1="{cx + 1:.1f}" y1="124" x2="{cx + adv - 1:.1f}" y2="124" stroke="{BLUE}" stroke-width="2"/>')

    # Footer
    el.append(f'  <line x1="12" y1="148" x2="648" y2="148" stroke="{RULE}" stroke-width="1"/>')
    el.append(text_el("Reported via the correction queue (csl-corrections batch_20240616, case 688), applied as a change file to the canonical", 12, 166, 9.5, MUTED))
    el.append(text_el("mw.txt in csl-orig, and checked against the printed page cited above.", 12, 180, 9.5, MUTED))
    el.append(text_el("Entry text drawn as vector paths - no font dependency. Org-wide progress: sanskrit-lexicon/csl-observatory.", 12, 206, 8.5, MUTED))

    body = "\n".join(el)
    svg = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" width="660" height="216" viewBox="0 0 660 216" '
        'role="img" aria-label="One real MW correction: the entry mud, sense text (aor. amumudat) corrected to (aor. amumudat with u-macron)">\n'
        '  <rect width="660" height="216" fill="#ffffff"/>\n'
        f"{body}\n"
        "</svg>\n"
    )
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print(f"wrote {OUT} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
