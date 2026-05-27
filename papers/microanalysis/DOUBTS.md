# DOUBTS.md — critical review of architecture decisions

**Mandate (2026-05-23):** [@gasyoun](https://github.com/gasyoun) — "Review everything. Doubt everything, all architecture solutions."

This document records honest reservations about the 28 design decisions in [VISUALISATIONS.md](VISUALISATIONS.md), the 4-paper plan in [README.md](README.md), and the broader docs-pass + microanalysis + atlas trajectory. Each doubt is rated **blocking** (must be resolved before further build) / **important** (should be resolved before publication) / **nice-to-resolve** (can ship without).

The goal is not to undo decisions but to make their weaknesses visible. If a doubt survives scrutiny, it should be documented as a known limitation in the paper(s) rather than hidden.

---

## Substantive doubts about the analytical claims

### D1 — Is "block economy" a genuine principle or print-economic artifact? · *important*

> **Result ([analysis/CROSS_DICT.md](analysis/CROSS_DICT.md)):** the doubt is borne out. The block-economy *shape* (small modal kernel + long tail) is **general to all eight CDSL dictionaries**, not MW-specific (modal blocks/entry: MW 5, PWG 4, PWK 3, AP 2, WIL 3, Benfey 3). PWG is ~4× denser per entry. PAPER.md §4 and §9.3 now soften the claim to "characteristic of single-volume scholarly dictionaries." A per-type follow-up ([analysis/CROSS_DICT_PROFILES.md](analysis/CROSS_DICT_PROFILES.md)) now covers all nine dicts: **single-volume** dicts differentiate `<lex>` types (MW 11.3, PWK 7.7, AP 15.2 pts) while **multi-volume PWG cites uniformly** (0.4) — type-differentiation is itself a single-volume economy. The **Sanskrit-Sanskrit lexica (SKD/VCP)** fall outside the framework (no `<lex>`/`<ls>`; inline `iti` citation) — the apparatus is genre-bound to structured bilingual dicts.


Our [paper](PAPER.md#4-the-block-economy-thesis) names "block economy" as MW's defining structural choice: a 6-block kernel reused across 286,561 entries with type-driven enrichment. But this could be just a **side-effect of being a single-volume print dictionary** — every printed dictionary economises blocks to fit pages. PWK (also single-volume, also condensed) might exhibit identical economy without anyone calling it a principle.

**Test:** compute the same kernel statistic for PWK / AP / WIL. If they all show the same 5–7 modal kernel, then "block economy" is a general property of all single-volume scholarly dictionaries, not MW-specific. The grounded paper would need to weaken its claim to *"MW exhibits the block economy characteristic of single-volume scholarly dictionaries"* — still publishable, less striking.

**Fix:** add Phase-4 cross-dict block matrices and compare kernels. Currently asserted on MW data alone.

### D2 — The `<ls>L.</ls>` claim, refined: MW *systematised* a convention pioneered typographically · *resolved 2026-05-27*

> **Resolution.** Print-preface read of Cappeller 1891 and Benfey 1866 (Wilson 1832 OCR partial; convention not attested in digital record) ([analysis/LS_HEDGE_CHECK.md §"Print-preface read"](analysis/LS_HEDGE_CHECK.md#print-preface-read-added-2026-05-27-closes-the-digital-only-gap)) establishes that the *concept* of an inline lexicographer-only hedge predates MW by 33 years. Cappeller 1891 defines asterisk `*` as "a word taught only by grammarians or lexicographers" — semantically the *exact* analogue of MW's `<ls>L.</ls>` — and Cappeller co-edited MW 1899, making the lineage direct. Benfey 1866 dagger `†` is a weaker variant ("no authoritative references"). **The "MW innovation" claim is downgraded:** MW's innovation is *structural* (promoting the hedge into the source-citation slot — 40,212 `<ls>L.</ls>` tags occupy the same XML position as `<ls>MBh.</ls>`), not *semantic* (the conceptual marker is older). [PAPER.md §7.2(ii)](PAPER.md#72-three-findings-all-three-frameworks-reach) and [Appendix C §C.2](PAPER.md#appendix-c--the-hausmann-wiegand-comment-class-reading-condensed) have been rewritten accordingly.

> **Earlier digital-record evidence:** MW has 40,212 `L.` hedges; PWG (of 570,817 `<ls>` tags), PWK, WIL, CAE, SKD, VCP have 0; AP has 1; Benfey 1866 has 0 of 14,708 `<ls>` tags (because his hedge is the typographic dagger `†`, not a tagged `<ls>`). The CDSL digitisation of CAE has 0 `<ls>` tags but uses `*` (1,370×) and `†` (903×) typographically — now interpretable from the 1891 print preface above.

> **Residual:** Wilson 1832 print preface not yet OCR-fetched in this pass; digital record shows 224 of 230 `<ls>` tags as `<ls>Rox.</ls>` and no inline-hedge pattern. WIL is treated as "no clear preface convention attested" — a future preface read could refine this but does not change the resolution direction (the precedents that matter are Benfey and Cappeller, both confirmed).

### D3 — The kosha-lineage of WIL is over-narrated · *nice-to-resolve*

We claim WIL is "the kosha tradition translated" based on (a) the subtitle ("learned natives at Fort William College") and (b) CDSL's `koSa` subject classification. The evidence is strong for *direction* but weak for *exclusivity*. Wilson's 1832 preface explicitly says he consulted **both** indigenous lexicographers (pandits) **and** European Sanskritists; his references list includes both Sanskrit *nighaṇṭus* and European editions.

**Risk:** the binary "WIL ← Koshas, MW ← PWG" is too clean. Reality may be:
- WIL ← (Koshas + early European Sanskritology including Colebrooke, Carey)
- PWG ← (Koshas + Vedic textual corpus + WIL itself)
- MW ← (PWG + WIL + the Petersburg supplements + new textual discoveries)

**Fix:** soften the lineage diagram. Replace the binary "two ancestries" framing with a directed graph that acknowledges cross-influence.

### D4 — 4 framework papers from the same data — is this honest? · *blocking*

> **Resolution:** consolidated to **one paper** ([PAPER.md](PAPER.md)), per option (a) below. The data-grounded reading is the body; the Wiegand / Atkins-Rundell / Hausmann readings are condensed into [Appendices A–C](PAPER.md#appendix-a--the-wiegand-theoretic-reading-condensed) and reframed (in [PAPER.md §7](PAPER.md#7-triangulation-three-external-frameworks-converge)) as *convergent triangulation* rather than parallel publications. The four standalone `paper-*.md` drafts are retained in this directory as supplementary extended drafts, each banner-linked back to PAPER.md.

We wrote 4 papers each analysing the same 286,561 records through a different theoretical lens. The danger: **a journal may see this as salami-slicing** (one finding split into four publications). The IJL editorial board specifically flags multi-version submission of the same data.

**Test:** if all four papers were submitted to IJL simultaneously, would they survive? Probably not — they would be told to consolidate.

**Fix:** **submit one paper** (probably the grounded paper, which is the most original) and treat the other three as either:
- (a) Appendix sections of the main paper
- (b) Companion documents released as a methodology supplement to the main paper
- (c) Separate venues — Wiegand to a German Wiegandian journal, Atkins-Rundell to *Lexikos*, Hausmann to *Lexicographica*, grounded to IJL

Right now we're presenting 4 simultaneous parallel papers, which is unusual.

### D5 — Article-type typology — refactored to 8 primary types + 3 orthogonal properties · *resolved 2026-05-27*

> **Resolution.** The 14-bucket scheme has been refactored into **8 primary types** (root, nominal — with gender sub-feature; adjective; indeclinable; compound; derived; continuation; encyclopedic — with botanical/biographical sub-feature) and **3 orthogonal properties** (Vedic-accented, lex-hedged, IE-cognate-bearing). The orthogonal properties were exactly the cases where the old scheme overlapped with itself. The refactored typology is documented in [PAPER.md §5](PAPER.md#5-profiles-as-the-unit-of-typology) (replacing the 14-row table with an 8-row primary table plus a 3-row property table and an 8×3 cross-tabulation), and in [MICROANALYSIS.md §3](MICROANALYSIS.md#3--articletype-typology-8-primary-types--3-orthogonal-properties) (full 8×3 cross-tab). The original 14-bucket classification is preserved in [MICROANALYSIS.md §3.1](MICROANALYSIS.md#31--the-original-14-bucket-classification-legacy) for reproducibility and for anyone running the legacy detector.

> **Original observation that drove the refactor:** the 14 buckets contained four kinds of overlap — `noun_{m,f,n,mn}` differ only in gender (collapsed to *nominal* with gender as sub-feature); `vedic_accented` orthogonally overlaps with everything (promoted to property); `biographical` overlaps with `noun_m` for proper-name masculines (collapsed to *encyclopedic* with sub-feature); `lexicographer_only` is a citation pattern, not an article kind (promoted to *lex-hedged* property).

> **Residual:** The block-by-type matrix (MICROANALYSIS §4) still carries the legacy 14-row layout because the per-bucket percentages are still useful for replication. The §5 refactor presents an 8×3 cross-tabulation; the 14-row matrix is now read as "the per-property and per-sub-feature breakdown of the 8-type view."

### D6 — Block detection is regex-based and approximate · *important*

> **Result ([analysis/SPOTCHECK.md](analysis/SPOTCHECK.md)):** detector reproduces the 286,561 count exactly. Confirmed and quantified: **F08 over-counts** (36.5% of its hits are compound `<e>3*` members, not inflected forms); **F09 over-counts** (66.7% of hits outside any root/etymological context). Downgraded: the **F11 under-count is negligible** (+0.02 pts under a broader pattern). New: the §4 "display headword 99%" was the structural-key rate; the *rendered* `<s>` rate is **76%** (corrected). A 100-record labelled sample (`analysis/SPOTCHECK_SAMPLE.txt`, seed 42) awaits per-entry Sanskritist review.


The `mw_block_matrix.py` script uses regular expressions to detect 18 blocks. Several are heuristic:
- F09 (editorial commentary): detected by parenthetical with substantial content — over-counts when the gloss happens to use parentheses.
- F11 (sense division): under-counts because MW's sense markers vary (a) 1) — a) etc.
- F08 (inflection form): assumes ≥2 `<s>` tags means inflection forms — but compound sub-entries also use multiple `<s>` for the compound members.
- F18 (correction record): we detected via `{{` and `->` patterns; some legitimate uses of `{{` might be miscounted.

**Test:** spot-check 100 random entries against the algorithm's classifications. Currently we have 8 sample entries; ~5% error rate on the full set would meaningfully shift percentages.

**Fix:** add a "Methodological limitations" section to the working notes. Document the regexes and known false-positive/false-negative cases.

### D7 — The block-by-article-type matrix has *no* statistical significance test · *nice-to-resolve*

> **Result ([analysis/SIGNIFICANCE.md](analysis/SIGNIFICANCE.md)):** every headline contrast is significant at α = 0.05 (chi-square / Fisher; Wilson 95% CIs reported). The specific small difference this doubt named — noun_m F08 (21.6%) vs noun_f F08 (22.6%) — is **not significant (p = 0.07)**, confirming the concern; gender-level F08 differences are dropped as findings. Biographical F13 has a wide CI [59.6, 69.6] (N = 346) now stated in PAPER.md §9.2.


We report percentages like "F09 commentary at 78.1% in roots vs ~5% baseline." But:
- Roots are only 750 entries; small N means high variance.
- We do not compute confidence intervals.
- "Statistical significance" of a 73-percentage-point difference is uncontroversial, but the smaller differences (e.g. "F08 inflection at 22% in noun_m vs 23% in noun_f") may not survive a chi-square test.

**Fix:** for a journal paper, add chi-square or Fisher-exact significance tests on the contingency tables, and confidence intervals on the percentages.

---

## Substantive doubts about the design decisions

### D8 — Observable Framework is heavy infrastructure for a research microsite · *blocking*

> **Resolution:** **keep Observable Framework** ([Decision 10](decisions/MICROSITE.md#decision-10--stack-observable-framework)). The user accepts the build-pipeline and lock-in trade-offs in exchange for built-in i18n routing, reactive D3/Plot, and Markdown pages, which match the [per-locale-file strategy](decisions/I18N.md) and [JSON-data architecture](decisions/MICROSITE.md#decision-2--build-both-static-paper-and-interactive-microsite). The static figures remain plain SVG/PNG (already built), so the paper does not depend on Observable; the framework is used only for the interactive microsite. The mitigations below (pin the Framework version; keep the highest-interactivity tools isolated; ensure figures degrade to static) become *implementation notes* rather than reasons to switch stacks.

We chose Observable Framework as the microsite stack (Decision 10). Pros: i18n routing, reactive D3, Markdown pages. Cons:
- Requires Node + npm + build pipeline.
- Lock-in to Observable's evolution; their commercial pivot in 2024 created uncertainty.
- A research microsite typically lives for 5–10 years; can we maintain Observable Framework that long?
- Plain D3 + HTML + a small CSS file is simpler, more portable, longer-lived.

**Test:** check Observable Framework's stability commitments and migration history. If they have broken API changes between minor versions, that's a maintenance hazard.

**Fix candidate:** consider downgrading to **vanilla HTML + D3 + Vega-Lite** for static parts. Reserve Observable for the highest-interactivity tools (type comparator). The plain-HTML choice was an option we considered and rejected; revisit.

### D9 — 28 design decisions before any code · *important*

The decision document is now 1500+ lines. Many decisions specify things that may not survive contact with implementation. Examples:
- Decision 9 (JSON-first tokens with build script generating 4 downstream artifacts) — *might be over-engineered*. A simple CSS file with hex colours, plus matplotlib-readable hex strings, may suffice.
- Decision 28 (Git SHA in footer) — adds build complexity for marginal benefit; reviewers don't typically check SHAs.
- Decision 14 (triple a11y: alt + desc + caption) — comprehensive but every figure now needs 3 separate texts in 2 languages = 6 texts per figure.

**Fix:** before building, **review the decisions and demote 5–7 to "v2 enhancements"**. Start with the simplest viable build:
- v1: matplotlib SVG, hex colors in script, EN-only labels
- v2: add palette JSON
- v3: add RU locale
- v4: add a11y triplicate
- v5: add Observable Framework

The "all 28 decisions implemented" target is **premature optimization** for a project that hasn't shipped a single figure yet.

### D10 — csl-atlas is named before scoped · *important*

We chose `csl-atlas` as the microsite name and committed to "9-dict atlas" as the Phase-4 brief. But:
- We have not actually scoped the Phase-4 atlas. Which 9 dicts? In what order?
- The name commits us to "atlas" framing — but we may discover the right delivery is a *book*, a *paper series*, a *desktop application*, etc.
- A name change later is cheap; but commits to repos and URLs accumulate technical debt.

**Fix:** **delay the repo creation** until the atlas scope is approved. Scaffold locally first (as planned: `D:/claude/csl-atlas/`). Push to the org only when scoped.

### D11 — Russian translations bootstrapped by Claude · *important*

Decision 11 commits to me bootstrapping Russian translations. My Russian indological terminology is good but not authoritative. Specific risks:
- Calques may sound non-native ("лексикограф-only" was already flagged).
- Terminology may inconsistently mix Soviet-era (post-1917) vs pre-revolutionary conventions.
- IAST inside Russian text is the right choice (Decision 6) but inline mixing may cause typesetting issues.

**Fix:** I'll bootstrap with maximum humility. Every Russian string gets a confidence flag (high/medium/low/uncertain). Low-confidence strings get `(?)` markers for review. **Do not publish any RU material until the user reviews.**

### D12 — Multi-normalisation strategy increases reader burden · *nice-to-resolve*

Decision 4 commits to using different normalisations for different figures, with each caption explaining its normalisation. The risk: readers won't read the captions; they'll see "PWG is 4× denser" in one figure and "PWG is 2.4× denser" in another and conclude the paper contradicts itself.

**Fix:** in the main paper, settle on **one canonical normalisation** (probably Option B per-entry) and use it for all narrative comparisons. Save the other normalisations for the methodology section ("we considered these normalisations and chose B because…").

---

## Architectural doubts

### D13 — Scope creep from "docs-pass" to "atlas" · *important*

Project trajectory:
1. Started: docs-pass for MWS (one repo)
2. Grew: 5-pilot docs-pass (5 repos)
3. Grew: typology + stats + lineage + roadmap
4. Grew: 4-paper microanalysis
5. Grew: visualisation catalogue
6. Grew: csl-atlas for 9 dicts
7. Grew: 28 design decisions

This is normal feature creep. **But none of it has shipped.** No PR merged. No paper submitted. No figure rendered.

**Fix:** declare a **v1 cut**: merge the docs-pass into MWS master, ship one figure (the heatmap), and call it a release. Then plan v2 from real reviewer feedback rather than from imagination.

### D14 — Memory file inflation · *nice-to-resolve*

The project memory file now has 9 distinct phases (3.1 through 3.9 and counting). Each is a substantial section. The MEMORY.md global index is being grown to maintain the recent project. Some risk of:
- Future Claude sessions skipping the most-recent phases (they're newest at the file top but become voluminous quickly).
- Cross-references between phases proliferating without an explicit "current state" pointer.

**Fix:** at end of session, **collapse memory to a "current state" + "archive"** — keep one canonical "where are we now?" snapshot at the top.

### D15 — Issue-tracker as cross-repo task management · *nice-to-resolve*

We've used GitHub issues across MWS / csl-sqlite / csl-inflect / hwnorm1 / COLOGNE. Cross-repo dependencies in the roadmap point to csl-pywork, csl-app, etc. But:
- GitHub doesn't natively cross-link issues across repos.
- The roadmap notes "Q1: address #178, #147, #73" without organizing by repo first.
- A single contributor working across 5+ repos will need to keep mental state on which issue is where.

**Fix:** consider a **central tracking issue in COLOGNE** that mirrors the per-repo work plans. Or a project board across the org. Or accept the limitation.

---

## What I'd cut if I had to

If forced to ship in 1 week with no further refinement:

1. **Keep:** the 5 pilot docs-passes; DICT_PROFILE; ENTRY_GUIDE; DATA_DICTIONARY; CONTRIBUTING; CITATION; ROADMAP; MICROANALYSIS data file; ONE figure (heatmap); ONE paper (grounded).
2. **Cut:** the four-paper plan → one paper. Cut three of four framework papers (keep grounded, demote others to appendix).
3. **Cut:** csl-atlas microsite → deliver as static figures only. Defer interactive to v2.
4. **Cut:** Russian translations → English-only first; add RU in v2.
5. **Cut:** the multi-normalisation strategy → pick one (per-entry) and stick with it.
6. **Cut:** 28 design decisions → 8 core decisions (palette, attribution, figure dimensions, font, license, accessibility, supp materials, bilingual labels).

This minimum-viable product would ship in 1 week and be a legitimate scholarly contribution. The current trajectory ships in 3+ months and may not be substantively better.

---

## Recommended next steps (in priority order)

1. **Ship one figure** (the heatmap, in English, with reasonable defaults) — *break the no-code spell*.
2. **Submit the grounded paper to IJL** with the heatmap as Figure 1 — *get reviewer feedback*.
3. **From reviewer feedback**, decide whether to expand to: comparative cross-dict figures · Russian publications · csl-atlas microsite · the other three framework papers.
4. **Phase 4 docs-pass** for other CDSL dicts proceeds in parallel; figures generated per-dict using the established pipeline.

**Don't build the atlas until the heatmap is rendered.** Don't write the four-paper preface until one paper is submitted. Don't commit to Russian until English ships.

---

## Status

This doubt review is itself a deliverable: it documents the project's known-unknown surface area as of 2026-05-23. Any of the 15 doubts above could be a paper-revision point or a Phase-4 design correction. Better to surface them now than to discover them in peer review.

**The next operational step** — over the user's 4-hour absence — is to ship the heatmap figure. That single act resolves D9 (we'll see what survives contact with implementation) and gives D4 a concrete artifact to revolve around.
