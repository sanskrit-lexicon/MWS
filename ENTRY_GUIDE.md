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

---

## Abbreviations (canonical list in `mwabbreviations/mwab_input.txt`)

A reading-time cheat sheet. Full expansions live in
[mwabbreviations/mwab_input.txt](mwabbreviations/mwab_input.txt) and resolve via
the CDSL tooltip system on the web interface.

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
