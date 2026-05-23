# The microstructure of *Monier-Williams 1899*: a Wiegand-theoretic analysis

> **Supplementary extended draft — superseded by [PAPER.md](PAPER.md).** One of four single-framework drafts consolidated into the single submission paper per [DOUBTS.md D4](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking). This Wiegand-theoretic reading is condensed into [PAPER.md Appendix A](PAPER.md#appendix-a--the-wiegand-theoretic-reading-condensed); this fuller draft is retained as supplementary material only. **For the canonical paper, read [PAPER.md](PAPER.md).**

**Draft for the [*International Journal of Lexicography*](https://academic.oup.com/ijl) (Oxford University Press).** ~8K words target.

**Theoretical framing:** Wiegand's microstructure theory (Wiegand 1989, 1996, 2002; Wiegand & Smit 2013). One of four parallel framework analyses of the same MW1899 data — see [README](README.md). Data source: [MICROANALYSIS.md](MICROANALYSIS.md).

---

## Abstract

This paper applies Herbert Ernst Wiegand's theory of dictionary microstructure to the 286,561 entries of Monier-Williams' *Sanskrit-English Dictionary* (1899) as digitized by the Cologne Digital Sanskrit Lexicon (CDSL). Using the digital edition's XML markup as a window onto MW's structural decisions, we identify 18 formal blocks realising 8 semantic comment-classes and demonstrate that MW exhibits an **integrated microstructure with strong type-bound variation**. The 14 article types we differentiate — verbal root, compound sub-entry, lexicographer-only entry, IE-etymological entry, and so on — each carry a characteristic block profile, with the verbal-root article averaging 9.7 of 18 possible blocks and the continuation sub-entry averaging only 4.8. The lexicographer-hedge marker `<ls>L.</ls>`, present in 13.4% of entries, emerges as the most distinctive Wiegandian *commenting structural indicator* in MW — one that PWG (Böhtlingk-Roth 1855–1875), MW's principal source, does not use at all. We argue that MW's `L.`-hedge constitutes a structural innovation specific to the re-edition for an Anglophone audience.

**Keywords:** dictionary microstructure, Wiegand, Monier-Williams, Sanskrit lexicography, CDSL, structural indicators, integrated microstructure

---

## 1. Introduction

The microstructure of a dictionary article — its internal organization into discrete information units — is the central object of metalexicographic analysis in the German tradition associated with Herbert Ernst Wiegand. Wiegand (1989, §6) defined the microstructure as

> *"the abstract hierarchical structure of an article, comprising the relations between the lemma and the items assigned to it, including the structural indicators that signal these relations."*

In Wiegand's framework the article is composed of a **lemma-sign** plus a series of **items** (*Angaben*), each of which conveys a specific kind of information about the lemma. The relations between lemma and items are signalled by **structural indicators** — typographical, positional, or symbolic devices that mark the function of each item. The microstructure can be **purely additive** (items are simply juxtaposed), **semi-integrated** (some items are grouped under sub-headings), or **fully integrated** (a recursive hierarchy of sense-divisions binds all items into one coherent tree).

This paper applies the framework to a dataset that Wiegand himself never analysed: Monier-Williams' *Sanskrit-English Dictionary* (1899) — henceforth **MW** — as preserved in the [Cologne Digital Sanskrit Lexicon](https://www.sanskrit-lexicon.uni-koeln.de/) [`mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) digital edition. MW is significant for the Wiegand framework for three reasons. First, it is a transitional 19th-century work, contemporary with but predating the German metalexicographic tradition that produced Wiegand's theory. Second, its 286,561 records constitute one of the largest pre-electronic lexicographical corpora ever produced. Third, the XML markup added by the Cologne project (Funderburk, Malten, Scharf 2005ff.) makes MW's microstructure computationally tractable in a way the print original is not — the XML tags are, in effect, an explicit reconstruction of MW's structural indicators by the digital editors.

We proceed by mapping the digital tags onto Wiegandian categories and then asking three questions: (i) what is the microstructure type of MW (additive, semi-integrated, integrated)? (ii) which structural indicators carry the most discriminative load? (iii) how does the microstructure vary across the dictionary's internal article-type typology?

The data for this analysis are the 18 formal blocks and 14 article types catalogued in our companion [working notes](MICROANALYSIS.md). All counts are computed from the live mw.txt (2026-05).

## 2. Wiegandian apparatus

For the analysis below we use the following Wiegand terminology (numbered in his sense where possible):

- **Article** (*Artikel*): the complete entry from `<L>` to `<LEND>` in the digital edition; a *fully-coded article* in Wiegand's typology.
- **Lemma** (*Lemma*): the headword identified by `<k1>` and displayed by `<s>` (see Wiegand 1989: 410ff.).
- **Lemma-sign** (*Lemmazeichen*): the lemma plus its [phonetic, accent, and graphic indicators](../../ENTRY_GUIDE.md#orthographical-conventions) — what MW realises as `<k2>` plus the optional `/` accent marker.
- **Item** (*Angabe*): a discrete unit of information about the lemma. The 18 formal blocks of MICROANALYSIS.md §1 are *Angaben* in Wiegand's sense.
- **Item-class** (*Angabeklasse*): an abstract category of items (e.g. *grammatical category*); MW's 8 semantic blocks (MICROANALYSIS.md §2) are item-classes.
- **Structural indicator** (*Strukturanzeiger*): a typographic or positional device signalling an item's class membership. In MW these are realised as XML tags: `<lex>`, `<ls>`, `<bot>`, etc.
- **Treatment unit** (*Behandlungseinheit*): the lemma + all items dedicated to it. For MW, the treatment unit equals the article — except for `<e>1A` continuation entries, which are formally separate articles but treatment-unit-wise belong to the preceding `<e>1` (see §6 below).

## 3. The 18 structural indicators of MW

In Wiegand's terms, an XML markup language *is* a system of structural indicators — each tag is a typographically-distinct signal of an item-class. The CDSL markup of MW makes 18 such indicators explicit:

| Wiegandian item-class | MW structural indicator | Frequency |
|---|---|--:|
| Formal indicator (lemma identification) | `<L>N<pc>P,C<k1>K1<k2>K2<h>H<e>E` (record header) | 286,561 |
| Lemma-form indicator | `<s>…</s>` / `<s1>…</s1>` | ~284,000 |
| Homophone indicator | `<hom>N.</hom>` | many |
| Word-class indicator | `<lex>…</lex>` | 185,888 |
| Conjugation-class indicator | `<ab>cl.</ab>`, `<ab>P.</ab>`, `<ab>Ā.</ab>` | ~2,500 |
| Etymological-base indicator | `√` + root + `<ab>fr.</ab>` | ~17,000 |
| Comparative-cognate indicator | `<lang>…</lang>` with `<gk>` / `<etym>` content | 3,960 tags |
| Inflectional-form indicator | additional `<s>…</s>` | ~60,000 |
| Editorial-commenting indicator | parenthetical prose | ~25,000 |
| Definiendum-separator | `¦` (the *Strukturanzeiger* par excellence) | 286,488 |
| Sense-division indicator | numbered or lettered subdivisions | informal |
| Source-attribution indicator | `<ls>…</ls>` | ~230,000 entries / 311,932 tags |
| **Evidence-hedging indicator** | `<ls>L.</ls>` (a sub-type of the above) | 38,414 entries / 40,213 tags |
| Botanical-identifier | `<bot>…</bot>` | 8,923 tags |
| Encyclopedic-identifier (mythological/biographical) | `<bio>`, `<s1>` | many |
| Cross-reference indicator | `q.v.`, `<ab>cf.</ab>`, `<ab>id.</ab>` | ~25,000 |
| Machine-annotation indicator | `<info …/>` | 292,603 |
| Correction-provenance indicator | `{{old -> new \|\| date \| author \| URL \|}}` | < 30 |

This inventory exceeds the typical Wiegandian count for monolingual learner dictionaries (which usually carry 8–12 distinct indicators; cf. Wiegand 1995) but is consistent with what Wiegand calls a **scholarly all-information dictionary** (*Sprachwissenschaftliches Wörterbuch mit umfassendem Informationsangebot*), the category in which MW belongs alongside Grimm's *Deutsches Wörterbuch*.

## 4. The microstructure type of MW

Wiegand distinguishes three microstructure types (1989: 416–425):

- **Purely additive** (*rein additiv*): items are juxtaposed without hierarchical relations.
- **Semi-integrated** (*halbintegriert*): some items are grouped under sub-headings; the article has a flat sense list but optional clusters.
- **Fully integrated** (*voll integriert*): the article has a recursive hierarchy in which sub-senses dominate sub-items.

**MW1899 is fully integrated**, with caveats. The integration is most visible in three places:

### 4.1 The `<e>` hierarchy

The `<e>1` → `<e>1A` → `<e>2` → `<e>3` series ([data](../../ENTRY_GUIDE.md#entry-hierarchy-distribution)) realises a 4-deep integration:

```
<e>1  primary lemma                            (32,116 entries)
 ├── <e>1A continuation sense                  (9,294)
 ├── <e>2  derived form (suffix derivative)    (32,499)
 └── <e>3  compound sub-entry                  (112,183)
```

The `<e>1A` continuation **is** Wiegand's archetypal integrated-microstructure marker: a sub-article whose lemma is suppressed (only 33.9% of `<e>1A` entries carry `<s>`; see MICROANALYSIS.md §4) and whose existence is intelligible only in relation to the preceding `<e>1`. This is "integrated" in the strict sense: removing the parent article makes the sub-article meaningless.

### 4.2 The compound family

Each top-level lemma (`<e>1`) with derivable compounds carries a tail of `<e>3*` compound sub-entries clustered in print sequence under its parent. *aṃśu* ([L47](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L169)) is followed in mw.txt by 9 continuation senses (L48–56) and then ~40 compound sub-entries (L57+). The cluster has explicit hierarchical integration through the `<e>3` indicator + the em-dash `—` in `<k2>`.

### 4.3 The sense-division `1)`, `a)`, `— b)`

Within a single article body, sense-divisions are marked by numbered or lettered indicators. These are *informal* in MW (less consistently applied than in PWG) but realise the same integration principle: senses are not just listed but ranked and sub-ranked.

**Two caveats** keep MW from being maximally integrated:

- (i) The `<e>1A` continuation entries are formally **separate articles** in the data file (each gets its own `<L>` record) rather than being structurally nested under their parent. The integration is implicit in adjacency and the `<e>1A` indicator — Wiegandian readers would call this **adjacency-integration**, somewhere between full integration and semi-integration.
- (ii) Lexicographer-only entries (38,414 of them; T2–T3 fullness; see §6) often have a *purely additive* microstructure internally: a single sense + a single `<ls>L.</ls>` and nothing else.

The composite picture: **MW is fully integrated at the macro level (the article cluster around a lemma) and additive at the micro level for thin entries.** This dual character is a defining feature.

## 5. Structural-indicator load

Wiegand emphasises that not all structural indicators carry equal *discriminative load* — the ability to differentiate articles of different types. In MW, the load distribution is striking. The matrix in MICROANALYSIS.md §4 shows which indicators concentrate in which article types. Three indicators emerge as **maximally discriminative** (≥ 50 percentage-point differences across types):

### 5.1 `<info verb="genuineroot"/>` — root vs non-root

This indicator achieves a 100%/0% split: present in 100% of verbal-root articles (by definition) and effectively absent elsewhere. It is the **type-defining structural indicator** for verbal roots — the article type with the most elaborate microstructure (avg. 9.73 of 18 blocks; see MICROANALYSIS.md §5).

### 5.2 `<ls>L.</ls>` — the lexicographer-hedge

Present in **100% of lexicographer-only articles** (definitionally) but also striking off-diagonals: **71.5% of botanical articles** and **64.7% of biographical articles**. The lexicographer-hedge is not merely a category marker — it is a **transverse indicator** that cuts across article types, signalling that *this particular article's evidence base is the indigenous lexicon, not a published text*, regardless of what kind of article it is.

This indicator is **specific to MW**: PWG's [571,152 `<ls>` citations](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) contain zero instances of `<ls>L.</ls>`. PWG handled the same situation by citing the specific kosha (`H.` Hemacandra 17,337 times, `AK.` Amarakośa 14,473 times, `MED.` Medinīkośa 13,055 times, etc.). MW collapsed these into the single `L.` indicator. In Wiegandian terms this is a **deliberate impoverishment** of the structural-indicator system — gaining typographic compactness but losing source granularity. The trade-off is documented in MW's own preface and discussed in [DICT_PROFILE Lineage](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg).

### 5.3 `<lang>` — the comparative-cognate indicator

Present in 100% of IE-etymological articles (by definition) and < 1% elsewhere. As with `genuineroot`, this is a **type-defining** indicator. Its presence concentrates in just 0.7% of records (2,099 entries) but those entries carry MW's distinctive philological contribution — the [comparative-IE apparatus](../../ENTRY_GUIDE.md#ie-cognate-density--lang-breakdown) absent or muted in WIL, AP90, and SKD.

## 6. Article-type microstructure profiles

Wiegand's notion of *Artikeltyp* (article-type) is most useful when applied to *empirically-derived* profiles rather than a-priori categories. The matrix in MICROANALYSIS.md §4 yields 14 such profiles, of which we discuss six here.

### 6.1 The **verbal root** profile (T5 Elaborate, 9.73 blocks avg.)

Type-defining indicators: F05 verb-inflection class (98.4%), F08 inflection forms (99.9%), F17 `genuineroot` machine annotation (100%). Highly enriched: F09 editorial commentary (78.1%), F03 homophone marker (49.6%, vs ~5% elsewhere), F16 cross-reference (54.5%, vs ~7% elsewhere), F06 etymology root (44.7%, vs ~5% elsewhere). **The verbal root is MW's most elaborately treated article-type — and it is also the rarest** (750 of 286,561, 0.26%).

### 6.2 The **masculine-noun** profile (T3 Typical, 6.43 blocks avg.)

The "default" article-type. Core blocks: F01 header + F02 display + F04 grammatical category (100%) + F10 sense gloss (100%) + F12 source citation (78%) + F17 machine annotation (99.8%). Variable enrichment: F06 etymology (8.8%), F08 inflection (21.6%), F12 hedge (18.9%), F15 biographical (19.9% — these are masculine nouns that are also names of deities or heroes).

### 6.3 The **compound sub-entry** profile (T3 Typical, 6.02 blocks avg.)

Core blocks as masculine noun, but with **F11 sense-division at 0.0%** (transparent compounds rarely need sub-senses) and **F06 etymology at 1.6%** (transparent compounds rarely need etymology — the compound members carry it). The em-dash in `<k2>` does the structural work; the body is concise.

### 6.4 The **lexicographer-only** profile (T3, 6.89 blocks avg.)

Type-defining: F13 hedge L. = 100%. Otherwise standard: F04 grammar 65.2%, F10 sense 100%, F12 citation 100% (since the only citation IS the L. hedge). What's striking is **what's absent**: F09 editorial commentary at just 2.6% (vs 78.1% in roots). MW does **not** comment on lexicographer-only words — accepting them on the indigenous lexicons' authority but signalling the weak evidence base via `L.` alone.

### 6.5 The **IE-etymological** profile (T4 Rich, 7.70 blocks avg.)

Type-defining: F07 IE cognate = 100%. Highly enriched: F09 editorial commentary at 38.4% (vs ~5% baseline), F16 cross-reference at 54.5%, F03 homophone at 17.6%. These entries serve a specifically philological function — to record MW's contribution to the comparative-IE knowledge of Sanskrit (see §3 above).

### 6.6 The **continuation** profile (T2 Skeletal, 4.76 blocks avg.)

This is the structurally **most reduced** article-type. F02 display headword is **suppressed in 66.1% of cases** (33.9% present), reflecting headword-inheritance from the parent `<e>1`. F04 grammar at 0.3% (also inherited). F08 inflection at just 6.5%. The continuation is the strongest evidence for MW's *integrated* microstructure — these "articles" are intelligible only in cluster with their parent.

## 7. Fullness as a graded property

The 5-tier fullness scale we propose (MICROANALYSIS.md §5) graduates MW's article-types along a single axis. In Wiegandian terms, fullness corresponds to **microstructure density** (*Mikrostrukturdichte*) — the count of distinct item-classes realised per article.

| Tier | Item-classes realised | % of dictionary |
|---|---|--:|
| T1 Vestigial | 1–3 | 3.7% |
| T2 Skeletal | 4–5 | 30.5% |
| T3 Typical | 6 | 31.9% |
| T4 Rich | 7–9 | 32.4% |
| T5 Elaborate | 10+ | 1.4% |

Median microstructure density is 6 item-classes. This is **higher than typical monolingual learner dictionaries** (median 4–5; Atkins & Rundell 2008: 199) but **lower than the German Grimm Wörterbuch** (median ~10; estimates from Reichmann 1999). MW occupies a middle position — *scholarly but compact*, fitting its design brief as a single-volume desk reference for the English-speaking Sanskritist.

The dispersion is also notable: 65% of entries fall in T2–T3 (4–6 blocks), and the long tail (T4–T5) accounts for 33.8% of entries but disproportionately for the dictionary's intellectual content. The 1.4% T5 entries are likely high-traffic lemmas — *ātman*, *dharma*, *karma*, *brahman*, and so on — which would account for an out-sized share of *consultations* if query logs were available.

## 8. The `L.`-hedge as a Wiegandian innovation

We return to a finding flagged in §5.2: the `<ls>L.</ls>` indicator is **specific to MW**, absent from PWG. From a Wiegand-theoretic perspective this is not a trivial editorial decision but a **deliberate restructuring of the source-attribution item-class** — what Wiegand would call a *Strukturveränderung* (structural change).

PWG's source-attribution item-class was **maximally articulated**: 821 distinct `<ls>` values, each naming a specific work or kosha. The Wiegandian reader of a PWG article could see exactly which textual or lexicographic source supported each gloss. MW, in re-editing PWG for an English audience, replaced this with a **binary distinction**:

- **Named textual source** (`<ls>MBh.</ls>`, `<ls>RV.</ls>`, `<ls>Pāṇ.</ls>`, etc.): real textual evidence.
- **`<ls>L.</ls>`** (the hedge): indigenous-lexicographer-only evidence; treat with weaker weight.

This binary works *as Wiegandian structural indicator* in two senses: (i) it signals an **evidentiary class** (textual vs lexicographic); (ii) it provides **reader-guidance** — telling the user "evaluate this gloss differently." In one stroke MW collapsed PWG's fine-grained source taxonomy into a two-category evidential system. This is a **simplification** of microstructure that produces a **gain** of reader-guidance — a Wiegand-theoretic trade-off worth flagging as an innovation rather than an impoverishment.

## 9. Discussion

Three observations close the analysis:

**(i) MW is more Wiegandian than its date suggests.** Wiegand's framework was developed in the 1980s–90s on the basis of *modern* dictionaries with explicit microstructural design. MW (1899) predates this theoretical work by 90 years. Yet MW exhibits a coherent integrated microstructure with a small, discriminative set of structural indicators — exactly what Wiegand's framework predicts a well-designed scholarly dictionary should have. Either MW is a remarkable proto-instance of Wiegandian design, or — more likely — Wiegand's framework is sufficiently general to capture a long tradition of European scholarly lexicography of which MW is one mature instance.

**(ii) Article-type variation is the central empirical fact.** A Wiegand-theoretic analysis that treats MW as having "the microstructure" obscures the most important finding: MW has at least 14 article-type-specific microstructures, ranging from the 9.7-block elaborate verbal-root to the 4.8-block skeletal continuation. Future Wiegand-theoretic work on scholarly dictionaries would benefit from treating *article-type* as a first-class theoretical category.

**(iii) The `L.`-hedge is a candidate for cross-linguistic comparative study.** MW's innovation of collapsing source-attribution into a binary textual/lexicographic split is **not** standard in 19th-century European lexicography. Is it a Sanskrit-specific response to the unusual *koshic* evidentiary base of much Sanskrit vocabulary? Or a more general feature of dictionaries derived from a meta-source (like PWG) where re-citation of every source would be impractical? Comparative work with similar derived dictionaries (e.g. Roget, Apte) might illuminate this.

## 10. Conclusion

MW1899 has, in Wiegand-theoretic terms, an **integrated microstructure with 18 structural indicators realising 8 item-classes across at least 14 article-type-specific profiles**. The microstructure is dominated by a **modal-6-block typical article** with a long tail of more elaborate types. The single most distinctive structural feature — absent from MW's source PWG — is the `<ls>L.</ls>` lexicographer-hedge, present in 13.4% of entries, which compresses PWG's fine-grained kosha-attribution into a binary textual/lexicographic evidence system. This innovation is the strongest Wiegand-theoretic case for treating MW as an *editorial reworking* of PWG rather than a translation.

The digital edition's XML markup makes the analysis tractable for the first time; the same approach is portable to the other dictionaries in the [CDSL collection](https://www.sanskrit-lexicon.uni-koeln.de/) — PWG, AP, WIL, SKD, GRA, BHS — and to the four kosha dictionaries ([ARMH](https://github.com/sanskrit-lexicon/armh), [ABCH](https://github.com/sanskrit-lexicon/abch), [ACPH](https://github.com/sanskrit-lexicon/acph), [ACSJ](https://github.com/sanskrit-lexicon/acsj)) that constitute MW's deep lineage. A Wiegand-theoretic comparative study of the eight-dictionary CDSL stack would be a natural next step.

---

## References (selected)

- Apresjan, J. (2002). *Principles of Systematic Lexicography*. In M.-H. Corréard (ed.), *Lexicography and natural language processing*. Euralex.
- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Funderburk, J., Malten, T., & Scharf, P. (2014). *Wilson's Sanskrit-English Dictionary, digital edition*. Cologne Digital Sanskrit Lexicon.
- Hausmann, F. J. & Wiegand, H. E. (1989). *Component parts and structures of general monolingual dictionaries: A survey*. In F. J. Hausmann et al. (eds.), *Wörterbücher / Dictionaries / Dictionnaires* (HSK 5.1). De Gruyter.
- Monier-Williams, M. (1899). *A Sanskrit-English Dictionary, Etymologically and Philologically Arranged*. 2nd edn, with E. Leumann and C. Cappeller. Oxford: Clarendon Press.
- Reichmann, O. (1999). *Das Deutsche Wörterbuch von Jacob und Wilhelm Grimm: Erfahrungen mit einem mehrgenerationen-Projekt*. In *Lexikographica* 15.
- Wiegand, H. E. (1989). *Aspekte der Makrostruktur im allgemeinen einsprachigen Wörterbuch*. In HSK 5.1: 371–409.
- Wiegand, H. E. (1996). *Über die Mediostrukturen bei gedruckten Wörterbüchern*. In *Symposium on Lexicography VII*: 11–43.
- Wiegand, H. E. (2002). *Equivalence in Bilingual Lexicography*. Lexikos 12: 239–255.
- Wiegand, H. E. & Smit, M. (eds.) (2013). *Dictionaries: An International Encyclopedia of Lexicography*. Supplementary Volume. De Gruyter.

---

*Source data: [MICROANALYSIS.md](MICROANALYSIS.md). Companion framework papers: [Atkins-Rundell](paper-atkins-rundell.md) · [Hausmann-Wiegand](paper-hausmann.md) · [Grounded](paper-grounded.md). All four analyse the same MW1899 dataset through different theoretical lenses.*
