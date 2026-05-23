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

## Design decisions (2026-05-23)

Five open questions raised in the original draft of this document have been resolved by [@gasyoun](https://github.com/gasyoun). Decisions:

### Decision 1 — Shared colour palette via CSS

**All four framework papers + the interactive microsite use the same colour palette for the 14 article types.** Implementation: **via CSS** (custom properties / design tokens), so that a single source-of-truth defines colours that flow through (a) the static SVG figures generated for the paper, (b) the Mermaid diagrams embedded in markdown docs, and (c) the interactive microsite.

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
- Hosting target: TBD — see [follow-up questions](#follow-up-questions-2026-05-23) below.

### Decision 3 — Bilingual labels: English + Russian

**Bilingual labels in English and Russian** — not Sanskrit. Sanskrit is the meta-level (the language being described, not a label language used to describe). Russian is the second target audience: some findings additional to the English journals will be published in Russian-language venues.

**Implications:**
- All visualisation labels exist in two locale strings: `en` and `ru`.
- Labels live in a JSON file (`papers/microanalysis/figures/locales/`) — `en.json` and `ru.json` — keyed by an i18n identifier.
- Static renderer (Python) accepts a locale flag and emits the right strings.
- Interactive microsite has a locale-switcher control.
- Sanskrit terms (lemmas, abbreviations, tag names) are preserved in their conventional rendering (IAST in italic, SLP1 in code blocks); they are not translated, only the surrounding labels are.

The exact convention for how Sanskrit terms appear inside Russian text is a [follow-up question](#follow-up-questions-2026-05-23) below.

### Decision 4 — Cross-dictionary normalisation: detailed analysis

The choice of normalisation strategy materially affects what the visualisations *say*. Per [@gasyoun](https://github.com/gasyoun)'s request, here are the seven approaches with their numerical and visual implications:

#### Option A — Raw absolute counts (no normalisation)

| Dict | Entries | `<ls>` tags | Kosha cites named |
|---|--:|--:|--:|
| MW | 286,561 | 312,159 | 209 (`Amar.` only) |
| PWG | 123,366 | 571,152 | 68,730+ |
| AP | 90,654 | ~50,000 (TBD) | TBD |
| WIL | 44,577 | 230 | 0 (kosha-derived, no `<ls>`) |
| SKD | 42,531 | TBD | (different format) |

**Visual story this tells:** "MW is the largest single-volume dictionary, but PWG is more citation-dense overall."

**What it obscures:** PWG's density is partly an artifact of having no `L.` hedge — PWG distributes its citations across 821 named sources where MW collapses to 1. **Raw counts make PWG look more rigorous than it is**, by hiding the fact that 12.9% of MW's apparently-thinner citation apparatus IS the kosha attribution PWG names separately.

**When to use:** Whenever absolute scale is the message — e.g. "MW is the standard reference because of its size."

#### Option B — Per-entry normalisation (cites/entry, blocks/entry)

| Dict | `<ls>` cites/entry | Blocks/entry (avg) |
|---|--:|--:|
| MW | 1.09 | 6.1 |
| PWG | **4.63** | ~7–8 (estimate) |
| AP | ~0.55 (estimate) | ~5 |
| WIL | 0.005 | 5–6 |
| SKD | n/a (different cite format) | — |

**Visual story:** "PWG is 4× more citation-dense per entry than MW; WIL has essentially zero textual citations per entry."

**What it obscures:** Penalises MW for having many `<e>3` compound sub-entries that don't *need* citations. MW's 126K compounds inflate the denominator without diluting the citation effort — what matters editorially is *coverage of citations among entries that need them*, not the raw ratio.

**When to use:** When the comparison is **about editorial citation density** — does this dictionary prefer 1 cite or 10 cites for the same word?

#### Option C — Per-headword normalisation (top-level entries only, `<e>1`)

Excluding sub-entries (continuations, derivatives, compounds), counting only top-level lemmas:

| Dict | Top-level | Top-level / total | `<ls>` cites/top-level entry |
|---|--:|--:|--:|
| MW | 32,116 | 11.2% | ~9.7 |
| PWG | ~45,000 (estimate) | ~36.5% | ~12.7 |
| AP | ~13,000 (estimate) | ~14% | ~3.8 |
| WIL | ~9,000 (estimate) | ~20% | ~0.026 |

**Visual story:** "MW has only 32K main lemmas — fewer than PWG. The bulk of MW is sub-entries."

**What it obscures:** PWG and MW segment their data differently. PWG often runs compounds in the main article body (no separate `<L>` record); MW always splits them. Comparing *just* top-level entries punishes MW's structural choice.

**When to use:** When comparing the **lemma inventory choice** — what counts as a "word" in this dictionary?

#### Option D — Per-million-words normalisation (text-volume normalised)

| Dict | Approx word count | Cites / 10⁶ words | Bytes (raw) |
|---|--:|--:|--:|
| MW | ~1.4M | ~223K | 49 MB |
| PWG | ~1.5M | **~381K** | 53 MB |
| AP | ~500K | ~100K | 18 MB |
| WIL | ~280K | ~0.8K | 10 MB |
| SKD | ~600K | n/a | 22 MB |

**Visual story:** "PWG packs more citation per unit of text than any other CDSL dictionary."

**What it obscures:** Heavy compound enumeration in MW inflates word count via the gloss text. Doesn't disentangle "citation density" from "verbose definitions." A dictionary that gives 5-word glosses but cites RV/MBh systematically will look denser than one with 25-word glosses and one general cite.

**When to use:** When comparing the **textual artifacts as artifacts** — how much content fits in how many pages? Useful for arguments about print economy.

#### Option E — Per-unique-headword normalisation (deduplicated `<k1>`)

Counts unique `<k1>` SLP1-form values, ignoring homophone numbering:

| Dict | Unique `<k1>` | `<ls>` per unique headword |
|---|--:|--:|
| MW | ~210,000 (estimate) | ~1.49 |
| PWG | ~95,000 (estimate) | ~6.01 |
| AP | ~75,000 (estimate) | ~0.67 |
| WIL | ~35,000 (estimate) | ~0.007 |

**Visual story:** Similar to Option B but rescued from compound-bloat (no double-counting of homophone groups).

**What it obscures:** Different dicts have different homophone-numbering conventions; standardising requires per-dict adjustment.

**When to use:** When you want the **truest "per-word" comparison** — but it's expensive to compute properly.

#### Option F — Coverage normalisation (% of entries citing X)

For each source X, what fraction of the dictionary's entries cite X at all?

| Source | MW (% entries citing) | PWG | WIL |
|---|--:|--:|--:|
| RV. (Rigveda) | 5.6% | 12.0% | 0% |
| MBh. | 9.8% | 13.7% | 0% |
| Hemacandra (`H.`) | 0% | 14.0% | 0% (in `<ls>`) |
| Amarakośa | 0.07% (`Amar.`) | 11.7% (`AK.`) | 0% |
| Lexicographers (`L.`) | 13.4% | 0% | 0% |

**Visual story:** Direct comparison of **editorial policy**. PWG cites Hemacandra in 14% of entries; MW cites it in 0% of entries (collapsed to L.). This is the **most informative** view for the lineage argument.

**What it obscures:** Doesn't show **how often** within an entry the source is cited — just whether at all. A source cited 10 times in one entry and 1 time in 99 others would have 100% coverage in this metric.

**When to use:** When the question is **editorial choice** — does this dictionary include kosha sources in its citation system at all?

**This is the recommended normalisation for the lineage Sankey** (Tier 1 #2).

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

### Decision 7 — Microsite hosting: new repo `csl-microsite`

The interactive microsite lives in a **new repository** (working name `csl-microsite`) under the `sanskrit-lexicon` org, rather than embedded in the MWS repo. Rationale:

- The microsite covers (will cover) **multiple CDSL dictionaries** for Phase 4 — natural to give it its own home.
- Hosted on GitHub Pages from `csl-microsite` → e.g. `sanskrit-lexicon.github.io/csl-microsite/`.
- Pulls data via JSON files in `csl-microsite/data/` regenerated from each dict's `mw_block_matrix.py` equivalent.
- Versioned independently from any single dict's docs-pass.
- Allows a clean separation: **MWS repo holds the static paper + the data scripts; csl-microsite holds the live web app.**

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

Each file is self-contained Markdown with a single Mermaid code-fence. GitHub renders both natively. Cross-linking between English/Russian variants is via plain Markdown `[Русская версия](timeline-ru.md)` / `[English version](timeline-en.md)`.

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

## Implementation decisions — round 3

Three follow-up questions remain before any figure can be built. See the next message for the explicit AskUserQuestion call.

---

## Status

This document is the **planning catalogue**. None of the visualisations listed are yet built. Tier-1 (4 figures) is the recommended next step. The Python data is already in [MICROANALYSIS.md](MICROANALYSIS.md) and the working scripts are at [`mw_block_matrix.py`](MICROANALYSIS.md) (regenerable in seconds against any updated mw.txt).

When figures are built, they should land in `papers/microanalysis/figures/` (created on first commit) and be referenced from both MICROANALYSIS.md and the four framework papers, plus DICT_PROFILE.md where they support the cross-dict and lineage sections.
