# HANDOFF_PROMPTS — three prompt lists, one per model

**Companion to [HANDOFF.md](HANDOFF.md).** Where HANDOFF.md describes the *state*, this file gives the **paste-ready prompts** for new Claude chats — organised by **which model to pick**, with explicit **downshift criteria** so you know when to stop paying for Opus.

The decision flow you actually want:

```
   START HERE → "Which model am I willing to pay for today?"
        │
        ├──► Opus 4.7  (judgment, scholarly synthesis, high-stakes prose)
        │       └── pick from §2 OPUS LIST
        │
        ├──► Sonnet 4.6  (routine pattern, technical execution)
        │       └── pick from §3 SONNET LIST
        │
        └──► Haiku 3.5  (pure mechanics, batch fixes)
                └── pick from §4 HAIKU LIST

   While running, watch for §5 "downshift signals"
   to drop from Opus → Sonnet → Haiku within the same task.

```

---

## 1. Universal kickoff block (prepend to any task)

Paste this BEFORE the task line. It carries the read-list, paths, and conventions every new chat needs:

```
Continue the MW1899 microanalysis + csl-atlas project for @gasyoun
(CDSL member; sanskrit-lexicon GitHub org).

Read these in this order before doing anything:
1. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/HANDOFF.md
2. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/DOUBTS.md  (note the "Result" blocks at top of D1/D2/D4/D6/D7/D8)
3. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md  (the canonical paper)
4. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/README.md
5. C:/Users/user/.claude/projects/D--claude/memory/feedback_issue_links.md  (the link-every-claim rule — universal)

Local working clone: D:/claude/mws_repo/ on the `docs-pass` branch.
Dictionary data at /tmp/  (= C:/Users/user/AppData/Local/Temp/  on Windows):
  mw.txt, pwg.txt, pw.txt (PWK), ap.txt, wil.txt, ben.txt (Benfey 1866),
  cae.txt (Cappeller 1891), skd.txt, vcp.txt + the four koshas
  armh.txt, abch.txt, acph.txt, acsj.txt.

Conventions:
- Every verifiable claim in issues or docs must be a `[text](URL)` hyperlink.
- git commits prefixed `docs-pass:`, trailer `Co-Authored-By: Claude <MODEL> <noreply@anthropic.com>`.
- Never push to master; only `docs-pass`.

Now: [PASTE ONE TASK LINE FROM THE OPUS / SONNET / HAIKU LIST BELOW]

```

---

## 2. OPUS 4.7 prompts — when judgment matters

Opus only earns its cost when at least one of these conditions holds:
- The output is **scholarly prose** that will be published (paper, cover letter, RU venue).
- The decision **propagates** — getting it wrong forces rework downstream.
- The task requires **synthesis across multiple unstructured sources** (print prefaces, foreign-language indological references).
- The output is **user-facing** at the @gasyoun-or-reviewer quality bar.

Otherwise, drop to Sonnet.

### O1 · Read Cappeller / Benfey / WIL print prefaces, resolve D2

**Effort: ~2–3h** ([D2](DOUBTS.md#d2--the-lslls-mw-innovation-claim--under-checked--important) close-out)

```
Address DOUBTS D2's remaining open item. Read the 1891 Cappeller, 1866 Benfey,
and 1832 Wilson print prefaces (scans from archive.org or sanskrit-lexicon.uni-koeln.de
where available) and check whether any predates MW's <ls>L.</ls> with an
analogous "lexicographer-only" hedge convention. Also: resolve the Cappeller
asterisk + dagger markers (1,370× and 903× per analysis/LS_HEDGE_CHECK.md) —
is either an entry-level hedge? Update PAPER.md Appendix C with findings;
soften or keep the "MW innovation" claim accordingly; close or refine DOUBTS D2.

```

**↓ Downshift to Sonnet when:** the findings are written into PAPER.md Appendix C and DOUBTS D2 is closed. Subsequent reference-list maintenance, BibTeX entries, and link audits are Sonnet/Haiku work.

---

### O2 · D5 typology refactor in PAPER.md

**Effort: ~2h** ([D5](DOUBTS.md#d5--article-type-typology--14-is-too-many--overlapping--important))

```
Refactor PAPER.md §5 to address DOUBTS D5: the 14 article types have heavy
overlap (vedic_accented orthogonal to all gender types; biographical overlaps
with noun_m for proper-name masculines; lexicographer_only is a citation
property not an article type). Restructure into ~8 primary article types
(root / nominal-with-gender-subfeature / adjective / indeclinable / compound /
derived / continuation / encyclopedic) + ~3 orthogonal properties (Vedic
accent / lex-hedged / IE-cognate-bearing). Update the block-by-type matrix
presentation. Update MICROANALYSIS.md §3 in parallel so the two stay in sync.

```

**↓ Downshift to Sonnet when:** the new structure is decided in PAPER.md §5 and MICROANALYSIS.md §3. Re-rendering the heatmap and treemap against the new categories is mechanical Python — Sonnet.

---

### O3 · Final PAPER.md polish for IJL submission

**Effort: ~3–4h**

```
Final pre-submission pass on PAPER.md. Currently ~5.7K words; IJL target 8–10K.
Tighten the abstract; sharpen §7 triangulation; verify §9 limitations cite
the empirical audits (SPOTCHECK, SIGNIFICANCE_FULL, CROSS_DICT, LS_HEDGE_CHECK)
with specific numbers. Verify every cross-reference resolves. Confirm Appendices
A–C are properly condensed (each ~1.5K words). Improve any limp prose. Do NOT
run mechanical scripts in this session.

```

**↓ Downshift to Sonnet when:** the prose is final. Then run `analysis/check_docs.py` to find link rot (Haiku is fine), regenerate any stale figure cross-references (Sonnet), and re-build the supplementary ZIP via `make_supplement.py` (Sonnet).

---

### O4 · Russian translation review with @gasyoun in the loop

**Effort: 1–2h per batch, ~3 batches**

```
Walk @gasyoun through papers/microanalysis/figures/locales/ru.json
section by section. For each Russian string, flag confidence
(high/medium/low). Bootstrap drew on Zaliznyak's grammatical terminology,
Indoevropeyskoe yazykoznanie conventions, Petersburg Indological Studies
register. Verify each term against current academic Russian indological usage.
Sanskrit terms stay in IAST italics per Decision 6 — do not transliterate
to Cyrillic. Commit corrections after each batch is reviewed.

```

**↓ Downshift to Sonnet when:** all batches reviewed and `ru.json` is committed in its corrected form. Regenerating `-ru.svg/png` figures from the updated locale is Sonnet (mechanical Python).

---

### O5 · Phase-4 atlas dict ordering decision

**Effort: ~1h** ([D10](DOUBTS.md#d10--csl-atlas-is-named-before-scoped--important))

```
Decide the Phase-4 atlas dict ordering. Inputs: analysis/CROSS_DICT_PROFILES.md
(shows PWG/PWK/AP behave structurally like MW; SKD/VCP fall outside the
framework); HANDOFF.md §6c (csl-atlas planned, not yet scaffolded);
@gasyoun's editorial priorities. Propose an order for the 9 dicts (MW, PWG,
PWK, AP, WIL, SKD, ARMH, ABCH + VCP) covering: which goes first, which
chapter template variants are needed, what minimum data each chapter requires.
Commit rationale to decisions/MICROSITE.md.

```

**↓ Downshift to Sonnet when:** the order is committed. Per-dict chapter scaffolding and per-dict block-matrix extraction are Sonnet routine.

---

### O6 · Maintainer-review integration (5 pilot issues)

**Effort: ~2–4h depending on review depth**

```
@funderburkjim and @Andhrabharati have left review comments on one or more of
the 5 pilot docs-pass issues: MWS #195, csl-sqlite #1, csl-inflect #15,
hwnorm1 #20, COLOGNE #455. Read each comment, judge whether to accept (most
maintainer corrections should be accepted; flag any that contradict the
empirical-audit findings). Apply accepted corrections to the relevant
docs-pass branch in a commit per repo. Respond on each issue with a
linking-rule-compliant summary of what changed.

```

**↓ Downshift to Sonnet when:** the substantive corrections are landed. Routine follow-up edits across the rolled-out Phase-4 repos are Sonnet.

---

### O7 · Hostile peer-review of PAPER.md (new doubts)

**Effort: ~1.5h** ([D-surface](DOUBTS.md))

```
Read PAPER.md as a hostile peer reviewer would. Surface any new doubts: under-
evidenced claims; regex-brittle methodology; cross-dict over-generalisations;
framework attribution sloppiness; rhetorical overreach. Each new doubt gets
blocking/important/nice-to-resolve rating and a "Test:" recipe. Commit to
DOUBTS.md as D16, D17, … as needed. Don't fix what you find — just record it.

```

**↓ Downshift to Sonnet when:** new doubts are recorded. Empirical audit scripts to address them are Sonnet (extending analysis/ in the established pattern).

---

### O8 · IJL cover letter

**Effort: ~1h**

```
Compose the IJL submission cover letter for PAPER.md. Single page. Justify
(a) the data-grounded approach over imposing one framework, (b) the
consolidation into one paper rather than four (per D4), (c) the empirical-
audit suite as supplementary materials, (d) why IJL is the right venue.
Tone: confident but not boastful; specific not vague. Save to
papers/microanalysis/IJL_COVER_LETTER.md.

```

**↓ Downshift to Haiku when:** the cover letter is final. Cover-letter formatting / line spacing / minor proofreading is Haiku.

---

### O9 · Russian-language venue paper composition

**Effort: ~4–6h**

```
Draft the Russian-language companion paper for a Russian indological venue
(Indoevropeyskoe yazykoznanie / Petersburg Indological Studies / a Zograf
Readings proceedings volume). Cover the findings specific to a Russian
academic audience: kosha lineage (WIL ← Indian kosha tradition), Sanskrit
microstructure typology, MW's <ls>L.</ls> hedge as 19th-century European
editorial innovation. ~5K Russian words. IAST in italics for Sanskrit (no
Cyrillic transliteration). Commit to papers/microanalysis/PAPER_RU.md.

```

**↓ Downshift to Opus stays:** Russian-language drafting is full-Opus work. After draft is complete, Opus reviews edits; Sonnet handles bibliography formatting.

---

### O10 · Memory consolidation (D14) — when it matters

**Effort: ~1h** ([D14](DOUBTS.md#d14--memory-file-inflation--nice-to-resolve)) — *do in Opus only if you're also making strategic project-direction decisions*

```
Read C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md
(9+ phases). Collapse to a "Current state (HEAD=X)" snapshot at the top
+ an "Archive" section below with each phase summarised in 3-5 lines.
Decide which phase facts are still relevant vs which are archival.
Update MEMORY.md index. Do not lose facts.

```

**↓ Downshift to Sonnet** if the project-direction question is settled — Sonnet is fine for the mechanical consolidation if you've already decided what to keep.

---

## 3. SONNET 4.6 prompts — the workhorse tier

Sonnet for **pattern application, technical execution, routine docs work**. The vast majority of Phase-4 rollout work belongs here.

### S1 · Build the reproducibility ZIP (Decision 16)

**Effort: ~15 min**

```
Run papers/microanalysis/analysis/make_supplement.py to produce the IJL
supplementary-materials ZIP. Verify the ZIP contents against
analysis/SUPPLEMENT_MANIFEST.md. Confirm the ZIP is gitignored. If the
manifest has drifted from the script's actual output, update the manifest
to match. Commit only if SUPPLEMENT_MANIFEST.md changed.

```

### S2 · Regenerate Russian figures after locale review

**Effort: ~30 min**

```
After @gasyoun's review of locales/ru.json is committed, regenerate the
Russian-locale figures: heatmap-ru.svg/png, treemap-ru.svg/png,
sankey-ru.svg/png/html, timeline-ru.md. Re-export via
papers/microanalysis/figures/scripts/. Verify every label matches the
updated locale strings. Commit the new figures.

```

### S3 · csl-atlas local scaffolding (Observable Framework)

**Effort: ~2h**

```
Scaffold a new D:/claude/csl-atlas/ directory using Observable Framework
(npm install observable, etc.). Hybrid-nav structure per Decision 20:
src/papers/{wiegand,atkins-rundell,hausmann,grounded}.md tour pages +
src/tools/{matrix-explorer,lineage-sankey,typology-treemap,timeline,type-
comparator,citation-tracer}.md tool pages. EN at root, RU at /ru/ per
Decision 25. Pull JSON data from papers/microanalysis/figures/data/ via
relative paths. Do NOT push to the org yet — local scaffold only.

```

### S4 · Per-dict atlas chapter

**Effort: ~1h per dict**

```
Use analysis/CROSS_DICT_PROFILES.md data to populate a chapter for DICT={X}
in csl-atlas. Apply the MW chapter template: pull the dict's block matrix,
apply the heatmap renderer, generate a per-type radar, embed the dict's
Cologne web display link. Same colour palette + locale strings. Replace {X}
with one of: pwg, pw, ap, wil, skd, vcp, armh, abch.

```

### S5 · Per-dict block-matrix extension

**Effort: ~30 min per dict**

```
Extend the block-detection pipeline to dict {X}. Reuse papers/microanalysis/
figures/scripts/export_data.py (the published detector). Account for dict-
specific markup conventions (PWG/PWK use <ab> differently; SKD/VCP have no
<lex>). Output JSON to papers/microanalysis/figures/data/{X}_blocks.json.
Document any dict-specific detector adjustments in
analysis/CROSS_DICT_PROFILES.md.

```

### S6 · Phase-4 wave-1 rollout (next 15 dict repos)

**Effort: ~8–10h**

```
Apply the docs-pass pattern to wave 1 of Phase 4. Pull the next 15 dict repos
from the sanskrit-lexicon org (skip the 5 already-done pilots: MWS, csl-sqlite,
csl-inflect, hwnorm1, COLOGNE; skip the 4 temp_corrections_*). For each repo:
create docs-pass branch, run D:/claude/sanskrit-lexicon-docs-review/runbooks/
dict-docs-pass.md, open a tracking issue with @-mentions to @funderburkjim
and @Andhrabharati. Every filename in every issue body linked per the linking
rule. Use MWS's DICT_PROFILE.md + ENTRY_GUIDE.md as templates.

```

### S7 · Per-dict ROADMAP composition

**Effort: ~1h per dict**

```
For dict {DICT}: synthesise its open + closed GitHub issues into a ROADMAP.md
following the MWS template (https://github.com/sanskrit-lexicon/MWS/blob/
docs-pass/ROADMAP.md). 10 task subtypes + quarterly cadence + cross-repo
dependencies + complete issue → roadmap map. Commit on the dict's docs-pass
branch.

```

### S8 · Per-dict DICT_PROFILE.md from MWS template

**Effort: ~2h per dict**

```
For dict {DICT}: produce a DICT_PROFILE.md following the MWS template
(https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md).
Sections: At-a-Glance, Orthographical conventions (short — link to ENTRY_GUIDE
for full), Historical background, Scholarly significance, When-to-use matrix,
Article types, Citation markers, Relationship to other CDSL dicts, Sample
entries (~3), Known issues, Further reading, BibTeX. Use real data from the
dict's csl-orig source. Commit on docs-pass branch.

```

### S9 · Issue body composition with linking rule

**Effort: ~30 min per issue**

```
Compose the tracking-issue body for the {REPO} docs-pass branch. Apply the
linking rule (feedback_issue_links.md) strictly: every filename in tables,
prose, AND checklists is a `[text](URL)` hyperlink to the docs-pass branch;
every record number links to mw.txt line anchor; every abbreviation links
to its definition; every section description links to its section anchor.
@-mention @funderburkjim and @Andhrabharati for review.

```

### S10 · Memory file consolidation (D14)

**Effort: ~1h** (when project direction is already settled)

```
Address DOUBTS D14. Read C:/Users/user/.claude/projects/D--claude/memory/
project_docs_review.md (9+ phases). Collapse the older phases (3.1–3.7) into
a single Archive section; keep the latest 1–2 phases as "Current state."
Preserve all factual content; reorganise for next-session readability. Update
MEMORY.md index. Verify links still resolve.

```

### S11 · Cross-figure data consistency audit

**Effort: ~30 min**

```
Verify the data behind the four Tier-1 figures + Fig 5–6 is internally
consistent. Heatmap and treemap should agree on type counts; Sankey should
agree with LS_HEDGE_CHECK on `L.` counts. Run a script that reads
figures/data/*.json and checks for discrepancies. Report any mismatch.

```

### S12 · ROADMAP velocity update

**Effort: ~15 min**

```
Refresh papers/MWS/blob/docs-pass/ROADMAP.md velocity numbers. Re-query the
GitHub issue API for: total open, total closed, closed in last 12 months,
per-label counts. Compare to the snapshot dated 2026-05-23 in §"Status
snapshot." Commit updated numbers.

```

---

## 4. HAIKU 3.5 prompts — pure mechanics

Haiku for **batch fixes, format conformance, pattern matching with no judgement**. Cheap and parallel.

### H1 · Link-rotting audit

**Effort: ~5 min**

```
Run papers/microanalysis/analysis/check_docs.py against the entire
papers/microanalysis/ directory plus the docs-pass branch root. Fix anything
flagged: relative paths, broken section anchors, missing files. Single commit
titled `docs-pass: link audit`.

```

### H2 · Markdown format-conformance sweep

**Effort: ~10 min**

```
Sweep papers/microanalysis/*.md and decisions/*.md for: missing blank line
before code fences, inconsistent heading levels, trailing whitespace, mixed
tabs/spaces. Apply mechanical fixes; commit as `docs-pass: lint sweep`.
Do NOT change content.

```

### H3 · README synchronisation

**Effort: ~5 min**

```
After {COMMIT_SHA} introduced new files, update the affected README.md to
mention them in the index/table-of-contents. Apply to: papers/microanalysis/
README.md, papers/microanalysis/decisions/README.md, papers/microanalysis/
analysis/README.md, papers/microanalysis/figures/ (no README — skip).

```

### H4 · Find-and-replace pass

**Effort: ~5 min**

```
Across papers/microanalysis/ and the docs-pass branch root: find every
occurrence of "{OLD}" and replace with "{NEW}". Verify each replacement is
appropriate (not inside code blocks meant to preserve the old text). Commit
as `docs-pass: rename {OLD} -> {NEW}`.

```

### H5 · License-header injection

**Effort: ~5 min**

```
Inject the standard CC-BY-SA-4.0 license header into every new file added
since {COMMIT_SHA} that lacks one. Header text: matches existing files in
the repo. Commit as `docs-pass: license headers`.

```

### H6 · Footer / version-stamp regeneration

**Effort: ~10 min**

```
Re-render the version-stamp footer in every static figure under
papers/microanalysis/figures/. Format: "Source: CDSL mw.txt 2026-05-23 ·
CC-BY-SA-4.0 · build {SHA}" where {SHA} is the current HEAD commit short SHA.
Inject as SVG <text> element at bottom-right per Decision 26.

```

### H7 · Single-line typo corrections

**Effort: ~2 min per fix**

```
Apply these typo corrections (one per line below) across the docs-pass branch
files where the typo occurs. Single commit per batch of ~20.

{TYPO LIST GOES HERE}

```

### H8 · Listing extraction

**Effort: ~5 min**

```
Extract from /tmp/{DICT}.txt the unique set of <ls> values + their occurrence
counts. Output as a CSV sorted by count desc. Save to papers/microanalysis/
analysis/data/{DICT}_ls_counts.csv. Do not analyse the output — just produce
the file.

```

### H9 · PNG↔SVG parity check

**Effort: ~5 min**

```
For each SVG figure in papers/microanalysis/figures/, verify a matching PNG
exists and has the same content (re-render PNG from SVG if missing/stale).
Report any divergence.

```

### H10 · CI / build status summary

**Effort: ~3 min**

```
Read the most recent GitHub Actions workflow run logs for the MWS repo (or
csl-atlas once created). Summarise: pass/fail status, total time, any
warnings. Post a one-paragraph summary on the relevant tracking issue.

```

---

## 5. Downshift signals — when to stop paying for Opus

This is the answer to "when do I turn off Opus to save tokens." Watch for these signals **during** an Opus session and switch to Sonnet (or end the session and start a Sonnet one) when one appears:

| Signal | What it means | Action |
|---|---|---|
| **The judgement call has been made** | You wrote the prose, decided the architecture, chose the wording | Drop to Sonnet for implementation + Haiku for formatting |
| **You're doing find-and-replace** | The task became mechanical | Haiku |
| **You're running a script someone else wrote** | No new reasoning happening | Haiku (or just bash) |
| **You're regenerating a figure from updated data** | The pipeline does the work, you just trigger it | Sonnet |
| **You're updating timestamps, SHAs, or version stamps** | Pure mechanics | Haiku |
| **You're applying a runbook to a new repo** | Pattern-application, no judgement | Sonnet |
| **You're writing the Nth issue body following the linking-rule template** | Convention, not creation | Sonnet |
| **The current edit is a typo or one-liner** | Trivial | Haiku |
| **You realise you've been re-reading the same files for 10 minutes** | Probably stuck on a procedural step | Switch model AND re-orient via HANDOFF.md |
| **The user said "just do X mechanically"** | Direct instruction to drop the high-judgement model | Sonnet or Haiku |

**Inverse: when to ESCALATE to Opus mid-Sonnet session:**
- The task required a judgement Sonnet handled but you don't trust
- A novel scholarly question appeared (a new doubt, a fact you can't verify)
- @gasyoun pushed back on a Sonnet output with a substantive correction
- You're about to write text that will appear in PAPER.md
- The convention you've been applying turned out to be wrong

---

## 6. Sample fully-composed prompts (paste-ready)

### Sample for Opus 4.7

```
[Kickoff block from §1]

Now: Address DOUBTS D2's remaining open item. Read the 1891 Cappeller, 1866
Benfey, and 1832 Wilson print prefaces (scans from archive.org or
sanskrit-lexicon.uni-koeln.de where available) and check whether any
predates MW's <ls>L.</ls> with an analogous "lexicographer-only" hedge
convention. Also: resolve the Cappeller asterisk + dagger markers (1,370×
and 903× per analysis/LS_HEDGE_CHECK.md) — is either an entry-level hedge?
Update PAPER.md Appendix C with findings; soften or keep the "MW innovation"
claim accordingly; close or refine DOUBTS D2.

```

### Sample for Sonnet 4.6

```
[Kickoff block from §1, with the Co-Authored-By trailer set to "Claude Sonnet 4.6"]

Now: Apply the docs-pass pattern to wave 1 of Phase 4. Pull the next 15 dict
repos from the sanskrit-lexicon org (skip the 5 already-done pilots: MWS,
csl-sqlite, csl-inflect, hwnorm1, COLOGNE; skip the 4 temp_corrections_*).
For each repo: create docs-pass branch, run the runbook at
D:/claude/sanskrit-lexicon-docs-review/runbooks/dict-docs-pass.md, open a
tracking issue with @-mentions to @funderburkjim and @Andhrabharati. Every
filename in every issue body linked per the linking rule. Use MWS's
DICT_PROFILE.md + ENTRY_GUIDE.md as templates.

```

### Sample for Haiku 3.5

```
[Kickoff block from §1, with the Co-Authored-By trailer set to "Claude Haiku 3.5"]

Now: Run papers/microanalysis/analysis/check_docs.py against the entire
papers/microanalysis/ directory plus the docs-pass branch root. Fix anything
flagged: relative paths, broken section anchors, missing files. Single
commit titled `docs-pass: link audit`. Don't change semantic content.

```

---

## 7. When NOT to start a new chat

A new chat session costs in-conversation context. Stay in the existing chat when:

- The current task is a small follow-up (< 30 min) on what was just done.
- You'd lose conversational state (mid-PR discussion, mid-doubt-surfacing).
- You need to refer to a recent tool result that hasn't been committed yet.
- The compaction summary from the current chat is still fresh.

Start a new chat when:
- A long break has elapsed (> 1 day).
- The context window is full or near-full.
- The previous chat's conclusion was an explicit handoff.
- The task changes scope substantially (Opus paper polish → Sonnet rollout).
- You want to **switch model tiers** — this is the most common reason.

---

## 8. Quick reference

```
NEW CHAT? Three steps:
  1. From §1 above, paste the kickoff block.
  2. From §2 (Opus) / §3 (Sonnet) / §4 (Haiku), append one task.
  3. Pick the model that matches the list you took the task from.

MID-CHAT? Watch §5 downshift signals.
  When one fires, switch to the cheaper model in a NEW chat.

LOOKING FOR STATE? Read HANDOFF.md (state) + DOUBTS.md (known unknowns).
LOOKING FOR DECISIONS? Read VISUALISATIONS.md → decisions/ subfolder.
LOOKING FOR THE PAPER? Read PAPER.md (canonical) + analysis/README.md (audits).

```

---

*Maintained alongside [HANDOFF.md](HANDOFF.md). Update when new task patterns emerge from real usage. Sample-prompt §6 examples should be refreshed after each major project phase.*
