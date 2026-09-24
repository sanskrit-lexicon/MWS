# SIGNOFF A18 — author-voice pass on A18_citation_registers_paper.md: residual human rulings

_Created: 06-09-2026 · Last updated: 24-09-2026 (§4 added: re-sync + venue-fit pass, H5326)_

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

## 4. Re-sync + venue-fit pass, 24-09-2026 (H5326, Fable 5.1 `claude-fable-5-1`)

**What this pass is.** Not a voice pass: it re-derives every atlas-dependent figure against the
live [`csl-atlas` `data/obs/citation_registers.json`](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/data/obs/citation_registers.json), pins the build, and fits the
manuscript to the [*Dictionaries* style sheet (June 2024)](https://dictionarysociety.com/wp-content/uploads/2024/07/Style-Sheet-Dictionaries-June-2024.pdf). Numbers changed by
design, so the H3857 numeric drift gate does not apply; the receipts are below instead.

### 4.1 The one finding that drove the pass

The atlas MW row the draft "corrected" in §6.2 (`ls: 312160`, `lsWithLocator: 47289`) had
**already been regenerated upstream on 17-07-2026** — [csl-atlas PR #266](https://github.com/sanskrit-lexicon/csl-atlas/pull/266) (H1086, commit
[`c89e679`](https://github.com/sanskrit-lexicon/csl-atlas/commit/c89e67979bc3f50809aac3817a5ef6c61806374c)), one day after the draft was written — and the fix was **corpus-wide**, so
§2, §6.1, §6.2 and §7 all carried pre-fix atlas numbers for ten weeks. Live row today: `ls` 320,828 ·
`lsWithLocator` 60,822 · corpus `ls` 1,517,609 · locator share 66.8 % · PWG 801,788 at 6.50/entry ·
27 of 44 dicts with zero `<ls>`. The 2-citation gap (60,822 vs our 60,820) is the two meta sigla with
a locator-shaped token (`L. i`, `W. 1`) and is documented in PR #266's own body.

### 4.2 Figures changed (old → new, section)

| # | Section | Old | New | Source |
|---|---|---|---|---|
| 1 | §2 | 1,245,644 · 59.3 % · ~41 % | 1,517,609 · 66.8 % · 33.2 % (old pair kept as history) | `totals` in the live artifact |
| 2 | §1 | "28 of 44 dictionaries carry no tagged citations" | 27 of 44 | live artifact (`ls == 0` count) + [CITATION_REGISTERS.md](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/CITATION_REGISTERS.md) line "27 of the 44" |
| 3 | §6.1 | PWG 568,730 at 4.61/entry vs MW 1.09; atlas "reports 40.7 %/59.3 %" | PWG 801,788 at 6.50 vs MW 1.12; three generations named (43-dict 40.2/59.8 → 44-dict pre-fix 40.7/59.3 → post-fix 33.2/66.8) | live `pwg`/`mw` rows |
| 4 | §6.1 | "15.15 % by the atlas's stricter one" (present tense) | atlas now also 18.96 %; 15.15 % is its pre-fix figure | live `mw` row |
| 5 | §6.2 | "undercounts … the MW row wants regenerating" | rewritten as a reported-and-adopted correction; Table 3 gains an "after" column; pre-fix code pinned to `efd52b8`; corpus-wide effect stated | PR #266 |
| 6 | §6.2 | atlas bare bucket "is 84.85 %" | 81.0 % after the fix (260,006 / 320,828), 84.85 % before | computed from the live row |
| 7 | §7 | neither "312,160 citations" nor … | "320,828 citations" | — |
| 8 | §7 | "57.1 % (5,762) of the resolutions are same-cluster" | of the 10,094 `ib.` citations (§2 flag 3 of this file — the module's denominator is all `ib.`, 5,762 + 4,332 = 10,094) | [relative_refs/IB_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/relative_refs/IB_SUMMARY.md) |
| 9 | §7 matrix | MW 9.16 % | 9.16 % (29,392; rounded rows sum to 9.17 %) — §2 flag 4 | census_stats.json |
| 10 | Abstract, §1 item 4, §6 intro | "both … flattered / overstated the apparatus" | one overstated, one understated — the draft contradicted its own §6.2 (an undercount does not flatter) | — |
| 11 | §8 sigla | — | added the atlas fold-layer facts (MBH./MBh. 75,548; ṚV./RV. 32,316) and that its resolvability band awaits a re-run on the corrected extraction | CITATION_REGISTERS.md |
| 12 | §8 source · §9 | "@DO: pin the `mw.txt` source commit" | pinned: `csl-orig` [`de8c186`](https://github.com/sanskrit-lexicon/csl-orig/commit/de8c186); re-run 24-09-2026 against head [`f4c08c5`](https://github.com/sanskrit-lexicon/csl-orig/commit/f4c08c5) reproduces `census_stats.json` byte-identically (both runs) | this pass, `/tmp/census_rerun.sh` receipts in the PR body |

### 4.3 Venue fit applied (style sheet → manuscript)

1. American spelling (artefact→artifact, digitisation→digitization, characterisable, normalisation, defence, programme, catalogue, capitalised — 14 tokens; verifier round 1 caught two more, neighbour and travelled, plus "New edn." → "New ed." and one period-outside-quote — fixed in the follow-up PR).
2. Em dashes closed (66 spaced " — " → "—"; the two inside the §3.1 code fence left alone).
3. Tables numbered and titled (Table 1 rules · Table 2 census · Table 3 atlas before/after · Table 4 matrix), each referred to by number in the text.
4. Glosses in single quotes ('Lexicographers'), centuries in words (19th→nineteenth, 3×), dates in MONTH DAY, YEAR where they occur in the body.
5. Author-date citations added at first mention (Monier-Williams 1899; Cologne Digital Sanskrit Dictionaries 2026; Gasūns 2026 for the atlas; Hellwig 2010–2026 for DCS; Whitney 1885) and a §10 References list in the sheet's formats (book · web paper · dictionary). Every in-text cite has a list entry and vice versa.
6. §9's project-internal `@DO` line moved into the draft-status block; the body is journal-clean except the block itself, which is deleted at export.
7. Not applicable to the Markdown source, noted for the docx export: Times New Roman 12 pt, double spacing, tab indents, run-in secondary headings, hanging-indent references, no automated heading styles. The sheet states **no word limit**.

### 4.4 Still human (unchanged from §2, renumbered)

1. Byline/venue confirm + final read (draft-status item 1).
2. Dataset DOI (item 2) — the source commit is pinned, the DOI is not minted.
3. §5.3 sense-level gate (item 3 / old §2 flag 7): `sense_verify/` 80-sense sample still unadjudicated.
4. §2 flag 1 (two headers + YAML between them): the two `Created` dates are now unified to the git creation date 17-07-2026; the YAML-between-headers layout is left for the export step.
5. Megastructure evidence: [H5324](https://github.com/gasyoun/Uprava/blob/main/handoffs/H5324-Opus_csl-atlas_megastructure-catalogue-schema-pilot-skd-mw_23.09.26.md)/[H5325](https://github.com/gasyoun/Uprava/blob/main/handoffs/H5325-OxAlpha_csl-atlas_megastructure-catalogue-remaining-seven-dicts_23.09.26.md) are open (🟡 at 24-09-2026); nothing exists to fold. If they ship before submission, the only natural hook is §8's "cited editions" limitation.

Resolved and closed by this pass: old §2 flags 2 (heading), 3 (denominator), 4 (9.16/9.17), 5 (source pin half), 6 (item 3 — went upstream and was fixed).


_Dr. Mārcis Gasūns_
