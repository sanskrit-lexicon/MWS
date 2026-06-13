# MW analysis modules — index & architecture notes

Read-only analytical studies of `mw.txt` (and joins to external corpora) added
2026-06-13. Each module is a self-contained directory: a Python script, its
derived CSV(s), and a summary. **Analysis only — none mutate `mw.txt`.**

## Modules

| Module | What it answers | Headline | Actionable output |
|---|---|---|---|
| [lexicographer_dcs/](lexicographer_dcs/) | Which `<ls>L.</ls>` lexicographer-only lemmas does the corpus now attest? | 30.2% (DCS-2021) / 31.4% (DCS-2026) of 18,930 strict purely-lex lemmas — stable across snapshots | retire-candidate CSVs |
| [relative_refs/](relative_refs/) | Resolve `ib.` (and spec `id.`/#98) to antecedent sources | 7,538/10,094 (74.7%) `ib.` → real source | `ib_resolved.csv` candidate map |
| [botanical_glossary/](botanical_glossary/) | Sanskrit ↔ Linnaean glossary (#74) | 8,923 `<bot>` → 7,063 headwords / 1,223 species; 1,528 clean L.-only + DCS-attested | FAIR dataset + synonym rings |
| [phw_graph/](phw_graph/) | Audit MW's phrasal-headword cross-reference graph | 2,364 edges, 99.3% reciprocal | **31 broken-link bugs** → `phw_integrity.csv` |
| [root_crosswalk/](root_crosswalk/) | MW ↔ Whitney ↔ DCS root crosswalk + class concordance | 550/935 roots fully triangulated; 94.4% class agree/overlap, 32 conflicts | 40-root anchor gap; 32 class conflicts |

See each module's `README.md` / `*SUMMARY.md` for method, caveats, and numbers.
A recurring methodological theme: lemma-level corpus joins suffer **homograph
collisions** (a common word with a rare hedged sense) — every corpus-join module
documents how it controls for this.

## Architecture status — known debt, refactor deferred (2026-06-13)

**Decision (M.G.):** keep modules as-is for now; **no refactor or repo split.**
The debt below is recorded so it is a deliberate deferral, not an oversight.

Known debt (from the 2026-06-13 architecture review):
1. **No shared library.** The `<L>`/`<LEND>` parser is re-implemented in all 7
   scripts; the SLP1↔IAST map (×4), `K1_RE`/`LS_RE` (×4), `bare()` (×2), and
   locale boilerplate (×7) are copy-pasted. Copies have already diverged.
2. **Reinvented transcoder.** [mwtranscode/transcoder.py](mwtranscode/transcoder.py)
   (`transcoder_processString`) is importable and complete; the hand-rolled maps
   are partial (no accents) and will drift from canonical.
3. **Cross-repo coupling.** Modules read `csl-orig`, `VisualDCS`, `WhitneyRoots`
   via hardcoded `../../` paths — non-portable, undeclared. The corpus-join
   modules (`lexicographer_dcs`, `root_crosswalk`) are conceptually
   cross-dictionary work that would normally live in **csl-atlas**.
4. **Corpus-snapshot inconsistency.** DCS-2021 summary vs DCS-2026 sqlite vs
   WhitneyRoots' 2026 CoNLL-U are mixed across modules that cross-cite — pin one
   before the numbers go into P3.
5. **2.7 MB of committed, unstamped derived data** that will silently drift when
   `mw.txt` changes. No `{mw_revision, corpus_version, date}` provenance stamp.
6. **No committed test** on the correctness-critical transcoder.
7. **No naming convention** across dirs / scripts / summary files.

Deferred target (when a refactor is greenlit): a shared `analysis/mwlib/`
(`parse.py`, `translit.py` wrapping the canonical transcoder, `io.py` with
provenance stamping, `corpus.py` with a pinned DCS snapshot, committed tests);
each study drops to ~40–60 LOC; corpus-join modules move to csl-atlas; bulk
derived CSVs `.gitignore`d behind a regenerate target. **Not scheduled.**

## Security (reviewed 2026-06-13)

**Clean — zero high/medium findings.** Threat model: local, read-only batch
scripts over trusted project data, run manually. Scan results:

- **No** code execution (`eval`/`exec`/`subprocess`/`pickle`), **no** network
  egress, **no** user/argv/env input, **no** hardcoded secrets.
- SQL: the single query is a static string — no injection surface.
- Writes go only to each module's own dir (`os.path.join(HERE, …)`); no deletes,
  no path traversal. Committed outputs leak no local paths / PII.
- Outputs are public CC-licensed MW content joined to public corpus stats —
  nothing sensitive.

Informational (defense-in-depth, no action): scripts implicitly trust the
sibling-repo `.sqlite`/JSON inputs and set no resource bounds — both fine under
the trusted-input model. The architecture debt above is a maintainability, not a
security, concern.
