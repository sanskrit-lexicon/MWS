# Reading *Monier-Williams 1899* with Atkins & Rundell: a practical-lexicography microanalysis

> **Supplementary extended draft — superseded by [PAPER.md](PAPER.md).** One of four single-framework drafts consolidated into the single submission paper per [DOUBTS.md D4](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking). This Atkins-Rundell reading is condensed into [PAPER.md Appendix B](PAPER.md#appendix-b--the-atkins-rundell-practical-lexicography-reading-condensed); this fuller draft is retained as supplementary material only. **For the canonical paper, read [PAPER.md](PAPER.md).**

**Draft for the [*International Journal of Lexicography*](https://academic.oup.com/ijl) (Oxford University Press).** ~7.5K words target.

**Theoretical framing:** Atkins & Rundell, *The Oxford Guide to Practical Lexicography* (2008). One of four parallel framework analyses — see [README](README.md). Data source: [MICROANALYSIS.md](MICROANALYSIS.md).

---

## Abstract

This paper reads the *Monier-Williams Sanskrit-English Dictionary* (1899) through the lens of Atkins & Rundell's *Practical Lexicography* (2008). Treating the digital CDSL edition of MW as a finished lexicographic product, we ask: what design decisions does the *Practical Guide* framework let us recover from the artefact? We examine MW's **headword list policy** (286,561 entries, 44% of them compounds — a deliberate over-enumeration vs the German PWG source); its **sense-division** practice (numbered/lettered sub-senses, often with the "9 continuation senses" cluster pattern); its **definition style** (terse English glosses with embedded etymological reasoning); its **example policy** (citations as locators, not as quoted examples — a sharp departure from modern English dictionaries); and its **syntactic-pattern recording** (verb class, voice, gender). MW emerges as a **scholarly retrieval dictionary** — Atkins & Rundell's term for a reference work optimised for the user already familiar with the language; not a production dictionary; not a learner's dictionary. We argue that several of MW's apparently archaic features (the `<ls>L.</ls>` lexicographer-hedge in 13.4% of entries; the 84.9% bare-work citations without coordinate; the suppression of glosses on continuation entries) are *coherent design choices* under this typology, even where Atkins & Rundell's prescriptions for modern dictionaries would reject them.

**Keywords:** practical lexicography, Atkins, Rundell, dictionary design, Monier-Williams, Sanskrit lexicography, CDSL, headword inventory, sense division

---

## 1. Why Atkins & Rundell on Monier-Williams?

Atkins & Rundell's *Oxford Guide to Practical Lexicography* (2008) is the standard manual for the modern dictionary maker. It is **a designer's handbook** — its 540 pages walk through the decision-tree a lexicographer faces, from corpus design through final proofing. It is also **defiantly modern**: its target reader is a 21st-century team building a learner's dictionary or a high-end monolingual on a digital platform. MW1899 is none of these things — it is a 125-year-old scholarly reference for an extinct audience, in a target-language register no working lexicographer would now adopt, with a citation discipline that contradicts most of A&R's prescriptions.

This is precisely why the framework is useful. Atkins & Rundell offer a vocabulary for naming and rating lexicographic *choices* — and MW's choices are crisp, consistent, and recoverable from the digital edition. Applying the framework backwards — from finished product to inferred design decision — lets us read MW as a coherent system rather than as a curiosity. Where A&R's prescriptions and MW's practice diverge, we get to see what 19th-century scholarly Sanskrit lexicography assumed about its readers.

The data source for this paper is our companion [working notes](MICROANALYSIS.md), built from the [CDSL `mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) digital edition (286,561 records).

## 2. The framework in brief

Atkins & Rundell organise the lexicographer's work into six broad design decisions (A&R 2008, ch. 3):

1. **Corpus and headword inventory** — what lemmas does the dictionary cover?
2. **Sense division** — how do you slice a polysemous word into senses?
3. **Definition writing** — what kind of definition (full sentence? gloss? translation equivalent?)
4. **Example provision** — illustrative phrases, real or invented.
5. **Syntactic and lexical patterns** — grammatical info; collocations.
6. **Encyclopedic and pragmatic content** — proper names, register, domain.

We work through MW against each in turn.

## 3. Headword inventory: a deliberate over-enumeration

A&R devote chapter 4 to **headword selection**. Their criterion is **user-need**: include a word if and only if a likely user will look for it. For learner dictionaries, this typically means 30K–80K headwords. For unabridged monolinguals, 200K–500K is common. MW's [286,561 records](../../ENTRY_GUIDE.md#entry-hierarchy-distribution) puts it in the unabridged-monolingual range — but the internal composition is unusual.

| Article type | Count | % of total | Comparable in A&R typology |
|---|--:|--:|---|
| Top-level main lemmas (`<e>1`) | 32,116 | 11.2% | "Standard headwords" |
| Top-level variants (`<e>1B/C`) | 10,858 | 3.8% | "Variant spellings" |
| Continuation senses (`<e>1A`) | 9,294 | 3.2% | "Sub-senses with their own record" |
| Derived forms (`<e>2/2A/2B/2C/2E`) | 72,118 | 25.2% | "Run-on derivatives" |
| Compounds (`<e>3/3A/3B/3C`) | 144,449 | 50.4% | **Atypical — see below** |
| Specialised (`<e>4*`) | 17,711 | 6.2% | Rare in modern dicts |

The striking number is **50.4% compounds**. A&R explicitly note (2008, p. 168) that modern dictionaries cover compounds via **run-on entries** under the parent or via **multi-word expressions** (MWEs) — not as full standalone entries. MW's compound treatment is **the opposite policy**: every compound gets its own `<L>` record, its own `<lex>`, its own gloss, its own (where applicable) `<ls>` citation. The em-dash in `<k2>` (`aMSu—jAla`) is the structural cue.

Why? Two interrelated reasons:

(a) Sanskrit is famously agglutinative — long compounds (six, ten, sometimes twenty members) are productive and frequent. A&R-style sub-entries would explode the parent article. MW's enumeration policy is a **scalability** decision.

(b) MW's source PWG also enumerates compounds, but not as systematically; we calculated in our [Beyond PWG analysis](../../DICT_PROFILE.md#beyond-pwg--what-mw-contributes) that MW has 2.3× as many records as PWG, and the compound count is the chief contributor. MW's editorial discipline was *systematic* compound enumeration where PWG was selective.

In A&R terms: MW exhibits a **maximally explicit headword inventory policy** for compounds. This is consistent with A&R's principle of *user-need* — but only if the user is an academic Sanskritist who needs every compound found and indexed, not a learner who needs the productive lexicon.

## 4. Sense division: the 9-continuation pattern

A&R's chapter 6 ("Splitting") discusses how to divide a polysemous word into senses. The fundamental tension is between **lumping** (one entry, many senses inside) and **splitting** (multiple entries). A&R recommend lumping for learners (fewer senses, more memorable) and splitting for scholars (each nuance gets its own treatment).

MW uses a **distinctive mixed strategy**: the polysemous lemma gets a single `<e>1` entry **and** a tail of `<e>1A` continuation entries. The paradigmatic case is [L10 *áṃśa*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L55), whose principal sense ("a share, portion, part, party") sits at `<L>10` and whose nine further senses ([L11–L19](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L58-L82)) follow as separate `<L>` records with `<e>1A`. The continuation senses extend *áṃśa* to: partition, share of booty, earnest money, stake (with `<ls>RV. v, 86, 5</ls>`), a lot, fraction denominator, latitude degree, day, and the proper name of an Āditya.

This is **neither lumping nor splitting in A&R's sense** — it is a *third* option: physically separate sub-entries that share a headword and rely on adjacency for cohesion. The 9,294 `<e>1A` entries in mw.txt all follow this pattern.

A&R do not have a term for this. We propose **adjacency-sub-entries** as the most economical name. Their characteristics, recoverable from the matrix in [MICROANALYSIS.md §4](MICROANALYSIS.md):

- **Display headword suppressed in 66.1% of cases** (only 33.9% retain `<s>`).
- **Grammatical category suppressed in 99.7%** (inheriting from the parent `<e>1`).
- **`<info>` machine-annotation present in 98.6%** (each is still a self-contained record for tooling).
- **Average fullness 4.76 of 18 blocks** — the lowest of any article type.

The adjacency-sub-entry is **the most distinctive design decision** A&R's framework lets us see in MW. It produces a sense-division apparatus that is *visually compact* in print (the senses cascade down the column) but *fully indexed* for digital retrieval (each gets its own record). It is, in retrospect, a remarkable forward-compatibility with the digital edition; perhaps not by design.

## 5. Definition style: the embedded etymology

A&R's chapter 7 distinguishes three definition styles:

- **Full-sentence definition** (typical of learner dictionaries: "*aṃśa*: a portion or share, especially of an inheritance").
- **Analytic definition** (Aristotelian genus-and-differentia: "A part; especially, a part allotted or received").
- **Translation equivalent** (the bilingual norm: "*aṃśa* = share, portion, part, party").

MW uses the **third** style — comma-separated translation equivalents — almost exclusively. From the [L10 entry](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L55):

> *aṃśa*: m. (probably fr. √ 1. *aś*, perf. *ān-áṃśa*, and not from the above √ *aṃś* fictitiously formed to serve as root), **a share, portion, part, party**.

The bold portion is the definition. The parenthetical that precedes is **embedded etymology** — what would, in a modern dictionary, be a separate `[Etym]` field. MW interweaves it into the definition body. This is a 19th-century practice that A&R explicitly recommend against (2008, p. 263): "Etymology should be a separable field that the user can ignore if they wish."

But MW's choice is consistent within itself. The [Article-type matrix](MICROANALYSIS.md) shows that **F09 editorial commentary** (the parenthetical block) is concentrated in two article types:

- **Verbal root**: 78.1% — almost every root has an editorial comment.
- **IE-etymological entry**: 38.4%.

Elsewhere F09 runs at 3–10%. The embedded-etymology habit is **not pervasive**; it is concentrated where philological reasoning matters most. A&R would still flag the practice as *inconsistent* — F09 should be its own field — but MW's choice has **internal logic**: comment where commentary is necessary, suppress where it is not.

## 6. Examples: citations are locators, not quotations

A&R chapter 8 is the longest in the book: it argues that **illustrative examples** are the heart of a modern dictionary. Modern English dictionaries (LDOCE, OALD, Collins COBUILD) all carry quoted or constructed examples for each sense.

MW carries **none**. The [311,932 `<ls>` citations](../../ENTRY_GUIDE.md#coverage-of-ls-citations) in mw.txt are **locators**, not quotations: they tell the user *where to look* in the cited text but do not reproduce the citing passage. Of those 311,932 citations:

- 15.1% carry a numeric coordinate (`<ls>RV. v, 86, 5</ls>` — book / hymn / verse).
- 84.9% are bare work-citations (`<ls>RV.</ls>` — just the work).

A user wanting to *see* the citing passage must consult the printed text of the cited work. This was sensible practice in 1899, when an academic Sanskritist owned (or had library access to) the Rigveda and the Mahābhārata. It is **defective practice** by A&R's standards: the user-burden is too high; modern dictionaries integrate the cited passage.

But MW's omission has a hidden benefit: it makes the dictionary much smaller than it would otherwise be (a constant problem for unabridged Sanskrit dictionaries, where the cited literature itself runs to thousands of pages). A&R-style example provision would have made MW unprintable as a single volume. The choice was practical.

The exception worth noting: the **lexicographer-hedge `<ls>L.</ls>`** — present in [40,213 citations (12.9% of all citations)](../../DICT_PROFILE.md#citation-markers--not-all-are-literary-works) — is **not a locator at all**. It is a *meta-annotation*: "this sense exists in the indigenous lexica only." In A&R's terms, this is a **register marker** — closer to *archaic* or *literary* than to a citation. We return to it in §8 below.

## 7. Syntactic and lexical patterns

A&R chapter 9 emphasises that a dictionary entry should record **the patterns** in which a word participates: subcategorisation, collocations, semantic preferences. MW records four:

- **Verb class** (`<ab>cl.</ab> N` — class 1 through 10, the Pāṇinian *gaṇas*) — present in 98.4% of verbal-root entries.
- **Voice** (`<ab>P.</ab>` Parasmaipada, `<ab>Ā.</ab>` Ātmanepada) — co-present with class.
- **Gender** (`<lex>m.</lex>` / `<lex>f.</lex>` / `<lex>n.</lex>` / `<lex>mfn.</lex>`) — present in 100% of noun and adjective entries.
- **Sub-categorisation** (`<ab>ifc.</ab>` in fine compositi, `<ab>ibc.</ab>` in initio compositi) — for compound positioning.

The first three are *grammatical-class indicators*; the fourth is **collocational** in A&R's sense (it tells the user that a particular word appears at the end of compounds). But MW provides **no other collocational information** — no examples of typical noun-verb pairings, no patterns of co-occurrence with other lexemes. A&R would mark this as a major gap in a modern dictionary. For MW it is consistent with the *retrieval dictionary* design type discussed below.

## 8. Pragmatic content: `L.` as register marker

We have already noted (§6) that `<ls>L.</ls>` is unusual. A&R offer a vocabulary for it: it is a **pragmatic register marker** — a tag attached to a sense that says something about the *kind of evidence* underlying it. In modern dictionaries register markers include *archaic*, *literary*, *colloquial*, *technical*, *taboo*, etc. MW's `L.` is a **register marker of a very particular type**: the *koshic-only* register.

A word marked `L.` carries the implicit pragmatic note: *"This word is recorded in the indigenous Sanskrit lexicons (Amarakośa, Hemacandra's Abhidhānacintāmaṇi, Halāyudha's Abhidhānaratnamālā, etc.) but has not been found in any published Sanskrit text."* The lexicographer-hedge is therefore both an evidential marker (no textual citation) AND a register marker (specifically: of the lexicographic tradition).

Its [distribution across article types](MICROANALYSIS.md):

- **100%** of lexicographer-only articles (by definition).
- **71.5%** of botanical articles — most plant names exist only in kosha/medical-text identifications.
- **64.7%** of biographical articles — many minor mythological figures are kosha-attested only.
- **21.1%** of continuation sub-entries — extension senses often have weaker evidence than main senses.

The `L.` register marker is therefore **strongly type-bound** — its incidence varies from 0.4% in "other" entries to 100% in the lexicographer-only type. This is exactly the kind of *register-distribution profile* A&R recommend tracking (2008, p. 386). MW does the tracking implicitly, via the marker's presence/absence; a modern reissue would expose it as a field-level register tag.

## 9. The retrieval dictionary

Atkins & Rundell distinguish (2008, ch. 3 §3.4) two macro-types of dictionary:

- **Production dictionary** — for users encoding (writing/speaking) in the target language. Needs collocational info, examples, register, usage notes.
- **Reception / retrieval dictionary** — for users decoding (reading) in the target language. Needs comprehensive coverage, etymological precision, source attribution.

**MW is a retrieval dictionary.** Every design choice we have reviewed makes sense under this rubric:

- Headword inventory maximally explicit (compounds enumerated) — for the user trying to *find* a compound, not produce it.
- Definition style: translation-equivalent — for fast English lookup.
- No examples — examples are for production, not retrieval.
- Citations as locators — point the user to the cited text for further reading.
- Verb class + voice + gender — needed for decoding the inflected forms.

A&R note that retrieval dictionaries are **declining as a category** in modern lexicography (replaced by online corpus-search tools). MW is one of the largest and most influential surviving examples.

## 10. What modern lexicography would change

If a modern team were to revise MW1899 along A&R's prescriptions, the high-impact changes would be:

1. **Add real examples** — quoted passages from RV/MBh/Pāṇ etc. for the principal senses. This is now technically possible via [GRETIL](http://gretil.sub.uni-goettingen.de/) and DCS corpora.
2. **Separate etymology from definition** — move the parenthetical `(probably fr. √…)` into a dedicated `<etym>` field.
3. **Convert `<ls>L.</ls>` into named-kosha citations** — replace the binary hedge with the specific kosha source (recovering PWG's discipline). [The lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) discusses why this matters.
4. **Add collocational data** — verb-noun pairings extracted from the digitised corpus.
5. **Modernise the gloss register** — many MW glosses ("an ascetic", "a ritual sacrifice") use 19th-century English that has shifted register.
6. **Re-evaluate the compound-enumeration policy** — perhaps too much for modern users; merge transparent compounds into run-on lists under their parents.

Each of these is *technically tractable* with the digital edition. None is *editorially trivial* — they require sustained scholarly judgement at the entry level.

## 11. Conclusion

Read through Atkins & Rundell, MW1899 emerges as a **maximally explicit retrieval dictionary** — a scholarly reference work whose design choices are internally consistent and, for its time and user, well-calibrated. The areas where MW *diverges* from A&R's prescriptions (no examples, embedded etymology, locator-only citations, kosha-hedge instead of named-source) are not arbitrary archaisms but **coherent design decisions under the retrieval-dictionary brief**. The areas where MW *anticipates* later best practice (the `<e>1A` adjacency-sub-entry pattern, the systematic compound enumeration, the `<info>` machine annotation) are remarkable for a 1899 work and account for MW's continued utility as a digital-era reference.

A working modern revision of MW would need to retain the retrieval-dictionary architecture while addressing the example-and-corpus gap. The [CDSL digital edition](https://www.sanskrit-lexicon.uni-koeln.de/) is the platform on which such a revision is now feasible.

---

## References (selected)

- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Hanks, P. (2013). *Lexical Analysis: Norms and Exploitations*. MIT Press.
- Hartmann, R. R. K. (2001). *Teaching and Researching Lexicography*. Pearson.
- Monier-Williams, M. (1899). *A Sanskrit-English Dictionary*. 2nd edn. Oxford: Clarendon Press.
- Rundell, M. (2014). *Building a New Corpus of Indian English*. In *Proceedings of the XVI Euralex International Congress*.
- Schreyer, R. (1985). *Sanskrit Dictionary-Making: A Critical Bibliography of the European Tradition*. Brill.

---

*Source data: [MICROANALYSIS.md](MICROANALYSIS.md). Companion framework papers: [Wiegand](paper-wiegand.md) · [Hausmann-Wiegand](paper-hausmann.md) · [Grounded](paper-grounded.md). All four analyse the same MW1899 dataset through different theoretical lenses.*
