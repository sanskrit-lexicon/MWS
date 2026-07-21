---
paper_id: A39
title: "Grammar, Dictionary, Corpus: Where the Three Authorities Disagree about Sanskrit Verbal Roots"
status: draft (full prose, 3/5) — scaffolded 2026-07-08 (H158), drafted 2026-07-21 (H1383)
readiness: 3/5
venue: "WSC 2027 / Lexikos / IIJ / ISCLS (once mature)"
author: "**Mārcis Gasūns**, independent scholar ([ORCID 0000-0003-4513-884X](https://orcid.org/0000-0003-4513-884X)), gasyoun@ya.ru"
data_source: "WhitneyRoots/crosswalk/ (ppp_validation.json, token_attribution.json, root spine) + MWS/root_crosswalk/ (class_concordance.csv, root_crosswalk.csv); DCS corpus via VisualDCS DCS-2026 extraction"
---

# Grammar, Dictionary, Corpus: Where the Three Authorities Disagree about Sanskrit Verbal Roots

_Created: 08-07-2026 · Last updated: 21-07-2026_

> **Draft status (2026-07-21, readiness 3/5).** Full prose draft per
> [H1383](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1383-Fable_WhitneyRoots_a39-verbal-root-disagreement-skeleton-to-draft_20.07.26.md),
> written by Fable 5 (`claude-fable-5`) over the skeleton scaffolded per
> [H158](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H158-Fable_WhitneyRoots_a39_verbal_roots_disagreement_scaffold_04.07.26.md).
> Every numerical claim carries a row in the claim→artifact inventory (§ Data and
> reproducibility); every headline count states its instrument and its error exposure in the
> text. Two figures were corrected against the current artifacts during drafting: the MW-side
> record count (750 typed verbal-root records, 810 anchored roots matched — the skeleton's
> 2,113/734 predated [PR #238](https://github.com/sanskrit-lexicon/MWS/pull/238)) and the
> §-concordance size (9,878 edges on 790 roots — the skeleton's 7,315/785 predated the
> category-detection fixes logged in
> [WhitneyRoots/.ai_state.md](https://github.com/gasyoun/WhitneyRoots/blob/main/.ai_state.md)).
>
> **Open before submission (author/@DO):**
> (1) **venue** — WSC 2027 / Lexikos / IIJ / a later ISCLS edition; the standing ruling
> (04-07-2026) is that the current ISCLS is too early; reaching 3/5 activates the question and
> a human decides it; (2) the WhitneyRoots adjudication queues
> ([docs/DECISIONS_NEEDED.md](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md))
> are human-gated — this paper **reports** the queue and its evidentiary method, it does not
> resolve it; (3) cite the A38 dataset DOI and the A04/A35 venue details once minted/frozen;
> (4) the §6 snapshot-freeze decision (versioned snapshots of both canonical builds via
> `/data-release`) is open — a human decides; (5) re-check the next ISCLS TOC for adjacent
> work at submission time (none found as of 04-07-2026).
>
> **Canonical-build note.** The MW↔Whitney↔DCS triangulation exists in TWO independent builds
> (a known duplication — [Uprava/PROJECT_INTERLINKS.md](https://github.com/gasyoun/Uprava/blob/main/PROJECT_INTERLINKS.md)):
> the MW-anchored build in [MWS/root_crosswalk/](https://github.com/sanskrit-lexicon/MWS/tree/master/root_crosswalk)
> and the Whitney-hub-keyed build in [WhitneyRoots/crosswalk/](https://github.com/gasyoun/WhitneyRoots/tree/main/crosswalk).
> This paper treats **MWS `root_crosswalk/` as canonical for the class-concordance and coverage
> numbers** (it reads MW's own `<info whitneyroots>`/`<info westergaard>` anchors and `cp`
> attribute directly from the source `mw.txt`) and **WhitneyRoots `crosswalk/` as canonical for
> the PPP-validation, homonym-attribution, and paradigm evidence** (it is keyed on the 935-root
> Whitney hub with per-homonym resolution). Neither build is re-derived here.
>
> **Anti-salami note.** A39 is the *disagreement-quantification and validation* paper. The
> homonym-key method it relies on is **A04's contribution (cited, not re-derived)**; the DCS-2026
> corpus release that supplies the attestation denominator is **A38's contribution (cited, not
> re-described)**; the Pāṇinian-derivation coverage of the ten Cologne dictionaries is **A35's**.
> A39 does not lead with any of those claims.

## Abstract

For a Sanskrit verbal root, three kinds of authority make overlapping claims: the Western
grammatical tradition (Whitney's *Sanskrit Grammar* and its 1885 *Roots* supplement), the
dictionary (Monier-Williams 1899, itself compiled from the Petersburg lexicons and carrying the
indigenous Dhātupāṭha class tradition in its `cp` attribute), and the annotated corpus (the
Digital Corpus of Sanskrit). Digitization makes the three comparable at scale for the first time
— and they systematically disagree about root identity, conjugation class (gaṇa), and attested
participial forms. We quantify the disagreement over a 935-root hub keyed to Whitney's roots:
of **651** roots where both MW and Whitney assign a present class, the two **agree outright on
57.8%**, **overlap on 38.2%**, and **conflict on 4.0%** (26 roots, 18 of them adjudicable by the
Westergaard/Dhātupāṭha class as a third witness). Against the corpus, **86.5%** of the hub is
attested in MW but only **63.1%** in DCS, with **58.8%** triangulated in all three. On
participles, a generator-assisted validation of 338 recorded past passive participles finds
**327 matches and 11 residual mismatches, 3 of them corpus-corroborated — and a
three-verifier panel found that not one
corpus-corroborated mismatch is an error in the grammatical record**: every apparent
"correction" the corpus suggests is a homonym artifact or a legitimate aniṭ/seṭ doublet. The
central methodological finding is therefore a caution: corpus signal against a curated root
inventory is a **homonym and variant detector, not a correction list**. We show two structural
reasons why: (i) the unaccented corpus cannot distinguish class I from VI, or class IV presents
from passives, which silently manufactures agreement where the grammar is in fact specific; and
(ii) the corpus "class" is lexicon metadata inherited from the same Petersburg tradition as the
dictionary, so grammar-vs-corpus class comparisons are largely lexicon-vs-lexicon. We release
the disagreement inventory as an adjudication queue with per-item Grammar-§ evidence, and
position it as the validation layer for homonym-key alignment across the Cologne dictionaries.

## 1. Introduction

Ask what a Sanskrit verbal root *is*, and the answer depends on whom you ask. For the Western
grammatical tradition, a root is a philological reconstruction: Whitney's *Sanskrit Grammar*
(1879, 2nd ed. 1889) and its companion volume *The Roots, Verb-Forms, and Primary Derivatives
of the Sanskrit Language* (1885) record, for each root, an identity, one or more present
classes, the tense-systems actually attested, and the past passive participle — each claim
period-tagged (Vedic, Brāhmaṇa, Sūtra, Epic, Classical) and each resting, ultimately, on a
single scholar's reading of the texts available to him in 1885. For the dictionary, a root is a
compilation: Monier-Williams (1899) descends from the Petersburg lexicons of Böhtlingk and
Roth, and its digitized form carries the root's conjugation class in a `cp` attribute whose
class numbers transmit the indigenous Dhātupāṭha tradition — the Cologne digitization makes
this explicit by anchoring root entries both to Whitney's 1885 root pages (`<info
whitneyroots>`) and to Westergaard's edition of the Dhātupāṭha (`<info westergaard>`). And for
the annotated corpus, a root is an emergent property of annotation: the Digital Corpus of
Sanskrit (DCS) attests lemmata with token frequencies, but its lemmatization is model output,
and the "grammar" field attached to each lemma is lexicon metadata, not corpus observation.

Until recently these three kinds of claim could only be compared anecdotally, root by root, by
a scholar with all three works open on the desk. Digitization changes that: with Whitney's
*Roots* parsed into a structured spine, MW's anchors and class attributes machine-readable, and
DCS queryable by lemma, the three authorities can be joined and their disagreements *counted*.
This paper does so, over a hub of 935 root entries keyed to Whitney's inventory, and reports
what the counting shows.

The result is not the one a naive reading of "data-driven lexicography" would predict. The
three authorities do disagree — on class assignment, on attestation, on participial forms — but
when each disagreement is traced to its source, the great majority dissolve into artifacts of
the comparison itself: same-spelled roots conflated under one join key, unaccented surface
forms that neutralize exactly the distinction at issue, and corpus metadata that silently
restates one of the parties rather than witnessing independently. The disagreements that
survive this filtering are few, and they are precisely the philologically interesting ones.
The paper's central finding is methodological and deliberately negative: **corpus signal
measured against a curated root inventory functions as a homonym and variant detector, not as
a correction list.** We state this as a result, not a limitation, because acting on the
opposite assumption demonstrably corrupts the inventory: in our own pipeline, a naive
corpus-verification pass wrote 117 spurious class assignments before being caught and
reverted (§5.1).

Why is disagreement the interesting object at all? Because the three authorities fail in
*different* ways. The grammar errs by singular judgment — Whitney read everything, but he read
it alone, and we exhibit a case where his own paragraphs contradict one another (§4.5). The
dictionary errs by inheritance — its class data descends through the Petersburg lexicons from
the Dhātupāṭha, so a dictionary "confirmation" of the Dhātupāṭha is often the same witness
counted twice. The corpus errs by conflation — homonyms lumped under one lemma, accent lost,
model error in the annotation layer. Because the failure modes are disjoint, systematic
three-way comparison can localize *which* authority is wrong about a given root — or show that
the comparison itself is ill-posed, which turns out to be the modal case.

The contributions are: (1) the quantified three-way disagreement inventory over the 935-root
Whitney hub — class concordance, attestation coverage, and participle validation, every count
carrying its instrument and error exposure in the text; (2) the panel-verified finding that
corpus-corroborated participle mismatches are homonym and doublet signals, not corrections
(0 of 13 genuine errors, §4.3); (3) the negative result turned method: two structural corpus
blind spots — the class I/VI accent collapse and the class IV/passive collapse — that any
grammar-vs-corpus comparison must control for, quantified at 117 manufactured assignments in
our own pipeline before the control existed (§5); and (4) a FAIR adjudication queue with
pre-pulled Grammar-§ evidence, released for expert review rather than auto-applied (§6).

## 2. Related work

This paper sits inside a small cluster of sibling studies on the Cologne Digital Sanskrit
Dictionaries and takes care to consume rather than restate them. The homonym-aware key scheme
that aligns root entries across the Cologne dictionaries is the contribution of A04, which this
paper *validates* on the verbal-root domain and supplies with a citation base; the key scheme
itself is not re-derived here. The DCS-2026 extraction that supplies our attestation
denominator — 98,606 corpus lemmata — is the contribution of A38, which documents the
extraction pipeline and its release; we cite its canonical figure and do not re-describe the
pipeline. The census of how the ten Cologne dictionaries encode Pāṇinian root derivations is
A35's. A39's own territory is the *disagreement layer*: what happens when the aligned sources
are actually compared.

On the corpus side, the relevant NLP lineage is Hellwig's. Hellwig & Nehrdich (2018)
established neural sandhi and compound segmentation for Sanskrit; Nehrdich, Hellwig & Keutzer
(2024) unified segmentation, lemmatization, and morphosyntactic tagging in a single
ByT5-Sanskrit model. The framing that matters for this paper: that model *produces* the DCS
lemma attribution we treat as "corpus evidence" throughout. Lemmatizer error is therefore not
background noise but a first-class candidate explanation for any individual grammar-vs-corpus
mismatch (§5.5), and the corpus column of every table in §4 should be read with that
provenance in mind. (Hellwig's Vedic treebank work, e.g. the 2020 LREC release, concerns the
syntax layer and is not directly disputed here.)

As a generative witness we use vidyut-prakriya, an open-source Pāṇinian derivation engine:
given a root and class, it generates the paradigm the Pāṇinian system licenses. We use it
strictly in an *advisory* role — paradigm generation and participle validation, never
auto-correction — following the pilot finding, reproduced in §3.3, that generator evidence can
bind a gaṇa only through the present system: the past passive participle is formed from the
root, not the present stem, and so cannot discriminate between candidate classes at all.

Finally, the source digitizations themselves: the machine-readable Whitney's *Roots* is the
warnemyr.com digitization (mirrored for this project), whose transcription quirks — apparatus
bleed, ASCII romanization collapse, doublet truncation — turn out to be measurable
contributors to apparent disagreement (§5.6); and Westergaard's *Radices linguae Sanscritae*
(1841) serves as the Dhātupāṭha witness, reaching this study through MW's own `<info
westergaard>` anchors rather than through a fresh digitization.

## 3. Data and method

### 3.1 The 935-root Whitney hub (WhitneyRoots)

The backbone of the study is a hub of 935 verbal-root entries keyed to Whitney's *Roots*,
maintained in the WhitneyRoots repository as
[`src/app_data.json`](https://github.com/gasyoun/WhitneyRoots/blob/main/src/app_data.json).
Its root spine was re-derived per-homonym from the full local mirror of the warnemyr
digitization of Whitney 1885 (939 pages): 930 roots parse to a keyed record, and 35 of those
carry a `class_uncertain` flag that keeps hesitant attributions separate from asserted classes.
Same-spelled roots are distinct entries with distinct homonym numbers (e.g. `1 paś` "see"
vs `2 paś` "fasten"), each with its own gloss, class set, participle record, and period tags —
the property the rest of the paper leans on.

Onto this spine three evidence layers are joined, each hard-guarded so that no join may write
into the class field it is supposed to test. The corpus fold attaches DCS frequency data to
713 of the 930 spine roots — frequency only; the guard exists precisely because of the
incident reported in §5.1. The dictionary alignment links 765 of 930 roots to MW and/or Apte
entries (MW 569, Apte 697), with 45 ambiguous links parked in a human queue rather than
auto-resolved (§3.4). The Grammar concordance links roots to the sections of Whitney's
*Grammar* that discuss their forms: 9,878 root → form-category → § edges over 790 of the 930
roots, spanning 34 detectable form categories, each edge validated against the fetched section
text. The whole crosswalk is emitted in FAIR form — CSV with a CSVW metadata sidecar,
normalized `root_class.csv`, SQLite, and RDF (24k+ triples, rdflib-validated) — in
[`WhitneyRoots/crosswalk/`](https://github.com/gasyoun/WhitneyRoots/tree/main/crosswalk).

*Instrument and exposure.* The spine inherits the warnemyr mirror's transcription noise
(quantified in §5.6), and its homonym numbering is not guaranteed to coincide with any other
source's numbering — which is why every cross-source join below either unions over homonyms
(§3.2) or binds them by morphological feature (§3.3), never by homonym number alone. No human
gold pass has been run over the spine extraction itself; its reliability is argued from the
audit trail (a 23-flag Phase-0 audit against the re-harvested mirror) rather than from an
inter-annotator statistic — a gap we flag rather than hide, and return to in §7.

### 3.2 The MW-side crosswalk (MWS `root_crosswalk/` — canonical for the §4.1–4.2 numbers)

The dictionary side is read directly from the Cologne source file `mw.txt`. MW records typed
as verbal roots (`verb="genuineroot"` or `verb="root"`) number **750**. Across the dictionary
the digitization carries **813** `<info whitneyroots>` anchors — each naming a root and its
page in Whitney's 1885 appendix — and **1,309** `<info westergaard>` anchors into the
Dhātupāṭha. Decoding the Whitney anchors (the number is an appendix *page*, shared by many
roots, not a root identifier) and joining on the homonym-normalized root string matches **810**
distinct MW-anchored roots to the hub, leaving **3 unmatched** — candidate anchor errors,
listed in
[`mw_whitney_unmatched.csv`](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/mw_whitney_unmatched.csv).
The join itself is the canonical implementation in
[`WhitneyRoots/scripts/root_triangulation.py`](https://github.com/gasyoun/WhitneyRoots/blob/main/scripts/root_triangulation.py);
the MWS-side script is a thin consumer and re-emitter, and a regression lock asserts the
published coverage figures so that a silently different join cannot slip past a re-run.

For the class concordance, a root qualifies when it carries *both* a Whitney anchor and a
non-empty `cp` class: **737** MW roots do. Class extraction reads the digits of the `cp`
attribute (`"1P,1Ā"` → {1}) against the hub's roman-numeral classes (`['I','IV']` → {1,4}),
with one sentinel rule: MW's `cp="0P"` means "pada known, no gaṇa assigned" and is dropped, so
a 0-only root counts as `mw_empty`, never as a conflict. Two design choices deliberately bias
the instrument *against* finding conflict. First, hub classes are unioned over all homonyms
sharing a bare root, and MW classes over all its genuine-root records for that bare root, so a
class match with *any* homonym counts as agreement. Second, the comparison is set-based:
"agree" requires identical class sets, "overlap" a non-empty intersection, and "conflict" only
disjoint sets. Of the 737 anchored-and-classed roots, **651** are comparable (both sources
assign at least one class); the remainder split into `whitney_empty` 57, `mw_empty` 18, and
`both_empty` 11.

*Instrument and exposure.* The concordance inherits whatever error lives in MW's `cp`
attribute and in the anchor layer — an anchor pointing at the wrong Whitney page attributes
one root's classes to another, and the three unmatched anchors show this error class is real,
if rare. The leniency guard means the reported conflict rate is a *floor*: real per-homonym
disagreements can hide inside an "overlap" verdict, and §4.1's paś case shows exactly that
mechanism producing the opposite artifact — a conflict verdict where no shared root is
actually disputed. No human gold pass has scored the extractor; what has been human-verified
is the 26-row conflict set itself, each row of which was re-derived from the CSV for this
paper (twice, catching the "two 18s" trap described in §4.1).

### 3.3 The PPP validation harness (WhitneyRoots `crosswalk/ppp_validation.json`)

The participle layer asks a sharper question than class concordance: for each root whose 1885
record includes a past passive participle, does the recorded form survive comparison against
(a) what the Pāṇinian system generates and (b) what the corpus attests? The harness,
[`scripts/vidyut_validate_ppp.py`](https://github.com/gasyoun/WhitneyRoots/blob/main/scripts/vidyut_validate_ppp.py),
generates the kta participle with vidyut-prakriya — both primary and causative (ṇic) — and
compares it against *all* of warnemyr's recorded PPP doublets and against the corpus's top
attested form. The comparison key is a length-preserving, nasal-folding normalization
(`form_key`): the naive NFD-decompose-and-strip approach destroys vowel length and
retroflexion, which in this domain are precisely the contrasts that distinguish forms (a
method caveat documented in
[SanskritLexicography FINDINGS](https://github.com/gasyoun/SanskritLexicography/blob/master/FINDINGS.md)).
A match needs only one recorded form to be generated, and every verdict records *why* it
matched: `match_basis` (spine form 317 · corpus_fill 33 · doublet 8 · source_alt 2) and
`matched_against` (vidyut 347 · dcs 10 · vidyut_caus 3), so any class of match can be revisited
later by filtering the JSON rather than re-running the pipeline.

Two further disciplines govern the harness. Homonym binding of generated paradigms is
two-gated — gaṇa membership plus present-stem corroboration — because the present stem carries
gaṇa identity while the PPP, formed from the root, is shared across classes and cannot bind
one. And corpus attestation is joined from the VisualDCS verbal-forms database
([`dcs_ppp_verified.tsv`](https://github.com/gasyoun/VisualDCS/blob/main/derived-data/Glagolnye-formy/Bazadannyh-glagolnyh-form-Korpusa/dcs_ppp_verified.tsv),
5,181 corpus-attested PPP forms with counts) as **magnitude-only evidence**: frequency of a
form is not a grammatical rule, a caveat carried from the source dataset and enforced in the
verdict logic (§4.3's "attestation, not a rule" residue class).

*Instrument and exposure.* The harness's own metadata block states its epistemic status
better than we could: it is *"Advisory; never edits the spine"*, and its surviving
corpus-corroborated mismatch class *"is a HOMONYM/VARIANT detector, NOT a correction signal"*
([`ppp_validation.json`](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/ppp_validation.json)
`_meta.note`) — the instrument's self-description is, in effect, this paper's thesis, written
at the point of measurement. Its blind spots: vidyut-prakriya generates what Pāṇini licenses,
so genuinely Vedic formations that fall outside the Pāṇinian system can only surface as
mismatches (a bias *toward* flagging the oldest material); and the corpus side inherits the
DCS lemmatization's homonym conflation, which is exactly what the panel in §4.3 found the
surviving flags to consist of.

### 3.4 The adjudication protocol

Nothing the instruments produce is applied automatically. The protocol fixes an authority
order *ex ante* — **Grammar > Whitney's Roots > corpus > accent index (Zaliznyak-style)** —
with the corpus deliberately lowest, and routes every candidate change into human queues with
the evidence pre-pulled:
[`DECISIONS_NEEDED.md`](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md)
currently holds Queue A (16 kept class additions, each with a Grammar-§ citation verdict of
the form "+IV: §770b — LEAN KEEP" or "✗ — NEEDS ZALIZNIAK"), the Phase-0 audit queue (7
capture-gaps and 16 class smears from the warnemyr re-harvest), and the three §3a homonym
keeps from the participle layer. The queues are regenerated from the data by script, so a
resolved item cannot silently resurrect.

Where this paper reports a human verdict, the panel behind it must be described precisely,
because it is the paper's main exposure to reliability critique: the §4.3 finding rests on a
**three-verifier Sanskritist panel** that examined the 13 corpus-corroborated participle
mismatches and reached unanimity on all 13 (13/13). That is a small expert panel with complete
agreement — it is *not* an inter-annotator reliability study, no κ statistic is computable
from a unanimous panel of three on 13 items, and we do not present it as one. The verdicts
are, however, fully auditable: each carries its evidence row (the recorded form, the generated
form, the corpus form, and the homonym or doublet that resolves the apparent clash) in
[`DECISIONS_NEEDED.md §3`](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md).
The paper reports the queue and its method; resolving the queues is expert work outside its
scope.

## 4. Results: the disagreement inventory

### 4.1 Class (gaṇa) disagreement, MW vs Whitney

Of the 651 comparable roots, the two traditions **agree outright on 376 (57.8%)**, **overlap
on 249 (38.2%)**, and assign **disjoint class sets on 26 (4.0%)** —
[class_concordance.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/class_concordance.csv).
Read against the instrument's deliberate leniency (§3.2), the striking figure is the smallness
of the conflict rate: after a century-and-a-half of independent transmission — Whitney reading
texts, Monier-Williams compiling lexica, the Dhātupāṭha propagating through both — the two
inventories place fewer than one root in twenty-five in genuinely different classes. Of the 26
conflicts, **18 also carry a Westergaard anchor**, so the indigenous Dhātupāṭha class is
available as a third witness for adjudication: carv, cūṣ, guph, knū, kṛp, kṣā, majj, mlā, paś,
pyā, sphā, spṛh, styā, taḍ, vruḍ, vyā, śyā, ḍamb. (A trap for the replicator: the summary
document's 18-row conflict table is the first 18 of the 26 *alphabetically* — a different set
of 18. The Westergaard-adjudicable set above is re-counted from the CSV's `has_westergaard`
column, and any reuse of these figures should re-count the same way.)

What does a conflict row actually contain? The two flagged during scaffolding repay close
reading, because they turn out to fail in opposite directions.

**cūṣ "suck" (MW class 1, Whitney class 4) — a real two-tradition disagreement, which the
corpus cannot adjudicate.** MW's entry (L 74874) reads "cl. 1. `cūṣati`, to suck, suck out",
citing Dhātup. xvii, 22 — and its Westergaard anchor (`cUza,17.22,01`) confirms that the
Dhātupāṭha assigns the same class 1. Whitney's hub entry records class IV. Whitney's *Grammar*
is silent on the question: its sole mention of cūṣ (§240b) is phonological, an item in a list
illustrating ū/o alternation, so the class-IV attribution rests on the 1885 *Roots* record
alone. Here, then, are the two Western sources genuinely split, with the indigenous tradition
siding with the dictionary — under the §3.4 authority order the Grammar cannot break the tie
(it says nothing), and the row goes to the expert queue. Could the corpus decide? No — and the
reasons are instructive. DCS attests the root at all of 22 tokens, its per-lemma class
metadata says "1" — but that metadata descends from the same Petersburg tradition as MW
(§5.4), so it is the dictionary's vote counted twice, not independent evidence. Worse, the
form that would support class IV, a middle `cūṣyate`, is attested — MW itself prints "Pass.
`cūṣyate`, to be sucked up" (Suśruta) — but an unaccented `°yate` is structurally ambiguous
between a class-IV present and a passive (§5.2). The corpus, lacking accent, cannot tell the
two readings apart; the one witness that could settle it is exactly the one digitization lost.

**paś (MW class 10, Whitney class 4) — an artifact of root identity, not a class
disagreement.** The concordance row looks dramatic — classes 10 and 4 do not even neighbor
each other — until one asks *which* paś each source classed. MW's only class-bearing paś
record (L 120526) is homonym 3: "cl. 10. P. `pāśayati`, to fasten, bind, Dhātup. xxxiii, 45"
— the Dhātupāṭha's denominative-looking root behind `pāśa` "noose", faithfully transmitted
with its Westergaard anchor (`paSa,33.45,10`). MW's paś "see" (homonym 1, L 120516) is
assigned *no class at all*: the entry reads "only Pres. P. Ā. `páśyati` (cf. √`dṛś` and Pāṇ.
vii, 3, 78)" — the dictionary declines to give a gaṇa to what it treats as the suppletive
present of dṛś. Whitney's class IV, meanwhile, belongs to paś "see" (`páśyati`); his
inventory has no class-10 "bind" at all. So the two class-bearing entries are *different
lexemes that happen to share a spelling*: no root is actually placed in two classes by two
authorities, and even the §3.2 leniency union cannot rescue the row, because the class sets of
the distinct homonyms never intersect. The verdict "conflict" is true of the join and false of
the scholarship — which is the paper's thesis in a single row. The correct repair is not to
change either source but to split the join key by homonym, which is A04's alignment layer, and
the row stands as positive evidence for needing it.

The general lesson of the case studies: a class conflict between curated inventories is a
*symptom* whose differential diagnosis — real scholarly disagreement (cūṣ) vs join-key
conflation (paś) — requires reading the entries, and the automated verdict cannot distinguish
the two. This is why the 26 rows are published as a queue with evidence attached (§6), not as
a correction list.

### 4.2 Attestation coverage, three ways

Joining the full 935-root hub against dictionary and corpus:
**809 roots (86.5%) are attested in MW, 590 (63.1%) in DCS, and 550 (58.8%) in all three** —
[ROOT_CROSSWALK_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/ROOT_CROSSWALK_SUMMARY.md).
The residues are as informative as the intersection. **259** roots stand in both Whitney and
MW but are absent from the corpus: the grammarians' and lexicographers' stratum — roots whose
warrant is a citation tradition rather than surviving usage the DCS happens to cover. **40**
roots are attested in both Whitney and DCS but carry no MW anchor: not missing knowledge but
an anchoring gap in the digitization, mechanically closable by adding `<info whitneyroots>`
anchors. **86** hub roots appear in neither MW nor DCS. The triangulated 550 form the working
core of a grammar–corpus–dictionary crosswalk: roots one can simultaneously define,
conjugate, and frequency-rank.

*Instrument and exposure.* These joins run on the homonym-collapsed bare root, so "in all
three" asserts co-presence of the *spelling*, not identity of the *lexeme* — the paś row
above is the cautionary example, and homonym-level alignment is A04's layer, not this table.
The DCS column additionally inherits the lemmatizer provenance of §5.5: "attested in DCS"
means "the ByT5-Sanskrit annotation pipeline assigned at least one token to this lemma", which
for rare roots is a weaker claim than it sounds. The coverage figures are pinned by a
regression lock in the emitting script, so the published numbers cannot drift from the
committed artifact without failing the build.

### 4.3 Participles: the panel finding

The validator checked **384** roots; **338** of them have a recorded PPP in the 1885 record,
and of those, **327 match** and **11 mismatch** under the §3.3 matching rules (the remaining
46: 33 roots where only the corpus supplies a candidate form, `fill_candidate`, and 13 where
only the generator does, `vidyut_only`) —
[ppp_validation.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/ppp_validation.json)
`_meta.counts`. The mismatch history matters as much as the count: an earlier, stricter run
flagged 33; honoring warnemyr's full comma-separated doublet lists and vidyut's causative kta
resolved 20 of those as legitimate matches; diacritic restoration of two ASCII-collapsed
source forms (kṣubh, piś — both independently confirmed as single-root doublets by Whitney's
*Grammar* §956b) brought the residue to the current 11. Each resolution class is recorded in
the per-item provenance fields, so the trajectory is auditable, and the current `_meta.counts`
— not any intermediate figure — is the citable state.

The corpus corroborates the generator against the record in only **3** of the 11 surviving
mismatches. The naive reading — "the corpus and the Pāṇinian generator agree against Whitney,
so Whitney is wrong" — is the reading the three-verifier panel (§3.4) tested against the
historical set of **13** corpus-corroborated flags, and rejected in every case, 13/13
unanimous: **not one is an error in Whitney's record.** Ten of the 13 dissolved under the
doublet-and-causative refinement above. The three that remain flagged are homonym artifacts,
kept deliberately: iṣ "send", whose recorded seṭ participle `iṣitá` is correct while the
corpus's `iṣṭa` belongs to same-spelled iṣ "desire" (aniṭ); mṛ "crush" (`mūrṇá`), shadowed by
the corpus-dominant mṛ "die" (`mṛtá`); and hā "go forth" (`hāna`), shadowed by hā "abandon"
(`hīna`). In each, the DCS lemma lumps two same-spelled roots, and the corpus's "correction"
is the participle of the *other* one. A further residue class is left open on principle: for
10 roots the recorded form equals the corpus's most frequent attested form while the generator
produces a more regular alternative — an attestation agreement, not a rule, and one a grammar
cannot adjudicate (a grammar states which forms are possible, not which are frequent), so
these stay parked in the queue
([DECISIONS_NEEDED.md §3e](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md)).

The consequence, stated at the scale this evidence licenses: on this layer, with n = 13 and a
unanimous panel of three, **every apparent corpus correction to the curated participle record
resolved to homonymy or legitimate variation.** That is the paper's thesis in miniature —
corpus-vs-inventory signal detects conflation and doublets; it does not correct scholarship —
and we resist generalizing it beyond the participle layer: it is a strong finding on a small
n, from a panel, not a reliability study.

### 4.4 Homonym attribution: how far the corpus can be split

If homonym conflation is the dominant artifact, the natural question is how much of it the
corpus itself can resolve. DCS internally distinguishes some same-spelled verbal lemmata by
`lemma_id`; mapping each lemma_id to the Whitney homonym whose gaṇa matches recovers
per-homonym token frequencies for **26 reliable splits** (of 72 candidate groups; the other 46
fail the reliability gates — coverage ≥ 0.55, distinct homonyms on both sides) —
[token_attribution.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/token_attribution.json).
Where the split succeeds it is decisive: vid "know" 9,391 tokens vs vid "find" 1,923; as "be"
35,466 vs as "throw" 287; kṛ "make" 40,555 vs kṛ "scatter" 211. These are exactly the
frequency asymmetries that explain §4.3's homonym artifacts — the corpus-dominant homonym
swamps the rarer one under a shared lemma.

The ceiling is structural. Of the 38 homonym groups DCS lumps under a single lemma_id, only
**5 are gaṇa-distinct** — separable by any morphological signal at all. The remaining 33 share
a gaṇa, so no paradigm-based tool can split them even in principle: both vidyut-prakriya and a
word-sense-style alignment dataset were piloted against this residue, and neither raised
coverage. Past this point homonym splitting is a lexical-semantic task — the honest statement
of where the morphological program ends.

### 4.5 The grammar disagreeing with itself

The comparison so far treats each authority as internally coherent, and for one measured cell
Whitney is demonstrably not. Encoding his accent rules for machine validation forced a
decision his text does not make. For derivative (polysyllabic) feminine stems in -ī/-ū, §320
rules that these stems decline like the corresponding short-vowel stems "save that the tone is
not thrown forward upon the ending in gen. plural" — genitive plural accent stays on the stem,
`-ī́nām`. His own §319a, one page earlier, reports that in the Rig-Veda the bahvī́-type
adjectives "usually" *do* throw the accent forward: `bahvīnā́m`. And §356's printed paradigm
quietly takes a side, giving `nadī́nām`, `tanū́nām` — the §320 pattern, against §319a's
frequency claim. Three paragraphs, two incompatible accentuations, no reconciliation in the
text: the encoding records the cell as a per-lemma *variant*
([accent_rules.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/accent_rules.json),
rule R13), because forcing either value would mis-score forms Whitney himself prints.

The variant cell then becomes a measurement target: which pattern does the accented corpus
attest? The answer, so far, is thinner than the question deserves — the Rig-Veda yields only
**two** attested genitive plurals in this cell across the sampled lemmata, `rathī́nām` (RV
1.11.1) and `vadhū́nām` (RV 8.19.36), both re-verified against VedaWeb's accented text, and
both carrying the acute on the stem vowel — the §356/§320 pattern, not §319a's (an earlier run
had mislabeled both; the re-read is documented, with query provenance, in
[ACCENT_VALIDATION_REPORT.md](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/ACCENT_VALIDATION_REPORT.md)).
Both attested lemmata are nouns, consistent with Whitney's noun/adjective split rather than
refuting it; at n = 2 the contradiction stays open as a measurement question. The point for
this paper is not the resolution but the existence of the cell: **"authority" is not
internally monolithic either.** When §7 weighs grammar against corpus, this is the reminder
that the grammar column, too, has error bars — and that encoding a reference work precisely
enough to validate against a corpus is itself a way of discovering contradictions a century of
readers passed over.

## 5. Sources of spurious disagreement (caveats as first-class results)

Every comparison in §4 is shadowed by channels that manufacture disagreement — or, worse,
manufacture agreement — without any authority being wrong. We treat these as results, not
limitations: each was measured in this pipeline, several at material scale, and any
grammar-vs-corpus comparison in this domain will hit all six.

**5.1 The class I/VI accent collapse.** Whitney's class I (`cárati`: guṇa root, root accent)
and class VI (`tudáti`: weak root, suffix accent) contrast principally in accent placement —
and DCS is unaccented. Their unaccented thematic present stems are therefore very often
identical in surface form, and a naive corpus verifier duly "confirms" both classes for nearly
every thematic root. This is not hypothetical: in this project's own Phase-6 pipeline, exactly
that verifier wrote **117 spurious I/VI class additions** into the working inventory before a
critical review caught the mechanism, and all were reverted (within a 120-addition revert:
117 I/VI collapses, 2 invalid IV-vs-passive additions, and one smeared +VI — WhitneyRoots
commit
[6aa5adc](https://github.com/gasyoun/WhitneyRoots/commit/6aa5adc) and
[PR #9](https://github.com/gasyoun/WhitneyRoots/pull/9) for the three that had landed on
empty-class baselines). Without accent, only root-vowel grade distinguishes the classes, and
only where guṇa would visibly change the vowel. A grammar-vs-corpus class comparison that does
not control for this reports *fake agreement* — the corpus appears to confirm whichever class
the grammar states, plus one more.

**5.2 Class IV vs passive.** The same structural blindness, second instance: a class-IV
present (`nahyati`) and a middle passive (`jñāyate`, `dhriyáte`) are both unaccented
root-plus-`ya` formations. The accent distinguishes them (`náhyati` vs `jñāyáte`); the corpus
surface form does not. §4.1's cūṣ shows the consequence at adjudication time: the attested
`cūṣyate` is evidence for Whitney's class IV under one accentuation and mere passive
morphology under the other, and the unaccented corpus cannot say which.

**5.3 UD `Tense=Past` conflation.** The DCS/UD tense layer collapses aorist and perfect into
a single past label, so any attestation claim about *tense-systems* — Whitney's per-root
attested-systems record being a natural comparison target — inherits that granularity limit.
Comparisons in this paper therefore stop at the present-system and participle layers.

**5.4 "Corpus class" is lexicon metadata.** The class field DCS carries per lemma descends
from the Böhtlingk/MW lexicographic tradition — the same tradition MW itself transmits. A
grammar-vs-corpus class comparison is therefore largely **lexicon-vs-lexicon**: when the
corpus's metadata "sides with" MW against Whitney (as in cūṣ, §4.1), no second witness has
spoken; the first witness has been counted twice. Genuine corpus evidence for a class is
attested *forms* — and 5.1–5.2 bound how much those can say without accent. The same
discipline applies to the participle layer: attestation frequency is magnitude-only evidence
(§3.3), never a rule.

**5.5 Lemmatizer error.** Every DCS lemma and tag in this study is model output
(ByT5-Sanskrit; Nehrdich et al. 2024). Model error is therefore a standing candidate
explanation for any *individual* mismatch, alongside genuine variation — one more reason the
protocol (§3.4) routes candidate corrections to humans rather than applying them. We name
this channel rather than quantify it: no gold pass over the DCS annotations was run here, and
the corpus columns of §4 are conditioned on the annotation pipeline's correctness.

**5.6 Digitization noise on the grammar side.** The machine-readable Whitney is a
transcription with measurable artifacts: the pipeline identified and repaired 39
apparatus-bleed records and 6 gloss-bleeds, and the participle-mismatch trajectory of §4.3
(33 → 13 → 11) was driven substantially by transcription phenomena — truncated doublet lists
and ASCII romanization collapse (ṣ/ś/ṛ flattened) — rather than by anything Whitney wrote.
Two forms (kṣubh, piś) changed verdict on diacritic restoration alone. The general rule this
enforces: cite the current
[`ppp_validation.json`](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/ppp_validation.json)
`_meta.counts`, never an intermediate pipeline figure, and treat any comparison against a
digitized reference as a comparison against *the digitization* until the source scan has been
consulted.

## 6. The released artifacts

The study's outputs are released as revisable evidence, not as applied corrections. The
adjudication queue
([DECISIONS_NEEDED.md](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md))
is regenerated by script from the underlying data and carries, per item, the pre-pulled
Grammar-§ evidence a reviewer needs: the 16 Queue-A class additions each cite the section that
licenses (or fails to license) the added class; the Phase-0 audit rows carry both sources'
classes; the §3 participle rows carry the recorded, generated, and attested forms with the
resolving homonym or doublet. The FAIR crosswalk
([WhitneyRoots/crosswalk/](https://github.com/gasyoun/WhitneyRoots/tree/main/crosswalk):
CSV + CSVW, normalized `root_class.csv`, SQLite, RDF) preserves per-verdict provenance —
`match_basis`, `matched_against`, `matched_form` — precisely so that every validator verdict
in this paper can be *revised* by filtering, without re-running the pipeline: the §3e
attestation matches, for instance, are recoverable as `matched_against == "dcs"`. The
MW-side build
([MWS/root_crosswalk/](https://github.com/sanskrit-lexicon/MWS/tree/master/root_crosswalk))
ships the concordance CSV, the coverage tables, and the generating scripts, with the coverage
figures regression-locked.

One release decision is deliberately left open: whether to freeze versioned, DOI-carrying
snapshots of both canonical builds (via the org's data-release process, with a kosha manifest
row) at submission time, so that the paper's numbers cite an immutable artifact rather than a
moving repository head. The trade-off — citation stability against duplicate-artifact
maintenance — is recorded here; a human decides at the venue gate.

## 7. Discussion and conclusion

The three authorities fail differently, and the shape of this study's evidence tracks that
difference. The grammar errs by singular judgment — and, §4.5 shows, occasionally by internal
contradiction that only machine-precision encoding surfaces. The dictionary errs by
inheritance: its class layer transmits the Dhātupāṭha through the Petersburg tradition, which
is exactly why its "agreements" with the corpus's lexicon-derived metadata carry so little
independent weight (§5.4). The corpus errs by conflation: homonyms lumped by the lemmatizer,
accent lost in transcription, model error in annotation. Because the failure modes are
disjoint, triangulation genuinely localizes error — the 40 MW-unanchored roots of §4.2 are a
digitization gap, not a scholarly one; the paś conflict is a join artifact; the cūṣ conflict
is a real two-tradition split awaiting expert adjudication — but *only after* the conflation
channels of §5 are controlled. Uncontrolled, the same comparisons manufacture agreement and
disagreement in quantity: 117 spurious class confirmations from one channel alone.

Put together, the 4.0% hard-conflict rate on classes and the 0-of-13 panel result on
participles argue that the curated inventories are substantially more reliable than raw
corpus signal would suggest. Where the corpus appeared to correct Whitney, it was — in every
panel-examined case — detecting something real but different: a homonym split the lemma layer
collapses, a doublet the record abbreviates, a capture gap in the digitization. That is
genuine value. A corpus run against a curated inventory is a powerful *detector* — of
homonymy, of variation, of transcription loss — and this study's queues, filled by exactly
that detector, are its constructive output. What the corpus signal is not, on this evidence,
is a *correction list*; the asymmetry deserves to be stated plainly because the opposite
default — auto-applying corpus "corrections" to curated resources — is the natural engineering
temptation, and in our own pipeline it lasted exactly one review cycle.

The limits of this study are the limits its instruments disclose. The headline counts rest on
extractors and a generator with no human-gold reliability pass (§3.1–§3.3); the one human
verdict is a unanimous three-expert panel on thirteen items, not an inter-annotator study
(§3.4); the corpus columns are conditioned on a neural annotation pipeline (§5.5); and the
accent evidence that would resolve both §5.1 and §5.2 — and Whitney's own §4.5 contradiction —
exists only for the accented Vedic slice of the corpus, where our first measurement returned
n = 2. Each of these is a stated exposure, and together they define the follow-up program: a
human-gold pass with a reliability statistic per instrument, homonym-level alignment as the
join key (A04's layer, for which this study supplies the validation case), and accented-corpus
measurement of the variant cells. Until then, the finding stands at the scale claimed: three
authorities, digitized and joined, disagree far less than they appear to — and where they
appear to, the first suspect is the instrument, not the scholar.

## Data and reproducibility — claim→artifact inventory

| # | Claim (as used above) | Number(s) | Committed artifact | Status |
|--:|---|---|---|---|
| 1 | MW vs Whitney class concordance | 651 comparable of 737; 376/249/26 = 57.8/38.2/4.0%; non-comparable 57/18/11 | [class_concordance.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/class_concordance.csv) + [CLASS_CONCORDANCE_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/CLASS_CONCORDANCE_SUMMARY.md) | ✅ committed; re-derived from the CSV 21-07-2026 |
| 2 | Dhātupāṭha tiebreaker availability | 18 of 26 conflicts (`verdict=conflict` ∧ `has_westergaard=yes`) | [class_concordance.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/class_concordance.csv) | ✅ committed; re-counted from the CSV (the summary's 18-row table is a different, alphabetical 18) |
| 3 | Three-way coverage of the hub | 809 MW (86.5%) · 590 DCS (63.1%) · 550 both (58.8%) · 259/40/86 residues | [ROOT_CROSSWALK_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/ROOT_CROSSWALK_SUMMARY.md) + [root_crosswalk.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/root_crosswalk.csv); regression-locked in [root_crosswalk.py](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/root_crosswalk.py) | ✅ committed |
| 4 | MW-side record and anchor counts | 750 typed verbal-root records · 813 `whitneyroots` + 1,309 `westergaard` anchors · 810 matched · 3 unmatched | [ROOT_CROSSWALK_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/ROOT_CROSSWALK_SUMMARY.md) + [mw_whitney_unmatched.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/mw_whitney_unmatched.csv) | ✅ committed (updated by [PR #238](https://github.com/sanskrit-lexicon/MWS/pull/238); supersedes the skeleton's 2,113/734) |
| 5 | PPP validator verdicts | 384 checked; 338 with recorded PPP = 327 match + 11 mismatch (3 corpus-corroborated); 33 `fill_candidate` · 13 `vidyut_only`; `match_basis` 317/33/8/2; `matched_against` 347/10/3 | [ppp_validation.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/ppp_validation.json) `_meta` | ✅ committed; `_meta` re-read 21-07-2026 |
| 6 | Panel: 0/13 corpus-corroborated mismatches are Whitney errors | 13/13 unanimous; 10 auto-resolved by doublet+causative refinement (§3d); 3 homonym keeps iṣ/mṛ/hā (§3a); 10 attestation-only matches left open (§3e) | [DECISIONS_NEEDED.md §3](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md) | ✅ committed (regenerable) |
| 7 | 117 spurious I/VI additions reverted | 117 I/VI (of 139 audited; 120 total reverted incl. 2 IV-vs-passive + 1 smeared +VI) | WhitneyRoots commit [6aa5adc](https://github.com/gasyoun/WhitneyRoots/commit/6aa5adc) (`revert_collapse_additions.py`) + [PR #9](https://github.com/gasyoun/WhitneyRoots/pull/9) (3 onto-empty survivors) + [review_queue.json](https://github.com/gasyoun/WhitneyRoots/blob/main/review_queue.json) | ✅ committed; revert commit/PR cited |
| 8 | Token-level homonym splits | 26 reliable of 72 groups (46 unreliable); vid 9,391/1,923 · as 35,466/287 · kṛ 40,555/211; ceiling: 5 gaṇa-distinct of 38 lumped groups | [token_attribution.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/token_attribution.json) | ✅ committed; splits re-read 21-07-2026 |
| 9 | Adjudication queues | Queue A 16 rows · Phase-0 7 GAP + 16 SMEAR · §3a 3 keeps | [DECISIONS_NEEDED.md §1–3](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md) | ✅ committed (regenerable) |
| 10 | Corpus PPP attestation join | 5,181 verified PPP forms (magnitude-only) | [dcs_ppp_verified.tsv](https://github.com/gasyoun/VisualDCS/blob/main/derived-data/Glagolnye-formy/Bazadannyh-glagolnyh-form-Korpusa/dcs_ppp_verified.tsv) | ✅ committed (VisualDCS) |
| 11 | Whitney self-contradiction (ī-stem G.pl accent) + empirical split | §320 vs §319a vs §356; variant cell R13; n=2: rathī́nām (RV 1.11.1), vadhū́nām (RV 8.19.36), both stem-accented after the H115 re-read | [accent_rules.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/accent_rules.json) + [ACCENT_VALIDATION_REPORT.md](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/ACCENT_VALIDATION_REPORT.md) | ✅ committed |
| 12 | DCS-2026 denominator | 98,606 lemmas | A38 / [VisualDCS CHANGELOG.md](https://github.com/gasyoun/VisualDCS/blob/main/CHANGELOG.md) + [m6_validation.md](https://github.com/gasyoun/VisualDCS/blob/main/src/DCS-data-2026/reports/m6_validation.md) — NB [dcs_lemma_summary.json](https://github.com/gasyoun/VisualDCS/blob/main/dcs_lemma_summary.json) is DCS-**2021** (83,239 lemmas), do not cite it for this figure | ✅ committed; cite A38 DOI when minted |
| 13 | Hub layer joins (§3.1) | 935 hub entries; 930 keyed spine + 35 `class_uncertain`; DCS fold 713/930; dict links 765/930 (MW 569, Apte 697; 45 ambiguous); §-concordance 9,878 edges on 790/930 roots (34 categories); RDF 24k+ triples | [app_data.json](https://github.com/gasyoun/WhitneyRoots/blob/main/src/app_data.json) + [root_section_edges.csv](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/root_section_edges.csv) + [roots.ttl](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/roots.ttl) + [.ai_state.md](https://github.com/gasyoun/WhitneyRoots/blob/main/.ai_state.md) | ✅ committed; edge/root counts re-counted from the CSV 21-07-2026 (supersede the skeleton's 7,315/785) |
| 14 | Case-study particulars (§4.1) | cūṣ: MW L 74874 cl. 1, Dhātup. xvii, 22, DCS 22 tokens, DCS class-tag "1"; paś: MW L 120526 hom 3 cl. 10 (Dhātup. xxxiii, 45), L 120516 hom 1 classless "only Pres. páśyati" | [csl-orig mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) (L 74874, 120516, 120526) + [roots.csv](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/roots.csv) (nos. 234, 446, 447) | ✅ committed; read from source 21-07-2026 |

## References

- Whitney, W. D. 1889. *Sanskrit Grammar*, 2nd ed. Cambridge, MA: Harvard University Press —
  [Wikisource digitization](https://en.wikisource.org/wiki/Sanskrit_Grammar_(Whitney)).
- Whitney, W. D. 1885. *The Roots, Verb-Forms, and Primary Derivatives of the Sanskrit
  Language*. Leipzig: Breitkopf & Härtel — machine-readable via the warnemyr.com digitization
  (project mirror: [samskrtam.ru/whitney-roots](https://samskrtam.ru/whitney-roots/)).
- Monier-Williams, M. 1899. *A Sanskrit-English Dictionary*. Oxford: Clarendon Press —
  Cologne digitization ([csl-orig](https://github.com/sanskrit-lexicon/csl-orig)).
- Westergaard, N. L. 1841. *Radices linguae Sanscritae*. Bonn: König — the Dhātupāṭha witness
  via MW `<info westergaard>`.
- Hellwig, O. *Digital Corpus of Sanskrit (DCS)* — via the DCS-2026 extraction (A38).
- Hellwig, O. & S. Nehrdich. 2018. [Sanskrit word segmentation using character-level recurrent
  and convolutional neural networks](https://aclanthology.org/D18-1295/). *EMNLP 2018*.
- Nehrdich, S., O. Hellwig & K. Keutzer. 2024. [One model is all you need:
  ByT5-Sanskrit…](https://aclanthology.org/2024.findings-emnlp.805/). *Findings of EMNLP 2024*.
- Prasad, A. *vidyut-prakriya* — Pāṇinian word generator, part of the Vidyut toolkit (MIT
  license) — [github.com/ambuda-org/vidyut](https://github.com/ambuda-org/vidyut).
- VedaWeb: *Online Research Platform for Rig-Veda* (accented text; CC BY 4.0), University of
  Cologne — [vedaweb.uni-koeln.de](https://vedaweb.uni-koeln.de/) (accessed for the §4.5
  attestation queries; the host's availability caveat is documented in the accent report).
- *A04, A35, A38 self-citations to be completed once their DOIs/venues freeze (see draft-status
  blockquote).*

_Dr. Mārcis Gasūns_
