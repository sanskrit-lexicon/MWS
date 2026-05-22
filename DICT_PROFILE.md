# [DRAFT] Dictionary Profile — Monier-Williams Sanskrit-English Dictionary (MWS)

*Draft from public sources (Wikipedia, Cologne CDSL site, digitised prefaces).
Reviewed by @gasyoun before deployment.*

---

## At a glance

| Fact | Value |
|---|---|
| Full title | *Monier-Williams Sanskrit-English Dictionary* |
| Author(s) | Sir Monier Monier-Williams |
| Language | Sanskrit → English |
| Year | 1899 |
| Publisher | Clarendon Press, Oxford |
| Print entries | ≈ 286,561 |
| Volumes | 1 |
| Period covered | Vedic through Classical Sanskrit |
| Script in print | Latin (IAST-based) |
| CDSL short name | `mw` |
| Digital license | CC-BY-SA-4.0 |
| Printed source | Public domain |

---

## Historical background

[DRAFT] Sir Monier Monier-Williams (1819–1899) was the second Boden Professor of Sanskrit at the University of Oxford, succeeding Horace Hayman Wilson in 1860. His predecessor Wilson had produced a Sanskrit-English dictionary in 1819; Monier-Williams spent decades expanding and re-compiling that work, alongside building on the earlier 1832 edition and drawing from the great German comparative-philological tradition represented by the St. Petersburg lexicon (Böhtlingk and Roth's Großes Petersburger Wörterbuch, 1852–1875). The 1899 edition, published in the last year of his life by the Clarendon Press, Oxford, is often called the "enlarged and improved" edition to distinguish it from his earlier 1872 dictionary.

[DRAFT] The 1899 dictionary represents the culmination of Victorian Sanskrit scholarship in the English-speaking world. Monier-Williams benefited from the work of the German philological school while writing for an Anglophone audience. The dictionary covers Sanskrit vocabulary from the Rigveda (c. 1500 BCE) through the classical period (c. 1000 CE) and into the later Sanskrit of legal, philosophical, and Purāṇic texts. Each entry typically records the grammatical category, etymology where known, meanings in roughly chronological order, and citations from named works. The Clarendon Press printed it as a single large folio volume with approximately 1,333 double-column pages.

[DRAFT] Monier-Williams' 1899 dictionary quickly became the standard reference for Sanskrit scholars writing in English, and remained the dominant desk dictionary throughout the twentieth century. The Cologne Digital Sanskrit Lexicon (CDSL) project digitised the full text in the 1990s and 2000s, making it freely searchable online. The CDSL digital edition was later released under CC-BY-SA-4.0, enabling derivative works and redistributions. Further details about the original preface, compilation methodology, and the relationship to the 1872 edition should be drawn from the preface of the 1899 print edition and from secondary literature on the history of Sanskrit studies.

<!-- 2–3 paragraphs: who wrote it, when, why, how it was compiled,
     relationship to other dictionaries of the era, reception by scholars.
     Sources: Wikipedia, dictionary preface, Cologne CDSL "About" page. -->

---

## Scholarly significance

[DRAFT] The Monier-Williams 1899 dictionary (MW) is the most comprehensive Sanskrit-English dictionary and remains the primary English-language reference for classical Sanskrit scholarship. It covers a broader chronological and textual range than Apte's Practical Sanskrit-English Dictionary (AP90), includes etymology and cognates from Indo-European comparativist tradition, and provides source citations allowing users to trace usages to specific texts. Its citation system (abbreviated work names such as RV., MBh., R.) is the standard notation used in most English-language Sanskrit scholarship.

[DRAFT] Known limitations include: (a) the 1899 print shows some inconsistencies in Vedic accent marking; (b) Tantric, Purāṇic, and late-classical vocabulary is less systematically covered than the earlier Vedic and classical strata; (c) the abbreviation system requires familiarity with a specialised key. The CDSL digital edition introduced additional corrections and supplementary entries (see `6602-entries-from-supplements-MW.txt` in this repo). Scholars working with highly specialised or late texts may need to supplement MW with Apte's dictionary or domain-specific glossaries.

<!-- 1–2 paragraphs on: what corpus this dictionary draws on most heavily,
     what it covers better than alternatives, known limitations, influence
     on subsequent lexicography. -->

---

## When to use this dictionary

| Question / use case | MWS appropriate? | Better alternative if not |
|---|---|---|
| Looking up a Classical Sanskrit word | [DRAFT] Yes — comprehensive for classical period | |
| Vedic vocabulary | [DRAFT] Partial — covers Vedic but less depth than GRA | GRA (Grassmann) |
| Buddhist Hybrid Sanskrit | [DRAFT] Partial — some BHS vocabulary present | BHS (Edgerton) |
| Technical terms in Dharmaśāstra / Arthaśāstra | [DRAFT] Yes — well covered | |
| Tantric / Purāṇic vocabulary | [DRAFT] Partial — Purāṇic coverage present but uneven | |
| Sanskrit → English (quick lookup) | [DRAFT] Yes — largest English-language Sanskrit dict | |
| Sanskrit → English (comprehensive, with sources) | [DRAFT] Yes — best option with citations | |
| Reading assistance for students | [DRAFT] Yes — but AP90 may be more accessible | AP90 (Apte) |
| Manuscript / epigraphic forms | [DRAFT] Partial — consult primary sources for rare forms | |

**Summary:** [DRAFT] MW is the standard first port of call for Classical and most Vedic Sanskrit, offering comprehensive coverage with source citations. For Vedic specialist work use Grassmann; for students, Apte's AP90 may be more accessible.

<!-- Fill in Yes / Partial / No for each row. Add rows for domain-specific use cases. -->

---

## Relationship to other CDSL dictionaries

| Dictionary | Relationship to MWS |
|---|---|
| PWG (Böhtlingk & Roth) | Complementary German-language reference; MW drew on PWG but covers different textual strata and gives English glosses |
| AP90 (Apte 1890) | Abridged English-language alternative; less comprehensive than MW but often more accessible for students |
| WIL (Wilson 1832) | Earlier English Sanskrit dictionary that MW superseded and greatly expanded |

<!-- Examples: "earlier edition", "complementary (German)", "abridged version",
     "covers same period with different methodology", etc. -->

---

## Sample entries

Three representative entries annotated to illustrate the dictionary's style,
depth of coverage, and source-citation practice.

### Sample 1 — simple noun with etymology

**Headword:** `aMSa` (IAST: *aṃśa*)  
**Print reference:** p. 1, col. 1

```
<L>10<pc>1,1<k1>aMSa<k2>a/MSa<e>1
<s>a/MSa</s> ¦ <lex>m.</lex> (probably <ab>fr.</ab> √ <hom>1.</hom> <s>aS</s>, <ab>perf.</ab> <s>An-a/MSa</s>, and not from the above √ <s>aMS</s> fictitiously formed to serve as root), a share, portion, part, party<info lex="m"/>
<LEND>
```

**Annotation:** [DRAFT] The `<hom>1.</hom>` marker distinguishes this homophone from others with the same headword. `<ab>fr.</ab>` means "from" (etymology marker). `<ab>perf.</ab>` means "perfect (tense form)". The `<info lex="m"/>` packet records that the grammatical category is masculine. This is a main entry (`<e>1`), and its sub-entries follow with `<e>1A` codes showing additional meanings (partition, inheritance, stake, etc.).

---

### Sample 2 — verbal root with source reference

**Headword:** `aMS` (IAST: *aṃś*)  
**Print reference:** p. 1, col. 1

```
<L>9<pc>1,1<k1>aMS<k2>aMS<e>1
<s>aMS</s> ¦ <ab>cl.</ab> 10. <ab>P.</ab> <s>aMSayati</s>, to divide, distribute, <ls>L.</ls>; also occasionally <ab>Ā.</ab> <s>aMSayate</s>, <ls>L.</ls>; also <s>aMSApayati</s>, <ls>L.</ls><info verb="genuineroot" cp="10P,10Ā"/>
<LEND>
```

**Annotation:** [DRAFT] Verbal root entries begin with the root in `<s>`, then give the class (`<ab>cl.</ab> 10.`), voice (`<ab>P.</ab>` = Parasmaipada, `<ab>Ā.</ab>` = Ātmanepada), the conjugated present form, and the English gloss. `<ls>L.</ls>` = lexicographers (a late authority, indicating the root may be secondary). The `<info verb="genuineroot"/>` tag marks this as a root entry in the CDSL system.

---

### Sample 3 — compound with cross-references

**Headword:** `aMSu—jAla` (IAST: *aṃśu-jāla*)  
**Print reference:** p. 1, col. 2

```
<L>57<pc>1,2<k1>aMSujAla<k2>aMSu—jAla<e>3
<s>aMSu—jAla</s> ¦ <lex>n.</lex> a collection of rays, blaze of light.<info lex="n"/>
<LEND>
```

**Annotation:** [DRAFT] The `—` (em-dash) in `k2` separates the members of a compound. The `<e>3` hierarchy code marks this as a multi-member compound sub-entry under the parent headword `aMSu`. The `<info lex="n"/>` records neuter gender. This is a compact compound entry without source citations, which is typical for straightforward descriptive compounds in MW.

---

## Known digitisation issues

[DRAFT] The mw.txt file uses a custom cp1252-to-UTF-8 conversion pipeline (`history/cp1252-to-utf8.py`). Three words are known to produce a non-invertible round-trip in the SLP1 → IAST → SLP1 transcoding chain (documented in `mwtranscode/readme.txt`). The markup-fix audit (see `mwissues/markup_fix/markup_audit.txt`) identified 9,313 adjacent `</ab> <ab>` pairs that are mostly intentional two-abbreviation sequences. The supplement entries (`6602-entries-from-supplements-MW.txt`) cover vocabulary from the 1899 Supplement pages and have been integrated into the digital edition.

<!-- E.g.: "The 1899 print has cp1252 encoding; converted to UTF-8 by the history/ pipeline."
     "Certain Vedic accent marks were not captured in the first pass."
     "Entries from the Supplement (pp. 1333–1333) are present but may have lower accuracy." -->

---

## Further reading

- [DRAFT] Monier-Williams, M. (1899). *A Sanskrit-English Dictionary*. Clarendon Press, Oxford. Facsimile available at [archive.org](https://archive.org/search?query=monier+williams+sanskrit+english+dictionary) — reviewer to add direct link
- [DRAFT] Cologne Digital Sanskrit Lexicon project page: <https://www.sanskrit-lexicon.uni-koeln.de/> — see "About" and "MWS" sections for digitisation history

<!-- E.g. print facsimile link at archive.org, Wikipedia article, scholarly review, preface PDF. -->

---

## Cite the print edition

```bibtex
@book{mw-print,
  author    = {Monier Monier-Williams},
  title     = {A Sanskrit-English Dictionary},
  year      = {1899},
  publisher = {Clarendon Press},
  address   = {Oxford}
}
```
