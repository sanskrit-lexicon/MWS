# Dictionary Profile — Monier-Williams Sanskrit-English Dictionary (MWS)

A reading companion to the Cologne digital edition of MW. Facts verified against
Wikipedia, the 1899 print preface, and the CDSL `mw.txt` itself; sample-entry
annotations decoded from the real source.

---

## At a glance

| Fact | Value |
|---|---|
| Full title | *A Sanskrit-English Dictionary, Etymologically and Philologically Arranged with Special Reference to Cognate Indo-European Languages* |
| Author | Sir Monier Monier-Williams (1819–1899) |
| Collaborators (1899 edn) | Ernst Leumann · Carl Cappeller |
| Language | Sanskrit → English |
| First edition | 1872 |
| Second edition | 1899 (this is the edition CDSL digitised) |
| Publisher | Clarendon Press, Oxford |
| Volume | 1 (folio) — ~1,333 double-column pages |
| Entries (digital) | 286,561 `<L>` records in `mw.txt` |
| Period covered | Vedic through late Classical Sanskrit |
| Script in print | Latin (IAST-like) |
| CDSL short name | `mw` |
| Digital license | CC-BY-SA-4.0 |
| Printed source | Public domain |

---

## Historical background

Monier Monier-Williams (born Bombay 1819; *né* Williams, hyphenated his name in
1887) was the second Boden Professor of Sanskrit at Oxford, elected in 1860 in
the famously contested vote against Max Müller. The Boden chair, founded by a
bequest from Colonel Joseph Boden, had been established explicitly to support
Christian missionary work in India — the chair's evangelical purpose was decisive
in Monier-Williams' election and shaped the trajectory of his scholarship. His
*Sanskrit-English Dictionary* was conceived as an instrument for that broader
mission: to give Anglophone scholars a comprehensive desk reference to the
Sanskrit textual corpus.

The **1872 first edition** drew heavily on the great German lexicon of the time,
Böhtlingk and Roth's *Sanskrit-Wörterbuch* (the so-called Petersburg Wörterbuch
or PWG, 1855–1875). Monier-Williams condensed the PWG's German citations into
English glosses, added etymological cross-references to cognate Indo-European
languages (Greek, Latin, Gothic, Anglo-Saxon, German, English), and reorganised
many entries.

The **1899 second edition**, the one digitised by the Cologne project, is the
substantial revision Monier-Williams produced in collaboration with Ernst
Leumann and Carl Cappeller. Published in the year of his death, it expanded
coverage, refined etymologies, integrated new textual material, and added a
Supplement (~6,600 additional entries — preserved in the CDSL repo as
[6602-entries-from-supplements-MW.txt](6602-entries-from-supplements-MW.txt)).
The 1899 edition is what scholars cite simply as "Monier-Williams" or "MW."

---

## Scholarly significance

MW is the most comprehensive Sanskrit-English dictionary ever published and
remains the first port of call for the English-speaking Sanskritist 125+ years
after its appearance. Its strengths:

- **Breadth.** Vedic, Epic, Classical, philosophical, dharma-śāstra, kāvya, and
  much Purāṇic vocabulary in one volume.
- **Source citations.** Most entries name the text(s) in which the word appears,
  using a stable abbreviation system (`RV.`, `AV.`, `MBh.`, `R.`, `BhP.`, `Pāṇ.`,
  etc.) — see [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for counts (320,827 `<ls>`
  source-reference tags across the digital edition).
- **Etymology.** Indo-European cognates marked with `<lang>` tags (3,968 occurrences),
  far more than any English-language Sanskrit dictionary before or since.
- **Compound coverage.** Members of long compounds appear as cross-referenced
  sub-entries, supporting the agglutinative nature of Sanskrit.

Limitations:

- **Buddhist Hybrid Sanskrit** is partial; serious BHS work needs Edgerton.
- **Vedic accent** marking is inconsistent — Grassmann's RV-dictionary is the
  reference for accent-sensitive Vedic work.
- **Late Tantric / Āgamic / regional vocabulary** is uneven.
- **Christian missionary framing** occasionally colours definitions of religious
  and philosophical terms; readers should triangulate against AP90, PWG, or
  domain-specific glossaries for theologically loaded vocabulary.

---

## When to use this dictionary

| Question / use case | MW appropriate? | Better alternative |
|---|---|---|
| Looking up a Classical Sanskrit word | **Yes** — first port of call | — |
| Vedic vocabulary, with accent | Partial | [GRA](https://github.com/sanskrit-lexicon/GRA) (Grassmann) |
| Buddhist Hybrid Sanskrit | Partial | [BHS](https://github.com/sanskrit-lexicon/BHS) (Edgerton) |
| Dharmaśāstra / Arthaśāstra technical terms | **Yes** | — |
| Tantric / late Purāṇic vocabulary | Partial | Domain glossaries; PWG for older |
| Sanskrit → German (comprehensive) | No | [PWG](https://github.com/sanskrit-lexicon/PWG) (Böhtlingk-Roth) |
| Sanskrit → English (quick lookup) | **Yes** | [AP90](https://github.com/sanskrit-lexicon/AP90) for students |
| Sanskrit → English (deep, with sources) | **Yes** | — |
| Reading assistance for students | Yes, but dense | [AP90](https://github.com/sanskrit-lexicon/AP90) (Apte) is gentler |
| Manuscript / epigraphic forms | Partial | Primary editions + IEG |
| Etymological cognates (IE family) | **Yes** — uniquely strong | — |

**Summary:** Open MW first for any Classical or general Sanskrit lookup. For
Vedic accent-sensitive work, Buddhist Hybrid Sanskrit, or German-language
philological depth, complement with GRA, BHS, or PWG respectively.

---

## Relationship to other CDSL dictionaries

| Dictionary | Relationship to MW |
|---|---|
| [PWG](https://github.com/sanskrit-lexicon/PWG) (Böhtlingk-Roth, 1855–1875) | German Sanskrit-Wörterbuch — the principal source MW condensed and translated into English |
| [PWK](https://github.com/sanskrit-lexicon/PWK) (Böhtlingk, 1879–1889) | Abridged "kürzerer Fassung" of PWG; contemporary with MW's first edition |
| [AP90](https://github.com/sanskrit-lexicon/AP90) (Apte, 1890) | Student-oriented English Sanskrit dictionary — narrower scope but cleaner pedagogy |
| [AP](https://github.com/sanskrit-lexicon/AP) (Apte, 1957–59 *Practical*) | Apte's later revised and expanded English Sanskrit dictionary |
| [WIL](https://github.com/sanskrit-lexicon/WIL) (Wilson, 1832) | Earlier English Sanskrit dictionary by the first Boden Professor — superseded by MW |
| [GRA](https://github.com/sanskrit-lexicon/GRA) (Grassmann, 1873) | Specialised RV-Wörterbuch — the reference for Vedic accent work |
| [BHS](https://github.com/sanskrit-lexicon/BHS) (Edgerton, 1953) | Buddhist Hybrid Sanskrit dictionary — the BHS counterpart MW lacks |

---

## Sample entries

Three real entries from `csl-orig/v02/mw/mw.txt`, decoded line-by-line. All
abbreviations resolve via the canonical
[mwabbreviations](https://github.com/sanskrit-lexicon/MWS/blob/master/mwabbreviations/mwab_input.txt)
tooltip list.

### Sample 1 — verbal root with derivation note

**Headword:** `aMS` (IAST: *aṃś*) · **Print reference:** p. 1, col. 1 · **Record:** `<L>9`

```
<L>9<pc>1,1<k1>aMS<k2>aMS<e>1
<s>aMS</s> ¦ <ab>cl.</ab> 10. <ab>P.</ab> <s>aMSayati</s>, to divide, distribute, <ls>L.</ls>;
also occasionally <ab>Ā.</ab> <s>aMSayate</s>, <ls>L.</ls>; also <s>aMSApayati</s>, <ls>L.</ls>
<info verb="genuineroot" cp="10P,10Ā"/>
<LEND>
```

**Reading:**
- `<L>9` — entry 9 in the file.
- `<pc>1,1` — page 1, column 1 of the 1899 print.
- `<k1>aMS` / `<k2>aMS` — primary headword in SLP1 (no accent here).
- `<e>1` — top-level entry, no sub-hierarchy.
- `<s>aMS</s>` — the Sanskrit headword span (displayed as *aṃś*).
- `¦` — separator between headword and gloss body.
- `<ab>cl.</ab> 10.` — *class* 10 verb (Sanskrit verbs split into 10 conjugational
  classes; class 10 is the causative-like *cur-ādi*).
- `<ab>P.</ab>` — *Parasmaipada* (active voice).
- `<s>aMSayati</s>` — 3rd-sg present indicative form.
- `<ls>L.</ls>` — citation: "L." is MW's marker for *lexicographers* (i.e.
  attested only in the indigenous Sanskrit lexicon tradition, not in living
  textual usage). This is a hedge: the root is real but its productive forms are
  late or theoretical.
- `<ab>Ā.</ab>` — *Ātmanepada* (middle voice).
- `<info verb="genuineroot" cp="10P,10Ā"/>` — CDSL machine-readable annotation
  packet recording that this is a genuine root with class-10 P. and Ā. forms.

### Sample 2 — masculine noun with etymology

**Headword:** `aMSa` (IAST: *áṃśa*, with Vedic accent) · **p. 1, col. 1** · **Record:** `<L>10`

```
<L>10<pc>1,1<k1>aMSa<k2>a/MSa<e>1
<s>a/MSa</s> ¦ <lex>m.</lex> (probably <ab>fr.</ab> √ <hom>1.</hom> <s>aS</s>,
<ab>perf.</ab> <s>An-a/MSa</s>, and not from the above √ <s>aMS</s>
fictitiously formed to serve as root), a share, portion, part, party
<info lex="m"/>
<LEND>
```

**Reading:**
- `<k2>a/MSa` — secondary headword **with** Vedic accent: the slash `/` after `a`
  marks an *udātta* (high-pitch) accent on the first vowel.
- `<lex>m.</lex>` — grammatical category: masculine noun.
- `<ab>fr.</ab>` — etymology marker: *from*.
- `√ <hom>1.</hom> <s>aS</s>` — derived from root *aś* (homophone 1; MW
  numbers homophonous roots to disambiguate).
- `<ab>perf.</ab>` — perfect tense form cited as evidence.
- `<s>An-a/MSa</s>` — the perfect form *ānáṃśa* showing the root behaviour.
- Note MW's editorial commentary: he rejects an alternative derivation from
  *aṃś* (Sample 1) as a "fictitiously formed" pseudo-root — a glimpse of
  Indo-European philological reasoning at work.
- `<info lex="m"/>` — machine-readable: masculine.

### Sample 3 — compound sub-entry (cross-reference)

**Headword:** `aMSu-jAla` (IAST: *aṃśu-jāla*) · **p. 1, col. 2** · **Record:** `<L>57`

```
<L>57<pc>1,2<k1>aMSujAla<k2>aMSu—jAla<e>3
<s>aMSu—jAla</s> ¦ <lex>n.</lex> a collection of rays, blaze of light.
<info lex="n"/>
<LEND>
```

**Reading:**
- `<k1>aMSujAla` — primary key concatenated (used for SLP1 lookups).
- `<k2>aMSu—jAla` — secondary key with em-dash separating the compound members
  *aṃśu* (ray) + *jāla* (net, collection).
- `<e>3` — third-level entry: a compound sub-entry under the parent *aṃśu*.
  The `<e>` hierarchy lets the reader navigate compounds without losing their
  parent context.
- `<lex>n.</lex>` — neuter noun.
- No source citation: this compound is a transparent semantic combination that
  MW glosses without naming a specific attestation — typical for descriptive
  compounds.

---

## Known digitisation issues

- **CP1252 → UTF-8 conversion** is preserved at `history/cp1252-to-utf8.py` for
  reproducibility.
- **Three non-invertible transcoding round-trips** (SLP1 → IAST → SLP1) are
  documented in [mwtranscode/readme.txt](mwtranscode/readme.txt).
- **Adjacent `</ab> <ab>` pairs (9,313 instances)** flagged by the markup-fix
  audit are mostly intentional — two-abbreviation sequences such as
  `<ab>cf.</ab> <ab>RV.</ab>`. See
  [mwissues/markup_fix/markup_audit.txt](mwissues/markup_fix/markup_audit.txt).
- **Supplement entries (~6,602)** from the 1899 Supplement pages are integrated
  but tagged so reviewers can track them — see
  [6602-entries-from-supplements-MW.txt](6602-entries-from-supplements-MW.txt).
- **Vedic accent** capture is partial; the `<k2>` field carries accents only
  where the print clearly marked them.

---

## Further reading

- [Wikipedia: Monier Monier-Williams](https://en.wikipedia.org/wiki/Monier_Monier-Williams) — biography and Boden chair context.
- [Wikipedia: Sanskrit-Wörterbuch](https://en.wikipedia.org/wiki/Sanskrit-W%C3%B6rterbuch) — the Petersburg lexicon (PWG) on which MW's first edition was based.
- [Internet Archive: 1899 facsimile](https://archive.org/details/sanskritenglish00moniuoft) — full scanned print of the 1899 second edition.
- [Cologne digital edition (online browser)](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php) — the CDSL web interface.
- [MW abbreviation key](https://github.com/sanskrit-lexicon/MWS/blob/master/mwabbreviations/mwab_input.txt) — annotated list of `<ab>` expansions with `<INFER/>`/`<UNMARKED>` status markers.
- [MWS mwauthorities](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) — structured XML authority record for MW's "List of Works and Authors"; maps `<ls>` abbreviations to bibliographic records and scan links. Prepared ca. 2010 by Peter Scharf and Malcolm Hyman (Sanskrit Library).

---

## Cite the print edition

```bibtex
@book{monier-williams-1899,
  author    = {Monier-Williams, Monier},
  title     = {A Sanskrit-English Dictionary, Etymologically and
               Philologically Arranged with Special Reference to
               Cognate Indo-European Languages},
  edition   = {2nd, revised},
  year      = {1899},
  publisher = {Clarendon Press},
  address   = {Oxford},
  note      = {With the collaboration of E.~Leumann and C.~Cappeller}
}
```
