{% raw %}
# MW1899 — Microstructural working notes

**Working document.** Exhaustive block-by-block analysis of the Monier-Williams *Sanskrit-English Dictionary* (1899) as digitized in [CDSL `mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt). This file is the **data source** for the consolidated [paper](PAPER.md) in this directory ([README](README.md)).

All counts computed 2026-05-23 against [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) (286,561 records, 48.9 MB).

---

## 1 · Formal block inventory (18 blocks)

A *formal block* is a discriminable structural component of an MW entry that can be detected by markup or stereotyped notation. Each block has (a) a marker/locus in the data, (b) a semantic role (see §2), and (c) a population frequency.

| # | Formal block | Marker / locus | Semantic role (§2) | Entries with this block | % of 286,561 |
|---:|---|---|---|--:|--:|
| F01 | **Record header** | `<L>N<pc>P,C<k1>K1<k2>K2<h>H<e>E` | Identity + form | 286,561 | 100.0% |
| F02 | **Display headword** | `<s>…</s>` or `<s1>…</s1>` first after header | Form | ~284,000 | ~99% |
| F03 | **Homophone disambiguator** | `<hom>N.</hom>` | Form (identity) | — | many |
| F04 | **Grammatical category** | `<lex>…</lex>` | Grammar | 185,888 | 64.9% |
| F05 | **Verb inflection class** | `<ab>cl.</ab>` *N*, `<ab>P.</ab>`, `<ab>Ā.</ab>` | Grammar (verbal) | ~2,500 | < 1% |
| F06 | **Etymology root marker** | `√` glyph + root-headword, `<ab>fr.</ab>` | Etymology | ~17,000 | ~6% |
| F07 | **IE cognate** | `<lang>…</lang>` + `<gk>`/`<etym>` content | Etymology (comparative) | 3,960 tags / ~2,099 entries | 0.7% |
| F08 | **Inflection form** | additional `<s>…</s>` after primary headword | Form (inflection) | ~60,000 | ~21% |
| F09 | **Editorial commentary** | parenthetical prose, often introduced by `(probably …)`, `(perhaps …)` | Discourse | ~25,000 | ~9% |
| F10 | **Sense gloss** | English text after `¦` separator | Sense | 286,488 | ~100% |
| F11 | **Sense division** | numbered `1)` / lettered `a)`, or implicit by semicolon | Sense | many (informal) | varies |
| F12 | **Source citation** | `<ls>…</ls>` (with optional numeric coordinate) | Evidentiary | ~230,000 | ~80% |
| F13 | **Hedge marker (L.)** | `<ls>L.</ls>` specifically — "lexicographers only" | Evidentiary (hedged) | 39,962 entries / 40,212 cites (audited; see `analysis/SPOTCHECK.md`) | 13.9% / 12.9% of all cites |
| F14 | **Botanical name** | `<bot>…</bot>` | Encyclopedic | 8,923 tags / ~8,059 entries | 2.8% |
| F15 | **Biographical content** | `<bio>…</bio>`, `<s1>…</s1>` (proper-name Sanskrit) | Encyclopedic | many | ~few % |
| F16 | **Cross-reference** | `q.v.`, `<ab>cf.</ab>`, `<ab>id.</ab>`, "see X" | Discourse | ~25,000 | ~9% |
| F17 | **Machine annotation** | `<info …/>` self-closing | Meta | 292,603 tags / ~275,000 entries | ~96% |
| F18 | **Correction record** | `{{old -> new \|\| YYYY-MM-DD \| author \| URL \|}}` | Meta (provenance) | tiny | < 0.01% |

**Note F12 vs F13:** F13 (`L.`) is technically a special case of F12 (any `<ls>`). They are tracked separately because of their distinct evidentiary value — see [DICT_PROFILE Citation markers](../../DICT_PROFILE.md#citation-markers--not-all-are-literary-works) and the [PWG↔MW lineage analysis](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg).

**Note F08:** "Inflection form" detected as `<s>…</s>` count ≥ 2. Roots typically have 3-5 (P., Ā., causative, intensive, perfect…).

---

## 2 · Semantic block taxonomy (8 categories)

A *semantic block* is the kind of information conveyed, independent of its formal locus. Each formal block (§1) maps to one or more semantic categories.

| # | Semantic block | What it conveys | Realised by formal blocks |
|---:|---|---|---|
| S1 | **Identity** | Which lemma this is (vs. homophones) | F01, F02, F03 |
| S2 | **Form** | Orthography, accent, segmentation, compound boundary | F01 (k1/k2), F02, F08 |
| S3 | **Grammar** | POS, gender, voice, conjugation class | F04, F05 |
| S4 | **Etymology** | Source root, comparative cognates, MW's historical reasoning | F06, F07, F09 (when etymological) |
| S5 | **Sense** | Definition, sense divisions, sub-senses | F10, F11 |
| S6 | **Evidentiary** | Textual / lexicographic attestation; hedges on evidence strength | F12, F13 |
| S7 | **Encyclopedic** | Identification of proper nouns, botanical species, mythological figures | F14, F15, partly F10 |
| S8 | **Discourse** | Cross-references, editorial commentary, comparative remarks | F09 (when editorial), F16 |

**Meta-block (M):** F17 (machine annotation) and F18 (correction record) belong to neither dictionary content nor a semantic role — they are *infrastructure*.

---

## 3 · Article-type typology (8 primary types + 3 orthogonal properties)

Per [DOUBTS D5](DOUBTS.md#d5--article-type-typology--refactored-to-8-primary-types--3-orthogonal-properties--resolved-2026-05-27), the original 14-bucket classification conflated two orthogonal axes — *what kind of entry this is* (primary type) versus *what additional information it happens to carry* (orthogonal property). The refactored typology separates them. The original 14 buckets are preserved in [§3.1 below](#31--the-original-14-bucket-classification-legacy) for traceability and for anyone running the legacy detector.

### 3 · The 8 primary types

Primary types are **mutually-near-exclusive descriptors** of the entry's *kind*. Counts reflect each entry classified to one primary type (with *other* as the residual bucket).

| Type code | Defined by | Count | % of 286,561 |
|---|---|--:|--:|
| **root** | `<info verb="genuineroot"/>` | 750 | 0.26% |
| **nominal** (sub-feature: gender m/f/n/mn) | `<lex>m./f./n./mn.</lex>` (without compound marker) | ≈ 37,700 | ≈ 13.2% |
| **adjective** | `<lex>mfn.</lex>` | 12,240 | 4.27% |
| **indeclinable** | `<lex>ind.</lex>` | 1,929 | 0.67% |
| **compound** | `<e>3*` + em-dash/hyphen in `<k2>` | 126,360 | 44.10% |
| **derived** | `<e>2*` | 72,119 | 25.17% |
| **continuation** | `<e>1A` | 9,294 | 3.24% |
| **encyclopedic** (sub-feature: botanical / biographical) | `<bot>` or `<bio>` tag(s) | 8,405 | 2.93% |
| **other** | none of the above | 19,460 | 6.79% |

The dictionary is dominated by **compound sub-entries (44%)** and **derived forms (25%)** — together 69% of all records. The two encyclopedic sub-types share the *encyclopedic-doubled* signature (semantic comment is itself encyclopedic) but differ in distribution (8,059 botanical vs 346 biographical).

### 3.2 · The 3 orthogonal properties

Orthogonal properties are **flags** attached to any primary type. An entry can carry zero, one, two, or all three. They were promoted out of the type list because they describe *additional information present on the entry*, not the entry's structural kind.

| Property | Defined by | Count | % of 286,561 | Most concentrated in |
|---|---|--:|--:|---|
| **Vedic-accented** | `/` in `<k2>` | 47,598 | 16.6% | nominals, especially Vedic vocabulary |
| **Lex-hedged** | `<ls>L.</ls>` present | 39,962 entries (40,212 hedge *instances* — a record can carry more than one) | 13.9% | 100% of former "lexicographer_only" bucket; 72% of botanicals, 65% of biographicals |
| **IE-cognate-bearing** | `<lang>` tag(s) | 2,099 | 0.73% | roots (35%) |

### 3.3 · Cross-tabulation of primary types × orthogonal properties

Approximate joint counts (`E` = encyclopedic; counts derive from the same `mw_block_matrix.py` over `mw.txt`):

| Primary type ↓ / Property → | **Vedic-acc.** | **Lex-hedged** | **IE-cognate** | None of the 3 |
|---|--:|--:|--:|--:|
| **root** | 8% | 7% | 35% | ≈ 58% |
| **nominal** | 18–24% | 12–21% | < 1% | ≈ 60–70% |
| **adjective** | 11% | 4% | < 1% | ≈ 85% |
| **indeclinable** | 9% | 2% | 2% | ≈ 88% |
| **compound** | 14% | 13% | < 1% | ≈ 73% |
| **derived** | 19% | 16% | < 1% | ≈ 65% |
| **continuation** | 12% | 21% | < 1% | ≈ 67% |
| **encyclopedic** (bot+bio) | 6–16% | 65–72% | < 1% | ≈ 20–30% |

**Reading.** Lex-hedging dominates the encyclopedic primary type (65–72%) and the continuation type (21%); Vedic-accenting concentrates in nominals and derived forms (18–24% / 19%); IE-cognate-bearing is overwhelmingly a roots phenomenon (35%). A *Vedic-accented lex-hedged nominal* is a real entry-shape in MW (≈ 4% of nominals) and would have been silently lost in the old 14-bucket scheme.

### 3.1 · The original 14-bucket classification (legacy)

Retained for reproducibility of the [§4 matrix](#4--the-block-by-article-type-matrix) and the [mw_block_matrix.py](#8--cross-references-to-docs-pass-material) detector. Counts reflect overlapping buckets — an entry can be (e.g.) `noun_m` AND `vedic_accented` AND `biographical`.

| Type code | Defined by | Count | % of 286,561 |
|---|---|--:|--:|
| **root** | `<info verb="genuineroot"/>` | 750 | 0.26% |
| **noun_m** | `<lex>m.</lex>` (without compound marker) | 19,204 | 6.70% |
| **noun_f** | `<lex>f.</lex>` (without compound marker) | 8,479 | 2.96% |
| **noun_n** | `<lex>n.</lex>` (without compound marker) | 9,918 | 3.46% |
| **noun_mn** | `<lex>mn.</lex>` | small | < 1% |
| **adjective_mfn** | `<lex>mfn.</lex>` | 12,240 | 4.27% |
| **indeclinable** | `<lex>ind.</lex>` | 1,929 | 0.67% |
| **compound** | `<e>3*` + em-dash/hyphen in `<k2>` | 126,360 | 44.10% |
| **derived** | `<e>2*` | 72,119 | 25.17% |
| **continuation** | `<e>1A` | 9,294 | 3.24% |
| **lexicographer_only** | only `<ls>L.</ls>` citations (no other) | 38,414 | 13.41% |
| **etymological_ie** | has `<lang>` tag(s) | 2,099 | 0.73% |
| **botanical** | has `<bot>` tag(s) | 8,059 | 2.81% |
| **biographical** | has `<bio>` tag(s) | 346 | 0.12% |
| **vedic_accented** | `/` in `<k2>` | 47,598 | 16.61% |
| **other** | none of the above | 19,460 | 6.79% |

Legacy-to-refactored mapping: `noun_m + noun_f + noun_n + noun_mn → nominal`; `adjective_mfn → adjective`; `botanical + biographical → encyclopedic (with gender-like sub-feature)`; `lexicographer_only → primary type whose distinguishing feature is the *lex-hedged* property`; `etymological_ie → IE-cognate-bearing property`; `vedic_accented → Vedic-accented property`. The 14-row matrix in §4 is identical in data to the refactored view; only the row labels reorganise.

---

## 4 · The block-by-article-type matrix

Each cell: percentage of entries of that type that contain that formal block.

| Block ↓ / Type → | **root** | **noun_m** | **noun_f** | **noun_n** | **adj.** | **ind.** | **comp.** | **deriv.** | **cont.** | **lex.only** | **IE etym** | **bot.** | **bio.** | **Ved.acc.** | other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| F01 header | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 100% |
| F02 display headword | 100% | 72.3 | 77.4 | 71.8 | 70.2 | 83.0 | 84.7 | 68.5 | 33.9 | 69.2 | 94.9 | 66.6 | 75.4 | 69.7 | 80.9 |
| F03 homophone | **49.6** | 3.8 | 2.4 | 2.7 | 6.0 | 9.8 | 0.9 | 4.3 | 0.7 | 1.5 | 17.6 | 0.6 | 2.0 | 4.3 | 10.9 |
| F04 grammatical cat. | 0.1 | **100** | **100** | **100** | **100** | **100** | 80.7 | 51.0 | 0.3 | 65.2 | 27.0 | 69.1 | 74.9 | 51.2 | 10.9 |
| F05 verb inflect class | **98.4** | 0.0 | 0.0 | 0.0 | 0.1 | 0.0 | 0.3 | 1.3 | 0.0 | 0.2 | **24.7** | 0.0 | 0.0 | 0.1 | 25.3 |
| F06 etymology root | **44.7** | 8.8 | 4.0 | 8.2 | 17.1 | 8.7 | 1.6 | 4.8 | 1.3 | 1.7 | **29.1** | 0.9 | 1.4 | 5.9 | 42.9 |
| F07 IE cognate | **35.2** | 0.5 | 0.5 | 0.4 | 0.2 | 2.0 | 0.1 | 0.6 | 0.6 | 0.1 | **100** | 0.1 | 0.3 | 0.8 | 0.0 |
| F08 inflection form | **99.9** | 21.6 | 22.6 | 18.4 | 24.9 | 30.2 | 18.5 | 23.2 | 6.5 | 16.7 | **52.7** | 14.0 | 20.2 | 28.1 | 60.2 |
| F09 editorial commentary | **78.1** | 7.1 | 5.5 | 5.3 | 5.4 | 11.5 | 3.5 | 7.4 | 10.0 | 2.6 | **38.4** | 6.4 | 15.0 | 10.7 | 10.2 |
| F10 sense gloss | **100** | **100** | **100** | **100** | **100** | **100** | 97.9 | 98.3 | 97.0 | **100** | **100** | **100** | **100** | 98.7 | 93.3 |
| F11 sense division | 0.0 | 0.1 | 0.1 | 0.1 | 0.2 | 0.2 | 0.0 | 0.2 | 0.0 | 0.0 | 0.4 | 0.0 | 0.3 | 0.2 | 0.0 |
| F12 source citation | **99.3** | 78.2 | 67.8 | 66.4 | 84.6 | 77.2 | 81.2 | 80.6 | 80.7 | **100** | 57.5 | 93.1 | 93.6 | 88.1 | 62.8 |
| F13 hedge L. | 7.2 | 18.9 | 20.8 | 12.2 | 4.4 | 2.2 | 13.1 | 16.2 | 21.1 | **100** | 3.2 | **71.5** | **64.7** | 10.5 | 0.4 |
| F14 botanical | 0.0 | 3.4 | 5.9 | 1.8 | 0.2 | 0.1 | 3.3 | 2.5 | 2.4 | 14.5 | 0.5 | **100** | 1.7 | 1.7 | 0.0 |
| F15 biographical | 5.9 | 19.9 | 13.9 | 12.5 | 6.0 | 5.7 | 14.7 | 11.2 | 15.2 | 11.7 | 7.0 | 2.4 | **100** | 17.6 | 7.5 |
| F16 cross-reference | **54.5** | 8.3 | 7.5 | 5.8 | 5.2 | 8.7 | 4.7 | 7.8 | 7.3 | 6.3 | **54.5** | 3.5 | 8.7 | 7.5 | 8.2 |
| F17 machine annotation | **100** | 99.8 | 99.6 | 99.9 | **100** | 99.9 | 96.3 | 95.1 | 98.6 | 99.2 | 63.0 | 99.5 | 99.7 | 97.9 | 82.2 |
| F18 correction record | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

**Reading the matrix.** Each row is a block; each column is an article type. Bold cells highlight the **type-defining blocks** (>50%) or the most striking concentrations. Diagonal-like patterns: F14 botanical → botanical type 100%, F15 biographical → biographical type 100%, F13 hedge → lexicographer_only 100%. **The off-diagonals matter most**: F13 (L.) at 71.5% in botanicals and 64.7% in biographicals reveals that MW's botanical and mythological identifications come overwhelmingly from indigenous lexica, not from textual attestation — a hedging that the [Beyond PWG section](../../DICT_PROFILE.md#beyond-pwg--what-mw-contributes) does not surface.

---

## 5 · Fullness scale

For each entry, count how many of the 18 formal blocks are present.

### Distribution

| # blocks | Entries | % | Label |
|--:|--:|--:|---|
| 1 | 4,393 | 1.5% | Vestigial |
| 2 | 1,272 | 0.4% | Skeletal |
| 3 | 5,118 | 1.8% | Skeletal |
| 4 | 38,958 | 13.6% | Compact |
| 5 | 48,472 | 16.9% | Compact |
| 6 | 91,299 | **31.9%** | **Typical** |
| 7 | 57,043 | 19.9% | Standard |
| 8 | 27,070 | 9.4% | Rich |
| 9 | 8,867 | 3.1% | Rich |
| 10 | 2,982 | 1.0% | Full |
| 11 | 861 | 0.3% | Full |
| 12 | 206 | 0.1% | Elaborate |
| 13+ | 20 | 0.0% | Elaborate |

**Modal entry has 6 blocks.** Median 6. Mean ≈ 6.1.

### Fullness scale (5-tier)

I propose a 5-tier scale for descriptive use:

| Tier | Blocks | % of dictionary | Typical contents |
|---|---|--:|---|
| **T1 Vestigial** | 1–3 | 3.7% | Header + one sense; often a continuation entry or a cross-reference stub |
| **T2 Skeletal** | 4–5 | 30.5% | Header + display + grammar + sense + (machine-annotation OR one citation) |
| **T3 Typical** | 6 | 31.9% | T2 + citation + machine-annotation |
| **T4 Rich** | 7–9 | 32.4% | T3 + etymology OR encyclopedic OR cross-reference OR editorial commentary |
| **T5 Elaborate** | 10+ | 1.4% | T4 + multiple optional blocks (IE cognates + editorial + multiple inflection forms + sub-entries) |

### Average fullness by article type

| Article type | Avg blocks | Tier (modal) |
|---|--:|---|
| **root** | **9.73** | **T5 Elaborate** |
| **etymological_ie** | **7.70** | **T4 Rich** |
| **biographical** | 7.58 | T4 Rich |
| **botanical** | 7.28 | T4 Rich |
| **lexicographer_only** | 6.89 | T3/T4 |
| **noun_m** | 6.43 | T3 Typical |
| **indeclinable** | 6.39 | T3 |
| **noun_f** | 6.28 | T3 |
| **adjective_mfn** | 6.25 | T3 |
| **noun_n** | 6.05 | T3 |
| **compound** | 6.02 | T3 |
| **other** | 5.96 | T2/T3 |
| **vedic_accented** | 5.93 | T2/T3 |
| **derived** | 5.73 | T2/T3 |
| **continuation** | **4.76** | **T2 Skeletal** |

**Roots are 2× as elaborate as continuations.** This reflects MW's editorial priority: verbal roots (`<info verb="genuineroot"/>`, just 750 of them) are the conceptual scaffolding of the dictionary, treated with maximum apparatus. Continuation senses (`<e>1A`, 9,294 of them) are economical pointers under their primary lemma.

---

## 6 · Worked microstructure samples

Each sample shows: the raw `mw.txt` content, the formal blocks present, the semantic-block mapping, and the fullness tier.

### Sample A: Verbal root — [L9 *aṃś*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L52) (T5 Elaborate)

```
<L>9<pc>1,1<k1>aMS<k2>aMS<e>1
<s>aMS</s> ¦ <ab>cl.</ab> 10. <ab>P.</ab> <s>aMSayati</s>, to divide, distribute, <ls>L.</ls>;
also occasionally <ab>Ā.</ab> <s>aMSayate</s>, <ls>L.</ls>; also <s>aMSApayati</s>, <ls>L.</ls>
<info verb="genuineroot" cp="10P,10Ā"/>

```

| Block | Realisation | Semantic role |
|---|---|---|
| F01 header | `<L>9<pc>1,1<k1>aMS<k2>aMS<e>1` | S1 + S2 |
| F02 display headword | `<s>aMS</s>` | S2 |
| F04 grammatical cat. | (none — verb, no `<lex>` tag) | — |
| F05 verb inflect class | `<ab>cl.</ab> 10. <ab>P.</ab>` … `<ab>Ā.</ab>` | S3 |
| F08 inflection form | `<s>aMSayati</s>`, `<s>aMSayate</s>`, `<s>aMSApayati</s>` (×3) | S2 (inflection) |
| F10 sense gloss | "to divide, distribute" | S5 |
| F12 source citation | `<ls>L.</ls>` (×3) | S6 |
| F13 hedge L. | all three are `L.` — entry is lexicographer-only | S6 (hedged) |
| F17 machine annotation | `<info verb="genuineroot" cp="10P,10Ā"/>` | M (meta) |

**Blocks present: 9.** Tier T5 (Elaborate). Semantic categories covered: S1, S2, S3, S5, S6 — Identity / Form / Grammar / Sense / Evidentiary. The triple `<ls>L.</ls>` is the most striking feature: the root is real but its productive forms are *not textually attested* — a hedge MW makes explicit ([PWG would have named the kosha here](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg)).

### Sample B: Masculine noun with etymology — [L10 *áṃśa*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L55) (T5 Elaborate)

```
<L>10<pc>1,1<k1>aMSa<k2>a/MSa<e>1
<s>a/MSa</s> ¦ <lex>m.</lex> (probably <ab>fr.</ab> √ <hom>1.</hom> <s>aS</s>,
<ab>perf.</ab> <s>An-a/MSa</s>, and not from the above √ <s>aMS</s>
fictitiously formed to serve as root), a share, portion, part, party
<info lex="m"/>

```

| Block | Realisation | Semantic role |
|---|---|---|
| F01 header | `<L>10<pc>1,1<k1>aMSa<k2>a/MSa<e>1` | S1, S2 (accent in `<k2>`) |
| F02 display headword | `<s>a/MSa</s>` | S2 |
| F03 homophone | `<hom>1.</hom>` (referring to root `aś`) | S1 |
| F04 grammatical cat. | `<lex>m.</lex>` | S3 |
| F06 etymology root | `<ab>fr.</ab> √ <s>aS</s>` | S4 |
| F08 inflection form | `<s>An-a/MSa</s>` (the perfect) | S2 (inflection) |
| F09 editorial commentary | "(probably … fictitiously formed to serve as root)" | S4 + S8 |
| F10 sense gloss | "a share, portion, part, party" | S5 |
| F17 machine annotation | `<info lex="m"/>` | M |

**Blocks present: 9.** Tier T5. The editorial commentary block here is **classic MW** — interpolated reasoning rejecting the kosha derivation (Sample A) in favour of an IE-comparable one. Note the absence of F07 (`<lang>`) on this entry despite the etymology — the IE cognates for *aṃsa* "shoulder" appear at [L92.1](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L307), a separate entry.

### Sample C: Compound sub-entry — [L57 *aṃśu-jāla*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L199) (T3 Typical)

```
<L>57<pc>1,2<k1>aMSujAla<k2>aMSu—jAla<e>3
<s>aMSu—jAla</s> ¦ <lex>n.</lex> a collection of rays, blaze of light.
<info lex="n"/>

```

| Block | Realisation | Semantic role |
|---|---|---|
| F01 header | `<L>57<pc>1,2<k1>aMSujAla<k2>aMSu—jAla<e>3` | S1, S2 |
| F02 display headword | `<s>aMSu—jAla</s>` | S2 |
| F04 grammatical cat. | `<lex>n.</lex>` | S3 |
| F10 sense gloss | "a collection of rays, blaze of light" | S5 |
| F17 machine annotation | `<info lex="n"/>` | M |

**Blocks present: 5.** Tier T2/T3 boundary. **No citation** (F12 absent), **no etymology** (F06 absent), **no encyclopedic block** (F14/F15 absent). The em-dash in `<k2>` does carry compound-segmentation information — this is *structural* in F01 itself, not a separate block.

### Sample D: IE-etymological — [L92.1 *aṃsa*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L307) (T5 Elaborate)

```
<L>92.1<pc>1,2<k1>aMsa<k2>aMsa<e>2E
<s>aMsa</s> ¦ [<ab>cf.</ab> <lang>Goth.</lang> <etym>amsa</etym>;
<lang>Gk.</lang> <gk>ὦμος</gk>, <gk>ἄσιλλα</gk>;
<lang>Lat.</lang> <etym>humerus</etym>, <etym>ansa</etym>.]

```

| Block | Realisation | Semantic role |
|---|---|---|
| F01 header | `<L>92.1<pc>1,2<k1>aMsa<k2>aMsa<e>2E` | S1, S2 |
| F02 display headword | `<s>aMsa</s>` | S2 |
| F07 IE cognate | `<lang>Goth.</lang> <etym>amsa</etym>; <lang>Gk.</lang> <gk>ὦμος</gk> …` | S4 (comparative) |
| F09 editorial commentary | the entire `[…cf.…]` block is editorial | S4 + S8 |
| F16 cross-reference | `<ab>cf.</ab>` ("compare") | S8 |

**Blocks present: 5.** Tier T2/T3. Note the absence of F10 (sense gloss) — this entry exists *purely* to carry IE cognates; the gloss "shoulder" appears at a different L-record. This is **the IE-etymological article type** and it has its own atypical block profile.

### Sample E: Botanical — [L72 *aṃśu-matī*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L244) (T4 Rich)

```
<L>72<pc>1,2<k1>aMSumatI<k2>aMSu—ma/tI<e>3B
¦ <bot>Hedysarum Gangeticum</bot>, <ls>Suśr.</ls><info lex="inh"/>

```

| Block | Realisation | Semantic role |
|---|---|---|
| F01 header | `<L>72<pc>1,2<k1>aMSumatI<k2>aMSu—ma/tI<e>3B` | S1, S2 (with accent + compound) |
| F10 sense gloss | (the `<bot>` content doubles as the gloss) | S5 + S7 |
| F12 source citation | `<ls>Suśr.</ls>` (Suśruta-Saṃhitā, medical) | S6 |
| F14 botanical | `<bot>Hedysarum Gangeticum</bot>` | S7 (encyclopedic) |
| F17 machine annotation | `<info lex="inh"/>` (inherited from parent *aṃśumat*) | M |

**Blocks present: 5.** Tier T3. Note the genre alignment: botanical entries are typically cited from **medical texts** (Suśruta) rather than literary works. F02 (display headword) is suppressed — `<bot>` itself is the display. F04 absent — the `<info lex="inh"/>` tells the renderer to inherit the parent's `<lex>f.</lex>`.

### Sample F: Biographical — [L830 *agastya-mārga*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L2997) (T4 Rich)

```
<L>830<pc>4,3<k1>agastyamArga<k2>agastya—mArga<e>3
<s>agastya—mArga</s> ¦ <lex>m.</lex> the path of <s1>Agastya</s1>
(<bio>Canopus</bio>), <ab>i.e.</ab> the South.

```

| Block | Realisation | Semantic role |
|---|---|---|
| F01 header | `<L>830<pc>4,3<k1>agastyamArga<k2>agastya—mArga<e>3` | S1, S2 |
| F02 display headword | `<s>agastya—mArga</s>` | S2 |
| F04 grammatical cat. | `<lex>m.</lex>` | S3 |
| F10 sense gloss | "the path of … i.e. the South" | S5 |
| F15 biographical | `<s1>Agastya</s1>`, `<bio>Canopus</bio>` | S7 |

**Blocks present: 5.** Tier T3. **Two biographical entities**: the proper-name Sanskrit `<s1>Agastya</s1>` (the sage) and the astronomical `<bio>Canopus</bio>` (the star). This dual encoding is **how MW links Sanskrit mythology to Western astronomy** — a knowledge-bridging move worth flagging in any framework analysis.

### Sample G: Lexicographer-only — [L8 *a-ṛṇin*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L49) (T2 Compact)

```
<L>8<pc>1,1<k1>afRin<k2>a-fRin<e>1
<s>a-fRin</s> ¦ <lex>mfn.</lex> free from debt, <ls>L.</ls><info lex="m:f:n"/>

```

| Block | Realisation | Semantic role |
|---|---|---|
| F01 header | `<L>8<pc>1,1<k1>afRin<k2>a-fRin<e>1` | S1, S2 |
| F02 display headword | `<s>a-fRin</s>` | S2 |
| F04 grammatical cat. | `<lex>mfn.</lex>` | S3 |
| F10 sense gloss | "free from debt" | S5 |
| F12 source citation | `<ls>L.</ls>` | S6 |
| F13 hedge L. | same — sole citation is L. | S6 (hedged) |
| F17 machine annotation | `<info lex="m:f:n"/>` | M |

**Blocks present: 6.** Tier T3. The **minimal lex-only article**: 1 sense, 1 citation, that citation is `L.`. There are 38,414 such entries — 13% of MW.

### Sample H: Continuation — [L11 *áṃśa* sub-entry](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L58) (T1 Vestigial)

```
<L>11<pc>1,1<k1>aMSa<k2>a/MSa<e>1A
¦ partition, inheritance.

```

| Block | Realisation | Semantic role |
|---|---|---|
| F01 header | `<L>11<pc>1,1<k1>aMSa<k2>a/MSa<e>1A` | S1, S2 |
| F10 sense gloss | "partition, inheritance" | S5 |

**Blocks present: 2.** Tier T1 (Vestigial). Note F02 (display headword) is **absent** — the continuation inherits its headword from the preceding `<e>1` entry [L10](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L55). This **headword-suppression** is a defining feature of `<e>1A`: 66.1% of continuation entries lack F02 (1 − 33.9% from the matrix).

---

## 7 · Block co-occurrence patterns

The 20 most frequent block-pairs across the first 50K entries:

| Block 1 | Block 2 | Co-occurrences |
|---|---|--:|
| header | sense_gloss | 48,222 |
| header | machine_annotation | 47,490 |
| machine_annotation | sense_gloss | 46,833 |
| display_headword | header | 37,523 |
| display_headword | sense_gloss | 37,513 |
| display_headword | machine_annotation | 36,258 |
| header | source_citation | 33,875 |
| sense_gloss | source_citation | 33,868 |
| machine_annotation | source_citation | 33,372 |
| grammatical_category | header | 31,953 |
| grammatical_category | sense_gloss | 31,952 |
| grammatical_category | machine_annotation | 31,770 |
| display_headword | grammatical_category | 29,846 |
| display_headword | source_citation | 26,345 |
| grammatical_category | source_citation | 22,797 |
| display_headword | inflection_form | 11,187 |
| header | inflection_form | 11,187 |
| inflection_form | sense_gloss | 11,186 |
| inflection_form | machine_annotation | 10,437 |
| inflection_form | source_citation | 8,261 |

**The "core quintet"** — F01 + F02 + F04 + F10 + F17 (header / display / grammar / sense / machine-annotation) — is present in the modal entry. Adding F12 (source) gives the T3 typical article. The remaining 13 blocks are *optional* in the sense that no single one is required, but at least one is usually present.

---

## 8 · Cross-references to docs-pass material

This working notes file *depends on* and *extends* the existing docs-pass content:

- [DICT_PROFILE.md Article types](../../DICT_PROFILE.md#article-types--what-youll-encounter) — typology source
- [DICT_PROFILE.md Citation markers](../../DICT_PROFILE.md#citation-markers--not-all-are-literary-works) — F13 analysis
- [DICT_PROFILE.md Lineage: WIL ← Koshas](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) — F13 as MW's editorial invention vs PWG
- [ENTRY_GUIDE.md Entry hierarchy](../../ENTRY_GUIDE.md#entry-hierarchy-distribution) — `<e>` distribution
- [ENTRY_GUIDE.md Entry-type breakdown](../../ENTRY_GUIDE.md#entry-type-breakdown-by-content) — `<lex>` counts
- [ENTRY_GUIDE.md Coverage of `<ls>`](../../ENTRY_GUIDE.md#coverage-of-ls-citations) — F12 evidentiary stats
- [DATA_DICTIONARY.md](../../DATA_DICTIONARY.md) — formal tag inventory

---

## 9 · Open analytical questions (for the paper)

1. **Are the 8 primary article types categorically distinct, or a gradient?** Wiegand's microstructure types might suggest categorical; the data (entries fluidly satisfy multiple primary types when type-membership is computed without precedence rules) might suggest gradient. The refactor in §3 promotes the three most-overlap-prone "types" (Vedic-accented, lexicographer_only, etymological_ie) to *properties*, partly resolving the overlap question by design rather than by data analysis.

2. **What is F17's status?** Is `<info>` part of the microstructure (a structural indicator in Wiegand's sense) or is it metadata about the microstructure?

3. **Is F13 (the L. hedge) a *citation* or a *commentary*?** Functionally it's both — formally it's an `<ls>`, but semantically it shifts the entire entry's evidentiary weight. PWG handles this differently (named-kosha citations) — see [Lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg).

4. **Continuation entries (`<e>1A`, T1 Vestigial)** — are they entries at all in the lexicographic sense, or are they sub-articles within a larger article? Different frameworks answer differently.

5. **The 1.4% of T5 Elaborate entries (10+ blocks)** — what fraction of dictionary *usage* do they account for? These are likely the high-traffic lemmas (*ātman*, *karma*, *dharma*, *bhakti*, …) and account for far more than 1.4% of consultations. Hypothesis testable against query logs if available.

6. **F18 correction records** — virtually zero in mw.txt. Are corrections happening exclusively in the issue-tracker rather than in-file? Cross-reference [ROADMAP.md velocity note](../../ROADMAP.md#status-snapshot-2026-06-12).

---

*Last computed: 2026-05-23 against [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt). Python source: `/tmp/mw_block_matrix.py` in [the docs-pass build artifacts](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass).*
{% endraw %}
