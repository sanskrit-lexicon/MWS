---
paper_id: A45
title: "Naming the Plants: A Corpus-Attested Sanskrit-to-Linnaean Crosswalk from the Monier-Williams Dictionary"
status: draft (skeleton, 2/5) — scaffolded 2026-06-26
readiness: 2/5
venue: "Lexikos / Biodiversity Data Journal / Journal of Open Humanities Data (JOHD)"
author: "**Mārcis Gasūns**, independent scholar ([ORCID 0000-0003-4513-884X](https://orcid.org/0000-0003-4513-884X)), gasyoun@ya.ru"
data_source: "MWS/botanical_glossary/ (mw_botanical_glossary.csv + species_to_sanskrit.json + BOTANICAL_SUMMARY.md; built by bot_glossary.py from csl-orig mw.txt; DCS-2021 attestation via VisualDCS/dcs_lemma_summary.json)"
---

# Naming the Plants: A Corpus-Attested Sanskrit-to-Linnaean Crosswalk from the Monier-Williams Dictionary

> **Draft status (2026-06-26).** Manuscript skeleton built directly on the FAIR dataset
> in [`../botanical_glossary/`](../botanical_glossary/). All numerical claims below are
> transcribed from that dataset and re-count from the committed
> [`mw_botanical_glossary.csv`](../botanical_glossary/mw_botanical_glossary.csv) and
> [`species_to_sanskrit.json`](../botanical_glossary/species_to_sanskrit.json).
> **Open before submission:** (1) write §2 Related work; (2) run the GBIF/POWO
> nomenclatural-currency pass (or commit to the historical-lexicographic framing);
> (3) regenerate the two homograph-controlled figures (4,148 botanical-only headwords /
> 1,567 L.-only-and-attested) and emit the headword list — these come from
> [`BOTANICAL_SUMMARY.md`](../botanical_glossary/BOTANICAL_SUMMARY.md) and are **not**
> reconstructible from the CSV alone, so they are marked *(per `BOTANICAL_SUMMARY.md`)*
> below until regenerated; (4) finalise byline + ORCID; (5) cite A38 once its DCS-2026
> release DOI is minted, and decide DCS-2021 (83,239 lemmas) vs DCS-2026 (98,606) as the
> attestation base.
>
> **Anti-salami note.** This paper is the *resource + corpus-coverage* contribution. The
> evidentiary-gradient interpretation of corpus-confirmed kośa vocabulary is the subject of
> a separate paper (A18/P3) and is **cited here, not argued**. A45 does not lead with the
> "1,567 corpus-confirmed" claim.

## Abstract

The botanical layer of a great historical Sanskrit dictionary is a record of two different
kinds of knowledge: plant names the lexicographer read in running texts, and plant names he
collected from the indigenous synonym lexicons (kośas and nighaṇṭus) without a textual
witness. We extract the complete botanical layer of Monier-Williams' *A Sanskrit-English
Dictionary* (1899) — **8,923** `<bot>` tags spanning **7,063** distinct Sanskrit headwords
mapped to **1,223** canonical Linnaean species — and release it as the first machine-readable
Sanskrit-to-botanical-Latin crosswalk derived from a Cologne dictionary. Two further layers are
joined per occurrence: the dictionary's own lexicographer-only marker (`<ls>L.</ls>`), which
flags a sense attested only in the synonym lexicons, and lemma-level attestation against the
Digital Corpus of Sanskrit (DCS). We find the botanical layer is **predominantly kośa-derived**:
**72%** of botanical headwords (5,054 of 7,063; 6,064 occurrences) carry their plant sense as
lexicographer-only. A naive corpus join would overstate textual support, because common words
carry rare plant senses as homographs (e.g. *kṛṣṇa*, *indra*, *kāla*); after a homograph control
that restricts attention to headwords whose every sense is a plant, a substantial share of the
genuinely plant-only vocabulary is nonetheless DCS-attested *(figure per
`BOTANICAL_SUMMARY.md`; see §4)*. The contribution is the dataset and its corpus-coverage
characterisation, not the evidentiary-gradient interpretation of the corpus-confirmed subset,
which we cite to companion work. The release is FAIR, reproducible from the open Cologne source,
and intended as a reusable bridge between Sanskrit lexicography and biodiversity informatics.

## 1. Introduction

A historical bilingual dictionary of a classical language inherits its subject vocabulary from
two channels. Some words the lexicographer met in texts and could cite; others he took on the
authority of the indigenous lexical tradition — for Sanskrit, the kośas and nighaṇṭus, the verse
synonym-lists that name a plant a dozen poetic ways without ever quoting a passage. Botanical
vocabulary sits squarely at this fault line: the plant world is exactly where a synonym lexicon
is richest and a running text is thinnest. Monier-Williams marks the distinction in his own
apparatus — a sense given on lexical authority alone is tagged `<ls>L.</ls>` ("Lexicographers") —
and the Cologne digitisation preserves that marker, alongside an explicit `<bot>…</bot>` span
naming the Linnaean binomial for each botanical sense.

This paper asks a resource-shaped question: what does the complete botanical layer of MW look
like when it is extracted, canonicalised, and joined to (a) its own lexicographer-only flag and
(b) a modern annotated corpus — and what reusable object does that produce? We make three
contributions:

1. **A FAIR crosswalk.** We release the first machine-readable Sanskrit ↔ botanical-Latin
   crosswalk extracted from a Cologne dictionary: 8,923 occurrences, 7,063 headwords, 1,223
   species, with per-occurrence provenance (L-number, page/column, citation).
2. **A provenance characterisation.** We quantify how much of the botanical layer is
   kośa-derived (lexicographer-only) versus text-citable, and show it is predominantly the
   former (72%).
3. **A corpus-coverage statistic with an explicit homograph control.** We measure how much of
   the layer is attested in the DCS, and show why the join must be restricted to non-homographic
   (botanical-only) headwords before any textual-support claim is defensible.

The evidentiary-gradient reading of the homograph-controlled, corpus-confirmed subset — the
claim that the corpus rehabilitates a measurable slice of vocabulary MW had only from lexicons —
is developed in companion work (A18/P3) and is cited here rather than argued, to keep this paper
to its resource scope.

## 2. Related work  *(TODO — to be written)*

Position against: (i) Sanskrit ethnobotany and plant-name lexicons (the printed nighaṇṭu/kośa
tradition and prior scholarly indices of Sanskrit plant names); (ii) biodiversity-informatics
nomenclatural authorities used for the currency pass — GBIF Backbone Taxonomy, Plants of the
World Online (POWO), the International Plant Names Index (IPNI); (iii) prior digitisation and
structured extraction from the Cologne Monier-Williams; and (iv) the Digital Corpus of Sanskrit
as an attestation source. The novelty claim is the **machine-readable, corpus-attested,
FAIR-packaged crosswalk from a Cologne dictionary** with provenance and a homograph-aware
coverage statistic — not the botanical identifications themselves, which are MW's.

## 3. Data and method

### 3.1 Source and extraction
The source is the Cologne digitisation of Monier-Williams (1899), `mw.txt` in `csl-orig`, in SLP1
transliteration with custom XML-like markup. For every `<bot>…</bot>` span the generator
[`bot_glossary.py`](../botanical_glossary/bot_glossary.py) captures the Sanskrit headword (the
`<k1>` key, SLP1 + an exact SLP1→IAST rendering; `k1` carries no accents), the Linnaean binomial
(raw and canonicalised), and provenance: the `<L>` record number and the `<pc>` page,column of
the 1899 print edition, plus the sense's citation string where present. The work is analysis only
— it never mutates `mw.txt`.

### 3.2 Species canonicalisation
Binomials are folded to a canonical form — Genus capitalised, epithet lower-cased, notes and
punctuation trimmed — so that `Abrus Precatorius` and `Abrus precatorius` collapse to one species.
This yields **1,223** distinct canonical species from the 8,923 occurrences.

### 3.3 The two joined layers
**Lexicographer-only flag.** Each occurrence is flagged `lexicographer_only = yes` when the
botanical sense is given on lexical authority alone (`<ls>L.</ls>`). This is MW's own marker, read
directly from the entry.

**DCS attestation.** Each headword is joined lemma-level to the Digital Corpus of Sanskrit
frequency summary ([`dcs_lemma_summary.json`](../../VisualDCS/dcs_lemma_summary.json),
**DCS-2021**, 83,239 attested lemmas, CC BY, Oliver Hellwig). A headword that matches a DCS lemma
receives a frequency **band**: hapax (1), rare (2–9), uncommon (10–99), common (100–999), or
very-common (1000+), on a log10-orders rule. *(TODO: decide whether to re-run against DCS-2026,
98,606 lemmas, before submission — see A38; the band labels would not change, the coverage would
rise.)*

### 3.4 The homograph control
A naive lemma-level join between "lexicographer-only botanical headword" and "DCS-attested lemma"
is contaminated, because a common word can carry a rare *plant* sense as a homograph: *kṛṣṇa*,
*indra*, and *kāla* are all high-frequency words whose corpus frequency is the non-plant sense,
yet each has a botanical sense MW marked `L.` Lemma attestation therefore does **not** confirm the
*botanical* sense for such headwords. The defensible coverage statistic restricts attention to
**botanical-only headwords** — lemmas whose *every* MW sense is a plant, so no non-plant homograph
can supply the corpus frequency. *(TODO: emit the kept/dropped headword lists as a committed
artifact so the filter is auditable; the 4,148/1,567 figures in §4 are computed over the full MW
sense inventory and are not reconstructible from the released CSV alone.)*

### 3.5 Nomenclatural currency  *(TODO — pass not yet run)*
MW's binomials are 19th-century Linnaean names; many are now synonyms of accepted names
(e.g. *Hedysarum gangeticum*, *Andropogon muricatus*, *Cocculus cordifolius*). A planned pass
resolves each `species_canonical` against POWO / the GBIF Backbone, adding an `accepted_name` and
`nomenclatural_status` field and reporting the accepted-vs-synonym split. **If this pass is not
run, the dataset is framed strictly as a historical-lexicographic crosswalk — MW's names as MW
gave them — not as a claim about current botanical identity.**

## 4. Results

### 4.1 Scale of the botanical layer
The complete botanical layer comprises **8,923** `<bot>` occurrences over **7,063** distinct
Sanskrit headwords mapped to **1,223** canonical Linnaean species. The species-to-synonym
direction ([`species_to_sanskrit.json`](../botanical_glossary/species_to_sanskrit.json)) holds
**1,223** species and **8,859** Sanskrit synonym entries (mean ≈ 7.2 Sanskrit names per species).

### 4.2 The layer is predominantly kośa-derived
**6,064** occurrences — **5,054** distinct headwords, **72%** of all botanical headwords — carry
the plant sense as lexicographer-only. The botanical vocabulary of MW is therefore mostly the
indigenous synonym tradition rather than text-citable plant names: exactly the channel where a
nighaṇṭu is richest.

### 4.3 Synonym rings
The kośa tradition's many-names-for-one-plant habit is visible in the largest synonym rings:

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

### 4.4 Corpus coverage
Joined lemma-level to DCS-2021, **6,341** occurrences across **4,679** distinct headwords are
attested (band non-empty). The attested occurrences distribute across frequency bands as:

| band | occurrences |
|---|--:|
| rare (2–9) | 2,221 |
| uncommon (10–99) | 1,648 |
| hapax (1) | 1,525 |
| common (100–999) | 753 |
| very-common (1000+) | 194 |

### 4.5 Coverage after the homograph control
A naive lemma-level join of lexicographer-only botanical headwords against DCS attestation
recovers a large but **contaminated** set: at the headword level, of the 4,773 headwords whose
every botanical *occurrence* is L.-only, 3,078 are DCS-attested by lemma — but the high-band hits
are dominated by homograph collisions (the *kṛṣṇa/indra/kāla* problem of §3.4), so lemma
attestation does not confirm the plant sense for them. Restricting to **botanical-only** headwords
(no non-plant homograph) gives the defensible figure: **4,148 such headwords, of which 1,567 are
both lexicographer-only and DCS-attested** *(per
[`BOTANICAL_SUMMARY.md`](../botanical_glossary/BOTANICAL_SUMMARY.md); these two numbers are
computed over the full MW sense inventory and are not reconstructible from the released CSV — to be
regenerated and the headword list committed before submission)*. The interpretation of this subset
as an evidentiary gradient — corpus vindication of kośa-only vocabulary — is developed in companion
work (A18/P3) and is not argued here.

### 4.6 Nomenclatural currency  *(TODO — table to be filled after the GBIF/POWO pass)*
Accepted-vs-historical-synonym split of the 1,223 canonical species against POWO/GBIF: **TODO**.

## 5. Discussion

The botanical layer of MW is, by its own marking, mostly an inheritance from the kośa tradition
rather than a harvest from running text — 72% lexicographer-only is a strong, dictionary-internal
statement about where a 19th-century lexicographer's plant knowledge came from. Releasing this
layer as a machine-readable crosswalk turns an internal apparatus into a reusable bridge: a
Sanskrit-to-Linnaean lookup with provenance, usable from the biodiversity-informatics side
(species → attested Sanskrit names) and from the lexicographic side (headword → species + textual
support). The homograph control is the methodological point that makes any corpus-coverage claim
honest: a plain lemma join silently imports the frequency of the wrong sense. The further question
of what the corpus-confirmed, homograph-controlled subset *means* for the evidentiary status of
kośa vocabulary is deferred to A18.

## 6. Limitations

- **Attestation is lemma-level, not sense-level.** DCS matching confirms that a Sanskrit *lemma*
  occurs in the corpus, not that its *botanical* sense does. The homograph control mitigates but
  does not eliminate this; true sense-level confirmation needs sense-tagged corpus data.
- **Nomenclatural currency.** MW's binomials are 19th-century names; without the GBIF/POWO pass
  (§3.5) the dataset is a historical-lexicographic record, not a statement of current taxonomy.
- **Corpus release.** Attestation uses DCS-2021 (83,239 lemmas, the vendored summary); a re-run
  against DCS-2026 (98,606 lemmas; see A38) would raise coverage. The 2021 figure is stated
  explicitly so it is not conflated with the larger 2026 release.
- **Derived homograph-controlled figures.** The 4,148 / 1,567 figures depend on the full MW sense
  inventory and are reported here per `BOTANICAL_SUMMARY.md`; they are to be regenerated with a
  committed headword list before submission.
- **Canonicalisation folds at the binomial level**; genus-only tags (e.g. *Abrus*, *Areca*) remain
  distinct from their binomials by design and are counted as separate canonical species.

## 7. Conclusion

The botanical layer of Monier-Williams — 8,923 tags, 7,063 Sanskrit headwords, 1,223 Linnaean
species — is predominantly kośa-derived (72% lexicographer-only), and we release it as the first
machine-readable, corpus-attested Sanskrit-to-botanical-Latin crosswalk from a Cologne dictionary.
A homograph-controlled join to the Digital Corpus of Sanskrit measures how much of this
lexicon-only vocabulary the modern corpus nonetheless attests, while leaving the evidentiary
interpretation to companion work. The dataset is reproducible from the open Cologne source and is
intended as a durable bridge between Sanskrit lexicography and biodiversity informatics.

## Data and reproducibility

The dataset, its generator, and the headline numbers live under
[`../botanical_glossary/`](../botanical_glossary/):
[`mw_botanical_glossary.csv`](../botanical_glossary/mw_botanical_glossary.csv) (per-occurrence),
[`species_to_sanskrit.json`](../botanical_glossary/species_to_sanskrit.json) (species → synonym
ring), [`BOTANICAL_SUMMARY.md`](../botanical_glossary/BOTANICAL_SUMMARY.md) and
[`README.md`](../botanical_glossary/README.md). Everything regenerates with
`python bot_glossary.py` from the Cologne `mw.txt` source plus the DCS-2021 summary
[`dcs_lemma_summary.json`](../../VisualDCS/dcs_lemma_summary.json). The work is an analysis layer
only — it never edits `mw.txt`. *(TODO: DOI + per-file SHA256 after release; pin the `mw.txt`
source commit; cite A38 for the DCS denominator and A18 for the evidentiary-gradient analysis.)*
