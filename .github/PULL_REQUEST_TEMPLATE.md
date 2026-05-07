<!--
Thank you for contributing to a CDSL repository.
Please fill in the sections below before submitting.
-->

## Summary

<!-- One sentence: what does this PR change and why? -->

## Type

<!-- Tick one -->
- [ ] `text-correction` — typo, missing word, wrong gloss
- [ ] `markup` — XML tag content or structure
- [ ] `link-target` / `link-splitting` — citation linking
- [ ] `encoding` — SLP1/IAST/Devanagari transcoding
- [ ] `content-enhancement` — new material or display upgrade
- [ ] `bug` — broken link / malformed XML / broken file
- [ ] `scan-quality` — replacement scan
- [ ] `documentation` — README, CLAUDE.md, CONTRIBUTING.md, etc.

## Related issues

<!-- e.g. Fixes #123, refs #456 -->

## Authority for the change

<!-- Print edition, scholarly authority, or rule that justifies the correction.
     For markup changes, link to the relevant CLAUDE.md / data dictionary section. -->

## Verification

<!-- How did you verify the change? -->
- [ ] Ran `python updateByLine.py` (if applicable) and the output diff matches expectation
- [ ] Round-trip SLP1 ↔ IAST checked (for encoding changes)
- [ ] No `<L>` / `<LEND>` imbalance introduced (run `scripts/count_headwords.py` from `csl-observatory`)

## Licence

By submitting this pull request I agree my contribution is licensed under the same terms as the repository (CC BY-SA 4.0 for data, GPL-3.0 for code).
