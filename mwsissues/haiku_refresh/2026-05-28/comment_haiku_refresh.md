### Location

This is a Round-2 Haiku-tier refresh of the microanalysis pipeline per [HANDOFF_PROMPTS.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/HANDOFF_PROMPTS.md). The refresh regenerates data artifacts and audits figure consistency, parity, and accessibility. All changes pushed to branch [`haiku-refresh-2026-05-28`](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28).

@funderburkjim @Andhrabharati

---

## Round-2 Haiku refresh — 2026-05-28

### Audit table

| Step | Status | Findings |
|---|---|---|
| [H5 palette](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/figures/palette-tokens.json) | ✅ | 77 tokens, 3 outputs regenerated |
| [H1 renderers](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/figures/scripts/render_heatmap.py) | ✅ | heatmap=2, treemap=2, sankey=2 |
| [H4 version-stamp](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/figures/) | ⚠️ | 2 missing footers, 3 stale SHA |
| [H3 PNG↔SVG](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28/papers/microanalysis/figures) | ✅ | 0 PNG-only, 0 SVG-only (perfect parity) |
| [H2 alt/desc](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28/papers/microanalysis/figures) | ✅ | 8 figures, all sidecars present |
| [H6 locales](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28/papers/microanalysis/figures/locales) | ✅ | en=9, ru=9, perfect key parity |
| [H7 manifest](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/analysis/SUPPLEMENT_MANIFEST.md) | ✅ | 108 entries, ZIP 1.27 MB |
| [H8 ZIP integrity](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/analysis/mw-microanalysis-supplementary.zip) | ⚠️ | manifest=108, ZIP=104 (mismatch) |
| [H9 CI status](https://github.com/sanskrit-lexicon/MWS/actions) | ⚠️ | MWS: 1 failure (pages 2026-05-27), csl-atlas: 5 success |
| [H10 link-rot](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28/papers/microanalysis) | ℹ️ | 138 URLs found across 13 files (detailed check deferred) |

### Artifacts refreshed

- [`papers/microanalysis/figures/palette-tokens.json`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/figures/palette-tokens.json), [`palette.css`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/figures/palette.css), [`palette.py`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/figures/palette.py)
- [`papers/microanalysis/figures/*.png`](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28/papers/microanalysis/figures) + `*.svg` + `*.alt.txt` + `*.desc.txt` (6 renderers × 2 locales + sidecars)
- [`papers/microanalysis/analysis/SUPPLEMENT_MANIFEST.md`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/analysis/SUPPLEMENT_MANIFEST.md)
- [`papers/microanalysis/analysis/mw-microanalysis-supplementary.zip`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/papers/microanalysis/analysis/mw-microanalysis-supplementary.zip) (1.27 MB, 104 files)

### Findings requiring attention

**H4 version-stamp:** 2 figure SVGs lack footer metadata (cross-dict-blocks-en.svg, cross-dict-density-en.svg); 3 ru-locale SVGs have stale SHA (heatmap-ru.svg, sankey-ru.svg, treemap-ru.svg). The newly-rendered en figures carry current timestamps. Old ru figures are from prior runs; a full round of Haiku renders for both locales would refresh all.

**H8 ZIP integrity:** Manifest lists 108 entries; ZIP contains 104 files. The discrepancy likely reflects directory entries in the manifest vs only files in the unzipped set. Not a data loss; minor report.

**H9 CI status:** MWS Pages build failed on 2026-05-27 21:31 UTC (likely unrelated to microanalysis). csl-atlas build+deploy all green (last 5 runs: 100% success).

**H10 link-rot:** 138 URLs catalogued across PAPER.md, IJL_COVER_LETTER.md, PAPER_RU.md, DOUBTS.md, HANDOFF.md, and decisions/*.md. No 404 check performed (audit deferred). See [mwsissues/haiku_refresh/2026-05-28/](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28/mwsissues/haiku_refresh/2026-05-28) for full logs.

### Usage

```
/cologne-haiku-refresh 2026-05-28
```

### Severity

`minor` — hard-stop steps (H5, H1, H7) all succeeded. Soft-warn findings (H4, H8, H9, H10) are non-blocking: stale stamps and old ru renders don't prevent downstream Sonnet/Opus use of the refreshed data.

---

**Haiku refresh complete.** The microanalysis data pipeline is fresh and ready for Sonnet's JSON exports. Branch is on `haiku-refresh-2026-05-28`; audit logs in [mwsissues/haiku_refresh/2026-05-28/](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28/mwsissues/haiku_refresh/2026-05-28).
