# Submission-readiness report — A16

**Paper:** *The microstructure of Monier-Williams 1899: a data-grounded framework, triangulated against three metalexicographic traditions*
**Repo / venue:** MWS → *International Journal of Lexicography* (OUP, ScholarOne portal)
**Byline (locked):** M. Gasūns, sole author (ORCID to confirm)
**Readiness:** 4/5
**Date:** 2026-06-26
**Canonical manuscript:** [`PAPER.md`](PAPER.md) on branch `master`, commit `03c72b2`.

This report is the Month-1 writing-pass companion to the new cover letter [`cover_letter_A16.md`](cover_letter_A16.md). It is additive: it does **not** modify [`PAPER.md`](PAPER.md). Every proposed body edit below is a precise instruction for the author to apply, not applied here.

---

## What is done

- **Manuscript is draft-complete and internally coherent.** [`PAPER.md`](PAPER.md) (read in full) carries Abstract + §§1–10 + Appendices A (Wiegand) / B (Atkins–Rundell) / C (Hausmann) + 18 selected references. Raw file ~9,167 words; the paper self-reports a ~7.4K-word prose body, inside IJL's 8–10K window.
- **The argument has survived a hostile-review pass** (DOUBTS D16–D22). The one formerly *blocking* doubt, D21 (the Cappeller-precedent narrative), is resolved into the three-stage `<ls>L.</ls>` lineage now in §7.2(ii) and Appendix C.2. Do not re-open it.
- **Five of six §9 limitations are audited** with reproducible scripts in [`analysis/`](analysis/): SPOTCHECK, SIGNIFICANCE / SIGNIFICANCE_FULL, LS_HEDGE_CHECK, CROSS_DICT, CROSS_DICT_PROFILES.
- **Corrected cover letter written** → [`cover_letter_A16.md`](cover_letter_A16.md). It fixes the two locked items: sole-author M. Gasūns (CDSL-collaboration credit removed; voice switched to "I"), and all branch URLs re-pointed from the stale `docs-pass` to canonical `master`.
- **The empty gold harness exists and is sound.** On `feat/p1-gold-standard` (commit `d0270a4`): `GOLD_STANDARD.md`, `GOLD_SAMPLE.json` (200 stratified entries, seed 2026), `gold_sample.py`, `gold_score.py`. The scoring instrument is built and `--selftest`-able.

---

## Branch situation (precise)

Three live branches carry pieces of this paper; they have drifted since the 2026-05-27 cover letter was written. Confirmed from the repo today:

| Branch | Role | State |
|---|---|---|
| `master` (`03c72b2`) | **Canonical current paper.** Holds the newest [`PAPER.md`](PAPER.md) and the audit suite. | 59 commits **ahead** of `docs-pass`, 2 behind. This is the submission line. |
| `feat/p1-gold-standard` (`d0270a4`) | The **200-entry gold harness** for detector validation. | **EMPTY: `GOLD_STANDARD_SCORES.md` reads "Annotated: 0 (both annotators: 0)"; every per-block precision/recall/F1/κ cell is `—`.** Harness only — no human annotation yet. |
| `docs-pass` (`bada3cb`) | **Stale.** The branch the old cover letter and the R2 handoff link at. | 59 commits behind `master`. Must not be the submission line; the gold files do **not** live here either. |

Net effect: the canonical text is on `master`, the validation instrument is on `feat/p1-gold-standard` and is unfilled, and `docs-pass` is obsolete. The old letter [`IJL_COVER_LETTER.md`](IJL_COVER_LETTER.md) (commit `5c5e4c4`) points reviewers at `docs-pass` — that is why the new [`cover_letter_A16.md`](cover_letter_A16.md) re-points everything to `master`.

> **Do NOT perform any git branch merge in this pass — it is flagged, not executed.** Folding `feat/p1-gold-standard` into `master` (to bring the gold files alongside the current paper) and deciding the fate of `docs-pass` is a separate, deliberate reconciliation step. It is also gated on the human annotation below: merging the harness while it is still all-`—` would land an empty instrument onto the submission line.

---

## Proofread / house-style findings

Concrete, with line references into [`PAPER.md`](PAPER.md) as read (commit `03c72b2`).

1. **No author byline or affiliation block anywhere in [`PAPER.md`](PAPER.md).** The file goes title (L1) → framing paragraphs (L3–L5) → Abstract (L9). There is no author line, affiliation, ORCID, or corresponding-author email. IJL/ScholarOne collects author metadata in the portal, but the manuscript itself should carry a byline for the de-anonymised/accepted version. (Author gate — see below.)
2. **Collaborative "we"/"our" used 35× throughout the prose** (e.g. abstract L11 "We then **triangulate**"; L21 "we build", "we make"; §2 L25 "Our data"). For a sole-author paper this is the conventional scholarly "we" and is acceptable in IJL — but it must be a **deliberate** choice, reconciled against the locked sole-author record, not a residue of the former CDSL-collaboration framing. See the proposed edit below.
3. **Stale `docs-pass` build-artefact link in §2 (L27):** "The block-detection source is in the [docs-pass build artefacts](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass)." This points at the obsolete branch. It should resolve to wherever the detector source lands on the canonical branch after reconciliation.
4. **§9 limitations #1 and #6 still cite only the random 100-record sample** (L236, L241: `analysis/SPOTCHECK_SAMPLE.txt`, seed 42) and carry the explicit "±2–4 pts" hedge and "per-entry Sanskritist review of that sample is the remaining step." They do **not** yet cite the stratified 200-entry gold or any measured precision/recall/κ — because those numbers do not exist yet (harness empty). This is the single substantive prose gap to 5/5, not a typo.
5. **Cited cell-count drift between paper and old cover letter.** [`PAPER.md`](PAPER.md) §9.2 (L237) reports "**200 of 225** block × type cells … under Benjamini–Hochberg (q = 0.05)"; the old [`IJL_COVER_LETTER.md`](IJL_COVER_LETTER.md) §3 says "**217/270**". These disagree. Confirm which figure is current from [`analysis/SIGNIFICANCE_FULL.md`](analysis/SIGNIFICANCE_FULL.md) and make the letter match the paper. (The new [`cover_letter_A16.md`](cover_letter_A16.md) deliberately omits the raw cell counts to avoid carrying a stale number forward; add the verified figure when the audit paragraph is restored.)
6. **Word-count statements to reconcile at submission.** Title block L3 says "~7.4K words"; abstract-adjacent prose and the old letter say "~7,700"; the raw file is 9,167 words (tables + appendices + refs included). Pick one prose-body figure and state it consistently in the manuscript and the ScholarOne word-count field. Not blocking, but IJL desk-checks length.
7. **Diacritics / encoding.** Author surname is consistently "Gasūns" (ū = U+016B) in the byline target; ś/ṣ/ṛ etc. appear throughout. Ensure the ScholarOne upload preserves UTF-8 (both new files are UTF-8, no BOM — verified). No mojibake found in the read.

---

## Remaining HUMAN GATES

These block 5/5 and cannot be done by an agent. Bracketed `@DO` items only.

- **[@DO] Approve the G5 200-entry gold spec and supply a second annotator.** The stratified packet ([`analysis/GOLD_STANDARD.md`](analysis/GOLD_STANDARD.md) on `feat/p1-gold-standard`) is designed for **two independent Sanskritist annotators** marking FP/FN per entry, with agreement *measured* as Cohen's κ. Both annotation sets are currently empty ("Annotated: 0"). The author must (a) sign off that the stratified-sample design is the instrument they want, and (b) serve as / recruit the two annotators. **This is the long pole to 5/5** — every downstream agent step (scoring, the §9 rewrite, the cover-letter audit paragraph) is unblocked only once the two annotation sets exist.
- **[@DO] Reconcile the byline between [`PAPER.md`](PAPER.md) prose and the sole-author record.** The locked decision is sole author M. Gasūns. The cover letter is already corrected; the author must confirm that the manuscript's editorial "we" stays (as conventional sole-author voice) and add the byline (proposed edit below). The former "on behalf of the CDSL collaboration" framing must not reappear at submission.
- **[@DO] Confirm ORCID for M. Gasūns** and add it to the byline + cover letter. No ORCID string appears anywhere in `papers/microanalysis/` today; both new files mark it "to be confirmed."
- **[@DO] Confirm the corresponding-author email.** The old letter signed `gasyoun@gmail.com`; the new letter marks it "to be confirmed" pending the author's choice of submission address.
- **[@DO] Final submission to IJL** via the OUP ScholarOne portal once the above land.

---

## Proposed manuscript edits

Exact, for the author to apply. **Not applied in this pass.**

### Edit 1 — add an author byline to [`PAPER.md`](PAPER.md) (authorship reconciliation)

There is currently no byline. Insert one line immediately after the title (current L1), before the "**Draft for the …**" paragraph:

```markdown
**Mārcis Gasūns** · sole author · ORCID: [TBC] · corresponding: [email TBC]
```

This makes the manuscript consistent with the locked sole-author A16 record. Do **not** add any "on behalf of the CDSL collaboration" line. The existing editorial "we" throughout the body may remain (conventional sole-author scholarly voice) — no global find-replace to "I" is needed in the manuscript, and changing it is not recommended.

### Edit 2 — un-stale the §2 detector-source link (current L27)

Replace:

```markdown
The block-detection source is in the [docs-pass build artefacts](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass).
```

with a link to the detector source on the canonical branch (e.g. `…/tree/master/papers/microanalysis/analysis/…`) once branch reconciliation places it there. This is the only `docs-pass` reference in the manuscript body.

### Edit 3 — §9 limitations #1 and #6: estimated → measured (the 4→5 prose change; apply ONLY after gold is annotated)

Current §9 #1 (L236) ends: *"per-entry Sanskritist review of that sample is the remaining step."* Current §9 #6 (L241) carries the *"±2–4 pts"* hedge and cites only the random 100-record sample (seed 42).

After the 200-entry gold is annotated and scored, rewrite both to cite the **stratified 200-entry gold** and quote the **measured** F08 precision, F09 precision, F11 recall, and inter-annotator Cohen's κ from `analysis/GOLD_STANDARD_SCORES.md`, replacing the "±2–4 pts" estimate. This is the substantive change that moves the paper from "limitations estimated" to "limitations measured." **Do not draft placeholder numbers** — the cells are all `—` today.

### Edit 4 — reconcile the FDR cell-count figure

§9.2 (L237) says "200 of 225 … cells"; the old letter said "217/270." Verify against [`analysis/SIGNIFICANCE_FULL.md`](analysis/SIGNIFICANCE_FULL.md) and make the manuscript and the cover letter's audit paragraph state the same numbers.

### Edit 5 — single word-count figure

Settle on one prose-body word count (title block L3 currently "~7.4K"; old letter "~7,700") and use it in both the manuscript and the ScholarOne length field.

---

## Verdict

**Current readiness: 4/5.** The manuscript is draft-complete, hostile-reviewed, internally cross-referenced, and the venue fit is strong; the corrected sole-author cover letter is written and re-pointed to `master`. What holds it at 4/5 is that the detector-validation instrument is **built but empty** — the 200-entry gold has zero annotations — so §9's two validation limitations still rest on an estimate rather than a measurement.

**What flips it to 5/5 (in order):**

1. **[@DO]** Author approves the G5 gold spec and a second Sanskritist annotator fills the 200 entries (the long pole).
2. **[agent]** Score the populated gold (`gold_score.py`), commit `GOLD_STANDARD_SCORES.md`.
3. **[agent]** Apply Proposed Edit 3 — rewrite §9 #1 and #6 with the measured P/R + κ.
4. **[agent]** Reconcile branches onto `master` (fold in the now-filled gold; retire `docs-pass`) — flagged here, not performed.
5. **[agent]** Restore the measured audit paragraph in [`cover_letter_A16.md`](cover_letter_A16.md) and apply Edits 1, 2, 4, 5.
6. **[@DO]** Confirm ORCID + corresponding email; **[@DO]** submit via OUP ScholarOne.

Items 2–5 are agent-doable and fast; the gate is item 1.
