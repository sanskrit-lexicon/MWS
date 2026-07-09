# Changelog

All notable changes to MWS are documented here.

This repository does not currently publish versioned release notes. Entries use
dated maintenance snapshots; keep upcoming work under [Unreleased] until it is
ready for a dated entry.

## [Unreleased]

## [1.0.2] - 2026-07-09

### Added - A46 paper skeleton (MW 1899 preface as a methodological document)
- [papers/A46_mw_preface_method.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/A46_mw_preface_method.md) — paper A46 scaffolded (readiness 1/5 → 2/5, H395, [PR #235](https://github.com/sanskrit-lexicon/MWS/pull/235)): the 29-page 1899 front matter read as a primary methodological document, 8 stated-vs-measured pairings against the digitized dictionary (194,084 distinct headwords vs MW's stated 180,000).
- [papers/a46_preface_method_stats.py](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/a46_preface_method_stats.py) — stdlib-only recompute script for every mw.txt-derived figure in A46 (records, headwords, `<ls>` apparatus, accent incidence, `<hom>`, root-flagged records).
- Verified in passing: the 11 `prefaces/mwepref*.md` pages are the front matter of the **1851 English–Sanskrit dictionary** (Motilal Banarsidass reprint scans), a different work from the 1899 Sanskrit–English one.

## [1.0.1] - 2026-07-03

### Changed - Adjudication and review cycle completions

## [1.0.0] - 2026-06-13

### Added
- Added this changelog so repository-level changes have a stable home.
- Recorded the current repository purpose: Monier Monier-Williams, Sir; A Sanskrit-English Dictionary.

### Recent Git History
- 2026-06-13 Build verification review-packets (turnkey Sanskritist yes/no sheets)
- 2026-06-13 mw.txt structural-integrity review: data is sound (1 cosmetic flag)
- 2026-06-13 Reproducibility review: re-sync to corrected DCS data, kill drift hazards
- 2026-06-13 Apply red-team fixes: soften overstated claims across docs + generators
- 2026-06-13 Adversarial red-team of session findings; fix sense-as-record overclaim
