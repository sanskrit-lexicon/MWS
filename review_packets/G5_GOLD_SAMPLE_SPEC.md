# G5 Gold Sample Spec — MW Block-Economy Paper

_Created: 26-06-2026 · Last updated: 02-07-2026_

Purpose: define the 200-entry double-annotation sample needed before the P1
paper reports precision/recall for MW block detectors F01-F18. This is a spec
and worksheet design only. It does not perform human annotation.

## Scope

- Data source: live `mw.txt` records used by the microanalysis paper.
- Unit: one MW record (`<L>...<LEND>`), not a visual page block and not a
  grouped headword family.
- Target size: 200 records.
- Annotation: two independent passes, followed by disagreement adjudication.
- Output use: update `papers/microanalysis/PAPER.md` limitations with measured
  detector precision/recall per formal block.

## Sampling Strata

The sample must stress both common kernel blocks and rare/high-risk blocks. Use
deterministic sampling with a fixed seed and record the source commit / file
timestamp. The pinned algorithm, seed, and resulting worksheet live in
[g5/G5_SAMPLING_ADDENDUM.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/g5/G5_SAMPLING_ADDENDUM.md) — both annotation
passes draw from `g5/G5_gold_sample_skeleton.csv` there.

| Stratum | Target n | Why it exists |
|---|---:|---|
| Kernel/common records | 40 | Baseline precision for F01/F02/F04/F10/F12/F17. |
| Root / verbal records | 25 | F05/F06/F09 are denser here; homonym roots stress profile logic. |
| Continuation senses (`<e>` letter suffixes) | 25 | Tests the paper's record-as-sense claim and continuation handling. |
| Lexicographer hedge (`<ls>L.</ls>`) | 25 | Tests F13 and hedge-vs-source-citation distinction. |
| Botanical / biographical / encyclopedic records | 25 | Tests F14/F15 and type-enriched profiles. |
| Cross-reference / phrasal-headword records | 20 | Tests F16 and phw graph-adjacent records. |
| Correction / machine-info edge cases | 15 | Tests F17/F18 and digitisation infrastructure boundaries. |
| Random residual control | 25 | Catches detector errors not anticipated by targeted strata. |

If strata overlap, keep the first assigned stratum and backfill the later stratum
from the next deterministic candidate. The final sample must contain exactly 200
distinct L-numbers.

## Annotation Fields

Each row in `G5_gold_sample.csv` should contain:

| Field | Type | Notes |
|---|---|---|
| `sample_id` | string | `G5-001` ... `G5-200`. |
| `stratum` | enum | One of the strata above. |
| `L` | string | MW record number. |
| `k1` | string | Source key, SLP1 as in `mw.txt`. |
| `pc` | string | Page-column, if present. |
| `record_excerpt` | string | Short clipped source excerpt for review context. |
| `detected_blocks` | string | Semicolon list emitted by the current detector. |
| `gold_blocks_A` | string | Annotator A block list, F01-F18. |
| `gold_blocks_B` | string | Annotator B block list, F01-F18. |
| `adjudicated_blocks` | string | Final block list after disagreement review. |
| `false_positive_blocks` | string | Detector blocks not in adjudicated gold. |
| `false_negative_blocks` | string | Gold blocks missed by detector. |
| `notes` | string | Short reason for hard cases. |

Allowed block ids are `F01` through `F18`, matching the paper. A row may carry
multiple blocks in source order. Annotators should mark uncertainty in `notes`,
not by inventing new block ids.

## Reviewer Instructions

1. Read the clipped excerpt and, when unclear, open the full source record.
2. Mark only formal blocks present in the record.
3. Treat `<info>` as F17 digital infrastructure, not as MW print microstructure.
4. Treat `<ls>L.</ls>` as F13 hedge when it qualifies the whole entry's
   lexicographer-only evidence; other `<ls>` references remain F12.
5. Treat letter-suffixed `<e>` continuation records as record-level senses.
6. Do not resolve scholarly correctness of the entry; this is a structural
   annotation task.

## Disagreement Workflow

1. Annotator A and B fill their columns independently.
2. A script computes per-row set differences.
3. Rows with identical block sets are accepted automatically.
4. Disagreements are adjudicated by a senior reviewer, who fills
   `adjudicated_blocks` and `notes`.
5. Keep both original annotations for inter-annotator agreement reporting.

Report:

- exact agreement over full block sets;
- per-block agreement;
- Cohen-style binary agreement per block if computed;
- number of adjudicated rows.

## Scoring Output

The scorer should emit `G5_gold_scores.json` and `G5_gold_scores.md`.

Required metrics per block:

| Metric | Definition |
|---|---|
| `true_positive` | Detector and adjudicated gold both contain the block. |
| `false_positive` | Detector contains the block, adjudicated gold does not. |
| `false_negative` | Adjudicated gold contains the block, detector does not. |
| `precision` | `TP / (TP + FP)`, null when denominator is 0. |
| `recall` | `TP / (TP + FN)`, null when denominator is 0. |
| `support` | Number of adjudicated rows containing the block. |

Also emit macro-average precision/recall across F01-F18 and a warning list for
blocks with support below 5, because rare blocks may be too sparse for stable
claims.

## Acceptance Criteria

- `G5_gold_sample.csv` has 200 distinct records.
- Every row has two independent annotations before adjudication.
- Every adjudicated row uses only F01-F18.
- Scoring output includes per-block precision/recall and support.
- `PAPER.md` limitations cite both the sample method and the weak-support
  warnings instead of reporting naked percentages.

_Dr. Mārcis Gasūns_
