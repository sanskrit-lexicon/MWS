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

> **Draft status (2026-07-08, readiness 3/5).** Manuscript built directly on the FAIR dataset
> in [`../botanical_glossary/`](../botanical_glossary/). All numerical claims below are
> transcribed from that dataset and re-count from the committed
> [`mw_botanical_glossary.csv`](../botanical_glossary/mw_botanical_glossary.csv),
> [`species_to_sanskrit.json`](../botanical_glossary/species_to_sanskrit.json), and
> [`homograph_control_headwords.csv`](../botanical_glossary/homograph_control_headwords.csv).
> **Done this pass:** §2 Related work written; the homograph-control figures (4,148 botanical-only
> / 1,567 clean confirmations) are now emitted as an auditable committed CSV and reproduce from it;
> the GBIF nomenclatural-currency pass is run and §3.5/§4.6 report the accepted-vs-synonym split;
> the synonym-ring distribution is quantified (§4.3). **Open before submission (author/@DO):**
> (1) finalise byline + ORCID (in front matter, to confirm); (2) cite A38 once its DCS-2026 release
> DOI is minted, and decide DCS-2021 (83,239 lemmas) vs DCS-2026 (98,606) as the attestation base;
> (3) pick the venue and do the final read; (4) mint the dataset DOI and fill the per-file SHA256s
> in §"Data and reproducibility".
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
that restricts attention to headwords whose every sense is a plant (4,148 such headwords), a
substantial share — 1,567 — is nonetheless DCS-attested (see §4.5, reproducible from the committed
audit file). The contribution is the dataset and its corpus-coverage
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

## 2. Related work

Four bodies of work meet in this dataset: the indigenous Sanskrit tradition of plant naming, the
scholarly indices that have tried to fix those names to modern botany, the digitisation of the
source dictionary, and the biodiversity-informatics infrastructure that supplies a nomenclatural
ground truth.

**The Sanskrit plant-name tradition.** Plant vocabulary in Sanskrit is transmitted less through
running text than through the synonym lexicons — the *kośa* and *nighaṇṭu* literature. The
*Amarakośa* devotes a whole section (the *vanauṣadhi-varga*) to the names of trees and herbs, and
the medical *nighaṇṭus* — the *Dhanvantarīya-*, *Rāja-*, and *Bhāvaprakāśa-nighaṇṭu* among them —
list a single plant under a dozen or more poetic synonyms, typically without a textual citation.
This is precisely the material Monier-Williams marked "L." ("Lexicographers"): a botanical sense
carried on the authority of these lists rather than an attested passage. Our dataset makes that
lexical stratum machine-readable and measurable for the first time.

**Sanskrit ethnobotanical indices.** Mapping these Sanskrit names onto Linnaean species is an old
scholarly project. Nineteenth- and twentieth-century materia medica and floras — Roxburgh's
*Flora Indica*, from which MW's own identifications partly descend; Kirtikar and Basu's *Indian
Medicinal Plants*; Nadkarni's *Indian Materia Medica*; and the *dravyaguṇa* handbooks of the
Ayurvedic tradition — pair Sanskrit plant names with botanical binomials, and modern efforts such
as the FRLHT/ENVIS databases of Indian medicinal plants continue the work in digital form. These
resources are organised around the *plant* (a species and its uses, with Sanskrit names as one
attribute); none is a complete, per-occurrence extraction of a *dictionary's* botanical layer
carrying the dictionary's own provenance markers, which is what we release here.

**Digitisation of Monier-Williams.** The Cologne Digital Sanskrit Dictionaries (CDSL) project has
digitised MW and some seventy other Sanskrit dictionaries into a consistent XML-like markup, in
which the `<bot>` binomial span and the `<ls>L.</ls>` source flag we exploit are explicit,
queryable elements. Prior structured extractions from the Cologne MW have targeted headwords,
senses, and cross-references; the botanical layer as a self-standing, corpus-joined resource has
not previously been isolated. We build directly on the open Cologne source and add only an
analysis layer, never editing it.

**Biodiversity-informatics authorities and corpus attestation.** For the nomenclatural-currency
pass we resolve MW's binomials against the standard aggregators of botanical nomenclature — the
GBIF Backbone Taxonomy, Plants of the World Online (POWO), and the International Plant Names Index
(IPNI) — which record for each name whether it is currently accepted or a synonym of an accepted
name. For textual attestation we use the Digital Corpus of Sanskrit (DCS; Hellwig), the largest
lemmatised, morphologically annotated Sanskrit corpus, as the witness against which a dictionary
headword is judged corpus-attested. The novelty of this paper is not the botanical identifications
(which are MW's) nor the corpus (which is Hellwig's), but the **machine-readable, corpus-attested,
FAIR-packaged crosswalk from a Cologne dictionary**, with per-occurrence provenance and an explicit
homograph-aware coverage statistic that keeps the corpus claim honest.

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
can supply the corpus frequency. The filter is fully auditable: the generator emits
[`homograph_control_headwords.csv`](../botanical_glossary/homograph_control_headwords.csv), one row
per distinct botanical headword, flagging whether it is lexicographer-only, botanical-only (the
homograph control), and DCS-attested. Every headline count in §4.5 reproduces by filtering that
file. The `botanical_only` flag is derived from the full MW sense inventory (the presence of any
non-plant sense on the lemma), which the per-occurrence release CSV does not itself carry — hence
the dedicated audit file.

### 3.5 Nomenclatural currency
MW's binomials are 19th-century Linnaean names; many are now synonyms of accepted names
(e.g. *Hedysarum gangeticum*, *Andropogon muricatus*, *Cocculus cordifolius*). We resolve each of
the 1,223 `species_canonical` values against the GBIF Backbone Taxonomy via its `/species/match`
endpoint (kingdom Plantae), which folds POWO, IPNI, and the Catalogue of Life. The generator
[`gbif_currency.py`](../botanical_glossary/gbif_currency.py) records, per species, the GBIF
taxonomic status (accepted / synonym / doubtful), the currently accepted name where MW's is a
synonym, the family, and the match rank and quality, into
[`species_currency.csv`](../botanical_glossary/species_currency.csv). Because a genus-only MW tag
(*Sesamum*, *Abrus*) resolves "accepted" at genus rank and would inflate the accepted share, the
honest currency figure is computed on the subset GBIF matched at **species** rank (§4.6). The
dataset is nonetheless framed as a **historical-lexicographic crosswalk** — MW's names as MW gave
them, with the modern accepted name attached as a resolvable layer, not a silent overwrite.

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
The species-to-Sanskrit direction holds 1,223 species and 8,859 synonym entries, a mean of 7.2
Sanskrit names per species — but the mean is a poor summary of a sharply right-skewed distribution
(median 2). The mass is at the two ends: **473 species (38.7%) are singletons** with a single
Sanskrit name, while **147 species (12.0%) carry twenty or more**, and the largest rings run to
dozens. This is the signature of the kośa tradition: a plant of ritual, medical, or poetic
importance accretes a long tail of synonyms, while an incidental plant is named once.

| ring size (Sanskrit names per species) | species | % |
|---|--:|--:|
| 1 (singleton) | 473 | 38.7% |
| 2–4 | 302 | 24.7% |
| 5–9 | 176 | 14.4% |
| 10–19 | 125 | 10.2% |
| 20+ | 147 | 12.0% |

The largest synonym rings:

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
recovers a large but **contaminated** set: of the 5,054 headwords carrying a lexicographer-only
botanical sense, 3,348 are DCS-attested by lemma — but the high-band hits are dominated by
homograph collisions (the *kṛṣṇa/indra/kāla* problem of §3.4), so lemma attestation does not
confirm the plant sense for them. Restricting to **botanical-only** headwords (no non-plant
homograph) gives the defensible figure: MW has **4,148 botanical-only headwords, of which 1,567
are both lexicographer-only and DCS-attested** — plant vocabulary MW carried only from the
lexicons that the modern corpus nonetheless attests, with no homograph escape hatch. All four
counts (7,063 botanical headwords; 5,054 lexicographer-only; 4,148 botanical-only; 1,567 clean
confirmations) reproduce directly from the committed
[`homograph_control_headwords.csv`](../botanical_glossary/homograph_control_headwords.csv). The
interpretation of the 1,567-headword subset as an evidentiary gradient — corpus vindication of
kośa-only vocabulary — is developed in companion work (A18/P3) and is not argued here.

### 4.6 Nomenclatural currency
Resolving the 1,223 canonical species against the GBIF Backbone Taxonomy, **726 are matched at
species rank** (a full binomial identification), 272 at genus rank (genus-only MW tags), 51 at
family rank, and 164 only to kingdom Plantae — i.e. 164 of MW's names are not in the modern
backbone at all, and are neither confirmed nor superseded, only unlocated.

The currency verdict is clearest on the 726 species-rank binomials, and it is striking: **only
about half of MW's identifiable binomials are still accepted names.**

| GBIF status (species-rank matches) | species | % |
|---|--:|--:|
| accepted | 377 | 51.9% |
| synonym (superseded) | 346 | 47.7% |
| doubtful | 3 | 0.4% |

Almost half of the binomials MW gave (346 of the 723 accepted-or-synonym) are now historical
synonyms of a currently accepted name — *Acacia arabica* → *Vachellia nilotica*, *Acacia
farnesiana* → *Vachellia farnesiana*, *Achyranthes aquatica* → *Centrostachys aquatica*, and so
on. This is exactly why the release keeps MW's name verbatim and attaches the accepted name as a
separate resolvable field (`accepted_name` in
[`species_currency.csv`](../botanical_glossary/species_currency.csv)) rather than modernising the
identifications in place: the dataset is a *historical-lexicographic* record whose taxonomy can be
brought current on demand, not a claim about present-day botanical identity. (Counting all 1,216
resolved names including genus-rank matches gives 68.2% accepted / 31.8% synonym, but that figure
is inflated by genus-only tags that are trivially "accepted" at genus rank; the species-rank split
is the defensible one.) The most-represented families are Fabaceae (142), Poaceae (55),
Apocynaceae (43), Malvaceae and Lamiaceae (41 each) — the legumes, grasses, and mints of the
subcontinent's economic and medicinal flora.

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

The nomenclatural-currency pass adds a second, independent reason to treat the crosswalk as a
historical document rather than a modern determination: nearly half of the binomials MW gave are,
a century and a quarter later, superseded names. Rather than modernise the identifications — which
would erase what MW actually wrote and bake in a 2020s taxonomy that will itself age — we keep MW's
name and attach the current accepted name as a separate field. The crosswalk is thus usable in
both directions in time: as a record of what a great nineteenth-century lexicographer identified,
and, through the GBIF layer, as a bridge to present-day biodiversity data.

## 6. Limitations

- **Attestation is lemma-level, not sense-level.** DCS matching confirms that a Sanskrit *lemma*
  occurs in the corpus, not that its *botanical* sense does. The homograph control mitigates but
  does not eliminate this; true sense-level confirmation needs sense-tagged corpus data.
- **Nomenclatural currency.** MW's binomials are 19th-century names, and the GBIF pass (§4.6)
  shows nearly half of the species-rank binomials are now synonyms. The dataset is therefore a
  historical-lexicographic record with the modern accepted name attached as a resolvable layer,
  not a statement of current taxonomy; 164 names GBIF could not place at all remain unlocated.
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
ring), [`homograph_control_headwords.csv`](../botanical_glossary/homograph_control_headwords.csv)
(the auditable homograph-control flags behind §4.5),
[`species_currency.csv`](../botanical_glossary/species_currency.csv) +
[`CURRENCY_SUMMARY.md`](../botanical_glossary/CURRENCY_SUMMARY.md) (the GBIF currency pass),
[`BOTANICAL_SUMMARY.md`](../botanical_glossary/BOTANICAL_SUMMARY.md) and
[`README.md`](../botanical_glossary/README.md). The glossary and audit files regenerate with
`python bot_glossary.py` from the Cologne `mw.txt` source plus the DCS-2021 summary
[`dcs_lemma_summary.json`](../../VisualDCS/dcs_lemma_summary.json); the currency pass regenerates
with `python gbif_currency.py` (cached against the GBIF Backbone Taxonomy). The work is an analysis
layer only — it never edits `mw.txt`. *(TODO: DOI + per-file SHA256 after release; pin the `mw.txt`
source commit; cite A38 for the DCS denominator and A18 for the evidentiary-gradient analysis.)*
