---
paper_id: A39
title: "Grammar, Dictionary, Corpus: Where the Three Authorities Disagree about Sanskrit Verbal Roots"
status: draft (skeleton, 2/5) — scaffolded 2026-07-08 (H158)
readiness: 2/5
venue: "WSC 2027 / Lexikos / IIJ / ISCLS (once mature)"
author: "**Mārcis Gasūns**, independent scholar ([ORCID 0000-0003-4513-884X](https://orcid.org/0000-0003-4513-884X)), gasyoun@ya.ru"
data_source: "WhitneyRoots/crosswalk/ (ppp_validation.json, token_attribution.json, root spine) + MWS/root_crosswalk/ (class_concordance.csv, root_crosswalk.csv); DCS corpus via VisualDCS DCS-2026 extraction"
---

# Grammar, Dictionary, Corpus: Where the Three Authorities Disagree about Sanskrit Verbal Roots

_Created: 08-07-2026 · Last updated: 08-07-2026_

> **Draft status (2026-07-08, readiness 2/5).** Skeleton scaffolded per
> [H158](https://github.com/gasyoun/Uprava/blob/main/handoffs/H158-Fable_WhitneyRoots_a39_verbal_roots_disagreement_scaffold_04.07.26.md).
> Every numerical claim below is transcribed from a committed artifact and carries a row in the
> claim→artifact inventory (§ Data and reproducibility). Sections marked ⬜ are outlined, not yet prose.
> **Open before drafting continues (author/@DO):** (1) venue choice (WSC 2027 / Lexikos / IIJ /
> a later ISCLS edition — MG ruled 04-07-2026 the current ISCLS is too early); (2) the
> WhitneyRoots adjudication queues ([docs/DECISIONS_NEEDED.md](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md))
> are human-gated — this paper **reports** the queue and its evidentiary method, it does not
> resolve it; (3) cite A38's dataset DOI once minted.
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

## 1. Introduction ⬜

- The three authorities and what each actually asserts about a verbal root:
  - **Grammar** (Whitney 1879/1889 *Sanskrit Grammar*; Whitney 1885 *Roots, Verb-Forms and
    Primary Derivatives*): root identity, present class(es), attested tense-systems, PPP —
    philologically curated, period-tagged (V/B/S/E/C), but a single scholar's judgment.
  - **Dictionary** (Monier-Williams 1899 via the Cologne digitization): root senses, class in
    the `cp` attribute, cross-anchors to Whitney's root pages (`<info whitneyroots>`) and to
    Westergaard's Dhātupāṭha edition (`<info westergaard>`) — a compilation whose class data
    descends from the Petersburg lexicons and the indigenous Dhātupāṭha tradition.
  - **Corpus** (Digital Corpus of Sanskrit, DCS-2026 extraction — cite A38): lemmatized token
    attestation with frequencies — but its per-lemma "grammar" field is lexicon metadata, and
    its lemmatization is model output (ByT5-Sanskrit; see §5).
- Why disagreement is the interesting object: each source's failure mode is different, so
  systematic three-way comparison localizes *which* authority is wrong (or whether the
  comparison itself is ill-posed — the homonym problem).
- Contribution statement: (1) the quantified three-way disagreement inventory over the 935-root
  Whitney hub; (2) the panel-verified finding that corpus-corroborated PPP mismatches are
  homonym/doublet signals, not corrections (0/13 genuine errors); (3) the negative result turned
  method: two corpus blind spots (I/VI accent collapse; IV/passive) that any grammar-vs-corpus
  comparison must control for; (4) the FAIR adjudication queue with pre-pulled Grammar-§
  evidence, released for Sanskritist review.

## 2. Related work ⬜

- **A04 (homonym-key alignment, csl-atlas)** — the method this paper validates and consumes:
  homonym-aware keys across Cologne dictionaries. Cite for the alignment method; A39 supplies
  its verbal-root validation and citation base. Do NOT re-derive the key scheme here.
- **A35 (Pāṇinian derivation across 10 dictionaries, csl-orig `etymology_stats/`)** — the
  dictionary-side root-derivation census; cite for how dictionaries encode root attributions.
- **A38 (DCS 2026 release, VisualDCS)** — the corpus denominator (98,606 lemmas); cite for the
  extraction pipeline and release; do not re-describe it.
- **Hellwig NLP cluster** (verified live 04-07-2026, see
  [WhitneyRoots/.ai_state.md](https://github.com/gasyoun/WhitneyRoots/blob/main/.ai_state.md) Dev Notes):
  - Hellwig & Nehrdich 2018, rcNN sandhi/compound segmentation, EMNLP —
    [aclanthology.org/D18-1295](https://aclanthology.org/D18-1295/).
  - Nehrdich, Hellwig & Keutzer 2024, ByT5-Sanskrit unified
    segmentation/lemmatization/tagging, Findings of EMNLP —
    [aclanthology.org/2024.findings-emnlp.805](https://aclanthology.org/2024.findings-emnlp.805/).
    **Framing: this model *produces* the DCS lemma attribution treated as "corpus evidence" —
    lemmatizer error is a first-class candidate source of spurious grammar-vs-corpus
    disagreement (§5), not just background.**
  - (Lower priority: Hellwig et al. 2020 Vedic treebank, LREC —
    [aclanthology.org/2020.lrec-1.632](https://aclanthology.org/2020.lrec-1.632/) — syntax layer,
    not the lemma/morphology layer disputed here.)
- **vidyut-prakriya** (Pāṇinian form generator, MIT) — used strictly as an *advisory* witness
  (paradigm generation + PPP validation), never as an auto-corrector; cite the WhitneyRoots
  pilot finding that generator evidence binds a gaṇa only through the present system.
- Whitney's *Roots* digitizations (warnemyr.com mirror as the machine-readable source);
  Westergaard's *Radices* as the Dhātupāṭha witness inside MW.
- ⬜ Check the next ISCLS TOC for adjacent work before submission (none found as of 04-07-2026).

## 3. Data and method ⬜

### 3.1 The 935-root Whitney hub (WhitneyRoots)
- Root spine re-derived per-homonym from the warnemyr mirror of Whitney 1885 (930 keyed roots;
  35 `class_uncertain` kept separate from asserted class); FAIR emission (CSV/SQLite/RDF, 24k+
  triples).
- Layer joins: DCS frequency fold (713/930 with tokens), MW + Apte dictionary alignment
  (765/930 linked), Whitney Grammar §-concordance (7,315 root→form-category→§ edges).

### 3.2 The MW-side crosswalk (MWS `root_crosswalk/` — canonical for §4.1–4.2 numbers)
- 2,113 MW verbal-root records; 813 with a Whitney anchor, 1,309 with a Westergaard anchor;
  734 distinct MW-anchored roots matched to the hub (3 unmatched = candidate anchor errors).
- Class extraction: MW `cp` digits vs Whitney roman classes; `cp="0P"` treated as a sentinel
  (no gaṇa assigned), not a conflict.
- Leniency guard: hub classes are unioned over homonyms sharing a bare root, so measured
  conflicts are conservative — real disagreements, not homonym artifacts.

### 3.3 The PPP validation harness (WhitneyRoots `crosswalk/ppp_validation.json`)
- vidyut-prakriya generated kta (primary + causative ṇic) vs warnemyr's recorded PPP doublets
  vs DCS top attested form; comparison via a length-preserving, nasal-folding `form_key`
  (naive NFD+strip normalization destroys vowel length and retroflexion — method caveat worth
  a footnote; see [SanskritLexicography FINDINGS](https://github.com/gasyoun/SanskritLexicography/blob/master/FINDINGS.md)).
- Two-gate homonym binding for generated paradigms: gaṇa membership + present-stem
  corroboration (the present carries gaṇa identity; the PPP is shared across classes and
  cannot bind one).
- Corpus PPP attestation joined from the VisualDCS verbal-forms DB
  ([dcs_ppp_verified.tsv](https://github.com/gasyoun/VisualDCS/blob/main/derived-data/Glagolnye-formy/Bazadannyh-glagolnyh-form-Korpusa/dcs_ppp_verified.tsv),
  5,181 corpus-attested PPP forms + counts) — **magnitude-only evidence: frequency is not a
  grammatical rule** (provenance caveat carried from the source).

### 3.4 The adjudication protocol
- Authority order (fixed ex ante): **Grammar > Whitney Roots > corpus > Zaliznyak-style
  accent index** — corpus is lowest.
- Human queues with pre-pulled Grammar-§ evidence
  ([DECISIONS_NEEDED.md](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md)):
  Queue A (16 kept class additions, each with a §-citation verdict), Phase-0 audit
  (7 capture-gaps + 16 class smears), PPP §3a homonym keeps (3).
- The paper reports the queue and protocol; resolution is expert work outside its scope.

## 4. Results: the disagreement inventory ⬜

### 4.1 Class (gaṇa) disagreement, MW vs Whitney
- Comparable roots (both assign ≥1 class): **651** of 737 anchored.
- **Agree 376 (57.8%) · overlap 249 (38.2%) · conflict 26 (4.0%)** —
  [class_concordance.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/class_concordance.csv).
- Of the 26 disjoint-class conflicts, **18 carry a Westergaard/Dhātupāṭha anchor** — the
  indigenous class is available as tiebreaker (per `has_westergaard` in the CSV: carv, cūṣ,
  guph, knū, kṛp, kṣā, majj, mlā, paś, pyā, sphā, spṛh, styā, taḍ, vruḍ, vyā, śyā, ḍamb —
  note the summary doc's 18-row conflict table is the first 18 of the 26 alphabetically, NOT
  this set; re-count from the CSV, not the table).
- ⬜ Case studies: cūṣ (MW 1 vs Whitney 4 — Whitney's own §240b is phonological only, class IV
  is from *Roots*); paś (MW 10 vs Whitney 4).

### 4.2 Attestation coverage, three ways
- Whitney hub: **809/935 (86.5%) in MW · 590/935 (63.1%) in DCS · 550 (58.8%) in all three** —
  [ROOT_CROSSWALK_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/ROOT_CROSSWALK_SUMMARY.md).
- 259 roots MW+Whitney but corpus-absent (the grammarians'/lexical stratum); 40 DCS+Whitney but
  MW-unanchored (anchoring gap); 86 in none of MW/DCS.
- Caveat carried from the source: the triangulation joins on the homonym-collapsed bare root —
  "in all three" does not assert the three mean the *same* homonym (homonym-level alignment is
  §4.4 / A04's layer).

### 4.3 Participles: the panel finding
- Validator verdicts: **327 match · 11 mismatch, of which 3 corpus-corroborated** (of 338
  roots with a recorded PPP; the validator checks 384 roots in total, the rest lacking a
  recorded form: 33 `fill_candidate` + 13 `vidyut_only`) —
  [ppp_validation.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/ppp_validation.json).
- The headline: a 3-verifier Sanskritist panel on the 13 corpus-corroborated mismatches
  (13/13 unanimous): **zero are errors in Whitney's record**. 10/13 resolve once the full
  doublet list and the causative kta are honoured; the 3 survivors (iṣ "send", mṛ "crush",
  hā "go forth") are homonym artifacts — the corpus form belongs to a *different* same-spelled
  root that the DCS lemma conflates.
- Consequence (the paper's thesis in miniature): **corpus signal vs a curated inventory is a
  homonym/variant detector, not a correction list.**

### 4.4 Homonym attribution: how far the corpus can be split
- DCS's own per-token lemma_id separation recovers per-homonym frequencies for **26 reliable
  splits** (vid know 9,391 / find 1,923; as be 35,466 / throw 287; kṛ make 40,555 / scatter
  211 …) — [token_attribution.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/token_attribution.json).
- The ceiling: of 38 DCS-lumped homonym groups, only **5 are gaṇa-distinct** (morphologically
  separable at all); the other 33 share a gaṇa — past this point homonym splitting is a
  lexical-semantic task, and **no morphological tool changes that** (both vidyut-prakriya and
  the ND-SWSMP alignment dataset were piloted; neither raises coverage).

### 4.5 The grammar disagreeing with itself ⬜
- Whitney self-contradiction found during accent-rule encoding: derivative ī-stem G.pl — §320
  "not thrown forward" vs §319a (RV *bahvīnā́m* "usually") vs §356's own printed *nadī́nām* —
  encoded as a per-lemma variant cell and validated against attested Rig-Veda accents.
  Use as the §7 discussion anchor: "authority" is not internally monolithic either.

## 5. Sources of spurious disagreement (caveats as first-class results) ⬜

1. **The I/VI accent collapse.** DCS is unaccented; class I (*cárati*, guṇa root, root accent)
   and class VI (*tudáti*, weak root, suffix accent) have identical unaccented surface
   present-stems. A naive corpus verifier returns "I, VI" for nearly every thematic root — in
   the WhitneyRoots pipeline this manufactured **117 spurious class additions, all reverted**.
   Only root-vowel grade distinguishes them without accent, and only where guṇa would change
   the vowel. Any grammar-vs-corpus class comparison that does not control for this reports
   fake agreement.
2. **Class IV vs passive.** Both are *root+ya* presents unaccented (*jñāyate*, *dhriyáte* are
   passives, not class IV) — same structural blindness.
3. **UD `Tense=Past` conflation.** The DCS/UD tense layer collapses aorist and perfect —
   tense-system attestation claims inherit this granularity limit.
4. **"Corpus class" is lexicon metadata.** DCS `lemma.grammar` descends from the
   Böhtlingk/MW tradition — a grammar-vs-corpus class disagreement is largely
   **lexicon-vs-lexicon**, never independent corpus proof. Likewise the PPP attestation
   evidence is magnitude-only (frequency ≠ rule).
5. **Lemmatizer error.** DCS lemma/tag attribution is ByT5-Sanskrit model output
   (Nehrdich et al. 2024) — model error is a candidate source of any individual mismatch and
   must be named alongside genuine variation.
6. **Digitization noise on the grammar side.** The machine-readable Whitney (warnemyr mirror)
   carries apparatus bleed, ASCII-romanization collapse (ṣ/ś/ṛ), and doublet truncation —
   quantified and repaired in the WhitneyRoots pipeline (39 apparatus-bleed records; 6
   gloss-bleeds; doublet/causative-aware validation moved mismatches 33→13, then 13→11 after
   diacritic restoration of the two Whitney-confirmed doublets kṣubh/piś — cite the JSON's
   current `_meta.counts`, not the intermediate 33→13 step logged in the pipeline journal).

## 6. The released artifacts ⬜

- The adjudication queue with §-evidence (DECISIONS_NEEDED.md, regenerable).
- The FAIR crosswalk (CSV/SQLite/RDF) + per-verdict provenance fields (`match_basis`,
  `matched_against`, `matched_form`) making every validator verdict revisable.
- ⬜ Decide at drafting time: freeze a versioned snapshot of both canonical builds for the
  paper (kosha manifest row + DOI via `/data-release`).

## 7. Discussion and conclusion ⬜

- The three authorities fail differently: grammar errs by singular judgment (and occasionally
  self-contradicts, §4.5), the dictionary by inherited compilation, the corpus by conflation
  (homonyms, accentlessness, model error). Triangulation therefore localizes error — but only
  after the conflation channels of §5 are controlled.
- The 4.0% hard class conflict + the 0/13 PPP panel result together argue the curated
  inventories are far more reliable than raw corpus signal suggests — the corpus's real value
  against them is *detection* (of homonymy, doublets, capture gaps), not correction.
- Positioning: this is the validation and citation base for homonym-key alignment (A04)
  across the Cologne dictionaries.

## Data and reproducibility — claim→artifact inventory

| # | Claim (as used above) | Number(s) | Committed artifact | Status |
|--:|---|---|---|---|
| 1 | MW vs Whitney class concordance | 651 comparable; 376/249/26 = 57.8/38.2/4.0% | [class_concordance.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/class_concordance.csv) + [CLASS_CONCORDANCE_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/CLASS_CONCORDANCE_SUMMARY.md) | ✅ committed |
| 2 | Dhātupāṭha tiebreaker availability | 18 of 26 conflicts | [CLASS_CONCORDANCE_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/CLASS_CONCORDANCE_SUMMARY.md) | ✅ committed |
| 3 | Three-way coverage of the hub | 809 MW (86.5%) · 590 DCS (63.1%) · 550 both (58.8%) · 259/40/86 residues | [ROOT_CROSSWALK_SUMMARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/ROOT_CROSSWALK_SUMMARY.md) + [root_crosswalk.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/root_crosswalk.csv) | ✅ committed |
| 4 | MW anchor errors | 3 unmatched | [mw_whitney_unmatched.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/root_crosswalk/mw_whitney_unmatched.csv) | ✅ committed |
| 5 | PPP validator verdicts | 338 with recorded PPP: 327 match · 11 mismatch (3 corpus-corroborated); 384 checked | [ppp_validation.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/ppp_validation.json) `_meta.counts` | ✅ committed |
| 6 | Panel: 0/13 corpus-corroborated mismatches are Whitney errors; 3 homonym keeps | 13/13 unanimous; §3a table (iṣ/mṛ/hā) | [DECISIONS_NEEDED.md §3](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md) | ✅ committed (regenerable) |
| 7 | 117 spurious I/VI additions reverted | 117 (of 139 audited; 120 total reverted) | WhitneyRoots Phase-8 revert ([.ai_state.md](https://github.com/gasyoun/WhitneyRoots/blob/main/.ai_state.md) + [review_queue.json](https://github.com/gasyoun/WhitneyRoots/blob/main/review_queue.json)) | ✅ committed; ⬜ cite the revert commit/PR precisely |
| 8 | Token-level homonym splits | 26 reliable splits; 38 lumped groups, 5 gaṇa-distinct | [token_attribution.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/token_attribution.json) | ✅ committed |
| 9 | Adjudication queues | Queue A 16 rows · Phase-0 7 GAP + 16 SMEAR | [DECISIONS_NEEDED.md §1–2](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/DECISIONS_NEEDED.md) | ✅ committed (regenerable) |
| 10 | Corpus PPP attestation join | 5,181 verified PPP forms | [dcs_ppp_verified.tsv](https://github.com/gasyoun/VisualDCS/blob/main/derived-data/Glagolnye-formy/Bazadannyh-glagolnyh-form-Korpusa/dcs_ppp_verified.tsv) | ✅ committed (VisualDCS) |
| 11 | Whitney self-contradiction (ī-stem G.pl accent) | §319a vs §320 vs §356 | [accent_rules.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/accent_rules.json) + [ACCENT_VALIDATION_REPORT.md](https://github.com/gasyoun/WhitneyRoots/blob/main/docs/ACCENT_VALIDATION_REPORT.md) | ✅ committed |
| 12 | DCS-2026 denominator | 98,606 lemmas | A38 / [VisualDCS CHANGELOG.md](https://github.com/gasyoun/VisualDCS/blob/main/CHANGELOG.md) + [m6_validation.md](https://github.com/gasyoun/VisualDCS/blob/main/src/DCS-data-2026/reports/m6_validation.md) — NB [dcs_lemma_summary.json](https://github.com/gasyoun/VisualDCS/blob/main/dcs_lemma_summary.json) is DCS-**2021** (83,239 lemmas), do not cite it for this figure | ✅ committed; ⬜ cite A38 DOI when minted |

## References ⬜

- Whitney, W. D. 1889. *Sanskrit Grammar*, 2nd ed. — [Wikisource digitization](https://en.wikisource.org/wiki/Sanskrit_Grammar_(Whitney)).
- Whitney, W. D. 1885. *The Roots, Verb-Forms, and Primary Derivatives of the Sanskrit Language*.
- Monier-Williams, M. 1899. *A Sanskrit-English Dictionary* — Cologne digitization ([csl-orig](https://github.com/sanskrit-lexicon/csl-orig)).
- Westergaard, N. L. 1841. *Radices linguae Sanscritae* (the Dhātupāṭha witness via MW `<info westergaard>`).
- Hellwig, O. Digital Corpus of Sanskrit — via the DCS-2026 extraction (A38).
- Hellwig, O. & S. Nehrdich. 2018. [Sanskrit word segmentation using character-level recurrent and convolutional neural networks](https://aclanthology.org/D18-1295/). EMNLP.
- Nehrdich, S., O. Hellwig & K. Keutzer. 2024. [One model is all you need: ByT5-Sanskrit…](https://aclanthology.org/2024.findings-emnlp.805/). Findings of EMNLP.
- ⬜ A04, A35, A38 self-citations once their DOIs/venues freeze; vidyut-prakriya citation.

_Dr. Mārcis Gasūns_
