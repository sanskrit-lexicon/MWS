# SIGNOFF A18 — author-voice pass on A18_citation_registers_paper.md: residual human rulings

_Created: 06-09-2026 · Last updated: 06-09-2026_

**Paper:** [A18_citation_registers_paper.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/A18_citation_registers_paper.md) (A18, "One Slot, Many Warrants: The Evidentiary Stratification of the Citation Apparatus in Monier-Williams' *Sanskrit-English Dictionary*", EN; venue *Dictionaries: Journal of the Dictionary Society of North America*). Readiness before this pass: 3/5 (full draft, pending author sign-off).
**Pass:** author-voice pass per [H3857](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md), Fable 5.1 (`claude-fable-5-1`), 06-09-2026.
**Scope discipline:** voice, register and framing only; no number, claim or citation altered; mechanical drift gate ([voice_drift_check.py](https://github.com/gasyoun/Uprava/blob/main/tools/voice_drift_check.py) against `origin/master`) CLEAN — numbers 229 = 229, URLs 6 = 6, IAST 25 = 25, headings 19 = 19, table rows 26 = 26. The only lines excluded from the gate are the two dated headers and the status line that now names this file.

**Instruction:** read this file (~30 minutes together with a spot-check of the places below), veto any voice call you dislike (each reverts with one edit), and rule on the substance flags in §2 — only after that should readiness move.

---

## 1. Voice calls made — each may be vetoed

Full diff: the commit of this pass on branch `voice-pass/A18`. The manuscript was already close to the author's voice (direct claims, transitions that carry the thread, the §1 question answered in §7); the pass is correspondingly light.

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | File header (line 1) and paper header (under the H1) | `Last updated` bumped to 06-09-2026 in both; front-matter `status:` gains "author-voice pass 06-09-2026 (SIGNOFF_A18_author_pass.md)" | Brief-mandated header note; the `Created` mismatch between the two headers is flagged in §2, not fixed |
| 2 | §1, contribution paragraph | "Our claim is that **register is one axis and warrant is another** … We contribute:" → "Its one claim is that **register is one axis and warrant is another** … Four contributions carry that claim:" | One explicit singular contribution statement; the claim sentence is the abstract's own, at the same strength, and the four numbered items are unchanged |
| 3 | §2, "Two things follow" | "and it is worth separating them" → "and they need to be kept apart" | "it is worth …" is an empty opener from the de-AI list |
| 4 | §3.2, last sentence | "which is precisely why the corpus test in §5 needs a strict subset" → "which is why …" | Filler intensifier |
| 5 | §5.1, DCS-2021 / DCS-2026 sentence | "The stability across snapshots is worth exactly what it is worth and no more — these are …" → "The stability across snapshots should not be over-read: these are …" | Decorative tautology; the qualification that follows (controls for version, not for DCS's conventions) is untouched and still carries the hedge |
| 6 | §5.2, homograph control | "The restriction is not fussiness." → "The restriction does real work." | Rhetorical "not X" denial with no content of its own; the next sentence is the argument |
| 7 | §6.3, closing paragraph | Re-wrapped the one over-long line after "or **28.6%**.)"; "stated in §3.1 for exactly this reason" → "stated in §3.1 for this reason" | Line hygiene plus one filler intensifier |
| 8 | §7, matrix lead-in | "the objects a reader, a lexicographer, and a parser each actually need" → "… each need" | Filler adverb |
| 9 | §7, "For the digital apparatus" | "it is exactly how the two errors in §6 arose" → "it is how the two errors in §6 arose" | Filler intensifier |
| 10 | §7, "For the linkable core", last sentence | "But they establish the direction:" → "But the numbers establish the direction:" | Dangling pronoun — the preceding sentence's subject is "All of it", so "they" had no antecedent |

Not done, deliberately (human ruling, see §3, and consistent with the A16/A17 passes in this repo): the editorial "we/our" (34 occurrences) was left as is; the bold on key phrases in running text was left as is; the many "not X; it is Y" contrasts that carry substance (§2 "not a rounding error … a category mistake", §4 "not a weaker citation … a kośa quotative with its source field emptied", §6.3 "The defence is not better regexes") were kept because each half states a claim.

## 2. Substance flags carried (not fixed)

1. **Two dated headers with two creation dates.** Line 1 says `Created: 17-07-2026`, the header under the H1 says `Created: 16-07-2026`, and the YAML front matter sits *between* them, so it is not front matter for any renderer (it will show as a horizontal rule plus literal `paper_id:` lines). One header, at the top of the file, before submission; the byline then needs to move out of the YAML block into the visible text under the H1 (it is present now only as the `author:` key).
2. **§6.2 heading says "undercounts its apparatus by 28.6%".** The 28.6% is the locator-bearing (linkable) share (60,820 vs 47,289); the apparatus as a whole is undercounted by 2.7% (8,668 of 320,828). The body says this correctly ("MW's linkable apparatus is thus 28.6% larger"); the heading overstates it. Heading text is off-limits to this pass.
3. **§7, `ib.` resolution: "57.1% (5,762) of the resolutions are same-cluster".** 5,762 / 10,094 = 57.1%, so the denominator is all `ib.` citations, not the 7,538 resolutions (5,762 / 7,538 = 76.4%). Either "of the `ib.` citations" or the 76.4% figure; carried from `relative_refs/`, so check which the module reports.
4. **§7 matrix, "relative / authority — MW 9.16%".** From raw counts (29,392 / 320,828) the figure is 9.16%; a reader adding the table's rounded rows gets 6.02 + 3.15 = 9.17%. One clause, or round the row from the sum.
5. **Draft-status blockquote and the `@DO` items.** The block under the H1 (four open author items, "Scope discipline") and §9's closing "**@DO before submission:** pin the `mw.txt` source commit and mint the dataset DOI" are project-internal and cannot go to a journal. The two open items themselves are still open: no pinned `mw.txt` commit, no dataset DOI.
6. **Draft-note item (3) is still undecided:** whether the §6.2 correction to the atlas MW row (`ls: 312160` → 320,828; `lsWithLocator: 47289` → 60,820) travels as a footnote or as an issue against `csl-atlas`. §6.2 now says "the MW row wants regenerating", which is the issue route; a human should decide, since a fix there changes a published number.
7. **Draft-note item (4), the sense-level gate.** §5.3 states the lemma-level 31% with its ceiling; the 80-sense `sense_verify/` sample is packaged but not adjudicated. Publishing without it is a defensible choice already argued in §5.3; publishing with it changes the strength of §5's headline.
8. **Relative links.** `[register_b/](register_b/)`, `[lexicographer_dcs/](../../lexicographer_dcs/)`, `relative_refs/`, `root_crosswalk/`, `botanical_glossary/`, `sense_verify/`, `register_census/` resolve only inside the GitHub tree; a submitted PDF loses them. Untouched (URL rule); a submission copy needs full URLs or a data-availability footnote.
9. **§2 `iti` count, 250 vs the atlas's 172.** The paper says the gap is 45% and calls both noise-level; §8 says MW's 250 is the atlas's own word-boundary indicator. If the same indicator gives two counts, the sentence "The atlas's own count is 172" needs one clause saying what differs (source snapshot, tag stripping). Not a voice matter.
10. **Editorial "we" in a single-author paper.** *Dictionaries* accepts first-person singular; 34 occurrences of "we/our", one mechanical pass. Same ruling as A16, left to a human so the three MWS papers move together.

## 3. Read-and-sign

1. ~30 minutes: read §1 against the diff and veto by reverting single rows; then rule on §2 items 2, 3 and 4 first (each touches a stated figure or a heading), then item 6 (the csl-atlas issue vs footnote).
2. Two voice rulings a human should decide, not made here: (a) editorial "we" → "I" throughout; (b) whether the bolded key phrases in running text stay for the journal (copy-editing will usually strip them).
3. Proposed readiness after §2 items 1–5 are handled: 4/5 (propose only — a human confirms; 5/5 waits on the pinned source commit, the DOI and the final read). Venue: *Dictionaries* (DSNA) stands; the paper's shape (one dictionary, an apparatus census, two measurement corrections) fits its historical-lexicography strand and no change is recommended.
4. Submission is frozen until 2026-11-01; nothing here is a submission step.

_Dr. Mārcis Gasūns_
