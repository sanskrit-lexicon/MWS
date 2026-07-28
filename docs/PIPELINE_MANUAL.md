# MWS pipelines — operator manual

_Created: 28-07-2026 · Last updated: 28-07-2026_

How to operate the Monier-Williams (MW) correction and extraction tooling in this
repository: the universal correction loop against
[csl-orig](https://github.com/sanskrit-lexicon/csl-orig)'s
[mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt),
the link-target machinery, the 2026 zero-argument analysis modules, and every
extractor that is still re-runnable — plus an explicit list of what is frozen and
must not be re-run. Scope is **tooling operations only**: the papers under
[papers/](https://github.com/sanskrit-lexicon/MWS/tree/master/papers) and the
specs under
[planning/](https://github.com/sanskrit-lexicon/MWS/tree/master/planning) carry
their own passports and are out of scope here (see
[Pipeline ops vs papers](#pipeline-ops-vs-papers--the-boundary)).

The documents describing this repo, with different jobs:

- [README.md](https://github.com/sanskrit-lexicon/MWS/blob/master/README.md) — directory inventory, history, issue taxonomy, contributors.
- [CLAUDE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CLAUDE.md) — the agent-facing command contract (data format, common commands).
- [CONTRIBUTING.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CONTRIBUTING.md) — the correction workflow in contributor terms, including the in-file correction-record format.
- [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DATA_DICTIONARY.md) — tag and field reference for `mw.txt`.
- [ENTRY_GUIDE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ENTRY_GUIDE.md) — how to read an MW entry.
- [DICT_PROFILE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DICT_PROFILE.md) — the dictionary itself: editions, history, when to use.
- [ANALYSIS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ANALYSIS.md) — index of the five read-only 2026 analysis modules.
- [ROADMAP.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ROADMAP.md) — the 2026 H2 plan (workstreams W1–W4, model-tier policy).
- **This manual** — how to actually run things, what breaks, and what is frozen.

**Verification provenance.** Authored 28-07-2026 by Fable 5 (`claude-fable-5`)
under handoff
[H1786](https://github.com/gasyoun/Uprava/blob/main/handoffs/H1786-Fable_MWS_correction-pipeline-tooling-manual_28.07.26.md),
from a same-day survey of every workspace by three parallel read-only agents:
commands are quoted from the workspace readmes and the scripts themselves, and
every input path was checked against this machine's flat `GitHub/` layout.
Pipelines were **not** re-executed for this manual — the 2026 analysis modules
are cheap to re-run at will, while correction campaigns operate on live
`csl-orig` data and are never run casually. Where a readme's command line no
longer works as written, this manual gives the corrected form and says so.

## Cheat-sheet: the universal correction loop

Every MW text correction, whatever its origin, moves through the same loop.
Run from a working directory inside this repo (an `mwsissues/issueNNN/` dir or
a scratch dir); `../../csl-orig` is the sibling checkout.

```sh
# 0. Seed a working copy (two sanctioned ways; temp_* files are gitignored)
cp ../../csl-orig/v02/mw/mw.txt temp_mw_0.txt                        # live copy
git -C ../../csl-orig show <commit>:v02/mw/mw.txt > temp_mw_0.txt    # pinned copy

# 1. Produce temp_mw_1.txt — by a correction script, by updateByLine.py,
#    or by a hand edit. One temp_mw_N.txt per round, N = 1, 2, ...

# 2. Turn the edit into an auditable change file
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt

# 3. Prove the change file is complete by re-applying it mechanically
python updateByLine.py temp_mw_0.txt change_mw_1.txt temp_mw_1_check.txt
diff temp_mw_1.txt temp_mw_1_check.txt        # must be empty

# 4. Validate the XML build (csl-pywork sibling; N = current round)
cp temp_mw_N.txt ../../csl-orig/v02/mw/mw.txt
cd ../../csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

# 5. Park the correction in the monthly queue — NEVER push csl-orig yourself.
#    /cologne-correction-queue → csl-corrections/batch_pending/dictionaries/mw/
# 6. Roughly monthly, everything ships as ONE consolidated PR: /cologne-batch-pr
```

The change file is the deliverable; the `temp_mw_N.txt` outputs are disposable
(and gitignored — see [Invariants](#invariants)). Its format, applied by
`updateByLine.py <in.txt> <changes.txt> <out.txt>`:

```
; comment lines start with a semicolon
1582 old <s>akza</s> ¦ [the exact current text of line 1582]
1582 new <s>akza</s> ¦ [the corrected text]
2077 ins <a line to insert AFTER line 2077>
3105 del 
```

Line numbers are 1-based **absolute positions in the input file**; `ins`
inserts after the numbered line; `del` ignores its text part but a space must
follow the keyword. The change file must be UTF-8. On any `old`-text mismatch
the tool hard-fails with `exit(1)` — that strictness is the safety property
that makes change files auditable, not a bug. Producers:
`diff_to_changes_dict.py old.txt new.txt changes.txt` (requires **equal line
counts**; emits `; <L>…` metalines so each change is attributable to a record)
and the metaline-less `diff_to_changes.py`. Canonical copies of all three
travel with the issue dirs (e.g.
[mwsissues/issue182/updateByLine.py](https://github.com/sanskrit-lexicon/MWS/blob/master/mwsissues/issue182/updateByLine.py),
[mwsissues/issue188/diff_to_changes_dict.py](https://github.com/sanskrit-lexicon/MWS/blob/master/mwsissues/issue188/diff_to_changes_dict.py));
a generic applier also lives at
[mwtranscode/revdoc/updateByLine.py](https://github.com/sanskrit-lexicon/MWS/blob/master/mwtranscode/revdoc/updateByLine.py).

## Map of the workspaces

Status vocabulary: **Live** = current, run at will; **Re-runnable** = works
today, possibly after the noted path fix; **Frozen** = one-shot history, do not
re-run (see [What not to re-run](#what-not-to-re-run)).

| Workspace | What it is | Status |
|---|---|---|
| [phw_graph/](https://github.com/sanskrit-lexicon/MWS/tree/master/phw_graph) | Phrasal-headword graph audit (2,369 edges) | **Live**, zero-arg |
| [botanical_glossary/](https://github.com/sanskrit-lexicon/MWS/tree/master/botanical_glossary) | FAIR Sanskrit↔Linnaean dataset from 8,923 `<bot>` tags | **Live**, zero-arg |
| [lexicographer_dcs/](https://github.com/sanskrit-lexicon/MWS/tree/master/lexicographer_dcs) | DCS attestation of `<ls>L.</ls>` hedges (31.4%) | **Live**, zero-arg |
| [mw_integrity/](https://github.com/sanskrit-lexicon/MWS/tree/master/mw_integrity) | Structural check of `mw.txt` (286,560 records) | **Live**, zero-arg |
| [relative_refs/](https://github.com/sanskrit-lexicon/MWS/tree/master/relative_refs) | `ib.` citation resolution (10,094 refs) | **Live**, zero-arg |
| [root_crosswalk/](https://github.com/sanskrit-lexicon/MWS/tree/master/root_crosswalk) | MW ↔ Whitney ↔ DCS verbal-root crosswalk | **Live** (needs sibling `WhitneyRoots`) |
| [mwauthorities/link_candidates/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities/link_candidates) | Unlinked-siglum candidate generator (340 candidates) | **Live**, zero-arg |
| [review_packets/](https://github.com/sanskrit-lexicon/MWS/tree/master/review_packets) | Human review-sheet generator (Packets A/B/C + G5) | **Live** generator; packets are human-only (H966) |
| [prefaces/](https://github.com/sanskrit-lexicon/MWS/tree/master/prefaces) | 1899 front-matter OCR + RU translation | **Live** regenerator |
| [mwsissues/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwsissues) | Per-issue correction campaigns (issue65–issue190) | **Live pattern** — the method is current; past campaigns are not replayable |
| [mwissues/markup_fix/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwissues/markup_fix) | Agent-era markup fixer emitting `updateByLine` change files | **Live** |
| [basic04a/](https://github.com/sanskrit-lexicon/MWS/tree/master/basic04a) · [list02php/](https://github.com/sanskrit-lexicon/MWS/tree/master/list02php) | Web display samples against the live Cologne API | **Live** demos |
| [mwtranscode/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwtranscode) | SLP1 ↔ IAST ↔ Devanagari transcoding | **Re-runnable**, self-contained |
| [botbio/](https://github.com/sanskrit-lexicon/MWS/tree/master/botbio) | `<bot>`/`<bio>` tag extraction | **Re-runnable** (readme path is stale) |
| [mwverbs/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwverbs) → [verbs01/](https://github.com/sanskrit-lexicon/MWS/tree/master/verbs01) | Verb extraction → 16-dictionary verb matrix | **Re-runnable** chain (path fixes) |
| [Lithuanian/](https://github.com/sanskrit-lexicon/MWS/tree/master/Lithuanian) | Lithuanian etymology extraction + pre-staged change file | **Re-runnable** (path fix) |
| [mwsupplement/freshlook/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwsupplement/freshlook) | Supplement-entry family classifier | **Re-runnable** (copy `mw.txt` in first) |
| [greek_andhrabharati/](https://github.com/sanskrit-lexicon/MWS/tree/master/greek_andhrabharati) | Greek-text diff vs Andhrabharati's list | **Partially re-runnable** (one step commented out) |
| [accent_diff/](https://github.com/sanskrit-lexicon/MWS/tree/master/accent_diff) | `<k2>` accent diff MW vs PWG | **Re-runnable** after path fix (needs `pwg.txt` too) |
| [CORRECTIONS_issue_362/](https://github.com/sanskrit-lexicon/MWS/tree/master/CORRECTIONS_issue_362) | Language-tag reconciliation vs Andhrabharati | **Converged** — re-runnable in principle, goal is a blank `log.txt` |
| [mwauthorities/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) (legacy: `tooltip.py`, `ls/`) | Authority records + `<ls>` link campaigns | **Frozen** (Python 2; campaigns archived) |
| [mwabbreviations/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwabbreviations) | Abbreviation reconciliation (2017) | **Frozen** (Python 2 + missing `mw.xml`) |
| [homophone/](https://github.com/sanskrit-lexicon/MWS/tree/master/homophone) | Scharf/Goyal homophone markup extension (2013–2015) | **Frozen** — applied to Cologne in 2015 |
| [transcodeExample/](https://github.com/sanskrit-lexicon/MWS/tree/master/transcodeExample) | 2014 PHP transcoder worked example | **Frozen** (needs `mw.xml` build product) |
| [k1k2/](https://github.com/sanskrit-lexicon/MWS/tree/master/k1k2) | 2015 key1/key2 clash analysis | **Frozen** — dead code (Python 2 + lxml + vanished input path) |
| [history/](https://github.com/sanskrit-lexicon/MWS/tree/master/history) | Malten's 2004 `MONIER.ALL` archive | **Frozen archive**; the cp1252→UTF-8 conversion is reproducible |

## Environment and prerequisites

**Layout — the single biggest trap in this repo.** Two path conventions
collide:

1. **Legacy (2015–2022):**
   [CLAUDE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CLAUDE.md) and
   [CONTRIBUTING.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CONTRIBUTING.md)
   document a Cologne/XAMPP layout (`$BASE/sanskrit-lexicon/MWS` +
   `$BASE/cologne/csl-orig`, `$BASE=/c/xampp/htdocs`), and the older readmes
   write input paths like `../../../cologne/csl-orig/v02/mw/mw.txt`. Note
   `$BASE` appears **only in prose** — the era's scripts (e.g.
   `mwsissues/issue182/redo_mw.sh`) hardcode `/c/xampp/htdocs` outright.
2. **Modern (2026):** a flat checkout where `csl-orig`, `csl-pywork`,
   `csl-devanagari`, `VisualDCS`, `WhitneyRoots` and the 16 dictionary repos
   are **siblings of MWS** under one parent directory. The 2026 scripts
   compute the repo's own location and resolve
   `<parent>/csl-orig/v02/mw/mw.txt` with zero arguments.

On a flat checkout every legacy command must have its input path rewritten to
`../../csl-orig/v02/mw/mw.txt` (from a first-level subdirectory of MWS) or an
absolute path. This manual quotes the **corrected** forms and flags each
disagreement with the local readme.

- **Python:** everything from 2020 onward is Python 3 (or 2/3-dual via
  `from __future__ import print_function`). Thirteen files are still
  Python-2-only and crash on `python3`: all of `homophone/pywork/` (5 scripts +
  the 3 in `pykeysxml/`), `homophone/updlogs/prep1.py`,
  `mwauthorities/tooltip.py`, `mwabbreviations/work/filter_simple.py`,
  `mwabbreviations/work/compare.py`, `k1k2/clash.py`.
- **Java** only for the frozen 2013 homophone originals; **PHP** only for
  `transcodeExample/` (CLI) and `list02php/` (needs a web server, e.g. XAMPP).
- **Validation** needs the sibling
  [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork)
  (`v02/generate_dict.sh`, `v02/xmlchk_xampp.sh`).
- **Encoding:** everything UTF-8; `mw.txt` carries **no BOM** (asserted by
  `mw_integrity`). On Windows consoles, modern scripts use
  `sys.stdout.reconfigure(encoding='utf-8')`.
- **Default branch is `master`**, not `main` — PRs must target it, and blob
  URLs into this repo carry `/blob/master/`.

## Delivery — the batched-PR rule (read before installing anything)

Agents **never commit or push directly to
[csl-orig](https://github.com/sanskrit-lexicon/csl-orig)** and generate no PR
noise there. A validated correction is parked with
[/cologne-correction-queue](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-correction-queue.md)
into `csl-corrections/batch_pending/dictionaries/mw/`, and roughly monthly the
whole queue ships as **one** consolidated PR via
[/cologne-batch-pr](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-batch-pr.md).
The canonical workflow doctrine is
[csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) —
this manual does not restate it. Two MW-specific notes:

- Historically, MW change files are also mirrored into
  [csl-corrections/dictionaries/mw/mw_printchange.txt](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/dictionaries/mw/mw_printchange.txt)
  (see the
  [issue182 readme](https://github.com/sanskrit-lexicon/MWS/blob/master/mwsissues/issue182/readme.txt)).
- Corrections land inside `mw.txt` as in-file records of the form
  `{{old -> new || YYYY-MM-DD | author | URL |}}` — machine-processed by the
  `updateByLine.py` toolchain, **never edited by hand**
  ([CONTRIBUTING.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CONTRIBUTING.md)).

## Walkthrough 1 — a classic text correction (mwsissues/issueNNN/)

The 34 `issueNNN/` dirs under
[mwsissues/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwsissues) are
the campaign archive; each holds the scripts, the `change_*.txt` transaction
logs, and `readme.txt`/`readme2.txt`/… narratives recording every step and the
case-by-case rationale. The `temp_mw_N.txt` working files are gitignored
(`temp*`), so a past campaign **cannot be re-executed from this repo alone** —
its pinned inputs are recoverable only from `csl-orig` history via the commit
hashes in its readme. What you reuse is the *method* (the cheat-sheet loop) and
the reference campaigns:

- **[issue188](https://github.com/sanskrit-lexicon/MWS/tree/master/mwsissues/issue188)**
  (VIKRAMORVAŚĪ link targets) — the cleanest end-to-end example: seed →
  `make_js_index.py` → sample-check with `generate_random.py` → hand edit →
  validate → `diff_to_changes_dict.py` (20 changes). Its readme also carries
  the canonical **xmlchk-error recovery recipe**: open the `csl-pywork`-built
  `mw.xml` in Emacs and jump to the reported line (`C-c C-n`).
- **[issue182](https://github.com/sanskrit-lexicon/MWS/tree/master/mwsissues/issue182)**
  (Bhāgavata-Purāṇa links) — the best-documented multi-round campaign
  (4 rounds, including a temporary reformat in round 1 that round 3 undoes);
  wraps the validation loop in `redo_mw.sh` (`sh redo_mw.sh N` — beware: it
  hardcodes `/c/xampp/htdocs` and `cd`s away without returning).
- **[issue190](https://github.com/sanskrit-lexicon/MWS/tree/master/mwsissues/issue190)**
  (lost headwords) — the archaeology pattern: `comphw*.py` headword compares
  between a current and a historic `mw.txt`, narrowing 194k headwords to 16
  written-up cases.
- **[abcleanup](https://github.com/sanskrit-lexicon/MWS/tree/master/mwsissues/abcleanup)**
  — the *iterative accumulation* idiom: keep the input fixed, append
  transactions to one growing change file, re-run
  `python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt` after each
  step. The change file is the single source of truth.

The modern bridge between this 2014 contract and the 2026 layout is
[mwissues/markup_fix/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwissues/markup_fix):
`python 08_markup_fix.py` (falls back to the sibling
`csl-orig/v02/mw/mw.txt`), then `python test_markup_fix.py` (7 tests); it
emits `markup_fix_changes.txt` in exact `updateByLine` format. Note the
easily-confused names: `mwsissues/` is the legacy campaign archive,
`mwissues/` is the 2026 agent-era drop.

## Walkthrough 2 — link-target and citation tooling (mwauthorities/)

MW-specific link-target work lives in
[mwauthorities/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities)
(the cross-dictionary aggregate view is csl-atlas's, not this repo's). The
data model
([readme.md](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/readme.md)):
the Sanskrit Library's `MWWorksAuthorsCurrentMarkup3.xml` authority file
(Scharf/Hyman, ~2010), the derived `mwauthorities_init.txt`, the
`linkmwauthorities_init.txt` link table (`<ls>` siglum → authority record),
and the `mwauth.txt` amalgam.

- **Re-runnable today:**
  [link_candidates/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities/link_candidates)
  — `python link_candidates.py` (zero-arg) regenerates
  `link_candidates.csv` + `LINK_CANDIDATES_SUMMARY.md`: 877 distinct live
  `<ls>` sigla, 537 linked, 340 unlinked candidates. It is a review-candidate
  generator only — it **touches no authority file**; acceptance into
  `linkmwauthorities_init.txt` is manual.
- **Frozen legacy:** the `ls/` campaign dirs
  ([20211005-panini](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities/ls/20211005-panini)
  is the reference pattern for a new campaign; also `20220628-rv`, `issue131`,
  `issue134`, `issue135`, `issue136`), and `tooltip.py`
  (`python tooltip.py roman mwauth.txt tooltip.txt`) — Python 2, and it
  imports `transcoder` from the repo root where no `transcoder.py` exists;
  copy `mwtranscode/transcoder.py` up (or fix the path) before any revival.
- **Adjacent citation resolution:**
  [relative_refs/](https://github.com/sanskrit-lexicon/MWS/tree/master/relative_refs)
  — `python ib_resolve.py` resolves the 10,094 `<ls>ib.</ls>` citations to
  candidate antecedents (`ib_resolved.csv`, `IB_SUMMARY.md`). Results are
  "resolvable, not verified"; verification is Packet A in `review_packets/`.
- **New scan-link campaigns** (Suśr./Kathās./ŚBr.) are specced in
  [SPEC-1](https://github.com/sanskrit-lexicon/MWS/blob/master/planning/specs/2026-07/SPEC-1-w1c-scanlink.md)
  but **blocked on an edition-identification `@DECIDE`**
  ([MWS#234](https://github.com/sanskrit-lexicon/MWS/issues/234)) — do not
  start one until that is ruled.

## Walkthrough 3 — the 2026 analysis modules (zero-arg, read-only)

Five self-contained modules, indexed in
[ANALYSIS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ANALYSIS.md),
all Python 3, all resolving their inputs relative to the repo location, none of
them ever mutating `mw.txt`. Run each from inside its own directory:

| Command | Output | External input |
|---|---|---|
| `python phw_audit.py` | `phw_edges.csv`, `phw_integrity.csv`, `PHW_SUMMARY.md` | sibling `csl-orig` |
| `python bot_glossary.py` then `python gbif_currency.py` | `mw_botanical_glossary.csv`, `species_to_sanskrit.json`, `species_currency.csv`, summaries | sibling `csl-orig` + `VisualDCS`; GBIF API on first currency run (cached in `species_currency_cache.json`) |
| `python ls_L_dcs_pilot.py` then `python ls_L_dcs2026.py` | attested/unattested CSVs, `SUMMARY.md`, `SUMMARY_2026.md` | sibling `csl-orig` + `VisualDCS` (2021 JSON, 2026 sqlite); the 2026 script reloads the pilot's CSVs — run the pilot first |
| `python mw_integrity.py` | `INTEGRITY_REPORT.md`, `integrity_issues.csv` | sibling `csl-orig` |
| `python ib_resolve.py` | `ib_resolved.csv`, `IB_SUMMARY.md` | sibling `csl-orig` |
| `python root_crosswalk.py`; `python class_concordance.py` | `root_crosswalk.csv`, `class_concordance.csv`, summaries | sibling `WhitneyRoots` (imports its `root_triangulation.py`) + its DCS frequency data |

Current integrity state (28-07-2026): 286,560 records, **one** open flag
(L27713.2 carries two trailing spaces after `<e>2` — a pending
maintainer-gated one-line fix).

[review_packets/](https://github.com/sanskrit-lexicon/MWS/tree/master/review_packets)
belongs operationally with these: `python build_packets.py` regenerates
Packets A (ib. resolutions), B (band-3 `L.`→DCS) and C (class conflicts) from
sibling `csl-orig` + `VisualDCS`. **The packets themselves are human-only**:
the kill-gate ruling
[H966_KILL_GATE_FINDING.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/H966_KILL_GATE_FINDING.md)
(18-07-2026) establishes that every verdict is a genuine philological
judgement — do not attempt to auto-fill them. The `g5/` subdir is a separate,
**completed** gold-sample pipeline; leave it alone.

## Walkthrough 4 — the extractor pipelines

All commands below are the **path-corrected** forms for the flat layout, run
from inside each workspace.

**botbio** — unique `<bot>`/`<bio>` values with frequencies (superseded for
botany by `botanical_glossary/`, still the quick raw extraction):

```sh
python tagunique.py bot ../../csl-orig/v02/mw/mw.txt mw_bot.txt
python tagunique.py bio ../../csl-orig/v02/mw/mw.txt mw_bio.txt
```

(The readme's `../../../cologne/…` form fails on a flat checkout. The script
`exit(1)`s on duplicate `<L>` numbers — that is a data alarm, not a crash.)

**mwverbs → verbs01** — verb extraction, then the 16-dictionary verb matrix.
Strictly sequential; do not skip step 3 (downstream `verbs01` parses
`mwverbs2.txt`'s field conventions, not `mwverbs1.txt`'s):

```sh
# in mwverbs/   (redo.sh says ../../../, its readme says ../../../../ — both stale)
python mwverb.py mw ../../csl-orig/v02/mw/mw.txt mwverbs.txt
python mwverbs1.py mwverbs.txt mwverbs1.txt
python mwverbs2.py mwverbs1.txt mwverbs2.txt
# in verbs01/  — see redo.sh for the four verbs1_merge.py variants
```

`verbs01/redo.sh` needs **16 sibling dictionary repos** (list hardcoded at
`verbs1_merge.py:105–123`, with three irregular paths: `pw` → `PWK/verbs01/`,
`pwg` → `PWG/verbs01a/`, `yat`/`shs` → `WIL/verbs01-yat/`, `WIL/verbs01-shs/`)
and copies its HTML outputs into the sibling `sanskrit-lexicon.github.io`
checkout. The HTML matrices are the useful output; the readme records the
markdown variant as a failed experiment.

**Lithuanian** — extracts every etymology line citing Lithuanian and
pre-stages a correction file:

```sh
python filter.py mw ../../csl-orig/v02/mw/mw.txt filter.txt manualByLine.txt
```

`manualByLine.txt` — the one "manual" hit a docs scan finds in this repo — is
a **pre-staged `updateByLine` change file**: for each of the 211 cases it
writes the absolute `mw.txt` line number with the current text as `old` and an
initially *identical* `new` line, which a human then edits by hand (hence the
name); apply with the generic
`mwtranscode/revdoc/updateByLine.py`. Its embedded line numbers are valid
**only** against the exact `mw.txt` revision that generated it — regenerate,
never hand-carry, after any upstream change.

**mwsupplement/freshlook** — supplement-entry family classifier. The scripts
read `../mw.txt`, i.e. a copy **inside** `mwsupplement/` that is not in git —
copy it in first:

```sh
cp ../../csl-orig/v02/mw/mw.txt ../mw.txt
python changes.py   0 ../mw.txt changes_0.txt     # filter ∈ {0,1,2,3,4,8,9}
python additions.py 0 ../mw.txt additions_0.txt   # filter ∈ {0,1,2}
```

**greek_andhrabharati** — `python place_greek_text.py` (zero-arg; its
hardcoded flat-layout path is already correct). Two traps: the Cologne-side
extraction `extract_greek(...)` is **commented out** in `__main__`, so the
diff reuses the committed 2021 `log_greek.txt` unless you uncomment it; and
the module docstring advertises an `mw1.txt` "placer" output that does not
exist — it is an extract-and-diff tool only.

**mwtranscode** — self-contained (ships its own pinned `mw.txt`, synced to a
January-2021 `csl-orig` commit recorded in its readme — re-sync before
trusting a diff against current data):

```sh
python mw_transcode.py slp1 roman mw.txt mw_iast.txt
python mw_transcode.py slp1 deva  mw.txt mw_deva.txt
# invertibility proofs
python mw_transcode.py roman slp1 mw_iast.txt temp_mw_slp1.txt && diff mw.txt temp_mw_slp1.txt
python mw_transcode.py deva  slp1 mw_deva.txt temp_mw_slp1.txt && diff mw.txt temp_mw_slp1.txt
```

Which rule set is used is **baked into the driver**, not a flag:
`mw_transcode.py` uses `transcoder/`, while `mw_transcode1.py`/
`mw_transcode2.py` use the accent-revised `transcoder1/` (2022). Exactly three
words are non-invertible on the SLP1→IAST→SLP1 round trip (documented in
[mwtranscode/readme.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwtranscode/readme.txt);
the driver patches them); SLP1↔Devanagari is fully invertible. The `revdoc/`
and `web/` subdirs are the frozen 2022 Andhrabharati IAST-review cycle — read,
don't re-run.

**accent_diff** — `python3 find_accent_diff.py mw pwg log.tsv log.html`; fix
its `../../../cologne/…` input path first, and note it needs **both** `mw.txt`
and `pwg.txt` from `csl-orig`.

**CORRECTIONS_issue_362** — `python issue_632.py` (yes: the directory says
362, the script says 632). Reads the sibling **`csl-devanagari`** copy of
`mw.txt`, not `csl-orig`. The committed `log.txt` is the residual-difference
list; "ultimate goal is to have log.txt blank." The `ab_lang.tsv` input and
its source `.xlsx` are declared immutable.

## Walkthrough 5 — prefaces (regenerate path)

The 29 front-matter pages (EN + RU) under
[prefaces/](https://github.com/sanskrit-lexicon/MWS/tree/master/prefaces) are
finished OCR, but the **consolidated editions are build products** and are
never hand-edited. After editing any per-page `mwprefNN.md`/`mwprefNN.ru.md`,
rebuild both consolidated files in one run:

```sh
DICT=mw python build_combined.py    # → mwpref_all.en.md + mwpref_all.ru.md
```

The script globs the page files and reads their YAML front matter, so there is
no page list to maintain. Russian register questions are governed by
[prefaces/RU_STYLE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/prefaces/RU_STYLE.md)
(the H1763 ruling set, intended as the house register for other dictionaries'
RU prefaces too). In-body headings must be `##`, not `#` — the builder's
sanity count depends on it. The `mwepref01–11.md` pages belong to the *1851
English–Sanskrit* dictionary, a different work — don't mix them into MW-1899
edits.

## Walkthrough 6 — web display samples

- **[basic04a/](https://github.com/sanskrit-lexicon/MWS/tree/master/basic04a)**
  — open `index.html` directly in a browser; pure HTML/JS against the live
  Cologne `apidev` endpoints (network and Cologne uptime required; `apidev`
  is a development endpoint and may move).
- **[list02php/](https://github.com/sanskrit-lexicon/MWS/tree/master/list02php)**
  — PHP: serve the directory from a web server (e.g. XAMPP `htdocs`) and
  browse `index.php`; opening it from the filesystem does nothing. Security
  invariant: every `$_GET` reflection into JS must go through
  `json_encode` — a reflected-XSS of exactly this class was already patched
  here (csl-corrections #210). Both samples were dependency-hardened in
  July 2026 (jQuery 3.7.1, js-cookie).

## What not to re-run

- **[homophone/](https://github.com/sanskrit-lexicon/MWS/tree/master/homophone)**
  — the 2015 campaign (~6,555 removeHom changes + 10,913 artificial
  homophones) is **already applied** to Cologne's data. It is also doubly
  blocked: Python-2-only, and its input `monier.xml` is a `csl-pywork` build
  product absent from a flat checkout. The
  [readme.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/homophone/readme.txt)
  documents the sequence for the record; treat it as history. The Java
  originals additionally ignore argv and hardcode a nonexistent
  `accent_logs/` directory.
- **[mwabbreviations/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwabbreviations)**
  — Python 2 + a vanished `pywork/mw.xml` input. The authoritative
  abbreviation list is `csl-pywork`'s `mwab_input.txt`, not the working copy
  here.
- **[transcodeExample/](https://github.com/sanskrit-lexicon/MWS/tree/master/transcodeExample)**
  and **[k1k2/](https://github.com/sanskrit-lexicon/MWS/tree/master/k1k2)** —
  2014/2015 one-shots against the old `mw.xml`; `k1k2/clash.py` is dead code
  (Python 2, lxml, vanished input path, and an unpacking bug).
- **Past `mwsissues/` campaigns** — the method is live, the campaigns are
  history; their `temp_mw_N.txt` inputs are gitignored and recoverable only
  from `csl-orig` history.
- **The `mwtranscode/` AB_3.x review cycle** (`revdoc/`, `web/`) — a
  completed 2022 review dialogue; the status files record what was DONE.
- **[history/](https://github.com/sanskrit-lexicon/MWS/tree/master/history)**
  — an archive. The only thing to ever re-run is the conversion one-liner
  (`unzip MONIER.ALL.zip` then
  `python cp1252-to-utf8.py MONIER.ALL mw_orig_utf8.txt`).
- **Review Packets A/B/C** — regenerating the *sheets* is fine; **filling
  them is not agent work** (H966 kill-gate).
- **Top-level frozen data drops** (`6602-entries-from-supplements-MW.txt`,
  `hiatus-190-entries.txt`, `key2-avagraha-225-entries.txt`,
  `key2-space-61-entries.txt`, `step1a-191-unique-entries.txt`,
  `mw_genuine_roots.txt`) — 2014-era dumps with no generating script
  committed; several are in the pre-`<L>` XML dialect. Reference data, not
  pipelines.

## Pipeline ops vs papers — the boundary

Everything under
[papers/](https://github.com/sanskrit-lexicon/MWS/tree/master/papers),
[planning/](https://github.com/sanskrit-lexicon/MWS/tree/master/planning) and
the human-vote halves of `review_packets/` is **not** operated from this
manual. The papers carry their own passports —
[papers/microanalysis/README.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/README.md)
(A16/A17),
[papers/p3_citation_registers/SYNTHESIS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/p3_citation_registers/SYNTHESIS.md)
(A18) plus per-module readmes, and the top-level paper drafts (A39, A45, A46)
next to their own signoff/citation files — and their revision state is
human-gated (author-pass signoffs, `@DO` rows). Monthly execution specs live
in
[planning/specs/2026-07/](https://github.com/sanskrit-lexicon/MWS/tree/master/planning/specs/2026-07).
One git-level hazard: the long-lived `docs-pass` branch (issue
[#195](https://github.com/sanskrit-lexicon/MWS/issues/195)) **contains paper
commits**, so it is not a pure docs branch — operator/docs PRs branch from
`master`, never from `docs-pass`, and never mix paper-tree edits into a
tooling PR.

## Symptom → cause → cure

| Symptom | Cause | Cure |
|---|---|---|
| `updateByLine.py` exits with a CHANGE-ERROR "old" mismatch | Change-file line numbers are absolute; the input is a different `mw.txt` revision than the one the file was generated against | Regenerate the change file against the current input (`diff_to_changes_dict.py`); never hand-carry line numbers. The hard-fail is intentional |
| `diff_to_changes_dict.py` refuses to run | The two files have unequal line counts — it cannot express insertions/deletions | Hand-write the `ins`/`del` records, or use a same-line-count intermediate |
| A documented command fails with "No such file: `../../../cologne/...`" | Legacy XAMPP-era path convention; that tree doesn't exist on a flat checkout | Rewrite the input path to `../../csl-orig/v02/mw/...` (see [Environment](#environment-and-prerequisites)) |
| `SyntaxError` on `print` when running an older script | One of the 13 Python-2-only files | Run under Python 2 or port first; the roster is in [Environment](#environment-and-prerequisites) |
| `homophone/` or `transcodeExample/` wants `monier.xml` / `mw.xml` | Those are `csl-pywork` **build products**, not committed sources | `sh generate_dict.sh mw` in `csl-pywork/v02` — but first check [What not to re-run](#what-not-to-re-run): both dirs are frozen |
| `mwsupplement/freshlook` scripts can't find `../mw.txt` | The expected copy inside `mwsupplement/` is not in git | `cp ../../csl-orig/v02/mw/mw.txt ../mw.txt` first |
| `greek_andhrabharati` diff ignores current `mw.txt` | `extract_greek(...)` is commented out in `__main__`; the 2021 log is reused | Uncomment the call to refresh the Cologne side |
| SLP1→IAST→SLP1 round trip shows 3 differing words | Known non-invertible words (h/gh ambiguity), documented in `mwtranscode/readme.txt` | Expected — the driver patches them; SLP1↔Devanagari is fully invertible |
| Transcoding output has wrong accent behaviour | Wrong driver generation — rules dir is baked in, not a flag | `mw_transcode.py` = `transcoder/`; `mw_transcode1.py`/`mw_transcode2.py` = `transcoder1/` (2022 accents) |
| `xmlchk_xampp.sh` reports an XML error | A correction broke tag structure | Open the generated `mw.xml` in Emacs, jump to the reported line (`C-c C-n`) — the recipe in the issue188 readme |
| GitHub Pages build breaks after committing an `.md` | The file contains literal `{%…%}` or `{{…}}` (correction records), which Jekyll/Liquid parses | Wrap the passage in `{% raw %}…{% endraw %}` ([CONTRIBUTING.md](https://github.com/sanskrit-lexicon/MWS/blob/master/CONTRIBUTING.md)) |
| `gbif_currency.py` is slow or fails offline | First run hits the live GBIF API | Re-runs are free via `species_currency_cache.json`; delete the cache only to force a refetch |
| `tooltip.py` dies on `import transcoder` | It expects `transcoder.py` at the repo root, which doesn't exist | Copy `mwtranscode/transcoder.py` up (or fix the path) — and note the script is Python 2 |

## Glossary

| Term | Meaning here |
|---|---|
| SLP1 | The ASCII Sanskrit encoding of `mw.txt`; all `<k1>`/`<k2>` keys and `<s>` spans |
| IAST | Roman transliteration with diacritics; `mwtranscode/` converts SLP1 ↔ IAST |
| change file | The auditable `NNN old` / `NNN new|ins|del` transaction list applied by `updateByLine.py` |
| `temp_mw_N.txt` | Gitignored working copy of `mw.txt`, one per correction round (N = 0 is the seed) |
| L-number | `<L>` record identifier (may be decimal, e.g. `27713.2`); stable across corrections |
| `<k1>` / `<k2>` | Headword keys — plain SLP1 vs accent-bearing form |
| `<ls>` | Literary-source citation tag; its abbreviations ("sigla") are what link-target work resolves |
| `<ab>` | Abbreviation tag (grammatical and editorial shorthands) |
| `<hom>` | Homophone number distinguishing same-spelling headwords |
| phw | Phrasal headword — the `<info phwchild=…>`/`<info phwparent=…>` graph audited by `phw_graph/` |
| supplement entry | A record flagged `<info n="sup"/>`, from MW's 1899 Additions — classified by `mwsupplement/` |
| `monier.xml` / `mw.xml` | Build products of `csl-pywork`'s `generate_dict.sh`, not committed sources |
| batch queue | `csl-corrections/batch_pending/dictionaries/mw/` — where validated corrections wait for the monthly PR |
| `$BASE` | The legacy XAMPP-layout root in old docs (`/c/xampp/htdocs`); appears in prose only, never in scripts |

## Maintainer appendix

### Invariants

1. **Agents never commit or push to `csl-orig`** — corrections travel only
   through the batch queue and the monthly consolidated PR.
2. **The change file is the artifact; `temp_mw_N.txt` is disposable.** The
   `.gitignore` pattern `temp*` enforces this — nothing named `temp*` ever
   lands in git.
3. **`updateByLine.py`'s hard-fail on mismatch is the safety property.** Any
   "fix" that makes it tolerant destroys the audit chain.
4. **`mw.txt` is UTF-8 with no BOM** (asserted by `mw_integrity`); change
   files are UTF-8.
5. **The consolidated preface editions are never hand-edited** — always
   regenerate via `build_combined.py`.
6. **PRs target `master`**, and never branch from `docs-pass` (it carries
   paper commits).

### Known traps and observed defects

1. The
   [README.md](https://github.com/sanskrit-lexicon/MWS/blob/master/README.md)
   Contents table predates the 2026 additions — `mwissues/`,
   `botanical_glossary/`, `lexicographer_dcs/`, `phw_graph/`,
   `mw_integrity/`, `relative_refs/`, `root_crosswalk/`, `review_packets/`,
   `papers/`, `planning/` are absent from it (though `mwissues/markup_fix/`'s
   audit is load-bearing for `DATA_DICTIONARY.md`).
2. `CORRECTIONS_issue_362/` names its script `issue_632.py` — a digit
   transposition, not a different issue.
3. `greek_andhrabharati/place_greek_text.py`'s docstring advertises an
   `mw1.txt` output and a "placing" function that were never written.
4. `mwverbs/redo.sh` and `mwverbs/readme.txt` disagree with each other about
   the input path (`../../../` vs `../../../../`) — and both are wrong on a
   flat checkout.
5. `README.md~` at the repo root is a stale editor backup;
   `missing1.html` is **Vācaspatya** (VCP) correction data misfiled into MWS.
6. Two frozen data drops (`key2-avagraha-225-entries.txt`,
   `step1a-191-unique-entries.txt`) begin with a UTF-8 BOM — unlike `mw.txt`,
   which must have none. Reference data only; do not imitate.
7. `parseheadline.py` is copy-pasted into six-plus workspaces — a ruled
   no-refactor ([ANALYSIS.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ANALYSIS.md));
   fix a bug in every copy or in none.
8. `basic04a/` and `list02php/` depend on the **live Cologne `apidev`
   endpoints** — a development surface that can move or rate-limit; a blank
   demo is usually Cologne-side, not a local regression.

Improvement backlog, provenance and revision history live in the companion
metadoc:
[docs/PIPELINE_MANUAL.meta.md](https://github.com/sanskrit-lexicon/MWS/blob/master/docs/PIPELINE_MANUAL.meta.md).

_Dr. Mārcis Gasūns_
