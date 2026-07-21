# SPEC-4 — W4: integrate the 2026-07 siglum adjudication into the atlas tooling

_Created: 02-07-2026 · Last updated: 02-07-2026_

**Tier:** Sonnet 5 (`claude-sonnet-5`). **Repo:** [csl-atlas](https://github.com/sanskrit-lexicon/csl-atlas)
(PR off `origin/main` via fresh worktree — this repo has known branch-contention; never
re-run the R2 checkpoint/drift/promotion seeders).

## Objective

Make the tooling consume the curated verdicts shipped in
[PR #185](https://github.com/sanskrit-lexicon/csl-atlas/pull/185)
([dict-source-aliases.json](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/data/dicts/dict-source-aliases.json) +
[mw-source-layers.json](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/data/mw-source-layers.json) v1.2.0),
and regenerate the candidate worklist so the August batch starts from families 51+.

## Steps

1. **Fold-rule fix**: in [scripts/lib/source-siglum.mjs](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/scripts/lib/source-siglum.mjs)
   `foldSiglum()` (and its Python port `fold_siglum()` in
   [scripts/obs/siglum_families.py](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/scripts/obs/siglum_families.py) —
   note: there is no separate `baseForm` function; the roman-numeral strip goes inside
   these two fold functions):
   strip trailing lowercase roman-numeral tokens before clustering. Add unit cases:
   `raghiii→ragh`, `dhatupxxxii→dhatup`, `paniv→pan`, `mbhi→mbh`, `susri→susr`,
   and negative cases `hariv→hariv` (the v is part of the siglum!), `divyav→divyav`,
   `malav→malav`, `rajav→rajav`, `vikram→vikram` — trailing-roman stripping must require a
   token boundary that doesn't eat real sigla ending in i/v/x letters; when in doubt the
   candidate CSV context decides, and any ambiguous key goes to the curated table instead.
2. **Generator honors the curated table**: `siglum_families.py` reads
   dict-source-aliases.json and emits `status` = `merged`/`distinct`/`uncertain`/`unreviewed`
   per family (member-level notes for mixed families) instead of the flat `unreviewed`.
   Align its docstring path (`src/data/dict-source-aliases.json` →
   `src/data/dicts/dict-source-aliases.json`).
3. Regenerate [data/obs/siglum_family_candidates.csv](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/data/obs/siglum_family_candidates.csv);
   report in the PR: raw sigla → fold-keys → families before/after (expected: ~120
   pseudo-members disappear; several families empty).
4. **mw-source-layers lookup check**: verify the consumer normalizes NFC/NFD before map
   lookup (mw.txt `<ls>` content vs composed JSON keys — the ś = s+U+0301 trap in
   [SanskritLexicography FINDINGS](https://github.com/gasyoun/SanskritLexicography/blob/master/FINDINGS.md));
   add a normalization shim + test if it doesn't.
5. Produce the per-dict raw-form evidence tables for the quarantined keys
   (`ratnam`, `samk`, `burn`, `mahav`, `bhar`, `maitr`: which dictionary, which raw
   spellings, counts) → `data/obs/siglum_uncertain_evidence.csv` — **evidence only, no
   merging**; the August planning session rules on them.

## Acceptance

- Unit tests green incl. the negative cases; regenerated CSV row count reported.
- No change to any verdict in the curated JSON (Sonnet integrates, does not re-adjudicate).

_Dr. Mārcis Gasūns_
