# HANDOFF — MW1899 microanalysis + csl-atlas

**Purpose:** let a fresh Claude session pick up this work without losing context.
**Author:** Claude Opus 4.7, on behalf of @gasyoun. Last updated 2026-05-23.

This document is **self-contained** — read it (and follow the links) before doing any new work. The full conversation history is multi-day; this file is the executive summary.

---

## 1. Five-line orientation

The Cologne Digital Sanskrit Lexicon (CDSL) project, sanskrit-lexicon org on GitHub, runs an org-wide **docs-pass** across ~76 repos to standardise documentation. The MWS (Monier-Williams) docs-pass is the flagship pilot, completed and reviewed via [issue #195](https://github.com/sanskrit-lexicon/MWS/issues/195). On top of that, we built a [**microanalysis** of MW1899's microstructure](README.md) (286,561 records, 18 formal blocks, 14 article types, 28 design decisions) — originally four parallel framework papers, **now consolidated into a single paper** ([PAPER.md](PAPER.md), per [D4](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking)): a data-grounded body + three condensed framework appendices — plus a [visualisation catalogue](VISUALISATIONS.md) and four [Tier-1 figures](figures/) (heatmap / treemap / Sankey / Mermaid timeline). The next strategic phase is [**csl-atlas**](decisions/MICROSITE.md) — a 9-dict **Observable Framework** microsite (stack confirmed, per [D8](DOUBTS.md#d8--observable-framework-is-heavy-infrastructure-for-a-research-microsite--blocking)) covering MW + PWG + AP + WIL + SKD + ARMH + ABCH + ACPH + ACSJ + VCP + PWK.

---

## 2. What exists right now (state as of HEAD = `6e6fb28`)

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
| [DICT_PROFILE.md](../../DICT_PROFILE.md) | Reader-facing profile of MW. Contains: At-a-Glance, Orthographical conventions, Historical background, Scholarly significance, When to use (with [14-row article typology](../../DICT_PROFILE.md#article-types--what-youll-encounter) + [citation markers callout](../../DICT_PROFILE.md#citation-markers--not-all-are-literary-works)), Relationship to other CDSL dicts, [Beyond PWG analysis](../../DICT_PROFILE.md#beyond-pwg--what-mw-contributes), [Same entry across 7 dictionaries (MW+PWG+PWK+AP+WIL+SKD+VCP)](../../DICT_PROFILE.md#same-entry-across-five-dictionaries), [Lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) with citation evidence, Sample entries L9/L10/L57, Known issues, Further reading, BibTeX. |
| [ENTRY_GUIDE.md](../../ENTRY_GUIDE.md) | Reader's guide. Encoding, [Orthographical conventions (full)](../../ENTRY_GUIDE.md#orthographical-conventions), Common tags with real counts, `<ls>` coverage stats, [Top-25 cited sources](../../ENTRY_GUIDE.md#top-25-most-cited-sources), Period breakdown, Top orphans, [Entry hierarchy distribution](../../ENTRY_GUIDE.md#entry-hierarchy-distribution), [Entry-type breakdown](../../ENTRY_GUIDE.md#entry-type-breakdown-by-content), [IE cognate density](../../ENTRY_GUIDE.md#ie-cognate-density--lang-breakdown), Vedic accent coverage, Cross-reference patterns, mwauthorities/. |
| [DATA_DICTIONARY.md](../../DATA_DICTIONARY.md) | Tag inventory with audit counts, `<INFER/>`/`<UNMARKED>`/`<UNUSED/>` taxonomy, `<lex>` vs `<ab>` distinction, `<ab n="…">` variant, operative-vs-audit `mwab_input.txt` distinction (csl-pywork 2024 vs MWS 2017). |
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | Issue templates, label taxonomy, multi-step correction workflow. |
| [CITATION.cff](../../CITATION.cff) | Full title, Leumann + Cappeller editors, 286,561 entry count. |
| [ROADMAP.md](../../ROADMAP.md) | 34 open + 157 closed MWS issues synthesised; 10 task subtypes; quarterly cadence. |
| [DOCS_ISSUE.md](../../DOCS_ISSUE.md) | The issue-body draft for [#195](https://github.com/sanskrit-lexicon/MWS/issues/195). |

### Microanalysis suite — [`papers/microanalysis/`](.)

| File | Purpose |
|---|---|
| [MICROANALYSIS.md](MICROANALYSIS.md) | **Data backbone** — 18 formal blocks, 8 semantic blocks, 14 article types, the [block-by-type matrix](MICROANALYSIS.md#4--the-block-by-article-type-matrix), [fullness scale T1–T5](MICROANALYSIS.md#5--fullness-scale), 8 worked entry samples, co-occurrence pairs. |
| [PAPER.md](PAPER.md) | **The consolidated paper (~5.7K words).** Data-grounded body (five constructs — block / slot / profile / hedge / infrastructure; the **block-economy** thesis), §7 triangulation showing three external frameworks converge, three condensed appendices (**A** Wiegand microstructure · **B** Atkins-Rundell practical lexicography / retrieval-dictionary typology · **C** Hausmann-Wiegand comment-classes + proposed *Provenienz-Komment* 5th class), and a §9 methodological-limitations section. Consolidates the four `paper-*.md` drafts, which are **retained in this directory as supplementary extended drafts** (each banner-linked back to PAPER.md). |
| [README.md](README.md) | Indexes PAPER.md + the consolidation rationale + the triangulation summary. |
| [VISUALISATIONS.md](VISUALISATIONS.md) | Catalogue of ~40 visualisation ideas across 10 categories, prioritised Tier 1/2/3. **Redirects to thematic decisions/* sub-docs for the 28 design decisions.** |
| [DOUBTS.md](DOUBTS.md) | **Critical review.** 15 substantive doubts (D1–D15) about analytical claims, design decisions, architecture. Read this before publishing anything. |
| [decisions/README.md](decisions/README.md) | Index for the 7 thematic decision sub-docs. |
| [decisions/PALETTE.md](decisions/PALETTE.md) | Colour palette JSON-first tokens; Noto Sans font; CC-BY-SA. Decisions 1, 9, 18, 19. |
| [decisions/I18N.md](decisions/I18N.md) | Bilingual EN/RU; IAST in italics in RU; per-locale Mermaid files; bootstrap-and-correct RU translations; default locale EN. Decisions 3, 6, 8, 11, 25. |
| [decisions/MICROSITE.md](decisions/MICROSITE.md) | csl-atlas in new repo; Observable Framework; hybrid nav; GitHub Actions CI/CD. Decisions 2, 7, 10, 20, 24, 27. |
| [decisions/FIGURES.md](decisions/FIGURES.md) | Legends, accessibility triplet, numbering, dimensions, heatmap layout, Sankey structure, footer, versioning. Decisions 13, 14, 15, 17, 21, 22, 23, 26, 28. |
| [decisions/NORMALISATION.md](decisions/NORMALISATION.md) | Multi-normalisation strategy; 7 options (A–G) with real counts. Decision 4. |
| [decisions/SUPPLEMENTARY.md](decisions/SUPPLEMENTARY.md) | Attribution + supp materials ZIP. Decisions 5, 16. |
| [decisions/BUILD-ORDER.md](decisions/BUILD-ORDER.md) | Foundation → heatmap → treemap → Sankey → Mermaid. Decision 12. |

### Figures — [`papers/microanalysis/figures/`](figures/)

| File | Purpose |
|---|---|
| [palette-tokens.json](figures/palette-tokens.json) | Single source of truth for colours, fonts |
| [palette.css](figures/palette.css) | Generated CSS custom properties |
| [palette.py](figures/palette.py) | Generated Python module for matplotlib |
| [mermaid-theme.json](figures/mermaid-theme.json) | Generated Mermaid theme variables |
| [heatmap-{en,ru}.svg/png + .alt.txt + .desc.txt](figures/) | **Figure 1** — 18×14 block × article-type heatmap |
| [treemap-{en,ru}.svg/png + .alt.txt + .desc.txt](figures/) | **Figure 4** — Article-type composition treemap |
| [sankey-{en,ru}.svg/png/html + .alt.txt + .desc.txt](figures/) | **Figure 2** — PWG → kosha → MW `L.` Sankey (3-stage) |
| [timeline-{en,ru}.md](figures/) | **Figure 3** — Mermaid lexicographic timeline (per-locale files per Decision 8) |
| [locales/{en,ru}.json](figures/locales/) | Translation strings |
| [data/](figures/data/) | JSON data exports consumed by both static + interactive renderers |
| [scripts/](figures/scripts/) | Build scripts (palette, heatmap, treemap, Sankey renderers) |

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

## 3. Recent commits (this session arc)

In reverse chronological order:

| SHA | Author | Summary |
|---|---|---|
| `6e6fb28` | gasyoun | Restructure VISUALISATIONS.md into 7 thematic decision sub-docs |
| `0901c81` | gasyoun | Build Tier-1 figures (heatmap, treemap, Sankey, Mermaid timeline) + DOUBTS critical review |
| `e4b202b` | gasyoun | Add VCP+PWK to cross-dict; replace VISUALISATIONS estimates with real counts; fix csl-microsite → csl-atlas |
| `a36614a` | Claude | Document VISUALISATIONS round-7 decisions (locale / footer / CI / versioning) |
| `2e6b23a` | Claude | Document VISUALISATIONS round-6 decisions (heatmap layout / Sankey / citation / atlas name) |
| `abc8596` | Claude | Document VISUALISATIONS round-5 decisions (dimensions / font / license / nav) |
| `8e5107d` | Claude | Document VISUALISATIONS round-4 decisions (legends / a11y / numbering / supp materials) |
| `2bb37af` | Claude | Document VISUALISATIONS round-3 decisions + summary table |
| `be41dc9` | Claude | Document VISUALISATIONS implementation decisions round 2 (4 more) |
| `b3e355c` | Claude | Document VISUALISATIONS design decisions (5) + detailed normalisation analysis |
| `91c0dff` | Claude | Add VISUALISATIONS.md catalogue (10 categories, 3 priority tiers) |
| `de5f73b` | Claude | Add 4-framework microstructural analysis of MW1899 |
| `717f5b9` | Claude | Add ROADMAP.md + fix WIL characterization |
| `60cdc19` | Claude | Distinguish operative (csl-pywork 2024) vs audit (MWS 2017) mwab_input |
| `b26e174` | Claude | Prove WIL ← kosha, MW ← PWG lineage with quantified evidence |
| `6016641` | Claude | Orthographical conventions, Beyond-PWG analysis, cross-dict comparison |
| `aa29b42` | Claude | Add typology, citation-markers callout, stats, MW72 links |
| `1ae5fc0` | Claude | Deepen MWS docs (CONTRIBUTING, CITATION, DATA_DICTIONARY, ENTRY_GUIDE) |
| `1ab6c98` | Claude | Replace [DRAFT] placeholders with researched content |

Earlier history before this arc: see `git log --all` on the MWS repo or [project_docs_review.md](file:///C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md) Phase 3.1–3.5.

---

## 4. Critical doubts — read [DOUBTS.md](DOUBTS.md) before acting

Brief summary of the 15 doubts D1–D15:

**Blocking** — both now **RESOLVED (2026-05-23)**:
- [**D4**](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking) ✅ **consolidated to one paper.** The four parallel drafts became [PAPER.md](PAPER.md): grounded body + three condensed appendices, with §7 reframing the external frameworks as convergent triangulation rather than parallel publications.
- [**D8**](DOUBTS.md#d8--observable-framework-is-heavy-infrastructure-for-a-research-microsite--blocking) ✅ **keep Observable Framework.** Stack confirmed ([Decision 10](decisions/MICROSITE.md#decision-10--stack-observable-framework)); static SVG/PNG figures stay independent of it so the paper carries no build dependency.

**Important** (should be resolved before publication):
- [**D1**](DOUBTS.md#d1--is-block-economy-a-genuine-principle-or-print-economic-artifact--important): "block economy" might be a general property of all single-volume scholarly dicts, not MW-specific. Test against PWK / AP / WIL block matrices.
- [**D2**](DOUBTS.md#d2--the-lsl-mw-innovation-claim--under-checked--important): the L.-hedge "MW innovation" claim is under-checked. Verify WIL / Benfey / Cappeller don't have analogous markers.
- [**D5**](DOUBTS.md#d5--article-type-typology--14-is-too-many--overlapping--important): 14 article types have heavy overlap. Distinguish "primary article types" from "orthogonal properties."
- [**D6**](DOUBTS.md#d6--block-detection-is-regex-based-and-approximate--important): regex-based block detection has known heuristic errors. Add a methodological limitations section.
- [**D9**](DOUBTS.md#d9--28-design-decisions-before-any-code--important): 28 decisions may be over-engineering before shipping anything. Consider v1 cut.
- [**D10**](DOUBTS.md#d10--csl-atlas-is-named-before-scoped--important): csl-atlas name committed before Phase-4 scope. Delay repo creation.
- [**D11**](DOUBTS.md#d11--russian-translations-bootstrapped-by-claude--important): RU translations need user review before publication.
- [**D13**](DOUBTS.md#d13--scope-creep-from-docs-pass-to-atlas--important): scope has grown without anything shipped. Declare v1 cut.

**Nice-to-resolve:**
- [**D3**](DOUBTS.md#d3--the-kosha-lineage-of-wil-is-over-narrated--nice-to-resolve), [**D7**](DOUBTS.md#d7--the-block-by-article-type-matrix-has-no-statistical-significance-test--nice-to-resolve), [**D12**](DOUBTS.md#d12--multi-normalisation-strategy-increases-reader-burden--nice-to-resolve), [**D14**](DOUBTS.md#d14--memory-file-inflation--nice-to-resolve), [**D15**](DOUBTS.md#d15--issue-tracker-as-cross-repo-task-management--nice-to-resolve).

The DOUBTS.md document closes with a **"What I'd cut if I had to"** section recommending a 1-week MVP path: keep the 5 pilot docs-passes + one paper (grounded) + one figure (heatmap) + EN-only; defer everything else.

---

## 5. What's pending — three explicit threads

### 5a. User review of the 5 pilot docs-passes

[@funderburkjim](https://github.com/funderburkjim) and [@Andhrabharati](https://github.com/Andhrabharati) are tagged on each issue. Awaiting:

- [MWS #195](https://github.com/sanskrit-lexicon/MWS/issues/195) — fact-check historical claims, WIL ← kosha lineage, kosha-citation counts, sample-entry annotations
- [csl-sqlite #1](https://github.com/sanskrit-lexicon/csl-sqlite/issues/1) — per-dict schema, release tag convention, CI gap
- [csl-inflect #15](https://github.com/sanskrit-lexicon/csl-inflect/issues/15) — examples, downstream consumers, SQLite schema
- [hwnorm1 #20](https://github.com/sanskrit-lexicon/hwnorm1/issues/20) — input/output schema, coverage, usage examples
- [COLOGNE #455](https://github.com/sanskrit-lexicon/COLOGNE/issues/455) — CROSSREF_INDEX accuracy, links currency

Once reviewed, **Phase 4 (org-wide rollout)** can proceed: waves of ~15 repos.

### 5b. Microanalysis publication path

**Decided (2026-05-23):** option (a)/(c) — **one consolidated paper** ([PAPER.md](PAPER.md)) for [IJL](https://academic.oup.com/ijl). The grounded reading is the body; the three external frameworks are condensed appendices and reframed in §7 as convergent triangulation. (The rejected alternative was splitting across different venues — Wiegand → German venue, A-R → *Lexikos*, Hausmann → *Lexicographica*.)

Still open: a final pre-submission pass on the [§9 limitations](PAPER.md#9-methodological-limitations) (regex spot-check, significance tests, the `L.`-innovation preface checks) and the planned Russian-language venue (per Decision 3, 6, 11).

### 5c. csl-atlas microsite

Per [D10](DOUBTS.md#d10--csl-atlas-is-named-before-scoped--important): repo not yet created. Should be scaffolded locally first (`D:/claude/csl-atlas/`) before pushing to org. Phase-4 dict coverage scope (which 9 dicts, in what order?) is unresolved.

---

## 6. Conventions and rules

### Linking rule (CRITICAL — applies everywhere)

Per [`feedback_issue_links.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/feedback_issue_links.md): **Every verifiable claim in issue bodies AND docs must be a hyperlink.** Files, sections, data points, editions, record numbers, abbreviations, dates, persons, works. Bare backticks only for short code tokens inside a sentence that already links the surrounding reference. **Codified in all 5 runbooks** under `sanskrit-lexicon-docs-review/runbooks/*.md`.

### Data attribution

Every figure caption: `Source: CDSL mw.txt 2026-05-23 · CC-BY-SA-4.0 · build {SHA}` (per Decision 5, 26, 28).

### Bilingual labels

EN + RU; Sanskrit terms in IAST italics inside both (per Decision 3, 6). Sanskrit is meta-level, not a label language.

### Mermaid i18n

One file per locale (`timeline-en.md` + `timeline-ru.md`), NOT parallel blocks in same file (per Decision 8).

### Issue body format

Tables / prose / checklists — every filename, section, record number, abbreviation linked. Use `[FILENAME](https://github.com/ORG/REPO/blob/docs-pass/FILENAME)` and section anchors `[when-to-use](FILE.md#when-to-use-this-dictionary)`.

### Branch + commit conventions

- Work happens on the `docs-pass` branch in each pilot repo
- Commits begin with `docs-pass:` prefix
- Use `Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>` (or `Claude Sonnet 4.6` if running on Sonnet) at end of message
- Never push to `master` directly

### Memory hygiene

Memory files at `C:/Users/user/.claude/projects/D--claude/memory/`. One fact per file. Update existing files rather than creating duplicates. See [`MEMORY.md`](file:///C:/Users/user/.claude/projects/D--claude/memory/MEMORY.md) for index.

---

## 7. Files to read first (priority order, for a new chat)

1. **This file** — HANDOFF.md
2. [DOUBTS.md](DOUBTS.md) — what NOT to take for granted
3. [VISUALISATIONS.md](VISUALISATIONS.md) — the catalogue + tier prioritisation
4. [decisions/README.md](decisions/README.md) — index of the 7 thematic decision sub-docs
5. [MICROANALYSIS.md](MICROANALYSIS.md) — the data backbone
6. [README.md](README.md) — index of the paper + consolidation/triangulation rationale
7. [PAPER.md](PAPER.md) — the consolidated submission paper (grounded body + triangulation + Appendices A–C)
8. [../../ROADMAP.md](../../ROADMAP.md) — MWS issue synthesis + quarterly plan
9. [../../DICT_PROFILE.md](../../DICT_PROFILE.md) — reader-facing MW profile (the most-developed docs-pass artefact)
10. [project_docs_review.md](file:///C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md) — full project history with phases 3.1–3.9

---

## 8. How to continue (concrete steps for the next chat)

**If reviewing what's been built:** start with #1–#3 above. Browse the [figures/](figures/) directory to see the actual rendered outputs.

**If continuing the build:**
1. Address blocking doubts in [DOUBTS.md](DOUBTS.md) §D4 (paper consolidation) and §D8 (Observable vs vanilla D3) BEFORE adding new infrastructure.
2. The four Tier-1 figures exist as SVG/PNG/HTML — consider adding Tier-2 figures (radar small-multiples, fingerprint icons, 5-dict comparison).
3. Russian translations in [locales/ru.json](figures/locales/) need user review (per [D11](DOUBTS.md#d11--russian-translations-bootstrapped-by-claude--important)).

**If pivoting to Phase 4 (org-wide docs-pass rollout):**
1. Wait for maintainer review of the 5 pilots (per HANDOFF §5a).
2. Apply the established pattern to waves of ~15 repos (see [`sanskrit-lexicon-docs-review/runbooks/`](file:///D:/claude/sanskrit-lexicon-docs-review/runbooks/)).
3. Each dict-repo docs-pass yields its own ROADMAP.md following the [MWS ROADMAP](../../ROADMAP.md) template.

**If continuing the cross-dict atlas:**
1. Per [D10](DOUBTS.md#d10--csl-atlas-is-named-before-scoped--important), scaffold `csl-atlas` locally first.
2. Generate per-dict block matrices using [mw_block_matrix.py](MICROANALYSIS.md#9--open-analytical-questions-for-the-four-framework-papers) extended to each of the 8 other dicts.
3. Re-run Tier-1 figure scripts against each.
4. Compose a per-dict "chapter" page per Decision 20.

**If addressing user feedback that landed in a new turn:**
- Read the latest user message carefully — they often push back on specific claims with evidence (e.g. the WIL "bare minimum" correction; the kosha-lineage assertion; the stale `mwab_input.txt` link; the WIL→PWK substitution in Option F).
- Verify their claim against data files before responding.
- Update docs in the same commit; don't accumulate fixes.

---

## 9. Cross-repo dependencies

| Repo | Status | Relevance |
|---|---|---|
| [csl-orig](https://github.com/sanskrit-lexicon/csl-orig) | Canonical | All `<dict>.txt` source files live here |
| [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork) | Active | Build system; `sqlite.py`, `generate_dict.sh`; operative `mwab_input.txt` lives at `v02/distinctfiles/mw/pywork/mwab/` |
| [csl-sqlite](https://github.com/sanskrit-lexicon/csl-sqlite) | docs-pass branch reviewable | SQLite distribution; pilot reviewed |
| [csl-app](https://github.com/sanskrit-lexicon/csl-app) | Active | Web display; UI improvements land here |
| [csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect) | docs-pass branch reviewable | Inflection tables; pilot reviewed |
| [hwnorm1](https://github.com/sanskrit-lexicon/hwnorm1) | docs-pass branch reviewable | Headword normalisation processing; pilot reviewed |
| [COLOGNE](https://github.com/sanskrit-lexicon/COLOGNE) | docs-pass branch reviewable | Org hub; pilot reviewed |
| [csl-homepage](https://github.com/sanskrit-lexicon/csl-homepage) | TBD | Where org-wide docs hub will live |
| `csl-atlas` (planned) | Not yet created | Phase-4 microsite (see [D10](DOUBTS.md#d10--csl-atlas-is-named-before-scoped--important)) |

---

## 10. Open questions for the new chat

Pick whichever is most actionable:

1. ~~**D4 paper consolidation**~~ ✅ **DECIDED** — one consolidated paper to IJL ([PAPER.md](PAPER.md)).
2. ~~**D8 microsite stack**~~ ✅ **DECIDED** — keep Observable Framework ([Decision 10](decisions/MICROSITE.md#decision-10--stack-observable-framework)).
3. **Russian translation review:** when can [@gasyoun](https://github.com/gasyoun) review the [bootstrap RU translations](figures/locales/ru.json)?
4. **Phase-4 scope:** which dicts join csl-atlas in what order? PWG first? AP90? GRA?
5. **MVP cut:** does the user accept the 1-week MVP path proposed in [DOUBTS.md §"What I'd cut if I had to"](DOUBTS.md#what-id-cut-if-i-had-to)?
6. ~~**Methodological limitations section**~~ ✅ **DONE** — added as [PAPER.md §9](PAPER.md#9-methodological-limitations) (regex limits, significance testing, cross-dict scope, `L.`-innovation checks, typology overlap), per [D6](DOUBTS.md#d6--block-detection-is-regex-based-and-approximate--important).
7. **csl-atlas repo creation:** is the user ready to create the repo on the sanskrit-lexicon org, or wait?
8. **Cross-dict block matrices:** should we extend the analysis to PWG / AP / WIL / SKD / PWK / VCP for the Phase-4 atlas? (Would also settle whether [block-economy is MW-specific](PAPER.md#9-methodological-limitations).)

---

## 11. Quick environment facts

- **Working directory:** `D:/claude/` (Windows; PowerShell + Bash both available; **no `find`/`grep`/`cat` via Bash — use Glob/Grep/Read tools**)
- **MWS local clones (two, same `origin`):** `C:/Users/user/Documents/GitHub/MWS/` (the GitHub-Desktop clone — **now the active working copy**, on `docs-pass` as of 2026-05-23) and `D:/claude/mws_repo/` (also on `docs-pass`). Both track `origin/docs-pass`; commit/push in one, then `git fetch && git pull` in the other to avoid divergence.
- **Other pilot repos:** `D:/claude/csl-sqlite_repo/`, `D:/claude/csl-inflect_repo/`, `D:/claude/hwnorm1_repo/`, `D:/claude/cologne_repo/`
- **Docs-review workspace:** `D:/claude/sanskrit-lexicon-docs-review/` (runbooks, templates, hand-offs)
- **Data files (downloaded for analysis):** `/tmp/mw.txt`, `/tmp/pwg.txt`, `/tmp/ap.txt`, `/tmp/wil.txt`, `/tmp/skd.txt`, `/tmp/pw.txt`, `/tmp/vcp.txt`, plus the four koshas `armh.txt`, `abch.txt`, `acph.txt`, `acsj.txt`
- **Today's date:** 2026-05-23
- **CDSL data freshness:** as of 2026-05-23 fetch from `csl-orig/master`

---

## 12. Acknowledgments

This work is a collaboration between [@gasyoun](https://github.com/gasyoun) (Mārcis Gasūns, CDSL member) and Claude (multiple sessions across Opus 4.7 and Sonnet 4.6). The four-paper microanalysis, the 28-decision visualisation design, the 5-pilot docs-pass, the WIL-kosha lineage proof, the citation markers callout, and the typology of MW article types are joint products. Where mistakes appear in the analysis, they are Claude's; where the project is interesting, they are [@gasyoun](https://github.com/gasyoun)'s.

---

**End of HANDOFF.** A new chat session reading this file from top to bottom — plus [DOUBTS.md](DOUBTS.md), [VISUALISATIONS.md](VISUALISATIONS.md), [decisions/README.md](decisions/README.md), and [project_docs_review.md](file:///C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md) — should be productive within minutes.
