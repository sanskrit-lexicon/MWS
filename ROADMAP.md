# MWS Roadmap — 2026 H2

Forward plan for June–November 2026, superseding the 2026-05-27 snapshot.
It sequences four workstreams chosen 2026-06-12 and bakes in a model-tier
policy so that frontier-model (Fable-class) sessions are spent only where
judgment is required.

Sources: the 34 open [MWS issues](https://github.com/sanskrit-lexicon/MWS/issues),
the [docs-pass microanalysis](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis),
the [csl-atlas](https://github.com/sanskrit-lexicon/csl-atlas) M1–M8 cross-dictionary methods,
the [Salt API integration roadmap](https://github.com/sanskrit-lexicon/csl-standards/blob/main/docs/SALT_API_INTEGRATION_ROADMAP.md),
and the SanskritLexicography 12-month publication roadmap (P1–P6).

---

## Status snapshot (2026-06-12)

| Metric | Value |
|---|--:|
| Records in [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) | 286,561 |
| Open issues | 34 |
| Closed issues (historical) | 157 |
| Closed in last 12 months (velocity signal) | 4 |
| `<ls>` citation instances (measured 2026-06-13, live mw.txt) | **312,160** |
| Distinct bare `<ls>` abbreviations (locator stripped) | ~895 (≈821 after variant folding) |
| Authority records on disk ([mwauthorities_init.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/mwauthorities_init.txt)) | **568** (≥`<expandMW>`); **230** also carry `<expandNorm>` |
| Distinct canonical authorities linked from text | 513 (via 650 text-spelling variants) |
| **True orphans (cited authority with no record at all)** | **~0** — every canonical authority cited already has a record |
| `<ls>` citations carrying a numeric locator | 59.8% (40.2% are bare abbreviations) |
| **Meta / hedge / relative citations** (`L.`+`ib.`+`W.`+`MW.`+`Cat.`) | **69,603 = 22.3%** — structurally cannot link to a primary-text scan |
| Vedic accent coverage | 16.6% of `<k2>` fields |
| `<ls>L.</ls>` lexicographer hedges | 40,212 (12.9% of citations) — unique to MW among CDSL dicts |
| `<etym>` tags (IE cognate forms; **absent from DATA_DICTIONARY**) | 2,637 |

> **Correction (2026-06-13):** the previous snapshot's "232 with authority record
> (28.3%) / 589 orphans" was re-derived by direct inspection and found to be a
> **measurement artifact**: the 232 ≈ the **230 records carrying `<expandNorm>`**,
> not record existence. 568 records already exist; there are essentially **no true
> orphans**. W1 is therefore three distinct jobs, not one — see §W1. The
> "64%→85% coverage" target also collides with the 22.3% meta-citation ceiling
> above and the 40.2% bare-locator gap: the scan-linkable-to-primary-text fraction
> is well below 85%. *Reprioritization pending maintainer decision.*

**Velocity note:** ~1 issue/month sustained, bursts when a maintainer is active.
Everything below is therefore decomposed into self-contained, resumable units.

---

## Model-tier policy (how to not waste frontier-model budget)

Default rule: **Fable-class models decide; cheaper tiers execute.** A frontier
session should end with either a decision recorded in a doc/issue or a batch
spec that a cheaper agent can run without judgment.

| Tier | Use for | Concrete MWS examples |
|---|---|---|
| **Fable / Opus (judgment)** | Monthly planning review; scholarly adjudication; markup-policy decisions; paper prose and peer-review responses; designing batch specs and acceptance criteria | Alternate-form markup decision ([#178](https://github.com/sanskrit-lexicon/MWS/issues/178)/[#147](https://github.com/sanskrit-lexicon/MWS/issues/147)/[#73](https://github.com/sanskrit-lexicon/MWS/issues/73)); P1 gold-sample disagreement adjudication; choosing the top-orphan authority editions; Salt API contract questions |
| **Sonnet (skilled execution)** | Authority-record drafting from a spec; correction batches with the temp_mw_N workflow; analysis scripts; issue triage | One authority record per session from the orphan queue; running and interpreting `xmlchk` validation |
| **Haiku (mechanical)** | Lint passes, link checks, table regeneration, label hygiene, doc refresh sweeps | `/cologne-haiku-refresh`-style passes; regenerating coverage stats after each authority batch |

Session discipline:

- One Fable planning/review session per month (first week), working from this
  file and `.ai_state.md`; it re-prioritizes, adjudicates queued questions, and
  writes the next month's batch specs.
- Never use a frontier session to *execute* a spec it could have delegated —
  if the work is "apply known rules to N items", it belongs a tier down.
- Every session, any tier, updates `.ai_state.md` before ending (org protocol).

---

## Workstream W1 — `<ls>` source apparatus (three layers, not "589 orphans")

**Reframed 2026-06-13.** Direct inspection killed the "589 orphans / create
records from scratch" framing (see status-snapshot correction). 568 records
already exist; ~0 are true orphans. The real work is three distinct, much
smaller jobs with very different effort and value — **priority order is the
open decision** (W1 rescope question):

| Layer | Size | Effort | Value | Tier |
|---|---|---|---|---|
| **(a) Link unlinked text variants** | ~171 (821 text-side − 650 linked) | mechanical | closes tooltip/resolution gaps | Haiku/Sonnet |
| **(b) Add `<expandNorm>`** to records that have only `<expandMW>` | 338 (568 − 230): 273 `ti` (mostly mechanical hyphen-join, e.g. `adButa brAhmaRa`→`adButa-brAhmaRa`; some single-word titles need no work at all) + 43 `au` + 22 litcat/subti | **~1–2 sessions, not months** — scriptable draft + review | raises the docs-pass metric; cleaner MDF/TEI exports. NB the metric itself is flawed: it counts single-word titles that are already normal as "missing" | Sonnet (Fable for the 65 attributed/author cases) |
| **(c) Scan-link targets** per work | per-work, slow | scholarly (edition ID + pagination) | the real "unlock thousands of cites" leverage — but capped (see below) | Sonnet + Fable for edition calls |

**Hard ceiling on layer (c):** 22.3% of all citations are meta/hedge/relative
(`L.` 40,212 · `ib.` 10,094 · `W.` 8,285 · `MW.` 5,710 · `Cat.` 5,302) and can
never point to a primary-text scan; another 40.2% are bare (no locator). So the
realistic scan-linkable-now ceiling is far below the old "85%" target. **But `ib.`
is recoverable:** the resolver in
[relative_refs/](https://github.com/sanskrit-lexicon/MWS/tree/master/relative_refs)
resolves **7,538 of 10,094 (74.7%)** `ib.` citations to a real text source
(`MBh.` 1,149, `RV.` 1,064, …) by document-order antecedent walk — moving them
out of the meta set. The `id.` analog (4,401, [#98](https://github.com/sanskrit-lexicon/MWS/issues/98))
is sense-level and display-policy-gated (spec only).

**Top sources by citation weight** (bare-form counts, live): `MBh.` 22,990 ·
`RV.` 9,707 · `R.` 9,049 · `BhP.` 6,979 · `Kathās.` 5,926 · `Suśr.` 5,690 ·
`ŚBr.` 5,493 · `Hariv.` 5,229 · `AV.` 4,971 · `Kāv.` 4,662 · `Mn.` 3,519. Pāṇ.
(citation-weighted ~8,500) is spread across thousands of *sūtra-locator* strings,
which is why it needs a sūtra→scan scheme, not a page record — same family as the
2021 [Pāṇini link-target work](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities/ls/20211005-panini).

**Unit of work for layer (c)** (Sonnet-tier, one per session, resumable):
1. Pick next high-weight source.
2. Confirm the edition MW cited (MW's "Sources of the work" preface + [mwauthorities](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) precedents; Fable only when ambiguous).
3. Locate a scan (archive.org), verify pagination against 3–5 sample citations.
4. Add/extend the record + scan map; document in an issue.

**Targets:** TBD once layer priority is chosen. Coverage targets to be
recomputed per layer against the live 312,160-citation base, not the inherited 85%.

## Workstream W2 — P1 paper: MW block economy → IJL (Q3 2026)

**Goal:** submit *"The block economy of Monier-Williams"* to the International
Journal of Lexicography, per the publication roadmap (P1, feeds monograph Ch. 3).

State: paper consolidated on the [docs-pass branch](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis)
(PAPER.md, doubts D1–D22 closed, RU version, IJL cover letter drafted).

**Remaining steps:**
1. **G5 gold sample (blocker):** 200-entry MW sample, double-annotated for block
   types; compute precision/recall per block (F01–F18) against the automated
   detectors in [analysis/](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis/analysis).
   Annotation passes = Sonnet ×2 independent; disagreement adjudication = Fable.
2. Fold gold-sample numbers into PAPER.md §limitations; re-run `check_docs.py` consistency suite.
3. Merge or finalize docs-pass ([#195](https://github.com/sanskrit-lexicon/MWS/issues/195)) so cited URLs are stable.
4. Final hostile-review pass (Fable, one session), then format to IJL house style and submit.

**Target:** submission by end of August 2026.

## Workstream W3 — Salt API MW pilot (csl-apidev Phases 1–2)

**Goal:** MW live behind C-SALT-compatible REST + GraphQL endpoints, proving
the pipeline before any scale-out decision (Phase 3 gate).

State: docs complete in [csl-apidev/doc/](https://github.com/sanskrit-lexicon/csl-apidev/tree/master/doc)
(salt_entries, salt_ids, salt_graphql, cleanurl); Phase 1 skeleton tracked in
[csl-apidev#46](https://github.com/sanskrit-lexicon/csl-apidev/pull/46); normative profile in
[csl-standards#2](https://github.com/sanskrit-lexicon/csl-standards/issues/2);
simple-search v1.2 handoff in [csl-apidev#47](https://github.com/sanskrit-lexicon/csl-apidev/issues/47).

**Remaining steps:**
1. Land Phase 1 (`salt_entries.php` + `salt_ids.php`, PHP-native search, MW only) — Sonnet implementation, Fable only for contract questions.
2. Parity check against live C-SALT MW responses (scripted; report diffs as a table to the loss report).
3. Phase 2 GraphQL (`webonyx/graphql-php`, type `mw`).
4. Clean-URL `/MW/{ref}` content negotiation, dict-code whitelist.
5. Write the Phase 3 decision memo (expand to 7 C-SALT dicts vs all ~40) into [DECISIONS_NEEDED.md](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/docs/DECISIONS_NEEDED.md) — Jim's call.

Note: deployment depends on the Cologne server (Jim); local work stops at
tested PR + parity report. Event-driven, not polled.

## Workstream W4 — MW as template for the other dictionaries

**Goal:** convert what the atlas analyses proved about MW's markup into
concrete, reusable upgrades for the markup-poor dictionaries — and fix MW's own
documented weaknesses while doing so (they define the template's limits).

Four tracks, in leverage order:

1. **Siglum alias consolidation (cross-dict, cheap, big).** The org-wide `<ls>`
   apparatus has 13,021 raw sigla folding to 9,180, with ~265 prefix-clustered
   families awaiting alias review
   ([dict-source-aliases.json](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/data/dicts/dict-source-aliases.json),
   `scripts/obs/siglum_families.py`). Haiku generates candidates; Fable reviews
   merges in monthly batches of ~50. Also clears the 449 "unknown" MW
   source-layer sigla in [mw-source-layers.json](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/data/mw-source-layers.json).
2. **`<lex>` grammar-tag retrofits.** Only 5 dicts (MW, AP, PWG, PWK, WIL) are
   grammar-reliable. MW's `<lex>`/`<info lex>` model is the template; pilot a
   retrofit on one tag-bearing-but-unreliable dictionary (candidate from atlas
   coverage matrix), MW-style `<info>` packets emitted by rule, sampled by Fable.
3. **Register B — indigenous citation infrastructure for SKD/VCP.** MW's `<ls>`
   Register A *cannot* be forced onto SKD/VCP (zero `<ls>` by design; citations
   live in prose `iti` quotatives — 69,215 in SKD). Build the M4-style
   indigenous normalizer the atlas proposes
   ([CITATION_REGISTERS.md](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/CITATION_REGISTERS.md))
   instead. This also feeds papers P3/P4.
4. **Sense structure — surface it for cross-dict tooling (not a retrofit).**
   The old "MW has no sense markers" premise was **revised** (register #1):
   MW's sense unit is the record (`¦` + `<e>`-letter code). So the job is not a
   `<div>` retrofit but a small adapter that exposes record-grouped senses to the
   atlas sense-depth pipeline (which currently only reads `<div>`). Cheap; lands
   MW into the cross-dict sense comparison it was wrongly excluded from.
5. **`<ls>L.</ls>` → corpus verification (DONE, both snapshots, 2026-06-13).**
   Shipped in [lexicographer_dcs/](https://github.com/sanskrit-lexicon/MWS/tree/master/lexicographer_dcs):
   of **18,930** strict purely-lexicographic MW lemmas (no text witness, known
   only from kośas), **30.2% are attested in DCS-2021 and 31.4% in DCS-2026** —
   stable across two independent corpus snapshots (so not a version artefact),
   hedges that corpus evidence can re-examine. Strong tier = bands 2–3 (~2,330
   plant/medical/technical terms). IAST→SLP1 join validated (11/5,723 drift).
   Bridges P3 (citation registers) + the grammar-corpus-dict crosswalk.
   Next: hand-verify the ~180 band-3 lemmas into a P3-ready core; sense-level
   for the 10,264 partially-hedged lemmas (needs sense-tagged corpus).
7. **Root crosswalk MW↔Whitney↔DCS (built 2026-06-13).**
   [root_crosswalk/](https://github.com/sanskrit-lexicon/MWS/tree/master/root_crosswalk)
   is Layer-1 of the grammar-corpus-dict crosswalk: of 935 Whitney roots, **550
   (58.8%) are fully triangulated** (MW gloss + Whitney grammar + DCS frequency).
   Anchoring is near-clean (3/795 unmatched). Two spin-offs: a 40-root
   `<info whitneyroots>` anchoring batch (common verbs MW left untagged), and 259
   corpus-absent roots as a P3/P4 signal. Westergaard layer (1,362) not yet joined.
6. **phw cross-reference graph (audited 2026-06-13).**
   [phw_graph/](https://github.com/sanskrit-lexicon/MWS/tree/master/phw_graph)
   maps MW's undocumented phrasal-headword graph (2,364 edges, 99.3% reciprocal)
   — a queryable structured-data layer. Two concrete spin-offs: **(i)** a
   `bug`+`markup` batch fixing the **31 broken links** (`phw_integrity.csv`);
   **(ii)** document the `phwchild`/`phwparent`/`<lex type="phw">` family and
   `<etym>` (2,637 tags) in [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DATA_DICTIONARY.md).

---

## Monthly cadence (2026 Jun–Nov)

Each month: 1 Fable planning session, ~4 Sonnet execution sessions, Haiku sweeps as needed.

| Month | W1 authority | W2 paper | W3 Salt API | W4 template |
|---|---|---|---|---|
| **Jun** | Template + tracking issues; first 2 records (ŚBr., Kathās.) | G5 gold-sample spec + first annotation pass | Land Phase 1 PR locally; parity script | Siglum alias batch 1 (50) |
| **Jul** | 5 records (Suśr., Kāv., VarBṛS., Rājat., Pañcat.) | Second annotation pass; adjudication; fold into paper | Parity report; Phase 2 GraphQL start | Alias batch 2; MW unknown source-layers triage |
| **Aug** | 5 records (Ragh., KātyŚr., Yājñ. + 2); Pāṇ. scheme decision | Hostile review; IJL formatting; **submit** | GraphQL done; clean-URL routing | Alias batch 3; pick `<lex>` retrofit pilot dict |
| **Sep** | 5 records | (referee wait) | Phase 3 decision memo → DECISIONS_NEEDED | `<lex>` retrofit pilot run + sample review |
| **Oct** | 5 records | Revisions if back | Support Jim deployment as needed | Register B `iti` extractor prototype (SKD) |
| **Nov** | Top-25 complete; coverage re-measured | — | — | MW sense-`<div>` decision document |

Standing low-tier queue (fill idle capacity, any month): quick-win issues
[#192](https://github.com/sanskrit-lexicon/MWS/issues/192),
[#183](https://github.com/sanskrit-lexicon/MWS/issues/183),
[#86](https://github.com/sanskrit-lexicon/MWS/issues/86); close
[#168](https://github.com/sanskrit-lexicon/MWS/issues/168) and
[#90](https://github.com/sanskrit-lexicon/MWS/issues/90) as superseded by
[DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DATA_DICTIONARY.md) /
[ENTRY_GUIDE.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md);
link-targets [#185](https://github.com/sanskrit-lexicon/MWS/issues/185),
[#186](https://github.com/sanskrit-lexicon/MWS/issues/186),
[#187](https://github.com/sanskrit-lexicon/MWS/issues/187) fold into W1's queue.

---

## MW markup — known-weaknesses register

Documented by the atlas/microanalysis work; listed here because each one
bounds what W4 may copy into other dictionaries.

| # | Weakness | Evidence | Consequence |
|---|---|---|---|
| 1 | ~~No structural sense markers~~ **Revised 2026-06-13** — MW's sense unit *is* the record: **282,199 of 286,560 records carry exactly one `¦` gloss** (only 3 have two; **0** use `(a)…(b)` or `1)…2)` in-prose enumeration). 92,670 letter-suffixed `<e>` codes (1A/2A/3A…) are continuation senses. | measured on live mw.txt; `agni`/`Darma` each explode one-sense-per-record | **Not a weakness — a positive paper result (W2).** Atlas excluded MW from [sense-depth.json](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/data/dicts/sense-depth.json) only because its detector reads `<div>`, not record-boundary+`¦`. Cross-dict tooling needs to group records; the data is fully machine-readable |
| 2 | **22.3% of citations are meta/hedge/relative + 40.2% bare** | measured 2026-06-13: `L.`+`ib.`+`W.`+`MW.`+`Cat.` = 69,603; bare-locator from [CITATION_REGISTERS.md](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/CITATION_REGISTERS.md) | Scan-linkable-to-primary-text ceiling is well under 85%; `ib.` (10,094) needs antecedent-resolution first ([#98](https://github.com/sanskrit-lexicon/MWS/issues/98) family) |
| 3 | **Siglum chaos** — case/diacritic variants, ~265 prefix families | 13,021 raw → 9,180 folded sigla org-wide | Inflates the orphan count; W4 track 1 attacks this |
| 4 | **Shallow microstructure by design** — derivatives/preverbs promoted to headwords | M1 density 0.48 vs PWK 3.77, PWG 2.35; M2 = 0 | MW is the wrong template for subentry-rich targets; use PWG/PWK there |
| 5 | **Homonym splitting partly discretionary** | 64–65% split concordance with PWG/PW | Homonym numbering can't be mechanically reconciled cross-dict |
| 6 | **Accent confined to `<k2>`** and only 16.6% covered | ENTRY_GUIDE accent stats | Lemma normalization loses accent; Vedic work needs GRA cross-check |
| 7 | **No DTD/schema** — tag soup validated only by the build pipeline | no schema file in repo | Every consumer re-implements parsing; argues for the csl-standards interop layer, not for copying tags verbatim |
| 8 | **`<ls>L.</ls>` hedge is untyped** | 40,213 instances; no MDF slot ([MDF_EXPORT_MAPPING.md](https://github.com/sanskrit-lexicon/csl-standards/blob/main/docs/MDF_EXPORT_MAPPING.md)) | Unique evidential innovation, but lossy in every export; needs explicit evidence-class in the interop model |

---

## Cross-repo dependencies

| Repo | Role in this roadmap |
|---|---|
| [csl-orig](https://github.com/sanskrit-lexicon/csl-orig) | Canonical mw.txt — all text corrections land here (validated, then committed) |
| [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork) | Build + validation (`generate_dict.sh`, `xmlchk_xampp.sh`); server-side `redo_xampp_selective.sh` refresh is Jim-triggered |
| [csl-atlas](https://github.com/sanskrit-lexicon/csl-atlas) | M1–M8 evidence base for W4; siglum tooling; learner's-layer landing site |
| [csl-standards](https://github.com/sanskrit-lexicon/csl-standards) | Salt API profile, interop model, MDF mapping — W3/W4 normative home |
| [csl-apidev](https://github.com/sanskrit-lexicon/csl-apidev) | W3 implementation |
| [csl-corrections](https://github.com/sanskrit-lexicon/csl-corrections) | Audit trail for every mw.txt change |
| [csl-observatory](https://github.com/sanskrit-lexicon/csl-observatory) | DECISIONS_NEEDED.md — where maintainer-blocking decisions are parked |
| [mwauthorities/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) | W1 lands here |

---

## Deferred / long-running (unchanged from previous roadmap)

[#98](https://github.com/sanskrit-lexicon/MWS/issues/98) (resolve `id.`, 4,401 instances),
[#64](https://github.com/sanskrit-lexicon/MWS/issues/64) (cross-entry links),
[#76](https://github.com/sanskrit-lexicon/MWS/issues/76)/[#75](https://github.com/sanskrit-lexicon/MWS/issues/75) (inflection, needs csl-inflect),
[#163](https://github.com/sanskrit-lexicon/MWS/issues/163) (GRA-style grouping),
display bundle [#37](https://github.com/sanskrit-lexicon/MWS/issues/37)/[#108](https://github.com/sanskrit-lexicon/MWS/issues/108)/[#170](https://github.com/sanskrit-lexicon/MWS/issues/170)/[#180](https://github.com/sanskrit-lexicon/MWS/issues/180),
~~[#74](https://github.com/sanskrit-lexicon/MWS/issues/74) (botanical export)~~ **DONE** → [botanical_glossary/](https://github.com/sanskrit-lexicon/MWS/tree/master/botanical_glossary) (8,923 `<bot>` → 7,063 headwords / 1,223 species FAIR dataset; 72% lexicographer-only, 1,528 clean L.-only+DCS-attested plant lemmas),
[#24](https://github.com/sanskrit-lexicon/MWS/issues/24), [#154](https://github.com/sanskrit-lexicon/MWS/issues/154),
[#155](https://github.com/sanskrit-lexicon/MWS/issues/155) (IAST→ISO 15919, decision-blocked),
Vedic accent expansion beyond 16.6%, `<ls>L.</ls>` verification (40,213 citations, crowd/corpus-assisted — natural successor to W1 once authority records exist).

---

## Maintenance

- **Updated:** at each monthly Fable planning session and after any strategic finding.
- **Source of truth for status:** GitHub issues; this doc sequences, it does not track.
- **Owners:** @funderburkjim and @Andhrabharati (maintainers); @gasyoun (coordination, papers, cross-repo).
- Companion docs: [DICT_PROFILE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DICT_PROFILE.md),
  [ENTRY_GUIDE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ENTRY_GUIDE.md),
  [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DATA_DICTIONARY.md),
  [CONTRIBUTING.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CONTRIBUTING.md).
