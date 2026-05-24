# Decisions — attribution and supplementary materials

Covers decisions **5** and **16**. See [decisions/README.md](README.md) for the full index.

---

## Decision 5 — Attribution: cite the digital edition

All figures, papers, and supplementary materials cite **"CDSL `mw.txt` 2026-05-23"** as the data source.

If a journal requires citing the print original (MW 1899), figures can be regenerated against the print at that point — but the digital edition is what we computed against, and the date stamp captures the exact state.

Implementation:
- Every static figure carries a small grey footer (per [FIGURES.md Decision 26](FIGURES.md)).
- Every paper section that quotes a count points to where the count came from.
- The interactive microsite carries the same attribution in a persistent footer.

## Decision 16 — Supplementary materials: self-contained ZIP

**Implemented:** built by [`analysis/make_supplement.py`](../analysis/make_supplement.py) → `mw-microanalysis-supplementary.zip` (87 files, ~1.5 MB; a gitignored build artefact). Contents and rebuild steps are recorded in [`analysis/SUPPLEMENT_MANIFEST.md`](../analysis/SUPPLEMENT_MANIFEST.md). The raw dictionary `.txt` files are not bundled (they live in [csl-orig](https://github.com/sanskrit-lexicon/csl-orig)); the included scripts regenerate every derived artefact from them.

The IJL submission includes a single ZIP archive `mw-microanalysis-supplementary.zip` containing:

```
supplementary/
  README.md                            entry point
  paper/                               PAPER.md (PDF + markdown source)
  data/                                JSON dumps of the block matrix,
                                       citation stats, fullness distribution, etc.
  figures/                             all static SVG figures + PNG fallbacks
                                       + alt + desc + caption files
  scripts/                             Python reproducibility code:
                                       mw_block_matrix.py, build_palette.py,
                                       export_data.py, render_heatmap.py,
                                       render_treemap.py, render_sankey.py
  microsite-static-export/             offline-renderable HTML export of csl-atlas
  LICENSE                              CC-BY-SA-4.0
```

**No external dependencies.** A reviewer with the ZIP, Python 3, and a modern browser can:
- Reproduce every figure (Python scripts + JSON data).
- Explore every visualisation offline (microsite-static-export).
- Verify every count (the underlying `mw.txt` is referenced by date but also fetchable from CDSL).

Survives:
- URL rot (no live links required for reproduction).
- Microsite outages (offline copy preserved).
- Post-submission infrastructure changes (csl-atlas could be deprecated; ZIP still works).

## Implementation status (2026-05-23)

- [x] Per-figure attribution footer implemented (Decision 5, see [FIGURES.md](FIGURES.md))
- [x] All data files exported to JSON in [`figures/data/`](../figures/data/)
- [x] All Python scripts in [`figures/scripts/`](../figures/scripts/)
- [x] Static figures rendered as SVG + PNG with sidecar alt/desc files
- [ ] Supplementary ZIP not yet packaged (waits for paper-submission phase)
- [ ] Microsite static export not yet generated (waits for csl-atlas `npm run build`)

## Cross-links

- [VISUALISATIONS.md](../VISUALISATIONS.md) — catalogue
- [FIGURES.md](FIGURES.md) — footer typography
- [PALETTE.md](PALETTE.md) — license (CC-BY-SA-4.0)
- [BUILD-ORDER.md](BUILD-ORDER.md) — when the ZIP gets packaged
