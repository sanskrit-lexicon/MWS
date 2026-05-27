# Decisions — build order

Covers decision **12**. See [decisions/README.md](README.md) for the full index.

---

## Decision 12 — Build sequence

The figure-build phase proceeds in dependency order:

1. **Foundation** — colour palette + locales + data exports
   - [x] `figures/palette-tokens.json` ([PALETTE.md](PALETTE.md))
   - [x] `figures/scripts/build_palette.py` runs → `palette.css`, `palette.py`, `mermaid-theme.json`
   - [x] `figures/locales/en.json`, `figures/locales/ru.json` ([I18N.md](I18N.md))
   - [x] `figures/scripts/export_data.py` runs → 5 JSON files in `figures/data/`

2. **Heatmap** (depends on tokens + locales + matrix data)
   - [x] `figures/scripts/render_heatmap.py` runs in EN and RU
   - [x] Outputs: `heatmap-{en,ru}.{svg,png,alt.txt,desc.txt}` ([Decision 21 in FIGURES.md](FIGURES.md))

3. **Treemap** (depends on tokens + locales + article-type-counts data)
   - [x] `figures/scripts/render_treemap.py` runs in EN and RU
   - [x] Outputs: `treemap-{en,ru}.{svg,png,alt.txt,desc.txt}`

4. **Sankey** (depends on separate kosha-collapse data prep)
   - [x] `figures/scripts/render_sankey.py` runs in EN and RU
   - [x] Outputs: `sankey-{en,ru}.{svg,png,html,alt.txt,desc.txt}` ([Decision 22 in FIGURES.md](FIGURES.md))

5. **Mermaid timeline** (zero new dependencies; just labels + dates)
   - [x] `figures/timeline-en.md` + `figures/timeline-ru.md` ([Decision 8 in I18N.md](I18N.md))

6. **README updates + commit**
   - [x] `papers/microanalysis/README.md` updated to index VISUALISATIONS.md + DOUBTS.md
   - [x] Committed to docs-pass branch as commit `0901c81`

**Target effort:** 1–2 hours.
**Actual:** ~1.5 hours over the 4-hour autonomous session 2026-05-23.

---

## What's next (after Tier 1 figures)

Per [VISUALISATIONS.md](../VISUALISATIONS.md) Tier 2 (~3–5 hours):

7. **Per-article-type radar small-multiples** — paper figure showing 14 type profiles
8. **Annotated sample-entry anatomy** — "anatomy of an MW entry" opening figure
9. **5-dict comparative microstructure fingerprints**
10. **Lineage forest (Mermaid)** — sibling to the timeline
11. **Fullness-distribution histogram**
12. **CDSL pipeline diagram (Mermaid)** — extract from existing csl-sqlite ARCHITECTURE.md

Per Tier 3 (microsite, longer-running):

13. **Type comparator** — interactive side-by-side
14. **Citation tracer** — click a source, see citing entries
15. **Per-dictionary fingerprint cards** — 9 dicts side-by-side

## Cross-links

- [VISUALISATIONS.md](../VISUALISATIONS.md) — full catalogue and tier prioritisation
- [PALETTE.md](PALETTE.md) — foundation step 1
- [I18N.md](I18N.md) — foundation step 1 (locales)
- [FIGURES.md](FIGURES.md) — figure-by-figure conventions
- [MICROSITE.md](MICROSITE.md) — Tier 3 deliverable
- [DOUBTS.md D9](../DOUBTS.md) — "28 decisions before code is premature optimisation" — now demonstrably resolved by Tier 1 shipping
