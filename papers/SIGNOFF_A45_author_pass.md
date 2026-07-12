# SIGNOFF — A45 author-voice pass

_Created: 10-07-2026 · Last updated: 10-07-2026_

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

_Dr. Mārcis Gasūns_
