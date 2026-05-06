MWS
===

Monier Monier-Williams, Sir; *A Sanskrit-English Dictionary*. Oxford, 1899.

This repository holds corrections, enhancements, and tooling for the [Cologne digitization](http://www.sanskrit-lexicon.uni-koeln.de/) of the MW dictionary. The canonical source data (`mw.txt` in SLP1 encoding) lives in the companion repository [csl-orig](https://github.com/sanskrit-lexicon/csl-orig), and the build system is in [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork). Issues and corrections are tracked at the [MWS GitHub issue tracker](https://github.com/sanskrit-lexicon/MWS/issues).

## Contents

| Directory | Description |
|-----------|-------------|
| `history/` | Original MONIER.ALL from Thomas Malten (2004); cp1252→UTF-8 conversion |
| `homophone/` | Homophone markup corrections and enhancements; Java and Python pipelines |
| `mwtranscode/` | Transcoding between SLP1, IAST, and Devanagari |
| `mwsissues/` | Per-issue correction workflows and documentation |
| `mwabbreviations/` | Analysis of abbreviations used in the digitization |
| `mwauthorities/` | Works and authors cited in MW |
| `mwverbs/` | Verb and preverb extraction from the digitization |
| `botbio/` | Botanical (`<bot>`) and biographical (`<bio>`) tag extraction |
| `k1k2/` | Headword key1/key2 clash analysis |
| `accent_diff/` | Accent markup discrepancy analysis |
| `Lithuanian/` | Lithuanian word list comparison against MW |
| `mwsupplement/` | MW supplement entries |
| `greek_andhrabharati/` | Greek words comparison between Cologne digitization and Andhrabharati |
| `CORRECTIONS_issue_362/` | Language-tag corrections from Andhrabharati (csl-corrections issue #362) |
| `verbs01/` | Verb merge and cross-reference tooling |
| `transcodeExample/` | Example transcoder PHP/Python scripts and SLP1→IAST table |
| `basic04a/` | Simple two-dictionary web display sample |
| `list02php/` | PHP-based display sample |

## Timeline

| Date | Milestone |
|------|-----------|
| 2004 | Thomas Malten provides MONIER.ALL — original digitization in cp1252 encoding |
| Jan 2014 | Repository initialized; early data analysis (hiatus entries, avagraha, space in keys) |
| Sep 2014 | Transcoder example added (issue #5) |
| Apr–Jun 2015 | Homophone corrections: ~6,500 removeHom + 10,913 artificial homophones assigned |
| Dec 2015 | k1k2 headword clash analysis |
| Jul 2016 | mwauthorities XML structure established |
| Feb 2017 | Web display samples added (basic04a, list02php) |
| Nov 2017 | mwabbreviations analysis added |
| Jan 2020 | Greek words file received from Andhrabharati (issue #89) |
| Jun 2020 | botbio tag extraction and mwverbs pipeline added |
| Jan 2021 | mwtranscode: SLP1 ↔ IAST ↔ Devanagari pipeline; Lithuanian comparison; Andhrabharati (AB) version work |
| 2024 | Issues 141–181: accent corrections, Grassmanizing, AB3 (Andhrabharati) alternate format, supplement revisions |
| Aug–Nov 2025 | Issue 190: recovery of 16+ lost headwords (with Andhrabharati and aumsanskrit) |
| Feb 2026 | History folder: MONIER.ALL archived and documented |

## Contributors

- **Thomas Malten** — provided the original MONIER.ALL digitization (2004)
- **Peter Scharf** — designed the rational extension of homophone markup (2013); requested Python reimplementation
- **Pawan Goyal** — co-designed homophone markup with Scharf (2013)
- **Jim Funderburk** ([@funderburkjim](https://github.com/funderburkjim)) — primary repository maintainer; tooling and correction workflows
- **Mārcis Gasūns** ([@marcis-gasuns](https://github.com/marcis-gasuns)) — initial commit and early data analysis
- **drdhaval2785** ([@drdhaval2785](https://github.com/drdhaval2785)) — k1k2 clash analysis; AB/Cologne comparison tooling
- **Andhrabharati** (Nagabhushana Rao) — Greek words file; AB version analysis; extensive issue contributions
- **aumsanskrit** — issue analysis and corrections (issue #190 and others)
- **Darius** — Lithuanian word list comparison

## Homophone corrections and enhancements

See the [readme.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/homophone/readme.txt) in the homophone directory.
