---
paper_id: A46
title: "The Lexicographer's Own Method: Monier-Williams' 1899 Preface as a Methodological Document, Read Against the Digitized Dictionary"
status: draft (skeleton, 2/5) — scaffolded 2026-07-09 (H395)
readiness: 2/5
venue: "International Journal of Lexicography / Dictionaries / Historiographia Linguistica — venue choice open (a human decides)"
author: "Mārcis Gasūns, independent scholar ([ORCID 0000-0003-4513-884X](https://orcid.org/0000-0003-4513-884X)), gasyoun@ya.ru — venue + byline to confirm (a human decides)"
data_source: "prefaces/mwpref01–29.md (committed faithful transcription of the 1899 front matter) + csl-orig v02/mw/mw.txt @ 392ed6b; every mw.txt-derived figure recomputed 2026-07-09 by the committed papers/a46_preface_method_stats.py"
---

# The Lexicographer's Own Method: Monier-Williams' 1899 Preface as a Methodological Document, Read Against the Digitized Dictionary

_Created: 09-07-2026 · Last updated: 09-07-2026_

> **Draft status (2026-07-09, H395, Fable 5 `claude-fable-5`).** Manuscript skeleton
> scaffolded from scratch (readiness 1/5 → 2/5) per the `/paper-scaffold` discipline,
> following the A43 house shape. Every mw.txt-derived figure below was **recomputed in
> the scaffolding pass** by
> [`papers/a46_preface_method_stats.py`](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/a46_preface_method_stats.py)
> against [csl-orig `v02/mw/mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/main/v02/mw/mw.txt)
> @ `392ed6b` (2026-06-27); figures taken from this project's earlier committed
> artifacts are cited to those artifacts with their measurement dates and are **not**
> re-derived here. Every preface quotation carries its page file (`mwprefNN`) and
> printed page.
> **Open before submission:** (1) **[@DECIDE]** venue and byline/ORCID confirmation
> (a human decides); (2) §2 Related work is a **labelled stub** — no citations are
> faked at 2/5; a verified literature pass (history of lexicography, MW biography and
> reception, metalexicography of front matter) is the main 2/5 → 3/5 lever; (3) the
> §4.7 collaborator-segment hypothesis is stated but **not yet measured** (TODO);
> (4) the §4.3 citation-coverage figure is per-instance, not per-record — the
> per-record "which entries carry no authority at all" census is a TODO before 3/5.

## Abstract

The 29-page front matter of Monier-Williams' *A Sanskrit-English Dictionary* (Oxford,
1899) is one of the most explicit methodological self-descriptions in 19th-century
lexicography: a preface and a five-section introduction in which the lexicographer
states his arrangement principle, his compression devices, his citation policy, his
accentuation policy, his transliteration rationale, and a page-exact account of who
compiled what. Because the dictionary itself is now fully digitized (286,525 records)
and instrumented with measured statistics, each checkable claim in that front matter
can be paired with the measured reality of the finished work — a *stated-versus-
measured* reading that is impossible for most dictionaries of the period. We present
the preface as a primary methodological document and test its quantitative claims:
the stated growth "to about 180,000 words" against the 194,084 distinct headwords of
the digitization; the stated post-page-60 rule of "no words … without quoting some
authority" against the 320,828-citation apparatus and its measured hedge share; the
stated `L.` convention for lexicographer-only words against its 40,212 instances and
their 31% corpus attestation today; the stated accentuation programme against the
17.0% of records that carry accent marks; the stated root-arranged compromise against
the 2,113 root-flagged records. The result is a case study in how far a lexicographer's
self-declared method matches the artefact he produced — and a demonstration that
digitized dictionaries turn front matter from rhetoric into testable methodology.

## 1. Introduction

Dictionary front matter is usually read as history or as rhetoric; it is rarely
*testable*. For the 1899 Monier-Williams it now is: the complete front matter — title
page, Preface with Postscript (pp. v–x), and the Introduction's five sections
(pp. xi–xxxii) — has been transcribed faithfully page-by-page in this project
([`prefaces/`](https://github.com/sanskrit-lexicon/MWS/tree/master/prefaces),
consolidated in
[`mwpref_all.en.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/prefaces/mwpref_all.en.md)),
and the dictionary it describes exists as a fully digitized, structurally instrumented
text ([csl-orig `mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/main/v02/mw/mw.txt),
286,525 records) with an existing layer of measured statistics built in this
repository (block microanalysis, citation-apparatus verification, root crosswalks,
homonym and compound graphs).

The paper's object is the preface **as a methodological document**: what
Monier-Williams *says* his method is — and, wherever the claim is checkable, what the
finished dictionary *measures as*. Our claims:

1. **A primary-source reading.** The 1899 front matter states an explicit method:
   an etymological-arrangement compromise between a root-arranged lexicon and an
   alphabetic one (§I–II), a declared corpus scope (§III), a defended romanization
   and transliteration scheme (§IV), and a page-exact division of collaborative
   labour (§V). We read these sections systematically, with every claim page-cited
   to the committed transcription (§4).
2. **A stated-versus-measured axis.** For each quantitative or checkable claim we
   pair the lexicographer's statement with the measured value from the digitization —
   recomputed in this pass or cited to a committed, dated artifact of this project
   (§4, inventory in §9). The pairings range from strikingly accurate (the 180,000-word
   estimate, §4.2) to programmatically honest (the admitted non-uniformity of
   accentuation, §4.4).
3. **A method for the genre.** The pairing procedure — transcribed front matter +
   instrumented digitization + per-claim recomputation — generalizes to any digitized
   dictionary whose front matter survives, and turns a neglected genre into an
   evaluable methodological source (§5).

## 2. Related work

> **⬜ STUB (readiness 2/5)** — to be written in a verified literature pass; no
> citations are faked here. Position against four axes: (a) **metalexicography of
> front matter** — the study of dictionary prefaces/outside matter as a genre
> (Hausmann/Wiegand-line reference works; the front-matter chapters of dictionary-
> research handbooks); (b) **history of Sanskrit lexicography** — the
> Böhtlingk–Roth ↔ Monier-Williams relationship and its 19th-century polemics,
> MW's biography and the Boden Chair context; (c) **digitization-era re-evaluation
> of legacy dictionaries** — the Cologne Digital Sanskrit Dictionaries as the
> digitization frame; (d) **this project's own measured layers** — the MWS block
> microanalysis and citation-register series, which supply the measured half of
> the pairing (cross-cited in §9, owned by their own papers per §10). The novelty
> claim to land precisely: not "MW's preface is interesting" but "a dictionary
> preface's methodological claims are here *systematically tested against the
> digitized artefact* — stated method versus measured practice."

## 3. Data and method

### 3.1 The primary source: the 1899 front matter

The object is the complete 29-page front matter of the New Edition (Oxford, Clarendon
Press, 1899), transcribed page-by-page from the Cologne (CDSL) csldoc scans into
[`prefaces/mwpref01–29.md`](https://github.com/sanskrit-lexicon/MWS/tree/master/prefaces)
with per-page scan provenance, and consolidated by
[`build_combined.py`](https://github.com/sanskrit-lexicon/MWS/blob/master/prefaces/build_combined.py)
into [`mwpref_all.en.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/prefaces/mwpref_all.en.md)
(a Russian translation exists in parallel,
[`mwpref_all.ru.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/prefaces/mwpref_all.ru.md)).
Structure (per [`prefaces/README.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/prefaces/README.md)):

| part | printed pages | page files | content |
|---|---|---|---|
| Preface to the New Edition | v–ix | `mwpref02–06` | genesis, relation to Böhtlingk–Roth, scale and delay, the four "principal characteristics", responsibility statement |
| Postscript (M. F. Monier-Williams) | x | `mwpref07` | completion "a few days before his death" (11 April 1899) |
| Introduction §I | xi–xiii | `mwpref08–10` | circumstances of the "peculiar system": Wilson's root-arranged project, the Āryan-root argument |
| Introduction §II | xiv–xix | `mwpref11–16` | the plan: four type-lines, compound grouping, citation policy, accentuation, compression devices |
| Introduction §III | xx–xxi | `mwpref17–18` | declared corpus scope |
| Introduction §IV | xxii–xxx | `mwpref19–27` | romanization rationale and transliteration choices |
| Introduction §V | xxx–xxxii | `mwpref27–29` | collaborators, page-exact segments, sources consulted |

A sibling in-progress transcription set,
[`prefaces/mwepref01–11.md`](https://github.com/sanskrit-lexicon/MWS/tree/master/prefaces),
covers a **different work** — the front matter (title, dedication, preface) of MW's
*English and Sanskrit* dictionary of 1851, from the Motilal Banarsidass reprint scans.
It is out of scope here except where the 1899 Preface itself narrates the 1851 work as
its own prehistory (p. ix note 3, `mwpref06`); we verified its identity directly from
its page files rather than assuming it is an "earlier edition" of the 1899 dictionary.

### 3.2 The measured layers (consumed, not rebuilt)

The measured half of every pairing comes from two kinds of source, kept explicitly
distinct throughout:

1. **Recomputed in this pass** —
   [`papers/a46_preface_method_stats.py`](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/a46_preface_method_stats.py)
   (stdlib-only, deterministic) run 2026-07-09 against csl-orig `mw.txt` @ `392ed6b`:
   record and headword counts, citation-apparatus counts (`<ls>`), accent incidence
   in `key2`, homonym numbers (`<hom>`), root-flagged record counts (`<info verb=>`),
   hierarchy-code distribution (`<e>`). Counting frames are stated per figure in §4.
2. **Committed, dated artifacts of this repository** — the citation-apparatus
   verification and hedge census (measured 2026-06-13,
   [`.ai_state.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/.ai_state.md) log and
   [`lexicographer_dcs/`](https://github.com/sanskrit-lexicon/MWS/tree/master/lexicographer_dcs)),
   the `ib.` antecedent resolver
   ([`relative_refs/`](https://github.com/sanskrit-lexicon/MWS/tree/master/relative_refs)),
   the MW↔Whitney↔DCS root crosswalk
   ([`root_crosswalk/`](https://github.com/sanskrit-lexicon/MWS/tree/master/root_crosswalk)),
   the phrasal-headword graph audit
   ([`phw_graph/`](https://github.com/sanskrit-lexicon/MWS/tree/master/phw_graph)), and
   the transcoder round-trip record
   ([`mwtranscode/readme.txt`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwtranscode/readme.txt)).
   These are cited with their measurement dates; where their counting frame differs
   from this pass's, the difference is stated (§4.3 note).

### 3.3 The pairing method

Each checkable front-matter claim is recorded as a triple: (a) the **stated** claim,
quoted verbatim with page file + printed page; (b) the **measured** value, with its
source per §3.2; (c) a **verdict note** — where the frames are commensurable, how
close statement and measurement are; where they are not (MW counts "words", the
digitization counts records and headword strings), what the frame difference is.
Claims that are checkable but not yet checked are carried as explicit TODO rows in
§9, never silently dropped. Interpretive (non-quantitative) method statements —
e.g. the meaning-separation semantics of comma versus semicolon (p. xv, `mwpref12`)
— are read in §4 as method description and marked not-testable-yet where no
detector exists.

## 4. Results: stated method versus measured practice

### 4.1 The arrangement compromise (§I–II)

**Stated.** Wilson's original project was a dictionary "in which all the words in the
language were to be scientifically arranged under about 2,000 roots" (p. xi,
`mwpref08`); MW reports abandoning "the theoretically perfect ideal of a wholly
root-arranged Dictionary in favour of a more practical performance" (p. xi,
`mwpref08`), settling on "some middle course — some compromise by virtue of which the
two lexicographical methods might be, as it were, interwoven" (p. xiv, `mwpref11`),
implemented as "four mutually correlated lines of Sanskrit words" distinguished
typographically (p. xiv, `mwpref11`). A footnote quantifies the root inventory
tradition: "The number of distinct Dhātus or radical forms given in some collections
is 1,750, but … the number is thereby swelled to 2,490 … even, as some think, to a
list not more than about 120 primitive roots" (p. xiii n. 5, `mwpref10`).

**Measured.** The digitization encodes the compromise structurally: every record
carries a hierarchy code (`<e>`), whose distribution (recomputed: codes `3` =
112,183, `2` = 32,500, `1` = 32,116, `4` = 17,091, plus lettered sub-codes
`2A/2B/3A/3B` for tens of thousands more) is the machine trace of the four-line
plan. Root standing is
marked explicitly: **750** records flagged `verb="genuineroot"` and **1,363** flagged
`verb="root"` (recomputed) — a root layer of 2,113 records against the stated
"about 2,000 roots", with the genuine/artificial split MW himself draws ("all the
roots of the language, both genuine and artificial (the genuine being in *large*
Nāgarī type)", p. xiv, `mwpref11`). Externally, 809 of Whitney's 935 roots (86.5%)
match an MW root anchor (root crosswalk, measured 2026-06-13,
[`root_crosswalk/`](https://github.com/sanskrit-lexicon/MWS/tree/master/root_crosswalk)).
The compound-grouping device ("the third or branch line … for grouping together under
a leading word all the words compounded with that leading word", p. xiv, `mwpref11`)
survives as the phrasal-headword graph: 2,364 `phwchild` edges, 99.3% reciprocal,
with 31 broken links found (measured 2026-06-13,
[`phw_graph/`](https://github.com/sanskrit-lexicon/MWS/tree/master/phw_graph)).

**Note.** The stated "about 2,000" and the measured 2,113 root-flagged records agree
at frame level but are not the same object: MW's figure is the *inventory of Dhātus*
in the grammatical tradition, the digitization's is the count of records the encoders
flagged as root articles. The close agreement is real but partly conventional — both
descend from the same Dhātupāṭha-shaped tradition. ⬜ TODO before 3/5: per-record
audit of what the `verb="root"` (non-genuine) layer actually contains.

### 4.2 The scale claims (Preface, §II)

**Stated.** "It has consisted in adding about 60,000 Sanskṛit words to about
120,000 — the probable amount of the first edition" (p. vii, `mwpref04`); "the number
to be provided for in the new edition could not be reckoned at less than 180,000",
illustrated by the builder "told that he had to provide for the crowding of 1,800
human beings into a room, originally constructed by him to hold only twelve hundred"
(p. xvi, `mwpref13`); the volume grew "in thickness by more than one hundred pages
(and with the Addenda by 147 pages)" (p. xvii, `mwpref14`).

**Measured.** The digitization holds **286,525 records** and **194,084 distinct
headword strings** (`key1`; both recomputed 2026-07-09). Against MW's own counting
frame — "Sanskrit words — simple and compound" — the distinct-headword figure is the
commensurable one: **194,084 measured versus "not … less than 180,000" stated**, i.e.
the lexicographer's rough calculation ("after a somewhat rough calculation … very
little short of 60,000 additional Sanskrit words", p. xvii, `mwpref14`) understated
his finished inventory by about 8% — remarkably accurate for a pre-mechanical count
of a work this size.

**Note.** Records exceed distinct headwords because homonyms, hierarchy members, and
Additions entries share headword strings; neither digitization figure is exactly
MW's "word" (his 180,000 predates the Addenda he describes as 147 pages). The
frame difference is stated, not adjusted away. ⬜ TODO before 3/5: separate the
Additions/supplement records (`<listinfo n=sup/rev>` layer, 936 marked lines per the
2026-06-13 markup audit) to give the like-for-like body-only figure.

### 4.3 The citation policy (§II)

**Stated.** The first edition's "almost entire absence of independent references of
my own was animadverted upon regretfully by even friendly critics" (p. xvii,
`mwpref14`); for the new edition, "after the printing of page 60 I decided, with
Professor Leumann's co-operation, to give no words and no series of meanings without
quoting some authority for their use, or referring to the particular book or portion
of literature in which they occur" (p. xvii, `mwpref14`). Full enumeration being
impossible, "the use of the symbol &c., would answer all the purpose" (p. xvii,
`mwpref14`), with the conventions: "RV. &c. &c. denotes that a word occurs in the
whole literature", "Mn. &c. signifies that the use of a word is restricted to the
later literature", and — the decisive one for evidence-grading — "when a word had
not yet been met with in any published literary work, but only in native lexicons,
it was decided to denote this by the letter L." (p. xviii, `mwpref15`). Words "given
on my authority" are "marked MW." (p. xviii, `mwpref15`); "All the words and meanings
marked W. … rest on his [Wilson's] authority" (p. xxx, `mwpref27`).

**Measured.** The apparatus is real and vast: **320,828** `<ls>` citation instances
(recomputed; frame: every `<ls…>` element including attributed forms — the project's
2026-06-13 verification counted 312,160 under a narrower frame, and measured its
composition: 22.3% of instances are meta/hedge rather than text citations). The
stated conventions all left measurable traces: **40,212** instances of `<ls>L.</ls>`
(12.5% of all citation instances; 39,962 distinct records), **5,711** MW.-authority
instances, **8,286** W.-authority instances, **15,918** RV.-headed instances, and
**10,094** bare `ib.` instances — the space-saving back-reference whose antecedent
the project's resolver recovers mechanically for 74.7% (measured 2026-06-13,
[`relative_refs/`](https://github.com/sanskrit-lexicon/MWS/tree/master/relative_refs)).
The `L.` convention, followed downstream: of 18,930 strictly lexicographer-only
lemmas, 31.0–31.4% are attested in the DCS corpus across two snapshots (measured
2026-06-13, [`lexicographer_dcs/`](https://github.com/sanskrit-lexicon/MWS/tree/master/lexicographer_dcs))
— i.e. about a third of what MW honestly hedged as "not yet met with in any published
literary work" has since been met with, exactly the outcome his wording anticipates.

**Note.** The stated rule is per-*word* ("no words and no series of meanings
without…"), the recomputed figure is per-*instance*. ⬜ TODO before 3/5: per-record
census of authority coverage (which records after MW's page 60 carry no `<ls>` and
no authority marker at all) — the direct test of the stated rule, including its
stated exception zone (pages 1–60).

### 4.4 The accentuation programme (Preface, §II)

**Stated.** The labour included "the accentuation of nearly every Sanskṛit word to
which accents are usually applied" (p. vii, `mwpref04`); "a third improvement in the
present edition … is the accentuation of words occurring in accentuated texts,
although it will be found, I fear, that occasional accidental omissions occur, and
in cross-references the accent has often been designedly dropped. Many accents, too,
which are only known from Pāṇini and the Phiṭ-sūtras have been intentionally omitted"
(p. xviii, `mwpref15`); and the concession "incidence of accent has not been treated
with exact uniformity in every page of this volume" (p. xviii, `mwpref15`).

**Measured.** **48,630** records (17.0% of 286,525) carry accent marks in their
`key2` headword field (recomputed; frame: presence of the digitization's accent
markers in `key2`). The bounded claim — accents for words *occurring in accentuated
texts*, not for the whole lexicon — is consistent with an order-of-magnitude
smaller-than-total accented layer; the preface's own hedges (designed omissions in
cross-references, intentional omission of Pāṇini-only accents, admitted
non-uniformity) are the correct qualitative description of a partial layer.

**Note.** 17.0% is a *floor* frame for the stated claim: `key2` accent presence
per record, not accent presence anywhere in an article, and no measure yet of the
denominator MW intends ("words occurring in accentuated texts"). ⬜ TODO before 3/5:
estimate that denominator (e.g. records whose citations include Vedic sources) so
the stated "nearly every" becomes a testable ratio.

### 4.5 Homonym discipline (§II)

**Stated.** "It will also be seen that words which are different in meaning, but
appear identical in form, are distinguished from each other by the figures 1, 2, 3,
&c." (pp. xiv–xv, `mwpref11–12`), with
the space-saving rider that the figures "have been in some cases dropped" towards
the end of the work (p. xv n. 1, `mwpref12`; p. xx, `mwpref17`).

**Measured.** **11,517** `<hom>` homonym-number elements in the digitization
(recomputed; matching the 2026-06-13 markup audit's figure). The admitted
late-alphabet dropping of figures is a known digitization pain point — homonym
disambiguation is record-splitting work in exactly the zone MW says the print
economized.

### 4.6 The transliteration rationale (§IV) — and the digitization's quiet verdict

**Stated.** §IV defends romanization at length and then defends *specific* choices
against the emerging international standard: *ṛi/ṛī* for ऋ/ॠ rather than *ṛ/ṝ*
("when the dot under the *r* is accidentally dropped or broken off … the result is
worse", p. xxx, `mwpref27`); *sh* retained for the cerebral sibilant against *ṣ*
("This will be clear if we write the important word **Rishi** in the way German
scholars write it, namely **Ṛṣi**, and then omit the dots thus, **Rsi**", p. xxx,
`mwpref27`); the new adoption of *c* for च "in common with many other Sanskṛitists"
(p. xxx, `mwpref27`); *ṅ/ñ* "in accord with the Geneva Transliteration Committee"
(p. xxx, `mwpref27`).

**Measured.** The digitization is itself a transliteration verdict: the machine text
is **SLP1** (one sound, one 7-bit symbol — the "one sound one symbol" principle MW
praises in Nāgarī at p. xxviii, `mwpref25`, carried further than his own print
scheme), with IAST held in a parallel field (`<s1>`, 52,169 instances per the
2026-06-13 markup audit) and MW's *ṛi/sh* print forms surviving nowhere in the
encoding. The project's transcoder round-trips SLP1↔IAST with exactly **3**
documented non-invertible words
([`mwtranscode/readme.txt`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwtranscode/readme.txt))
— a measured residue of precisely the ambiguity-under-degradation argument MW makes
against dotted forms. History sided with the Geneva forms he resisted (*ṛ*, *ṣ*, and
IAST generally), while vindicating his larger §IV claim that romanization with
"diacritical points and marks … may be regarded as a thoroughly scientific instrument"
(p. xxix, `mwpref26`): the entire digitization rests on it.

### 4.7 The collaboration ledger (§V) — a testable division of labour

**Stated.** §V gives a page-exact ledger: Leumann "laboured with me in a scholarly
way as far as p. 474; but his collaboration did not extend beyond 355 pages, because
he took no part in pp. 137–256, which represent the period of Dr. Schönberg's
collaboration" (p. xxxi, `mwpref28`); Cappeller worked "starting from the word Dāda
(p. 474) … the production of 834 finished pages between March, 1891, and July, 1898",
with Dr. Blau assisting "from the beginning of the letter प *p*" (pp. xxxi–xxxii,
`mwpref28–29`); Kielhorn supervised "the grammatical portions … from about the year
1886" (p. xxxii, `mwpref29`). The Preface adds the honesty clause: a collaborative
compilation "must in some degree reflect the idiosyncrasies and infirmities peculiar
to each" (p. viii, `mwpref05`), and names the Schönberg segment as the weakly
supervised one (p. ix n. 1, `mwpref06`).

**Measured.** ⬜ TODO — this is the paper's designed measurement, not yet run. The
digitization carries the print page of every record (`<pc>`), so the four segments
(pp. 1–136 Leumann-A; 137–256 Schönberg; 257–474 Leumann-B; 474–end Cappeller/Blau)
are recoverable per record, and segment-level style statistics (citation density,
hedge share, accent incidence, meaning-separation punctuation) can test whether the
ledger's seams are visible in the finished text — MW's "idiosyncrasies" clause as a
falsifiable hypothesis. The existing per-block detector layer of the microanalysis
series supplies the feature set; only the page-segment cut is new (§9, row 10).

### 4.8 The corpus-scope claim (§III)

**Stated.** "[I]t aims at including every department, or at least such portions of
each department as have been edited up to the present date" (p. xxi, `mwpref18`),
against a literature whose catalogue "would probably amount to a total number not
far short of the 10,000 which the Pandits of India are said to be able to enumerate"
(p. xxi, `mwpref18`), with the conviction "that, notwithstanding the enormous extent
of Sanskṛit literature, nearly all the most important portions of it … worthy of
being edited or translated have been already printed" (p. xxi, `mwpref18`).

**Measured.** The realized scope is the citation apparatus's source inventory:
**44,303 distinct verbatim `<ls>` strings** (recomputed; raw strings, including
locator variants of the same work), reducing to 877 distinct live sigla, of which
537 are linked to authority records (568 authority records exist; measured
2026-06-13, [`mwauthorities/`](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities)).
The distance between "every department" and a countable source list of under a
thousand works is the measurable shape of the claim — comprehensiveness as MW
defines it (everything *edited*), not as the 10,000-work catalogue.

## 5. Discussion

> ⬜ Skeleton — three threads staked out, to be written at 3/5:
> (1) **The preface as evidence-grading manifesto.** The `L.` / `MW.` / `W.` / `&c.`
> conventions (§4.3) are an explicit evidential typology — the 1899 preface states
> the register system whose measured internal structure the project's citation-
> register work develops; stated policy and measured apparatus meet cleanly here.
> (2) **Accuracy of self-description.** Where frames are commensurable, MW's
> quantitative self-statements hold up (180,000 → 194,084 measured, §4.2; bounded
> accentuation claims matching a 17.0% accented layer, §4.4) — against the genre
> expectation that prefaces advertise. His hedges ("rough calculation", "not …
> exact uniformity") are calibrated, not rhetorical.
> (3) **What the digitization decides.** On transliteration the digitization is an
> after-the-fact referee (§4.6): MW's specific letter choices lost, his architectural
> argument won. The general point: a digitized dictionary retroactively adjudicates
> its own front matter.

## 6. Limitations

- The transcription, while faithful and page-provenanced, is this project's own OCR
  pass ([`prefaces/README.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/prefaces/README.md));
  quotations here inherit its accuracy. Spot-verification of quoted passages against
  the scans is a pre-submission step (⬜ TODO).
- Frame gaps are irreducible: MW counts "words", the digitization counts records and
  headword strings (§4.2); the citation rule is per-word, the recomputed apparatus
  figure per-instance (§4.3). Every pairing states its frame rather than forcing
  equivalence.
- The digitization is not the 1899 print: it includes later corrections and
  markup layers. All measured figures are pinned to csl-orig `mw.txt` @ `392ed6b`;
  none have been checked against a physical copy of the 1899 edition.
- Committed-artifact figures date from 2026-06-13 measurements on the then-current
  `mw.txt`; the source has since received corrections (record count 286,560 →
  286,525 in this pass). Differences at this scale do not affect any pairing's
  verdict, but exact reconciliation is a 3/5 hygiene task.
- §4.7 (collaborator segments) is stated as a designed measurement, not a result.

## 7. Conclusion

> ⬜ Skeleton — to be written when §4.7 and the §4.3 per-record census land. The
> arc: the 1899 front matter is a testable methodological document; tested, it is
> substantially accurate in its quantitative self-description and explicit about its
> own non-uniformities; the digitization both confirms the stated method's traces
> (hierarchy codes, homonym numbers, citation conventions) and quietly overrules its
> transliteration particulars. Dictionary prefaces of digitized dictionaries are no
> longer just history — they are checkable method statements.

## 8. Data and reproducibility

- **Primary source:** committed transcription
  [`prefaces/mwpref01–29.md`](https://github.com/sanskrit-lexicon/MWS/tree/master/prefaces)
  + consolidated [`mwpref_all.en.md`](https://github.com/sanskrit-lexicon/MWS/blob/master/prefaces/mwpref_all.en.md),
  with per-page scan URLs to the Cologne csldoc build.
- **Dictionary text:** [csl-orig `v02/mw/mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/main/v02/mw/mw.txt)
  @ `392ed6b` (public repository).
- **Recomputation:** [`papers/a46_preface_method_stats.py`](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/a46_preface_method_stats.py)
  — stdlib-only, deterministic; run 2026-07-09 for every mw.txt-derived figure here.
- **Consumed committed artifacts** (each with its own README and provenance):
  [`lexicographer_dcs/`](https://github.com/sanskrit-lexicon/MWS/tree/master/lexicographer_dcs),
  [`relative_refs/`](https://github.com/sanskrit-lexicon/MWS/tree/master/relative_refs),
  [`root_crosswalk/`](https://github.com/sanskrit-lexicon/MWS/tree/master/root_crosswalk),
  [`phw_graph/`](https://github.com/sanskrit-lexicon/MWS/tree/master/phw_graph),
  [`mwauthorities/`](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities),
  [`mwtranscode/`](https://github.com/sanskrit-lexicon/MWS/tree/master/mwtranscode).

## 9. Claim → artifact inventory

| # | Claim | Figure(s) | Artifact | Status |
|--:|---|---|---|---|
| 1 | Scale: stated 180,000 vs measured inventory | 286,525 records · 194,084 distinct `key1` (§4.2) | [a46_preface_method_stats.py](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/a46_preface_method_stats.py) @ mw.txt `392ed6b` | ✅ recomputed 2026-07-09 |
| 2 | Citation apparatus exists at stated scale | 320,828 `<ls>` instances; frame note vs the 312,160 of 2026-06-13 (§4.3) | same | ✅ recomputed 2026-07-09 |
| 3 | `L.` convention | 40,212 instances = 12.5% (§4.3) | same | ✅ recomputed 2026-07-09 (matches 2026-06-13) |
| 4 | `MW.` / `W.` / `RV.` / `ib.` conventions | 5,711 / 8,286 / 15,918 / 10,094 (§4.3) | same | ✅ recomputed 2026-07-09 |
| 5 | `L.`-hedge corpus attestation today | 31.0–31.4% of 18,930 strict lemmas (§4.3) | [lexicographer_dcs/](https://github.com/sanskrit-lexicon/MWS/tree/master/lexicographer_dcs) | ✅ committed, measured 2026-06-13 |
| 6 | `ib.` economy device resolvable | 74.7% of 10,094 (§4.3) | [relative_refs/](https://github.com/sanskrit-lexicon/MWS/tree/master/relative_refs) | ✅ committed, measured 2026-06-13 |
| 7 | Accentuation programme | 48,630 records = 17.0% accented `key2` (§4.4) | a46_preface_method_stats.py | ✅ recomputed 2026-07-09; ⬜ denominator TODO |
| 8 | Homonym figures | 11,517 `<hom>` (§4.5) | same | ✅ recomputed 2026-07-09 |
| 9 | Root layer: stated ~2,000 | 750 genuineroot + 1,363 root = 2,113 (§4.1); 809/935 Whitney (86.5%) | same + [root_crosswalk/](https://github.com/sanskrit-lexicon/MWS/tree/master/root_crosswalk) | ✅ recomputed / committed 2026-06-13; ⬜ non-genuine-layer audit TODO |
| 10 | §V collaborator segments visible in text | segment cut at pp. 137/257/474 via `<pc>` (§4.7) | — | ⬜ TODO — the designed measurement |
| 11 | Per-record authority coverage (the stated post-p.-60 rule) | — (§4.3 note) | — | ⬜ TODO before 3/5 |
| 12 | Corpus scope realized | 44,303 verbatim `<ls>` strings · 877 live sigla · 568 authority records (§4.8) | a46_preface_method_stats.py + [mwauthorities/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) | ✅ recomputed / committed 2026-06-13 |
| 13 | Transliteration round-trip residue | 3 non-invertible words (§4.6) | [mwtranscode/readme.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwtranscode/readme.txt) | ✅ committed |
| 14 | Quotation fidelity to the 1899 print | — (§6) | scans linked per page in [prefaces/](https://github.com/sanskrit-lexicon/MWS/tree/master/prefaces) | ⬜ TODO pre-submission spot-check |

## 10. Scope versus companion papers (anti-salami)

- **A16/A17 (MWS block-economy microanalysis series)** own the block-level markup
  economy of the digitized MW and its detector/gold-standard apparatus. A46 consumes
  their measured layer as the "measured" half of pairings and adds none of its own
  block detectors; the §4.7 segment study would *reuse* their features, cut by
  `<pc>` page, and any such result cross-cites the series.
- **A40 (CDSL headword census)** owns cross-dictionary headword inventory
  methodology. A46 cites single-dictionary headword counts only as the measured
  frame for MW's own scale claim (§4.2) and makes no cross-dictionary comparison.
- **A35 (etymology-tradition comparison)** owns the comparative etymology question.
  A46 reads MW's *stated* etymological-arrangement rationale (§4.1) and does not
  evaluate etymological correctness.
- **A45 (botanical crosswalk)** owns the botanical layer; A46 mentions plants only
  where the preface itself does (capitalization policy, p. xvi, `mwpref13` — not
  treated here).
- **The [`prefaces/`](https://github.com/sanskrit-lexicon/MWS/tree/master/prefaces)
  transcription itself** is a project data asset, not this paper's contribution;
  A46 is its first scholarly *consumer*.
- A46 leads with exactly what nothing else owns: **the 1899 front matter read as a
  testable methodological document — stated method paired against the measured
  digitized dictionary.**

## 11. References

> **⬜ STUB (readiness 2/5)** — primary sources listed; scholarship to be added in
> the verified literature pass (§2), never faked.

- Monier-Williams, M. 1899. *A Sanskrit-English Dictionary. Etymologically and
  philologically arranged with special reference to cognate Indo-European
  languages.* New edition. Oxford: Clarendon Press. (Front matter pp. i–xxxii,
  cited per page as `mwprefNN` from the committed transcription.)
- Monier-Williams, M. 1851. *A Dictionary, English and Sanskṛit.* London: East
  India Company. (As narrated in the 1899 Preface; transcription in progress as
  `mwepref*`, §3.1.)
- Böhtlingk, O., and R. Roth. 1855–1875. *Sanskrit-Wörterbuch.* 7 vols.
  St. Petersburg: Kaiserliche Akademie der Wissenschaften. (As "the great
  seven-volumed Thesaurus" of the Preface.)
- Whitney, W. D. 1885. *The Roots, Verb-forms and Primary Derivatives of the
  Sanskrit Language.* Leipzig: Breitkopf & Härtel. (Named at p. xv n. 2 and
  p. xxxii; the crosswalk partner of §4.1.)
- Cologne Digital Sanskrit Dictionaries: [csl-orig](https://github.com/sanskrit-lexicon/csl-orig)
  (dictionary text), MW digitization.
- ⬜ A16/A40 self-citations to be finalized once their venues/DOIs freeze.

_Dr. Mārcis Gasūns_
