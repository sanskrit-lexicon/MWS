# MW phrasal-headword (phw) graph — audit

Undocumented bidirectional cross-reference structure: a parent sense links to
inline phrases promoted into their own micro-records (`<info phwchild>`), which
point back (`<info phwparent>`). Reconstructed and integrity-checked here.

## Size
- `<info phwchild>` edges: **2,364** from **2,078** parent senses
  to **2,354** child records.
- `<info phwparent>` back-links: 2,362
- `<lex type="phw">` in-gloss markers: 2,074
- Children targeted by >1 parent: 1

## Integrity
- **Reciprocal (parent↔child both link): 2,348 / 2,364 (99.3%)**
- Issues found:
  - `orphan_backlink`: 14
  - `dangling_phwchild`: 9
  - `asymmetric`: 7
  - `dangling_phwparent`: 1

See `phw_integrity.csv` for the exact records (maintainer-fixable).

## What gets promoted (child `<lex>` distribution)
| child lex | count |
|---|--:|
| `n.` | 789 |
| `ind.` | 533 |
| `f.` | 509 |
| `mfn.` | 257 |
| `m.` | 237 |
| `(none)` | 29 |

## Notes
- Promoted children span `n.` (789), `ind.` (533, adverbial phrases like
  `dharmeṇa`), `f.` (509), `mfn.` (257), `m.` (237) — inline derivative forms
  MW made separately addressable. A genuine structured-data layer (queryable
  phrase sub-entries), undocumented in DATA_DICTIONARY. Candidate W4 export.
- **The 31 integrity issues are real, fixable markup bugs** (mostly off-by-one
  L-number typos in `phwchild` targets). `phw_integrity.csv` is the actionable
  list — a ready `bug`+`markup` correction batch. Analysis only, no mutation.
