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
| `<ls>` citations | 311,932 |
| Unique `<ls>` abbreviations | 821 |
| With [authority record](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) | 232 (28.3%) — covering 64.0% of citations |
| `<ls>` citations carrying a numeric locator | 59.8% (40.2% are bare abbreviations) |
| Vedic accent coverage | 16.6% of `<k2>` fields |
| `<ls>L.</ls>` lexicographer hedges | 40,213 (12.9% of citations) — unique to MW among CDSL dicts |

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

## Workstream W1 — Authority records: 589 orphan `<ls>` abbreviations

**Goal:** lift citation coverage from 64% to ≥85% by completing authority
records for the most-cited orphan abbreviations. Highest-leverage work in the
repo: each record unlocks scan click-through for thousands of citations.

**Top orphans by citation count:** Pāṇ. (8,527), ŚBr. (7,029), Kathās. (6,757),
Suśr. (6,200), Kāv. (4,667), VarBṛS. (3,467), Rājat. (3,410), Pañcat. (2,670),
Ragh. (2,654), KātyŚr. (2,537), Yājñ. (2,249). Top-25 covers ~80% of orphan citations.

**Unit of work** (Sonnet-tier, one per session, fully resumable):
1. Pick next abbreviation from the queue.
2. Identify the edition MW actually cited (frontier question only when ambiguous — MW's "Sources of the work" preface and [mwauthorities/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) precedents first).
3. Locate a scan (archive.org), verify pagination against 3–5 sample citations.
4. Add the record following the existing [mwauthorities](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) format; document in an issue.

**Frontier-tier items inside W1:**
- Pāṇ. is special: grammar-sūtra citations, not page citations — needs a linking-scheme decision (sūtra-number → scan page map), same family as the 2021 [Panini link-target work](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities/ls/20211005-panini).
- Open the proposed `authority-record.yml` issue template and one tracking issue per top-10 orphan.

**Targets:** 5 records/month → top-25 done by November (≈80% → coverage ~85%).

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
4. **Sense `<div>` policy for MW itself.** MW's own worst structural gap is
   prose-embedded senses (no `<div>` markers; excluded from cross-dict
   sense-depth analysis). A retrofit is large and print-fidelity-sensitive —
   in H2 2026, only produce the *decision document* (options, cost, risk) for
   maintainer review; no mass edit.

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
| 1 | **No structural sense markers** — senses live in prose, no `<div>` | Excluded from atlas [sense-depth.json](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/data/dicts/sense-depth.json) (AP/PWG/PWK only) | Cross-dict sense alignment requires bespoke parsing (R2 rebuild); blocks P2-style analyses for MW |
| 2 | **40.2% of `<ls>` citations are bare** — no book/chapter/verse locator | [CITATION_REGISTERS.md](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/CITATION_REGISTERS.md): 59.8% resolvability | ~125k MW citations cannot link to a scan page even with a perfect authority record |
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
[#74](https://github.com/sanskrit-lexicon/MWS/issues/74) (botanical export, crowd),
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
