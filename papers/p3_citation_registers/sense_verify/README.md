# A18 / P3 sense-level verification package (band-3 `L.` hand-verify prep)

_Created: 04-07-2026 · Last updated: 04-07-2026_

The lemma-level joins in [lexicographer_dcs/](https://github.com/sanskrit-lexicon/MWS/blob/master/lexicographer_dcs/README.md)
showed ~31% of the 18,930 strict purely-lexicographic (`<ls>L.</ls>`-only) MW
lemmas occur in DCS. That is *lemma-now* evidence only — [SYNTHESIS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/SYNTHESIS.md)
requires the homograph caveat: does the corpus attest **the hedged sense**?
This module is the *sense-next* step it defers: the machine-prepared sample and
verification sheet for the human (Sanskritist) band-3 pass. **The judging
itself stays a human gate** — nothing here decides sense identity.

## Design

- **Hedge stratum (60):** deterministic sample (seed `20260704`) of the 174
  band-3 (uncommon, 10–99 DCS-2026 tokens) strict purely-lexicographic lemmas —
  the "~180 publication-ready core" the lexicographer_dcs README names. Band 3
  because attestation there is neither hapax noise (band 1) nor
  homograph-prone high frequency (bands 4–5).
- **Control stratum (20):** single-entry MW lemmas whose only `<ls>` citations
  name a primary text (no `L. / W. / MW. / ib. / Cat.`), also DCS band 3
  (pool: 3,792). Text-cited senses should verify at a high rate; the control
  measures the method's ceiling, against which the hedge stratum's
  sense-attestation rate is read.
- Per item: full MW entry line(s) from csl-orig `mw.txt`, its `<ls>`
  citations, and ≤4 DCS-2026 occurrences (text, chapter ref, sandhied
  sentence, matched form highlighted) — enough to judge without opening
  other files.
- The two strata map onto P3's registers: the `L.` hedge is MW's pointer to
  the indigenous lexicographic register; the control is the European
  text-citation register at work.

## Files

| File | What |
|---|---|
| [build_sense_verify.py](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/sense_verify/build_sense_verify.py) | sampling + MW extraction + DCS alignment (`python build_sense_verify.py`) |
| [sense_verify_items.json](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/sense_verify/sense_verify_items.json) | the 80 items with full context |
| [sense_verify_sample.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/sense_verify/sense_verify_sample.csv) | flat summary table |
| [SAMPLE_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/sense_verify/SAMPLE_SUMMARY.md) | strata counts + method note (generated) |
| [make_review_sheet.py](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/sense_verify/make_review_sheet.py) | regenerates `review/A18_sense_verify_sheet.html` (gitignored personal artifact) |
| [apply_decisions.py](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/sense_verify/apply_decisions.py) | consumes `review/decisions.json` → `SENSE_VERIFY_RESULTS.md` (refuses partial passes) |

## Human loop

1. Open `review/A18_sense_verify_sheet.html` (regenerate any time:
   `python make_review_sheet.py`). Vote per item: ✅ sense attested ·
   ❌ homograph / other sense · ⏸ unsure. Keyboard: `a`/`r`/`d`, `j`/`k`.
2. Download `decisions.json` into `review/`.
3. `python apply_decisions.py` → `SENSE_VERIFY_RESULTS.md` with the two
   strata's sense-attestation rates — the P3 sense-level figure with its
   built-in ceiling.

## Data sources (consumed, not re-derived)

- [purely_lexicographic_attested_2026.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/lexicographer_dcs/purely_lexicographic_attested_2026.csv) — the strict L.-only DCS-attested pool
- `../../../../csl-orig/v02/mw/mw.txt` — MW source, sibling repo of MWS (read-only)
- `../../../../VisualDCS/src/DCS-data-2026/dcs_full.sqlite` — the DCS-2026 master, sibling repo (per [PROJECT_INTERLINKS](https://github.com/gasyoun/Uprava/blob/main/PROJECT_INTERLINKS.md): consume, don't re-parse CoNLL-U)
- IAST→SLP1 transcoder reused from [ls_L_dcs2026.py](https://github.com/sanskrit-lexicon/MWS/blob/master/lexicographer_dcs/ls_L_dcs2026.py)

Built 04-07-2026 by Fable 5 (`claude-fable-5`) per [H150](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H150-Fable_MWS_a18_citation_registers_corpus_prep_04.07.26.md).

_Dr. Mārcis Gasūns_
