### Location

Round-2 Haiku-tier refresh per [HANDOFF_PROMPTS.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/HANDOFF_PROMPTS.md), executing the `/cologne-haiku-refresh` skill **after** the post-mortem patches landed (per [#197](https://github.com/sanskrit-lexicon/MWS/issues/197) and its [GAPS.md](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28/mwsissues/haiku_refresh/2026-05-28/GAPS.md)). All changes pushed to branch [`haiku-refresh-2026-05-28-rerun`](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun).

This is a validation run — the audit table below is what the patched skill produces end-to-end without manual cleanup. Compare against #197's original audit to confirm the lessons stuck.

@funderburkjim @Andhrabharati

---

## Round-2 Haiku refresh — 2026-05-28-rerun

### Audit table

| Step | Status | Findings |
|---|---|---|
| [H5 palette](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures/palette-tokens.json) | ✅ | 77 tokens, 3 outputs regenerated |
| [H1.5 data refresh](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures/data) | ✅ | skipped (mw.txt unchanged — conditional gate working as designed) |
| [H1 renderers](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures/scripts) | ✅ | heatmap=2, treemap=2, sankey=2, cross-dict=2 (all 4 renderers; en+ru where supported — cross-dict ru deferred per DOUBTS D11) |
| [H4 version-stamp](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures) | ✅ | 0 missing footers, 0 stale SHA — all 8 SVGs stamped at HEAD (`ceda6e3`) with the locale-agnostic verifier |
| [H3 PNG↔SVG](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures) | ✅ | 0 PNG-only, 0 SVG-only (perfect parity) |
| [H2 alt/desc](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures) | ✅ | 8 figures, all `.alt.txt` + `.desc.txt` sidecars present |
| [H6 locales](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures/locales) | ✅ | en=9, ru=9, perfect key parity |
| [H7 manifest](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/papers/microanalysis/analysis/SUPPLEMENT_MANIFEST.md) | ✅ | 104 files (parsed from `**N files**` header), ZIP 1.61 MB |
| [H8 ZIP integrity](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/papers/microanalysis/analysis/.gitignore) | ✅ | manifest=104, ZIP=104 — perfect match |
| [H9 CI status](https://github.com/sanskrit-lexicon/MWS/actions) | ⚠️ | MWS: [run 26556808199](https://github.com/sanskrit-lexicon/MWS/actions/runs/26556808199) blocks on ``Unknown tag 'Theil'`` in [DICT_PROFILE.md:235](https://github.com/sanskrit-lexicon/MWS/blob/master/DICT_PROFILE.md) (the German word "Theil" parsed as a Liquid tag — unrelated to microanalysis). Yesterday's `DATA_DICTIONARY.md` Liquid fix landed via [PR #198](https://github.com/sanskrit-lexicon/MWS/pull/198). csl-atlas: 5 successes. |
| [H10 link-rot](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/mwsissues/haiku_refresh/2026-05-28-rerun/h10_link_rot.log) | ⚠️ | 73 unique URLs HEAD-checked, **7 broken** (6 unique + 1 false-positive `<code` template-hole). Same set as #197 — broken URLs are content concerns, not skill bugs. Full report: [h10_link_rot.log](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/mwsissues/haiku_refresh/2026-05-28-rerun/h10_link_rot.log) |

### Artifacts refreshed

- [`papers/microanalysis/figures/palette-tokens.json`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures/palette-tokens.json), [`palette.css`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures/palette.css), [`palette.py`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures/palette.py)
- [`papers/microanalysis/figures/*.png`](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun/papers/microanalysis/figures) + `*.svg` + `*.alt.txt` + `*.desc.txt` (4 renderers × locales: 8 figure bases, 32 files total)
- [`papers/microanalysis/analysis/SUPPLEMENT_MANIFEST.md`](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/papers/microanalysis/analysis/SUPPLEMENT_MANIFEST.md)
- `papers/microanalysis/analysis/mw-microanalysis-supplementary.zip` (1.61 MB, 104 files) — **not committed** ([analysis/.gitignore](https://github.com/sanskrit-lexicon/MWS/blob/haiku-refresh-2026-05-28-rerun/papers/microanalysis/analysis/.gitignore) excludes `*.zip` by repo policy; rebuild locally with `python papers/microanalysis/analysis/make_supplement.py`)

### Findings requiring attention

**H9 CI status — `DICT_PROFILE.md` Liquid landmine:** the 2026-05-28 MWS Pages run ([26556808199](https://github.com/sanskrit-lexicon/MWS/actions/runs/26556808199)) fails on ``github-pages 232 | Error: Liquid syntax error (line 235): Unknown tag 'Theil'``. Source: [DICT_PROFILE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DICT_PROFILE.md) line 235 — the German word "Theil" (likely in a PWG dictionary part-reference like "*1. Theil*") sits inside `{% ... %}` brackets that Jekyll's Liquid templating engine tries to parse. Same root mechanism as the `DATA_DICTIONARY.md` fix that landed yesterday ([PR #198](https://github.com/sanskrit-lexicon/MWS/pull/198)); same remediation (`{% raw %}...{% endraw %}` wrap). Unrelated to microanalysis.

Additional non-fatal Liquid warnings in the same run come from [`mwsissues/issue178/rev1a/change_notes_rev1a.txt`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwsissues/issue178/rev1a/change_notes_rev1a.txt) lines 44/49/56 — record-number-pair strings like `{{16884.1, 16886.2}}` interpreted as Liquid output tags. Worth wrapping too (`{% raw %}...{% endraw %}`) to clean the warnings.

**H10 link-rot — same set as #197:** 6 unique broken URLs, all content concerns:

- `https://github.com/sanskrit-lexicon/{armh,abch,acph,acsj}` (404) — referenced in FIGURES.md, MICROSITE.md, PAPER.md, PAPER_RU.md. These look like planned dict-repo placeholders that don't exist yet.
- `https://amzn.github.io/style-dictionary/` (404) — PALETTE.md. Amazon's project relocated; needs an updated link.
- `https://www.ivran.ru/east` (404) — PAPER_RU.md. Likely moved.

One additional 404 (`https://github.com/sanskrit-lexicon/<code`) is a false positive — MICROSITE.md has a literal `<code…>` snippet that the URL regex caught.

These were also flagged on #197 and remain audit-only per skill design.

### Usage

```
/cologne-haiku-refresh 2026-05-28-rerun
```

### Severity

`medium` — hard-stop steps (H5, H1.5, H1, H7) all succeeded. Two ⚠️ rows: H9 (real CI failure but unrelated to microanalysis — content bug elsewhere in MWS) and H10 (real broken URLs, audit-only per skill). The skill's rule is `medium if any of H3/H2/H6/H8/H9 ⚠️` — H9 alone keeps the severity at `medium`.

### Comparison vs original 2026-05-28 run ([#197](https://github.com/sanskrit-lexicon/MWS/issues/197))

| Audit row | First run | This rerun | Delta |
|---|---|---|---|
| H1.5 data refresh | (didn't exist) | ✅ skipped (mw.txt unchanged) | new phase from skill patch |
| H1 renderers | partial (3 scripts, en only) | full (4 scripts × en+ru) | gap #6 + #7 fix landed |
| H4 version-stamp | ⚠️ (5 false alarms) | ✅ (0 missing, 0 stale) | regex patch + ru renders |
| H7 manifest | counted 108 (bug) | counted 104 (correct) | gap #10 patch landed |
| H8 ZIP integrity | ⚠️ (108 vs 104) | ✅ (104 vs 104) | downstream of #10 fix |
| H9 CI status | "1 failure" (vague) | named root cause `Unknown tag 'Theil'` | gap #11 patch landed |
| H10 link-rot | "138 URLs (deferred)" | 73 unique, 7 broken (real HEAD) | gap #9 patch landed |
| Labels | created off-script | auto create-if-missing | gap #3 patch landed |
| ZIP link | hyperlinked → 404 | bare-text with rebuild instruction | gap #12 patch landed |

**Conclusion:** all 9 skill-side gaps from #197 are sealed. The 2 ⚠️ rows in this rerun are content concerns external to the skill itself (one MWS-wide Liquid landmine + one set of stale prose URLs).

---

**Haiku refresh complete (rerun).** Microanalysis pipeline is fresh and ready for Sonnet's JSON exports / Opus's chapter authoring. Audit logs in [mwsissues/haiku_refresh/2026-05-28-rerun/](https://github.com/sanskrit-lexicon/MWS/tree/haiku-refresh-2026-05-28-rerun/mwsissues/haiku_refresh/2026-05-28-rerun).
