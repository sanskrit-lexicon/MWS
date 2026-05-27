# Reproducibility supplement — manifest (Decision 16)

Built by [`make_supplement.py`](make_supplement.py) into `mw-microanalysis-supplementary.zip` (a gitignored build artefact). The raw dictionary `.txt` files are not bundled — they live in [csl-orig](https://github.com/sanskrit-lexicon/csl-orig); the included scripts regenerate every derived artefact from them.

**88 files**, 2611 kB uncompressed (2026-05-27, after Opus O1–O10 + doubts batch).

## To rebuild

```
cd papers/microanalysis/analysis
python make_supplement.py

```

## Contents

- **(root)/** — 9 files
- **analysis/** — 18 files
- **decisions/** — 8 files
- **figures/** — 53 files

<details><summary>Full file list</summary>

- `PAPER.md`
- `README.md`
- `MICROANALYSIS.md`
- `DOUBTS.md`
- `VISUALISATIONS.md`
- `paper-grounded.md`
- `paper-wiegand.md`
- `paper-atkins-rundell.md`
- `paper-hausmann.md`
- `decisions/BUILD-ORDER.md`
- `decisions/FIGURES.md`
- `decisions/I18N.md`
- `decisions/MICROSITE.md`
- `decisions/NORMALISATION.md`
- `decisions/PALETTE.md`
- `decisions/README.md`
- `decisions/SUPPLEMENTARY.md`
- `analysis/_common.py`
- `analysis/check_docs.py`
- `analysis/cross_dict_kernel.py`
- `analysis/cross_dict_profiles.py`
- `analysis/ls_hedge_check.py`
- `analysis/make_supplement.py`
- `analysis/significance.py`
- `analysis/significance_full.py`
- `analysis/spotcheck_blocks.py`
- `analysis/CROSS_DICT.md`
- `analysis/CROSS_DICT_PROFILES.md`
- `analysis/LS_HEDGE_CHECK.md`
- `analysis/README.md`
- `analysis/SIGNIFICANCE.md`
- `analysis/SIGNIFICANCE_FULL.md`
- `analysis/SPOTCHECK.md`
- `analysis/SUPPLEMENT_MANIFEST.md`
- `analysis/SPOTCHECK_SAMPLE.txt`
- `figures/cross-dict-blocks-en.svg`
- `figures/cross-dict-density-en.svg`
- `figures/heatmap-en.svg`
- `figures/heatmap-ru.svg`
- `figures/sankey-en.svg`
- `figures/sankey-ru.svg`
- `figures/treemap-en.svg`
- `figures/treemap-ru.svg`
- `figures/cross-dict-blocks-en.png`
- `figures/cross-dict-density-en.png`
- `figures/heatmap-en.png`
- `figures/heatmap-ru.png`
- `figures/sankey-en.png`
- `figures/sankey-ru.png`
- `figures/treemap-en.png`
- `figures/treemap-ru.png`
- `figures/cross-dict-blocks-en.alt.txt`
- `figures/cross-dict-density-en.alt.txt`
- `figures/heatmap-en.alt.txt`
- `figures/heatmap-ru.alt.txt`
- `figures/sankey-en.alt.txt`
- `figures/sankey-ru.alt.txt`
- `figures/treemap-en.alt.txt`
- `figures/treemap-ru.alt.txt`
- `figures/cross-dict-blocks-en.desc.txt`
- `figures/cross-dict-density-en.desc.txt`
- `figures/heatmap-en.desc.txt`
- `figures/heatmap-ru.desc.txt`
- `figures/sankey-en.desc.txt`
- `figures/sankey-ru.desc.txt`
- `figures/treemap-en.desc.txt`
- `figures/treemap-ru.desc.txt`
- `figures/timeline-en.md`
- `figures/timeline-ru.md`
- `figures/mermaid-theme.json`
- `figures/palette-tokens.json`
- `figures/palette.css`
- `figures/palette.py`
- `figures/data/article-type-counts.json`
- `figures/data/avg-fullness-by-type.json`
- `figures/data/block-by-type-matrix.json`
- `figures/data/block-counts.json`
- `figures/data/cross-dict.json`
- `figures/data/fullness-distribution.json`
- `figures/scripts/build_palette.py`
- `figures/scripts/export_cross_dict.py`
- `figures/scripts/export_data.py`
- `figures/scripts/render_cross_dict.py`
- `figures/scripts/render_heatmap.py`
- `figures/scripts/render_sankey.py`
- `figures/scripts/render_treemap.py`
- `figures/locales/en.json`
- `figures/locales/ru.json`

</details>
