# MW botanical glossary (#74) — summary

- `<bot>` occurrences: **8,923**
- Distinct Sanskrit headwords with a botanical sense: **7,063**
- Distinct canonical species (binomials): **1,223**
- DCS-attested headwords (any band): 6,221 occurrences

## Cross-link with the `<ls>L.</ls>` finding
- Botanical senses marked **lexicographer-only**: 6,064 occurrences,
  5,054 distinct headwords (72% of botanical headwords).
- Naive lemma-level join: 3,281 of those headwords are DCS-attested —
  **but most high-band hits are homograph collisions** (`kṛṣṇa`, `indra`, `kāla`
  are common words with a rare *plant* sense marked L.; the corpus frequency is
  the non-plant sense). Lemma attestation does NOT confirm the botanical sense here.
- **Filtered subset — botanical-only headwords** (lemma whose *every* sense is a
  plant, so no homograph): 4,148 such headwords; of these,
  **1,528 are both L.-only and DCS-attested** — clean confirmations
  of plant vocabulary MW had only from kośas that the corpus nonetheless attests.

## Biggest synonym rings (one species, many Sanskrit names)
| species | # Sanskrit synonyms |
|---|--:|
| *Sesamum* | 84 |
| *Asparagus racemosus* | 65 |
| *Agallochum* | 59 |
| *Abrus precatorius* | 58 |
| *Asteracantha longifolia* | 56 |
| *Butea frondosa* | 55 |
| *Costus speciosus* | 54 |
| *Bignonia suaveolens* | 53 |
| *Cyperus rotundus* | 53 |
| *Andropogon muricatus* | 50 |
| *Alhagi maurorum* | 46 |
| *Cocculus cordifolius* | 46 |

## Files
- `mw_botanical_glossary.csv` — per-occurrence: headword (SLP1+IAST), species
  (canonical+raw), L-number, page, citation, lexicographer-only flag, DCS band.
- `species_to_sanskrit.json` — canonical species → sorted Sanskrit synonym ring.

## Notes
- Canonicalisation: Genus capitalised, epithet lowercase, notes/punctuation
  trimmed — folds `Abrus Precatorius`/`Abrus precatorius` into one species.
- Headword IAST via exact SLP1→IAST (k1 carries no accents).
- DCS attestation is lemma-level (DCS-2021 summary). Re-run against DCS-2026
  for fuller coverage (see ../lexicographer_dcs/).
- Supersedes the frequency-only `botbio/mw_bot.txt`; this is the FAIR export.
