# Entry Reading Guide — MWS

A practical reference for reading and interpreting entries in `mw.txt`.

For the full org-wide primer (encoding, tag system, abbreviation lookup) see the
[Entry Reading Primer](https://github.com/sanskrit-lexicon/csl-homepage/blob/master/docs/ENTRY_READING_PRIMER.md).

---

## Record structure

Each entry spans from an `<L>` header to a `<LEND>` marker:

```
<L>10<pc>1,1<k1>aMSa<k2>a/MSa<e>1
<s>a/MSa</s> ¦ <lex>m.</lex> a share, portion, part<info lex="m"/>
<LEND>
```

| Part | Meaning |
|---|---|
| `<L>N` | Record number (decimal sub-entries like `103.1` are homophone variants) |
| `<pc>P,C` | Page and column in the **1899 print edition** |
| `<k1>` | Headword in SLP1, no accents — used for lookups |
| `<k2>` | Headword in SLP1, with Vedic accent marks where present |
| `¦` | Separates the headword span from the definition body |
| `<LEND>` | End of entry |

---

## Encoding

Sanskrit text in the data file is stored in **SLP1** (a lossless ASCII scheme).
The web interface and exports transcode it to IAST (roman) or Devanagari on the fly.

| Display | Example | SLP1 source |
|---|---|---|
| IAST | *nara* | `nara` |
| IAST | *mahārāja* | `mahArAja` |
| IAST | *ṛṣi* | `fzi` |
| Devanagari | नर | `nara` |

SLP1 consonant quick-reference: `k K g G N c C j J Y w W q Q R t T d D n p P b B m y r l v S z s h`.  
Vowels: `a A i I u U f F x X e E o O M H`.

---

## Common tags

| Tag | Role | Example (as it appears in file) |
|---|---|---|
| `<s>…</s>` | Sanskrit text span | `<s>aMSa</s>` |
| `<lex>…</lex>` | Grammatical category | `<lex>m.</lex>` |
| `<ab>…</ab>` | Abbreviation | `<ab>cf.</ab>` · `<ab>cl.</ab>` |
| `<ls>…</ls>` | Literary source reference | `<ls>RV.</ls>` |
| `<lang>…</lang>` | Foreign language label | `<lang>Gk.</lang>` |
| `<bot>…</bot>` | Botanical name | `<bot>Ficus religiosa</bot>` |
| `<bio>…</bio>` | Person / biographical name | `<bio>Pāṇini</bio>` |
| `<zoo>…</zoo>` | Zoological name | `<zoo>Delphinus gangeticus</zoo>` |
| `<hom>N.</hom>` | Homophone number | `<hom>1.</hom>` |
| `<s1>…</s1>` | Proper name / untranscoded Sanskrit | `<s1>Viṣṇu</s1>` |
| `<info …/>` | Grammatical attribute packet | `<info lex="m:f:n"/>` |
| `<srs/>` | Visarga ligature marker | (self-closing) |
| `{%…%}` | Italic span | `{%also written%}` |
| `{#…#}` | Devanagari / alternate script span | `{#कृ#}` |

---

## Abbreviations

Abbreviations appear as `<ab>X</ab>` and expand via the CDSL tooltip system.
Common ones you will encounter in MWS:

| Abbreviation | Expansion |
|---|---|
| `m.` | masculine |
| `f.` | feminine |
| `n.` | neuter |
| `mfn.` | adjective (can be m./f./n.) |
| `ind.` | indeclinable |
| `cf.` | compare (*confer*) |
| `v.l.` | variant reading (*varia lectio*) |
| `fr.` | from (etymology marker) |
| `cl.` | class (of a verbal root) |
| `P.` | Parasmaipada (active voice) |
| `Ā.` | Ātmanepada (middle/reflexive voice) |
| `perf.` | perfect (tense) |
| `aor.` | aorist |
| `ifc.` | in fine compositi (at the end of a compound) |
| `e.g.` | for example |
| `q.v.` | which see (*quod vide*) |
| `w.r.` | wrong reading |
| `N.` | name (proper noun) |
| `L.` | lexicographers (late or uncertain attestation) |

<!-- Add MWS-specific abbreviations here. The canonical list is at
https://github.com/sanskrit-lexicon/MWS/blob/master/mwabbreviations/mwab_input.txt -->

---

## Literary source references

Source references appear as `<ls>X</ls>` where `X` is an abbreviated title.
Hover on the web interface to see the expansion, or see the abbreviation page:
<https://www.sanskrit-lexicon.uni-koeln.de/scans/MWSScan/2020/web/webtc/abbrev.php>

Common sources in MWS:

| Abbreviation | Work |
|---|---|
| `RV.` | Rigveda |
| `AV.` | Atharvaveda |
| `ŚBr.` | Śatapatha-Brāhmaṇa |
| `TBr.` | Taittirīya-Brāhmaṇa |
| `MBh.` | Mahābhārata |
| `R.` | Rāmāyaṇa |
| `BhP.` | Bhāgavata-Purāṇa |
| `Pāṇ.` / `P.` | Aṣṭādhyāyī of Pāṇini |
| `Suśr.` | Suśruta-saṃhitā (medical) |
| `Yājñ.` | Yājñavalkya-smṛti |
| `T.` | Tantric sources (general) |
| `L.` | Lexicographers |

<!-- Add MWS-specific source abbreviations here. -->

---

## Dict-specific conventions

MW uses a rich set of paired tag types (22 types, vs. 5 in PWG, 12 in PWK) including
specialized tags for structure: `<s1>` (proper names not transcoded inline), `<etym>` (etymological
cognates in other languages), `<ns>` (notes on Sanskrit form), `<pcol>` (page column markers),
`<old>` and `<new>` (in-file correction records, with `<chg>` wrapper), `<hom>` (homophone
index), and `<srs/>` (visarga-r ligature self-closing tag, used 37,041 times).

The `<e>` hierarchy codes in the record header distinguish entry types:
- `<e>1` — main entry (root word or simple headword)
- `<e>1A` — continuation sub-entry (additional meanings of the same headword)
- `<e>2` — derived form / secondary entry
- `<e>3` — compound entry

Correction records embedded in mw.txt use the format:
```
{{old text -> new text || YYYY-MM-DD | author | URL |}}
```
These are processed by the `updateByLine.py` toolchain and do not appear in the rendered dictionary.

---

## Sample entries with annotation

### Entry 1 — simple noun with etymology

```
<L>10<pc>1,1<k1>aMSa<k2>a/MSa<e>1
<s>a/MSa</s> ¦ <lex>m.</lex> (probably <ab>fr.</ab> √ <hom>1.</hom> <s>aS</s>, <ab>perf.</ab> <s>An-a/MSa</s>, and not from the above √ <s>aMS</s> fictitiously formed to serve as root), a share, portion, part, party<info lex="m"/>
<LEND>
```

**Reading:** [DRAFT] Record L10, print p.1 col.1. Headword `aṃśa`, masculine noun (lex=m). Etymology: probably from root `aś` (√1 aś), with perfect form `ān-aṃśa`; distinguishes from a later fictitious root `aṃś`. Primary meanings: share, portion, part, party. Additional meanings follow in sub-entries L11–L19 with `<e>1A` codes (partition, inheritance, booty share, stake, lot, fraction denominator, degree of latitude, day, name of an Āditya). — [reviewer: verify etymology gloss and sub-entry enumeration]

---

### Entry 2 — verbal root with source reference

```
<L>9<pc>1,1<k1>aMS<k2>aMS<e>1
<s>aMS</s> ¦ <ab>cl.</ab> 10. <ab>P.</ab> <s>aMSayati</s>, to divide, distribute, <ls>L.</ls>; also occasionally <ab>Ā.</ab> <s>aMSayate</s>, <ls>L.</ls>; also <s>aMSApayati</s>, <ls>L.</ls><info verb="genuineroot" cp="10P,10Ā"/>
<LEND>
```

**Reading:** [DRAFT] Record L9, print p.1 col.1. Root `aṃś`. Class 10 verb (gaṇa: curādi). Parasmaipada: `aṃśayati` (to divide, distribute); attestation `L.` = lexicographers only. Also attested in Ātmanepada: `aṃśayate`. Also `aṃśāpayati` (causative form?), all lexicographer-only. The `<info verb="genuineroot"/>` tag classifies this as a root entry in the CDSL verb index. — [reviewer: verify cp="10P,10Ā" expansion and causative interpretation]

---

### Entry 3 — compound

```
<L>57<pc>1,2<k1>aMSujAla<k2>aMSu—jAla<e>3
<s>aMSu—jAla</s> ¦ <lex>n.</lex> a collection of rays, blaze of light.<info lex="n"/>
<LEND>
```

**Reading:** [DRAFT] Record L57, print p.1 col.2. Compound `aṃśu-jāla` (ray + net/collection), neuter. No source citation, which is typical for straightforward descriptive compounds. The `—` in `k2` separates compound members; `<e>3` marks this as a compound sub-entry under the parent headword `aṃśu` (L47 ff.). — [reviewer: confirm print page reference and whether any source citation was omitted]
