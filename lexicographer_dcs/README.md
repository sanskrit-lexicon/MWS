# `<ls>L.</ls>` → DCS corpus verification

MW marks **40,212** senses `<ls>L.</ls>` = *"lexicographers only"* — attested
only in indigenous kośas/nighaṇṭus, with no text witness Monier-Williams knew of.
Modern corpora (Oliver Hellwig's [DCS](http://www.sanskrit-linguistics.org/dcs/))
can now attest some of these words. This pilot quantifies how many.

It is the first concrete step of the roadmap's `<ls>L.</ls>` verification track
(ROADMAP.md §W1 / deferred crowd item) and feeds **paper P3** (citation registers)
and the **grammar-corpus-dict crosswalk**.

## Method

Lemma-level join, no transcoding (MW `<k1>` and DCS lemmas are both SLP1):

1. Group MW records by headword `<k1>`; tally `L.` vs non-`L.` `<ls>` and uncited glosses.
2. **Strict purely-lexicographic lemma** = every `<ls>` is `L.`, *and* no uncited
   gloss or cross-ref stub. (The strict filter matters — see the method note in
   [SUMMARY.md](SUMMARY.md); a coarse test misclassifies common words like
   `anta`/`anila` that leave their main sense uncited.)
3. Look each up in [`dcs_lemma_summary.json`](../../VisualDCS/dcs_lemma_summary.json)
   (DCS-2021, 83,273 lemmas, frequency-banded).

For a strict purely-lexicographic lemma, **any** corpus attestation is a clean
refutation: MW cited no text, yet the word occurs.

## Result (DCS-2021)

**5,723 of 18,930 (30.2%)** strict purely-lexicographic MW lemmas are attested in DCS.
Strongest tier = bands 2–3 (rare/uncommon): ~2,232 lemmas, mostly plant/medical/
technical terms now corpus-attested. See [SUMMARY.md](SUMMARY.md) for bands and caveats
(band-1 hapax = weak; top-band short strings = homograph collisions).

## Files

| File | What |
|---|---|
| [`ls_L_dcs_pilot.py`](ls_L_dcs_pilot.py) | the analysis (re-run: `python ls_L_dcs_pilot.py`) |
| `purely_lexicographic_attested.csv` | retire-candidates: lemma, L-sense count, DCS band, gloss |
| `purely_lexicographic_unattested.csv` | hedge stands (corpus-absent) |
| [`SUMMARY.md`](SUMMARY.md) | headline numbers, bands, interpretation, caveats |

## Next (sense-level, not yet done)

This is lemma-level (*lemma-now*). Verifying the specific hedged **sense**
(*sense-next*) needs sense-tagged corpus data. Re-running against the newer
**DCS-2026** snapshot ([`VisualDCS/src/DCS-data-2026/`](../../VisualDCS/src/DCS-data-2026/))
would raise coverage. The 10,264 *partially*-hedged lemmas are deliberately
excluded here — they need sense-level evidence.
