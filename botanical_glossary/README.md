# MW botanical glossary (issue #74)

A FAIR Sanskrit ↔ Linnaean botanical dataset extracted from MW's 8,923 `<bot>`
tags, with provenance and corpus attestation. Supersedes the frequency-only
[`botbio/mw_bot.txt`](../botbio/mw_bot.txt).

## Contents

| File | What |
|---|---|
| [`bot_glossary.py`](bot_glossary.py) | builds everything (`python bot_glossary.py`) |
| `mw_botanical_glossary.csv` | one row per `<bot>` occurrence: headword (SLP1+IAST), species (canonical + raw), L-number, page/col, sense citation, lexicographer-only flag, DCS band |
| `species_to_sanskrit.json` | canonical species → sorted Sanskrit synonym ring |
| [`BOTANICAL_SUMMARY.md`](BOTANICAL_SUMMARY.md) | headline numbers + the L. cross-link |

## Headline

- **8,923** `<bot>` occurrences → **7,063** distinct Sanskrit headwords, **1,223**
  canonical species (binomials folded by Genus-species canonicalisation).
- Biggest synonym rings: *Sesamum* 84 Sanskrit names, then Asparagus racemosus,
  Agallochum… (one plant, dozens of poetic synonyms — the kośa tradition).

## Cross-link with the `<ls>L.</ls>` finding

**72%** of botanical headwords (5,054 of 7,063) carry their plant sense as
**lexicographer-only** — MW had most of its botany from kośas/nighaṇṭus, not text.

The honest corpus check (a naive lemma join is contaminated by homograph
collisions — `kṛṣṇa`/`indra`/`kāla` are common words with a rare plant sense):
restrict to **botanical-only headwords** (lemma whose every sense is a plant).
Of 4,148 such headwords, **1,528 are both L.-only and DCS-attested** — clean
confirmations of plant vocabulary MW knew only from lexicons that the modern
corpus nonetheless attests (`agnimukha`=Plumbago zeylanica, `ambuvallī`=Momordica
charantia, `amlī`=Oxalis corniculata, …).

## Notes

- Canonicalisation: Genus capitalised, epithet lowercase, punctuation trimmed.
- Headword IAST via exact SLP1→IAST (k1 carries no accents).
- DCS attestation is lemma-level (DCS-2021); re-run against DCS-2026 for fuller
  coverage. Sense-level confirmation of the *plant* meaning needs sense-tagged
  corpus (the homograph caveat above).
- Analysis only — no `mw.txt` mutation.
