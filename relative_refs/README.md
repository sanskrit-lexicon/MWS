# Relative-reference resolution (`ib.`, `id.`)

MW's two largest *relative* citation classes point at an antecedent rather than
being truly sourceless. They inflate the "unlinkable meta" share of the citation
apparatus (the 22.3% scan-link ceiling). Resolving them recovers linkable
citations and feeds paper P3.

| marker | count | meaning | antecedent | status |
|---|--:|---|---|---|
| `<ls>ib.</ls>` | 10,094 | ibidem — same *work* just cited | preceding `<ls>` | **resolved** (this dir) |
| `<ab>id.</ab>` | 4,401 | idem — same *meaning* as previous | preceding gloss | spec ([IDEM_NOTE.md](IDEM_NOTE.md), issue #98) |

## `ib.` result

These figures are **resolvable, not verified** — the walk finds an antecedent; no
hand-check against the print has confirmed it is the source MW meant (the required
next step).

The defensible core is the **5,762 (57.1%) same-cluster** resolutions, where the
antecedent sits in the same headword. A further 42.9% cross a headword boundary
(compound runs chaining `ib.` to a shared source — lower confidence, flagged in the
CSV); combined, **7,538 (74.7%)** reach a real text source as a *mechanical upper
bound*. Top targets: `MBh.` 1,149, `RV.` 1,064, `BhP.` 381, `Pāṇ.` 344, `Suśr.` 280.
See [IB_SUMMARY.md](IB_SUMMARY.md).

Resolution is pure document order — *ibidem* = the last work cited in reading
order — so every `ib.` resolves; the only judgement is the cross-boundary
confidence flag.

✅ **Fixed 2026-06-13** ([CODE_REVIEW.md](../papers/CODE_REVIEW.md) #8, #12): the
[`ib_resolve.py`](ib_resolve.py) module docstring still describes the OLD
k1-cluster-scoped algorithm, but the code now resolves over the global document
stream (crossing headwords) — **now rewritten to describe that**; and `re.split` now
passes `maxsplit=1` as a keyword. No number above changes.

## Files

| File | What |
|---|---|
| [`ib_resolve.py`](ib_resolve.py) | the resolver (`python ib_resolve.py`) |
| `ib_resolved.csv` | candidate map: L-number, resolved `<ls>`, siglum, kind, confidence |
| [`IB_SUMMARY.md`](IB_SUMMARY.md) | headline, confidence, top sources |
| [`IDEM_NOTE.md`](IDEM_NOTE.md) | `id.`/#98 scoped plan (display-policy gated) |

Analysis only — no `mw.txt` mutation. `ib_resolved.csv` is the candidate map for a
maintainer-gated enrichment pass.
