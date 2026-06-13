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

**7,538 of 10,094 (74.7%)** resolve to a real text source; 25.3% to a meta
marker (stays unlinkable); 0 unresolvable. Top targets: `MBh.` 1,149, `RV.`
1,064, `BhP.` 381, `Pāṇ.` 344, `Suśr.` 280. Confidence: 57.1% land in the same
headword cluster (high), 42.9% cross a headword boundary (compound runs sharing a
source — flagged in the CSV for review). See [IB_SUMMARY.md](IB_SUMMARY.md).

Resolution is pure document order — *ibidem* = the last work cited in reading
order — so every `ib.` resolves; the only judgement is the cross-boundary
confidence flag.

## Files

| File | What |
|---|---|
| [`ib_resolve.py`](ib_resolve.py) | the resolver (`python ib_resolve.py`) |
| `ib_resolved.csv` | candidate map: L-number, resolved `<ls>`, siglum, kind, confidence |
| [`IB_SUMMARY.md`](IB_SUMMARY.md) | headline, confidence, top sources |
| [`IDEM_NOTE.md`](IDEM_NOTE.md) | `id.`/#98 scoped plan (display-policy gated) |

Analysis only — no `mw.txt` mutation. `ib_resolved.csv` is the candidate map for a
maintainer-gated enrichment pass.
