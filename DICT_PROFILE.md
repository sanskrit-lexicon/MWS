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

The **[1872 first edition](https://www.sanskrit-lexicon.uni-koeln.de/scans/MW72Scan/2020/web/index.php)** ([MW72 scan](https://www.sanskrit-lexicon.uni-koeln.de/scans/MW72Scan/2020/web/index.php) on the Cologne server) drew heavily on the great German lexicon of the time,
Böhtlingk and Roth's *Sanskrit-Wörterbuch* (the so-called Petersburg Wörterbuch
or [PWG](https://github.com/sanskrit-lexicon/PWG), 1855–1875). Monier-Williams condensed the PWG's German citations into
English glosses, added etymological cross-references to cognate Indo-European
languages (Greek, Latin, Gothic, Anglo-Saxon, German, English — see the [IE cognate density section](ENTRY_GUIDE.md#ie-cognate-density--lang-breakdown) for counts), and reorganised
many entries.

The **[1899 second edition](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php)** ([MWScan](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php) on the Cologne server), the one digitised by the Cologne project, is the
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
philological depth, complement with [GRA](https://github.com/sanskrit-lexicon/GRA), [BHS](https://github.com/sanskrit-lexicon/BHS), or [PWG](https://github.com/sanskrit-lexicon/PWG) respectively.

### Article types — what you'll encounter

A working typology of MW entries with live samples. Counts from the 2026-05
audit of [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) ([markup audit file](https://github.com/sanskrit-lexicon/MWS/blob/markup-fix-audit/mwissues/markup_fix/markup_audit.txt)); click any "real sample" link to jump to the actual entry.

| Type | Identifying marker | Count | Real sample |
|---|---|---:|---|
| **Verbal root** | `<info verb="genuineroot"/>` | [750](ENTRY_GUIDE.md#entry-type-breakdown-by-content) | [L9 *aṃś*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L52) — class 10 P. *aṃśayati* "to divide" · [annotated](#sample-1--verbal-root-with-derivation-note) |
| **Masculine noun** | `<lex>m.</lex>` | [63,826](ENTRY_GUIDE.md#entry-type-breakdown-by-content) | [L10 *áṃśa*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L55) — "share, portion" · [annotated](#sample-2--masculine-noun-with-etymology) |
| **Feminine noun** | `<lex>f.</lex>` | [31,534](ENTRY_GUIDE.md#entry-type-breakdown-by-content) | [L72 *aṃśu-matī*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L244) — *Hedysarum Gangeticum* (a botanical) |
| **Neuter noun** | `<lex>n.</lex>` | [34,349](ENTRY_GUIDE.md#entry-type-breakdown-by-content) | [L57 *aṃśu-jāla*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L199) — "collection of rays, blaze of light" |
| **Adjective** | `<lex>mfn.</lex>` | [50,636](ENTRY_GUIDE.md#entry-type-breakdown-by-content) | [L8 *a-ṛṇin*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L49) — "free from debt" ([lexicographer-only](#citation-markers--not-all-are-literary-works)) |
| **Indeclinable** | `<lex>ind.</lex>` | [5,516](ENTRY_GUIDE.md#entry-type-breakdown-by-content) | [L224 *a-kasmāt*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L771) — "suddenly, accidentally" |
| **Compound sub-entry** | `<e>3` + em-dash in `<k2>` | [112,183](ENTRY_GUIDE.md#entry-hierarchy-distribution) | [L57 *aṃśu-jāla*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L199) — neuter compound · [annotated](#sample-3--compound-sub-entry-cross-reference) |
| **Derived form** | `<e>2` (*-aka*, *-in*, *-ya*, …) | [32,499](ENTRY_GUIDE.md#entry-hierarchy-distribution) | [L39 *aṃśaka*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L145) — "forming part" (in *ifc.*) |
| **Continuation senses** | `<e>1A` | [9,294](ENTRY_GUIDE.md#entry-hierarchy-distribution) | [L11–L19](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L58-L82) — 9 more senses of *áṃśa*: partition, booty, stake (with [RV. v, 86, 5](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L67)), lot, fraction denominator, latitude degree, day, an Āditya |
| **Botanical** | `<bot>…</bot>` | [8,923](ENTRY_GUIDE.md#botanical--biographical-tag-stats) | [L72 *aṃśu-matī*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L244) — *Hedysarum Gangeticum* with `<ls>Suśr.</ls>` |
| **IE etymological entry** | `<lang>` cognates | [3,960](ENTRY_GUIDE.md#ie-cognate-density--lang-breakdown) `<lang>` tags | [L92.1 *aṃsa*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L307) — Goth. *amsa*, Gk. ὦμος, Lat. *humerus*, "shoulder" |
| **Proper-name entry** | `<bio>` or `<s1>` after `<ab>N.</ab>` | [358](ENTRY_GUIDE.md#botanical--biographical-tag-stats) `<bio>` | [L830 *agastya-mārga*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L2997) — "the path of [Agastya](https://en.wikipedia.org/wiki/Agastya) (= [Canopus](https://en.wikipedia.org/wiki/Canopus))" |
| **Lexicographer-only** | sole citation is `<ls>L.</ls>` | [40,213](#citation-markers--not-all-are-literary-works) (12.9% of all citations) | [L8 *a-ṛṇin*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L49) — a [**hedge**](#citation-markers--not-all-are-literary-works): known only from indigenous lexicons, not from any published text |
| **Vedic accented** | `/` in `<k2>` | [47,598](ENTRY_GUIDE.md#vedic-accent-coverage) (16.6% of `<k2>`) | [L136 *á-ka*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L468) — "pain, trouble", cited from `<ls>TS.</ls>` |

### Citation markers — not all are literary works

Five of the top-15 most-cited `<ls>` values are **editorial annotations**, not literary works. Misreading them as text citations is a common pitfall. The full top-25 with identities is in the [ENTRY_GUIDE citation-stats section](ENTRY_GUIDE.md#top-25-most-cited-sources).

| Marker | What it means | Count | Treat as |
|---|---|--:|---|
| `L.` | **Lexicographers** — recorded in indigenous Sanskrit lexicons but not attested in any published text | 40,213 (12.9%) | A *hedge*: weaker than a textual citation. MW signals "the word exists in the dictionary tradition, but I cannot point to a real attested use." |
| `ib.` | *ibidem* — "the same source as the immediately preceding `<ls>`" | 10,100 | Resolves to the previous `<ls>`; never a work in itself |
| `W.` | Wilson — Horace Hayman Wilson's [1832 Sanskrit-English dictionary](https://github.com/sanskrit-lexicon/WIL) | 8,286 | Editorial cross-reference to a predecessor lexicon |
| `MW.` | Monier-Williams himself — a self-reference to his own earlier annotation or to the 1872 first edition | 5,711 | Editorial self-citation |
| `Cat.` | Catalogue — manuscript catalogue entries (e.g. India Office library catalogues) | 5,302 | Catalogue/bibliographic, not a text citation |

Versus **real literary sources** in the top-10:

- [`MBh.`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) Mahābhārata (28,047)
- `RV.` [Rigveda](https://en.wikipedia.org/wiki/Rigveda) (15,916)
- `R.` [Rāmāyaṇa](https://en.wikipedia.org/wiki/Ramayana) (10,811)
- `Pāṇ.` [Aṣṭādhyāyī of Pāṇini](https://en.wikipedia.org/wiki/A%E1%B9%A3%E1%B9%AD%C4%81dhy%C4%81y%C4%AB) (8,527)
- `BhP.` [Bhāgavata-Purāṇa](https://en.wikipedia.org/wiki/Bhagavata_Purana) (8,478)

When evaluating a gloss, count the **non-editorial** citations — that's the actual textual evidence MW has for the meaning.

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

**Headword:** `aMS` (IAST: *aṃś*) · **Print reference:** p. 1, col. 1 · **Record:** [`<L>9`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L52)

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
- [`<ls>L.</ls>`](#citation-markers--not-all-are-literary-works) — citation: **"L." is MW's marker for *lexicographers***. The word/meaning is attested only in the indigenous Sanskrit lexicon tradition, not in living textual usage. This is a **hedge**: the root is real but its productive forms are late or theoretical. `<ls>L.</ls>` is the **single most-cited "source" in MW** — [40,213 citations, 12.9% of all `<ls>` tags](ENTRY_GUIDE.md#top-25-most-cited-sources). See [Citation markers](#citation-markers--not-all-are-literary-works) for the full taxonomy distinguishing editorial markers (`L.`, `ib.`, `W.`, `MW.`, `Cat.`) from textual citations.
- `<ab>Ā.</ab>` — *Ātmanepada* (middle voice).
- `<info verb="genuineroot" cp="10P,10Ā"/>` — CDSL machine-readable annotation
  packet recording that this is a genuine root with class-10 P. and Ā. forms.

### Sample 2 — masculine noun with etymology

**Headword:** `aMSa` (IAST: *áṃśa*, with Vedic accent) · **p. 1, col. 1** · **Record:** [`<L>10`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L55)

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

**Continuation sub-entries** ([`<L>11`–`<L>19`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L58-L82), all `<e>1A`): nine further senses of *áṃśa* are listed as adjacent records — *partition* (inheritance), *share of booty*, *earnest money*, *stake (in betting)* with [`<ls>RV. v, 86, 5</ls>`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L67) (its first real textual citation), *a lot*, *fraction denominator*, *degree of latitude or longitude*, *a day* ([L.](#citation-markers--not-all-are-literary-works)), and *Name of an Āditya*. `<e>1A` continuations account for [9,294 entries](ENTRY_GUIDE.md#entry-hierarchy-distribution) across MW.

### Sample 3 — compound sub-entry (cross-reference)

**Headword:** `aMSu-jAla` (IAST: *aṃśu-jāla*) · **p. 1, col. 2** · **Record:** [`<L>57`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L199) · **Parent entry:** [`<L>47` *aṃśu*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L169)

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
- `<e>3` — third-level entry: a compound sub-entry under the parent [*aṃśu* (`<L>47`)](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L169). The `<e>` hierarchy lets the reader navigate compounds without losing their parent context. **`<e>3` is the largest single class in MW** with [112,183 entries (39.1% of the whole dictionary)](ENTRY_GUIDE.md#entry-hierarchy-distribution) — reflecting Sanskrit's heavily-compounding morphology.
- `<lex>n.</lex>` — neuter noun.
- No source citation: this compound is a transparent semantic combination that
  MW glosses without naming a specific attestation — typical for descriptive
  compounds. [264,705 of 311,932 `<ls>` tags (84.9%)](ENTRY_GUIDE.md#coverage-of-ls-citations) lack a numeric coordinate, and many compounds carry no `<ls>` at all.

---

## Known digitisation issues

- **CP1252 → UTF-8 conversion** is preserved at [history/cp1252-to-utf8.py](https://github.com/sanskrit-lexicon/MWS/blob/master/history/cp1252-to-utf8.py) for
  reproducibility.
- **Three non-invertible transcoding round-trips** (SLP1 → IAST → SLP1) are
  documented in [mwtranscode/readme.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwtranscode/readme.txt).
- **Adjacent `</ab> <ab>` pairs (9,313 instances)** flagged by the [2026-05 markup-fix audit](https://github.com/sanskrit-lexicon/MWS/blob/markup-fix-audit/mwissues/markup_fix/markup_audit.txt) (on the [markup-fix-audit branch](https://github.com/sanskrit-lexicon/MWS/tree/markup-fix-audit)) are mostly intentional — two-abbreviation sequences such as
  `<ab>cf.</ab> <ab>RV.</ab>`.
- **Supplement entries (~6,602)** from the 1899 Supplement pages are integrated
  but tagged so reviewers can track them — see
  [6602-entries-from-supplements-MW.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/6602-entries-from-supplements-MW.txt).
- **Vedic accent** capture is partial — [47,598 of 286,561 `<k2>` fields (16.6%)](ENTRY_GUIDE.md#vedic-accent-coverage) carry accent marks, only where the print clearly marked them. For accent-sensitive Vedic work, complement with [Grassmann's RV-dictionary](https://github.com/sanskrit-lexicon/GRA).
- **`<ls>` authority records cover only 28.3% of unique abbreviations** ([232 of 821](ENTRY_GUIDE.md#coverage-of-ls-citations)), though they cover 64.0% of total citations. Major orphans include [`Pāṇ.` (8,527 citations)](ENTRY_GUIDE.md#top-orphan-abbreviations), `ŚBr.`, `Kathās.`, `Suśr.` — a fixable gap.

---

## Further reading

- [Wikipedia: Monier Monier-Williams](https://en.wikipedia.org/wiki/Monier_Monier-Williams) — biography and [Boden chair](https://en.wikipedia.org/wiki/Boden_Professor_of_Sanskrit) context.
- [Wikipedia: Sanskrit-Wörterbuch](https://en.wikipedia.org/wiki/Sanskrit-W%C3%B6rterbuch) — the Petersburg lexicon ([PWG](https://github.com/sanskrit-lexicon/PWG)) on which MW's first edition was based.
- **Cologne web interfaces — the two MW editions side by side:**
  - [MW72Scan (1872 first edition)](https://www.sanskrit-lexicon.uni-koeln.de/scans/MW72Scan/2020/web/index.php) — the original Clarendon edition.
  - [MWScan (1899 second edition)](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php) — the standard "MW" of today; the edition this digitisation is based on.
- [Internet Archive: 1899 facsimile](https://archive.org/details/sanskritenglish00moniuoft) — full scanned print of the 1899 second edition.
- [MW abbreviation key](https://github.com/sanskrit-lexicon/MWS/blob/master/mwabbreviations/mwab_input.txt) — annotated list of `<ab>` expansions with [`<INFER/>`/`<UNMARKED>` status markers](DATA_DICTIONARY.md#status-markers-in-mwab_inputtxt).
- [MWS mwauthorities](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) — structured XML authority record for MW's "List of Works and Authors"; maps `<ls>` abbreviations to bibliographic records and scan links. Prepared ca. 2010 by Peter Scharf and Malcolm Hyman ([Sanskrit Library](http://www.sanskritlibrary.org/)). See [coverage stats](ENTRY_GUIDE.md#coverage-of-ls-citations).
- [Markup-fix-audit branch](https://github.com/sanskrit-lexicon/MWS/tree/markup-fix-audit) — full audit of MW's XML markup ([2026-05 audit file](https://github.com/sanskrit-lexicon/MWS/blob/markup-fix-audit/mwissues/markup_fix/markup_audit.txt)).

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
