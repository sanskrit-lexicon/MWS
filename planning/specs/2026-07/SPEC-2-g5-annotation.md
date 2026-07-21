# SPEC-2 — W2: G5 gold-sample annotation, two independent passes

_Created: 02-07-2026 · Last updated: 02-07-2026_

**Tier:** Sonnet 5 (`claude-sonnet-5`) × **two separate sessions that must not see each
other's output**. **Repo:** MWS, branch per pass. This is the sole hard blocker for the
end-of-August IJL submission of P1/A16.

## Objective

Execute the annotation protocol already specified in
[review_packets/G5_GOLD_SAMPLE_SPEC.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/G5_GOLD_SAMPLE_SPEC.md)
(200-record stratified MW sample, block-type annotation fields F01–F18) — that spec is the
contract; this spec only fixes the run mechanics.

## Run mechanics

1. Pass A and Pass B run in separate sessions/branches (`g5-pass-a`, `g5-pass-b`), each
   producing `review_packets/g5/pass_<X>/annotations.csv` per the G5 spec's schema.
   Annotator prompt = the G5 spec verbatim; no peeking at `analysis/` detector outputs.
2. Each pass self-reports: records completed, fields left blank + why, wall-clock.
3. After BOTH passes exist, a mechanical diff step (either session, or Haiku) computes the
   disagreement set → `review_packets/g5/disagreements.csv` (record, field, A, B).
4. **STOP.** Disagreement adjudication is reserved for the Fable A16 review session
   (window-plan S2) by name in [ROADMAP.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ROADMAP.md) §W2.
   Do not adjudicate, do not compute final P/R (that needs adjudicated gold).

## Acceptance

- 200/200 records annotated in both passes, schema-valid CSVs, zero cross-contamination
  (passes committed from different branches, merged only after both complete).
- disagreements.csv exists with per-field counts summarized in its header comment.

_Dr. Mārcis Gasūns_
