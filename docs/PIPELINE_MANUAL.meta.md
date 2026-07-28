# PIPELINE_MANUAL.md — metadoc

_Created: 28-07-2026 · Last updated: 28-07-2026_

Companion record for
[docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/MWS/blob/master/docs/PIPELINE_MANUAL.md)
— purpose, provenance, improvement backlog and revision history of the manual
itself (not of the pipelines it documents).

## Purpose

Give a new operator one document from which to run every live MW pipeline —
the universal correction loop against `csl-orig`, link-target and citation
tooling, the 2026 zero-argument analysis modules, the extractor chains, the
preface regenerator — without hunting through ~25 scattered folder-local
readmes, two colliding path conventions, and a Python-2/3 split. Equally: to
state plainly which workspaces are frozen history and must not be re-run.

## Audience

- **Operators** — the cheat-sheet, the workspace map, walkthroughs 1–6, and
  the symptom table.
- **Maintainers** — the invariants and the known-traps list in the appendix;
  the backlog below.
- **Historians** — the What-not-to-re-run section and the frozen-workspace
  rows of the map, which record *why* each dead pipeline died.

## Provenance

- Authored 28-07-2026 by Fable 5 (`claude-fable-5`) under handoff
  [H1786](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1786-Fable_MWS_correction-pipeline-tooling-manual_28.07.26.md)
  (the H1782–H1786 medium docs-debt batch, minted by Grok 4.5 `grok-4.5`).
- Modelled on the gold-standard operator manual
  [RussianRamayana Litpam-Indexator MANUAL.md](https://github.com/gasyoun/RussianRamayana/blob/main/Litpam-Indexator/docs/indesign-pipeline/MANUAL.md)
  and its census-batch siblings
  [PWK PIPELINE_MANUAL](https://github.com/sanskrit-lexicon/PWK/blob/main/docs/PIPELINE_MANUAL.md)
  (H530) and
  [AP90 PIPELINE_MANUAL](https://github.com/sanskrit-lexicon/AP90/blob/master/docs/PIPELINE_MANUAL.md)
  (H523).
- Source material: a same-day survey by three parallel read-only Explore
  agents over every workspace directory (readmes, entry-point scripts,
  `redo.sh` drivers, git recency), plus a fourth agent over the papers/ops
  boundary, branches, and changelog. Input paths were verified against the
  flat `GitHub/` sibling layout on this machine; sibling repos `csl-orig`,
  `csl-pywork`, `csl-devanagari`, `VisualDCS`, `WhitneyRoots` and the 16
  dictionary repos confirmed present.
- Doc-vs-code discrepancies found during the survey were corrected in the
  manual rather than propagated: the stale `../../../cologne/…` paths in the
  `botbio`/`Lithuanian`/`mwverbs` readmes, the `redo.sh`-vs-readme path
  disagreement in `mwverbs/`, the `issue_632.py` filename transposition, the
  `place_greek_text.py` docstring advertising a nonexistent output, and the
  `$BASE`-only-in-prose fiction.
- Pipelines were not re-executed for authorship; commands are
  transcription-verified against the scripts, and disk facts (paths, file
  presence, BOMs, py2 rosters) were checked 28-07-2026.

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Extend the [README.md](https://github.com/sanskrit-lexicon/MWS/blob/master/README.md) Contents table with the ten missing 2026-era directories (trap #1 in the manual's appendix) | open |
| 2 | Fix the stale `../../../cologne/…` input paths in [botbio/readme.md](https://github.com/sanskrit-lexicon/MWS/blob/master/botbio/readme.md), [Lithuanian/readme.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/Lithuanian/readme.txt), [mwverbs/redo.sh](https://github.com/sanskrit-lexicon/MWS/blob/master/mwverbs/redo.sh) + readme, and [CLAUDE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CLAUDE.md)'s auxiliary-commands section, or add a one-line flat-layout note beside each | open |
| 3 | Re-enable (behind a flag) the commented-out `extract_greek(...)` refresh in [greek_andhrabharati/place_greek_text.py](https://github.com/sanskrit-lexicon/MWS/blob/master/greek_andhrabharati/place_greek_text.py) and fix its docstring | open |
| 4 | Rename `CORRECTIONS_issue_362/issue_632.py` → `issue_362.py` (with a readme note) to kill the digit transposition | open |
| 5 | Mark the Python-2-only scripts as frozen in their own readmes (`homophone/`, `mwabbreviations/`, `k1k2/`, `mwauthorities/tooltip.py`) so a newcomer doesn't debug them | open |
| 6 | Remove the stray `README.md~` and rule on `missing1.html` (VCP data misfiled into MWS — move to the VCP repo or delete) | open |

## Known limitations

- Commands are transcription-verified, not live-re-executed; a future
  `csl-orig`/`csl-pywork` restructuring could silently invalidate the
  validation-loop section.
- The manual freezes counts as of 28-07-2026 (286,560 records, 877 sigla,
  2,369 phw edges, 31.4% DCS attestation); these drift with the data.
- The XAMPP-era layout is documented only as a trap, not operationally — an
  operator actually running Jim's original layout gets no help beyond the
  path-translation rule.
- Web-sample walkthroughs depend on the live Cologne `apidev` surface, which
  this repo does not control.

## Intended use / known misuse

- **Intended use:** operating and re-running MW tooling; deciding whether a
  workspace is live before touching it; diagnosing the standard failure
  modes.
- **Known misuse:** re-running the frozen campaigns (`homophone/` most of
  all — its output is already applied upstream); agent-filling the Review
  Packets (H966 kill-gate); editing the consolidated preface files by hand;
  committing directly to `csl-orig`; branching docs work from `docs-pass`.

## Maintenance & sunset plan

- **Trigger for re-verification:** any change to the correction workflow in
  [csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md),
  a new re-runnable workspace landing in MWS, or a `csl-pywork` build-script
  rename.
- **Owner:** repo maintainers; agent sessions bump "Last updated" and the
  revision history when they touch it.
- **Staleness signal:** a symptom-table cure that no longer works, or a map
  row whose Status contradicts `git log` recency.
- **Sunset condition:** superseded by an org-wide cross-dictionary operator
  manual, should one ever absorb the per-repo manuals.

## Deprecation status

`active`

## Related documents

- [docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/MWS/blob/master/docs/PIPELINE_MANUAL.md) — the subject of this metadoc.
- [CONTRIBUTING.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CONTRIBUTING.md) — contributor-facing correction workflow the manual builds on.
- [ANALYSIS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ANALYSIS.md) — the five 2026 analysis modules the manual's walkthrough 3 operates.
- [csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) — the canonical cross-dictionary correction doctrine.
- [PWK PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/PWK/blob/main/docs/PIPELINE_MANUAL.md) · [AP90 PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/AP90/blob/master/docs/PIPELINE_MANUAL.md) — sibling manuals of the same house shape.

## Revision history

| Date | Change | By |
|---|---|---|
| 28-07-2026 | Initial authoring (H1786) | Fable 5 (`claude-fable-5`) |

_Dr. Mārcis Gasūns_
