# Visualisation catalogue — MW1899 microanalysis and beyond

**Planning document.** A comprehensive catalogue of visualisations the data collected for the [microanalysis](README.md) supports, organised by purpose, with implementation notes and a tiered prioritisation. Useful for (a) figure selection for the consolidated [paper](PAPER.md) (body + [Appendices A–C](PAPER.md#appendix-a--the-wiegand-theoretic-reading-condensed)), (b) embedding in the docs-pass branch (DICT_PROFILE / ENTRY_GUIDE / ROADMAP), and (c) the reusable Phase-4 pattern for other CDSL dictionaries.

Data source: [MICROANALYSIS.md](MICROANALYSIS.md) and the docs-pass material in the parent directory.

---

## Data inventory — what we have to visualise

Quick recap of the quantitative dimensions available:

| Dimension | Source | Cardinality |
|---|---|---:|
| Total entries | [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) | 286,561 |
| Formal blocks | [MICROANALYSIS.md §1](MICROANALYSIS.md#1--formal-block-inventory-18-blocks) | 18 |
| Semantic blocks | [MICROANALYSIS.md §2](MICROANALYSIS.md#2--semantic-block-taxonomy-8-categories) | 8 |
| Article types | [MICROANALYSIS.md §3](MICROANALYSIS.md#3--article-type-typology-8-primary-types--3-orthogonal-properties) | 14 |
| Block-by-type matrix | [MICROANALYSIS.md §4](MICROANALYSIS.md#4--the-block-by-article-type-matrix) | 18 × 14 = 252 cells |
| Fullness tiers | [MICROANALYSIS.md §5](MICROANALYSIS.md#5--fullness-scale) | 5 |
| `<ls>` citation totals | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#coverage-of-ls-citations) | 311,932 across 821 unique abbreviations |
| Top sources | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#top-25-most-cited-sources) | top 25 with counts + periods |
| Period buckets | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#period-breakdown) | 14 (Epic, Vedic, Lex, Editorial, …) |
| `<lang>` IE cognates | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#ie-cognate-density--lang-breakdown) | 112 languages, 3,960 tags |
| `<e>` hierarchy codes | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#entry-hierarchy-distribution) | 21 sub-codes |
| `<lex>` distribution | [ENTRY_GUIDE](../../ENTRY_GUIDE.md#entry-type-breakdown-by-content) | m./f./n./mfn./ind./mn./… |
| Cross-dict comparison | [DICT_PROFILE Same entry](../../DICT_PROFILE.md#same-entry-across-seven-dictionaries) | MW / PWG / AP / WIL / SKD |
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

The 18 × 14 block-by-article-type matrix from [MICROANALYSIS.md §4](MICROANALYSIS.md#4--the-block-by-article-type-matrix) is the **single most important visualisation** for the paper.

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
| 3.5 | **Side-by-side entry-anatomy** | the *aṃśa* entry across 5 dicts | Pull from [DICT_PROFILE Same entry](../../DICT_PROFILE.md#same-entry-across-seven-dictionaries) — visualise as 5 columns with block annotations | Medium | Hand-crafted SVG or HTML |

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
| **#1** | [2.1] 18 × 14 block × type heatmap | Central figure of the paper. The "what is MW's microstructure" image | `papers/microanalysis/figures/heatmap.svg` referenced from [MICROANALYSIS.md §4](MICROANALYSIS.md#4--the-block-by-article-type-matrix) and [PAPER.md](PAPER.md) |
| **#2** | [3.4] PWG kosha → MW `L.` collapse Sankey | Killer figure for the lineage finding. Visually proves the kosha-collapse claim | `papers/microanalysis/figures/lineage-sankey.svg` referenced from [DICT_PROFILE Lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) |
| **#3** | [4.1] Lexicographic timeline (Mermaid) | Inline-renderable in GitHub markdown; zero infrastructure; orients the lineage for any reader | Embedded directly in [DICT_PROFILE Historical background](../../DICT_PROFILE.md#historical-background) |
| **#4** | [1.1] Article-type treemap | Single image for the dictionary's composition — the "what is MW?" overview | `papers/microanalysis/figures/typology-treemap.svg` referenced from [DICT_PROFILE Article types](../../DICT_PROFILE.md#article-types--what-youll-encounter) |

**Total effort:** ~1–2 hours with matplotlib + Plotly + Mermaid inline.

---

## Tier-2 recommendations (build second)

Medium effort, still high value. Worth doing if the paper goes to submission.

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

Each visualisation type generalises to any CDSL dictionary by re-running the block-detection script ([`mw_block_matrix.py`](../microanalysis/MICROANALYSIS.md#9--open-analytical-questions-for-the-paper)) against that dict's data file. The pattern:

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

## Design decisions (2026-05-23)

Five open questions raised in the original draft of this document have been resolved by [@gasyoun](https://github.com/gasyoun). Decisions:

### Decision 1 — Shared colour palette via CSS

**The paper + the interactive microsite use the same colour palette for the 14 article types.** Implementation: **via CSS** (custom properties / design tokens), so that a single source-of-truth defines colours that flow through (a) the static SVG figures generated for the paper, (b) the Mermaid diagrams embedded in markdown docs, and (c) the interactive microsite.

The CSS strategy lets us:

- Swap colour themes without re-rendering data (e.g. dark mode, print-friendly mode, colour-blind safe variant)
- Keep static SVG and interactive HTML visually consistent without manual sync
- Allow downstream Phase-4 dictionaries to inherit the same palette

**Implementation plan:**
- A `papers/microanalysis/figures/palette.css` file defines `--mw-color-*` custom properties (one per article type, one per semantic class, one per fullness tier, plus chart-element colours: background, grid, axes, text).
- Static SVG figures generated from Python embed inline `<style>` blocks that import the palette as variables (or have the palette baked in at render time).
- Mermaid diagrams use a Mermaid theme variables file (`mermaid-theme.json`) regenerated from the CSS palette.
- The interactive microsite (Decision 2) consumes the same CSS palette directly.

### Decision 2 — Build both static (paper) and interactive (microsite)

**Both deliverables.** Static figures (SVG, embeddable in IJL paper) plus an interactive microsite (HTML, linked from the paper as supplementary materials). The microsite lets reviewers explore the matrix, hover entries, filter by article type — value that no static figure delivers.

**Implications:**
- Tier 1 figures (heatmap, Sankey, timeline, treemap) are produced **twice**: once as static SVG with embedded palette, once as interactive HTML/JS.
- Tier 3 items (type comparator, entry browser, citation tracer) become *deliverables*, not "future-if-funded."
- Data binding strategy: the data lives in JSON files (`papers/microanalysis/figures/data/`) consumed by both the static renderer (Python) and the interactive renderer (D3 / Vega-Lite).
- Hosting target: resolved in [decisions/MICROSITE.md](decisions/MICROSITE.md) (new `csl-atlas` repo, GitHub Pages).

### Decision 3 — Bilingual labels: English + Russian

**Bilingual labels in English and Russian** — not Sanskrit. Sanskrit is the meta-level (the language being described, not a label language used to describe). Russian is the second target audience: some findings additional to the English journals will be published in Russian-language venues.

**Implications:**
- All visualisation labels exist in two locale strings: `en` and `ru`.
- Labels live in a JSON file (`papers/microanalysis/figures/locales/`) — `en.json` and `ru.json` — keyed by an i18n identifier.
- Static renderer (Python) accepts a locale flag and emits the right strings.
- Interactive microsite has a locale-switcher control.
- Sanskrit terms (lemmas, abbreviations, tag names) are preserved in their conventional rendering (IAST in italic, SLP1 in code blocks); they are not translated, only the surrounding labels are.

The exact convention for how Sanskrit terms appear inside Russian text is resolved in [decisions/I18N.md](decisions/I18N.md).

### Decision 4 — Cross-dictionary normalisation: detailed analysis

The choice of normalisation strategy materially affects what the visualisations *say*. Per [@gasyoun](https://github.com/gasyoun)'s request, here are the seven approaches with their **real** numerical and visual implications (computed 2026-05-23 against the live data files in [csl-orig](https://github.com/sanskrit-lexicon/csl-orig)):

#### Option A — Raw absolute counts (no normalisation)

| Dict | Entries | `<ls>` tags | Unique `<ls>` labels | `<ls>L.</ls>` |
|---|--:|--:|--:|--:|
| [MW](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) | **286,561** | **311,932** | 821 | **40,212** |
| [PWG](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt) | 123,366 | **570,817** | **2,420** | 0 |
| [PWK](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pw/pw.txt) | 170,556 | 86,750 | 915 | 0 |
| [AP](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/ap/ap.txt) | 90,654 | 62,656 | 608 | 1 |
| [VCP](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/vcp/vcp.txt) | 50,135 | 0 | 0 | 0 |
| [WIL](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/wil/wil.txt) | 44,577 | 230 | 5 | 0 |
| [SKD](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/skd/skd.txt) | 42,531 | 0 | 0 | 0 |

**Visual story this tells:** "MW is the largest single-volume Sanskrit-English dictionary, but PWG (across its 7-volume run) carries 1.8× more `<ls>` citations across nearly 3× as many distinct source labels."

**What it obscures:** PWG's density is partly an artifact of having **no `L.` hedge** — PWG distributes its citations across 2,420 named sources where MW collapses many of them into one. **Raw counts make PWG look more rigorous than it is** in a strict sense, by hiding the fact that 14% of MW's apparently-thinner citation apparatus IS the kosha attribution PWG names separately.

**When to use:** Whenever absolute scale is the message — e.g. "MW is the standard single-volume reference."

#### Option B — Per-entry normalisation (cites/entry)

| Dict | `<ls>` cites/entry |
|---|--:|
| PWG | **4.63** |
| MW | 1.09 |
| AP | 0.69 |
| PWK | 0.51 |
| WIL | 0.01 |
| VCP / SKD | 0 (no `<ls>` apparatus) |

**Visual story:** "PWG is **4.25× more citation-dense per entry** than MW, **6.7× more than AP**, **9× more than PWK**, **460× more than WIL**, **infinitely more than VCP / SKD**."

**What it obscures:** Penalises MW for having many `<e>3` compound sub-entries that don't *need* citations. MW's 126,360 compounds inflate the denominator without diluting the citation effort — what matters editorially is *coverage of citations among entries that need them*, not the raw ratio.

**When to use:** When the comparison is **about editorial citation density**.

#### Option C — Per-headword normalisation (top-level entries only)

Note: only MW and AP use the `<e>1` top-level marker. PWG / PWK / WIL / VCP / SKD use different structural conventions (no `<e>` tag at all in PWG and WIL). For these dicts, **top-level entries are not directly countable** from the markup; estimates would require dict-specific heuristics.

| Dict | `<e>1` entries | % of total | `<ls>` cites/`<e>1` |
|---|--:|--:|--:|
| MW | **32,116** | 11.2% | 9.71 |
| AP | **49,452** | 54.6% | 1.27 |
| PWG | 0 (no `<e>` markup) | — | — |
| PWK | 0 (no `<e>` markup) | — | — |
| WIL | 0 (no `<e>` markup) | — | — |
| VCP / SKD | 0 (no `<e>` markup) | — | — |

**Visual story:** "MW reserves `<e>1` for ~11% of entries (a true main-headword count); AP uses it for ~55% — different segmentation conventions."

**What it obscures:** Without parsing each dict's specific conventions, "top-level" isn't comparable. The right move for cross-dict work is **Option E (per-unique-`<k1>`)** which works for all dicts.

**When to use:** When comparing MW and AP specifically; not generalisable.

#### Option D — Per-million-words normalisation (text-volume normalised)

Word counts measured after stripping XML tags + SLP1 markers.

| Dict | Word count | `<ls>` per 10⁶ words | Bytes |
|---|--:|--:|--:|
| MW | 4,781,977 | 65,229 | 47.8 MB |
| PWG | 3,581,113 | **159,395** | 50.8 MB |
| VCP | 2,898,025 | 0 | 23.9 MB |
| SKD | 2,937,417 | 0 | 21.8 MB |
| PWK | 2,305,786 | 37,623 | 30.0 MB |
| AP | 1,781,226 | 35,176 | 17.7 MB |
| WIL | 1,104,886 | 208 | 9.5 MB |

**Visual story:** "PWG packs **2.4× more `<ls>` citations per word of text** than any other CDSL dictionary, twice as many as MW's per-word rate."

**What it obscures:** Heavy compound enumeration in MW inflates word count via gloss text. SKD/VCP have ~3M words but zero `<ls>` apparatus — Sanskrit-Sanskrit lexicography uses citation differently (embedded quotations rather than tagged `<ls>`).

**When to use:** When comparing **textual artifacts as artifacts** — how much content fits per page.

#### Option E — Per-unique-headword normalisation (deduplicated `<k1>`)

Counts unique `<k1>` SLP1-form values across the entire dict, ignoring homophone numbering and entry-type splits:

| Dict | Unique `<k1>` | `<ls>` per unique headword |
|---|--:|--:|
| MW | 194,084 | 1.61 |
| PWK | 151,349 | 0.57 |
| PWG | 106,083 | **5.38** |
| AP | 88,701 | 0.71 |
| VCP | 48,636 | 0 |
| WIL | 43,938 | 0.01 |
| SKD | 40,817 | 0 |

**Visual story:** PWG remains the most citation-dense per unique lemma; MW second; PWK and AP comparable; WIL/SKD/VCP near-zero.

**Comparison to Option B:** the ranking is identical but the absolute numbers shift. MW's 1.61 cites/unique-headword vs PWG's 5.38 is the cleanest "editorial citation choice" comparison.

**What it obscures:** Different dicts have different homophone-numbering conventions; standardising requires per-dict adjustment for true comparability.

**When to use:** Whenever you want the **truest "per-word" comparison** across dicts with different macrostructures.

#### Option F — Coverage normalisation (% of entries citing X)

For each source X, what fraction of each dict's entries cite X at all?

**WIL is excluded from this table** (always 0% — Wilson does not use the `<ls>` apparatus; see [DICT_PROFILE Lineage](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) for why). Per [@gasyoun](https://github.com/gasyoun)'s request, **PWK is included in the comparison** to show the middle term between PWG (kosha-rich) and MW (L.-collapsed):

| Source | MW | PWG | PWK | AP |
|---|--:|--:|--:|--:|
| RV. (Rigveda) | 4.63% | **8.96%** | 0.80% | 0.00% |
| MBh. (Mahābhārata) | 8.93% | **13.84%** | 2.19% | 0.00% |
| R. (Rāmāyaṇa) | 3.59% | 8.71% | 0.94% | 4.89% |
| Pāṇ. (Pāṇini) | 2.79% | **11.72%** | 0.18% | 1.32% |
| **H. (Hemacandra)** | **0.00%** | **12.18%** | **0.59%** | 0.73% |
| **AK. / Amar. (Amarakośa)** | **0.08%** | **8.35%** | **0.03%** | 0.00% |
| **MED. (Medinīkośa)** | **0.00%** | **4.20%** | **0.04%** | 0.06% |
| **TRIK. (Trikāṇḍaśeṣa)** | **0.00%** | **4.99%** | **0.03%** | 0.01% |
| **HALĀY. (Halāyudha)** | **0.00%** | **3.46%** | **0.01%** | 0.00% |
| ŚBr. (Śatapatha) | 2.31% | 4.75% | 0.67% | 0.00% |
| Suśr. (medical) | 2.13% | 5.59% | 0.36% | 0.20% |
| Mn. (Manu) | 2.33% | 5.14% | 0.30% | 0.63% |
| **L. (Lexicographers)** | **13.95%** | **0.00%** | **0.01%** | **0.42%** |

**Visual story — the killer finding:** Compare the five **bold** kosha-source rows. PWG cites Hemacandra in **12.18% of entries**, Amarakośa in **8.35%**, Medinīkośa in **4.20%**, *Trikāṇḍaśeṣa* in **4.99%**, Halāyudha in **3.46%**. **PWK abandoned all of them** — coverage dropped to 0.01–0.59%. **MW dropped them entirely** (0.00–0.08%) and **introduced `L.` at 13.95%** as a single consolidated hedge. The Sankey at Tier 1 #2 visualises this exact transition.

**What this proves:**
- PWG → PWK transition: Böhtlingk's *own* abridgement dropped the kosha apparatus when condensing his work.
- PWK → MW (chronologically and editorially): MW restored an evidentiary-hedge in the form of `L.` at 13.95% — *more thorough than PWK's silence* but with *one label instead of PWG's named koshas*.
- AP independently has **near-zero kosha citations and minimal L.** (0.42%) — Apte's dictionary descends from a different editorial tradition again.

**What it obscures:** Doesn't show **how often** within a single entry the source is cited (an entry citing RV. five times still counts as "1 entry citing RV.").

**When to use:** When the question is **editorial policy** — does this dictionary use kosha sources at all? **This is the recommended normalisation for the lineage Sankey** (Tier 1 #2), and the table above is its data source.

#### Option G — Z-score / cross-dict standardisation

Normalise each metric per-dictionary to mean 0, sd 1 across the comparison set.

**Visual story:** Pure patterns visible: "PWG is +1.8 SD above mean on `<ls>` density, WIL is −1.2 SD." Removes scale entirely.

**What it obscures:** All interpretability of the actual numbers. A reader cannot say "PWG has X cites/entry" without recovering raw data.

**When to use:** In a **multi-metric small-multiples chart** where the goal is to show patterns across 5–6 dimensions at once. The microstructure fingerprint visualisation (Tier 2 #7) is the natural use.

#### Recommendation — multi-normalisation strategy

**No single normalisation is correct.** Use different normalisations for different visualisations, and label each chart's normalisation choice prominently in the caption. Recommended mapping:

| Visualisation | Normalisation | Rationale |
|---|---|---|
| Multi-bar size comparison (Tier 1 #4 treemap, [3.1] multi-bar) | **A — Raw counts** | Establishes scale; honest about MW's size |
| Citation-density per dict (any density chart) | **B — Per-entry** | Reveals editorial citation choice |
| Lineage Sankey (Tier 1 #2) | **F — Coverage %** | Direct editorial-policy comparison |
| Microstructure fingerprints (Tier 2 #7) | **G — Z-score** | Pure pattern visibility |
| Per-headword density argument | **C — Per-headword** or **E — Per-unique-k1** | When discussing lemma inventory choice |

Each figure caption must state: "*Normalisation: [letter] — [one-line description]*" so readers can interpret the chart correctly.

### Decision 5 — Attribution: cite the digital edition

**All figures cite "CDSL `mw.txt` 2026-05-23"** as the data source. If a journal requires citing the print original (MW 1899), the figures can be regenerated against the print at that point. The data source citation goes in each figure caption as a footer.

**Implementation:** every static figure carries a small grey footer text:

```
Source: CDSL mw.txt 2026-05-23 · github.com/sanskrit-lexicon/csl-orig

```

The interactive microsite carries the same attribution in a persistent footer.

---

## Implementation decisions — round 2 (2026-05-23)

Four follow-up questions raised by the first round have been resolved:

### Decision 6 — Sanskrit-in-Russian rendering: IAST in italics

When Sanskrit terms appear inside Russian-language text or labels, they are rendered in **IAST in italics** (e.g. *aṃśa*, *kaṣāya*, *ṛṣi*) — exactly as in the English text. No Cyrillic transliteration layer, no Devanagari.

**Implementation:**
- Translation strings in `papers/microanalysis/figures/locales/ru.json` carry IAST tokens as inline `<em>` or Markdown italic.
- The locale switcher does **not** transcode Sanskrit; only the surrounding English/Russian prose changes.
- This is the **standard Russian indological convention** (used in *Индоевропейское языкознание*, the Roerich/Zograf Readings, *Petersburg Indological Studies*, etc.) — clean, no transcoding burden.

### Decision 7 — Microsite hosting: new repo `csl-atlas`

The interactive microsite lives in a **new repository** (working name `csl-atlas`) under the `sanskrit-lexicon` org, rather than embedded in the MWS repo. Rationale:

- The microsite covers (will cover) **multiple CDSL dictionaries** for Phase 4 — natural to give it its own home.
- Hosted on GitHub Pages from `csl-atlas` → e.g. `sanskrit-lexicon.github.io/csl-atlas/`.
- Pulls data via JSON files in `csl-atlas/data/` regenerated from each dict's `mw_block_matrix.py` equivalent.
- Versioned independently from any single dict's docs-pass.
- Allows a clean separation: **MWS repo holds the static paper + the data scripts; csl-atlas holds the live web app.**

### Decision 8 — Mermaid i18n: one file per locale, not parallel blocks

For Mermaid diagrams that need bilingual rendering (timeline, lineage forest), the strategy is **one .md file per locale**, not two Mermaid blocks in a single file.

Concrete file layout:

```
papers/microanalysis/figures/
  timeline-en.md         <-- single Mermaid block, English labels
  timeline-ru.md         <-- single Mermaid block, Russian labels
  lineage-forest-en.md   <-- ditto
  lineage-forest-ru.md

```

Each file is self-contained Markdown with a single Mermaid code-fence. GitHub renders both natively. Cross-linking between English/Russian variants is via plain Markdown `[Русская версия](figures/timeline-ru.md)` / `[English version](figures/timeline-en.md)`.

**Rationale (vs the alternative parallel-blocks approach):**
- Cleaner: each file presents the diagram in one language only — no visual clutter.
- Linkable: each locale gets its own canonical URL.
- Maintenance burden is the same (two file updates per diagram change) but the source is more readable.
- Friendly to a future build step that generates `timeline-{locale}.md` from a single source data file + locale-specific label lookup.

### Decision 9 — CSS palette: JSON-first design tokens

Single source of truth: `papers/microanalysis/figures/palette-tokens.json`. A build step generates downstream artifacts:

```
palette-tokens.json   ← THE source of truth
       │
       ├──→  palette.css            (CSS custom properties for HTML/SVG)
       ├──→  mermaid-theme.json     (consumed by Mermaid)
       ├──→  palette.py             (Python module, importable for matplotlib)
       └──→  palette.tex            (LaTeX colour definitions, for paper figures)

```

**Token structure:**

```json
{
  "article-type": {
    "root":        "#7a3d8f",
    "noun-m":      "#1f78b4",
    "noun-f":      "#e31a1c",
    "noun-n":      "#33a02c",
    "noun-mn":     "#6a3d9a",
    "adjective-mfn": "#ff7f00",
    "indeclinable":  "#b15928",
    "compound":      "#a6cee3",
    "derived":       "#b2df8a",
    "continuation":  "#fb9a99",
    "lexicographer-only": "#fdbf6f",
    "etymological-ie":    "#cab2d6",
    "botanical":     "#90ee90",
    "biographical":  "#dda0dd",
    "vedic-accented": "#ffd700",
    "other":         "#888888"
  },
  "semantic-block": {
    "identity":    "#...",
    "form":        "#...",
    "grammar":     "#...",
    "etymology":   "#...",
    "sense":       "#...",
    "evidentiary": "#...",
    "encyclopedic": "#...",
    "discourse":   "#..."
  },
  "fullness-tier": {
    "T1-vestigial":  "#cccccc",
    "T2-skeletal":   "#a0c4e8",
    "T3-typical":    "#5b8cd6",
    "T4-rich":       "#3d6cb0",
    "T5-elaborate":  "#1f4e8f"
  },
  "chart-element": {
    "background":  "#fafafa",
    "grid":        "#eaeaea",
    "axis":        "#333333",
    "text":        "#222222",
    "muted":       "#666666"
  },
  "_meta": {
    "wcag-checked": true,
    "colour-blind-safe": true,
    "source": "ColorBrewer 2.0 paired qualitative + manual additions for fullness tiers",
    "last-updated": "2026-05-23"
  }
}

```

The **colour-blind-safe** flag is important: at least one downstream variant of `palette.css` should be designed for deuteranopia/protanopia. We bake this commitment into the design-token spec from the start.

**Build tool:** A simple Python script (`build_palette.py`) reads `palette-tokens.json` and writes the four downstream artifacts. No need for [Style Dictionary](https://amzn.github.io/style-dictionary/) or similar — overkill for ~30 colour tokens.

---

## Implementation decisions — round 3 (2026-05-23)

### Decision 10 — Microsite stack: Observable Framework

The interactive `csl-atlas` is built with [**Observable Framework**](https://observablehq.com/framework). Rationale:
- Built-in i18n routing (one route per locale → matches Decision 8's per-locale file strategy).
- Reactive data + D3 + Markdown pages, all out of the box.
- Static-site output (HTML/JS) deployable to GitHub Pages.
- First-class support for declarative data files (CSV/JSON) → matches our JSON-data architecture.
- Polished defaults; research-microsite aesthetic.

Setup will live in the new `csl-atlas` repo (Decision 7).

### Decision 11 — Russian translations: bootstrap-and-correct

Russian labels are produced by **bootstrap-from-academic-Russian-indological-terminology**, then reviewed by [@gasyoun](https://github.com/gasyoun). The terminology base draws on standard Russian indological references: Andrey Zaliznyak's grammatical terminology, established conventions from *Индоевропейское языкознание*, *Petersburg Indological Studies*, the Zograf/Roerich Readings. Sample bootstrap mapping (subject to your review):

| English | Russian (bootstrap) | Confidence |
|---|---|---|
| Verbal root | глагольный корень | high |
| Masculine noun | существительное мужского рода | high |
| Feminine noun | существительное женского рода | high |
| Neuter noun | существительное среднего рода | high |
| Adjective (mfn.) | прилагательное (mfn.) | high |
| Indeclinable | неизменяемое слово | high |
| Compound | сложное слово / композит | medium |
| Derived form | производное / дериват | high |
| Continuation sense | продолжение значения | medium |
| Lexicographer-only | лексикограф-only | low (calque; user may prefer ‹только в индийских кошах›) |
| IE-etymological | индоевропейское этимологическое | high |
| Botanical | ботанический | high |
| Biographical | биографический / именной | medium |
| Vedic accented | ведийское с ударением | medium |
| Block | блок | high |
| Slot | позиция / слот | medium |
| Profile | профиль | high |
| Hedge | ограничитель | medium |
| Infrastructure | инфраструктура | high |

Edge cases flagged with `(?)` in `locales/ru.json` for [@gasyoun](https://github.com/gasyoun)'s correction.

### Decision 12 — Build order: foundation → 4 Tier-1 figures in dependency order

1. **Foundation** — `palette-tokens.json` + `build_palette.py` + `locales/{en,ru}.json` + data JSON exports
2. **Heatmap** (depends on tokens + locales)
3. **Treemap** (depends on tokens + locales)
4. **Sankey** (depends on data prep — kosha collapse data)
5. **Mermaid timeline** (zero new dependencies)
6. README updates + commit

**Total target effort: 1–2 hours.**

---

## Implementation decisions — round 4 (2026-05-23)

### Decision 13 — Legend strategy: hover + brief inset + caption-key

- **Interactive microsite:** legend appears on hover; full key accessible via toggle.
- **Static SVG figures:** brief inset (≤ 5 entries) with note "see full key in caption."
- **Caption:** carries the complete colour key as a structured legend block.

Lets static figures keep plot-space while remaining self-explanatory; interactive variant provides full richness.

### Decision 14 — Accessibility: triple coverage

Every figure carries:

1. **Short `alt` text** (~100 characters) — chart type + the single key takeaway. For screen readers, first contact.
2. **Long SVG `<desc>` element** — full description (~300–500 chars) embedded inside the SVG. Screen readers can navigate inside the figure.
3. **Long caption** — printed text alongside the figure with the full narrative + colour key + data-source citation.

Aligns with the [W3C SVG accessibility spec](https://www.w3.org/TR/SVG2/struct.html#DescriptionAndTitleElements) and IJL's standard accessibility checklist.

### Decision 15 — Figure numbering: single continuous sequence

Now that the study is **one paper** ([PAPER.md](PAPER.md)), figures are numbered in a single continuous sequence (Fig 1, Fig 2, …) across the body and the appendices — appendix figures may carry an `A`/`B`/`C` prefix (Fig A1, Fig B1) per the standard journal convention. Earlier drafts numbered per-paper; that convention is retired with the consolidation ([DOUBTS.md D4](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking)).

A separate **stable figure-ID manifest** (`papers/microanalysis/figures/manifest.json`) maps each figure's slug → its number. This survives reviewer-driven renumbering.

### Decision 16 — Supplementary materials: self-contained ZIP

The IJL submission includes a single ZIP archive `mw-microanalysis-supplementary.zip` containing:

```
supplementary/
  README.md                   <-- entry point
  paper/                      <-- PAPER.md (PDF + markdown source)
  data/                       <-- JSON dumps of the block matrix, citation stats, etc.
  figures/                    <-- all static SVG figures + PNG fallbacks
  scripts/                    <-- Python reproducibility code: mw_block_matrix.py,
                                   build_palette.py, render_heatmap.py, etc.
  microsite-static-export/    <-- offline-renderable HTML export of the live microsite
  LICENSE                     <-- CC-BY-SA-4.0 (matching the MWS digital edition)

```

**No external dependencies.** A reviewer with the ZIP, Python 3, and a modern browser can reproduce every figure and explore every visualisation offline. Survives URL rot, microsite outages, and post-submission infrastructure changes.

---

## All sixteen decisions in one table

| # | Decision | Choice |
|--:|---|---|
| 1 | Colour palette consistency | Shared via CSS across the paper + microsite |
| 2 | Static vs interactive | Both |
| 3 | Bilingual labels | English + Russian |
| 4 | Cross-dict normalisation | Multi-strategy; per-figure caption |
| 5 | Author attribution | "CDSL `mw.txt` 2026-05-23" |
| 6 | Sanskrit-in-Russian | IAST in italics |
| 7 | Microsite hosting | New repo `csl-atlas` |
| 8 | Mermaid i18n | One file per locale |
| 9 | CSS palette structure | JSON-first design tokens |
| 10 | Microsite stack | Observable Framework |
| 11 | Russian translations | Bootstrap-and-correct |
| 12 | Build order | Foundation → heatmap → treemap → Sankey → Mermaid |
| **13** | Legends | Hover (interactive) + brief inset (static) + caption key |
| **14** | Accessibility | Short alt + long `<desc>` + long caption (triple) |
| **15** | Figure numbering | Per-paper continuous + stable-slug manifest |
| **16** | Supplementary materials | Self-contained ZIP (no external deps) |
| **17** | Figure dimensions | IJL full-page-width (~175 mm) |
| **18** | Font | Noto Sans (Google universal; supports IAST + Cyrillic) |
| **19** | Figure license | CC-BY-SA-4.0 (inherits from MWS digital edition) |
| **20** | Microsite navigation | Hybrid: paper tours + standalone tools |
| **21** | Heatmap layout | Blocks on Y, types on X with horizontal short-code labels |
| **22** | Sankey structure | Three-stage: PWG `<ls>` → named-kosha works → MW `L.` |
| **23** | Citation style | Hybrid: Harvard for papers + DOI links for online resources |
| **24** | Microsite name | **csl-atlas** — "Atlas of the Cologne Digital Sanskrit Lexicons" |
| **25** | Default locale | English canonical (`/` = EN, `/ru/` = Russian) |
| **26** | Footer style | Small grey 7pt italic, bottom-right corner |
| **27** | CI/CD | GitHub Actions on push to main |
| **28** | Figure versioning | Git short SHA + build date in footer |

## Implementation decisions — round 7 (2026-05-23)

### Decision 25 — Default locale: English canonical

URL structure:
- `csl-atlas` root (`https://sanskrit-lexicon.github.io/csl-atlas/`) = English content
- `/ru/` prefix for Russian variants
- Language switcher in nav: `EN | RU` toggle, persists in localStorage
- `hreflang` tags in `<head>` for SEO

Sample paths:

```
/                        landing (EN)
/tools/heatmap           18×14 matrix explorer (EN)
/tools/lineage-sankey    PWG→MW Sankey (EN)
/papers/wiegand          Wiegand paper page (EN)
/ru/                     landing (RU)
/ru/tools/heatmap        18×14 matrix explorer (RU)
/ru/papers/wiegand       (RU translation if available; else EN with banner)

```

### Decision 26 — Footer style: 7pt grey, bottom-right

Exact footer text format:

```
Source: CDSL mw.txt 2026-05-23 · CC-BY-SA-4.0 · build {SHA}

```

- Font: Noto Sans Italic, 7pt
- Colour: `--mw-color-muted` (#666666 in the default palette)
- Position: bottom-right corner of every figure (SVG group with `text-anchor="end"` at `(width-10, height-10)`)
- For Mermaid diagrams: appended as a comment below the diagram block (Mermaid doesn't allow arbitrary text positioning)

### Decision 27 — CI/CD: GitHub Actions on push to main

`.github/workflows/build-and-deploy.yml` in `csl-atlas` repo:
1. Trigger on push to `main`
2. Set up Node + npm
3. Run `npm ci && npm run build`
4. Deploy `dist/` to GitHub Pages via `actions/deploy-pages`

A separate workflow handles data refreshes:
- `data-refresh.yml` — manual trigger only (or cron monthly)
- Re-downloads mw.txt, re-runs `mw_block_matrix.py`, regenerates JSON data files in `data/`, commits to main; the regular build-and-deploy then picks it up.

### Decision 28 — Figure versioning: SHA + date in footer

The footer text incorporates both:

```
Source: CDSL mw.txt 2026-05-23 · CC-BY-SA-4.0 · build 2e6b23a

```

The SHA is the **commit SHA at which the figure was last rendered** (injected at build time via the GitHub Action). A reviewer can `git show 2e6b23a` to see the exact code that produced the figure. Date is the human-readable companion.

For Mermaid diagrams (which can't carry a build SHA from the GitHub Action), the SHA is omitted; only the date appears.

## Implementation decisions — round 6 (2026-05-23)

### Decision 21 — Heatmap: blocks on Y, types on X, short codes

The 18 × 14 matrix lays out as:
- **Y-axis (vertical, 18 rows):** the formal blocks F01–F18, full names (room for "F12 Source citation" etc.).
- **X-axis (horizontal, 14 columns):** article types as **short codes** rendered horizontally — no rotation needed.

Short-code mapping for X-axis (to be confirmed):
| Article type | Short code |
|---|:---:|
| root | `root` |
| noun_m | `n.m` |
| noun_f | `n.f` |
| noun_n | `n.n` |
| noun_mn | `n.mn` |
| adjective_mfn | `adj` |
| indeclinable | `ind` |
| compound | `comp` |
| derived | `deriv` |
| continuation | `cont` |
| lexicographer_only | `lex.` |
| etymological_ie | `IE.et` |
| botanical | `bot` |
| biographical | `bio` |
| vedic_accented | `V.acc` |
| other | `oth` |

The short codes are defined once in `locales/en.json` and `locales/ru.json` (with Russian variants), and a key block in each figure caption.

### Decision 22 — Sankey: three-stage flow

Stage 1 (leftmost) — **PWG `<ls>` indicators** (6 nodes):
- `H.` 17,337 cites
- `AK.` 14,473
- `MED.` 13,055
- `H. an.` 9,771
- `TRIK.` 8,365
- `HALĀY.` 5,114

Stage 2 (middle) — **the actual kosha works** (6 nodes, with IAST italic):
- *Abhidhānacintāmaṇi* (Hemacandra)
- *Amarakośa*
- *Medinīkośa*
- *Anekārthasaṃgraha* (Hemacandra)
- *Trikāṇḍaśeṣa*
- *Abhidhānaratnamālā* (Halāyudha)

Stage 3 (rightmost) — **MW `<ls>L.</ls>`** (1 node, bold): 40,213 cites

All six PWG flows merge in stage 2 (named work) and then *collapse* into the single MW `L.` node. Visually: six narrow ribbons on the left → six labelled intermediate columns → six ribbons re-merging into one fat ribbon on the right.

Plus, where data is available, the four CDSL koshas ([ARMH](https://github.com/sanskrit-lexicon/armh), [ABCH](https://github.com/sanskrit-lexicon/abch), [ACPH](https://github.com/sanskrit-lexicon/acph), [ACSJ](https://github.com/sanskrit-lexicon/acsj)) are annotated against their corresponding stage-2 nodes (ARMH ↔ Halāyudha, ABCH ↔ Hemacandra's Abhidhānacintāmaṇi).

This makes the Sankey **both quantitative and bibliographic** — a single figure that shows the citation flow AND identifies the named koshas with their CDSL repos.

### Decision 23 — Citation style: Harvard + inline online DOIs

Print references in the paper use **author-date Harvard** for inline citations and an alphabetised reference list at paper end. Online resources (GitHub repos, archive.org scans, Wikipedia, CDSL web display) get **inline Markdown link** in the running text, not a separate reference-list entry, since URLs would clutter the references and DOI/URL provides direct access.

Reference list entries get DOIs where they exist (e.g. Wiegand 1989 has a DOI in the HSK reprint).

### Decision 24 — Microsite name: **csl-atlas**

Repo: `csl-atlas` under sanskrit-lexicon org. Full name: **"Atlas of the Cologne Digital Sanskrit Lexicons."** Tagline alternatives (TBD):
- "A comparative microstructural atlas of the CDSL corpus"
- "Mapping nine Sanskrit dictionaries from microstructure to lineage"
- "An interactive companion to the CDSL"

The "atlas" framing signals broader-than-MW Phase-4 ambition: the atlas covers MW + PWG + AP + WIL + SKD + ARMH + ABCH + ACPH + ACSJ (9 dicts). Each dictionary gets a chapter; each Tier-1 figure has a *per-dictionary* and a *comparative* variant.

## Implementation decisions — round 5 (2026-05-23)

### Decision 17 — Figure dimensions: full-page-width

All four Tier-1 figures render at **IJL full-page-width (~175 mm)** spanning both columns. Rationale:

- The 18 × 14 block × type heatmap is unreadable at single-column width — needs the room.
- The PWG → MW Sankey has 6 source nodes flowing to 1 destination; clearer at full-width.
- The article-type treemap with 14 cells reads better wide.
- The Mermaid timeline benefits from horizontal space for the kosha → MW → CDSL timespan.

Implementation in matplotlib: `figsize=(7, 4.5)` inches at 300 DPI for paper; SVG export for vectorisation.

### Decision 18 — Font: Noto Sans

**[Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans)** for all figure text. Rationale:

- Universal Unicode coverage: IAST diacritics (ā, ī, ū, ṛ, ṅ, ñ, ṭ, ḍ, ṇ, ś, ṣ, ḥ, ṃ) AND Cyrillic AND Devanagari (for any rare callouts).
- Open license (SIL OFL); ships with every modern OS.
- Designed by Google to harmonise across scripts — bilingual labels read consistently.
- Falls back gracefully if missing (DejaVu Sans is the matplotlib default).

Embedded in `palette-tokens.json` as `"font-family": "Noto Sans"`.

### Decision 19 — License: CC-BY-SA-4.0

All figures, data dumps, and the microsite are released under [**CC-BY-SA-4.0**](https://creativecommons.org/licenses/by-sa/4.0/), matching the [MWS digital edition's license](../../LICENSE). Rationale:

- Consistency across CDSL artefacts.
- Attribution + share-alike is the long-established CDSL norm.
- A note in each figure caption: "Released under [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) · Source: CDSL mw.txt 2026-05-23"

### Decision 20 — Microsite nav: hybrid (paper-tours + standalone tools)

Observable Framework structure:

```
csl-atlas/
  src/
    index.md                        <-- landing page
    papers/                         <-- paper-tour section
      wiegand.md                    <-- Wiegand paper figures embedded
      atkins-rundell.md
      hausmann.md
      grounded.md
    tools/                          <-- standalone visualisation tools
      matrix-explorer.md            <-- 18×14 heatmap, interactive
      lineage-sankey.md             <-- PWG→MW Sankey
      typology-treemap.md           <-- article-type treemap
      timeline.md                   <-- lexicographic timeline
      type-comparator.md            <-- Tier 3, side-by-side type compare
      citation-tracer.md            <-- Tier 3, click-source-see-entries
    data/                           <-- JSON data shared across pages
    locales/
      en/                           <-- English locale routes
      ru/                           <-- Russian locale routes

```

Reader paths:
- **Paper tour** for "I want to follow the argument of one framework paper."
- **Tools** for "I want to explore the data interactively without the paper context."

Both share the same underlying data + palette + locale strings.

---

## All twenty decisions in one table

| # | Decision | Choice |
|--:|---|---|
| 1 | Colour palette consistency | Shared via CSS across the paper + microsite |
| 2 | Static vs interactive | Both |
| 3 | Bilingual labels | English + Russian |
| 4 | Cross-dict normalisation | Multi-strategy; per-figure caption |
| 5 | Author attribution | "CDSL `mw.txt` 2026-05-23" |
| 6 | Sanskrit-in-Russian | IAST in italics |
| 7 | Microsite hosting | New repo `csl-atlas` |
| 8 | Mermaid i18n | One file per locale |
| 9 | CSS palette structure | JSON-first design tokens |
| 10 | Microsite stack | Observable Framework |
| 11 | Russian translations | Bootstrap-and-correct |
| 12 | Build order | Foundation → heatmap → treemap → Sankey → Mermaid |
| 13 | Legends | Hover (interactive) + brief inset (static) + caption key |
| 14 | Accessibility | Short alt + long `<desc>` + long caption |
| 15 | Figure numbering | Per-paper continuous + stable-slug manifest |
| 16 | Supplementary materials | Self-contained ZIP (no external deps) |
| 17 | Figure dimensions | IJL full-page-width (~175 mm) |
| 18 | Font | Noto Sans (universal IAST + Cyrillic) |
| 19 | Figure license | CC-BY-SA-4.0 |
| 20 | Microsite navigation | Hybrid: paper tours + standalone tools |

---

## Status

This document is the **planning catalogue**. None of the visualisations listed are yet built. Tier-1 (4 figures) is the recommended next step. The Python data is already in [MICROANALYSIS.md](MICROANALYSIS.md) and the working scripts are at [`mw_block_matrix.py`](MICROANALYSIS.md) (regenerable in seconds against any updated mw.txt).

When figures are built, they should land in `papers/microanalysis/figures/` (created on first commit) and be referenced from both MICROANALYSIS.md and the [paper](PAPER.md), plus DICT_PROFILE.md where they support the cross-dict and lineage sections.
