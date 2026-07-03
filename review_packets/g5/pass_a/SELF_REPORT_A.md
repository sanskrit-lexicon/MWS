# Pass A self-report — G5 gold-sample annotation

_Created: 02-07-2026 · Last updated: 02-07-2026_

Annotator: Sonnet 5 (`claude-sonnet-5`). Branch: `g5-pass-a`. Source:
`csl-orig/v02/mw/mw.txt` @ `392ed6bdda9c624c2a18e5730a61719fdacf645c`.

## Records completed

**200/200.** All rows in `annotations.csv` carry a non-empty `gold_blocks_A`
(minimum F01/F10/F17, the always-present kernel). No row was skipped.

## Fields left blank, and why

- `detected_blocks` — left blank for every row **on purpose**. Populating it
  requires reading `papers/microanalysis/analysis/`'s detector output, which
  the isolation rule (this pass's handoff, part (c)) explicitly forbids. Per
  [SPEC-2](https://github.com/sanskrit-lexicon/MWS/blob/master/planning/specs/2026-07/SPEC-2-g5-annotation.md)
  and the [G5 spec](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/G5_GOLD_SAMPLE_SPEC.md)'s own
  "Scoring Output" section, this is a separate, later step (the mechanical
  scorer), not part of either annotation pass.
- `gold_blocks_B`, `adjudicated_blocks`, `false_positive_blocks`,
  `false_negative_blocks` — out of scope for Pass A by design (Pass B's own
  branch; adjudication reserved for the Fable S2 session per SPEC-2 §4).
- `notes` — left blank on every row. The codebook (`CODEBOOK_A.md`) resolves
  the one structurally ambiguous rule (F12/F13 co-occurrence) uniformly
  rather than case-by-case, so no row needed an individual note. See
  `CODEBOOK_A.md`'s Limitations section for the two blocks (F08, F09) with a
  known systematic detection-rule approximation instead of per-row flags.

## Method note (read alongside CODEBOOK_A.md)

Two structural steps preceded annotation, both required because the 200-record
gold sample did not exist yet — only the spec ("does not perform human
annotation") did:

1. **Sample construction.** Built the deterministic 8-stratum 200-record
   sample from `mw.txt` per the G5 spec's stratification table, pinned the
   seed/algorithm in a companion doc, and merged it to `master` *ahead of*
   this pass (PR [sanskrit-lexicon/MWS#220](https://github.com/sanskrit-lexicon/MWS/pull/220),
   merged) so Pass B can independently reproduce the identical 200
   L-numbers without reading this branch — see
   [`review_packets/g5/G5_SAMPLING_ADDENDUM.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/g5/G5_SAMPLING_ADDENDUM.md).
   This step carries no annotation judgment (structural tag-presence only),
   so merging it ahead of both blind passes does not violate isolation.
2. **Annotation.** Applied the codebook in `CODEBOOK_A.md` (own reading of
   the G5 spec's F01–F18 definitions + `DATA_DICTIONARY.md`'s tag inventory,
   deliberately not consulting `papers/microanalysis/analysis/`) uniformly
   via `annotate_a.py`, run once, no per-record hand overrides. This trades
   some annotation nuance (a human Sanskritist would likely catch
   free-text-only F09 commentary the rule-based pass misses) for full
   reproducibility and an auditable rule set — a defensible tradeoff for a
   *first* independent pass whose job is to generate a genuine second data
   point against Pass B and the detector, not to be maximally accurate in
   isolation. Flagged explicitly in CODEBOOK_A.md's Limitations rather than
   silently presented as unhedged ground truth.

## Wall-clock

Single continuous session, approximately 25–30 minutes from handoff read to
this report (spec reading + tag-inventory reconnaissance ~10 min, sampler +
skeleton PR ~10 min, codebook + annotation run + writeup ~10 min). No precise
start timestamp was captured; this is an approximate range from file mtimes,
not a logged stopwatch figure.

## Acceptance checklist (G5 spec)

- [x] 200 distinct records
- [x] Independent annotation column (`gold_blocks_A`) complete
- [ ] Two independent annotations — Pass B not yet run
- [ ] Adjudication — reserved for Fable S2
- [x] Schema matches `G5_GOLD_SAMPLE_SPEC.md`'s column list exactly

_Dr. Mārcis Gasūns_
