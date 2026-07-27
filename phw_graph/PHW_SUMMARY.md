# MW phrasal-headword (phw) graph — audit

Undocumented bidirectional cross-reference structure: a parent sense links to
inline phrases promoted into their own micro-records (`<info phwchild>`), which
point back (`<info phwparent>`). Reconstructed and integrity-checked here.

## Size
- `<info phwchild>` edges: **2,369** from **2,082** parent senses
  to **2,369** child records.
- `<info phwparent>` back-links: 2,369
- `<lex type="phw">` in-gloss markers: 2,074
- Children targeted by >1 parent: 0

## Integrity
- **Reciprocal (parent↔child both link): 2,369 / 2,369 (100.0%)**
- **Distinct broken parent↔child links: 0** (equals the issue-row total here:
  this data has no mismatched-triangle case that a single defect would flag from both sides; the
  dedup is a safeguard for that case, not a correction to this count — CODE_REVIEW #9).
- No issues — graph is fully consistent.

See `phw_integrity.csv` for the exact records (maintainer-fixable).

## What gets promoted (child `<lex>` distribution)
| child lex | count |
|---|--:|
| `n.` | 797 |
| `ind.` | 536 |
| `f.` | 512 |
| `mfn.` | 258 |
| `m.` | 238 |
| `(none)` | 28 |

## Notes
- Promoted children span the `<lex>` distribution above (dominated by `n.`,
  `ind.` adverbial phrases like `dharmeṇa`, `f.`, `mfn.`, `m.`) — inline derivative
  forms MW made separately addressable. A genuine structured-data layer (queryable
  phrase sub-entries), undocumented in DATA_DICTIONARY. Candidate W4 export.
- The 31 broken links originally found here (mostly off-by-one L-number typos in
  `phwchild`/`phwparent` targets, plus two `{{Lbody=}}`-alias redirects and one
  duplicate pointer) were corrected in `csl-corrections/batch_pending/dictionaries/mw/`
  (H1500) — this script only analyses/audits, it never mutates `mw.txt`.
