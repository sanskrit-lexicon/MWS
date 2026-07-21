# SPEC-1 — W1(c): scan-link targets for Suśr., Kathās., ŚBr. (July batch)

_Created: 02-07-2026 · Last updated: 02-07-2026_

**Tier:** Sonnet 5 (`claude-sonnet-5`). One work per session; resumable. **Repo:** MWS
(writes under [mwauthorities/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities); csl-orig untouched).

## Objective

For each of **Suśr.** (17,284 cites), **Kathās.** (22,575), **ŚBr.** (5,493): produce a
verified per-work **scan + pagination index** (the decision-master-recommended "page index
first" shape), modeled on the existing
[mwauthorities/ls/20211005-panini](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities/ls/20211005-panini)
pattern.

## Steps (per work)

1. Confirm the edition MW cited: MW 1899 preface "Sources of the work" +
   the work's record in [mwauthorities_init.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/mwauthorities_init.txt).
   If the preface names an edition ambiguously, STOP and log the question in the tracking
   issue — edition identification beyond the preface is a frontier-tier call.
2. Locate a public scan (archive.org first) of THAT edition (or a page-concordant reprint).
3. Build `mwauthorities/ls/2026-07-<work>/pages.tsv`: locator-unit → scan page (chapter/verse
   → page for Kathās./Suśr.; kāṇḍa.adhyāya.brāhmaṇa → page for ŚBr.).
4. Validate against **5 random mw.txt citations** per work: extract the cited locator, resolve
   through pages.tsv, eyeball the scan page for the cited form. Record all 5 in a readme.
5. Document in a new MWS issue (milestone Dictionary to Book, label `link-target`), one issue
   per work; commit files + issue link.

## Acceptance

- pages.tsv covers ≥95% of the locator range cited in mw.txt (measure: extract all `<ls>` locators
  for the siglum, report % resolvable).
- 5/5 sample citations verified on the scan, shown in the readme.
- No edit to any `*_init.txt` authority file without the scan verification passing.

## Guardrails

Maintainer noise discipline (one issue per work, no comment streams). If the only findable
scan is a different edition with different pagination, deliver the index anyway but mark
`edition_mismatch: true` and stop before linking.

_Dr. Mārcis Gasūns_
