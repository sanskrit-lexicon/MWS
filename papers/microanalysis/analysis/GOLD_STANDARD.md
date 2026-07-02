# MW block detector — gold-standard validation

Date: 2026-06-13

> **⚠️ SUPERSEDED as the sampling instrument (Fable S2 ruling, 02-07-2026, Fable 5
> `claude-fable-5`).** The canonical G5 gold sample is
> [review_packets/g5/](https://github.com/sanskrit-lexicon/MWS/tree/master/review_packets/g5)
> (seed 20260702, 8 spec strata, pinned `csl-orig` commit, Pass A complete) — do **not**
> annotate `GOLD_SAMPLE.json` here; it is a *different* 200 records. What survives from this
> harness is the **scoring design** (per-block precision/recall/F1 + Cohen's κ in
> [`gold_score.py`](gold_score.py)), to be ported onto the g5 CSV at adjudication. See
> [A16_REVIEW_FABLE5.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/A16_REVIEW_FABLE5.md)
> Major 2.

Status: framework in place; awaiting two-annotator review. This upgrades the
random 100-record audit ([SPOTCHECK.md](SPOTCHECK.md)) to a **stratified,
double-annotated, precision/recall-scored** gold standard, so PAPER.md §9's
detector limitations are *measured* rather than estimated.

## Why

The MW formal-block counts in PAPER.md rest on a regex detector
([`figures/scripts/export_data.py`](../figures/scripts/export_data.py) →
`detect_blocks`). PAPER.md §9 / SPOTCHECK already document that it reproduces the
headline count exactly but over-counts **F08** (inflection form; 36.5 % of hits
are compound members) and **F09** (editorial commentary; 66.7 % fire outside a
philological context) and slightly under-counts **F11** (sense division: misses
`a)`/`b)` and roman numerals). Those figures came from a single reviewer's read
of a *random* 100-record sample. A reviewer of the paper will ask for
**precision and recall per block, on a stratified sample, with inter-annotator
agreement**. This is that instrument.

## Design

- **Reuses the detector under test.** `gold_sample.py` imports `detect_blocks` /
  `classify_type` from `export_data.py` (not a copy), so the sample validates the
  live code that produces the paper's tables.
- **Stratified by primary article type.** A round-robin draw across all 15
  primary types yields ~13–14 entries each (200 total, seed 2026), so rare types
  (`root`, `botanical`, `biographical`) are covered and `compound` (44 % of the
  dictionary) does not dominate — unlike a random draw, which would barely sample
  the rare types whose blocks (F06, F14, F15) most need validating.
- **Two independent annotators, error-only marking.** For each entry an annotator
  records just the detector's mistakes: `falsePositives` (blocks detected but not
  genuinely present) and `falseNegatives` (present blocks the detector missed).
  Ground truth = `(machine.blocks − falsePositives) ∪ falseNegatives`. Marking
  only errors keeps 200 × 2 reviews tractable.

## Files

| File | Role |
|---|---|
| [`gold_sample.py`](gold_sample.py) | builds the stratified sample |
| `GOLD_SAMPLE.json` | the double-keyed annotation packet (200 entries, empty A/B fields) |
| `GOLD_SAMPLE.md` | human worksheet grouped by stratum |
| [`gold_score.py`](gold_score.py) | scores the filled packet |
| `GOLD_STANDARD_SCORES.md` | generated report: per-block P/R/F1 + κ |

## Procedure

```bash
cd papers/microanalysis/analysis
python gold_sample.py          # (re)generate the sample — deterministic
# two reviewers fill annotations.A and annotations.B in GOLD_SAMPLE.json
python gold_score.py           # -> GOLD_STANDARD_SCORES.md
python gold_score.py --selftest  # verify the precision/recall/kappa maths
```

Each reviewer reads the raw entry body and marks `FP` / `FN` per the worksheet,
then sets their `annotator` id. They work **independently**; agreement is
measured, not assumed.

## Metrics

For each formal block F01–F18, against the **adjudicated gold** (block calls on
which both annotators agree; disagreements are reported and held out until a
human adjudicates):

- **precision** = TP / (TP + FP) — of the blocks the detector fired, how many are
  real (the F08/F09 over-count question);
- **recall** = TP / (TP + FN) — of the blocks genuinely present, how many the
  detector caught (the F11 under-count question);
- **F1**;
- **Cohen's κ** — inter-annotator agreement on that block (so "reviewed" carries a
  measured reliability, not a single opinion).

The scorer's arithmetic is checked by `gold_score.py --selftest`.

## How this armours the paper

Once annotated, the F08 and F09 rows give a *measured* precision for the two
known over-counts, and the F11 row a *measured* recall for the under-count —
replacing the "±2–4 pts" hedge in PAPER.md §9 with numbers and confidence. The κ
column lets the paper state inter-annotator reliability for every block. The
stratification ensures the rare-type blocks (etymology, botanical, biographical)
are validated, not just the common nominal/compound bulk.
