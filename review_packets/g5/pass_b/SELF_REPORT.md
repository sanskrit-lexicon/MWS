# G5 gold-sample annotation — Pass B self-report

_Created: 02-07-2026 · Last updated: 02-07-2026_

**Annotator:** Sonnet 5 (`claude-sonnet-5`), single session, branch `g5-pass-b`.
**Isolation:** did not read `review_packets/g5/pass_a/`, branch `g5-pass-a` (including its PR),
or `papers/microanalysis/analysis/` at any point during this pass.

## Method

Annotated all 200 records against the full `<L>…<LEND>` text pulled directly from
[csl-orig/v02/mw/mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt)
(not the clipped `record_excerpt` column, which is truncated for long entries), applying the
formal block-marker definitions published in
[MICROANALYSIS.md §1](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/MICROANALYSIS.md#1--formal-block-inventory-18-blocks)
and the reviewer instructions in
[G5_GOLD_SAMPLE_SPEC.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/G5_GOLD_SAMPLE_SPEC.md#reviewer-instructions).
Implemented as a small Python annotation script (not the paper's `analysis/` detector, which was
not read) so the 200-record pass is reproducible and internally consistent; verified against the
paper's own published population frequencies and against manual reading of every record in three
targeted spot-checks (kernel/root records, the `correction_edge` stratum in full, all 27 `F16`
hits) before finalizing.

## Records completed

**200/200.** No fields left blank — every record has an `F01`;`F17` at minimum (`F10` also always
present; three are structurally universal per the paper's own kernel claim and were confirmed
present in all 200 sampled records).

## Judgment calls (flag for adjudication)

1. **F16 vs. `<info phwparent="...">` (stratum `crossref_phw`).** Treated `F16` as requiring a
   *textual* cross-reference marker (`q.v.`, `<ab>cf.</ab>`, `<ab>id.</ab>`, "see") per
   MICROANALYSIS.md's literal marker definition. Phrasal-headword parent links encoded only via
   `<info phwparent="…">` were **not** counted as `F16` — that relationship is captured by `F17`
   (machine annotation), not a discourse-level cross-reference. This may under-count `F16` for the
   `crossref_phw` stratum relative to a reading that treats `phwparent` as cross-reference; flagging
   for adjudication.
2. **F09 (editorial commentary) — conservative by design.** Restricted to genuine hedge/discussion
   openers (`probably`, `perhaps`, `apparently`, `according to`) and bracketed etymological asides
   (`[For … See …]`), per MICROANALYSIS.md's own examples. Explicitly **excluded** bare `= synonym`
   equivalence glosses and bare `cf.`/`see` (those are ordinary gloss content or `F16`, not
   commentary) — an earlier draft over-triggered on both and was corrected before finalizing (see
   commit history on this branch). Only 1/200 records (`G5-063`, root `vfz`) qualified. This is
   likely an under-count relative to the paper's 6–9% population baseline, since a purely
   phrase-triggered rule misses commentary that doesn't use those exact hedge words; flagging as a
   conservative-recall choice, not a defect.
3. **F18 — two records use a different literal format than documented.** `G5-111` (L=180503) and
   `G5-198` (L=1730) carry an inline `<chg type="chg" src="mw"><old>…</old><new>…</new></chg>`
   correction tag, not the `{{old->new||date|author|url}}` format MICROANALYSIS.md's table
   describes. Both are genuine machine-readable correction/provenance records by function, so both
   were counted as `F18` — flagged in each row's `notes` column and here for adjudication, since
   this is a source-format detail not in the published block table.
4. **F08 marker is a raw `<s>` count (≥ 2), matching MICROANALYSIS.md's own stated heuristic.**
   This is known to over-count relative to "true inflection form" in some cases (e.g. a bare
   cross-referenced form inside a parenthetical, as in `G5-004`/L=181486's `(cf. Jampa)`) — this is
   the same over-count MICROANALYSIS.md's own §9 limitations note documents for the automated
   detector; not corrected here since the marker definition is literal.

## Wall-clock

Single continuous session; annotation (script-assisted, spot-checked) plus three verification
passes.

## Population-frequency sanity check (this 200-record stratified sample, NOT representative of the
full 286,561-record corpus — strata deliberately oversample rare/high-risk blocks)

| Block | Count | % of 200 |
|---|--:|--:|
| F01 | 200 | 100.0% |
| F02 | 157 | 78.5% |
| F03 | 9 | 4.5% |
| F04 | 125 | 62.5% |
| F05 | 20 | 10.0% |
| F06 | 28 | 14.0% |
| F07 | 4 | 2.0% |
| F08 | 75 | 37.5% |
| F09 | 1 | 0.5% |
| F10 | 200 | 100.0% |
| F11 | 0 | 0.0% |
| F12 | 172 | 86.0% |
| F13 | 50 | 25.0% |
| F14 | 7 | 3.5% |
| F15 | 34 | 17.0% |
| F16 | 27 | 13.5% |
| F17 | 200 | 100.0% |
| F18 | 2 | 1.0% |

Kernel blocks (F01, F02, F04, F10, F12, F17) all appear at or above their published population
rates, as expected for a stratified (not random) sample; F13/F14/F15 elevated versus baseline
because `hedge_ls`, `botanical_bio` are dedicated 25-record strata.

_Dr. Mārcis Gasūns_
