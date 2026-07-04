# P3 contribution — the corpus test: evidentiary status within the European (`<ls>`) register

*A synthesis of the 2026-06-13 MW corpus findings as one evidence block for paper
P3, "Two citation registers: European source apparatus and indigenous* iti
*quotation in nine Sanskrit dictionaries" (venue:* Dictionaries*, Q1 2027).*

> **Scope.** P3's spine is the Register A / Register B distinction across nine
> dictionaries — the atlas work ([CITATION_REGISTERS.md](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/CITATION_REGISTERS.md),
> `citation-apparatus.json`, the siglum alias table). This memo does **not**
> reproduce that; it contributes the **MW slice of one orthogonal axis** — what
> happens to the European `<ls>` register when it is tested against a modern
> corpus (DCS). It is lemma-level, MW-only, and says nothing about the *iti*
> register (that is the atlas / P4 side).

## The argument

The two-register thesis classifies citations by **form**: a tagged source
abbreviation (`<ls>MBh.</ls>`, Register A) versus an in-prose quotative (`… iti`,
Register B). Testing Register A against the DCS corpus exposes a second,
orthogonal axis the form-distinction cannot see: **evidentiary status**. MW's
`<ls>` register is not evidentiarily uniform. It stratifies into a gradient:

1. **Text-attested citations** — a named work with (often) a locator. The
   apparatus at face value.
2. **A lexicographer-only hedge** — `<ls>L.</ls>` (40,212 tags, ~13% of all
   citations), MW's own marker that a sense rests on the indigenous *kośa*
   tradition with no textual witness *known to MW*. The corpus test shows this
   layer is **partly recoverable**: of 18,930 lemmas whose entire attestation is
   `L.`, **~31% occur in DCS** (31.0% on the 2021 snapshot, 31.4% on the full
   2026 token corpus — stable across two DCS snapshots, though both are versions
   of one corpus project, so this controls for version not for DCS's conventions). The hedge is
   therefore **not** a statement of non-existence; it is a *19th-century
   evidence-gap marker*, and a modern corpus closes roughly a third of the gap.
3. **A hard kośa / grammarian residue** — the other **~69%** of purely-lexical
   lemmas, plus **259** verbal roots that MW and Whitney both record but DCS
   attests **zero** times. Here the evidence boundary is real and, for the
   present corpus, permanent: vocabulary the grammatical and lexicographic
   traditions carry that the surviving text corpus does not.

The pay-off for P3 is a sharpening: **registers are about citation *form*;
corpus-testing adds the *evidence* dimension.** The same `<ls>` slot holds a
text citation, a recoverable hedge, and an irrecoverable kośa attestation — three
evidentiary statuses in one formal register. This is "evidence-graded
lexicography" (the book's Ch. 2 method) applied to the citation apparatus itself.

A corollary refines the register's *measured size*. Of MW's citations, **22.3%**
are meta / relative (`L.`, `ib.`, `W.`, `MW.`, `Cat.`) — structurally unable to
point at a primary-text scan. But the relative class is largely an artefact of
compression: a document-order antecedent walk resolves the 10,094 `ib.` ("ibidem")
citations to a real Register-A source — **57.1% with high confidence** (the
antecedent in the same headword), up to a **74.7% mechanical upper bound** including
cross-boundary cases (`MBh.` 1,149, `RV.` 1,064, …). *These are resolvable, not yet
hand-verified.* So the "meta" fraction overstates how much of Register A is genuinely
sourceless; once `ib.` is resolved, the apparatus is more connected than the raw tag
counts suggest.

## Evidence

| # | Finding | Number | What it shows for P3 | Module |
|---|---|---|---|---|
| 1 | `L.`-hedge corpus-recoverability | 31% of 18,930 (stable 2021/2026) | the hedge is a recoverable evidence gap, not absence | [lexicographer_dcs/](../../lexicographer_dcs/) |
| 2 | Corpus-absent residue | ~69% of purely-lexical lemmas; **259** roots with 0 DCS | the hard floor of the lexicographic/grammatical register | [lexicographer_dcs/](../../lexicographer_dcs/), [root_crosswalk/](../../root_crosswalk/) |
| 3 | `ib.` resolvability | 57.1% same-cluster (high-conf); 74.7% upper bound — *resolvable, not verified* | the relative apparatus is largely recoverable; "meta" overstates sourcelessness | [relative_refs/](../../relative_refs/) |
| 4 | Botanical sub-register | 72% of 7,063 plant headwords `L.`-only; **1,567** corpus-confirmed | the gradient in one semantic field — kośa technical vocabulary partly corpus-real | [botanical_glossary/](../../botanical_glossary/) |
| 5 | Apparatus ceiling | 22.3% meta + 40.2% bare-locator | the true text-linkable fraction of Register A | [ROADMAP §W1](../../ROADMAP.md) |

## Methodological control (must travel with the claim)

Every lemma-level corpus join here is exposed to **homograph collision**: a common
word with a rare hedged sense (`kṛṣṇa` the deity vs the plant; `tā` a grammatical
form vs "Lakṣmī") is attested in the corpus for the *wrong* sense, inflating
"recoverability". Both corpus modules control for it — by restricting to lemmas
whose every sense is hedged (the 18,930 *strict* set) and, for botany, to
botanical-only headwords (the 1,567). The honest figure (~31%) is the controlled
one; a naive join reports higher and is wrong. P3 must carry this caveat, because
it bounds the central claim: this is **lemma-now** evidence; sense-level
verification (does the corpus attest *the hedged sense*?) needs sense-tagged data
and is deferred (the *sense-next* step, shared with P6 and the crosswalk).

> 🟡 **Sense-next prep built 04-07-2026** ([sense_verify/](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/sense_verify/README.md)):
> a deterministic 80-sense sample (60 band-3 `L.`-hedged + 20 text-cited
> controls) with MW entry text and DCS-2026 contexts, packaged as an
> interactive verification sheet. **The band-3 hand-verify itself remains the
> open human gate**; its output (`SENSE_VERIFY_RESULTS.md`) will supply the
> sense-level figure with a built-in method ceiling.

## Proposed placement in P3

A single section — *"The corpus test: evidentiary status within the European
register"* — after the Register A / Register B exposition and before the
indigenous-register treatment. It converts the binary register distinction into a
**form × evidence** matrix and supplies MW's column.

**Register B's column is now partly filled** ([register_b/](register_b/)): the
indigenous register is **constitutively lexicographic** — 40.5% of SKD's `iti`
citations target a named kośa/nighaṇṭu (a floor), so the `L.` hedge MW marks as
*exceptional* is Register B's *default*. Yet that vocabulary is **~half
corpus-grounded** (SKD 51.3%, VCP 48.9% of headwords in DCS, stem-aware). The
corpus test thus completes the matrix: a constitutively-lexical *citation style*
does not entail a corpus-detached *vocabulary*. Remaining open (shared with P4):
VCP's lexical-citation share (its source vocabulary differs from SKD's) and
sense-level verification.

> ✅ **Fixed 2026-06-13** ([CODE_REVIEW.md](../CODE_REVIEW.md) #1–#3, #7): the iti-citation regex and the de-inflection are corrected; the figures here (**40.5%** kośa share, **51.3%** SKD grounding) are the post-fix values.

## What this is **not**

- Not the nine-dictionary comparison (atlas).
- ~~Not a Register-B (*iti*) result.~~ Now includes a first Register-B corpus test ([register_b/](register_b/)); the nine-dict comparison remains atlas work.
- Not sense-level — lemma-level only, with the homograph control above.
- Not committed to any paper draft yet: this memo is the **evidence block** to be
  pulled into the canonical P3 draft (which will live in the SanskritLexicography
  paper pipeline, not in MWS).
