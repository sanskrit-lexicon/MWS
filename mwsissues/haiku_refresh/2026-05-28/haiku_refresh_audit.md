# Round-2 Haiku refresh — 2026-05-28

| Step | Status | Findings |
|---|---|---|
| H5 palette | ✅ | 77 tokens, 3 outputs regenerated |
| H1 renderers | ✅ | heatmap=2, treemap=2, sankey=2 |
| H4 version-stamp | ⚠️ | 2 missing footers, 3 stale SHA |
| H3 PNG↔SVG | ✅ | 0 PNG-only, 0 SVG-only (perfect parity) |
| H2 alt/desc | ✅ | 8 figures, all sidecars present |
| H6 locales | ✅ | en=9, ru=9, perfect key parity |
| H7 manifest | ✅ | 104 files (9+24+8+63), ZIP 1.27 MB |
| H8 ZIP integrity | ✅ | manifest=104, ZIP=104 — perfect match (original "108" was a Phase 8 counting bug, see [GAPS.md](GAPS.md) #10) |
| H9 CI status | ⚠️ | MWS: 1 failure ([run 26539941482](https://github.com/sanskrit-lexicon/MWS/actions/runs/26539941482) — Liquid syntax error in DATA_DICTIONARY.md, unrelated to microanalysis), csl-atlas: 5 success |
| H10 link-rot | ⚠️ | 138 URLs counted but zero HEAD-checked (skill requires HEAD with 5s timeout) — see [GAPS.md](GAPS.md) #9 |
