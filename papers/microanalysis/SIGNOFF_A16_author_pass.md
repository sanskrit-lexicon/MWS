# SIGNOFF A16 — author-voice pass on PAPER.md: residual human rulings

_Created: 06-09-2026 · Last updated: 06-09-2026_

**Paper:** [PAPER.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/PAPER.md) (A16, "The microstructure of *Monier-Williams 1899*: a data-grounded framework, triangulated against three metalexicographic traditions", EN; venue *International Journal of Lexicography*). Readiness before this pass: 5/5, journal voice already applied — this pass was deliberately conservative.
**Pass:** author-voice pass per [H3857](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md), Fable 5.1 (`claude-fable-5-1`), 06-09-2026. The RU twin [PAPER_RU.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/PAPER_RU.md) (A17) was not touched; its own pass is [SIGNOFF_A17_author_pass.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/SIGNOFF_A17_author_pass.md).
**Scope discipline:** voice, register and framing only; no number, claim or citation altered; mechanical drift gate ([voice_drift_check.py](https://github.com/gasyoun/Uprava/blob/main/tools/voice_drift_check.py) against `origin/master`) CLEAN — numbers 688 = 688, URLs 65 = 65, IAST 9 = 9, headings 30 = 30, table rows 61 = 61. The one line excluded from the gate is the added author byline (its ORCID URL and the IAST name are the only new tokens in the diff).

**Instruction:** read this file (~30 minutes together with a spot-check of the places below), veto any voice call you dislike (each reverts with one edit), and rule on the substance flags in §2 — only after that should readiness be confirmed at 5/5.

---

## 1. Voice calls made — each may be vetoed

Full diff: the commit of this pass on branch `voice-pass/A16`.

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | Header | `Last updated` bumped to 06-09-2026; author byline added under the H1 (`Mārcis Gasūns, independent scholar (ORCID …), gasyoun@ya.ru`) | The manuscript carried no byline at all; brief-mandated block |
| 2 | §4, kernel paragraph | "These six **make MW MW** in its *digital* form." → "These six give MW its recognisable shape in its *digital* form." | Colloquial flourish; same fix the RU twin took ("делают MW самим собой" → "определяют узнаваемый облик MW") — **reverted after adversarial verify:** author's figure, not a colloquialism |
| 3 | §4, same paragraph | Dropped the sentence "The print MW1899's kernel is one block smaller." | Third restatement of print = 5 / digital = 6 inside one paragraph; the two neighbouring sentences already say it — **reverted after adversarial verify:** substance — deleted a sentence of the author's argument |
| 4 | §4, *block-economy the constraint* bullet | "Print space is finite; setting cost is real; the user must be able to scan." → "Print space is finite, typesetting is expensive, and the user must be able to scan the page." | Staccato semicolon triplet with a colloquial "cost is real"; RU twin precedent ("набор стоит реальных денег" → "типографский набор дорог") |
| 5 | §4, last paragraph | "Importantly, the cross-dict audit … shows the *morphology* is …" → "The cross-dict audit … shows, however, that the *morphology* is …" | Empty opener from the de-AI list; "however" carries the actual contrast |
| 6 | §5.3, lex-hedged profile | "the property piggy-backs on the type" → "the property attaches to the type" | Register — **reverted after adversarial verify:** author's idiom |
| 7 | §5.4, closing paragraph | "see what's distinctive" → "see what is distinctive" | Contraction in journal prose |
| 8 | §7.2 (i), last sentence | "Four routes, one structural fact about the morphology;" → "Four routes lead to one structural fact about the morphology;" | Verbless telegram fragment — **reverted after adversarial verify:** author's rhetorical shape |
| 9 | §7.2 (ii), bold lead sentence | "… *tagged implementation* (1899), Cappeller is first …" → "… (1899); Cappeller is first …" | Comma splice between two independent clauses |
| 10 | §7.3, Atkins-Rundell bullet | "cannot place it in a landscape without borrowing A&R's apparatus" → "cannot place it among other dictionary types without borrowing A&R's apparatus" | "landscape" is on the de-AI list; the concrete referent is A&R's typology of purposes |
| 11 | §8, first bullet | "the highest-leverage editorial work" → "the highest-yield editorial work" | "leverage" is on the de-AI list |
| 12 | §8, second bullet | "A **first cut already exists**" → "A **first comparison already exists**" | Colloquial "first cut" — **reverted after adversarial verify:** author's idiom |
| 13 | §9.1 | "A separate discrepancy surfaced: … — corrected in §4." → "The §4 table's display-headword figure is the rendered-`<s>` rate (76%), not the structural-key rate (100%); §4 states the distinction." | Audit-trail voice ("surfaced", "corrected") describes draft history a journal reader never saw; the fact and both figures are kept (precedent: A16/H079 Major 8, lab journal → journal voice) — **reverted after adversarial verify:** substance+meaning — 'surfaced'/'corrected' record a real correction; neutral rewrite changes the claim |
| 14 | §9.3 | "…**not MW-specific**, exactly as feared — so the claim is softened to …" → "…**not MW-specific**, as this limit anticipated, and the claim is accordingly softened to …" | "as feared" is lab-journal affect; the hedging strength ("softened to") is unchanged — **reverted after adversarial verify:** meaning — 'exactly as feared' is the author's stance, not affect |
| 15 | §9.3 | "Two nuances survive:" → "Two qualifications survive:" | "nuance" is on the de-AI list — **reverted after adversarial verify:** meaning — 'nuances' is the author's word here |
| 16 | §9.4 | "Wilson 1832's preface was not OCR-fetched in this pass;" → "Wilson 1832's preface was not OCR-fetched;" | "in this pass" is working-notes chronology; the statement of what was not done is intact — **reverted after adversarial verify:** meaning — 'in this pass' scopes the negative claim |
| 17 | §10, second paragraph | "positions MW in a broader lexicographic landscape" → "situates MW within the broader field of lexicography" | "landscape" (de-AI list) |
| 18 | Appendix B.2 | "Visually compact in print, fully indexed for digital retrieval — a remarkable forward-compatibility, perhaps not by design." → "The result is visually compact in print and fully indexed for digital retrieval — a forward-compatibility that was perhaps not by design." | Verbless fragment plus the filler intensifier "remarkable" — **reverted after adversarial verify:** voice — author's aphoristic figure |
| 19 | Appendix B.3 | "Defective by A&R's standards (user-burden too high) but a *practical* choice — example provision would have made MW unprintable as one volume." → "This is defective by A&R's standards (the user-burden is too high) but a *practical* choice: example provision would have made MW unprintable as one volume." | Verbless fragment; em-dash-as-copula replaced by a colon — **reverted after adversarial verify:** voice — author's aphoristic figure |

Not done, deliberately (human rulings, see §3): the editorial "we" was left as is throughout (single-author paper; IJL accepts "I"); the heavy bold in running text was left as is ("format-robust" in §8/§9 is a technical term and was likewise kept).

## 2. Substance flags carried (not fixed)

1. **Compound share is stated two ways.** Appendix B.1 says "**50.4% are compounds** (`<e>3*`)", while the §5.1 table gives compound sub-entries as 126,360 = 44.10% (`<e>3*` plus em-dash/hyphen in `<k2>`) and §5.3 says "Compounds are 44% of MW's entries". If 50.4% is the raw `<e>3*` count and 44.10% the stricter definition, one clause saying so is needed; otherwise one of the two figures is stale.
2. **The hedge lineage contradicts itself between §7.2 (ii) and §9.4.** §7.2 (ii) (and the Appendix C.2 table) now says MW 1872 was **first with the concept** (preface declaration, D21 resolution). §9.4 still argues that "the *concept* of an inline lexicographer-only hedge **predates MW by at least 8 years (Cappeller)** and the *type* of intervention by 33 years (Benfey)" and that the innovation claim is "downgraded". Both cannot stand: §9.4 was written before the MW 1872 preface read and needs one sentence reconciling it with the three-stage lineage (concept 1872 MW → systematic typographic 1891 Cappeller → tagged 1899 MW).
3. **Word count in the header note.** The header says "~7.4K words, within IJL's ~8–10K window"; `wc -w` on the whole file gives 9,181 (header, appendices, references and footer included). Recount the body before submission and fix whichever figure is wrong.
4. **40,212 — entries or tags?** §5.2 calls it "40,212 distinct entries", §7.2 (ii) and the C.2 table "40,212 instances", §9.4 "appears 40,212×". If one entry can carry more than one `<ls>L.</ls>`, these are different counts; one wording throughout.
5. **§9.4 ends with a project-internal directive** ("The asterisk-meaning question for CAE's digitisation is itself a csl-orig issue — the digitisers should add the convention to CAE's `DATA_DICTIONARY.md`"). A journal reader cannot act on it; a footnote or removal is a substance call.
6. **Working-notes apparatus still in the journal text.** DOUBTS D5 / D7 / D18 / D19 / D20 are cited as if the reader had the file; the §5.1 table row 9 carries "(added 2026-05-27, per DOUBTS D18 audit)" inside a table cell; Appendix A.4 confesses that "an unverified earlier draft of this paper cited 'Reichmann 1999'"; the References section carries an HTML comment recording that removal. All are draft-history, not findings; untouched here because they sit in table cells, citations and references. A submission copy should drop or footnote them.
7. **Relative links.** `[`analysis/`](analysis/)`, `DOUBTS.md#…`, `MICROANALYSIS.md#…` are repo-relative and resolve only on GitHub; a submitted PDF or a copy outside the repo loses them. Untouched (URL rule).
8. **Eight vs nine dictionaries.** §9.3 and the first half of the §8 cross-dictionary bullet speak of "all eight CDSL dictionaries" (CROSS_DICT audit), the abstract and Figures 5–6 of nine (CROSS_DICT_PROFILES). Internally consistent, but a reviewer will ask; one clause naming which audit covers which set would close it.
9. **§7.2 (ii) "All four frameworks agree the convention is specific to MW in the CDSL corpus (40,212 instances vs 0 in … and 1 in AP)".** A count is not something frameworks agree on; and "specific to MW" sits next to "1 in AP". Minor phrasing-of-claim question, left alone because it touches the comparison.

## 3. Read-and-sign

1. ~30 minutes: read §1 above against the diff and veto by reverting single rows; rule on §2 items 1 and 2 first (they are the only ones that touch a stated finding).
2. Two voice rulings a human should decide, not made here: (a) editorial "we" → "I" throughout (IJL permits first-person singular for a single author; roughly forty occurrences, one mechanical pass); (b) strip bold from running text before submission (IJL copy-editing will do it anyway; doing it in the source keeps the RU twin and the EN in step).
3. Proposed readiness after the two §2 findings are reconciled: 5/5 (propose only — a human confirms). Venue: IJL stands; no change recommended.
4. Submission is frozen until 2026-11-01; nothing here is a submission step.

_Dr. Mārcis Gasūns_
