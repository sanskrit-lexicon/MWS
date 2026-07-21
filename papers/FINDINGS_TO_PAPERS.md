# Findings → paper pipeline (2026-06-13 session)

Maps this session's analysis modules to the paper pipeline so the roadmap stays
honest about what evidence exists. Canonical pipeline + venues live in
[SanskritLexicography/ROADMAP_2026_2027.md](https://github.com/sanskrit-lexicon/SanskritLexicography/blob/master/ROADMAP_2026_2027.md);
this note is the index from the MWS-side evidence.

## Paper-bound findings

| Finding (module) | Paper | Venue | Contribution | Status |
|---|---|---|---|---|
| **Sense-as-record** ([papers/microanalysis/PAPER.md §4.1](microanalysis/PAPER.md)) | **P1** block economy | IJL | explains the F11 <1% figure: senses are records, not in-entry blocks | **drafted into paper** |
| **`L.`→DCS** ([lexicographer_dcs/](../lexicographer_dcs/)) | **P3** citation registers | Dictionaries | Register A's `L.` hedge is ~31% corpus-recoverable (stable 2 snapshots) | in [SYNTHESIS](p3_citation_registers/SYNTHESIS.md) |
| **`ib.` resolver** ([relative_refs/](../relative_refs/)) | **P3** | Dictionaries | 74.7% of relative cites resolve → "meta" overstates Register A's sourcelessness | in SYNTHESIS |
| **Botanical `L.`-attestation** ([botanical_glossary/](../botanical_glossary/)) | **P3** | Dictionaries | the evidentiary gradient in one semantic field (1,567 confirmed) | in SYNTHESIS |
| **Register-B corpus test** ([papers/p3_citation_registers/register_b/](p3_citation_registers/register_b/)) | **P3** + **P4** | Dictionaries / IJL·WSC | Register B is constitutively lexicographic (SKD 40.5% `iti`→kośa) yet ~half corpus-grounded (SKD 51.3%, VCP 48.9%) | drafted (memo) |
| **Root crosswalk MW↔Whitney↔DCS** ([root_crosswalk/](../root_crosswalk/)) | **P6** learner's layer | Lexikos | the corpus+grammar+dict join P6 needs (550/935 roots triangulated by bare-root match) | data ready |
| **Class concordance** ([root_crosswalk/](../root_crosswalk/)) | **P6** (or grammar note) | — | MW vs Whitney conjugation class: 96.0% agree/overlap, 26 *candidate* conflicts | data ready, **needs Sanskritist** |
| **Corpus-absent roots** (root_crosswalk) | **P3/P4** | — | 259 MW+Whitney roots DCS attests zero times — the hard grammarian residue | in SYNTHESIS |

## Two cross-cutting threads

- **A shared methods caution** belongs in every corpus-join paper (P3/P4/P6) and
  in the book's Ch. 2 (*evidence-graded lexicography*): lemma-level corpus joins
  are confounded by (i) **homograph collision** (a common word's rare hedged sense)
  and (ii) **headword-form mismatch** (SKD nominative `aMSaH` vs DCS stem `aMSa`;
  the legacy digit-encoding in the authority links). Every module here documents
  its control; the controlled figure is always lower than the naive one. The
  recurring lesson — *an apparent absence may be a convention, not a gap* — is the
  same one P4 ("When zero means nothing") is built on.
- **`sense-now` vs `sense-next`.** Everything here is **lemma-level**. The shared
  open step across P3/P6 is sense-level corpus verification (does the corpus attest
  *the hedged sense*?), which needs sense-tagged data.

## Not paper-bound (infrastructure, supports all)

- **phw graph** ([phw_graph/](../phw_graph/)) — DATA_DICTIONARY documentation + a
  31-link `bug` correction batch (maintainer-gated).
- **`<ls>` link candidates** ([mwauthorities/link_candidates/](../mwauthorities/link_candidates/)) — W1 authority work, not a paper.
- **DATA_DICTIONARY additions** — tag documentation; keeps the data honest.

## Open (your calls, not Opus's)

- Which paper to push first; branch for the paper edits (`master` vs `docs-pass`).
- P3 memo → section prose; P1 abstract update.
- The 32 class conflicts and the band-3 `L.` subset need a Sanskritist, not a model.
