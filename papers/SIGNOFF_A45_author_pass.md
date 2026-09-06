# SIGNOFF — A45 author-voice pass

_Created: 10-07-2026 · Last updated: 06-09-2026_

Read-and-sign record for the author-voice pass over
[`A45_botanical_crosswalk_paper.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/A45_botanical_crosswalk_paper.md),
run under handoff
[H048](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H048-Fable_SanskritLexicography_botanical_crosswalk_26.06.26.md)
by Fable 5 (`claude-fable-5`) on 10-07-2026. Pass scope was **voice, register, and framing**; no
number, claim, or citation was altered. Budget the read at ~30 minutes: the manuscript does not
need a full reread, only the calls below.

## 0. Substance was re-verified before the voice pass

`/paper-referee` had never been run on A45, so every headline figure was re-counted from the
committed artifacts before any prose was touched. All reproduce exactly:

| figure | paper | recount | source |
|---|--:|--:|---|
| `<bot>` occurrences | 8,923 | 8,923 | [`mw_botanical_glossary.csv`](https://github.com/sanskrit-lexicon/MWS/blob/master/botanical_glossary/mw_botanical_glossary.csv) |
| distinct headwords | 7,063 | 7,063 | same |
| canonical species | 1,223 | 1,223 | same |
| lexicographer-only (occ / hw) | 6,064 / 5,054 | 6,064 / 5,054 | same |
| DCS-attested (occ / hw) | 6,341 / 4,679 | 6,341 / 4,679 | same |
| band split (hapax…very-common) | 1,525 / 2,221 / 1,648 / 753 / 194 | identical | same |
| species / synonym entries | 1,223 / 8,859 | 1,223 / 8,859 | [`species_to_sanskrit.json`](https://github.com/sanskrit-lexicon/MWS/blob/master/botanical_glossary/species_to_sanskrit.json) |
| ring distribution (473 / 302 / 176 / 125 / 147) | — | identical, median 2 | same |
| botanical-only headwords | 4,148 | 4,148 | [`homograph_control_headwords.csv`](https://github.com/sanskrit-lexicon/MWS/blob/master/botanical_glossary/homograph_control_headwords.csv) |
| clean confirmations | 1,567 | 1,567 | same |
| naive lex-only ∩ DCS | 3,348 | 3,348 | same |
| species-rank matches | 726 | 726 | [`species_currency.csv`](https://github.com/sanskrit-lexicon/MWS/blob/master/botanical_glossary/species_currency.csv) |
| accepted / synonym / doubtful | 377 / 346 / 3 | 377 / 346 / 3 | same |
| all-rank accepted share | 68.2% (1,216) | 68.2% (829 of 1,216) | same |

**The §4.5 claim that the naive join's high-frequency hits are homograph collisions is confirmed**,
and is now stated with its measured strength (see call 4): among the 3,348 naive hits,
homograph-bearing headwords are 18.4% of *hapax*, 51.8% of *rare*, **90.9% of *uncommon*, 99.4% of
*common*, and 100% (84/84) of *very-common***.

## 1. Voice calls made — each may be vetoed

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | front matter | `status`/`readiness` 2/5 → 3/5 | Metadata had drifted; body callout already said 3/5. |
| 2 | Abstract | Added one sentence carrying the GBIF result (346 of 726 superseded) | The abstract omitted a headline finding the paper reports in §4.6. Numbers are §4.6's own, unchanged. **Veto if you want the abstract kept to the crosswalk + kośa result alone.** |
| 3 | Abstract | "a substantial share — 1,567 — is nonetheless DCS-attested" → "of which 1,567 are DCS-attested" | A vague quantifier sitting next to an exact count. Anti-salami boundary preserved: the sentence still does not lead with 1,567 or read it as a gradient. |
| 4 | §4.5 | "the high-band hits are dominated by homograph collisions" → the measured per-band percentages | The claim was true but unquantified; the percentages come from the committed audit CSV. **This adds figures to the prose** — the closest this pass comes to substance. Veto if you prefer the qualitative sentence. |
| 5 | §4.6 | "The most-represented families are Fabaceae (142)…" → "**Across all 1,223 resolved names**, the most-represented families…" | The counts are correct but computed over *all* resolved names, while the paragraph had just argued the species-rank subset is the defensible denominator. A referee would read them as species-rank (where Fabaceae is 103, not 142). Denominator now stated; no number moved. |
| 6 | §6 Limitations | Rewrote the "4,148 / 1,567 to be regenerated before submission" bullet | **This bullet was stale and false.** The audit CSV exists and both figures reproduce from it. Replaced with the live limitation: the `botanical_only` flag inherits MW's own sense segmentation. |
| 7 | §3.3, §"Data and reproducibility" | Removed two inline `*(TODO: …)*` parentheticals from body prose | Both gates were already itemised in the draft-status callout; a manuscript body should not carry TODOs. Nothing was dropped — the DCS-2021-vs-2026 decision and the DOI/SHA256/source-pin gates are restated in the callout and in §2 below. |
| 8 | §§1, 4.2, 4.6, 5, 7 | De-editorialised: dropped "and it is striking", "This is exactly why", "a great historical/nineteenth-century…", duplicate "exactly"; "reusable bridge" (§5) / "durable bridge" (§7) de-duplicated | Filler intensifiers and grand epithets read as LLM register, not the author's. |
| 9 | §7 Conclusion | Added a clause on the GBIF layer, so the conclusion covers both joined layers | The conclusion mentioned the DCS join but not the currency pass, which is now a headline result. |

## 2. Standing gates — unchanged, still yours

These are the `[@DO]` items from H048; the author pass does not touch them.

- **Byline + ORCID.** Front matter currently reads `Mārcis Gasūns, independent scholar (ORCID
  0000-0003-4513-884X), gasyoun@ya.ru`. Confirm, and lock the sole-author form.
- **A38 citation + attestation base.** Cite A38 once its DCS-2026 release DOI is minted, and rule
  DCS-2021 (83,239 lemmas, current basis) vs DCS-2026 (98,606). Band labels would not change;
  coverage would rise. A38 is at 4/5 with the Hellwig CC-BY sign-off obtained — it should publish
  first.
- **Venue.** Lexikos vs Biodiversity Data Journal vs JOHD. Now materially easier: the GBIF currency
  pass is done, so BDJ's expectation of current nomenclature is met by the `accepted_name` layer
  while the paper still frames itself as a historical-lexicographic crosswalk.
- **Dataset DOI + per-file SHA256 + pinned `mw.txt` commit** in §"Data and reproducibility".
- **Two external nomenclatural sign-offs** gate *publication*, not this pass.

## 3. Not done here (referee lane)

- No sense-level attestation exists; the homograph control mitigates, does not eliminate. Stated in
  §6, not litigated.
- Optional strengthening the author may request: promote the per-band homograph table (call 4) to a
  real table in §4.5 rather than an inline sentence.

## Proposed readiness

**3/5 → 4/5 on your sign-off** (not 5/5: the dataset DOI, the A38 citation, and the venue choice are
still open, and 5/5 means ready-to-send). Bump via `/articles-update` once signed.

## Pass 2 — 06-09-2026 (Fable 5.1 `claude-fable-5-1`)

Second author-voice pass over
[`A45_botanical_crosswalk_paper.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/A45_botanical_crosswalk_paper.md), run under
[H3857](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3857-Fable_Uprava_all-articles-author-voice-pass-workflow_01.09.26.md) by Fable 5.1 (`claude-fable-5-1`) on 06-09-2026. Scope: **voice, register and framing
only; no number, claim or citation altered; mechanical drift gate CLEAN** (numbers 187/187, URLs
19/19, IAST tokens 30/30, headings 21/21, table rows 31/31 against `origin/master`). The pass-1
calls above are all in the text and were not revisited. Kept deliberately light: the
[ARTICLES.md](https://github.com/gasyoun/Uprava/blob/main/ARTICLES.md) pool row records that A45 did not make the PLUS5 five and that the heavy
author pass is not to be spent on it, so this pass removes register defects and nothing more.

### 1. Voice calls made — each may be vetoed

| # | Location | Call | Rationale |
|---|---|---|---|
| 1 | Header + front matter | `Last updated` bumped to 06-09-2026; `status:` line gains "author-voice pass 06-09-2026" with a link to this signoff | Brief-mandated header note; no other note added |
| 2 | §1, second paragraph | "Botanical vocabulary sits squarely at this fault line: the plant world is exactly where a synonym lexicon is richest" → "sits at this fault line: the plant world is where a synonym lexicon is richest" | Two filler intensifiers in one sentence; "fault line" itself kept as the author's figure |
| 3 | §2, first paragraph | "This is precisely the material Monier-Williams marked "L."" → "This is the material Monier-Williams marked "L."" | Filler intensifier; the identification is no weaker without it |
| 4 | §3.4 | "Lemma attestation therefore does **not** confirm" → bold removed from "not" | Decorative bold in running prose; the sentence carries the negation |
| 5 | §4.5, first sentence | "The contamination concentrates in the upper frequency bands, exactly as the *kṛṣṇa/indra/kāla* problem of §3.4 predicts" → "…, as the … problem of §3.4 predicts" | Third "exactly/precisely" in the paper; pass 1 already removed a duplicate |
| 6 | §4.5 | "with no homograph escape hatch" → "with no non-plant homograph to supply the corpus frequency" | Decorative metaphor replaced by the paper's own §3.4 wording of the same condition; no new claim |
| 7 | §5, first paragraph | "and does so worst precisely where the frequencies are largest" → "and does so worst where the frequencies are largest" | Filler intensifier |
| 8 | §5, second paragraph | "would erase what MW wrote and bake in a 2020s taxonomy" → "would erase what MW wrote and fix in place a 2020s taxonomy" | "bake in" is engineering slang, not journal register |

Reverted, not shipped: §4.2's closing clause "— the channel where a nighaṇṭu is richest and a
running text thinnest" repeats §1's figure verbatim; dropping it removed an IAST token and
tripped the drift gate, so the sentence stands and the repetition is listed as flag 7 below.

Not done, deliberately (human rulings, see §3, same stance as the A16 pass-2 signoff): the
editorial "we" was left throughout (sole-author paper; Lexikos, BDJ and JOHD all accept "I"),
and the bold on numbers and phrases in the Abstract and in §4 was left as house style.

### 2. Substance flags carried (not fixed)

1. **§4.6 rank breakdown does not sum to 1,223.** 726 species-rank + 272 genus + 51 family + 164
   kingdom-only = 1,213; ten resolved names are unaccounted for (order- or class-rank matches?).
   One clause naming the missing rank, or corrected counts, before submission.
2. **§4.6 family counts use a denominator the paragraph has just disowned.** "Across all 1,223
   resolved names, the most-represented families are Fabaceae (142)…" sits one sentence after
   "the species-rank split is the defensible one", and the 1,223 includes the 164 names GBIF placed
   only at kingdom Plantae, which carry no family. Pass 1 (call 5) named the denominator; whether
   it is the right denominator is a substance call. The same paragraph also says "all 1,216
   resolved names" for the accepted/synonym share, so "resolved" means two different sets within
   five lines.
3. **No reference list.** §2 names Roxburgh, Kirtikar & Basu, Nadkarni, FRLHT/ENVIS, CDSL, GBIF,
   POWO, IPNI and Hellwig's DCS, and the paper cites "A18/P3" and "A38" as companion work, but
   there is no References section and no bibliographic entry for any of them. Untouched (citation
   rule); a submission copy needs the list and a citable form for A18 and A38.
4. **Relative links** `[../botanical_glossary/](../botanical_glossary/)` and
   `[dcs_lemma_summary.json](../../VisualDCS/dcs_lemma_summary.json)` (§3.3, §"Data and
   reproducibility") resolve only inside the GitHub tree; a PDF loses them. Untouched (URL rule).
5. **Pool status vs this pass.** The [ARTICLES.md](https://github.com/gasyoun/Uprava/blob/main/ARTICLES.md) row for A45 ("НЕ ВОШЛА В ПЯТЁРКУ
   29-07-2026") says the heavy author pass is not to be spent on this paper; H3857 nevertheless
   scheduled it. This pass was kept to register fixes; a human should confirm no further voice work
   is wanted on A45 before the PLUS5 five are through.
6. **Closing byline.** The manuscript ends with the hub convention `_Dr. Mārcis Gasūns_` while the
   front-matter byline (correctly) carries no title; the closer must be stripped from any
   submission copy.
7. **§4.2 repeats §1 verbatim** ("the channel where a nighaṇṭu is richest and a running text
   thinnest"). Left in place (see the reverted hunk above); a one-word variation is the author's
   call.
8. **Standing gates unchanged** from pass 1 §2: A38 DOI + DCS-2021 vs DCS-2026 base, dataset DOI +
   SHA256s + pinned `mw.txt` commit, venue choice, two external nomenclatural sign-offs.

### 3. Read-and-sign

1. ~30 minutes: read §1 above against the diff (eight one-line calls, veto by reverting a row),
   then rule on flags 1 and 2 — they are the only ones that touch a stated result.
2. Two voice rulings a human should decide: (a) editorial "we" → "I" throughout (roughly twenty
   occurrences, one mechanical pass; all three candidate venues permit it); (b) strip the bold from
   the Abstract before submission.
3. Proposed readiness after flags 1–3 are closed: 4/5 (propose only — a human confirms; 5/5 still
   needs the dataset DOI, the A38 citation and the venue). Venue: the pass-1 note stands — the
   GBIF `accepted_name` layer makes Biodiversity Data Journal viable while the framing stays
   historical-lexicographic; no change recommended here.
4. Submission is frozen until 2026-11-01; nothing here is a submission step.

_Dr. Mārcis Gasūns_
