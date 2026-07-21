# Changelog

All notable changes to MWS are documented here.

This repository does not currently publish versioned release notes. Entries use
dated maintenance snapshots; keep upcoming work under [Unreleased] until it is
ready for a dated entry.

## [Unreleased]

## [1.0.4] - 2026-07-18

### Added - H966 kill-gate finding on review packets A/B/C
- [review_packets/H966_KILL_GATE_FINDING.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/H966_KILL_GATE_FINDING.md) (Sonnet 5 `claude-sonnet-5`, [PR #251](https://github.com/sanskrit-lexicon/MWS/pull/251)) — confirmed packets A/B/C (`ib.` resolution, band-3 `L.`→DCS, MW-vs-Whitney class conflicts) are not agent-fillable: every verdict is a genuine Sanskritist judgement call with no reproducible procedure. 0 verdicts fabricated; all three remain 100% blank pending human review.

## [1.0.3] - 2026-07-16

### Added - A18 paper (evidentiary stratification of MW's citation apparatus) + register census

- [papers/p3_citation_registers/A18_citation_registers_paper.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/A18_citation_registers_paper.md) — A18 drafted outline → full manuscript (readiness 2/5 → 3/5, H1076, Fable 5 `claude-fable-5`), venue *Dictionaries* (2027). Argues MW's single formal citation register (A08's Register A) decomposes into five **evidentiary** strata, and reads the `<ls>L.</ls>` hedge as Register-B kośa content compressed into a Register-A slot with the source name deleted.
- [papers/p3_citation_registers/register_census/](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/register_census/) — new deterministic census over `csl-orig` `mw.txt`: every one of MW's 320,828 tagged citations classified (attested 18.96% · bare 59.35% · hedge 12.53% · authority 6.02% · relative 3.15%), with per-stratum sigla, entry-level composition, and a self-check that the attested stratum decomposes exactly.

### Fixed - two propagated measurement errors in MW's apparatus figures

- **MW's scan-link ceiling was overstated ~2×.** [ROADMAP.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ROADMAP.md) (§status table, §W1, weaknesses row 2) and [SYNTHESIS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/SYNTHESIS.md) gave MW's apparatus as "22.3% meta + 40.2% bare-locator", implying ~37.5% text-linkable. The 40.2% was never an MW measurement — it is the **corpus-wide** CDSL bare share from a since-superseded 43-dictionary revision of csl-atlas' `CITATION_REGISTERS.md`, an aggregate dominated by PWG (4.61 `<ls>`/entry vs MW's 1.09); the two components were computed over different populations and were never additively coherent. MW's own locator-bearing share is **18.96%**.
- **csl-atlas' MW row undercounts the apparatus by 28.6%** (reported upstream, not fixed here): its extractor is literal (`_LS = re.compile(r"<ls>(.*?)</ls>")`, `scripts/forensic/parse_cslorig.py:41`) so it misses MW's 8,668 attributed-shape citations (`<ls n="RV.">vii, 96, 3</ls>`), and its locator rule (`re.compile(r"\d")`) misses 4,866 roman-only locators (`<ls>ŚBr. xiv</ls>`). Both its published figures (`ls: 312160`, `lsWithLocator: 47289`) reproduce exactly under its own rule, which localises the divergence.

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
