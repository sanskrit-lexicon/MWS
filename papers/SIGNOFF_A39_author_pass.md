# SIGNOFF A39 — author-voice pass

_Created: 06-09-2026 · Last updated: 06-09-2026_

**Scope.** Manuscript: [papers/A39_verbal_roots_disagreement_paper.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/A39_verbal_roots_disagreement_paper.md) (*Grammar, Dictionary, Corpus: Where the Three Authorities Disagree about Sanskrit Verbal Roots*, readiness 3/5, ~7.4k words, no prior signoff and no referee memo). Handoff: [H3857 — all-articles author-voice pass workflow](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md). Pass by Fable 5.1 (`claude-fable-5-1`), 06-09-2026. Voice, register and framing only; no number, claim or citation altered; mechanical drift gate ([voice_drift_check.py](https://github.com/gasyoun/Uprava/blob/main/tools/voice_drift_check.py) against `origin/master`) CLEAN: numbers 483/483, URLs 65/65, IAST tokens 144/144, headings 20/20, table rows 16/16 count-identical before and after. The draft was already tight (every count carries its instrument, the intro question is the one §7 answers, title and abstract match the result); the pass found one systemic seam, the editorial "we" in a sole-author paper, plus a handful of single sentences. Every call below may be vetoed by reverting the hunk.

## 1. Voice calls made — each may be vetoed

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | Header + status blockquote | Both `Last updated` lines bumped to 06-09-2026; one line "Author-voice pass 06-09-2026 (link to this signoff)" added at the end of the draft-status paragraph | Brief's manuscript-header rule; nothing else in the status block touched. The note sits on its own line because the drift gate ignores any line carrying the phrase, and the YAML `status:` line holds the `3/5` figure |
| 2 | Abstract, §1, §2, §3.1, §3.3, §3.4, §4.3, §5, §5.5 (15 sites) | Editorial "we" → "I" wherever the author is the agent: "We quantify / show / release / state / exhibit / cite / treat / use / flag / do not present / resist / name", "better than we could" | Sole-author paper; the target venues (Lexikos, IIJ, WSC proceedings) all take the singular. Consistent with the batch's A04/A06 pass-1 calls. **Veto as a block if the plural is wanted back — it restores cleanly** |
| 3 | §1 (twice), §2, §7 (twice) | "our own pipeline" → "this project's own pipeline" (×3); "our attestation denominator" → "this paper's attestation denominator"; "our first measurement" → "the first measurement" | Kept the possessive off the first person on purpose: §5.1 already says "this project's own Phase-6 pipeline", and the WhitneyRoots pipeline is a project artifact, not a personal one. "my own pipeline" was the alternative; veto to either |
| 4 | §2, para 2 | "The framing that matters for this paper: that model *produces* the DCS lemma attribution…" → "What matters for this paper is that this model *produces* the DCS lemma attribution…" | Telegram colon with the verb dropped; same claim, now a sentence |
| 5 | §2, last para | "Finally, the source digitizations themselves: the machine-readable…" → "Finally, there are the source digitizations themselves: the machine-readable…" | Same defect — verbless topic label as a paragraph opener |
| 6 | §3.1, instrument note | "a gap we flag rather than hide, and return to in §7" → "a gap I flag here and return to in §7" | "rather than hide" is candour posturing; the flagging itself is the honesty |
| 7 | §3.3, instrument note | "Its blind spots: vidyut-prakriya generates…" → "It has blind spots of its own: vidyut-prakriya generates…" | Verbless colon opener; no count added ("two blind spots" was rejected because it would add a number) |
| 8 | §4.1, first para | "the striking figure is the smallness of the conflict rate" → "the figure that matters is the smallness of the conflict rate" | "striking" is a decorative intensifier from the de-AI list; "smallness" (the claim) is untouched |
| 9 | §4.1, cūṣ case | "Could the corpus decide? No — and the reasons are instructive." → "The corpus cannot decide, and the reasons are instructive." | One-word parcel after a rhetorical question; "cannot" carries the same strength as "No". The intro's "Why is disagreement the interesting object at all?" was left — it is the author's own move and the answer follows in full |
| 10 | §4.4, last sentence | "…a lexical-semantic task — the honest statement of where the morphological program ends." → "…a lexical-semantic task; that is where the morphological program ends." | Fake candour ("honest") plus em-dash-as-copula |
| 11 | §7, para 2 | "…a capture gap in the digitization. That is genuine value. A corpus run against a curated inventory is a powerful *detector*…" → "…a capture gap in the digitization. That detection is genuine value: a corpus run against a curated inventory is a powerful *detector*…" | Two-word parcel merged into the sentence it introduces; nothing else in the paragraph moved |

Left alone on purpose: the four-item "The contributions are: (1)…(4)" list in §1 (inline, numbered, each item carrying its § pointer — the singular contribution statement is the bolded sentence just above it); the bold on the headline figures in the abstract and §4 (this paper uses bold sparingly and only on measured results); the "not X, it is Y" shapes in the thesis sentence ("a homonym and variant detector, not a correction list") — that contrast *is* the finding, not rhetoric; the em-dashes that carry parentheticals in the case studies.

## 2. Substance flags carried (not fixed)

1. **Two different "13"s in §4.3.** The mismatch trajectory is 33 → 13 → 11 (all mismatches), and separately the panel examined "the historical set of 13 corpus-corroborated flags" of which 10 dissolved and 3 remain. Both 13s are real, but a referee will read them as the same number. One clause naming them as distinct sets would fix it; that is a claim edit, so it is flagged, not made.
2. **Abstract vs body on the panel denominator.** The abstract says "11 residual mismatches, 3 of them corpus-corroborated — and a three-verifier panel found that not one corpus-corroborated mismatch is an error"; the body says the panel ruled on the historical 13, of which 3 survive. The abstract sentence is true but reads as if the panel ruled on 3. Untouched.
3. **MW coverage stated at two magnitudes.** §3.1 links 569 of 930 spine roots to MW (WhitneyRoots build); §4.2 reports 809 of 935 hub roots attested in MW (MWS build). The canonical-build note explains the two builds, but nowhere does the text say why the same dictionary covers 569 in one and 809 in the other (anchor-decoding vs entry-linking, presumably). A referee will ask.
4. **`match_basis` sums to 360, not 327.** 317 + 33 + 8 + 2 = 360 and 347 + 10 + 3 = 360, while the match count is 327; the 33 `fill_candidate` rows appear to be included in the basis tallies. Consistent with the artifact, but worth one parenthetical.
5. **Hellwig 2020 LREC treebank mentioned in §2 with no reference entry.** Cited in prose ("e.g. the 2020 LREC release") but absent from the References list.
6. **Whitney 1879 first edition cited in §1; only the 1889 edition is in the References.**
7. **Row 7 of the claim table carries "of 139 audited"** — a figure that appears nowhere in the body text (§5.1 gives 117 / 120 only).
8. **"Zaliznyak-style" (§3.4 prose) vs "NEEDS ZALIZNIAK" (quoted queue verdict).** Two romanisations of the same name; the quoted string is a verbatim artifact and cannot be normalised in the paper without changing the citation.
9. **Claim-table rows 6 and 9 use "§3a / §3d / §3e"** meaning sections of `DECISIONS_NEEDED.md`, while the same notation elsewhere in the paper means paper sections. Easy to misread.
10. **Standing open items from the draft-status block remain open:** A04/A35/A38 self-citations and the A38 DOI; the §6 snapshot-freeze decision; the venue ruling; the References ellipsis in the Nehrdich et al. title (a reference entry, left verbatim).

## 3. Read-and-sign

Budget about 30 minutes: read the abstract, §1 and §7 for the first-person register (call 2, the only pass-wide change), then spot-check calls 4–11 in place; the diff is 32 lines added against 31 removed, plus this file.

- **Readiness:** propose 3/5 → **4/5** once flags 1–2 (the two 13s, the abstract's panel denominator) and 5–6 (the two missing reference entries) are settled; those are the items a referee would open with. Not 5/5 (the DOI/venue gates are still open).
- **Venue:** no change recommended. The existing ranking (WSC 2027 / Lexikos / IIJ, ISCLS only once mature) fits a sole-author, singular-voice paper of this length; the first-person register adopted here is at home in all three.

_Dr. Mārcis Gasūns_
