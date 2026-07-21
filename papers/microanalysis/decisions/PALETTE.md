# Decisions — palette, design tokens, font, license

Covers decisions **1**, **9**, **18**, **19** from the visualisation-planning phase. See [decisions/README.md](README.md) for the full index.

---

## Decision 1 — Shared colour palette via CSS

The [paper](../PAPER.md) + the interactive [csl-atlas](https://github.com/sanskrit-lexicon/csl-atlas) microsite use the same colour palette for the 14 article types. Implementation: **via CSS** (custom properties / design tokens), so a single source-of-truth defines colours that flow through (a) the static SVG figures generated for the paper, (b) the Mermaid diagrams embedded in markdown docs, and (c) the interactive microsite.

The CSS strategy lets us:

- Swap colour themes without re-rendering data (dark mode, print-friendly, colour-blind safe).
- Keep static SVG and interactive HTML visually consistent without manual sync.
- Allow downstream Phase-4 dictionaries to inherit the same palette.

## Decision 9 — JSON-first design tokens

Single source of truth: [`figures/palette-tokens.json`](../figures/palette-tokens.json). A build step generates downstream artifacts:

```
palette-tokens.json   ← THE source of truth
       │
       ├──→  palette.css            (CSS custom properties for HTML/SVG)
       ├──→  mermaid-theme.json     (consumed by Mermaid)
       ├──→  palette.py             (Python module, importable for matplotlib)
       └──→  palette.tex            (LaTeX colour definitions, for paper figures)

```

**Token groups:**

| Group | Keys | Use |
|---|---|---|
| `article-type` | 16 keys (root, noun-m, …, vedic-accented, other) | Heatmap cells; treemap fills; type-comparator |
| `semantic-block` | 9 keys (identity, form, …, meta) | Block-level visualisations |
| `fullness-tier` | 5 keys (T1-vestigial … T5-elaborate) | Fullness histograms |
| `dictionary` | 11 keys (mw, pwg, pw, ap, wil, skd, vcp, armh, abch, acph, acsj) | Per-dict and cross-dict visualisations |
| `chart-element` | background, panel, grid, axis, text, muted, accent, highlight | Universal chart scaffolding |
| `footer` | text-color, font-size, font-style | Per-figure attribution footer |

WCAG-checked, colour-blind-safe flag baked into `_meta`. Build tool: [`scripts/build_palette.py`](../figures/scripts/build_palette.py) — simple, no [Style Dictionary](https://amzn.github.io/style-dictionary/) overkill.

## Decision 18 — Font: Noto Sans

[**Noto Sans**](https://fonts.google.com/noto/specimen/Noto+Sans) for all figure text. Rationale:

- Universal Unicode coverage: IAST diacritics (ā, ī, ū, ṛ, ṅ, ñ, ṭ, ḍ, ṇ, ś, ṣ, ḥ, ṃ) AND Cyrillic AND Devanagari (for any rare callouts).
- Open SIL Open Font License (OFL).
- Designed by Google to harmonise across scripts — bilingual labels read consistently.
- Falls back gracefully to DejaVu Sans (matplotlib default).

Embedded in `palette-tokens.json` `_meta.font-family`.

## Decision 19 — Licence: CC-BY-SA-4.0

All figures, data dumps, the [csl-atlas](https://github.com/sanskrit-lexicon/csl-atlas) microsite, and the supplementary ZIP are released under [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/), matching the [MWS digital edition's license](../../../LICENSE). Consistency across CDSL artefacts; attribution + share-alike is the long-established CDSL norm.

Per-figure caption note:

```
Released under CC-BY-SA-4.0 · Source: CDSL mw.txt 2026-05-23

```

---

## Implementation status (2026-05-23)

- [x] `palette-tokens.json` written ([figures/palette-tokens.json](../figures/palette-tokens.json))
- [x] `build_palette.py` written and run ([figures/scripts/build_palette.py](../figures/scripts/build_palette.py))
- [x] `palette.css` generated ([figures/palette.css](../figures/palette.css))
- [x] `mermaid-theme.json` generated ([figures/mermaid-theme.json](../figures/mermaid-theme.json))
- [x] `palette.py` generated ([figures/palette.py](../figures/palette.py))
- [ ] `palette.tex` not yet generated (LaTeX export reserved for paper-submission phase)
- [ ] Colour-blind-safe variant not yet validated against Sim Daltonism (planned)

## Cross-links

- [VISUALISATIONS.md](../VISUALISATIONS.md) — catalogue + tier prioritisation
- [DOUBTS.md D9](../DOUBTS.md) — "JSON-first tokens may be over-engineered" — known doubt
- [csl-atlas README](https://github.com/sanskrit-lexicon/csl-atlas) — Pages target
