# G5 Sampling Addendum — pinned deterministic algorithm

_Created: 02-07-2026 · Last updated: 02-07-2026_

Companion to
[G5_GOLD_SAMPLE_SPEC.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/G5_GOLD_SAMPLE_SPEC.md),
which requires "deterministic sampling with a fixed seed" but does not itself
pin the seed or predicate order. This addendum pins both, so that Pass A and
Pass B — run as two isolated sessions per
[SPEC-2](https://github.com/sanskrit-lexicon/MWS/blob/master/planning/specs/2026-07/SPEC-2-g5-annotation.md)
that must not read each other's branch — draw the **same** 200 records
without either session reading the other's output. `G5_gold_sample_skeleton.csv`
in this directory is the canonical, unannotated worksheet both passes copy
into their own `pass_<x>/annotations.csv` and fill independently.

## Source

- File: `csl-orig/v02/mw/mw.txt`
- Commit: `392ed6bdda9c624c2a18e5730a61719fdacf645c` (2026-06-27)
- Record count at that commit: 286,525 `<L>…<LEND>` records

## Algorithm

Script: [`build_sample.py`](build_sample.py) in this directory. Deterministic
seed: `20260702` (int; the date this addendum was ratified). Steps:

1. Parse `mw.txt` into records split on `<L>` / `<LEND>` boundaries.
2. For each of the 8 strata in [G5_GOLD_SAMPLE_SPEC.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/G5_GOLD_SAMPLE_SPEC.md#sampling-strata),
   in the table's listed order, build a candidate pool of records matching
   that stratum's structural predicate (tag/attribute presence — see
   `build_sample.py`'s `is_*` functions) **excluding L-numbers already
   assigned to an earlier stratum** (spec's overlap rule: "keep the first
   assigned stratum").
3. Sort each candidate pool by `L` (string sort, ascending — stable,
   independent of parse order) then shuffle with `random.Random(SEED ^ hash(stratum_name) & 0xffffffff)`
   and take the first `target_n`.
4. Concatenate all 8 stratum picks (200 records total), then shuffle the
   combined list once with `random.Random(SEED)` to interleave strata before
   assigning `sample_id` `G5-001`…`G5-200`.

Predicates (structural, from tag presence only — see `build_sample.py` for
exact regex):

| Stratum | Predicate |
|---|---|
| `kernel_common` | has `<lex>`, a display `<s>`, a non-`L.` `<ls>`, an `<info>`, is not a lettered continuation, and carries none of the enrichment markers (`<hom>`, `<lang>`, `<bot>`, `<bio>`, `<s1>`, `<etym>`, `<chg`, verb markers, `phwchild`/`phwparent`, `<div n=`, `<pcol>`, `√`) |
| `root_verbal` | `<ab>cl.</ab>`, `<ab>P.</ab>`, `<ab>Ā.</ab>`, or `verb="genuineroot\|root\|gati\|nom\|pre"` |
| `continuation` | `<e>` value ends in a letter after a digit (e.g. `1A`, `2B`) |
| `hedge_ls` | contains `<ls>L.</ls>` |
| `botanical_bio` | `<bot>`, `<bio>`, or `<s1>` |
| `crossref_phw` | `<ab>id.</ab>`, `type="phw"`, `phwchild=`/`phwparent=`, or `<pcol>` |
| `correction_edge` | `<chg` or `n="rev"` (incl. `<listinfo n="rev"/>`) |
| `random_residual` | any remaining record |

## Reproducing

```sh
cd MWS/review_packets/g5
python build_sample.py   # requires ../../../csl-orig sibling checkout at the pinned commit
```

Byte-identical `G5_gold_sample_skeleton.csv` output is the acceptance check
for "same sample" — diff the regenerated file against the committed one
before either pass starts annotating.

## Why this is not itself an annotation pass

This addendum and the resulting skeleton carry **zero** `gold_blocks_*`
judgments — only `sample_id`, `stratum`, `L`, `k1`, `pc`, `record_excerpt`
(all mechanically derived from `mw.txt` structure). It is merged straight to
`master` ahead of both passes so that Pass A and Pass B can each build their
own branch from an identical starting worksheet without violating the
isolation rule, which concerns the *annotation columns*, not the shared
sample list.

_Dr. Mārcis Gasūns_
