# Microanalysis audit scripts

Reproducible scripts that audit the claims in [PAPER.md](../PAPER.md) against the
live dictionary data, addressing the empirical doubts in [DOUBTS.md](../DOUBTS.md).
Each script reuses the **published** block-detection algorithm
([`../figures/scripts/export_data.py`](../figures/scripts/export_data.py)) via
[`_common.py`](_common.py), so the audits test the actual algorithm that produced
the figures — not a re-implementation.

## Data dependency

The dictionary `.txt` files are read from the MSYS `/tmp` (= Windows
`%LOCALAPPDATA%\Temp`): `mw.txt`, `pwg.txt`, `pw.txt` (PWK), `ap.txt`, `wil.txt`,
`ben.txt` (Benfey 1866), `cae.txt` (Cappeller 1891), `skd.txt`, `vcp.txt`. They are **not** committed here.
Refresh them from [`csl-orig`](https://github.com/sanskrit-lexicon/csl-orig) before
re-running.

## Scripts → reports → doubt addressed

| Script | Report | Doubt | What it does |
|---|---|---|---|
| [`spotcheck_blocks.py`](spotcheck_blocks.py) | [SPOTCHECK.md](SPOTCHECK.md) + `SPOTCHECK_SAMPLE.txt` | [D6](../DOUBTS.md#d6--block-detection-is-regex-based-and-approximate--important) | Reproduces the 286,561 count; quantifies F08/F09 over-counts and the F11 under-count; emits a 100-record labelled sample (seed 42) for human review. |
| [`significance.py`](significance.py) | [SIGNIFICANCE.md](SIGNIFICANCE.md) | [D7](../DOUBTS.md#d7--the-block-by-article-type-matrix-has-no-statistical-significance-test--nice-to-resolve) | Chi-square / Fisher per (type, block) vs baseline; Wilson 95% CIs; headline-claim audit incl. the D7 noun_m-vs-noun_f F08 pairwise test. |
| [`significance_full.py`](significance_full.py) | [SIGNIFICANCE_FULL.md](SIGNIFICANCE_FULL.md) | [D7](../DOUBTS.md#d7--the-block-by-article-type-matrix-has-no-statistical-significance-test--nice-to-resolve) | The complete 270-cell table with Benjamini–Hochberg FDR correction (217/270 significant at q=0.05). |
| [`check_docs.py`](check_docs.py) | (prints) | — | Docs-integrity: validates every relative file link and `#anchor` across the microanalysis + docs-pass markdown. |
| [`make_supplement.py`](make_supplement.py) | [SUPPLEMENT_MANIFEST.md](SUPPLEMENT_MANIFEST.md) | [Decision 16](../decisions/SUPPLEMENTARY.md) | Bundles paper + scripts + reports + figures into the reproducibility ZIP (gitignored). |
| [`ls_hedge_check.py`](ls_hedge_check.py) | [LS_HEDGE_CHECK.md](LS_HEDGE_CHECK.md) | [D2](../DOUBTS.md#d2--the-lslls-mw-innovation-claim--under-checked--important) | Counts the generic `<ls>L.</ls>` hedge and the `<ls>` apparatus across all eight dictionaries. |
| [`cross_dict_kernel.py`](cross_dict_kernel.py) | [CROSS_DICT.md](CROSS_DICT.md) | [D1](../DOUBTS.md#d1--is-block-economy-a-genuine-principle-or-print-economic-artifact--important) | Format-robust block-economy *shape* comparison across all nine dictionaries. |
| [`cross_dict_profiles.py`](cross_dict_profiles.py) | [CROSS_DICT_PROFILES.md](CROSS_DICT_PROFILES.md) | [D1](../DOUBTS.md#d1--is-block-economy-a-genuine-principle-or-print-economic-artifact--important) | Per-type block *profiles* across all nine dicts — Part A: 7 structured bilingual dicts (type differentiation); Part B: why SKD/VCP fall outside the framework. |
| [`export_dict_blocks.py`](../figures/scripts/export_dict_blocks.py) | `{code}_blocks.json` files | [Decision 5](../decisions/SUPPLEMENTARY.md#decision-5--per-dict-block-profiles-for-atlas-chapters) | Generates per-dict block-matrix JSON exports for all 9 CDSL dicts (input: mw.txt, pwg.txt, etc. from `/tmp`). Includes LEXMAP for cross-dict adjective normalisation. |
| [`phase4_rollout.py`](phase4_rollout.py) | GitHub tracking issues + branch creation | [Decision 7](../decisions/MICROSITE.md#decision-7--hosting-new-repo-csl-atlas) | Phase-4 automation: creates docs-pass branches and DICT_PROFILE.md stubs for 15 CDSL repos via GitHub API; tracks progress in per-repo issues. |
| [`push_pwg_roadmap.py`](push_pwg_roadmap.py) | `{repo}/ROADMAP.md` on docs-pass | — | Synthesises GitHub issues into quarterly roadmap (9 task subtypes); generates ROADMAP.md for Phase-4 rollout repos. |
| [`push_pwg_dict_profile.py`](push_pwg_dict_profile.py) | `{repo}/DICT_PROFILE.md` on docs-pass | [DICT_PROFILE](../../../DICT_PROFILE.md) | Generates full DICT_PROFILE.md per MWS template (15 sections: At-a-Glance through BibTeX). Reusable template for Phase-4 rollout. |
| [`check_figure_consistency.py`](check_figure_consistency.py) | (prints to stdout) | [Decision 16](../decisions/SUPPLEMENTARY.md#decision-16--reproducibility-supplement-manifest--28-audits) | 28 consistency checks across figure data files and per-dict blocks.json; validates total records, per-type counts, cross-dict MW consistency, per-dict block records. |
| [`lint_markdown.py`](lint_markdown.py) | (modifies files in-place) | — | Markdown format conformance: removes trailing whitespace, converts tabs to spaces, ensures blank lines before code fences. |

Run any of them from this directory: `python spotcheck_blocks.py` (needs
`scipy`, `numpy` for `significance.py`).

## Headline findings (2026-05-24)

- **D6** — detector reproduces the count exactly; **F08 over-counts** (36.5% of its hits are compound members, not inflected forms) and **F09 over-counts** (66.7% of hits outside a philological context); **F11 under-count is negligible**; the §4 "display headword 99%" was the structural-key rate — the *rendered* `<s>` rate is **76%** (corrected in PAPER.md §4).
- **D7** — every headline contrast is **significant** (p ≈ 0, with CIs); the small noun_m-vs-noun_f F08 difference is **not** (p = 0.07), confirming the doubt.
- **D2** — MW has 40,212 `L.` hedges; **PWG, PWK, WIL, CAE, SKD, VCP have 0; AP has 1; Benfey 1866 has 0** despite a full citation apparatus — strengthening the innovation claim. **Cappeller (CAE) fetched**: zero `<ls>` apparatus but two undocumented markers (asterisk `*` 1,370×, dagger `†` 903×); checked all CDSL metadata — none documents them, so the meaning needs Cappeller's 1891 print preface.
- **D1** — block-economy *shape* is **general to all single-volume CDSL dictionaries**, not MW-specific (modal blocks/entry: MW 5, PWG 4, PWK 3, AP 2, WIL 3, Benfey 3, Cappeller 3); PWG is ~4× denser per entry. The *profile* construct ties to economy: single-volume dicts differentiate types (MW 11.3, PWK 7.7, AP 15.2 pts) while multi-volume PWG cites uniformly (0.4); SKD/VCP fall outside the framework (no `<lex>`/`<ls>`; inline `iti` citation). Claims softened in PAPER.md §4/§8/§9.3.
