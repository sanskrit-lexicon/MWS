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

## Orthographical conventions (brief)

This profile follows the CDSL-wide conventions used across the [docs-pass branches](https://github.com/sanskrit-lexicon). Full reference: [ENTRY_GUIDE — Conventions](ENTRY_GUIDE.md#orthographical-conventions).

- **Stored form:** [SLP1](https://en.wikipedia.org/wiki/SLP1) — ASCII transliteration — in `<k1>`, `<k2>`, `<s>…</s>` spans (`aMSa`, `aMSu/`, `fzi`).
- **Displayed form:** [IAST](https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration) in *italic* in prose: *aṃśa*, *aṃśu*, *ṛṣi*. Backticks for code tokens and SLP1: `<lex>`, `aMSa`.
- **Vedic accent:** SLP1 `/` after a vowel = *udātta* (`a/MSa`); IAST shows acute over the vowel: *áṃśa*. [Coverage stats](ENTRY_GUIDE.md#vedic-accent-coverage).
- **Compound marker:** em-dash `—` in `<k2>` (`aMSu—jAla`); IAST uses hyphen: *aṃśu-jāla*.
- **L-record format:** `<L>9` (integer) or `<L>10.020` (decimal for sub-entries). Referenced in prose as `L9`.
- **Page/column citation:** `<pc>1,1` = page 1, column 1 of the [1899 Clarendon print](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php). Cited as "p. 1, col. 1".
- **`<e>` hierarchy code:** number + optional letter (`1`, `1A`, `2B`, `3C`). [Full inventory](ENTRY_GUIDE.md#entry-hierarchy-distribution).
- **`<ls>` citations:** roman, not italic. Numeric coordinates follow as Roman-book + Arabic-verse: `<ls>RV. v, 86, 5</ls>`. [15.1% have coordinates](ENTRY_GUIDE.md#coverage-of-ls-citations).

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
| [PWG](https://github.com/sanskrit-lexicon/PWG) (Böhtlingk-Roth, 1855–1875) | German Sanskrit-Wörterbuch — the principal source MW [condensed and reworked](#beyond-pwg--what-mw-contributes) into English |
| [PWK](https://github.com/sanskrit-lexicon/PWK) (Böhtlingk, 1879–1889) | Abridged "kürzerer Fassung" of PWG; contemporary with MW's first edition |
| [AP90](https://github.com/sanskrit-lexicon/AP90) (Apte, 1890) | Student-oriented English Sanskrit dictionary — narrower scope but cleaner pedagogy |
| [AP](https://github.com/sanskrit-lexicon/AP) (Apte, 1957–59 *Practical*) | Apte's later revised and expanded English Sanskrit dictionary |
| [WIL](https://github.com/sanskrit-lexicon/WIL) (Wilson, 1832) | Earlier English Sanskrit dictionary by the first Boden Professor — superseded by MW |
| [SKD](https://github.com/sanskrit-lexicon/SKD) (*Śabdakalpadruma*, 1822–1858) | Sanskrit→Sanskrit monolingual encyclopedic lexicon by Rāja Rādhākānta Deva — the indigenous Indian lexicographical tradition's masterpiece, frequently cited by MW |
| [ARMH](https://github.com/sanskrit-lexicon/armh) (Halāyudha, ~10th c.) | *Abhidhānaratnamālā* (*Halāyudhakośa*) — classical synonymic kosha; PWG cites it 5,114 times as `HALĀY.` |
| [ABCH](https://github.com/sanskrit-lexicon/abch) (Hemacandra, ~12th c.) | *Abhidhānacintāmaṇi* — classical synonymic kosha; PWG cites it 17,337 times as `H.` (most-cited kosha in PWG); the [`Pariśiṣṭa`](https://github.com/sanskrit-lexicon/acph) and [`Śiloñcha`](https://github.com/sanskrit-lexicon/acsj) supplements are separate CDSL repos |
| [GRA](https://github.com/sanskrit-lexicon/GRA) (Grassmann, 1873) | Specialised RV-Wörterbuch — the reference for Vedic accent work |
| [BHS](https://github.com/sanskrit-lexicon/BHS) (Edgerton, 1953) | Buddhist Hybrid Sanskrit dictionary — the BHS counterpart MW lacks |

---

## Beyond PWG — what MW contributes

MW1899 is often described as "an English translation of PWG." That's a half-truth. MW substantially **reworks** the Petersburg Wörterbuch — different audience, different conventions, different editorial decisions, and ~25 years of fresh philological work. The argument:

| Dimension | PWG (Böhtlingk-Roth, 1855–75) | MW1899 |
|---|---|---|
| **Target language** | German Indologists | The English-speaking world (Boden chair's stated mission) |
| **Total records** | [123,366](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt) | [286,561 — 2.3× more](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#entry-hierarchy-distribution) |
| **Compound enumeration** | Often glossed in running prose under the parent | [112,183 enumerated as `<e>3` sub-entries (39.1%)](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#entry-hierarchy-distribution) — see [Sample 3 *aṃśu-jāla*](#sample-3--compound-sub-entry-cross-reference) |
| **IE cognate marking** | Inline mentions in `<is>` italic-spans and parenthetical remarks | [3,960 `<lang>` tags across 112 languages](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#ie-cognate-density--lang-breakdown) (Lat./Gk./Goth./Lith./Zd./…) — a systematic comparative reach |
| **Lexicographer hedge** | Cites kosha sources by name (Hem. 17,337 / AK. 14,473 / MED. 13,055 / TRIK. 8,365 / HALĀY. 5,114 / …); **zero** `<ls>L.</ls>` tags | **Invents the generic [`<ls>L.</ls>` hedge](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md#citation-markers--not-all-are-literary-works) — 40,213 cites (12.9%)** — collapses PWG's named-kosha attributions into a single "lexicographers" label. Trade-off: bibliographic precision lost, compactness gained. See [Lineage section](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md#lineage-wil--koshas-mw--pwg). |
| **Botanical / zoological tagging** | Limited; in prose | [8,923 `<bot>` species names](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#botanical--biographical-tag-stats) in scientific Latin |
| **Biographical / mythological tagging** | Limited | [358 `<bio>` figures](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#botanical--biographical-tag-stats) (e.g. [*agastya-mārga* → Canopus](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L2997)) |
| **Editorial commentary** | Restrained; mostly citation chains | Frequent interpolated reasoning — see MW's [back-formation argument in Sample 2](#sample-2--masculine-noun-with-etymology) ("fictitiously formed to serve as root") |
| **Supplement** | — | [~6,602 supplement entries](https://github.com/sanskrit-lexicon/MWS/blob/master/6602-entries-from-supplements-MW.txt) added in 1899 |
| **Citation discipline** | German source conventions | English conventions; [editorial markers (L., ib., W., MW., Cat.)](#citation-markers--not-all-are-literary-works) carry distinct semantics |
| **Year span vs PWG** | 1855–1875 | [1872 first edn](https://www.sanskrit-lexicon.uni-koeln.de/scans/MW72Scan/2020/web/index.php) (during PWG run); [1899 second edn](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php) — adds 25 years of additional scholarship |
| **Collaborators (1899)** | Böhtlingk + Roth | Monier-Williams + [Leumann](https://en.wikipedia.org/wiki/Ernst_Leumann) + [Cappeller](https://en.wikipedia.org/wiki/Carl_Cappeller) |

**What MW does *not* do better than PWG:**

- **Source citation density** — PWG carries more granular citation chains for individual senses (multiple `<ls>RV. n,n,n.</ls>` per sense; MW more often gives a single representative cite).
- **Vedic-specialist accuracy** — PWG's Sanskritists were Vedic specialists; for Vedic accent and obscure Saṃhitā vocabulary, [GRA](https://github.com/sanskrit-lexicon/GRA) (Grassmann) remains the reference.
- **Kosha attribution** — PWG names the specific kosha (`H.` 17,337, `AK.` 14,473, `MED.` 13,055, `TRIK.` 8,365, `HALĀY.` 5,114); MW collapses all into `<ls>L.</ls>`. For a researcher tracing the indigenous lexicographical genealogy of a sense, PWG + the [four CDSL koshas (ARMH, ABCH, ACPH, ACSJ)](#lineage-wil--koshas-mw--pwg) are the primary references.
- **Bibliographic precision** — PWG's `<is>gaṇa</is>`, edition references, and page-pointers in citations are more rigorous; MW abbreviates more.

**What MW deliberately keeps from PWG:**

- The basic record structure (headword + grammatical category + senses + citations).
- The PWG abbreviation conventions for textual sources (`RV.`, `AV.`, `MBh.`, …) — MW's [Lists of Works and Authors](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) borrows heavily from PWG's bibliography.
- Most sense divisions for well-attested vocabulary.

The most accurate one-liner: **MW1899 is an English re-edition of PWG, rewritten for a different audience, with systematic IE comparative material added and editorial conventions changed throughout.**

---

## Same entry across seven dictionaries

A practical illustration of *what each lexicon adds*. We pull the same Sanskrit headword from seven CDSL dictionaries — spanning all three target languages (German, English, Sanskrit) and the kosha tradition — and show the first lines of each.

The seven: [PWG](https://github.com/sanskrit-lexicon/PWG) (German, 1855–75) · [PWK](https://github.com/sanskrit-lexicon/PWK) (Böhtlingk abridged, German, 1879–89) · [MW](https://github.com/sanskrit-lexicon/MWS) (English, 1899) · [AP](https://github.com/sanskrit-lexicon/AP) (Apte, English, 1957) · [WIL](https://github.com/sanskrit-lexicon/WIL) (Wilson, English, 1832) · [SKD](https://github.com/sanskrit-lexicon/SKD) (*Śabdakalpadruma*, Sanskrit-Sanskrit, 1822–58) · [VCP](https://github.com/sanskrit-lexicon/vcp) (Tārānātha's *Vācaspatya*, Sanskrit-Sanskrit, 1873–84).

### Headword 1: *aṃśa* — "share, portion"

**[PWG L7](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt#L124)** (German, 1855):

{% raw %}
```
1. {#a/MSa#}¦ (s. <is>gaṇa</is> {#vfzAdi#}) <lex>m.</lex>
<ls>SIDDH. K. 249,b, ult.</ls>
1) {%Theil%}    <ls>AK. 2,9,90.</ls>  <ls>H. 1434.</ls>
   — a) {%Theil, Abschnitt%}    <ls>H. an. 2,542.</ls>
   — b) {%ein Theil des Kaufpreises, Haftgeld%} <ls>ṚV. 3,45,4.</ls>
   — c) {%Antheil%}              <ls>ṚV. 7,32,12.</ls>
   — d) {%Partei%}               <ls>ṚV. 1,102,4.</ls>
   — e) {%Nenner eines Bruchs%}  <ls>COLEBR. Alg. 13.</ls>
2) {%Theilung, Erbschaftstheilung%}  <ls>H. an. 2,542.</ls>
```
PWG enumerates the sense tree (1, 1a–1e, 2) with **multiple `<ls>` cites per sub-sense** including pointer to the *Siddhāntakaumudī*'s grammatical analysis, Amarakośa, Hemacandra. Sense 1b "share of purchase price, deposit" with `<ls>ṚV. 3,45,4</ls>` is a Vedic textual citation. Glosses in German: *Theil*, *Theil-Abschnitt*, *Antheil*, *Partei*, *Nenner eines Bruchs*.

**[PWK L6](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pw/pw.txt#L21)** (Böhtlingk's *Sanskrit-Wörterbuch in Kürzerer Fassung*, abridged German, 1879–89):

```
{#a/MSa#}¦ <lex>m.</lex>
— 1〉 {%Theil:%} {#svAMSatas#} <ls n="Chr.">139,1</ls>.
— 2〉 {%Antheil, Erbtheil%}.
— 3〉 {%Einsatz bei Wetten%} <ls>ṚV. 5,86,5</ls>. <ls>TĀṆḌYA-BR. 25,13,3</ls>.
— 4〉 {%Partei%}.
— 5〉 {%Grad eines Kreises%}.
— 6〉 *{%Tag%} <ls>GAL.</ls>
— 7〉 <ab>N. pr.</ab> eines <is>Āditya</is>.
```
PWK is **Böhtlingk's own abridgement of PWG**, condensing the same 7 senses into ~70% the space. Crucially, **PWK drops nearly all the named-kosha citations** that PWG carried: of PWK's [86,750 `<ls>` tags](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pw/pw.txt), only 15 cite `H.` (Hemacandra), 4 cite `AK.` (Amarakośa), 18 cite `MED.`, 7 cite `TRIK.` ([see Option F](papers/microanalysis/VISUALISATIONS.md)) — compared to PWG's 17,337 / 14,473 / 13,055 / 8,365. PWK introduces a different hedge: the `*` prefix marks unattested/lexicon-only senses (note `*{%Tag%}` in sense 6 — citing `GAL.` only). **PWK is the missing link** between PWG's elaborate apparatus and MW's English compression: it shows that abandoning the kosha apparatus happened in Böhtlingk's own work *before* MW.
{% endraw %}

**[MW L10](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L55)** (English, 1899):

```
<s>a/MSa</s> ¦ <lex>m.</lex> (probably <ab>fr.</ab> √ <hom>1.</hom> <s>aS</s>,
<ab>perf.</ab> <s>An-a/MSa</s>, and not from the above √ <s>aMS</s>
fictitiously formed to serve as root), a share, portion, part, party
```
MW gives the **etymology argument up front** (the parenthetical back-formation claim — absent in PWG), then condenses 5+ PWG sub-senses into one comma-separated English gloss. The detailed sense breakdown follows in [9 continuation sub-entries L11–L19](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L58-L82) (booty, stake with `<ls>RV.</ls>` citation, lot, fraction denominator, latitude, day, Āditya). [See full annotation](#sample-2--masculine-noun-with-etymology).

**[AP L4](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/ap/ap.txt#L91)** (Apte, 1957):

```
{#aMSaH#}¦ [{#aMS-ac#}]
1 A share, part, portion, division; member; {#sakfdaMSo nipatati#} <ls>Ms. 9. 47</ls>;
  {#turyAMSaH#} a fourth part; ... {#mamEvAMSo jIvaloke#} <ls>Bg. 15. 7</ls>; {#BuvamaMSAviva#}
  {#DarmayorgatO#} <ls>R. 8. 16</ls>; {#aMSena darSitAnukUlatA#} <ls>K. 159</ls> partly.
2 A share in property, inheritance; ...
3 the numerator of a fraction; ...
4 A degree of latitude (or longitude); ...
5 The shoulder (more correctly written as {#aMsa#}, q.v.).
6 N. of one of the Ādityas; <ls>Mb. 1. 227. 25</ls>; ...
7 The vital note in a Rāga.
Comp.: aMSAMSaH, aMSAMSi, aMSAvatAraH, aMSAvataraRam, aMSakuRqalI, aMSaBAj, aMSahara, ...
```
AP includes the **Pāṇinian derivational formula** `[aMS-ac]` (root + suffix), gives 7 numbered senses with **inline Sanskrit example phrases + their textual sources**, and ends with a **list of compound entries** that follow as `<L>4.020`, `<L>4.022`, etc. — a deliberately pedagogical organization for students.

**[WIL L6](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/wil/wil.txt#L34)** (Wilson, 1832):

```
{#aMSa#}¦
<lex>m.</lex> ({#-SaH#})
1 A share or portion.
2 A part.
3 A shoulder, the shoulder blade.
4 (In arithmetic) a fraction.
5 The numerator of a fraction.
6 A degree of latitude or longitude, &c. See {#aMsa#}.
<ab>E.</ab>
{#aMSa#} to divide, {#ac#} affix.
```
Wilson gives **6 senses plus the [Pāṇinian derivation](https://en.wikipedia.org/wiki/Sanskrit_grammar)** (the `<ab>E.</ab>` "Etymology" line: *aṃśa* "to divide" + *ac* affix — the same `[aMS-ac]` analysis [AP L4](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/ap/ap.txt#L91) gives 125 years later). Wilson **predates** AP's formula by 58 years and MW1899 by 67 years.

**Critically, WIL is itself a kosha — not in style but in lineage.** WIL's own subtitle, in its [TEI header](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/wil/wilheader.xml), reads:

> *"…translated, amended, and enlarged from **an original compilation, prepared by learned natives for the College of Fort William**…"*

CDSL classifies WIL under the [Indic Subject Classification](https://github.com/sanskrit-lexicon/csl-orig) as `koSa` (kosha) — Wilson is treated by Cologne itself as a kosha, not as a European-philological dictionary. WIL's intellectual genealogy traces directly to the [pandits of Fort William College, Calcutta](https://en.wikipedia.org/wiki/Fort_William_College), working from the classical Sanskrit synonymies — [Amarakośa](https://en.wikipedia.org/wiki/Amarakosha) (~6th c.), [Halāyudha's *Abhidhānaratnamālā*](https://github.com/sanskrit-lexicon/armh) (~10th c.), and [Hemacandra's *Abhidhānacintāmaṇi*](https://github.com/sanskrit-lexicon/abch) (~12th c.).

What WIL lacks vs MW is therefore **not** the Sanskrit-grammatical scaffolding (which both have) but **a different lineage**: WIL is **the kosha tradition itself, translated into English**; MW is **PWG, condensed into English**. These are different intellectual ancestries colliding at almost the same headword.

**[SKD L6](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/skd/skd.txt#L70)** (Śabdakalpadruma, 1822–58, monolingual Sanskrit):

```
aMSaH¦, puM, (aMSa viBAjane, adantacurAdiH . karmmaRi GaY .)
viBAjanaM . tatparyyAyaH . BAgaH 2 . vaRwakaH 3 . ityamaraH .
viBAgaH 4 BaktiH 5 . iti jawADaraH .
aMsaSabdo dantyasAnto'pi . aMSAMsa t ka viBAjane iti kavikalpadrumadaSanAt .
skanDaH . iti vidyAvinodAdayaH .
(vastvekadeSaH . rikTaviBAgaH . caturTaBAgaH . BAjyANkaH . ravimUrttiviSezaH .
AdityaviSezaH, yaTA, ...
"DAtA mitro'ryyamA Sakro varuRastvaMSa eva ca ..." iti mahABAratam .)
```
SKD is a **Sanskrit-Sanskrit monolingual dictionary** — both gloss and citation are in Sanskrit. The format encodes **the indigenous lexicographical method**: Pāṇinian derivation (`adantacurAdiH . karmmaRi GaY` = "from the *cur-ādi* root with kṛt-suffix *GHaÑ* in the patient sense"), synonyms keyed to indigenous lexica (Amarakośa = `ityamaraH`, Jaṭādhara = `iti jawADaraH`, Vidyāvinoda = `iti vidyAvinodAdayaH`), MBh. quotation for the Āditya sense. No European-language target.

**[VCP L5](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/vcp/vcp.txt#L52)** (Tārānātha's *Vācaspatya*, monolingual Sanskrit, 1873–84):

```
aMSa¦ pu0 aMSa--BAve'c . viBAge "sakfdaMSo nipatati sakft-
kanyA pradIyate . sakfdAha dadAnIti trIRyetAni sakft
sakfditi smftiH . karmmaRi ac . viBAjye "dvAvaMSO
pratipadyeta viBajannAtmanaH piteti" "dvyaMSaharo'rdDaharo vA
putravittArjjanAt piteti" ca smftiH . saMKyAsUcakANkaviBAjye
taTANke, ca "anyonyahArABihatO harAMSAviti" aMSAhati-
SCedabaDena Bakteti" BajecCido'MSEraTa tErvimiSrEriti
ca lIlA0 . karaRe ac . avayave "aMSuraMSuzwe deva!
somApyAyasveti" yaju0 . […]
"mamEvAMSo jIvaloke jIvaBUtaH sanAtana" iti gItAvAkyam .
[…]
viSezAvayave, rASicakrasya zazwyuttaraSatatrayaDA viBAjake BAge,
[…] 6, 1, 203 pA0 sU0 vfzAdizu pAWAt asya AdyudAttatvam .
```
VCP is the **second major Sanskrit-Sanskrit monolingual** in CDSL, **contemporary with PWG** (1873–84 vs PWG's 1855–75). Where SKD is more concise and lexicographic, VCP is **encyclopedic**: this single entry quotes Manu-Smṛti (`smftiH`), the Bhagavad-Gītā (`mamEvAMSo jIvaloke...`), the Yajurveda (`yaju0`), Līlāvatī (`lIlA0`), Vedānta-pariBhāzā, Śārīraka-sūtra commentary, Jyotiṣa (astronomy), and ends with Pāṇini sūtra **6,1,203** explaining the *udātta* accent. **VCP demonstrates that the indigenous Sanskrit-Sanskrit lexicographic tradition continued *in parallel* with the European philological project** — Tārānātha worked simultaneously with PWG without using it.

### Headword 2: *aṃśu-jāla* — "a blaze of light"

A transparent compound. Tells you everything about which lexicons enumerate vs gloss compounds:

| Dictionary | Has separate entry? | Notes |
|---|---|---|
| [**MW** `<L>57`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L199) | **Yes** | `aMSu—jAla<e>3` `n.` "a collection of rays, blaze of light." See [Sample 3](#sample-3--compound-sub-entry-cross-reference). |
| [**AP** `<L>12.022`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/ap/ap.txt#L231) | **Yes** | `aMSujAlam` `<e>2` "a collection of rays, a blaze or halo of light." Listed as compound under `aMSuH` (`L12`). |
| [**WIL** `<L>25`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/wil/wil.txt#L181) | **Yes** | `aMSujAla` `n.` "A collection or blaze of light. A parcel or pencil of rays." With etymological note: `aMSu` + `jAla` "a net". |
| **PWG** | **No** | Not separately enumerated — PWG covers transparent compounds in running prose under the parent `aMSu` entry. |
| **PWK** | **No** | Same as PWG — Böhtlingk's own abridgement preserves the prose-compound convention. |
| **SKD** | **No** | Not separately enumerated; the relevant *aṃśu*-compounds in SKD are `aMSukaM` (cloth), `aMSumatI` (a creeper), `aMSumAlI` (sun), etc. — encyclopedic rather than transparent. |
| **VCP** | **No** | Same — Sanskrit-Sanskrit lexicography enumerates *encyclopedic* compounds (proper names, technical terms) but not *transparent* descriptive compounds. |

**Reading the table:** the English lexicons (WIL/MW/AP) systematically enumerate transparent compounds — a structural choice they share. PWG, PWK, SKD, and VCP all prefer prose-glossing under the parent. **This compound-enumeration policy alone accounts for much of MW's 2.3× size advantage over PWG**.

---

## Lineage: WIL ← Koshas; MW ← PWG

The user observation **"WIL is based on Koshas, MW is based on PWG"** is correct and can be quantitatively demonstrated from the data files themselves. The two dictionaries draw on different intellectual ancestries that meet at almost the same headwords.

### The four Cologne koshas

| CDSL repo | Title | Author | Date | Type |
|---|---|---|---|---|
| [ARMH](https://github.com/sanskrit-lexicon/armh) | *Abhidhānaratnamālā* (*Halāyudhakośa*) | [Halāyudha](https://en.wikipedia.org/wiki/Hal%C4%81yudha) | ~10th c. | Synonymic kosha |
| [ABCH](https://github.com/sanskrit-lexicon/abch) | *Abhidhānacintāmaṇi* | [Hemacandra](https://en.wikipedia.org/wiki/Hemachandra) | ~12th c. | Synonymic kosha |
| [ACPH](https://github.com/sanskrit-lexicon/acph) | *Abhidhānacintāmaṇi-pariśiṣṭa* | Hemacandra | ~12th c. | Supplement to ABCH |
| [ACSJ](https://github.com/sanskrit-lexicon/acsj) | *Abhidhānacintāmaṇi-śiloñcha* | Hemacandra (attr.) | ~12th c. | Gleanings supplement to ABCH |

These are **classical synonymic dictionaries** — verse lists of synonyms, grouped by sense. The same word *aṃśu* appears in [ARMH L369](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/armh/armh.txt#L3788) (in the verse listing names of the sun: *tigmAMSus taraRis tathA dinamaRir bhāsvān...*) and again in [ARMH L411](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/armh/armh.txt#L4188) (in the verse listing words for "ray": *rociḥ śociḥ abhīṣuḥ... aṃśu*). Same in [ABCH](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/abch/abch.txt) — *aṃśu* appears in the synonym groups for "sun" and for "ray." These are **the very sense divisions** that WIL ("A ray of light, a sun-beam... The sun...") and MW ("a filament... a ray... the sun") reproduce.

### The citation evidence

The lineage is provable by counting `<ls>` citations of named kosha sources in each dictionary's raw data file:

| Source cited as `<ls>` | Identity | WIL (1832) | PWG (1855–75) | MW (1899) |
|---|---|--:|--:|--:|
| `H.` | Hemacandra (= ABCH) | 0 | **17,337** | 0 |
| `AK.` | Amarakośa | 0 | **14,473** | 0 |
| `MED.` | Medinīkośa | 0 | **13,055** | 0 |
| `H. an.` | Hemacandra's *Anekārthasaṃgraha* | 0 | **9,771** | 0 |
| `TRIK.` | *Trikāṇḍaśeṣa* | 0 | **8,365** | 0 |
| `HALĀY.` | Halāyudha (= ARMH) | 0 | **5,114** | 0 |
| `Amar.` | Amarakośa (MW spelling) | 0 | 0 | 209 |
| **`L.`** | **"Lexicographers" (generic kosha hedge)** | 0 | **0** | **40,213** |
| **TOTAL `<ls>` tags** | All citations | [230](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/wil/wil.txt) | [571,152](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt) | [312,159](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#coverage-of-ls-citations) |

**The picture this reveals:**

1. **WIL has 230 `<ls>` tags total.** Wilson's dictionary has almost no `<ls>` citation apparatus because **it does not need one — WIL is itself the kosha tradition translated.** The kosha-derived senses are the entries; you don't cite your own source. Wilson's only systematic `<ls>` cites are [224 of `<ls>Rox.</ls>`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/wil/wil.txt) — references to [William Roxburgh's *Flora Indica*](https://en.wikipedia.org/wiki/William_Roxburgh) for botanical identifications, a 19th-century European source layered on top of the kosha base.

2. **PWG cites koshas by name — 68,000+ times.** Böhtlingk and Roth integrate the indigenous lexicographical tradition **with** the textual corpus. `H.` (Hemacandra) alone gets 17,337 cites — more than any text except the Mahābhārata. The Petersburg Wörterbuch is a **synthesis** of kosha and text.

3. **MW drops the kosha names — and invents the `L.` hedge to replace them.** Look at the row: PWG has **zero** `<ls>L.</ls>`. MW has **40,213**. MW is what happens when PWG's named kosha attributions (Hem., AK., MED., TRIK., HALĀY.) are collapsed into one generic "lexicographers-only" label. The hedge MW added is **not present in PWG** — it is MW's distinctive editorial choice when condensing PWG for an English audience.

### What this proves

- **WIL ← Koshas** (direct lineage, via the [Fort William College](https://en.wikipedia.org/wiki/Fort_William_College) pandits — confirmed by [WIL's own subtitle](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/wil/wilheader.xml) and CDSL's `koSa` subject classification).
- **MW ← PWG** (confirmed by MW's own preface and by the [structural alignment shown in the *aṃśa* sample-entry comparison](#same-entry-across-seven-dictionaries) above).
- **The koshas enter MW twice**: directly (the senses themselves, ultimately traceable to AK./H./MED./HALĀY.) and indirectly (via PWG, which named the kosha sources, then MW which abridged them as `L.`).

### Citation-discipline contrast — the deepest scholarly point

PWG's discipline was to **name the kosha**. If a word's only attestation was in Hemacandra's *Abhidhānacintāmaṇi*, PWG wrote `<ls>H.</ls>`. If only in Halāyudha's *Abhidhānaratnamālā*, PWG wrote `<ls>HALĀY.</ls>`. The reader could check the source.

MW's discipline was to **mark the type** without naming the source. All kosha-only attestations became `<ls>L.</ls>` regardless of which kosha. This is a **loss of bibliographic precision** in exchange for compactness — and one of [the legitimate criticisms of MW vs PWG](#beyond-pwg--what-mw-contributes) listed above.

This isn't accidental: it's a deliberate editorial decision documented in MW's preface. For a researcher tracing which indigenous lexicon attests a particular sense, **PWG is more useful than MW, and the four CDSL koshas above are the primary sources to consult.**

---

## Sample entries

Three real entries from [`csl-orig/v02/mw/mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt), decoded line-by-line.

**Abbreviation tooltip resolution:** All `<ab>` abbreviations resolve via the **operative** tooltip list at [`csl-pywork/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt`](https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt) (424 entries, last updated [2024-08-03](https://github.com/sanskrit-lexicon/csl-pywork/commits/master/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt) — feeds the [Cologne web display](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php) via `mwab.sqlite`). The [MWS `mwabbreviations/mwab_input.txt`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwabbreviations/mwab_input.txt) (267 entries, last updated [2017-11-08](https://github.com/sanskrit-lexicon/MWS/commits/master/mwabbreviations/mwab_input.txt)) is a separate research/audit copy with `<INFER/>`/`<UNMARKED>`/`<UNUSED/>` status markers — useful for understanding *which* abbreviations were added by the digitisation team vs which appear in the 1899 print. The two files have different formats and different scopes.

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
- **MW abbreviation tooltip list (operative)** — [`csl-pywork/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt`](https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt) — 424 entries, last updated [2024-08-03](https://github.com/sanskrit-lexicon/csl-pywork/commits/master/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt); feeds the [Cologne web display](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php) tooltips via `mwab.sqlite`.
- **MW abbreviation audit copy** — [`MWS/mwabbreviations/mwab_input.txt`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwabbreviations/mwab_input.txt) — 267 entries, last updated [2017-11-08](https://github.com/sanskrit-lexicon/MWS/commits/master/mwabbreviations/mwab_input.txt); research/annotation file with [`<INFER/>`/`<UNMARKED>` status markers](DATA_DICTIONARY.md#status-markers-in-mwab_inputtxt).
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
