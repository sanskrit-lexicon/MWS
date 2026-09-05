_Created: 23-05-2026 · Last updated: 05-09-2026_

# Decisions — index

The 28 architecture/design decisions captured during the visualisation-planning phase of the MW microanalysis project, split into thematic documents.

Each decision is also referenced from the canonical [VISUALISATIONS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/VISUALISATIONS.md) summary table.

| File | Decisions covered | Subject |
|---|---|---|
| [PALETTE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/decisions/PALETTE.md) | 1, 9, 18, 19 | Colour palette, JSON-first design tokens, font (Noto Sans), license (CC-BY-SA-4.0) |
| [I18N.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/decisions/I18N.md) | 3, 6, 8, 11, 25 | Bilingual EN/RU, Sanskrit-in-RU (IAST italics), Mermaid i18n, translation workflow, default locale |
| [MICROSITE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/decisions/MICROSITE.md) | 2, 7, 10, 20, 24, 27 | Static + interactive deliverables, csl-atlas repo, Observable Framework, navigation, name, CI/CD |
| [FIGURES.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/decisions/FIGURES.md) | 13, 14, 15, 17, 21, 22, 23, 26, 28 | Legends, accessibility, numbering, dimensions, heatmap layout, Sankey structure, citation style, footer typography, versioning |
| [NORMALISATION.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/decisions/NORMALISATION.md) | 4 | Cross-dictionary normalisation strategy (the big one — 7 options A-G with real data) |
| [SUPPLEMENTARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/decisions/SUPPLEMENTARY.md) | 5, 16 | Attribution, supplementary-materials ZIP |
| [BUILD-ORDER.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/decisions/BUILD-ORDER.md) | 12 | Build sequence (foundation → heatmap → treemap → Sankey → Mermaid) |

---

## Reading order

1. Start with [VISUALISATIONS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/VISUALISATIONS.md) for the visualisation catalogue + 3-tier prioritisation.
2. Drill into the relevant decision file for any specific topic.
3. For architectural critique: read [DOUBTS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/DOUBTS.md).
4. For the live data underlying every visualisation: [MICROANALYSIS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/MICROANALYSIS.md).

## Status (2026-05-23)

28 decisions across 7 rounds of refinement. Restructured 2026-05-23.

The decisions are stable as of the figure-build phase that landed in commit `0901c81` ([heatmap-en.svg](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/figures/heatmap-en.svg), [treemap-en.svg](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/figures/treemap-en.svg), [sankey-en.svg](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/figures/sankey-en.svg), [timeline-en.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/figures/timeline-en.md)). Revisions to specific decisions are tracked per-file with date stamps.

_Dr. Mārcis Gasūns_
