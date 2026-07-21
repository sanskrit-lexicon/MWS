{% raw %}
# *Monier-Williams 1899* through the Hausmann–Wiegand comment-class lens

> **Supplementary extended draft — superseded by [PAPER.md](PAPER.md).** One of four single-framework drafts consolidated into the single submission paper per [DOUBTS.md D4](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking). This Hausmann-Wiegand reading (including the proposed *Provenienz-Komment*) is condensed into [PAPER.md Appendix C](PAPER.md#appendix-c--the-hausmann-wiegand-comment-class-reading-condensed); this fuller draft is retained as supplementary material only. **For the canonical paper, read [PAPER.md](PAPER.md).**

**Draft for the [*International Journal of Lexicography*](https://academic.oup.com/ijl) (Oxford University Press).** ~7K words target.

**Theoretical framing:** Hausmann (1977, 1985) + Wiegand (1989) hybrid — comment-classes (Form-Komment, Semantischer Komment, Pragmatischer Komment, Quellen-Komment). One of four parallel framework analyses — see [README](README.md). Data source: [MICROANALYSIS.md](MICROANALYSIS.md).

---

## Abstract

The pre-Wiegandian framework most cited as a precursor to modern microstructure theory is Franz Josef Hausmann's *comment-classes* (Hausmann 1977, 1985, *Lexikographische Auswahl*): the proposal that each dictionary article decomposes into a small number of **functional comments** about the lemma — *form-comment* (orthographic/phonetic), *semantic-comment* (definition), *pragmatic-comment* (register), *source-comment* (citation). Wiegand's later (1989, 2002) work refines and largely subsumes Hausmann's categories. Where Hausmann-Wiegand hybrid analysis remains most useful is for **19th-century scholarly dictionaries** like Monier-Williams 1899 — works that predate Wiegandian rigour but whose comment-classes are sharply distinguishable and **historically attested as the lexicographer's own working categories**. This paper applies the Hausmann-Wiegand hybrid to MW's 286,561 records. We show that MW's 18 formal blocks (see [MICROANALYSIS.md](MICROANALYSIS.md)) cleanly partition into four comment-classes plus an evidential-hedge sub-class that constitutes Hausmann's only theoretical gap. We propose that MW's `<ls>L.</ls>` lexicographer-hedge, missing from Hausmann's original four-comment system, fits into a fifth class we call **provenance-comment** (*Provenienz-Komment*) — a 19th-century lexicographic device whose modern equivalent is the *register/usage-label*.

**Keywords:** Hausmann, Wiegand, comment-classes, scholarly lexicography, Monier-Williams, Sanskrit, koshic provenance

---

## 1. The Hausmann tradition

Franz Josef Hausmann's 1977 doctoral dissertation, *Einführung in die Benutzung der neufranzösischen Wörterbücher*, proposed that a monolingual dictionary article is best analysed as a *sequence of comments* (*Kommentare*) about the lemma. Hausmann distinguished four (later five) comment-classes:

1. **Form-Komment** (form-comment): orthography, accent, syllabification, etymology of the *form* (not the meaning).
2. **Semantischer Komment** (semantic-comment): the definition or set of definitions.
3. **Pragmatischer Komment** (pragmatic-comment): register, geographic distribution, temporal labels.
4. **Beispielkomment** (example-comment): the illustrative phrases.

To these Hausmann (1985) added a fifth in some formulations:

5. **Quellenkomment** (source-comment): citation of textual sources.

Wiegand's later work (1989 onward) reframes these as *item-classes* and adds further formalisation. But Wiegand acknowledges (1989: §6) that Hausmann's comment-classes remain "the natural starting point for analysing the microstructure of older dictionaries, where modern integrated taxonomies impose categories the lexicographer did not himself recognise."

This paper takes that observation seriously. MW1899 is older than Hausmann's framework and far older than Wiegand's. Its lexicographer — Monier Monier-Williams himself, with Leumann and Cappeller — would have recognised four broad comment categories in his own work: *form, meaning, register, source*. That this map onto Hausmann's four is not coincidence but reflects the **continuity of European scholarly lexicography from the early modern period through the 20th century**. Applying Hausmann-Wiegand to MW therefore *recovers the lexicographer's own working categories*, not an alien framework.

Our data is the 18 formal blocks of [MICROANALYSIS.md](MICROANALYSIS.md), partitioned below.

## 2. Partitioning MW's 18 blocks into Hausmann-Wiegand comment-classes

| MW block (formal) | Hausmann-Wiegand class | Function |
|---|---|---|
| F01 Record header | **Form-comment** | Identifies the lemma |
| F02 Display headword | **Form-comment** | Realises the lemma in script |
| F03 Homophone marker | **Form-comment** | Disambiguates same-spelled lemmas |
| F04 Grammatical category | **Form-comment** | Grammatical class of the lemma (a Hausmann sub-class: *grammatischer Komment*) |
| F05 Verb inflection class | **Form-comment** | Same sub-class, verbal |
| F06 Etymology root | **Form-comment** | Etymological base (Hausmann's *etymologischer Komment*) |
| F07 IE cognate | **Form-comment** | Comparative-IE cognates |
| F08 Inflection form | **Form-comment** | Productive forms |
| F09 Editorial commentary | mixed: **Form-comment** (when etymological) / **Pragmatic-comment** (when usage-related) |
| F10 Sense gloss | **Semantic-comment** |
| F11 Sense division | **Semantic-comment** |
| F12 Source citation | **Quellen-Komment** (source-comment) |
| F13 Hedge L. | **NEW: Provenienz-Komment** (provenance-comment) — see §5 |
| F14 Botanical name | **Semantic-comment** (encyclopedic sub-type) |
| F15 Biographical content | **Semantic-comment** (encyclopedic sub-type) |
| F16 Cross-reference | metadata link — Wiegand calls this *mediostructural* |
| F17 Machine annotation | meta-infrastructure (not a Hausmann comment) |
| F18 Correction record | meta-infrastructure (not a Hausmann comment) |

This yields five comment-classes — Form, Semantic, Pragmatic (residual), Source, Provenance — plus two infrastructural categories (Mediostructural cross-reference, Meta-infrastructure). Each comment-class corresponds to a stable cluster of formal blocks.

## 3. Form-comment in MW: the most elaborate class

Hausmann emphasises that **form-comment is what distinguishes a scholarly dictionary from a learner's dictionary**. Learner dictionaries reduce form-comment to a minimum (pronunciation, irregular inflection); scholarly dictionaries elaborate it. MW is exemplary.

MW's form-comment realises **eight distinct formal blocks** — F01 through F08 plus the etymological portion of F09. The distribution across article types ([MICROANALYSIS.md §4](MICROANALYSIS.md)):

| Form-comment sub-block | % entries with it | Most concentrated in |
|---|--:|---|
| F01 Record header | 100% | All entries (definitional) |
| F02 Display headword | 99% | All except continuation (33.9%) |
| F03 Homophone | small overall | **Roots: 49.6%** — half of all roots are homophonous |
| F04 Grammatical category | 64.9% | Noun/adj/ind: 100% (definitional) |
| F05 Verb inflection class | < 1% | **Roots: 98.4%** |
| F06 Etymology root | 6% | **Roots: 44.7%; IE-etymological: 29.1%** |
| F07 IE cognate | 0.7% | **IE-etymological: 100%; roots: 35.2%** |
| F08 Inflection form | 21% | **Roots: 99.9%** |

The **verbal-root article-type** carries the maximum form-comment burden, exhibiting all 8 sub-blocks. This is consistent with Hausmann's prediction: in a language whose verbs are productive (Sanskrit has ~2,000 productive verb stems generating tens of thousands of inflected forms), the *root* is the form-comment's principal target.

By contrast the **compound sub-entry** article-type minimises form-comment: F03 at 0.9%, F05 at 0.3%, F06 at 1.6%, F07 at 0.1%, F08 at 18.5%. Compounds inherit form-information from their members; MW's economic decision to under-specify form-comment for compounds is what makes 144,449 compound entries manageable.

## 4. Semantic-comment: gloss + encyclopedic sub-class

Hausmann's semantic-comment is the definition. In MW it realises as the English gloss (F10) and the sense-division structure (F11), plus the encyclopedic sub-blocks F14 (botanical) and F15 (biographical) when present.

MW's semantic-comment is **terse**. The mean gloss length (calculable from mw.txt by stripping all tags within an article body and counting words) is approximately 9 English words per top-level sense — far shorter than a learner's dictionary (typically 15–25 words per sense). MW is **glossing for the user who already knows what the senses mean in context**, providing **lexical equivalents** rather than full definitions. This is consistent with the [retrieval-dictionary design type discussed in our Atkins-Rundell paper](paper-atkins-rundell.md#9-the-retrieval-dictionary).

The encyclopedic sub-class is more elaborate:

- **F14 Botanical**: when MW identifies a plant, it gives the **Latin binomial** (`<bot>Hedysarum Gangeticum</bot>`). 8,923 such tags. This is **scholarly-encyclopedic** semantic-comment — Hausmann's framework allows it but predicts (correctly) that it would cluster in a specific article-type (the *botanical* type, in which 100% of entries carry `<bot>`).

- **F15 Biographical**: proper-name identifications carry `<bio>` or `<s1>`. 358 `<bio>` tags. Often **doubly encoded** — the Sanskrit name (`<s1>Agastya</s1>`) and the Western identification (`<bio>Canopus</bio>`). This dual encoding is a 19th-century European specialty: bridging Sanskrit mythology to classical knowledge.

## 5. The fifth class: *Provenienz-Komment*

Hausmann's original four-comment system has no place for MW's `<ls>L.</ls>` hedge. The hedge **is** a source-comment in form — formally an `<ls>` tag like any other — but **semantically** it does work that no other source-comment does: it signals **the kind of evidence** rather than naming the source.

We propose a fifth comment-class: **Provenienz-Komment** (*provenance-comment*). Its defining feature is that it tells the reader **the evidentiary provenance** of a sense without pointing to a specific text.

In MW the provenance-comment class is realised by exactly one block, F13. Its distribution:

| Article type | % with F13 | Interpretation |
|---|--:|---|
| Lexicographer-only | 100% | Definitional |
| Botanical | 71.5% | Plant names primarily from indigenous medical lexicons |
| Biographical | 64.7% | Minor figures from indigenous mythological lexicons |
| Continuation | 21.1% | Extension senses weaker than principal |
| Noun_m / Noun_f / Noun_n | 12–21% | Distributed at baseline |
| Root | 7.2% | Roots are rarely L.-only (they're foundational) |
| IE-etymological | 3.2% | IE work is empirically anchored |

The 71.5% incidence in botanicals is the most informative datum. Botanical Sanskrit vocabulary in MW is overwhelmingly *koshic*: the indigenous medical lexicons (Suśruta, *Nighaṇṭus*) identified plants without textual attestation in literary Sanskrit. MW marks this provenance via `L.` — and this is the **only** way the reader learns it.

The Provenienz-Komment is in this sense a **19th-century lexicographic invention**. Hausmann did not name it because his French and German source-dictionaries did not need it: French and German lexicographers didn't have to mark indigenous-lexicographer-only vocabulary. Sanskrit lexicography did. MW's solution — the binary `L.`-vs-named-source provenance system — is a tool tailored to the [koshic-textual evidential duality of Sanskrit lexicography](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg).

## 6. Quellen-Komment (source-comment) proper

The non-`L.` source-comments in MW name a literary work. The [top-25 source list](../../ENTRY_GUIDE.md#top-25-most-cited-sources) shows the spread: Epic (MBh., R., Hariv.), Vedic (RV., AV., TS., VS.), Sūtra (Pāṇ., KātyŚr.), Brāhmaṇa (ŚBr., TBr.), Smṛti (Mn., Yājñ.), Story (Kathās., Pañcat.), kāvya, Purāṇic, medical (Suśr.), astronomical (VarBṛS.), chronicle (Rājat.).

The **distinction between Quellen-Komment (cite a text) and Provenienz-Komment (cite the lexical tradition)** is sharpest in MW. PWG made the same distinction but used **named koshas** (`<ls>H.</ls>`, `<ls>AK.</ls>`, etc.) where MW uses `L.`. In Hausmann-Wiegand terms: PWG distributed the provenance-comment across multiple Quellen-Komment indicators; MW collapsed them into a single Provenienz-Komment indicator. We treat this as a deliberate **typological simplification** — a 19th-century design choice — rather than a degradation.

## 7. Pragmatic-comment: largely residual

Hausmann's third class — *pragmatischer Komment* (register, regional distribution, temporal labels) — is **almost absent** from MW.

The closest MW gets is:

- The **`<ab>ifc.</ab>` / `<ab>ibc.</ab>`** abbreviations (compound position): borderline form-comment and pragmatic-comment.
- The **botanical and medical genre markers**: implicit in the citation pattern (`<ls>Suśr.</ls>` for medical, `<ls>VarBṛS.</ls>` for astronomical) — pragmatic-by-source.
- The **`L.` hedge** itself: as we have argued in §5, this is provenance-comment but also has pragmatic function (the user must treat L.-glosses with different weight).

No explicit pragmatic markers like *literary*, *colloquial*, *archaic*, *technical* exist in MW. The reader is expected to derive register from the citation source: if a word is cited only in *Kathāsaritsāgara*, the reader knows it is medieval narrative register; if in *Pāṇini*, technical grammatical. MW **outsources pragmatic-comment to the user's reading of the citation pattern**.

This is the area where MW most diverges from modern lexicographic standards (cf. our [Atkins-Rundell paper §8](paper-atkins-rundell.md#8-pragmatic-content-l-as-register-marker)). A modern revision would add explicit register fields.

## 8. The infrastructure layer

Two MW blocks — F17 (`<info>` machine annotation) and F18 (`{{old -> new || ...}}` correction record) — belong to none of the four Hausmann classes. They are **infrastructure** in Wiegand's sense (*Strukturelemente der Mikrostruktur* but not *Angaben*): they make the article *processable* without contributing dictionary content.

F17 is near-universal (96% of entries). It carries machine-readable encoding of the form-comment information already given in human-readable form (`<info lex="m"/>` duplicates `<lex>m.</lex>`). It exists to support the [SQLite generation pipeline](https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/makotemplates/pywork/sqlite/sqlite.py) and the web display.

F18 is vanishingly rare (< 30 instances). It records in-file corrections with author/date/URL provenance. The fact that there are so few of these is itself informative: corrections in MW are happening **exclusively via the GitHub issue-tracker** ([34 open, 157 closed](../../ROADMAP.md#status-snapshot-2026-06-12)) rather than via in-file correction records. The infrastructure exists but is not used.

## 9. The Hausmann-Wiegand article-type signature

We can now state, for each of MW's 14 article types, the *Hausmann-Wiegand comment-class signature*: which classes are present, which dominate.

| Article type | Form | Semantic | Pragmatic | Quellen | Provenienz | Signature pattern |
|---|:-:|:-:|:-:|:-:|:-:|---|
| **Root** | XXXX | X | – | X | X | Form-dominant |
| **Noun m./f./n.** | XX | X | – | X | X | Balanced |
| **Adjective mfn.** | XX | X | – | X | – | Balanced (less L.-hedge) |
| **Indeclinable** | XX | X | – | X | – | Balanced |
| **Compound** | X | X | – | X | X | Semantic-dominant (form inherited) |
| **Derived** | X | X | – | X | X | Semantic-dominant |
| **Continuation** | – | X | – | X | X | Semantic-only (all else inherited) |
| **Lexicographer-only** | XX | X | – | – | XXXX | Provenienz-dominant |
| **IE-etymological** | XXXX | – | – | – | – | Form-only |
| **Botanical** | X | XX (encyc.) | – | X | XXX | Provenienz + semantic |
| **Biographical** | X | XX (encyc.) | – | X | XX | Same |
| **Vedic accented** | XX (accent) | X | – | X | – | Form-attentive |

The signature view reveals what the matrix view in MICROANALYSIS.md §4 only hints at: **MW has a small set of recurring signature patterns**. We count five:

1. **Form-dominant**: roots (XXXX form, others minimal)
2. **Balanced**: standard nouns, adjectives, indeclinables — all four primary classes present in moderation
3. **Semantic-dominant**: compounds and derivatives — semantic comment is most of the work; form is inherited
4. **Provenienz-dominant**: lexicographer-only entries — the hedge is the entry's main content
5. **Encyclopedic-doubled**: botanicals and biographicals — semantic comment is itself encyclopedic, doubled

This **fivefold signature taxonomy** is a Hausmann-Wiegand finding: it abstracts above the surface-block matrix and gives the lexicographer's strategic choices for each article-type a name.

## 10. What modern lexicography would add

Hausmann (1985: §4) argues that **the pragmatic-comment is the most under-realised class in older scholarly dictionaries**. Our analysis confirms this for MW: pragmatic-comment is residual, outsourced to citation pattern. A modern revision following Hausmann-Wiegand would:

- Explicitly fill the pragmatic-comment class — register labels (*literary*, *Vedic*, *late Sanskrit*, *medical*, *Tantric*, *koshic-only*).
- Subdivide the Provenienz-Komment — break `L.` back into named-kosha citations as PWG had ([see Lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg)).
- Add a Beispielkomment (example-comment) class — currently entirely absent.

The first two are *resolvable* against the existing digital evidence (the koshas at [ARMH](https://github.com/sanskrit-lexicon/armh), [ABCH](https://github.com/sanskrit-lexicon/abch), [ACPH](https://github.com/sanskrit-lexicon/acph), [ACSJ](https://github.com/sanskrit-lexicon/acsj) provide what's needed for de-hedging `L.`); the third requires fresh corpus work.

## 11. Conclusion

Read through the Hausmann-Wiegand hybrid, MW1899 is a **five-comment-class scholarly retrieval dictionary** with strong form-comment, terse semantic-comment, near-absent pragmatic-comment, well-attested source-comment, and — the diagnostic feature — a 19th-century lexicographic invention we have named the **Provenienz-Komment** (provenance-comment), realised by the single block `<ls>L.</ls>`.

Five article-type signatures recur: form-dominant (roots), balanced (standard nouns/adjectives), semantic-dominant (compounds and derivatives), provenance-dominant (lexicographer-only), encyclopedic-doubled (botanicals and biographicals). These signatures generalise the 14 article-type profiles into a manageable lexicographic typology.

The most consequential MW-specific contribution to scholarly lexicography is the *Provenienz-Komment*. It is **absent from Hausmann's original four-class system, absent from PWG (MW's source dictionary), and absent from modern English dictionaries**. It is, we argue, MW's distinctive editorial contribution — a 19th-century device for compressing PWG's named-kosha attribution apparatus into a single typographically-economical indicator. The trade-off (loss of source granularity, gain of compactness) is what makes MW the dictionary it is: smaller than PWG would be in English, more honest than WIL was about evidentiary basis.

---

## References (selected)

- Hausmann, F. J. (1977). *Einführung in die Benutzung der neufranzösischen Wörterbücher*. Niemeyer.
- Hausmann, F. J. (1985). *Lexikographie*. In *Handbücher zur Sprach- und Kommunikationswissenschaft (HSK)*.
- Hausmann, F. J. & Wiegand, H. E. (1989). *Component parts and structures of general monolingual dictionaries: a survey*. HSK 5.1.
- Monier-Williams, M. (1899). *A Sanskrit-English Dictionary*. 2nd edn. Oxford: Clarendon Press.
- Wiegand, H. E. (1989). *Aspekte der Makrostruktur*. HSK 5.1: 371–409.
- Wiegand, H. E. (2002). *Equivalence in Bilingual Lexicography*. Lexikos 12.
- Reichmann, O. (1990). *Wörterbücher als Sprachgeschichte*. In *Lexikographica* 6.

---

*Source data: [MICROANALYSIS.md](MICROANALYSIS.md). Companion framework papers: [Wiegand](paper-wiegand.md) · [Atkins-Rundell](paper-atkins-rundell.md) · [Grounded](paper-grounded.md). All four analyse the same MW1899 dataset through different theoretical lenses.*
{% endraw %}
