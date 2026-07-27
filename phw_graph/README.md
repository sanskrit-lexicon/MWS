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

- **2,369 `phwchild` edges** from 2,082 parent senses to 2,369 child records;
  2,369 `phwparent` back-links; **100.0% fully reciprocal**.
- Promoted children span `n.` (797), `ind.` (536), `f.` (512), `mfn.` (258),
  `m.` (238) — not just adverbs; a broad inline-derivative layer.
- ✅ **Fixed (H1500, 2026-07-27)** — the 31 integrity bugs (broken links) below were
  corrected via a `bug`+`markup` batch, parked in
  `csl-corrections/batch_pending/dictionaries/mw/change_mw_2.txt` per the standard
  `/cologne-correction-queue` workflow (never committed directly to `csl-orig`; ships in
  the next `/cologne-batch-pr`). Re-running `phw_audit.py` now shows **0 remaining issues**.

| issue | count (pre-fix) | meaning |
|---|--:|---|
| `orphan_backlink` | 14 | child names a parent that doesn't list it |
| `dangling_phwchild` | 9 | parent points to a child L-number that doesn't exist |
| `child_missing_backlink` | 7 | parent→child but child has no back-link |
| `dangling_phwparent` | 1 | child points to a missing parent |

✅ **Fixed 2026-06-13** ([CODE_REVIEW.md](../papers/CODE_REVIEW.md) #9, #10): the count
may double-count a single broken pair flagged by both the parent and child passes, and an
a child-with-no-backlink was bucketed the same as a wrong-parent mismatch — **now fixed**:
the buckets are split (`child_missing_backlink` / `child_wrong_parent`) and the summary reports
the distinct broken-link count (**31**) alongside the per-kind rows.

Most dangling cases were off-by-one/garbled L-number typos (e.g. `meTi` → corrected
`167759`, `167755`); a few needed redirecting a `phwparent` from a bodiless `{{Lbody=}}`
alias record to the record that actually carries the gloss text (no `{{Lbody=}}` stub in
the whole corpus ever carries an `<info>` tag). See `phw_integrity.csv` — now empty — and
`change_mw_2.txt` for the exact per-line corrections and rationale.

## Files

| File | What |
|---|---|
| [`phw_audit.py`](phw_audit.py) | reconstruct + audit (`python phw_audit.py`) |
| `phw_edges.csv` | full graph: parent_L, parent_k1, child_L, child_k1, child_lex, reciprocal |
| `phw_integrity.csv` | integrity issues — actionable fix list (0 rows since H1500) |
| [`PHW_SUMMARY.md`](PHW_SUMMARY.md) | headline + integrity + child distribution |

Analysis only — no `mw.txt` mutation.

## Follow-ups

- ~~Document the phw family + `<etym>` in DATA_DICTIONARY.md~~ — **done**
  ([DATA_DICTIONARY.md](../DATA_DICTIONARY.md), 2026-06-13).
- ~~Fix the 31 broken links~~ — **done** (H1500, 2026-07-27): change file parked via
  `/cologne-correction-queue`, ships to `csl-orig` in the next `/cologne-batch-pr`.
