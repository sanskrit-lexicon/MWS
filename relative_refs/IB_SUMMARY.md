# `<ls>ib.</ls>` resolution — results

> **These figures are *resolvable*, not *verified*.** The walk mechanically
> finds an antecedent; whether it is the source MW *meant* has not been checked
> against the print. No ground-truth sample has been hand-validated — that is the
> required next step before any paper or write-back.

- Total `<ls>ib.</ls>` citations: **10,094**
- **Same-cluster resolutions (high confidence — antecedent in the same headword): 5,762 (57.1%)** — the defensible core.
- Crossed-headword resolutions (lower confidence; compound runs chaining `ib.` to a
  shared source): 4,332 (42.9%) — need a spot-check before use.
- Combined, resolved to a real text source (mechanical upper bound): 7,538 (74.7%); to a meta marker 2,556 (25.3%); unresolvable 0.

## Effect on the scan-link ceiling
- The earlier "22.3% meta" ceiling counted all 10,094 ib. as unlinkable.
- Resolving recovers **7,538** of them to real sources, shrinking
  the truly-unlinkable meta set by that amount.

## What ib. actually points to (top real sources)
| terminal source | ib. citations resolved |
|---|--:|
| `MBh.` | 1,149 |
| `RV.` | 1,064 |
| `BhP.` | 381 |
| `Pāṇ.` | 344 |
| `Suśr.` | 280 |
| `R.` | 277 |
| `Dhātup.` | 249 |
| `Kathās.` | 244 |
| `Kāv.` | 230 |
| `Hariv.` | 195 |
| `AV.` | 126 |
| `Buddh.` | 123 |
| `ŚBr.` | 107 |
| `Rājat.` | 105 |
| `VarBṛS.` | 102 |

## Notes
- Resolution is in pure document order — `ibidem` = the last work cited in
  reading order. Every ib. therefore resolves (0 unresolvable). Antecedents
  in the same `<k1>` cluster are high-confidence; cross-boundary ones
  (compound runs sharing a source) are flagged for review in the CSV.
- Chained ib.->ib. is followed to the first non-ib. terminal.
- This is analysis only; no `mw.txt` mutation. `ib_resolved.csv` is the
  candidate map for a future enrichment pass (maintainer-gated).
- Sibling task: `<ab>id.</ab>` (4,401, issue #98) is the *sense*-level analog
  (resolve to the preceding gloss); see IDEM_NOTE.md.
