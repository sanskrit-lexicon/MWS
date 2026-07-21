---
paper_id: A18
title: "One Slot, Many Warrants: The Evidentiary Stratification of the Citation Apparatus in Monier-Williams' Sanskrit-English Dictionary"
status: full draft — outline 2026-06-13, drafted 2026-07-16 (H1076)
readiness: 3/5 (pending author sign-off)
venue: "Dictionaries: Journal of the Dictionary Society of North America (2027)"
author: "**Mārcis Gasūns**, independent scholar ([ORCID 0000-0003-4513-884X](https://orcid.org/0000-0003-4513-884X)), gasyoun@ya.ru"
data_source: "MWS/papers/p3_citation_registers/register_census/ (register_census.py over csl-orig v02/mw/mw.txt; census_stats.json + CENSUS.md). Corpus figures from MWS/lexicographer_dcs/, MWS/relative_refs/, MWS/botanical_glossary/, MWS/papers/p3_citation_registers/register_b/. Register terminology from csl-atlas docs/CITATION_REGISTERS.md (A08)."
---

# One Slot, Many Warrants: The Evidentiary Stratification of the Citation Apparatus in Monier-Williams' *Sanskrit-English Dictionary*

_Created: 16-07-2026 · Last updated: 16-07-2026_

> **Draft status (2026-07-16, readiness 3/5 pending author sign-off).** Every count in §3 is
> computed by [`register_census/register_census.py`](register_census/register_census.py) over
> `csl-orig` `v02/mw/mw.txt` and persisted to
> [`register_census/CENSUS.md`](register_census/CENSUS.md) +
> [`census_stats.json`](register_census/census_stats.json); the run is deterministic
> (re-running reproduces every artifact byte-identically). Corpus figures in §5 are carried
> from the committed modules cited there and are **not** re-derived here.
> **Open before submission (author/@DO):** (1) confirm byline + venue and do the final read;
> (2) pin the `mw.txt` source commit and mint the dataset DOI in §"Data and reproducibility";
> (3) decide whether §6.2's correction to the A08 MW row travels as a footnote or as a
> reported issue against `csl-atlas` (a fix there would change a *published* number);
> (4) rule on the §5.3 sense-level gate — the paper currently states the lemma-level figure
> with its ceiling, which is honest but leaves the sharper claim unclaimed.
>
> **Scope discipline.** This paper argues the *evidentiary gradient*. The nine-dictionary
> register comparison belongs to A08 (csl-atlas) and is **cited, not re-argued**; the botanical
> resource belongs to A45 and is **cited, not led with**.

## Abstract

A historical dictionary's citation apparatus looks, in digital form, like a single uniform
field: one tag, one slot, one kind of thing. We show that it is not. Recent work distinguishes
two *citation registers* across the Cologne Digital Sanskrit Dictionaries — the European
critical-apparatus form, a tagged source abbreviation, versus the indigenous form, an in-prose
quotative `iti` — and classifies dictionaries by which they use. That distinction is about
citation **form**. We test it against the largest Sanskrit-English dictionary, Monier-Williams
(1899), and find that form is only one axis. Within MW's single formal register, the same
`<ls>` slot carries at least five distinct evidentiary warrants, which we census exhaustively:
a **locator-bearing attestation** the reader can walk to (60,820 citations, 18.96%); a **bare
abbreviation** naming a work but no passage (190,403, 59.35%); a **lexicographer's hedge**,
MW's `L.`, marking a sense that rests on the indigenous synonym lexicons with no textual
witness (40,213, 12.53%); an **authority pointer** (`W.`, `MW.`, `Cat.`; 19,298, 6.02%); and an
**anaphoric relative** (`ib.`; 10,094, 3.15%). The hedge is the interesting one: it is
Register-B *content* — kośa material — compressed into a Register-A *slot* with the source name
discarded. It is therefore not a claim that no text exists, but a 19th-century evidence-gap
marker; corpus-testing closes roughly a third of that gap (31% of strictly hedged lemmas occur
in the Digital Corpus of Sanskrit). We argue that a citation apparatus should be read as a
**form × warrant matrix** rather than a list, and that this matters practically: MW's genuinely
locatable apparatus is 18.96%, not the ~37.5% its own project documentation reported, and any
tool that treats `<ls>` as a homogeneous "has a citation" feature is measuring a slot, not
evidence. We correct two propagated measurement errors along the way, both of which flattered
the apparatus, and both of which were artefacts of reading markup shape as though it were
scholarly substance.

## 1. Introduction

Ask a digital dictionary how well-evidenced it is and it will answer with a count. Monier-Williams'
*A Sanskrit-English Dictionary* (1899), in its Cologne digitisation, contains something over
three hundred thousand source citations across 286,525 records — a little more than one per
entry. On that number alone MW looks like a densely evidenced work, and by the standards of
19th-century bilingual lexicography it is.

The number is also nearly meaningless, and the reason is the subject of this paper. A citation
is a *warrant*: it is the lexicographer's answer to the question "how do you know?". Counting
citations assumes that every citation answers that question in the same way. In MW it demonstrably
does not. Some citations name a work and a verse and can, in principle, be walked to a page.
Some name a work and nothing else. Some name no work at all — they are MW's own admission that a
sense comes from the indigenous synonym-lexicon tradition, with no text behind it that he knew
of. All three occupy the same tag, in the same position, and are indistinguishable to any
counter that asks only whether a citation is present.

Recent corpus-wide work on the Cologne collection (§2) established that the collection contains
two *citation registers*, distinguished by **form**: a tagged source abbreviation inherited from
European critical-apparatus practice, and an in-prose quotative construction (`… iti <source>`)
inherited from the Sanskrit kośa tradition. That result is about how a citation is *written*, and
it is sharp: 28 of 44 dictionaries carry no tagged citations at all, and a counter that knows only
the tagged form ranks the densest indigenous citers at zero. MW sits unambiguously on the
European side of it.

This paper asks what is inside that single formal register once you look. Our claim is that
**register is one axis and warrant is another**, and that the second is invisible to the first.
We contribute:

1. **An exhaustive evidentiary census** of MW's apparatus (§3): every one of its 320,828 tagged
   citations classified into five mutually exclusive warrant strata, computed by a committed,
   deterministic script.
2. **A reading of the lexicographer's hedge** (§4) as Register-B content in a Register-A slot —
   the point where the two registers, ordinarily treated as disjoint dictionary populations, meet
   *inside a single entry*.
3. **A corpus test of the gradient** (§5), showing the hedge is a recoverable evidence gap rather
   than an assertion of absence, with an explicit and load-bearing homograph control.
4. **Two corrections** (§6) to published measurements of this same apparatus, both of which
   overstated it, and a general lesson about markup shape masquerading as scholarly fact.

The object we end up with is not a citation count but a matrix, and §7 argues that this is the
right shape for the question — for MW, for the Cologne collection, and for historical dictionaries
whose apparatus is being made machine-readable at all.

## 2. Background: the two registers, and what they do not tell us

We take the register distinction from the atlas measurement of the full Cologne collection
([`CITATION_REGISTERS.md`](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/CITATION_REGISTERS.md),
with its committed artifact
[`data/obs/citation_registers.json`](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/data/obs/citation_registers.json)),
and we adopt its terminology unchanged:

- **Register A** — the `<ls>`-tagged citation: a source abbreviation, optionally with a locator,
  marked up as a discrete apparatus element. The European critical-apparatus tradition.
- **Register B** — the in-prose quotative: a quoted authority followed by `iti` (`ityamaraḥ`,
  `iti viśvamedinyau`), with no apparatus markup at all. The indigenous kośa tradition.

The finding is that these are two disjoint citation *systems*, not two styles of one system. The
Sanskrit-Sanskrit kośas (SKD, VCP, KRM) carry **zero** tagged citations while citing constantly —
KRM at 6.00 quotatives per entry, the densest in the collection — so an `<ls>`-based density
counter mis-ranks the densest citers in the corpus as citation-free. Corpus-wide, Register A runs
1,245,644 citations, of which 59.3% carry a locator; the remaining ~41% name a source and no
passage.

Two things follow for the present paper, and it is worth separating them.

The first is that MW is a Register-A dictionary, and we confirm this rather than assume it (§3.1):
its indigenous-register footprint is 250 word-boundary `iti` hits across the whole dictionary,
0.001 per entry. The atlas's own count is 172; the gap between the two is 45% and we do not paper
over it — both are noise-level upper bounds on a proxy (§8), and at this order of magnitude the
divergence is uninteresting while the conclusion is not: MW does not cite in the indigenous
register. Whatever we find inside MW's apparatus, we cannot explain it as register
mixture at the level of *form*.

The second is what the register distinction, by construction, cannot see. It classifies citations
by their markup shape. It is therefore silent on the question a lexicographer actually cares
about: what does this citation *warrant*? A tagged `<ls>MBh. iii, 12</ls>` and a tagged
`<ls>L.</ls>` are both Register A, both one citation, both counted once. The first says "this
sense occurs in the Mahābhārata at book 3, verse 12". The second says "this sense is in the
lexicons and I have no text for it". Treating those as the same datum is not a rounding error;
it is a category mistake, and at 40,213 occurrences it is a category mistake with a large
denominator.

The atlas work is not at fault here — it measured what it set out to measure, per register, and
explicitly warns against reporting a single `<ls>`-only citation density. Our point is the
complementary one: *within* a register, density is still not evidence.

## 3. The census

### 3.1 Method

We parse the canonical Cologne source `csl-orig` `v02/mw/mw.txt` directly — 286,525
`<L>`…`<LEND>` records — and classify every tagged citation in it. The script
([`register_census/register_census.py`](register_census/register_census.py)) is committed, its
outputs are persisted next to it, and a re-run reproduces every artifact byte-identically.

Two features of MW's markup govern the method, and getting either wrong changes the answer
materially (§6.2). First, MW writes a citation in **two different shapes**:

```
<ls>Pāṇ. vi, 2, 161</ls>          PLAIN shape — siglum and locator inside the tag content
<ls n="RV.">vii, 96, 3</ls>       ATTRIBUTED shape — siglum in @n, locator in the content
<ls n="RV. viii, 96,">15</ls>     attributed, with the locator split across attribute and content
```

The attributed shape accounts for 8,668 citations (2.7% of the apparatus). A regex matching a
literal `<ls>` never sees them. We therefore read the citation's full text as `@n` + content and
split siglum from locator *positionally*, on the leading run of non-locator tokens.

Second, MW's locators are **arabic or roman**: `RV. 10, 12` and `ŚBr. xiv` are both locators, and
4,866 plain-shape citations carry a roman-only one. A digit-based locator test scores all of them as
sourceless. The roman test must be case-sensitive — MW's roman locators are lowercase, and folding
case makes the hedge `L.` read as roman 50 and capitalised sigla such as `Vi.` read as roman 6.
We found this the hard way: an early case-folding run silently reclassified some 46,000 bare
citations as attested and zeroed the hedge stratum entirely.

Each citation is assigned exactly one stratum, decided on the siglum first and the locator second:

| Stratum | Rule | Reading |
|---|---|---|
| `hedge` | siglum is `L.` | "Lexicographers" — kośa authority, no text |
| `authority` | siglum is `W.`, `MW.`, `Cat.` | a scholar, MW himself, or a catalogue |
| `relative` | siglum is `ib.` or `id.` | anaphoric — the source is the previous citation |
| `attested` | a named work **with** a locator | a walkable passage |
| `bare` | a named work with **no** locator | a work named, no passage |

(`id.` is admitted by the rule but never occurs inside a citation tag in MW: its 4,401 occurrences
are all `<ab>id.</ab>`, the *sense*-level idem marker, which is a separate object with its own
display-policy question. So the `relative` stratum is `ib.` in practice.)

### 3.2 Results

| Stratum | Citations | Share of apparatus | Entries carrying ≥1 |
|---|--:|--:|--:|
| attested (named work + locator) | 60,820 | **18.96%** | 43,680 |
| bare (named work, no locator) | 190,403 | **59.35%** | 130,584 |
| hedge (`L.`) | 40,213 | **12.53%** | 39,963 |
| authority (`W.`/`MW.`/`Cat.`) | 19,298 | **6.02%** | 19,256 |
| relative (`ib.`) | 10,094 | **3.15%** | 9,386 |
| **Total** | **320,828** | 100% | 226,712 |

The apparatus is 1.12 citations per entry, and 226,712 of 286,525 records (79.1%) carry at least
one. Those are the numbers that make MW look densely evidenced, and they are true.

The distribution underneath them is the finding. **Fewer than one citation in five carries a
locator.** The single largest stratum, at very nearly three in five, is a work named without a
passage — `<ls>MBh.</ls>`, standing alone, asserting that the Mahābhārata has this word somewhere
in its hundred thousand verses. And better than one citation in five (21.70%) does not name a
primary text at all: it is a hedge, an authority pointer, or an anaphor.

Two structural details matter later. The hedge is **concentrated, not diffuse**: 39,963 records
carry one, and 39,415 of those carry *no attested citation whatsoever*. Tighten the requirement to
records carrying a hedge and no citation of a named work at all — neither attested nor bare — and
38,538 remain. For that population the hedge is not a qualifier sprinkled onto otherwise-evidenced
entries; it is the entire warrant. Only 548 records (0.24% of citing records) place a hedged sense
beside an attested one. And the strata are per citation *occurrence*, not per sense: an entry
mixing warrants contributes to both, which is precisely why the corpus test in §5 needs a strict
subset rather than a naive join.

## 4. The hedge is Register B in a Register-A slot

`<ls>L.</ls>` expands to "Lexicographers", and MW's own front matter is explicit about what it
means: the sense is given on the authority of the indigenous lexical tradition — the kośas and
nighaṇṭus, the versified synonym-lists — with no textual witness known to him. It is, in other
words, a citation whose *source class* is exactly the source class of Register B.

This is the paper's central observation, and it is a structural one rather than a numerical one.
The register distinction (§2) is a claim about dictionary populations: MW cites in Register A,
SKD/VCP/KRM cite in Register B, and the two do not mix. That is true *of citation form*. But at
40,213 occurrences — one citation in eight — MW is citing kośa material with the source name
stripped out. `iti rājanighaṇṭuḥ` and `<ls>L.</ls>` point into the same tradition. The difference
is that the first names which lexicon and the second does not.

So the two registers are not, at the level of content, disjoint at all. They meet inside MW's
entries, and the meeting is invisible to a form-based classifier because MW performs the
compression: he takes an indigenous citation, discards its source, and writes the residue into a
European apparatus slot as a bare flag. The `L.` hedge is *Register-B content in a Register-A
slot with the bibliography deleted*.

Read this way, two things that look like curiosities become consequences.

The first is that the hedge is **lossy in a specific, characterisable direction**. Register B's
citation practice names its authority: SKD's quotatives target a named kośa or nighaṇṭu in at
least 40.5% of cases ([`register_b/`](register_b/)). MW's hedge names none. The information that
`<ls>L.</ls>` destroys — *which* lexicon — is exactly the information that would make it
resolvable, and it is information the indigenous register routinely preserves. The hedge is not a
weaker citation than a kośa quotative; it is a kośa quotative with its source field emptied.

The second is a reversal of the hedge's apparent meaning. Because Register B cites lexicons
*constitutively* — that is its normal, unmarked practice, not a confession — what MW marks as
exceptional is, one tradition over, simply how citation works. The `L.` hedge is the trace of a
European apparatus registering an indigenous norm as a deficiency. That is a statement about the
meeting of two lexicographic cultures in one dictionary, and it is legible only if you refuse to
read `L.` as just another citation.

## 5. The corpus test: is the hedge a gap or a wall?

If `<ls>L.</ls>` means "no text known **to MW**", it is a claim about the state of textual
knowledge in 1899, not about the language. It is therefore testable against a corpus MW did not
have.

### 5.1 The result

Joining MW's strictly hedged lemmas against the Digital Corpus of Sanskrit
([`lexicographer_dcs/`](../../lexicographer_dcs/)): of 18,930 lemmas whose entire attestation is
`L.`, **31.0%** occur in DCS-2021 and **31.4%** in the fuller DCS-2026 token corpus. The stability
across snapshots is worth exactly what it is worth and no more — these are two versions of one
corpus project, one annotation tradition, so the agreement controls for *version*, not for DCS's
conventions.

So the hedge is **not** a statement of non-existence. Roughly a third of it dissolves on contact
with a modern corpus. What MW recorded as "the lexicons say so and I cannot show you a text" was,
in a third of cases, a text he had not read or that had not been edited. The hedge is a
19th-century **evidence-gap marker**, and the gap is partly an artefact of its century.

The other ~69% is the more interesting residue: vocabulary the lexicographic tradition carries
that the surviving, digitised, annotated text corpus does not. Alongside it sit 259 verbal roots
that MW and Whitney both record and DCS attests zero times ([`root_crosswalk/`](../../root_crosswalk/)).
For that population the evidence boundary is real, and — for this corpus — permanent.

### 5.2 The homograph control, which is load-bearing

Any lemma-level corpus join of this kind is exposed to homograph collision: a common word carrying
a rare hedged sense (*kṛṣṇa* the deity beside *kṛṣṇa* the plant) is attested in the corpus for the
*wrong sense*, and a naive join counts that as recovery. This inflates the recoverability figure,
and it inflates it in the direction the researcher is hoping for, which is the dangerous
direction.

The 31% is the **controlled** figure: it restricts to the 18,930 lemmas whose *every* sense is
hedged, so that any corpus occurrence is at least an occurrence of a hedged lemma. The
restriction is not fussiness. A further **10,264 lemmas are partially hedged** — they carry both
`L.` and real citations ([`lexicographer_dcs/`](../../lexicographer_dcs/)) — and they are excluded
precisely because there the corpus cannot distinguish which sense it is attesting: an
uncontrolled join would credit the hedged sense with the evidence belonging to its attested
neighbour. The strict set is narrower still than the obvious one: a coarse "every citation is
`L.`" rule admits 20,146 lemmas, and 1,216 of those are dropped for carrying an uncited gloss or
stub, leaving the 18,930 genuinely known only from the kośas. Each exclusion costs population and
buys the only figure that means what it says. A naive join reports a higher number, and the higher
number is wrong.

The same control, applied within a single semantic field, reproduces the pattern: of MW's 7,063
botanical headwords, 72% carry their plant sense as hedged, and restricting to botanical-only
headwords leaves 1,567 corpus-confirmed plant lemmas (the resource itself is A45's contribution
and we cite rather than re-argue it).

### 5.3 What this is not

It is **lemma-level** evidence. It shows that a hedged lemma occurs in the corpus; it does not show
that the corpus attests *the hedged sense*. That is a strictly stronger claim, it requires
sense-tagged data, and we do not make it here. A deterministic 80-sense verification sample is
built and packaged for hand-adjudication ([`sense_verify/`](sense_verify/)); the sense-level figure
awaits it, and will arrive with a method ceiling of its own. We state the lemma-level figure with
its ceiling attached rather than the sharper claim we cannot yet support.

## 6. Two corrections, and what they have in common

Both errors below were found while building §3, both had propagated into project documentation,
and both made MW's apparatus look better evidenced than it is. Neither was a scholarly mistake.
Both were markup shape read as scholarly substance.

### 6.1 MW's linkable ceiling is ~19%, not ~37.5%

The project's own synthesis memo and roadmap state MW's apparatus ceiling as "22.3% meta + 40.2%
bare", implying that ~37.5% of MW's citations are text-linkable. The 22.3% is a real MW
measurement — the meta strata, 69,603 citations by a literal tag match, which our census
reproduces to within the two documented anomalies of §8 (69,605). The 40.2% is not a measurement
of MW at all: it is the **corpus-wide** bare-abbreviation share, imported from the atlas table —
an aggregate dominated by PWG, which contributes 568,730 citations at 4.61 per entry against MW's
1.09 (both on the atlas's own rule, the only way the comparison is legitimate). It is additionally
a **stale** figure: the current atlas covers 44 dictionaries and reports 40.7%/59.3%, while the
exact pair 40.2%/59.8% survives only in the superseded 43-dictionary pass (1,234,530 citations).
The number in the memo is a corpus-wide aggregate from a table that no longer exists.

The two components were never additively coherent — they are computed over different populations
and different denominators, so "22.3% + 40.2%" was not a valid subtraction from 100% even had both
been MW's. MW's own locator-bearing share is **18.96%** by our rule, and 15.15% by the atlas's
stricter one. The ceiling is roughly half what the documentation claimed.

This matters beyond bookkeeping, because the ceiling is what a scan-linking programme is budgeted
against. The realistic prize for linking MW's apparatus to page images is about one citation in
five, not two in five, and the difference is decided before any work starts — by *which citations
have a locator to link with at all*.

### 6.2 The atlas's MW row undercounts its apparatus by 28.6%

The atlas artifact reports MW as `ls: 312160`, `lsWithLocator: 47289` — a 15.15% locator share.
We reproduce both figures **exactly**, which localises the divergence precisely rather than
leaving it a disagreement of parsers. Its extractor is literal:

```python
_LS = re.compile(r"<ls>(.*?)</ls>", re.DOTALL)   # scripts/forensic/parse_cslorig.py:41
DIGIT_RE = re.compile(r"\d")                     # scripts/obs/citation_register_gaps.py:49
```

Two blind spots follow, and they compound:

| | atlas | this census | cause |
|---|--:|--:|---|
| Register-A citations | 312,160 | **320,828** | the literal `<ls>` never matches the 8,668 attributed citations |
| Locator-bearing | 47,289 | **60,820** | the attributed citations are where the locator *is* — 8,666 of the 8,668 bear one, 7,077 of them arabic and so countable had the tag matched at all — plus 4,866 plain-shape citations whose only locator is roman, which `\d` cannot see |
| Locator share | 15.15% | **18.96%** | |

MW's linkable apparatus is thus **28.6% larger** than the published row records. The direction of
the atlas's finding is untouched and its corpus-wide conclusion stands — MW remains a
locator-poor, Register-A dictionary — but the MW row wants regenerating. This is the same defect
class the atlas has already corrected once in this very dataset: its original `iti` rule was
space-or-quote-delimited and undercounted KRM roughly threefold, because KRM wraps its Sanskrit in
markup and its quotatives sit flush against a tag. A word-boundary rule fixed it. Here the mirror
image: a citation rule that assumes citations are shaped one way, in a dictionary that writes them
two ways.

A caution against reading the two documents as contradictory. The atlas's "bare abbreviation"
means *no arabic digit* — a single bucket holding everything that is not locator-bearing, which on
MW is 84.85% and silently contains the hedge, the anaphors, the authority pointers and every roman
locator. Our `bare` stratum (59.35%) means something narrower: a named work, no locator, and not a
meta marker. The numbers answer different questions. Decomposing that one bucket is the whole
point of the census.

### 6.3 The common lesson

Both errors have the same shape. A number was computed by a rule that encoded an assumption about
*how the markup is written* — one tag shape, arabic locators, one bare bucket — and the number was
then read as a fact about *what the lexicographer did*. The assumption was invisible because it
lived in a regex, and the resulting figure was plausible, quotable, and propagated: the 40.2%
travelled from a superseded corpus-wide table into a memo, a roadmap, and a paper outline, and at
no point did it stop looking like a fact about Monier-Williams.

The defence is not better regexes. It is that any number characterising a historical apparatus
should have to state *which markup shapes it counted* and *what it treated as a locator*, in the
same breath as the number. For MW both decisions are load-bearing and neither is visible in the
result. Together they hide 13,532 locator-bearing citations, and they split cleanly: 8,666 are lost
to counting one tag shape instead of two, and 4,866 to reading only arabic digits as locators.
(Against that, the older rule counts one citation as located that we class as authority — the
`<ls>W. 1</ls>` of §8 — so the net understatement of MW's linkable core is 13,531, or **28.6%**.) A third decision — whether the roman test is
case-sensitive — silently reclassified some 46,000 citations and erased the hedge stratum outright
in an early run of our own script, and it was caught only because the hedge count was known
independently. The census's rules are stated in §3.1 for exactly this reason, and its
limitations (§8) in the same spirit.

## 7. Consequence: the apparatus is a matrix, not a list

Put the two axes together. The register distinction sorts *dictionaries* by citation form.
The warrant strata sort *citations* by what they evidence. Neither reduces to the other, and the
cells of the resulting matrix are the objects a reader, a lexicographer, and a parser each
actually need:

| | Register A (tagged apparatus) | Register B (`iti` quotative) |
|---|---|---|
| **attested** — walkable passage | MW 18.96% — the linkable apparatus | quotative + named text |
| **bare** — work named, no passage | MW 59.35% — the bulk of MW | — |
| **hedge** — lexicon authority, no text | MW 12.53% — kośa content, source deleted | the *constitutive* norm of the kośas |
| **relative / authority** — no primary text | MW 9.16% — partly recoverable | — |

Three consequences follow.

**For the reader of MW.** "Cited" is not a property an MW sense has or lacks. Four fifths of the
apparatus does not point at a passage, and an eighth of it points at no text at all. A sense
marked `L.` is a genuinely different epistemic object from a sense marked `MBh. iii, 12`, and the
1899 dictionary says so — it is the digital reduction to a uniform tag that hides it.

**For the digital apparatus.** Any tool that treats `<ls>` as a boolean "has a citation" feature
is measuring a slot, not evidence. This is not hypothetical: it is exactly how the two errors in
§6 arose, and it is how a hedge — MW's explicit statement that he has *no* text — gets counted as
a citation *of* a text. The strata are cheap to compute, deterministic, and derivable from the
open source; there is no reason for a downstream consumer to keep flattening them.

**For the linkable core.** The apparatus is more connected than the raw strata suggest, in one
specific and bounded way. The 10,094 anaphoric `ib.` citations are not sourceless: a document-order
antecedent walk resolves **74.7%** (7,538) to a real text source, against 25.3% whose antecedent is
itself a meta marker and so recovers nothing. That 74.7% is a mechanical upper bound. On the
orthogonal axis of confidence, 57.1% (5,762) of the resolutions are same-cluster — the antecedent
sits inside the same headword — which is the defensible core; the remaining 42.9% cross a headword
boundary and want a spot-check before use ([`relative_refs/`](../../relative_refs/)). The two splits
are independent and should not be collapsed into a single "high-confidence real-source" rate: that
figure has not been measured. All of it is **resolvable, not hand-verified**, and we report it as
such. But they establish the direction: the meta share overstates how much of MW's
apparatus is genuinely detached from a source, just as the bare share understates how much of it
names a real work.

The honest summary of MW's apparatus is therefore neither "312,160 citations" nor "18.96% usable".
It is: a large apparatus, overwhelmingly naming works rather than passages, resting on the
indigenous lexical tradition for an eighth of its warrants, with a linkable core of about one
citation in five and a partly recoverable anaphoric layer on top. That sentence is longer than a
number, and it is the shortest true thing we can say.

## 8. Limitations

- **Locator presence is not linkability.** `attested` means a locator is present, an upper bound.
  It does not mean the locator is correct, that the cited edition is identifiable, or that a scan
  exists. Identifying MW's cited editions is a separate and genuinely hard problem: MW's front
  matter is an abbreviation-expansion key with no edition metadata, so for major sources the
  edition cannot be established from the dictionary at all.
- **Sigla are unnormalised surface forms.** `MBh.`/`MBH.` and `R.`/`Rām.` are not merged here.
  Siglum normalisation and abbreviation-family merging are the atlas's owned layer, with a curated
  alias table and a human review queue; we deliberately do not duplicate it, and the per-stratum
  distinct-siglum counts (510 attested, 824 bare) are therefore upper bounds.
- **The strata are per citation occurrence, not per sense.** An entry mixing warrants contributes
  to more than one stratum. §5's corpus figures use a strict lemma subset for this reason.
- **The `iti` count is a proxy.** It is the atlas's word-boundary indicator, which fires on quoted
  running text and on grammatical `iti`; MW's 250 is an upper bound on an already noise-level
  footprint, sufficient to establish that MW does not cite in Register B and nothing more.
- **The classification is siglum-first.** A meta siglum carrying a locator is classed by its
  siglum. All of MW contains exactly two such citations (`<ls>L. i</ls>`, `<ls>W. 1</ls>`), so the
  strata run +1 hedge and +1 authority against a literal tag match; we record this so it is not
  later mistaken for drift.
- **The source moves.** `mw.txt` is under active correction: this run sees 286,525 records against
  the 286,560 measured on 2026-06-13, a loss of 35 records to upstream corrections in about a
  month. Any figure here is a figure about a dated source, which is why the run is scripted and
  the artifact committed.

## 9. Data and reproducibility

All inputs are open. The dictionary source is `csl-orig` `v02/mw/mw.txt`; the census script,
its CSV outputs, its JSON statistics and its generated summary are committed at
[`papers/p3_citation_registers/register_census/`](register_census/). The run is deterministic —
re-running reproduces every artifact byte-identically, which is the property that makes the §6.2
divergence a *finding* rather than an anecdote.

```sh
cd papers/p3_citation_registers/register_census
python register_census.py     # -> register_census.csv, register_census_sigla.csv,
                              #    entry_level.csv, census_stats.json, CENSUS.md
```

Corpus figures are carried, not re-derived, from the committed modules cited at each point:
[`lexicographer_dcs/`](../../lexicographer_dcs/) (hedge → DCS),
[`relative_refs/`](../../relative_refs/) (`ib.` resolution),
[`root_crosswalk/`](../../root_crosswalk/) (corpus-absent roots),
[`register_b/`](register_b/) (the indigenous register's own corpus test), and
[`botanical_glossary/`](../../botanical_glossary/) (the botanical sub-register, A45's resource).

**@DO before submission:** pin the `mw.txt` source commit and mint the dataset DOI.

_Dr. Mārcis Gasūns_
