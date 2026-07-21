# Changelog

All notable changes to MWS are documented here.

This repository does not currently publish versioned release notes. Entries use
dated maintenance snapshots; keep upcoming work under [Unreleased] until it is
ready for a dated entry.

## [Unreleased]

### Changed - A17's coverage projection withdrawn: no unsourced percentage survives the hedge programme (H1380)
- [papers/microanalysis/PAPER_RU.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER_RU.md) §8(3) no longer projects "с текущих 64,0 % до ≈ 77 % (+12,9 п. п.)": the 64.0% base was [ENTRY_GUIDE.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md)'s **authority-record coverage** join (199,743/311,932) silently borrowed as a hedge-resolution base, computed on the census D23 superseded, with the +12.9 pp assuming 100% resolution. The conclusion now states the kośa-resolution programme qualitatively, cites A18 §5.1's measured **~31%** anchor with its unit (lemmas vs tags) and target (DCS vs the four *kośa*) mismatches stated, and names full resolution as a ceiling — reasoning recorded as [DOUBTS D24](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/DOUBTS.md); EN/RU twins now make the same claim (the projection was RU-only). A calibration correction to an openly flagged conditional, not the retraction of a concealed one. Review record annotated ([A17_review_fable5.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/A17_review_fable5.md) §7); PAPER.md pins in PAPER_RU repointed docs-pass→master. Fable 5 (`claude-fable-5`), [H1380](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1380-Fable_MWS_a17-hedge-projection-base-measured-band_20.07.26.md).

### Changed - A16 adopts A18's apparatus census + twin-table drift gate (H1379)
- [papers/microanalysis/PAPER.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md) App. B.3 restates MW's citation apparatus as **320,828 citations / 18.96% locator-bearing** per the A18 register census (run 2026-07-16, `mw.txt` @ 286,525 records), disclosing the superseded arabic-digit-only rule (311,932 / 15.1%) and its 28.6% undercount inline; §4's nine-dict PWG comparison deliberately keeps the literal rule, stated inline (author's ruling 21-07-2026, recorded as [DOUBTS D23](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/DOUBTS.md); Fable 5 `claude-fable-5`). [ENTRY_GUIDE.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md) + [DICT_PROFILE.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md) updated in the same pass so A16's citation links agree with the paper.
- [papers/microanalysis/analysis/check_figure_consistency.py](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/check_figure_consistency.py) gains section 7: the EN/RU §4 block-rate prose tables are now gated three ways (same row set, EN==RU after notation normalisation, exact decimals match `SPOTCHECK.md`) — the drift class that let the twins disagree on seven rows can no longer pass silently.

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
