# Visualisation catalogue — MW1899 microanalysis and beyond

**Planning document.** A comprehensive catalogue of visualisations the data collected for the [microanalysis](README.md) supports, organised by purpose, with implementation notes and a tiered prioritisation. Useful for (a) figure selection for the four framework papers ([Wiegand](paper-wiegand.md) · [Atkins-Rundell](paper-atkins-rundell.md) · [Hausmann-Wiegand](paper-hausmann.md) · [Grounded](paper-grounded.md)), (b) embedding in the docs-pass branch (DICT_PROFILE / ENTRY_GUIDE / ROADMAP), and (c) the reusable Phase-4 pattern for other CDSL dictionaries.

Data source: [MICROANALYSIS.md](MICROANALYSIS.md) and the docs-pass material in the parent directory.

---

## Data inventory — what we have to visualise

Quick recap of the quantitative dimensions available:

| Dimension | Source | Cardinality |
|---|---|---:|
| Total entries | [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) | 286,561 |
| Formal blocks | [MICROANALYSIS.md §1](MICROANALYSIS.md#1--formal-block-inventory-18-blocks) | 18 |
| Semantic blocks | [MICROANALYSIS.md §2](MICROANALYSIS.md#2--semantic-block-taxonomy-8-categories) | 8 |
| Article types | [MICROANALYSIS.md §3](MICROANALYSIS.md#3--article-type-typology-14-types) | 14 |
| Block-by-type matrix | [MICROANALYSIS.md §4](MICROANALYSIS.md#4--the-block-by-article-type-matrix) | 18 × 14 = 252 cells |
| Fullness tiers | [MICROANALYSIS.md §5](MICROANALYSIS.md#5--fullness-scale) | 5 |
| `<ls>` citation totals | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#coverage-of-ls-citations) | 311,932 across 821 unique abbreviations |
| Top sources | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#top-25-most-cited-sources) | top 25 with counts + periods |
| Period buckets | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#period-breakdown) | 14 (Epic, Vedic, Lex, Editorial, …) |
| `<lang>` IE cognates | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#ie-cognate-density--lang-breakdown) | 112 languages, 3,960 tags |
| `<e>` hierarchy codes | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#entry-hierarchy-distribution) | 21 sub-codes |
| `<lex>` distribution | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#entry-type-breakdown-by-content) | m./f./n./mfn./ind./mn./… |
| Cross-dict comparison | [DICT_PROFILE Same entry](../../DICT_PROFILE.md#same-entry-across-five-dictionaries) | MW / PWG / AP / WIL / SKD |
| Kosha lineage data | [DICT_PROFILE Lineage](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) | 6 named kosha sources in PWG vs 1 (`L.`) in MW |
| Issue tracker | [ROADMAP](../../ROADMAP.md) | 34 open, 157 closed, 9 label classes |
| Authority coverage | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#coverage-of-ls-citations) | 232 / 821 with records (28.3%) |
| Timeline anchors | [DICT_PROFILE Historical background](../../DICT_PROFILE.md#historical-background) | 8 events from ~6th c. to 2024 |

---

## Category 1 · Composition / distribution charts

Show what proportions are in the dictionary at a glance.

| # | Visualisation | Data source | What it shows | Effort | Format |
|--:|---|---|---|---|---|
| 1.1 | **Treemap of 286,561 entries by article type** | 14 article-type counts | Compound dominance (44%); derived (25%); the "long tail" of rarer types | Low | PNG/SVG (squarify, D3) |
| 1.2 | **Donut / pie — `<e>` hierarchy codes** | 21 e-codes with counts | The `<e>3` compound 39% slice tells the structural story | Low | PNG/SVG/inline matplotlib |
| 1.3 | **Fullness histogram (1–13 blocks per entry)** | block-count distribution | Modal 6-block kernel + long tail; supports the "block economy" claim | Trivial | PNG bar chart |
| 1.4 | **Stacked bar — top 25 sources coloured by period** | top-25 counts × 14 period buckets | Lexicographer L. = 40K dominates; Epic/Vedic/Editorial visible at scale | Low | matplotlib `barh` |
| 1.5 | **Tag-frequency cloud** | top 100 `<ls>` / `<lang>` / `<ab>` values | Quick visual of dictionary's citation universe | Low | `wordcloud` lib |
| 1.6 | **Cumulative coverage curve** | sorted source-citation counts | Top-10 sources cover ~50%; top-100 cover ~90% — visualises the power-law | Low | matplotlib step plot |

---

## Category 2 · The matrix heatmap — central paper figure

The 18 × 14 block-by-article-type matrix from [MICROANALYSIS.md §4](MICROANALYSIS.md#4--the-block-by-article-type-matrix) is the **single most important visualisation** for the four framework papers.

| # | Visualisation | What it adds | Effort | Format |
|--:|---|---|---|---|
| 2.1 | **18 × 14 block × type heatmap (raw %)** | Diagonal hot-spots: F14→botanical 100%, F15→biographical 100%, F13→lex_only 100%. Off-diagonals: F13 hedge at 71.5% in botanicals reveals the *koshic* basis of plant names | Low | `matplotlib.imshow`, Vega-Lite heatmap |
| 2.2 | **Diverging heatmap — block deviation from baseline** | Red = under-represented vs column mean, green = over-represented. Crisper signal than raw % | Low | Same, `cmap='RdYlGn'` |
| 2.3 | **Block co-occurrence heatmap (18 × 18)** | Reveals the "core quintet" F01+F02+F04+F10+F12+F17 — the kernel of the block-economy thesis | Low | Symmetric matrix |
| 2.4 | **Chord diagram of block co-occurrence** | Same data as 2.3 but visualises *strength* of pair-co-occurrence as arc thickness | Medium | D3 chord, Plotly |

---

## Category 3 · Cross-dictionary comparison

MW against PWG / AP / WIL / SKD — the comparative dimension of the [Beyond PWG analysis](../../DICT_PROFILE.md#beyond-pwg--what-mw-contributes).

| # | Visualisation | Data | What it shows | Effort | Format |
|--:|---|---|---|---|---|
| 3.1 | **Multi-bar comparison: 5 dicts × 4 metrics** | records (MW 286K / PWG 123K / AP 91K / WIL 45K / SKD 43K) + `<ls>` totals + kosha cites + L. cites | The "block economy" claim quantified across the 5 dicts in one chart | Low | matplotlib grouped bar |
| 3.2 | **Parallel-coordinates / slope chart** | 5 dicts × 6 normalised metrics | Tracks each dictionary's "fingerprint" across dimensions; reveals MW's atypical L.-spike | Medium | D3 parallel-coords, Plotly |
| 3.3 | **Microstructure fingerprints (small multiples)** | 5 dicts × 18 block frequencies | Each dict gets a small heat-strip placed side by side — instant visual comparison | Medium | matplotlib subplots grid |
| 3.4 | **Sankey: PWG kosha cites → MW `L.` collapse** | PWG `H.` 17,337 + `AK.` 14,473 + `MED.` 13,055 + `H. an.` 9,771 + `TRIK.` 8,365 + `HALĀY.` 5,114 → MW `L.` 40,213 | **The definitive visualisation of the lineage finding.** Six PWG flows merging into one MW flow. Would be the killer figure of the [Lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) | Medium | Plotly Sankey, D3 Sankey |
| 3.5 | **Side-by-side entry-anatomy** | the *aṃśa* entry across 5 dicts | Pull from [DICT_PROFILE Same entry](../../DICT_PROFILE.md#same-entry-across-five-dictionaries) — visualise as 5 columns with block annotations | Medium | Hand-crafted SVG or HTML |

---

## Category 4 · Lineage / temporal

| # | Visualisation | Data | What it shows | Effort | Format |
|--:|---|---|---|---|---|
| 4.1 | **Lexicographic timeline** | Amarakośa ~6c → Halāyudha ~10c → Hemacandra ~12c → Śabdakalpadruma 1822–58 → WIL 1832 → PWG 1855–75 → MW 1872 → MW 1899 → CDSL 2014ff → csl-pywork 2024 update | Anchors the kosha → WIL/PWG → MW lineage in one image | Low | **Mermaid `timeline`** (renders natively in GitHub) |
| 4.2 | **Dictionary forest** | The kosha → WIL/PWG → MW network with directional arrows + citation counts | The figure for the lineage section | Low | Mermaid `graph LR` or `flowchart` |
| 4.3 | **Citation-flow chord** | 12 most-cited literary works × 7 period buckets | Which periods MW privileges | Medium | D3 chord diagram |
| 4.4 | **Cumulative count timeline** | total Sanskrit lexicographic words over time | Growth of the lexicographic tradition 6th c. → 2024 | Medium | Stepped area chart |

---

## Category 5 · Sample-entry anatomy diagrams

| # | Visualisation | Data | Where it belongs | Effort | Format |
|--:|---|---|---|---|---|
| 5.1 | **Annotated sample entry — L10 *áṃśa*** | the raw entry + 18-block tags | Opening figure of the IJL paper — "anatomy of an MW entry" | Low | Hand-built SVG, Inkscape |
| 5.2 | **The 14 article types as anatomy small-multiples** | one sample per type + its block profile | Per-type at-a-glance — supports the §6 worked-samples section of MICROANALYSIS.md | Medium | SVG grid, ~14 small figures |
| 5.3 | **`<e>` hierarchy tree for *áṃśa* / *aṃśu*** | L10 + L11–L19 + L47 + L48–56 + L57+ compound chain | Visualises the integrated-microstructure claim concretely | Low | Mermaid tree or D3 dendrogram |

---

## Category 6 · Geographic / cognate visualisations

| # | Visualisation | Data | What it shows | Effort | Format |
|--:|---|---|---|---|---|
| 6.1 | **Map of `<lang>` distribution** | top 25 IE languages with counts + centroids | MW's Indo-European reach: Lat. 527 (Italy), Gk. 504 (Greece), Goth. 200 (Crimea/Gothic), Lith. 182 (Baltic), Zd. 139 (Persia), Pers. 17 (Iran) | Medium | Folium, D3 + GeoJSON |
| 6.2 | **Cognate-density circular diagram** | `<lang>` per IE branch (Celtic / Italic / Hellenic / Germanic / Slavic / Baltic / Indo-Iranian) | Branch-wise comparison | Medium | D3 sunburst |
| 6.3 | **Heatmap: kosha citation density by region** | PWG cites of AK/H/MED by compilation region (Kashmir / Gujarat / Bengal / South) | Where MW's indigenous lexica come from | High — requires kosha provenance research | D3 chloropleth |

---

## Category 7 · Statistical / methodological

| # | Visualisation | Data | What it shows | Effort | Format |
|--:|---|---|---|---|---|
| 7.1 | **Scatter — avg-fullness vs entry-count per type** | 14 article types | Inverse: roots = 9.73 blocks × 750 entries; compounds = 6.02 blocks × 126K entries | Trivial | matplotlib scatter |
| 7.2 | **Boxplot of block-count per type** | block counts grouped by type | Where each type's "fullness" centres + disperses; outliers visible | Trivial | seaborn box/violin |
| 7.3 | **Coverage vs orphan rate** | authority-record coverage per dict | The 28.3% / 64.0% / 96.1% figure, generalisable to other dicts in Phase 4 | Medium | Stacked bar |
| 7.4 | **Distribution comparison: with/without coordinate** | 47,227 (15.1%) coordinate vs 264,705 (84.9%) bare cites | Visual evidence that most `<ls>` cites are work-name-only | Trivial | Stacked bar / pie |

---

## Category 8 · Process / pipeline diagrams

| # | Visualisation | Data | Where | Effort | Format |
|--:|---|---|---|---|---|
| 8.1 | **CDSL pipeline architecture** | csl-orig → csl-pywork → csl-sqlite → csl-app | Already partly in [csl-sqlite ARCHITECTURE.md](https://github.com/sanskrit-lexicon/csl-sqlite/blob/docs-pass/ARCHITECTURE.md); could be extracted as standalone figure | Low | **Mermaid `graph LR`** |
| 8.2 | **Per-issue correction workflow** | temp_mw_N.txt → generate_dict.sh → xmlchk_xampp.sh → commit | Already in [CONTRIBUTING.md](../../CONTRIBUTING.md#correction-workflow-per-issue); visualise as sequence | Low | Mermaid `sequenceDiagram` |
| 8.3 | **Roadmap burndown / Gantt** | 34 open issues × 4 quarters | Q1/Q2/Q3 plan vs realistic 4-per-year velocity | Low | Mermaid `gantt` |
| 8.4 | **Issue-closure velocity (historical)** | 157 closed issues with `closedAt` dates | Closures per quarter over the project's lifetime | Low | Stepped line / bar |

---

## Category 9 · Specialty / radar-style

| # | Visualisation | Data | What it shows | Effort | Format |
|--:|---|---|---|---|---|
| 9.1 | **Microstructure radar per article type** | 14 radars × 18 axes | "Shape" of each article type's block profile. Roots = star-shaped (many spikes); continuations = small + minimal | Medium | matplotlib radar / D3 |
| 9.2 | **Block-profile fingerprint icons** | 18-cell mini-grid per type | Tiny iconic representation; useful at chart margins or in typology tables | Medium | Custom SVG (~14 icons) |
| 9.3 | **Type-comparison butterfly chart** | pick any 2 article types, plot block diffs | Side-by-side block comparison | Medium | Diverging-bar mirrored |

---

## Category 10 · Interactive (microsite)

Higher effort; assume an HTML hosting target (GitHub Pages, similar).

| # | Visualisation | What | Effort | Stack |
|--:|---|---|---|---|
| 10.1 | **Type comparator** | Pick 2 article types, see live block matrix diff | High | D3 + Vega |
| 10.2 | **Live entry browser with block highlighting** | Hover any entry, see blocks colour-coded; filter by type | High | D3, with mw.txt parsed to JSON |
| 10.3 | **Citation tracer** | Click `RV.`, see all entries citing it (entry-list / heatmap) | High | D3 + indexed JSON |
| 10.4 | **Per-dictionary fingerprint cards** | 8 CDSL dicts × 18 blocks as flippable cards | Medium-High | Tinder-style UI |
| 10.5 | **Quarterly roadmap viewer** | Quarter-by-quarter task drilldown linked to GitHub issues | Medium | Simple HTML + GitHub API |

---

## Tier-1 recommendations (build first)

High impact, low effort. These are the four images that would most strengthen the docs and the IJL paper.

| Rank | Visualisation | Why | Best home |
|:--:|---|---|---|
| **#1** | [2.1] 18 × 14 block × type heatmap | Single central figure for all four framework papers. The "what is MW's microstructure" image | `papers/microanalysis/figures/heatmap.svg` referenced from [MICROANALYSIS.md §4](MICROANALYSIS.md#4--the-block-by-article-type-matrix) and all four papers |
| **#2** | [3.4] PWG kosha → MW `L.` collapse Sankey | Killer figure for the lineage finding. Visually proves the kosha-collapse claim | `papers/microanalysis/figures/lineage-sankey.svg` referenced from [DICT_PROFILE Lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) |
| **#3** | [4.1] Lexicographic timeline (Mermaid) | Inline-renderable in GitHub markdown; zero infrastructure; orients the lineage for any reader | Embedded directly in [DICT_PROFILE Historical background](../../DICT_PROFILE.md#historical-background) |
| **#4** | [1.1] Article-type treemap | Single image for the dictionary's composition — the "what is MW?" overview | `papers/microanalysis/figures/typology-treemap.svg` referenced from [DICT_PROFILE Article types](../../DICT_PROFILE.md#article-types--what-youll-encounter) |

**Total effort:** ~1–2 hours with matplotlib + Plotly + Mermaid inline.

---

## Tier-2 recommendations (build second)

Medium effort, still high value. Worth doing if the four papers go to submission.

| Rank | Visualisation | Why | Best home |
|:--:|---|---|---|
| **#5** | [9.1] Per-article-type radar small-multiples | Paper figure showing 14 type-profiles in one panel | Microanalysis §6 |
| **#6** | [5.1] Annotated sample-entry anatomy | "Anatomy of an MW entry" opening figure for the IJL paper — instantly orienting | Microanalysis §6 opener; paper opener |
| **#7** | [3.3] 5-dict comparative microstructure fingerprints | Side-by-side visual showing dictionaries' different "shapes" | DICT_PROFILE.md cross-dict section |
| **#8** | [4.2] Dictionary lineage forest (Mermaid) | Inline-renderable; complements the timeline | DICT_PROFILE Lineage section |
| **#9** | [1.3] Fullness-distribution histogram | Visualises the modal-6-block + long-tail claim of the grounded paper | Microanalysis §5 |
| **#10** | [8.1] CDSL pipeline diagram (Mermaid) | Already partially built in csl-sqlite ARCHITECTURE.md; extract and reuse | ROADMAP.md cross-repo section |

**Total effort:** ~3–5 hours.

---

## Tier-3 recommendations (interactive microsite)

Only if hosting is set up. Each is a substantial project. Should not block paper submission.

- [10.1] Type comparator
- [10.2] Live entry browser
- [10.3] Citation tracer
- [10.4] Dictionary fingerprint cards

Estimated effort if undertaken: ~2–4 weeks for a polished microsite.

---

## Implementation notes — tool choice per visualisation type

| Visualisation type | Recommended tool | Where it embeds |
|---|---|---|
| Heatmap / matrix | `matplotlib.pyplot.imshow` or Vega-Lite | PNG/SVG in `papers/microanalysis/figures/` |
| Bar / histogram / scatter | `matplotlib` (paper-quality) or `plotly` (interactive) | Same |
| Sankey | `plotly.graph_objects.Sankey` (HTML+PNG) or `d3-sankey` | HTML + PNG export |
| Treemap | `squarify` (Python) + matplotlib | SVG/PNG |
| Radar / spider | `matplotlib` polar plot | SVG/PNG |
| Sunburst / chord | `plotly.graph_objects.Sunburst` / D3 chord | HTML + PNG |
| Tree / dendrogram | `scipy.cluster.hierarchy.dendrogram` or D3 | SVG |
| Geographic map | `folium` (HTML/Leaflet) or `geopandas` (matplotlib) | HTML or SVG |
| Word cloud | `wordcloud` Python lib | PNG |
| **Mermaid** (timeline / graph / flowchart / sequence / gantt) | inline ```mermaid blocks | **Inline in markdown — renders natively in GitHub** |
| Interactive HTML | D3.js + Vega-Lite | GitHub Pages site |

**For the IJL paper itself:** SVG figures preferred (vector, scales, archives well). Generate from Python (matplotlib/plotly) → SVG export → embedded in LaTeX or in the paper.md via markdown image embed.

**For the docs-pass branch:** Mermaid wherever possible (Tier-1 #3, Tier-2 #8, #10). PNG/SVG embed for the heatmap / Sankey / treemap.

---

## Reusability for Phase 4 (other CDSL dicts)

Each visualisation type generalises to any CDSL dictionary by re-running the block-detection script ([`mw_block_matrix.py`](../microanalysis/MICROANALYSIS.md#9--open-analytical-questions-for-the-four-framework-papers)) against that dict's data file. The pattern:

```
For each CDSL dict (PWG, AP, WIL, SKD, GRA, BHS, +the four koshas):
  1. Parse <L>...<LEND> records from <dict>.txt
  2. Classify each entry into the 14 article types (or dict-specific types)
  3. Compute block-by-type matrix
  4. Render the four Tier-1 figures
  5. Produce a one-page "microstructure card" per dictionary
```

A **comparative atlas** of 8+ CDSL dictionaries' microstructure cards would be a natural Phase-4 deliverable. The infrastructure cost is one-time (the block-detection script); the per-dictionary cost is one Python run plus minor type-specific adjustments.

Particularly interesting cross-dict visualisations:

- **Microstructure fingerprint atlas** (Tier-2 #7) extended to all 8+ dicts
- **Lineage tree** (Tier-2 #8) extended with all kosha-derived dicts
- **Per-dictionary radar grid** showing where each dictionary specialises
- **Authority-record coverage comparison** across all CDSL dicts — surfaces which dicts have orphans

---

## Open questions for visualisation design

1. **Colour palette consistency** — should all four framework papers use the same colours for the 14 article types? (Recommendation: yes; defines a palette in `papers/microanalysis/figures/palette.json` and reuses.)

2. **Static vs interactive trade-off** — IJL accepts only static figures, but a microsite would help reviewers explore. Should we build both (interactive supplementary materials linked from the paper)?

3. **Bilingual labels** — visualisation labels in English (paper) vs Sanskrit-also (community)? Important if any visualisation becomes the canonical "MW microstructure" reference image used by both audiences.

4. **Cross-dict comparison normalisation** — when comparing PWG (1855–75, 123K records) to MW (1899, 286K records), do we normalise by record count, by `<ls>` density, by something else? Different choices yield different visual stories.

5. **Author attribution on figures** — if these are journal figures, do they cite the data source as "CDSL `mw.txt` 2026-05-23" or the original MW1899 print? Different journals have different conventions.

---

## Status

This document is the **planning catalogue**. None of the visualisations listed are yet built. Tier-1 (4 figures) is the recommended next step. The Python data is already in [MICROANALYSIS.md](MICROANALYSIS.md) and the working scripts are at [`mw_block_matrix.py`](MICROANALYSIS.md) (regenerable in seconds against any updated mw.txt).

When figures are built, they should land in `papers/microanalysis/figures/` (created on first commit) and be referenced from both MICROANALYSIS.md and the four framework papers, plus DICT_PROFILE.md where they support the cross-dict and lineage sections.
