# Decisions — csl-atlas interactive microsite

Covers decisions **2**, **7**, **10**, **20**, **24**, **27**. See [decisions/README.md](README.md) for the full index.

---

## Decision 2 — Build both static (paper) and interactive (microsite)

**Both deliverables.** Static SVG figures (embeddable in the IJL paper) plus an interactive microsite (HTML, linked from the paper as supplementary materials).

The microsite lets reviewers:
- Explore the 18×14 matrix interactively (hover for percentages + counts).
- Filter the treemap by article type.
- Trace any `<ls>` source to the entries citing it.
- Compare two article types side-by-side.

Tier 1 figures (heatmap, Sankey, timeline, treemap) are produced **twice**: once as static SVG with embedded palette, once as interactive HTML/JS.

Data binding: JSON files in `papers/microanalysis/figures/data/` consumed by both the static renderer (Python) and the interactive renderer (D3 / Plot / Vega-Lite).

## Decision 7 — Hosting: new repo `csl-atlas`

The microsite lives in a new repo, **`csl-atlas`** under the `sanskrit-lexicon` org, rather than embedded in MWS. Rationale:

- Covers multiple CDSL dictionaries (9 in Phase 4) — natural to give it its own home.
- Hosted on GitHub Pages: `https://sanskrit-lexicon.github.io/csl-atlas/`.
- Pulls JSON data from per-dict `mw_block_matrix.py`-equivalent scripts.
- Versioned independently from any single dict's docs-pass.
- Clean separation: **MWS holds the static paper + data scripts; csl-atlas holds the live web app.**

## Decision 10 — Stack: Observable Framework

[Observable Framework](https://observablehq.com/framework). Rationale:
- Built-in i18n routing (matches per-locale-file strategy from [I18N.md](I18N.md)).
- Reactive data + D3 + Markdown pages out of the box.
- Static output (HTML/JS) deployable to GitHub Pages.
- First-class declarative data files (JSON/CSV) → matches our JSON-data architecture.
- Polished research-microsite aesthetic.

**[DOUBTS.md D8](../DOUBTS.md#d8--observable-framework-is-heavy-infrastructure-for-a-research-microsite--blocking) — RESOLVED 2026-05-23: keep Observable Framework.** The lock-in / build-pipeline trade-offs are accepted in exchange for built-in i18n routing, reactive D3/Plot, and Markdown pages. The vanilla-HTML+D3 alternative is *not* adopted. Mitigations become implementation notes: pin the Framework version, keep the static SVG/PNG figures independent of the framework (the paper does not depend on it), and reserve Observable for the interactive tools.

## Decision 20 — Navigation: hybrid (paper-tours + standalone tools)

Observable Framework `src/` structure:

```
csl-atlas/
  src/
    index.md                         landing page
    paper/                           paper-tour section (single consolidated paper)
      grounded.md                    body: five constructs + block economy
      triangulation.md               §7 — three frameworks converge
      appendices.md                  A Wiegand · B Atkins-Rundell · C Hausmann
    tools/                           standalone visualisation tools
      matrix-explorer.md             18×14 heatmap, interactive
      lineage-sankey.md              PWG→MW Sankey
      typology-treemap.md            article-type treemap
      timeline.md                    lexicographic timeline
      type-comparator.md             Tier 3 — side-by-side type compare
      citation-tracer.md             Tier 3 — click-source-see-entries
    dicts/                           Phase 4 per-dictionary chapters
      mw.md / pwg.md / pwk.md / ap.md / wil.md / skd.md / vcp.md
      armh.md / abch.md
    data/                            JSON data shared across pages
    locales/
      en/                            English locale routes
      ru/                            Russian locale routes

```

Reader paths:
- **Paper tour:** "I want to follow the argument of the paper — grounded body, then the triangulation, then the framework appendices."
- **Tools:** "I want to explore the data interactively without paper context."
- **Dictionary chapter:** "I'm here for one specific dict's microstructure."

Both share the same underlying data + palette + locale strings.

## Decision 24 — Name: `csl-atlas`

Full name: **"Atlas of the Cologne Digital Sanskrit Lexicons."** Tagline options (TBD):
- "A comparative microstructural atlas of the CDSL corpus"
- "Mapping nine Sanskrit dictionaries from microstructure to lineage"
- "An interactive companion to the CDSL"

The "atlas" framing signals Phase-4 ambition beyond MW. Each dictionary gets a chapter; each Tier-1 figure has per-dictionary and cross-dictionary variants.

## Decision 27 — CI/CD: GitHub Actions on push to `main`

`.github/workflows/build-and-deploy.yml` in `csl-atlas`:
1. Trigger on push to `main` (or manual dispatch).
2. Set up Node 20 + npm cache.
3. Run `npm ci && npm run build`.
4. Deploy `dist/` to GitHub Pages via `actions/deploy-pages@v4`.

A separate workflow (planned, not yet implemented) handles data refreshes:
- `data-refresh.yml` — manual trigger or cron monthly.
- Re-downloads `mw.txt` (and other dict data), re-runs `mw_block_matrix.py`, regenerates JSON in `data/`, commits to `main`; regular build-and-deploy then picks it up.

---

## Implementation status (2026-05-23)

- [x] Local scaffold complete at `D:/claude/csl-atlas/`
- [x] `package.json` + `observablehq.config.js` + `README.md` + `LICENSE` written
- [x] `src/index.md` landing page with paper-tour + tools + dicts grid
- [x] `src/tools/matrix-explorer.md` with working Plot.cell heatmap
- [x] `src/tools/lineage-sankey.md` with working D3-Sankey
- [x] `src/tools/typology-treemap.md` with Plot.cell treemap
- [x] `src/tools/timeline.md` Mermaid timeline reference
- [x] `data/` copied from MWS (5 JSON files + palette tokens)
- [x] `src/palette.css` copied from MWS
- [x] `.github/workflows/build-and-deploy.yml` GitHub Actions config
- [ ] Local Git initialised; **NOT yet pushed** to `sanskrit-lexicon/csl-atlas` — awaiting [@gasyoun](https://github.com/gasyoun)'s approval per Decision 7
- [ ] `npm install` not run; no dependency lock-file yet
- [ ] Paper-tour pages (4) not written — placeholder only
- [ ] Tier-3 tools (type-comparator, citation-tracer) not implemented
- [ ] Per-dictionary chapters (9) not written — Phase 4 work
- [ ] RU locale routes not yet wired

## Decision 29 — Phase-4 dictionary ordering, chapter templates, minimum data (added 2026-05-27)

Phase 4 commits the atlas to chapters for **nine** dictionaries. With chapter authoring sequenced one-at-a-time over months and each chapter linking forward and backward, **order matters** both for the reader's experience and for the editorial work itself. Three sub-decisions:

### 29.1 — Ordering: framework-fit first, then precedent, then genre-bound

The 9 chapters are sequenced to mirror the paper's argument arc: start at the framework's *home*, work outward through *direct ancestors* and *modern successors*, then visit the *typographic precedents* discovered in [O1](../analysis/LS_HEDGE_CHECK.md#print-preface-read-added-2026-05-27-closes-the-digital-only-gap), and finish at the *genre limit* where the framework stops applying.

| # | Code | Dictionary | Year | Why this position |
|--:|---|---|---|---|
| 1 | **MW** | Monier-Williams | 1899 | Framework's home; full block-by-type matrix; the paper's primary artefact. Atlas reader arrives here. |
| 2 | **PWG** | Böhtlingk-Roth, *Grosses* PW | 1855–75 | MW's direct ancestor; densest `<ls>` apparatus (4.6/record vs MW 1.1); the contrast that motivates *block economy*. |
| 3 | **PWK** | Böhtlingk, *kürzeres* PW | 1879–89 | PWG's own abridgement; demonstrates that single-volume economy is independent of the editor. |
| 4 | **AP** | Apte, *Practical* | 1957 | The modern successor; differentiates types (spread 15.2 pts, largest among CDSL); shows the framework on a 20th-century artefact. |
| 5 | **BEN** | Benfey | 1866 | First typographic precedent for the `<ls>L.</ls>` hedge (dagger `†` = "no authoritative references"); IE-cognate-heavy. |
| 6 | **CAE** | Cappeller | 1891 | Second typographic precedent (asterisk `*` = "taught only by grammarians or lexicographers"); Cappeller co-edited MW 1899, so the lineage is direct. The "structural innovation" claim in [§7.2(ii)](../PAPER.md#72-three-findings-all-three-frameworks-reach) lives here. |
| 7 | **WIL** | Wilson | 1832 | Earliest CDSL dict; minimal `<ls>` apparatus (224 of 230 tags = `<ls>Rox.</ls>`); the **base from which the European tradition departs**. The reader who has seen MW, PWG, PWK, AP, BEN, CAE now sees the starting point. |
| 8 | **SKD** | *Śabdakalpadruma* | 1822–58 | Sanskrit-Sanskrit lexicon (kosha-style). Framework's first genre-bound limit: no `<lex>`/`<ls>` markup, marks gender inline, cites via inline `iti` quotation (1.70/record). |
| 9 | **VCP** | *Vācaspatya* | 1873–84 | Second Sanskrit-Sanskrit lexicon. Confirms the genre boundary (inline `iti` at 0.26/record — even sparser). Closes the atlas with the explicit statement: **the block apparatus is genre-bound to structured bilingual dictionaries.** |

**What this ordering is NOT:**
- *Not chronological* (would put WIL 1832 first — disorienting for a reader who came for MW).
- *Not by record count* (would put MW first, then AP — but AP is a 20th-century outlier that belongs after PWG/PWK).
- *Not alphabetical* (no narrative arc).

**Rationale.** The ordering encodes a narrative: (1–4) build up the framework on data-rich, differentiated dictionaries; (5–6) discover the typographic precedents that downgrade the "MW innovation" claim; (7) return to the base; (8–9) show where the framework stops. A reader following this order learns the framework, then learns its history, then learns its limits — and that is the same arc as [PAPER.md](../PAPER.md) itself.

**The four kosha repos** ([ARMH](https://github.com/sanskrit-lexicon/armh), [ABCH](https://github.com/sanskrit-lexicon/abch), [ACPH](https://github.com/sanskrit-lexicon/acph), [ACSJ](https://github.com/sanskrit-lexicon/acsj)) are **not** Phase-4 chapters — they are the *resolution targets* for `<ls>L.</ls>` (per [PAPER.md §8](../PAPER.md#8-implications-for-future-cdsl-work)) and belong in a future Phase-5 "kosha lineage" companion area, not as full atlas chapters of the same shape as MW/PWG. Treating them as chapters would imply they are dictionaries to read; they are sources to resolve hedges *to*.

### 29.2 — Chapter template variants (three tiers)

The 9 dictionaries split structurally into three groups; one template per group keeps the atlas consistent without forcing genre-mismatched content.

**Tier A — Full template** (MW, PWG, PWK, AP; 4 chapters):

```
1. Overview (1 para; record count, editor, period, position in CDSL)
2. Profile table (8 primary types × 18 blocks; reuse PAPER.md §5)
3. Citation density and apparatus (cite/record, top 12 <ls> sigla)
4. Hedge analysis (if hedge present; what fraction of entries hedged; in which types)
5. Lineage statement (parent → this; this → successor; cross-link to relevant DICT_PROFILE.md)
6. Cross-references — adjacent chapters' divergence/convergence
7. Decisions log (per-dict editorial choices documented in this chapter)
8. Data dictionary link + repo link + license
```

**Tier B — Compact template + typography section** (BEN, CAE, WIL; 3 chapters):

The block-by-type matrix is *not* meaningful for these (BEN has no `<lex>` tags — all "other"; CAE and WIL have zero `<ls>` apparatus so the citation column is empty). Replace section 2 with a structural-features section, and add a typography-and-precedent section if applicable (BEN, CAE):

```
1. Overview
2. Structural features (what blocks ARE present; what's atypical)
3. Citation strategy (or lack thereof — explain why)
3a. Typography & precedent (BEN/CAE only) — the dagger/asterisk-as-hedge analysis from O1
4. (no hedge analysis section — see 3a)
5. Lineage statement
6. Cross-references
7. Decisions log
8. Data dictionary link + repo link + license
```

**Tier C — Genre-bound template** (SKD, VCP; 2 chapters):

The block apparatus does not apply. Replace sections 2–4 with a prose-pattern section centered on inline-`iti` citation:

```
1. Overview
2. Prose-pattern analysis (inline iti/record, sentence-mean-length, top inline citation sigla)
3. How indigenous-kosha citation differs from European source-tagging
4. Why the block framework does not transfer (link to PAPER.md §8 cross-dict audit and CROSS_DICT_PROFILES Part B)
5. Lineage statement (within the Sanskrit-Sanskrit tradition; relation to Amarakośa, Hemachandra)
6. Cross-references
7. Decisions log
8. Data dictionary link + repo link + license
```

### 29.3 — Minimum data per dictionary chapter

Each chapter, regardless of tier, must carry at least the following before being merged:

| Required datum | Source | Acceptance check |
|---|---|---|
| Record count | `wc -l` over the dict's `<L>...<LEND>` stream | Within 1% of the count published in the dict's own README. |
| Editor + period | The repo's CITATION.cff / README | One canonical reference per chapter. |
| Top-12 `<ls>` sigla (Tier A/B) or top-12 inline-`iti` sigla (Tier C) | `ls_hedge_check.py` / `cross_dict_profiles.py` | Numerical, reproducible. |
| Citation density | cite-tags ÷ records | Single decimal place. |
| Lineage statement | `DICT_PROFILE.md#lineage-*` | Linked, not paraphrased. |
| Repo URL | `https://github.com/sanskrit-lexicon/<code>` | Live link. |
| License | The repo's LICENSE | Single line; CC-BY-SA-4.0 for all CDSL dicts. |
| Reproducibility manifest line | `analysis/<dict>_block_matrix.py` output | The chapter must name the script that produced its numbers. |

Optional-but-strongly-encouraged (drives reader trust): one figure (the dict's own block-heatmap or its single most distinctive figure — see [FIGURES.md](FIGURES.md)) and one cross-link to the corresponding section in [PAPER.md](../PAPER.md) or [DICT_PROFILE](../../../DICT_PROFILE.md).

### 29.4 — Authoring order ≠ presentation order

The presentation order is fixed (29.1). The **authoring** order can differ — drafting BEN and CAE *before* AP is editorially efficient because the typographic-precedent finding from O1 is freshest in our notes. Suggested authoring sequence: MW → PWG → CAE → BEN → PWK → AP → WIL → SKD → VCP. The reader still encounters them in 29.1 order; only the writing happens in the order convenient for the editor.

---

## Cross-links

- [VISUALISATIONS.md](../VISUALISATIONS.md) — catalogue
- [I18N.md](I18N.md) — locale routing
- [FIGURES.md](FIGURES.md) — what the microsite renders
- [CROSS_DICT_PROFILES.md](../analysis/CROSS_DICT_PROFILES.md) — empirical basis for the 9-dict ordering (Part A bilingual / Part B genre-bound)
- [LS_HEDGE_CHECK.md](../analysis/LS_HEDGE_CHECK.md) — preface-read evidence that places CAE and BEN at positions 5–6
- [DOUBTS.md D8, D10](../DOUBTS.md) — known doubts about stack choice and premature naming
- [csl-atlas local scaffold](file:///D:/claude/csl-atlas/) — current local state
- Future: `https://github.com/sanskrit-lexicon/csl-atlas` — pending push
