# MW phrasal-headword (phw) cross-reference graph

An undocumented bidirectional structured-data layer in MW. A parent sense links to
inline phrases promoted into their own addressable micro-records, and the children
link back:

```
parent  L99906 (Darma, sense "virtue…")   <info phwchild="99930.1"/>
child   L99930.1 (DarmeRa "according to rule")   <info phwparent="99906,Darma"/>
                                                 + <lex type="phw"> in the parent gloss
```

This is real queryable data — MW's mechanism for making an inline phrase
(`dharmeṇa`) a first-class, linkable sub-entry. It is absent from
[DATA_DICTIONARY.md](../DATA_DICTIONARY.md) (as is `<etym>`, 2,637 tags).

## Findings

- **2,364 `phwchild` edges** from 2,078 parent senses to 2,354 child records;
  2,362 `phwparent` back-links; **99.3% fully reciprocal**.
- Promoted children span `n.` (789), `ind.` (533), `f.` (509), `mfn.` (257),
  `m.` (237) — not just adverbs; a broad inline-derivative layer.
- **31 integrity bugs** (broken links) — a ready `bug`+`markup` correction batch:

| issue | count | meaning |
|---|--:|---|
| `orphan_backlink` | 14 | child names a parent that doesn't list it |
| `dangling_phwchild` | 9 | parent points to a child L-number that doesn't exist |
| `asymmetric` | 7 | parent→child but child has no back-link |
| `dangling_phwparent` | 1 | child points to a missing parent |

✅ **Fixed 2026-06-13** ([CODE_REVIEW.md](../papers/CODE_REVIEW.md) #9, #10): the count
may double-count a single broken pair flagged by both the parent and child passes, and an
a child-with-no-backlink was bucketed the same as a wrong-parent mismatch — **now fixed**:
the buckets are split (`child_missing_backlink` / `child_wrong_parent`) and the summary reports
the distinct broken-link count (**31**) alongside the per-kind rows.

Most dangling cases are off-by-one L-number typos (e.g. `meTi` → missing
`167759.1`, `167755.01`). See `phw_integrity.csv` for the exact records.

## Files

| File | What |
|---|---|
| [`phw_audit.py`](phw_audit.py) | reconstruct + audit (`python phw_audit.py`) |
| `phw_edges.csv` | full graph: parent_L, parent_k1, child_L, child_k1, child_lex, reciprocal |
| `phw_integrity.csv` | the 31 issues only — actionable fix list |
| [`PHW_SUMMARY.md`](PHW_SUMMARY.md) | headline + integrity + child distribution |

Analysis only — no `mw.txt` mutation.

## Follow-ups

- ~~Document the phw family + `<etym>` in DATA_DICTIONARY.md~~ — **done**
  ([DATA_DICTIONARY.md](../DATA_DICTIONARY.md), 2026-06-13).
- **Fix the 31 broken links** — small `bug` correction batch via the standard
  `temp_mw_N.txt` workflow (still open; needs maintainer sign-off).
