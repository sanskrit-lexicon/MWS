# HANDOFF — MW1899 microanalysis + csl-atlas

**Purpose:** let a fresh Claude session pick up this work without losing context.
**Author:** Claude Opus 4.7, on behalf of @gasyoun. Last updated **2026-05-24** (after the empirical-audit pass).

This document is **self-contained** — read it (and follow the links) before doing any new work. The full conversation history is multi-day; this file is the executive summary.

---

## 1. Five-line orientation

The Cologne Digital Sanskrit Lexicon (CDSL) project, sanskrit-lexicon org on GitHub, runs an org-wide **docs-pass** across ~76 repos to standardise documentation. The MWS (Monier-Williams) docs-pass is the flagship pilot, completed and reviewable via [issue #195](https://github.com/sanskrit-lexicon/MWS/issues/195). On top of that, we built a [**microanalysis** of MW1899's microstructure](README.md) (286,561 records, 18 formal blocks, 14 article types, 28 design decisions) — originally four parallel framework papers, **now consolidated into a single paper** ([PAPER.md](PAPER.md), per [D4](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking)): a data-grounded body + three condensed framework appendices — plus a [visualisation catalogue](VISUALISATIONS.md), six [Tier-1 + cross-dict figures](figures/), and a full [empirical-audit suite](analysis/) that has now resolved or substantially advanced the analytical doubts D1, D2, D6, D7. The next strategic phase is [**csl-atlas**](decisions/MICROSITE.md) — a 9-dict **Observable Framework** microsite (stack confirmed per [D8](DOUBTS.md#d8--observable-framework-is-heavy-infrastructure-for-a-research-microsite--blocking)) covering MW + PWG + AP + WIL + SKD + ARMH + ABCH + ACPH + ACSJ + VCP + PWK.

---

## 2. What exists right now (state as of HEAD = `1f8090c`)

### docs-pass branches (5 pilot repos, reviewable)

| Repo | Issue | Branch | Status |
|---|---|---|---|
| [MWS](https://github.com/sanskrit-lexicon/MWS) | [#195](https://github.com/sanskrit-lexicon/MWS/issues/195) | [docs-pass](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass) | Flagship; reviewable |
| [csl-sqlite](https://github.com/sanskrit-lexicon/csl-sqlite) | [#1](https://github.com/sanskrit-lexicon/csl-sqlite/issues/1) | docs-pass | Reviewable |
| [csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect) | [#15](https://github.com/sanskrit-lexicon/csl-inflect/issues/15) | docs-pass | Reviewable |
| [hwnorm1](https://github.com/sanskrit-lexicon/hwnorm1) | [#20](https://github.com/sanskrit-lexicon/hwnorm1/issues/20) | docs-pass | Reviewable |
| [COLOGNE](https://github.com/sanskrit-lexicon/COLOGNE) | [#455](https://github.com/sanskrit-lexicon/COLOGNE/issues/455) | docs-pass | Reviewable |

### MWS docs-pass branch — files (all under [`docs-pass`](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass))

| File | Purpose |
|---|---|
| [DICT_PROFILE.md](../../DICT_PROFILE.md) | Reader-facing profile of MW. Contains: At-a-Glance, Orthographical conventions, Historical background, Scholarly significance, When to use (with [14-row article typology](../../DICT_PROFILE.md#article-types--what-youll-encounter) + [citation markers callout](../../DICT_PROFILE.md#citation-markers--not-all-are-literary-works)), Relationship to other CDSL dicts, [Beyond PWG analysis](../../DICT_PROFILE.md#beyond-pwg--what-mw-contributes), [Same entry across 7 dictionaries (MW+PWG+PWK+AP+WIL+SKD+VCP)](../../DICT_PROFILE.md#same-entry-across-seven-dictionaries), [Lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg), Sample entries L9/L10/L57, Known issues, Further reading, BibTeX. |
| [ENTRY_GUIDE.md](../../ENTRY_GUIDE.md) | Reader's guide. Encoding, [Orthographical conventions (full)](../../ENTRY_GUIDE.md#orthographical-conventions), Common tags, `<ls>` coverage stats, [Top-25 cited sources](../../ENTRY_GUIDE.md#top-25-most-cited-sources), Period breakdown, Top orphans, [Entry hierarchy distribution](../../ENTRY_GUIDE.md#entry-hierarchy-distribution), [Entry-type breakdown](../../ENTRY_GUIDE.md#entry-type-breakdown-by-content), [IE cognate density](../../ENTRY_GUIDE.md#ie-cognate-density--lang-breakdown), Vedic accent coverage, Cross-reference patterns, mwauthorities/. |
| [DATA_DICTIONARY.md](../../DATA_DICTIONARY.md) | Tag inventory, `<INFER/>`/`<UNMARKED>`/`<UNUSED/>` taxonomy, `<lex>` vs `<ab>` distinction, `<ab n="…">` variant, operative-vs-audit `mwab_input.txt` distinction (csl-pywork 2024 vs MWS 2017). |
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | Issue templates, label taxonomy, multi-step correction workflow. |
| [CITATION.cff](../../CITATION.cff) | Full title, Leumann + Cappeller editors, 286,561 entry count. |
| [ROADMAP.md](../../ROADMAP.md) | 34 open + 157 closed MWS issues synthesised; 10 task subtypes; quarterly cadence. |
| [DOCS_ISSUE.md](../../DOCS_ISSUE.md) | The issue-body draft for [#195](https://github.com/sanskrit-lexicon/MWS/issues/195). |

### Microanalysis suite — [`papers/microanalysis/`](.)

| File | Purpose |
|---|---|
| [PAPER.md](PAPER.md) | **THE canonical paper (~5.7K words; room to grow toward IJL's ~8–10K).** Data-grounded body (five constructs — block / slot / profile / hedge / infrastructure; the **block-economy** thesis); §7 triangulation showing three external frameworks converge; condensed appendices **A** Wiegand · **B** Atkins-Rundell · **C** Hausmann-Wiegand + proposed *Provenienz-Komment* 5th class; §9 methodological-limitations section (regex spot-check + significance + cross-dict + `L.`-innovation + typology overlap). Supersedes the four `paper-*.md` drafts. |
| [MICROANALYSIS.md](MICROANALYSIS.md) | **Data backbone** — 18 formal blocks, 8 semantic blocks, 14 article types, the [block-by-type matrix](MICROANALYSIS.md#4--the-block-by-article-type-matrix), [fullness scale T1–T5](MICROANALYSIS.md#5--fullness-scale), 8 worked entry samples, co-occurrence pairs. |
| [paper-grounded.md](paper-grounded.md), [paper-wiegand.md](paper-wiegand.md), [paper-atkins-rundell.md](paper-atkins-rundell.md), [paper-hausmann.md](paper-hausmann.md) | **Supplementary extended drafts** — superseded by PAPER.md but retained as fuller per-framework treatments. Each carries a banner pointing back to PAPER.md. |
| [README.md](README.md) | Indexes PAPER.md + the consolidation rationale + the triangulation summary. |
| [VISUALISATIONS.md](VISUALISATIONS.md) | Catalogue of ~40 visualisation ideas across 10 categories, prioritised Tier 1/2/3. **Redirects to thematic decisions/* sub-docs for the 28 design decisions.** |
| [DOUBTS.md](DOUBTS.md) | **Critical review.** 15 substantive doubts (D1–D15). **D1/D2/D4/D6/D7/D8 now have "Result" blocks at the top citing the empirical audit.** Read this before publishing anything. |
| [HANDOFF.md](HANDOFF.md) | This file. |

### Empirical-audit suite — [`papers/microanalysis/analysis/`](analysis/) (NEW — added 2026-05-24)

Reproducible scripts that audit PAPER.md's claims against the live dictionary data. Each script reuses the **published** block-detection algorithm via [`_common.py`](analysis/_common.py), so the audits test the actual algorithm that produced the figures. See [analysis/README.md](analysis/README.md) for the full mapping.

| Script | Report | Doubt addressed | Headline finding |
|---|---|---|---|
| [`spotcheck_blocks.py`](analysis/spotcheck_blocks.py) | [SPOTCHECK.md](analysis/SPOTCHECK.md) + [SPOTCHECK_SAMPLE.txt](analysis/SPOTCHECK_SAMPLE.txt) | [D6](DOUBTS.md#d6--block-detection-is-regex-based-and-approximate--important) | Detector reproduces 286,561 count exactly; **F08 over-counts** (36.5% are compound members not inflections); **F09 over-counts** (66.7% outside philological context); **F11 under-count is negligible**; "display headword 99%" was the structural-key rate — rendered `<s>` is **76%** (corrected in [PAPER.md §4](PAPER.md#4-the-block-economy-thesis)) |
| [`significance.py`](analysis/significance.py) | [SIGNIFICANCE.md](analysis/SIGNIFICANCE.md) | [D7](DOUBTS.md#d7--the-block-by-article-type-matrix-has-no-statistical-significance-test--nice-to-resolve) | Every headline contrast is **significant** (p ≈ 0 with Wilson 95% CIs); the small noun_m-vs-noun_f F08 difference is **not** (p = 0.07) — confirming the doubt |
| [`significance_full.py`](analysis/significance_full.py) | [SIGNIFICANCE_FULL.md](analysis/SIGNIFICANCE_FULL.md) | [D7](DOUBTS.md#d7--the-block-by-article-type-matrix-has-no-statistical-significance-test--nice-to-resolve) | Full 270-cell table with **Benjamini–Hochberg FDR correction**: 217/270 significant at q=0.05 |
| [`ls_hedge_check.py`](analysis/ls_hedge_check.py) | [LS_HEDGE_CHECK.md](analysis/LS_HEDGE_CHECK.md) | [D2](DOUBTS.md#d2--the-lslls-mw-innovation-claim--under-checked--important) | MW has 40,212 `L.` hedges; **PWG, PWK, WIL, CAE, SKD, VCP have 0; AP has 1; Benfey 1866 has 0** (despite 14,708 `<ls>` cites — strengthens innovation claim). **Cappeller (CAE) added**: zero `<ls>` apparatus but **undocumented `*` (1,370×) and `†` (903×) markers** — meaning needs Cappeller's 1891 print preface |
| [`cross_dict_kernel.py`](analysis/cross_dict_kernel.py) | [CROSS_DICT.md](analysis/CROSS_DICT.md) | [D1](DOUBTS.md#d1--is-block-economy-a-genuine-principle-or-print-economic-artifact--important) | Block-economy *shape* is **general to all single-volume CDSL dictionaries**, not MW-specific (modal blocks/entry: MW 5, PWG 4, PWK 3, AP 2, WIL 3, Benfey 3, Cappeller 3); PWG is ~4× denser. Claims softened in [PAPER.md §4/§8/§9.3](PAPER.md#4-the-block-economy-thesis) |
| [`cross_dict_profiles.py`](analysis/cross_dict_profiles.py) | [CROSS_DICT_PROFILES.md](analysis/CROSS_DICT_PROFILES.md) | [D1](DOUBTS.md#d1--is-block-economy-a-genuine-principle-or-print-economic-artifact--important) (deepening) | Single-volume dicts **differentiate `<lex>` types** (MW 11.3, PWK 7.7, AP 15.2 pts) while **multi-volume PWG cites uniformly** (0.4) — type-differentiation is itself a single-volume economy. SKD/VCP fall outside the framework (no `<lex>`/`<ls>`; inline `iti` citation) |
| [`make_supplement.py`](analysis/make_supplement.py) | [SUPPLEMENT_MANIFEST.md](analysis/SUPPLEMENT_MANIFEST.md) | [Decision 16](decisions/SUPPLEMENTARY.md) | Builds the reproducibility ZIP (paper + scripts + reports + figures), gitignored output |
| [`check_docs.py`](analysis/check_docs.py) | (prints) | docs-integrity | Validates every relative link + `#anchor` across microanalysis + docs-pass markdown |

### Figures — [`papers/microanalysis/figures/`](figures/)

| Figure | Files | What it shows |
|---|---|---|
| **Fig 1 — Block × article-type heatmap** | [heatmap-{en,ru}.svg/png + .alt.txt + .desc.txt](figures/) | 18 × 14 matrix of block-incidence percentages |
| **Fig 2 — Lineage Sankey** | [sankey-{en,ru}.svg/png/html + .alt.txt + .desc.txt](figures/) | PWG (`H./AK./MED./TRIK./HALĀY./H. an.`) → named kosha works → MW `<ls>L.</ls>` |
| **Fig 3 — Lexicographic timeline** | [timeline-{en,ru}.md](figures/) | Mermaid timeline ~6c kosha → CDSL 2024 |
| **Fig 4 — Article-type treemap** | [treemap-{en,ru}.svg/png + .alt.txt + .desc.txt](figures/) | 286,561 entries by type, compound dominance (44%) at a glance |
| **Fig 5 — Cross-dict block profiles** (NEW 2026-05-24) | [cross-dict-blocks-en.svg/png](figures/) | Per-type block-incidence across 7 structured bilingual dicts |
| **Fig 6 — Cross-dict citation density** (NEW 2026-05-24) | [cross-dict-density-en.svg/png](figures/) | `<ls>` per entry across all 9 dicts; PWG ~4× denser |

Plus: [palette-tokens.json](figures/palette-tokens.json), [palette.css](figures/palette.css), [palette.py](figures/palette.py), [mermaid-theme.json](figures/mermaid-theme.json), [locales/{en,ru}.json](figures/locales/), [data/](figures/data/), [scripts/](figures/scripts/).

### Decisions — [`papers/microanalysis/decisions/`](decisions/)

7 thematic sub-docs (split from VISUALISATIONS.md): [PALETTE](decisions/PALETTE.md), [I18N](decisions/I18N.md), [MICROSITE](decisions/MICROSITE.md), [FIGURES](decisions/FIGURES.md), [NORMALISATION](decisions/NORMALISATION.md), [SUPPLEMENTARY](decisions/SUPPLEMENTARY.md), [BUILD-ORDER](decisions/BUILD-ORDER.md). All 28 design decisions are catalogued with cross-references. See [decisions/README.md](decisions/README.md) for the index.

### Memory files (persist across sessions)

Read these BEFORE starting work:

| File | Why |
|---|---|
| [`MEMORY.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/MEMORY.md) | Index of all memory files |
| [`user_role.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/user_role.md) | Who @gasyoun is, who maintainers @funderburkjim @Andhrabharati @drdhaval2785 are |
| [`project_cologne.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/project_cologne.md) | CDSL org map |
| [`project_docs_review.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md) | Full project history (Phase 3.1 through 3.9 and counting) |
| [`feedback_issue_links.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/feedback_issue_links.md) | **CRITICAL** — the link-everything rule that applies to all issues + docs |
| [`reference_cdsl_abbreviations.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/reference_cdsl_abbreviations.md) | mwabbreviations precedent |
| [`reference_cologne_markup_fix.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/reference_cologne_markup_fix.md) | Markup-fix-audit skill |

---

## 3. Recent commits (the full arc)

In reverse chronological order:

| SHA | Summary |
|---|---|
| `1f8090c` | Reproducibility supplement builder (Decision 16) — `make_supplement.py` + [SUPPLEMENT_MANIFEST.md](analysis/SUPPLEMENT_MANIFEST.md) |
| `9d3bcca` | Full FDR stats appendix + docs-integrity pass (fix broken links/anchors) — 217/270 cells significant at q=0.05 |
| `8e17f09` | Add cross-dictionary comparison figures (Fig 5–6) |
| `b5cbaf4` | Complete cross-dict profiles for all 9 dicts (PWG/PWK/SKD/VCP) |
| `6d03eac` | Deepen D1 to per-type profiles; resolve Cappeller asterisk to print-preface gap |
| `ded06f7` | Add Cappeller (CAE) to the D2 hedge + D1 cross-dict audits |
| `be8f0a2` | **Empirical audits for microanalysis doubts D1/D2/D6/D7** — analysis/ directory created |
| `ca75769` | **Consolidate microanalysis into one paper (D4)** + confirm Observable stack (D8) — PAPER.md created |
| `4d1ef95` | Add HANDOFF.md for new chat continuity |
| `6e6fb28` | Restructure VISUALISATIONS.md into 7 thematic decision sub-docs |
| `0901c81` | Build Tier-1 figures (heatmap, treemap, Sankey, Mermaid timeline) + DOUBTS critical review |
| `e4b202b` | Add VCP+PWK to cross-dict; replace estimates with real counts; fix csl-microsite → csl-atlas |
| `a36614a` | Document VISUALISATIONS round-7 decisions (locale / footer / CI / versioning) |
| `2e6b23a` | Document VISUALISATIONS round-6 decisions (heatmap layout / Sankey / citation / atlas name) |
| `abc8596` | Document VISUALISATIONS round-5 decisions (dimensions / font / license / nav) |
| `8e5107d` | Document VISUALISATIONS round-4 decisions (legends / a11y / numbering / supp materials) |
| `2bb37af` | Document VISUALISATIONS round-3 decisions + summary table |
| `be41dc9` | Document VISUALISATIONS implementation decisions round 2 |
| `b3e355c` | Document VISUALISATIONS design decisions (5) + detailed normalisation analysis |
| `91c0dff` | Add VISUALISATIONS.md catalogue (10 categories, 3 priority tiers) |
| `de5f73b` | Add 4-framework microstructural analysis of MW1899 |
| `717f5b9` | Add ROADMAP.md + fix WIL characterization |
| `60cdc19` | Distinguish operative (csl-pywork 2024) vs audit (MWS 2017) mwab_input |
| `b26e174` | Prove WIL ← kosha, MW ← PWG lineage with quantified evidence |
| `6016641` | Orthographical conventions, Beyond-PWG analysis, cross-dict comparison |
| `aa29b42` | Add typology, citation-markers callout, stats, MW72 links |
| `1ae5fc0` | Deepen MWS docs (CONTRIBUTING, CITATION, DATA_DICTIONARY, ENTRY_GUIDE) |
| `1ab6c98` | Replace [DRAFT] placeholders with researched content |

Earlier history before this arc: see `git log --all` on the MWS repo or [project_docs_review.md](file:///C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md) Phase 3.1–3.5.

---

## 4. Headline audit findings (2026-05-24)

The empirical-audit pass ([analysis/](analysis/)) addressed the most important doubts. Bottom-line results:

### What survived (claims confirmed and strengthened)

- **MW's `<ls>L.</ls>` hedge IS a distinctive innovation.** Audited across 8 dictionaries: MW 40,212 hedges; PWG 0 (of 570,817 `<ls>` cites); PWK 0; WIL 0; CAE 0; SKD 0; VCP 0; AP 1; **Benfey 1866 0** (with full 14,708-cite `<ls>` apparatus, an earlier English-Sanskrit dictionary that **did not** invent the device). [LS_HEDGE_CHECK.md](analysis/LS_HEDGE_CHECK.md).
- **The block-by-type matrix percentages are statistically robust.** 217 of 270 cells (~80%) are significant at q=0.05 with Benjamini-Hochberg FDR correction. Every headline contrast in PAPER.md §4 holds. [SIGNIFICANCE_FULL.md](analysis/SIGNIFICANCE_FULL.md).
- **Block-detection reproduces the 286,561 record count exactly.** [SPOTCHECK.md](analysis/SPOTCHECK.md).

### What softened (claims requiring qualification)

- **"Block economy" is general to single-volume scholarly dictionaries, not MW-specific.** Modal blocks/entry: MW 5, PWG 4, PWK 3, AP 2, WIL 3, Benfey 3, Cappeller 3. PAPER.md §4 and §9.3 now phrase the claim as "characteristic of single-volume scholarly dictionaries." [CROSS_DICT.md](analysis/CROSS_DICT.md).
- **F08 (inflection forms) over-counts by 36.5%** — many hits are compound members, not inflections. **F09 (editorial commentary) over-counts by 66.7%** — many parenthetical hits are not philological. **F02 "display headword 99%" was the structural-key rate; rendered `<s>` is 76%.** All three caveats are now in [PAPER.md §4 + §9](PAPER.md). [SPOTCHECK.md](analysis/SPOTCHECK.md).
- **Type-differentiation IS the single-volume economy** (deepening of D1). Single-volume dicts differentiate `<lex>` types: MW 11.3, PWK 7.7, AP 15.2 pts. Multi-volume PWG cites uniformly: 0.4 pts. **Sanskrit-Sanskrit lexica (SKD, VCP) fall outside the framework** — no `<lex>`/`<ls>`; inline `iti` citation. [CROSS_DICT_PROFILES.md](analysis/CROSS_DICT_PROFILES.md).

### What's still open (audit identified but did not resolve)

- **Cappeller (CAE) 1891 has undocumented `*` (1,370×) and `†` (903×) markers.** An entry-final `*` sits where a hedge sits. Checked all CDSL metadata sources — no documentation found. **Cappeller's 1891 print preface** is needed to determine if either is a hedge precedent (Cappeller co-edited MW 1899).
- **WIL 1832 + Benfey 1866 print prefaces** — should still be read to verify no convention-marker predates MW's `L.`.
- **Statistical significance of the smallest contrasts** (e.g. noun_m-vs-noun_f F08 at p=0.07) is **not** significant — D7's caveat is real and called out.

---

## 5. Critical doubts — D1–D15 status

(Full review with empirical "Result" blocks at the top of each doubt in [DOUBTS.md](DOUBTS.md).)

| # | Title | Status |
|---|---|---|
| **D1** | Is "block economy" MW-specific? | ✅ **AUDITED.** General to single-volume dicts; claim softened in [PAPER.md §4/§8/§9.3](PAPER.md). |
| **D2** | The `<ls>L.</ls>` "MW innovation" claim | ✅ **AUDITED + strengthened.** MW innovation against 8 dicts including Benfey 1866. Open: Cappeller 1891 + WIL + Benfey print prefaces. |
| D3 | The kosha-lineage of WIL is over-narrated | Nice-to-resolve. Open. |
| **D4** | Four framework papers from same data — salami-slicing? | ✅ **RESOLVED.** Consolidated to [PAPER.md](PAPER.md). |
| D5 | 14 article types — too many, overlapping | Important. Open. |
| **D6** | Block detection is regex-based and approximate | ✅ **AUDITED.** F08 + F09 over-counts quantified; F11 under-count negligible; F02 corrected. [§9 limitations](PAPER.md#9-methodological-limitations) added. |
| **D7** | No statistical significance tests | ✅ **AUDITED.** 217/270 cells significant at q=0.05 with FDR. Caveats on the small contrasts called out. |
| **D8** | Observable Framework too heavy? | ✅ **DECIDED.** Keep Observable. |
| D9 | 28 decisions before any code | Important. Partially resolved — figures now built. |
| D10 | csl-atlas named before scoped | Important. Open. Scaffold locally first. |
| D11 | Russian translations bootstrapped by Claude | Important. Open — needs @gasyoun review. |
| D12 | Multi-normalisation increases reader burden | Nice-to-resolve. Open. |
| D13 | Scope creep from docs-pass to atlas | Important. Partially resolved — PAPER.md + figures shipped. |
| D14 | Memory file inflation | Nice-to-resolve. Open. |
| D15 | Issue-tracker as cross-repo task management | Nice-to-resolve. Open. |

**5 of the 15 doubts now have empirical Result blocks** at the top of [DOUBTS.md](DOUBTS.md); D4 + D8 are decided. The remaining 8 are mostly *procedural* (translation review, scoping, MVP cut) rather than *analytical*.

---

## 6. What's pending — three explicit threads

### 6a. User review of the 5 pilot docs-passes

[@funderburkjim](https://github.com/funderburkjim) and [@Andhrabharati](https://github.com/Andhrabharati) are tagged on each issue. Awaiting:

- [MWS #195](https://github.com/sanskrit-lexicon/MWS/issues/195) — fact-check historical claims, WIL ← kosha lineage, sample-entry annotations
- [csl-sqlite #1](https://github.com/sanskrit-lexicon/csl-sqlite/issues/1) — per-dict schema, release tag convention, CI gap
- [csl-inflect #15](https://github.com/sanskrit-lexicon/csl-inflect/issues/15) — examples, downstream consumers, SQLite schema
- [hwnorm1 #20](https://github.com/sanskrit-lexicon/hwnorm1/issues/20) — input/output schema, coverage, usage examples
- [COLOGNE #455](https://github.com/sanskrit-lexicon/COLOGNE/issues/455) — CROSSREF_INDEX accuracy, links currency

Once reviewed, **Phase 4 (org-wide rollout)** can proceed: waves of ~15 repos.

### 6b. Microanalysis publication path

**Decided (2026-05-23):** one consolidated paper ([PAPER.md](PAPER.md)) for [IJL](https://academic.oup.com/ijl). Grounded body + three condensed appendices + §7 triangulation.

**Outstanding before submission:**
- Read **Cappeller 1891** + **Benfey 1866** + **WIL 1832 print prefaces** to verify no pre-MW `L.`-hedge precedent.
- Polish [§9 limitations](PAPER.md#9-methodological-limitations) given the audit results.
- Final pass on §5 (article-type typology) to address [D5](DOUBTS.md#d5--article-type-typology--14-is-too-many--overlapping--important): distinguish primary article types from orthogonal properties.
- Russian-language venue (per [Decisions 3, 6, 11](decisions/I18N.md)) — content TBD.

### 6c. csl-atlas microsite

Per [D10](DOUBTS.md#d10--csl-atlas-is-named-before-scoped--important): repo not yet created. **Status:** scaffold locally first (`D:/claude/csl-atlas/`) before pushing to org. Phase-4 dict coverage scope (which 9 dicts in what order) is unresolved.

The block-detection extension to non-MW dicts has been **partially done** by the cross-dict audit (CROSS_DICT_PROFILES.md). The csl-atlas could be built from this data directly — the data backbone exists.

---

## 7. Conventions and rules

### Linking rule (CRITICAL — applies everywhere)

Per [`feedback_issue_links.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/feedback_issue_links.md): **Every verifiable claim in issue bodies AND docs must be a hyperlink.** Files, sections, data points, editions, record numbers, abbreviations, dates, persons, works. Bare backticks only for short code tokens inside a sentence that already links the surrounding reference. **Codified in all 5 runbooks** under `sanskrit-lexicon-docs-review/runbooks/*.md`.

### Data attribution

Every figure caption: `Source: CDSL mw.txt 2026-05-23 · CC-BY-SA-4.0 · build {SHA}` (per Decision 5, 26, 28).

### Bilingual labels

EN + RU; Sanskrit terms in IAST italics inside both (per Decision 3, 6). Sanskrit is meta-level, not a label language.

### Mermaid i18n

One file per locale (`timeline-en.md` + `timeline-ru.md`), NOT parallel blocks in same file (per Decision 8).

### Issue body format

Tables / prose / checklists — every filename, section, record number, abbreviation linked.

### Branch + commit conventions

- Work happens on the `docs-pass` branch in each pilot repo
- Commits begin with `docs-pass:` prefix
- Use `Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>` (or `Claude Sonnet 4.6` if running on Sonnet) at end of message
- Never push to `master` directly
- The MWS repo has **two local clones** that both track `origin/docs-pass` (see [§11](#11-quick-environment-facts)) — `git fetch && git pull` in one after commits to the other

### Memory hygiene

Memory files at `C:/Users/user/.claude/projects/D--claude/memory/`. One fact per file. Update existing files rather than creating duplicates.

---

## 8. Files to read first (priority order, for a new chat)

1. **This file** — HANDOFF.md
2. [DOUBTS.md](DOUBTS.md) — read the "Result" blocks at the top of D1/D2/D4/D6/D7/D8 first
3. [PAPER.md](PAPER.md) — the consolidated submission paper
4. [analysis/README.md](analysis/README.md) — audit-suite overview and headline findings
5. [MICROANALYSIS.md](MICROANALYSIS.md) — the data backbone behind the matrix
6. [VISUALISATIONS.md](VISUALISATIONS.md) — design-decision index
7. [decisions/README.md](decisions/README.md) — 7 thematic decision sub-docs
8. [../../ROADMAP.md](../../ROADMAP.md) — MWS issue synthesis + quarterly plan
9. [../../DICT_PROFILE.md](../../DICT_PROFILE.md) — reader-facing MW profile
10. [project_docs_review.md](file:///C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md) — full project history

For a fresh session **with no prior context**, files 1–4 are mandatory; files 5–10 are reference-as-needed.

---

## 9. How to continue (concrete steps for the next chat)

The blocking analytical doubts are resolved. The remaining work clusters into four threads:

**Thread A — Pre-submission paper polish.**
- Read the three print prefaces (Cappeller 1891 / Benfey 1866 / WIL 1832) and decide whether to soften or keep the "MW innovation" claim in [PAPER.md Appendix C](PAPER.md#appendix-c--the-hausmann-wiegand-comment-class-reading-condensed).
- Address [D5](DOUBTS.md#d5--article-type-typology--14-is-too-many--overlapping--important): refactor the 14 article types into primary types + orthogonal properties in [PAPER.md §5](PAPER.md).
- Run `make_supplement.py` to produce the reproducibility ZIP (per [Decision 16](decisions/SUPPLEMENTARY.md)).
- Decide submission timing.

**Thread B — Russian translation review** (per [D11](DOUBTS.md#d11--russian-translations-bootstrapped-by-claude--important)).
- Walk @gasyoun through [locales/ru.json](figures/locales/ru.json) bootstrap.
- Flag any low-confidence translations (any with `(?)` markers).
- Regenerate `-ru.svg/png` figures after corrections.

**Thread C — csl-atlas scaffolding** (per [D10](DOUBTS.md#d10--csl-atlas-is-named-before-scoped--important)).
- Scaffold `D:/claude/csl-atlas/` locally (Observable Framework, per [Decision 10](decisions/MICROSITE.md)).
- Choose Phase-4 dict ordering (PWG first? AP? GRA?).
- Populate using the data from [CROSS_DICT_PROFILES.md](analysis/CROSS_DICT_PROFILES.md) (already covers 9 dicts).
- Push to org only after scope is approved.

**Thread D — Phase 4 (org-wide docs-pass rollout)** (blocked by [§6a](#6a-user-review-of-the-5-pilot-docs-passes)).
- Wait for maintainer review of the 5 pilots.
- Apply the established pattern to waves of ~15 repos (see [`sanskrit-lexicon-docs-review/runbooks/`](file:///D:/claude/sanskrit-lexicon-docs-review/runbooks/)).
- Each dict-repo docs-pass yields its own ROADMAP.md following the [MWS ROADMAP](../../ROADMAP.md) template.

**If addressing user feedback** that lands in a new turn:
- Read the user's message carefully — they often push back on specific claims with evidence (e.g. WIL "bare minimum" correction; kosha-lineage assertion; stale `mwab_input.txt` link; WIL→PWK substitution in Option F).
- Verify their claim against data files before responding.
- Update docs in the same commit; don't accumulate fixes.

---

## 10. Cross-repo dependencies

| Repo | Status | Relevance |
|---|---|---|
| [csl-orig](https://github.com/sanskrit-lexicon/csl-orig) | Canonical | All `<dict>.txt` source files live here |
| [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork) | Active | Build system; `sqlite.py`, `generate_dict.sh`; operative `mwab_input.txt` at `v02/distinctfiles/mw/pywork/mwab/` |
| [csl-sqlite](https://github.com/sanskrit-lexicon/csl-sqlite) | docs-pass branch reviewable | SQLite distribution |
| [csl-app](https://github.com/sanskrit-lexicon/csl-app) | Active | Web display; UI improvements land here |
| [csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect) | docs-pass branch reviewable | Inflection tables |
| [hwnorm1](https://github.com/sanskrit-lexicon/hwnorm1) | docs-pass branch reviewable | Headword normalisation processing |
| [COLOGNE](https://github.com/sanskrit-lexicon/COLOGNE) | docs-pass branch reviewable | Org hub |
| [csl-homepage](https://github.com/sanskrit-lexicon/csl-homepage) | TBD | Where org-wide docs hub will live |
| `csl-atlas` (planned) | Not yet created | Phase-4 microsite (per [D10](DOUBTS.md#d10--csl-atlas-is-named-before-scoped--important)) |

---

## 11. Quick environment facts

- **Working directory:** `D:/claude/` (Windows; PowerShell + Bash both available; **no `find`/`grep`/`cat` via Bash — use Glob/Grep/Read tools**)
- **MWS local clones (two, same `origin`):** `C:/Users/user/Documents/GitHub/MWS/` (GitHub-Desktop clone — currently the active working copy, on `docs-pass`) and `D:/claude/mws_repo/` (also on `docs-pass`). Both track `origin/docs-pass`; commit/push in one, then `git fetch && git pull` in the other to avoid divergence.
- **Other pilot repos:** `D:/claude/csl-sqlite_repo/`, `D:/claude/csl-inflect_repo/`, `D:/claude/hwnorm1_repo/`, `D:/claude/cologne_repo/`
- **Docs-review workspace:** `D:/claude/sanskrit-lexicon-docs-review/` (runbooks, templates, hand-offs)
- **csl-atlas (planned, not yet scaffolded):** `D:/claude/csl-atlas/`
- **Data files (downloaded for analysis at `/tmp/`):** `mw.txt`, `pwg.txt`, `pw.txt` (PWK), `ap.txt`, `wil.txt`, `ben.txt` (Benfey 1866), `cae.txt` (Cappeller 1891), `skd.txt`, `vcp.txt`, plus four koshas `armh.txt`, `abch.txt`, `acph.txt`, `acsj.txt`. **Note: `/tmp` on Windows = `C:/Users/user/AppData/Local/Temp/`**; Python scripts must use the full path, not `/tmp/`. The data files are gitignored.
- **Today's date:** 2026-05-24
- **CDSL data freshness:** 2026-05-23/24 fetch from `csl-orig/master`

---

## 12. Open questions for the new chat

Pick whichever is most actionable:

1. ~~**D4 paper consolidation**~~ ✅ **DECIDED** — one paper to IJL ([PAPER.md](PAPER.md)).
2. ~~**D8 microsite stack**~~ ✅ **DECIDED** — keep Observable Framework.
3. ~~**Methodological limitations**~~ ✅ **DONE** — [PAPER.md §9](PAPER.md#9-methodological-limitations).
4. ~~**Cross-dict block matrices for D1**~~ ✅ **DONE** — [CROSS_DICT_PROFILES.md](analysis/CROSS_DICT_PROFILES.md) covers all 9 dicts.
5. ~~**Statistical significance for D7**~~ ✅ **DONE** — [SIGNIFICANCE_FULL.md](analysis/SIGNIFICANCE_FULL.md), 217/270 cells significant at q=0.05.
6. ~~**Cappeller / Benfey / WIL print prefaces**~~ ✅ **DONE 2026-05-27 (O1)** — D2 closed and downgraded: Cappeller `*` 1891 and Benfey `†` 1866 are typographic precedents; MW's innovation is structural promotion to the source-citation slot. See [DOUBTS D2](DOUBTS.md#d2--the-lsllls-claim-refined-mw-systematised-a-convention-pioneered-typographically--resolved-2026-05-27).
7. **Russian translation review:** when can [@gasyoun](https://github.com/gasyoun) review the bootstrap RU translations in [locales/ru.json](figures/locales/ru.json)? **(Opus pre-review pass complete 2026-05-27 (O4) — 4 string corrections + 2 (?)-clearances; 3 medium-confidence terms still flagged.)**
8. ~~**Phase-4 scope**~~ ✅ **DONE 2026-05-27 (O5)** — 9-chapter ordering and 3 template tiers documented in [decisions/MICROSITE.md Decision 29](decisions/MICROSITE.md#decision-29--phase-4-dictionary-ordering-chapter-templates-minimum-data-added-2026-05-27).
9. **MVP cut:** does the user accept shipping PAPER.md + one figure now, deferring everything else?
10. **csl-atlas repo creation:** scaffold locally now? Phase-4 ordering decided?
11. ~~**[D5](DOUBTS.md#d5--article-type-typology--refactored-to-8-primary-types--3-orthogonal-properties--resolved-2026-05-27) typology refactor**~~ ✅ **DONE 2026-05-27 (O2)** — 8 primary types + 3 orthogonal properties in [PAPER.md §5](PAPER.md#5-profiles-as-the-unit-of-typology) and [MICROANALYSIS.md §3](MICROANALYSIS.md#3--article-type-typology-8-primary-types--3-orthogonal-properties); legacy 14-bucket table preserved as §3.1.
12. **Russian-language venue:** which publication, what length, what overlap with the IJL paper? **(O9 in flight — drafting [PAPER_RU.md](PAPER_RU.md) ~5K words for Russian indological venue.)**

### Maintainer-review status (5 pilots, 2026-05-27 after O6)

| Issue | Status | Latest |
|---|---|---|
| [MWS#195](https://github.com/sanskrit-lexicon/MWS/issues/195) | No maintainer comments yet | [O1-O5 delta posted 2026-05-27](https://github.com/sanskrit-lexicon/MWS/issues/195#issuecomment-4555387587); D21 resolved post-Opus (three-stage lineage: 1872 MW concept · 1891 Cappeller systematic typographic · 1899 MW+Cappeller tagged); **all 7 O7 hostile-review doubts (D16-D22) closed**; submission-v1 tag pushed (8,654-word PAPER.md, 969-word IJL_COVER_LETTER.md, 4,045-word PAPER_RU.md, 104-file supplementary ZIP); csl-atlas [MW chapter](https://sanskrit-lexicon.github.io/csl-atlas/dicts/mw) authored to Decision 29 Tier A and pushed live |
| [csl-sqlite#1](https://github.com/sanskrit-lexicon/csl-sqlite/issues/1) | No comments | [Re-ping posted 2026-05-27](https://github.com/sanskrit-lexicon/csl-sqlite/issues/1#issuecomment-4555390868) |
| [csl-inflect#15](https://github.com/sanskrit-lexicon/csl-inflect/issues/15) | No comments | [Re-ping posted 2026-05-27](https://github.com/sanskrit-lexicon/csl-inflect/issues/15#issuecomment-4555392207) |
| [hwnorm1#20](https://github.com/sanskrit-lexicon/hwnorm1/issues/20) | No comments | [Re-ping posted 2026-05-27](https://github.com/sanskrit-lexicon/hwnorm1/issues/20#issuecomment-4555393218) |
| [COLOGNE#455](https://github.com/sanskrit-lexicon/COLOGNE/issues/455) | No comments | [Re-ping posted 2026-05-27](https://github.com/sanskrit-lexicon/COLOGNE/issues/455#issuecomment-4555394467) |

Deadline: if no reviews by 2026-06-15, propose merging as-is with follow-up issues for any later corrections.

---

## 13. Acknowledgments

This work is a collaboration between [@gasyoun](https://github.com/gasyoun) (Mārcis Gasūns, CDSL member) and Claude (multiple sessions across Opus 4.7 and Sonnet 4.6). The four-framework microanalysis (now consolidated), the 28-decision visualisation design, the 5-pilot docs-pass, the WIL-kosha lineage proof, the citation-markers callout, the typology of MW article types, the [empirical-audit suite](analysis/), and the [block-economy thesis](PAPER.md#4-the-block-economy-thesis) (with cross-dict corroboration) are joint products. Where mistakes appear in the analysis, they are Claude's; where the project is interesting, they are [@gasyoun](https://github.com/gasyoun)'s.

---

**End of HANDOFF.** A new chat session reading this file from top to bottom — plus [DOUBTS.md](DOUBTS.md), [PAPER.md](PAPER.md), [analysis/README.md](analysis/README.md), and [project_docs_review.md](file:///C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md) — should be productive within minutes.
