# W1 (a) — unlinked `<ls>` siglum candidates

Review candidates only — **nothing is written to any authority file.**

## Counts
- Distinct live `<ls>` bare abbreviations (meta excluded): **877**
- Already covered by an authority record / link: 537
- **Candidate unlinked: 340**

## Self-validation (false-positive check)
The linked-check is dual: a siglum counts as linked if its spelling is in the
link file col1 verbatim (ASCII sigla like `RV.`) OR its SLP1 transcription is a
known canonical key (diacritic sigla like `Pāṇ.`→`pAR`).
- Of the 40 highest-frequency sigla (certainly real and linked), **0 are
  flagged unlinked** — the check produces no false positives at the high-
  frequency end, so the candidates below are genuine gaps, not mismatches.

## Match confidence (of the candidates)
| confidence | count | meaning |
|---|--:|---|
| high (≥0.90) | 20 | near-certain spelling variant of an existing record |
| medium (0.80–0.89) | 112 | probable variant — quick human confirm |
| low (0.70–0.79) | 68 | weak — needs judgment |
| no-match | 140 | no close record — candidate NEW authority |

## How to use
- `link_candidates.csv` is sorted by citation count. The **high**-confidence
  rows are the mechanical wins (a spelling variant that should point to an
  existing canonical record); **no-match** rows are candidate new authorities.
- A maintainer reviews, then the accepted rows are added to
  `linkmwauthorities_init.txt` via the normal authority workflow. Not automated.
