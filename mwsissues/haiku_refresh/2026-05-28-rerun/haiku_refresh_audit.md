# Round-2 Haiku refresh — 2026-05-28-rerun

| Step | Status | Findings |
|---|---|---|
| H5 palette | ✅ | 77 tokens, 3 outputs regenerated |
| H1.5 data refresh | ✅ | skipped (mw.txt unchanged) |
| H1 renderers | ✅ | heatmap=2, treemap=2, sankey=2, cross-dict=2 (en+ru where supported) |
| H4 version-stamp | ✅ | 0 missing, 0 stale — all 8 SVGs stamped at HEAD |
| H3 PNG↔SVG | ✅ | 0 PNG-only, 0 SVG-only (perfect parity) |
| H2 alt/desc | ✅ | 8 figures, all sidecars present |
| H6 locales | ✅ | en=9, ru=9, perfect key parity |
| H7 manifest | ✅ | 104 files, ZIP 1606 kB |
| H8 ZIP integrity | ✅ | manifest=104, ZIP=104 — perfect match |
| H9 CI status | ⚠️ | MWS: 2 failures — [run 26556808199](https://github.com/sanskrit-lexicon/MWS/actions/runs/26556808199) blocks on `Unknown tag 'Theil'` in [DICT_PROFILE.md:235](https://github.com/sanskrit-lexicon/MWS/blob/master/DICT_PROFILE.md) (German word "Theil" parsed as Liquid tag, unrelated to microanalysis); yesterday's DATA_DICTIONARY.md fix landed via PR #198. csl-atlas: 5 successes. |
| H10 link-rot | ⚠️ | 73 unique URLs HEAD-checked, 7 broken — see [h10_link_rot.log](h10_link_rot.log) |
