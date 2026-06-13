# `<ls>ib.</ls>` resolution — results

- Total `<ls>ib.</ls>` citations: **10,094**
- **Resolved to a real text source (recoverable as linkable): 7,538 (74.7%)**
- Resolved to a meta marker (L./W./Cat./MW. — stays unlinkable): 2,556 (25.3%)
- Unresolvable (no prior citation in the whole dictionary): 0 (0.0%)

## Confidence (antecedent locality)
- **Same headword cluster (high confidence): 5,762 (57.1%)**
- Crossed a headword boundary (lower confidence — typical of compound runs
  where sibling compounds chain `ib.` to a shared source): 4,332 (42.9%)
  These are the candidates worth a maintainer spot-check before any write.

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
