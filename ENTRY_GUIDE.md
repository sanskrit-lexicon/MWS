{% raw %}
# Entry Reading Guide — MWS

A practical reference for reading and interpreting entries in `mw.txt`. Worked
examples and annotations verified against the live `csl-orig/v02/mw/mw.txt`.

For the org-wide primer (SLP1 cheatsheet, abbreviation lookup) see the
[Entry Reading Primer](https://github.com/sanskrit-lexicon/csl-homepage/blob/master/docs/ENTRY_READING_PRIMER.md).

---

## Record structure

Each entry spans from an `<L>` header line to a `<LEND>` marker:

```
<L>10<pc>1,1<k1>aMSa<k2>a/MSa<e>1
<s>a/MSa</s> ¦ <lex>m.</lex> a share, portion, part<info lex="m"/>
<LEND>
```

| Field | Meaning |
|---|---|
| `<L>N` | Record number. Integer for top-level records; decimals (`10.1`) for nested sub-entries. |
| `<pc>P,C` | Page and column in the **1899 Clarendon print edition**. |
| `<k1>` | Primary headword key in SLP1, **no accent**, no compound dashes. Used for lookups. |
| `<k2>` | Secondary headword key in SLP1, **may include Vedic accent marks** (`/` = udātta) and em-dashes for compound segmentation. |
| `<e>N[A]` | Hierarchy code (see below). |
| `<s>…</s>` | Sanskrit text span — transcoded at display time to IAST or Devanagari. |
| `¦` | Separates the headword span from the gloss body. |
| `<LEND>` | End of record. |

### `<e>` hierarchy codes

| Code | Meaning | Example |
|---|---|---|
| `<e>1` | Top-level entry (main headword) | `<L>10` `aMSa` |
| `<e>1A` | Continuation: another meaning of the same headword | `<L>11` … `<L>19` (nine additional meanings of `aMSa`) |
| `<e>2` | Derived form (e.g. an *-in* derivative) | `<L>45` `aMSin` (possessor of *aṃśa*) |
| `<e>3` | Compound sub-entry | `<L>57` `aMSu—jAla` |

---

## Encoding

Sanskrit text is stored in **SLP1**, a lossless ASCII transliteration. The web
interface and exports transcode it to IAST or Devanagari on the fly.

| Display | Example | SLP1 source |
|---|---|---|
| IAST | *nara* | `nara` |
| IAST | *mahārāja* | `mahArAja` |
| IAST | *ṛṣi* | `fzi` |
| IAST | *aṃśa* | `aMSa` |
| Devanagari | नर | `nara` |

SLP1 quick reference — **consonants:**
`k K g G N c C j J Y w W q Q R t T d D n p P b B m y r l v S z s h`
**Vowels:** `a A i I u U f F x X e E o O M H`

Three round-trip non-invertibilities exist (SLP1 → IAST → SLP1); see
[mwtranscode/readme.txt](mwtranscode/readme.txt).

---

## Orthographical conventions

The conventions below apply across all CDSL docs-pass branches and reading material.
[DICT_PROFILE.md](DICT_PROFILE.md#orthographical-conventions-brief) carries a short summary; this section is the full reference.

### Sanskrit display

| Context | Convention | Example (SLP1 / IAST / Devanagari) |
|---|---|---|
| **Stored in data file** | [SLP1](https://en.wikipedia.org/wiki/SLP1) ASCII | `<k1>aMSa<k2>a/MSa` ; `<s>aMSayati</s>` |
| **In prose, as a word** | IAST, italic | *aṃśa*, *aṃśu*, *ṛṣi* |
| **In prose, as a code token / tag name** | Backticks, roman | `<lex>m.</lex>`, `<ls>RV.</ls>`, `aMSa` (when discussing the SLP1 form) |
| **In code-blocks** | SLP1 verbatim | `<L>9<pc>1,1<k1>aMS<k2>aMS<e>1` |
| **In Devanagari display** | Cologne web display only | अंश, अंशु, ऋषि |

The transcoders live in [`mwtranscode/`](https://github.com/sanskrit-lexicon/MWS/tree/master/mwtranscode). Use [`mw_transcode.py`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwtranscode/mw_transcode.py) for batch conversion.

### Vedic accent

| Context | Marker | Example |
|---|---|---|
| In `<k2>` SLP1 | `/` after a vowel = *udātta* | `a/MSa` = *áṃśa* |
| In IAST display | Acute accent over the vowel | *áṃśa*, *aṃśú* |
| Anudātta and svarita | Not separately marked in `mw.txt` | — |

[16.6% of `<k2>` fields](#vedic-accent-coverage) carry an accent mark.

### Compounds

| Context | Marker | Example |
|---|---|---|
| In `<k1>` lookup key | No separator | `aMSujAla` |
| In `<k2>` display key | Em-dash `—` between members | `aMSu—jAla` |
| In IAST prose | Hyphen `-` | *aṃśu-jāla* |
| `<e>` hierarchy code | `3` (or `3A`/`3B`/`3C`) | [L57 *aṃśu-jāla*](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L199) |

### Record references

| Element | Format | Example |
|---|---|---|
| In data file | `<L>N` with integer N | `<L>9`, `<L>10`, `<L>57` |
| Sub-entry | `<L>N.NNN` with decimal | `<L>4.020`, `<L>4.022` |
| In prose | `L<number>` (no period) | `L9`, `L57`, `L4.020` |
| Page/column source | `<pc>P,C` (data) → "p. P, col. C" (prose) | `<pc>1,2` → p. 1, col. 2 |
| Line number in GitHub URL | `mw.txt#L<line>` (raw file line, not record) | [`mw.txt#L52`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L52) for record L9 |
| Range of records | GitHub line-range syntax | [`mw.txt#L58-L82`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L58-L82) for L11–L19 |

### Citation conventions

| Element | Format | Notes |
|---|---|---|
| `<ls>` tag content | Roman (no italic), abbreviated work title | `<ls>RV.</ls>`, `<ls>MBh.</ls>` |
| With numeric coordinate | Roman volume/book + Arabic verse/sutra | `<ls>RV. v, 86, 5</ls>` (book 5, hymn 86, verse 5) |
| With explicit expansion in `n=` attribute | `<ls n="canonical short">visible</ls>` | 12,779 of `<ab n="…">`; see [DATA_DICTIONARY](DATA_DICTIONARY.md#ab-n-variant) |
| In prose, when discussed | Backticks for code token | `RV.`, `<ls>MBh.</ls>` |
| Editorial markers (not literary) | Same backtick formatting, but flag the editorial status | `L.`, `ib.`, `W.`, `MW.`, `Cat.` — [see callout](DICT_PROFILE.md#citation-markers--not-all-are-literary-works) |

### Grammatical category in `<lex>`

| Marker | Meaning | Count |
|---|---|--:|
| `m.` | masculine noun | 63,826 |
| `f.` | feminine noun | 31,534 |
| `n.` | neuter noun | 34,349 |
| `mfn.` | adjective (declines in all three genders) | 50,636 |
| `mn.` | masculine or neuter | small |
| `ind.` | indeclinable | 5,516 |

Verb-class abbreviations (`cl. 1.`, `cl. 10.`) and voice markers (`P.` Parasmaipada, `Ā.` Ātmanepada) live in `<ab>` rather than `<lex>` — see [DATA_DICTIONARY](DATA_DICTIONARY.md#abbreviations-used-in-lex-rather-than-ab).

### `<e>` hierarchy code

A single-letter optional suffix marks variants. Full inventory in [Entry hierarchy distribution](#entry-hierarchy-distribution).

| Pattern | Role |
|---|---|
| `<e>1` | Top-level entry (main headword) |
| `<e>1A` | Continuation sense (additional meanings of the immediately-preceding `<e>1`) |
| `<e>1B`, `<e>1C` | Top-level variant within same headword group |
| `<e>2` | Derived form (suffix derivative: `-aka`, `-in`, `-ya`, …) |
| `<e>2A`, `<e>2B`, `<e>2E` | Derived sub-variants |
| `<e>3` | Compound sub-entry (`<k2>` has em-dash) |
| `<e>3A`, `<e>3B`, `<e>3C` | Compound sub-variants |
| `<e>4` | Specialised hierarchy (rarer) |

### Inline non-XML markup

| Marker | Role | Example |
|---|---|---|
| `¦` | Separator between headword and gloss body | `<s>aMSa</s> ¦ <lex>m.</lex> …` |
| `{#…#}` | Devanagari / SLP1 inline span (rendered as Devanagari) | `{#kf#}` → कृ |
| `{%…%}` | Italic text span (rendered as italic in display) | `{%also written%}` |
| `<srs/>` | Self-closing visarga-ligature marker | `<srs/>` |

### Correction-record format

In-file corrections use double-brace syntax (processed by [`updateByLine.py`](https://github.com/sanskrit-lexicon/MWS), never appears in rendered output):

```
{{old text -> new text || YYYY-MM-DD | author | URL |}}
```

---

## Common tags

Tag counts shown are from the markup-fix audit of `mw.txt` (2026-05) — see
[DATA_DICTIONARY.md](DATA_DICTIONARY.md) for the full inventory.

| Tag | Count | Role | Example |
|---|--:|---|---|
| `<s>…</s>` | 350,610 | Sanskrit text span | `<s>aMSa</s>` |
| `<lex>…</lex>` | 201,941 | Grammatical category | `<lex>m.</lex>`, `<lex>mfn.</lex>` |
| `<ab>…</ab>` | 194,879 | Abbreviation | `<ab>cf.</ab>`, `<ab>cl.</ab>` |
| `<ls>…</ls>` | 320,827 | Literary source reference | `<ls>RV.</ls>`, `<ls>MBh.</ls>` |
| `<lang>…</lang>` | 3,968 | Foreign language tag | `<lang>Gk.</lang>`, `<lang>Lat.</lang>` |
| `<bot>…</bot>` | 8,923 | Botanical name | `<bot>Ficus religiosa</bot>` |
| `<bio>…</bio>` | 358 | Biographical / personal name | `<bio>Pāṇini</bio>` |
| `<i>…</i>` | 197 | Italic (in print) | `<i>id est</i>` |
| `<hom>N.</hom>` | many | Homophone disambiguator | `<hom>1.</hom>` |
| `<s1>…</s1>` | many | Sanskrit proper name (rendered untranscoded) | `<s1>Viṣṇu</s1>` |
| `<info …/>` | 292,603 | Self-closing machine annotation | `<info lex="m"/>` |
| `<srs/>` | many | Visarga-ligature self-closing marker | `<srs/>` |
| `{%…%}` | many | Italic span (inline) | `{%also written%}` |
| `{#…#}` | many | Devanagari / alternate script | `{#कृ#}` |

`<zoo>` is unused in MW (0 occurrences) — zoological names appear inside `<bot>`
or unmarked prose.

**`<ab n="…">` variant:** 12,779 abbreviation tags carry an explicit expansion in
the `n` attribute (`<ab n="some full phrase">X</ab>`), bypassing the lookup table.
These all have real (non-placeholder) expansions — see [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

---

## Abbreviations — cheat sheet

A reading-time cheat sheet. Two distinct files cover MW's `<ab>` abbreviation system:

| Purpose | File | Entries | Last updated |
|---|---|--:|---|
| **Operative tooltip list** (feeds the web display via `mwab.sqlite`) | [`csl-pywork/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt`](https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt) | 424 | [2024-08-03](https://github.com/sanskrit-lexicon/csl-pywork/commits/master/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt) |
| **Research / audit copy** (with `<INFER/>`/`<UNMARKED>`/`<UNUSED/>` status markers) | [`MWS/mwabbreviations/mwab_input.txt`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwabbreviations/mwab_input.txt) | 267 | [2017-11-08](https://github.com/sanskrit-lexicon/MWS/commits/master/mwabbreviations/mwab_input.txt) |

Use the **csl-pywork** copy when you need the current tooltip-rendering definition; use the **MWS** copy when you need the `<INFER/>`/`<UNMARKED>` provenance flags. The formats differ — csl-pywork records [`<count>` usage statistics](https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt) (`<count>lex,32943 ab,37</count>`), MWS records [`<id>` round-trip checks and status flags](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DATA_DICTIONARY.md#status-markers-in-mwab_inputtxt). Both resolve via the CDSL tooltip system on the web interface.

| Abbreviation | Expansion |
|---|---|
| `m.` / `f.` / `n.` | masculine / feminine / neuter |
| `mfn.` | adjective (declines in all three genders) |
| `ind.` | indeclinable |
| `cl.` *N* | verb class *N* (1–10, the Pāṇinian *gaṇas*) |
| `P.` | Parasmaipada (active) |
| `Ā.` | Ātmanepada (middle / reflexive) |
| `cf.` | compare (*confer*) |
| `fr.` | from (etymology marker) |
| `e.g.` | for example |
| `q.v.` | which see (*quod vide*) |
| `v.l.` | variant reading (*varia lectio*) |
| `w.r.` | wrong reading |
| `perf.` | perfect tense |
| `aor.` | aorist |
| `ifc.` | *in fine compositi* — at the end of a compound |
| `N.` | name (proper noun) |
| `L.` | **Lexicographers** — attestation only in indigenous Sanskrit lexicons (a hedge, not a primary citation) |

---

## Literary source references

Source references appear as `<ls>X</ls>` where `X` is an abbreviated title.
The full list with expansions is on the
[CDSL abbreviations page](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWSScan/2020/web/webtc/abbrev.php).

Most-cited sources in `mw.txt`:

| Abbreviation | Work |
|---|---|
| `RV.` | Rigveda |
| `AV.` | Atharvaveda |
| `ŚBr.` | Śatapatha-Brāhmaṇa |
| `TBr.` | Taittirīya-Brāhmaṇa |
| `TS.` | Taittirīya-Saṃhitā |
| `TāṇḍyaBr.` | Tāṇḍya-Mahābrāhmaṇa |
| `MBh.` | Mahābhārata |
| `R.` | Rāmāyaṇa |
| `BhP.` | Bhāgavata-Purāṇa |
| `Mn.` | Manu-Smṛti |
| `Pāṇ.` (or `P.` after a number) | Aṣṭādhyāyī of Pāṇini |
| `Suśr.` | Suśruta-Saṃhitā (medical) |
| `Yājñ.` | Yājñavalkya-Smṛti |
| `T.` | Tantric sources (collective) |
| `L.` | Lexicographers |

When a numeric coordinate follows (e.g. `<ls>RV. v, 86, 5</ls>`), it points to
book / hymn / verse (or whatever the work's own internal numbering scheme is).

### The mwauthorities system

The `mwauthorities/` directory in this repo is the authority record for MW's
"List of Works and Authors" — the two-page bibliography that opens the 1899 print.

| File | Purpose |
|---|---|
| `MWWorksAuthorsCurrentMarkup3.xml` | Structured XML authority record prepared by Peter Scharf and Malcolm Hyman (Sanskrit Library, ca. 2010). Follows the `mw-authorities.rnc` schema. |
| `mwauthorities_init.txt` | Simplified text form of the authority record; includes post-Scharf/Hyman revisions for Kielhorn and *Kauṣītaki-Brāhmaṇa*. |
| `linkmwauthorities_init.txt` | Three-column tab-delimited file: `<ls>` abbreviation as it appears in `monier.xml` · occurrence count · authority-record abbreviation. Establishes the link between in-text citation spellings and the authority record. |
| `mwauth.txt` | Amalgam of the above two files; intended as the basis for further corrections to `<ls>` citation data. |
| `tooltip.txt` | Per-source expansion strings used for hover text in the CDSL web display; generated by `tooltip.py` from `mwauth.txt`. Prefers `<expandNorm>` over `<expandMW>` where both exist. |

The CDSL web display uses [`linkmwauthorities_init.txt`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/linkmwauthorities_init.txt) to resolve a `<ls>` tag's
abbreviation to a bibliographic record and, where a scan link exists, to an
archive.org or similar URL — enabling click-through to the cited passage.
Requests to add a new scan link use the [**Link target** issue template](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/.github/ISSUE_TEMPLATE/link-target.yml).

### Coverage of `<ls>` citations

Computed from the 2026-05 audit of [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) cross-referenced with [linkmwauthorities_init.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/linkmwauthorities_init.txt) and [tooltip.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/tooltip.txt).

| Metric | Value |
|---|---|
| Total `<ls>` citations | **311,932** |
| Unique `<ls>` abbreviations | **821** |
| With record in [linkmwauthorities_init.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/linkmwauthorities_init.txt) | 232 abbreviations (28.3%) — covering 199,743 citations (**64.0%**) |
| With tooltip expansion in [tooltip.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/tooltip.txt) | 603 abbreviations (73.4%) — covering 299,846 citations (**96.1%**) |
| Orphan abbreviations (no authority record) | 589 (71.7% of uniques, but only 36.0% of citations) |
| With numeric coordinate (e.g. *RV. v, 86, 5*) | **47,227 (15.1%)** — points to a specific verse |
| &nbsp;&nbsp;— with Roman book number (e.g. *v, 86*) | 43,898 |
| &nbsp;&nbsp;— with Arabic numbers only | 3,212 |
| Bare work citation (no coordinate) | **264,705 (84.9%)** — work named, no locus |

### Top 25 most-cited sources

The five top sources include **two editorial markers** (`L.`, `ib.`) — see [DICT_PROFILE.md Citation markers](DICT_PROFILE.md#citation-markers--not-all-are-literary-works) for why they're not literary works.

| Rank | Source | Count | Identity |
|--:|---|--:|---|
| 1 | `L.` | 40,213 | **[Lexicographers](DICT_PROFILE.md#citation-markers--not-all-are-literary-works)** — editorial hedge, not a work |
| 2 | `MBh.` | 28,047 | [Mahābhārata](https://en.wikipedia.org/wiki/Mahabharata) |
| 3 | `RV.` | 15,916 | [Rigveda](https://en.wikipedia.org/wiki/Rigveda) |
| 4 | `R.` | 10,811 | [Rāmāyaṇa](https://en.wikipedia.org/wiki/Ramayana) |
| 5 | `ib.` | 10,100 | ***ibidem*** — refers to immediately preceding `<ls>` |
| 6 | `Pāṇ.` | 8,527 | [Aṣṭādhyāyī of Pāṇini](https://en.wikipedia.org/wiki/A%E1%B9%A3%E1%B9%AD%C4%81dhy%C4%81y%C4%AB) |
| 7 | `BhP.` | 8,478 | [Bhāgavata-Purāṇa](https://en.wikipedia.org/wiki/Bhagavata_Purana) |
| 8 | `W.` | 8,286 | Wilson — [H.H. Wilson's 1832 dictionary](https://github.com/sanskrit-lexicon/WIL) |
| 9 | `AV.` | 7,081 | [Atharvaveda](https://en.wikipedia.org/wiki/Atharvaveda) |
| 10 | `ŚBr.` | 7,029 | [Śatapatha-Brāhmaṇa](https://en.wikipedia.org/wiki/Shatapatha_Brahmana) |
| 11 | `Mn.` | 7,010 | [Manu-Smṛti](https://en.wikipedia.org/wiki/Manusmriti) |
| 12 | `Kathās.` | 6,757 | [Kathāsaritsāgara](https://en.wikipedia.org/wiki/Kathasaritsagara) |
| 13 | `Hariv.` | 6,314 | [Harivaṃśa](https://en.wikipedia.org/wiki/Harivamsa) |
| 14 | `Suśr.` | 6,200 | [Suśruta-Saṃhitā](https://en.wikipedia.org/wiki/Sushruta_Samhita) (medical) |
| 15 | `MW.` | 5,711 | Monier-Williams' own annotation (self-reference) |
| 16 | `Cat.` | 5,302 | Catalogue (manuscript catalogues) |
| 17 | `Kāv.` | 4,667 | Kāvya / Kāvyādarśa |
| 18 | `VarBṛS.` | 3,467 | Varāhamihira's [Bṛhatsaṃhitā](https://en.wikipedia.org/wiki/Brihat_Samhita) |
| 19 | `Rājat.` | 3,410 | [Rājataraṅgiṇī](https://en.wikipedia.org/wiki/Rajatarangini) |
| 20 | `TS.` | 3,207 | [Taittirīya-Saṃhitā](https://en.wikipedia.org/wiki/Taittiriya_Samhita) |
| 21 | `VS.` | 2,998 | [Vājasaneyi-Saṃhitā](https://en.wikipedia.org/wiki/Vajasaneyi_Samhita) |
| 22 | `Pañcat.` | 2,670 | [Pañcatantra](https://en.wikipedia.org/wiki/Panchatantra) |
| 23 | `Ragh.` | 2,654 | Kālidāsa's [Raghuvaṃśa](https://en.wikipedia.org/wiki/Raghuvamsha) |
| 24 | `KātyŚr.` | 2,537 | Kātyāyana-Śrautasūtra |
| 25 | `Yājñ.` | 2,249 | [Yājñavalkya-Smṛti](https://en.wikipedia.org/wiki/Yajnavalkya_Smriti) |

### Period breakdown

Manual classification of top sources, covering ~73% of total citations:

| Period | Citations | % of all `<ls>` |
|---|--:|--:|
| Epic (MBh., R., Hariv.) | 45,172 | 14.5% |
| [**Lexicographer (L.)**](DICT_PROFILE.md#citation-markers--not-all-are-literary-works) | **40,213** | **12.9%** |
| Vedic Saṃhitā (RV., AV., TS., VS., …) | 30,507 | 9.8% |
| Editorial (ib., W., MW., Cat., Sch., Comm.) | 29,399 | 9.4% |
| Sūtra (Pāṇ., KātyŚr., …) | 13,517 | 4.3% |
| Brāhmaṇa (ŚBr., TBr., …) | 10,700 | 3.4% |
| Smṛti (Mn., Yājñ., …) | 10,017 | 3.2% |
| Story (Kathās., Pañcat.) | 9,427 | 3.0% |
| Classical kāvya (Ragh., Kum., Megh., …) | 8,835 | 2.8% |
| Classical Purāṇa (BhP.) | 8,478 | 2.7% |
| Medicine (Suśr.) | 6,201 | 2.0% |
| Astronomy (VarBṛS.) | 3,936 | 1.3% |
| Chronicle (Rājat.) | 3,410 | 1.1% |
| Upaniṣad | 1,550 | 0.5% |

**Reading the table:** [Epic](https://en.wikipedia.org/wiki/Itihasa) sources are the most-cited *real* literature, but the **lexicographer hedge `L.` is just behind** — every 8th citation in MW means "no textual attestation found." This is a signal MW is honest about evidentiary strength.

### Top orphan abbreviations

These are highly-cited `<ls>` abbreviations that have **no authority record** in [linkmwauthorities_init.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/linkmwauthorities_init.txt) — a fixable gap.

| Abbreviation | Citations | Identity |
|---|--:|---|
| `ib.` | 10,100 | *ibidem* — not a work, refers to the previous `<ls>`; no record by design |
| `Pāṇ.` | 8,527 | [Aṣṭādhyāyī of Pāṇini](https://en.wikipedia.org/wiki/A%E1%B9%A3%E1%B9%AD%C4%81dhy%C4%81y%C4%AB) — needs a record |
| `ŚBr.` | 7,029 | [Śatapatha-Brāhmaṇa](https://en.wikipedia.org/wiki/Shatapatha_Brahmana) — needs a record |
| `Kathās.` | 6,757 | [Kathāsaritsāgara](https://en.wikipedia.org/wiki/Kathasaritsagara) — needs a record |
| `Suśr.` | 6,200 | [Suśruta-Saṃhitā](https://en.wikipedia.org/wiki/Sushruta_Samhita) — needs a record |
| `Kāv.` | 4,667 | Kāvyādarśa — needs a record |
| `VarBṛS.` | 3,467 | [Bṛhatsaṃhitā](https://en.wikipedia.org/wiki/Brihat_Samhita) — needs a record |

---

## Structural & content stats

From the 2026-05 audit of [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt).

### Entry hierarchy distribution

**286,561** entries total. The `<e>` hierarchy code shows MW's structural skeleton:

| Code | Role | Count | % |
|---|---|--:|--:|
| `<e>3` | Compound sub-entry (em-dash in `<k2>`) | 112,183 | 39.1% |
| `<e>2` | Derived form (`-aka`, `-in`, `-ya`, …) | 32,499 | 11.3% |
| `<e>1` | Top-level entry (main headword) | 32,116 | 11.2% |
| `<e>2A` | Derived sub-variant | 21,421 | 7.5% |
| `<e>2B` | Derived sub-variant | 17,463 | 6.1% |
| `<e>4` | Specialised hierarchy | 17,091 | 6.0% |
| `<e>3A` | Compound sub-variant | 16,542 | 5.8% |
| `<e>3B` | Compound sub-variant | 14,943 | 5.2% |
| `<e>1B` | Top-level variant | 9,703 | 3.4% |
| `<e>1A` | Continuation sense (sees [L11–L19](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt#L58-L82) of *áṃśa*) | 9,294 | 3.2% |
| `<e>3C` | Compound sub-variant | 781 | 0.3% |
| `<e>1C` | Top-level variant | 637 | 0.2% |
| (others) | smaller categories | < 600 each | < 0.5% |

**Reading the table:** Compound sub-entries dominate (~57% across all `<e>3*` variants), reflecting Sanskrit's heavily-agglutinative compounding. Derived forms account for ~25%. Only ~15% are top-level main headwords — the rest are sub-entries hanging off a parent.

### Entry-type breakdown by content

From the `<lex>` field on 185,888 entries with a grammatical category:

| Type | Marker | Count | % of `<lex>` |
|---|---|--:|--:|
| Masculine noun | `m.` | 63,826 | 34.3% |
| Adjective | `mfn.` | 50,636 | 27.2% |
| Neuter noun | `n.` | 34,349 | 18.5% |
| Feminine noun | `f.` | 31,534 | 17.0% |
| Indeclinable | `ind.` | 5,516 | 3.0% |

**Verbal-root entries** (with `<info verb="genuineroot"/>`): **750**.

See [DICT_PROFILE.md Article types](DICT_PROFILE.md#article-types--what-youll-encounter) for live samples of each type.

### IE cognate density — `<lang>` breakdown

3,960 `<lang>` tags across 112 distinct values. Top 12 languages by tag count:

| Language | Tags | Notes |
|---|--:|---|
| Ved. | 612 | Vedic-only attestation marker (not strictly IE) |
| Lat. | 527 | [Latin](https://en.wikipedia.org/wiki/Latin) |
| Gk. | 504 | [Ancient Greek](https://en.wikipedia.org/wiki/Ancient_Greek) |
| ep. | 328 | Epic Sanskrit (period marker) |
| Prākṛt | 227 | [Prakrit](https://en.wikipedia.org/wiki/Prakrit) |
| Germ. | 210 | [German](https://en.wikipedia.org/wiki/German_language) |
| Goth. | 200 | [Gothic](https://en.wikipedia.org/wiki/Gothic_language) |
| Eng. | 190 | English |
| Lith. | 182 | [Lithuanian](https://en.wikipedia.org/wiki/Lithuanian_language) |
| Zd. | 139 | [Zend (Avestan)](https://en.wikipedia.org/wiki/Avestan) |
| Angl.Sax. | 129 | [Anglo-Saxon](https://en.wikipedia.org/wiki/Old_English) |
| Slav. | 111 | [Slavonic](https://en.wikipedia.org/wiki/Slavic_languages) |

This **IE comparative reach is MW's distinctive contribution** vs other Sanskrit dictionaries — see [DICT_PROFILE.md Scholarly significance](DICT_PROFILE.md#scholarly-significance) for context.

### Botanical & biographical tag stats

| Tag | Count | Role |
|---|--:|---|
| `<bot>` | 8,923 | Botanical Latin name (e.g. `<bot>Ficus religiosa</bot>`) |
| `<bio>` | 358 | Biographical / mythological figure (e.g. `<bio>Pāṇini</bio>`) |
| `<zoo>` | 0 | Zoological — unused; zoological names appear inside `<bot>` or unmarked |

### Vedic accent coverage

| Metric | Count | % |
|---|--:|--:|
| Total `<k2>` fields | 286,561 | — |
| `<k2>` with at least one `/` (udātta) | **47,598** | **16.6%** |
| `<k2>` with em-dash compound marker | 182,023 | 63.5% |

The 16.6% accent coverage is partial. For accent-sensitive Vedic work, [Grassmann's RV-dictionary (GRA)](https://github.com/sanskrit-lexicon/GRA) remains the reference.

### Cross-reference patterns

| Marker | Count | Role |
|---|--:|---|
| `<ab>cf.</ab>` | 11,620 | "compare" — sibling cross-reference |
| `<ab>id.</ab>` | 4,401 | "the same meaning as preceding" |
| `q.v.` | 3,551 | "which see" — see the named entry |
| `<ab>w.r.</ab>` | 1,992 | "wrong reading" |

---

## Dictionary-specific conventions

- **Vedic accents** in `<k2>`: the `/` character after a vowel marks the *udātta*
  (high pitch). Anudātta and svarita are not separately marked in `mw.txt`.
- **Homophone numbering** with `<hom>1.</hom>`, `<hom>2.</hom>` disambiguates
  identical-spelled but etymologically distinct headwords (Sanskrit has many).
- **`L.` (lexicographers) citations** are explicitly hedged: MW signals that the
  form is only known from indigenous Sanskrit lexicons, not from living textual
  attestation. Treat as weaker evidence than a named text citation.
- **Em-dash `—` in `<k2>`** marks compound boundaries (e.g. `aMSu—jAla`); it does
  not appear in `<k1>` because `<k1>` is the lookup key.
- **In-file correction records** use double-brace syntax:
  ```
  {{old text -> new text || YYYY-MM-DD | author | URL |}}
  ```
  Processed by `updateByLine.py`; never appears in rendered output.
- **Supplement entries** (from the 1899 print supplement) are integrated into the
  main entry sequence; see [6602-entries-from-supplements-MW.txt](6602-entries-from-supplements-MW.txt).

---

## Worked examples — three entries from `mw.txt`

### Example 1 — Verbal root with hedge citation

```
<L>9<pc>1,1<k1>aMS<k2>aMS<e>1
<s>aMS</s> ¦ <ab>cl.</ab> 10. <ab>P.</ab> <s>aMSayati</s>, to divide, distribute,
<ls>L.</ls>; also occasionally <ab>Ā.</ab> <s>aMSayate</s>, <ls>L.</ls>;
also <s>aMSApayati</s>, <ls>L.</ls><info verb="genuineroot" cp="10P,10Ā"/>
<LEND>
```

**Reading:**

Record 9, page 1 col. 1. Verbal root *aṃś* (no accent). The entry tells us:
- **Class 10** (the *curādi* gaṇa — characteristic 3rd-sg form ends in *-ayati*).
- **Parasmaipada** with form *aṃśayati*, meaning "to divide, distribute."
- All three forms (Parasmaipada *aṃśayati*, Ātmanepada *aṃśayate*, and what
  appears to be a causative *aṃśāpayati*) are cited as `<ls>L.</ls>` —
  **lexicographers only**. MW is telling us this root is known from indigenous
  Sanskrit lexicons but has no firm textual attestation. Compare Sample 2 below,
  where MW openly suggests this root may be a back-formation.
- The `<info>` packet records: this is treated as a `genuineroot`, classes 10P
  and 10Ā.

### Example 2 — Masculine noun with etymological commentary

```
<L>10<pc>1,1<k1>aMSa<k2>a/MSa<e>1
<s>a/MSa</s> ¦ <lex>m.</lex> (probably <ab>fr.</ab> √ <hom>1.</hom> <s>aS</s>,
<ab>perf.</ab> <s>An-a/MSa</s>, and not from the above √ <s>aMS</s>
fictitiously formed to serve as root), a share, portion, part, party
<info lex="m"/>
<LEND>
```

**Reading:**

Record 10, page 1 col. 1. Headword *áṃśa* (note the `/` accent in `<k2>` marking
*udātta* on the first vowel). Masculine noun.

The parenthetical is MW's **etymological reasoning**, in his own editorial voice:

- "probably from root *aś* (homophone 1)" — referring to the first listed root *aś*
  (he uses `<hom>1.</hom>` because Sanskrit has multiple roots of that shape).
- "perfect *ān-áṃśa*" — the perfect form *ān-aṃśa* is cited as evidence that the
  noun derives from *aś* rather than from the *aṃś* of Sample 1.
- "and not from the above √ *aṃś* fictitiously formed to serve as root" — MW
  explicitly says he believes *aṃś* (Sample 1) is a back-formation invented to
  rationalise the noun *aṃśa*. This is a window into the philological reasoning
  driving the 1899 edition.

Glosses: "a share, portion, part, party."

Nine `<e>1A` sub-entries follow (records 11–19) adding more meanings:
*partition* (inheritance), *share of booty*, *earnest money*,
*stake (in betting)* (with `<ls>RV. v, 86, 5</ls>` — its first real
textual citation!), *a lot*, *fraction denominator*, *degree of latitude or
longitude*, *a day* (`L.`), and *name of an Āditya*.

### Example 3 — Compound sub-entry under a parent stem

```
<L>57<pc>1,2<k1>aMSujAla<k2>aMSu—jAla<e>3
<s>aMSu—jAla</s> ¦ <lex>n.</lex> a collection of rays, blaze of light.
<info lex="n"/>
<LEND>
```

**Reading:**

Record 57, page 1 col. 2. Compound *aṃśu-jāla* = *aṃśu* "ray" + *jāla* "net,
collection."

- `<k1>aMSujAla` — concatenated lookup key (no dash).
- `<k2>aMSu—jAla` — display key with em-dash showing the compound boundary.
- `<e>3` — third-level entry, marking a compound under the parent *aṃśu* whose
  main entry is `<L>47` (records 48–56 are continuation sub-entries `<e>1A` of
  *aṃśu*; compound sub-entries `<e>3` begin at record 57).
- Neuter noun: "a collection of rays, blaze of light."
- No `<ls>` citation: transparent semantic compounds without attested-text
  citations are common — MW glosses the meaning without naming a primary
  source.

Compound sub-entries in MW are stored as siblings of the parent rather than as
nested records, with the parent–child relationship implicit in adjacency and
the `<e>3` hierarchy code.
{% endraw %}
