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

## Result — stable across two corpus snapshots

| Corpus | Attested | % of 18,930 | Strong tier (band ≥2) |
|---|--:|--:|--:|
| DCS-2021 (lemma summary, SLP1) | 5,723 | 30.2% | ~2,232 |
| **DCS-2026** (full token corpus, 5.69M tokens) | **5,935** | **31.4%** | **2,330** |

The headline barely moves (30.2% → 31.4%) across two DCS snapshots — so the finding
is not a corpus-version artefact. (These are two versions of the *same* corpus
project, one annotator, so this controls for version, not for DCS's lemmatisation
conventions — supporting, not proving, the P3 claim.)
Net +212 refutations from the corpus refresh (+223 gross, −11 lemmatization drift).
The 2026 join transcodes DCS IAST → SLP1 (validated: only 11/5,723 of the 2021 hits
drop out, all plain-ASCII so not a transcode failure).

Strongest tier = bands 2–3 (rare/uncommon), mostly plant/medical/technical terms
MW had only from kośas, now corpus-attested: `SAlaparRī` (Desmodium, 14×), `BfNgaja`
(Agallochum, 10×), `AvAri` ("a shop", 18×), `ISAnī` (silk-cotton tree, 21×). See
[SUMMARY.md](SUMMARY.md) / [SUMMARY_2026.md](SUMMARY_2026.md) for bands and caveats
(band-1 hapax = weak; top-band short strings = homograph collisions).

## Files

| File | What |
|---|---|
| [`ls_L_dcs_pilot.py`](ls_L_dcs_pilot.py) | the DCS-2021 analysis (re-run: `python ls_L_dcs_pilot.py`) |
| [`ls_L_dcs2026.py`](ls_L_dcs2026.py) | DCS-2026 re-join with IAST→SLP1 transcoder (`python ls_L_dcs2026.py`) |
| `purely_lexicographic_attested.csv` / `_2026.csv` | retire-candidates: lemma, L-sense count, DCS band/tokens, gloss |
| `purely_lexicographic_unattested.csv` | hedge stands (corpus-absent, 2021) |
| [`SUMMARY.md`](SUMMARY.md) / [`SUMMARY_2026.md`](SUMMARY_2026.md) | headline numbers, bands, interpretation, caveats |

## Next (sense-level, not yet done)

Both runs are lemma-level (*lemma-now*) and agree at ~31%. Verifying the specific
hedged **sense** (*sense-next*) needs sense-tagged corpus data — and the 10,264
*partially*-hedged lemmas (excluded here) need exactly that, since their lemma is
already text-attested in other senses. A hand-verified band-3 subset (~180 lemmas)
would be the publication-ready core for P3.
