# HANDOFF_PROMPTS — ready-to-paste kickoff prompts + model selection

**Companion to [HANDOFF.md](HANDOFF.md).** Where HANDOFF.md describes the *state*, this file gives the *messages* to paste into a new Claude chat and the *model* to pick for each kind of task.

---

## 1. Universal kickoff prompt (drop-in, then add a task)

Copy-paste into a fresh Claude chat, then append one of the task lines from §2:

```
Continue the MW1899 microanalysis + csl-atlas project for @gasyoun
(CDSL member; sanskrit-lexicon GitHub org).

Read these in this order before doing anything:
1. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/HANDOFF.md
2. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/DOUBTS.md  (note the "Result" blocks at top of D1/D2/D4/D6/D7/D8)
3. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md  (the canonical paper)
4. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/README.md  (audit-suite overview)
5. C:/Users/user/.claude/projects/D--claude/memory/feedback_issue_links.md  (the link-every-claim rule — applies universally)

Local working clone: D:/claude/mws_repo/ on the `docs-pass` branch.
Microanalysis suite: papers/microanalysis/  (HANDOFF, DOUBTS, PAPER, MICROANALYSIS, README, VISUALISATIONS + analysis/ + figures/ + decisions/)
Dictionary data files at /tmp/  (= C:/Users/user/AppData/Local/Temp/  on Windows):
  mw.txt, pwg.txt, pw.txt (PWK), ap.txt, wil.txt, ben.txt (Benfey 1866),
  cae.txt (Cappeller 1891), skd.txt, vcp.txt, plus the four koshas
  armh.txt, abch.txt, acph.txt, acsj.txt.  All gitignored.

Conventions to follow:
- Every verifiable claim in issues OR docs must be a [text](URL) hyperlink. No
  bare backticks for filenames, sections, dates, abbreviations, record numbers.
- Use the Bash tool for git (no `cd`); commit with prefix `docs-pass:` and the
  trailer `Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>` (substitute
  the actual model name if running on Sonnet/Haiku).
- Never push to master; only the `docs-pass` branch.
- The MWS repo has two local clones (`D:/claude/mws_repo/` and
  `C:/Users/user/Documents/GitHub/MWS/`); `git fetch && git pull` in one after
  commits to the other.

Now: [PASTE ONE OF THE TASK LINES FROM HANDOFF_PROMPTS §2 HERE]
```

---

## 2. Task-specific lines (append one to the kickoff prompt above)

### Thread A — Pre-submission paper polish

**A1 · Print-preface check** (Opus 4.7):
```
Address DOUBTS D2's remaining open item: read the 1891 Cappeller, 1866 Benfey, and 1832 Wilson print prefaces (or scans from archive.org if PDFs available) and check whether any predates MW's <ls>L.</ls> with an analogous "lexicographer-only" hedge convention. Update PAPER.md Appendix C with findings; soften or keep the "MW innovation" claim. Then resolve the Cappeller asterisk + dagger markers (1,370× and 903×) — is either an entry-level hedge?
```

**A2 · D5 typology refactor** (Opus 4.7):
```
Refactor PAPER.md §5 to address DOUBTS D5: distinguish "primary article types" (root / nominal / adjective / indeclinable / compound / derived / continuation / encyclopedic) from "orthogonal properties" (Vedic-accented / lexicographer-hedged / IE-cognate-bearing). Update the block-by-type matrix presentation accordingly. The current 14-type scheme has heavy overlap; the refactor should reduce to ~8 primary types + ~3 orthogonal properties without losing analytical depth.
```

**A3 · Build the reproducibility ZIP** (Sonnet 4.6):
```
Run analysis/make_supplement.py to produce the IJL supplementary-materials ZIP per Decision 16. Verify the ZIP contents against analysis/SUPPLEMENT_MANIFEST.md. Confirm the ZIP is gitignored. Update SUPPLEMENT_MANIFEST.md if the manifest drifted from the script.
```

**A4 · Final paper polish** (Opus 4.7):
```
Final pass on PAPER.md before IJL submission. Tighten the abstract (currently ~5.7K words; target ~8K for IJL). Verify every cross-link still resolves. Run analysis/check_docs.py and fix anything it flags. Ensure §9 limitations cite the empirical audits (SPOTCHECK, SIGNIFICANCE_FULL, CROSS_DICT, LS_HEDGE_CHECK).
```

### Thread B — Russian translation review

**B1 · Walk through bootstrap translations** (Opus 4.7):
```
Walk @gasyoun through papers/microanalysis/figures/locales/ru.json. For each Russian string, flag confidence (high/medium/low). The bootstrap drew on Zaliznyak's grammatical terminology, Indoevropeyskoe yazykoznanie, Petersburg Indological Studies, and Roerich/Zograf Readings conventions; verify each term against modern usage. Apply IAST-in-italics for embedded Sanskrit per Decision 6.
```

**B2 · Regenerate Russian figures** (Sonnet 4.6):
```
After @gasyoun's review of locales/ru.json (Thread B1), regenerate heatmap-ru.svg/png, treemap-ru.svg/png, sankey-ru.svg/png/html, and timeline-ru.md. Verify every label matches the updated locale file. Re-export figures via papers/microanalysis/figures/scripts/.
```

### Thread C — csl-atlas microsite

**C1 · Scaffold csl-atlas locally** (Sonnet 4.6):
```
Scaffold a new D:/claude/csl-atlas/ directory using Observable Framework (per Decision 10). Pull the per-dict JSON data from papers/microanalysis/figures/data/. Build the hybrid-nav structure (per Decision 20): src/papers/{wiegand,atkins-rundell,hausmann,grounded}.md tour pages + src/tools/{matrix-explorer,lineage-sankey,typology-treemap,timeline,type-comparator,citation-tracer}.md tool pages. EN at root, RU at /ru/ (Decision 25). Do NOT push to the org yet — local scaffolding only.
```

**C2 · Per-dict atlas chapter** (Sonnet 4.6, parameterised):
```
Use the data in papers/microanalysis/analysis/CROSS_DICT_PROFILES.md (covers 9 dicts) to populate a chapter for {DICT} in csl-atlas. The chapter pulls the dict's block matrix, applies the same heatmap renderer, generates a per-type radar, and embeds the dict's Cologne-web link. Match MW's chapter template.
```

**C3 · Phase-4 ordering decision** (Opus 4.7):
```
Decide the Phase-4 atlas dict ordering. Inputs: the cross-dict audit results (CROSS_DICT_PROFILES.md shows PWG/PWK/AP behave like MW; SKD/VCP fall outside the framework). User preferences: which dict matters most editorially. Propose an order and write the rationale.
```

### Thread D — Phase 4 (org-wide docs-pass rollout)

**D1 · Pilot review response** (Opus 4.7):
```
The 5 pilot docs-pass branches are awaiting review by @funderburkjim and @Andhrabharati (issues #195 in MWS, #1 in csl-sqlite, #15 in csl-inflect, #20 in hwnorm1, #455 in COLOGNE). Read the maintainers' comments and integrate corrections. Update DICT_PROFILE.md, ENTRY_GUIDE.md, etc. on the docs-pass branch in the affected repo(s).
```

**D2 · Wave-1 rollout (next 15 dict repos)** (Sonnet 4.6):
```
Apply the docs-pass pattern to wave 1 of Phase 4. Pull the next 15 dict repos from sanskrit-lexicon org (see D:/claude/sanskrit-lexicon-docs-review/runbooks/dict-docs-pass.md). For each: create docs-pass branch, run the runbook, open a tracking issue with proper links. Use the DICT_PROFILE.md + ENTRY_GUIDE.md templates from MWS as the model.
```

**D3 · Per-dict ROADMAP composition** (Sonnet 4.6):
```
For dict {DICT}: synthesise its open + closed GitHub issues into a ROADMAP.md following the MWS template (papers/MWS/blob/docs-pass/ROADMAP.md). 10 task subtypes, quarterly cadence, cross-repo dependencies. Commit on the dict's docs-pass branch.
```

### Cross-cutting / housekeeping

**X1 · Memory consolidation** (Sonnet 4.6):
```
Address DOUBTS D14 (memory file inflation). Read C:/Users/user/.claude/projects/D--claude/memory/project_docs_review.md (9 phases). Collapse to a single "current state" summary at the top + an archive section below. Do not lose facts; reorganise for next-session readability. Update MEMORY.md index after.
```

**X2 · Link-rotting audit** (Haiku 3.5):
```
Run papers/microanalysis/analysis/check_docs.py to validate every relative file link and #anchor across the microanalysis + docs-pass markdown. Fix anything broken in a single commit titled `docs-pass: link audit`.
```

**X3 · New doubt surfacing** (Opus 4.7):
```
Review PAPER.md as a hostile peer reviewer. Add new doubts to DOUBTS.md if any claim is under-evidenced, any methodology is regex-brittle, any cross-dict generalisation overreaches, or any framework attribution is sloppy. Be ruthless. Each new doubt gets blocking/important/nice-to-resolve rating.
```

---

## 3. Model selection matrix

Where Claude has multiple model variants available, the choice affects quality, speed, and cost. Heuristic: **Opus for judgment, Sonnet for pattern, Haiku for mechanics.**

### By task type

| Task class | Recommended model | Rationale |
|---|---|---|
| **Scholarly synthesis** (read print prefaces, integrate findings, propose new claims) | **Opus 4.7** | Multi-source interpretive work; mistakes propagate into the paper |
| **High-stakes prose** (paper abstract, conclusion, §9 limitations, journal cover letter) | **Opus 4.7** | Submission-quality writing |
| **Architectural restructuring** (D5 typology refactor; DOUBTS surfacing; consolidation decisions like D4) | **Opus 4.7** | Wide-context reasoning; one mistake can require rework |
| **Linguistic judgement** (Russian translation review, IAST/transliteration verification, Sanskrit terminology) | **Opus 4.7** | @gasyoun-facing quality bar |
| **Routine docs-pass on new repos** (apply established runbook, no novel decisions) | **Sonnet 4.6** | Pattern application across many files; Opus is overkill |
| **Figure generation from existing data** (re-render after locale edits; regenerate after stats update) | **Sonnet 4.6** | Mechanical Python execution |
| **Per-dict atlas chapter composition** (apply MW chapter template to a different dict) | **Sonnet 4.6** | Templated pattern application |
| **Issue-body composition** with the linking rule | **Sonnet 4.6** | Apply established convention |
| **Memory consolidation** (D14) | **Sonnet 4.6** | Routine restructuring with judgement at edges |
| **Reproducibility ZIP / supplement build** | **Sonnet 4.6** | Mechanical script execution |
| **Observable Framework scaffolding** | **Sonnet 4.6** | Standard web-stack setup |
| **Single-line typo fixes / format conformance** | **Haiku 3.5** | Cheap and fast for trivial edits |
| **Link-rot audits / regex sweeps** | **Haiku 3.5** | Pattern matching at scale |
| **README synchronisation after a commit** | **Haiku 3.5** | Templated updates |
| **Batch metadata extraction across files** | **Haiku 3.5** | Parallelisable simple reads |

### By thread

| Thread | Mostly | Sometimes |
|---|---|---|
| **A** Paper polish | Opus 4.7 | Sonnet for A3 (reproducibility ZIP) |
| **B** RU review | Opus 4.7 for B1 review | Sonnet 4.6 for B2 figure re-render |
| **C** csl-atlas | Sonnet 4.6 for build | Opus 4.7 for C3 scope decision |
| **D** Phase 4 rollout | Sonnet 4.6 | Opus 4.7 for D1 maintainer-feedback integration |
| **X** Housekeeping | Sonnet 4.6 or Haiku 3.5 | Opus 4.7 for X3 new-doubts review |

### Combined-model workflow ("escalation pattern")

For complex multi-step tasks, run multiple sessions:

1. **Opus 4.7 session** drafts the plan + writes the spec
2. **Sonnet 4.6 session** executes the spec (file edits, scripts, commits)
3. **Opus 4.7 session** reviews the result for quality before submission

This is more expensive in total but each step uses the right tool. Most appropriate for:
- Paper submission (draft → revise → final pass)
- Atlas scaffolding (architecture → implementation → review)
- Phase 4 wave (planning → batch rollout → consolidation)

### Cost notes (rough, 2026 pricing tiers)

If cost matters:
- **Haiku** is ~1/10 the cost of Sonnet, ~1/30 the cost of Opus
- **Sonnet** is the default working horse; ~3/10 the cost of Opus
- **Opus** for high-stakes; reserve for paper writing, RU review, new-doubt surfacing, architecture

For sustained Phase 4 work (~76 repos × routine docs-pass), Sonnet is the practical default. Opus only when an editorial judgement is required.

---

## 4. Sample fully-composed prompts (ready to paste)

### Sample 1 — "Pre-submission polish + ZIP" (Opus 4.7)

```
Continue the MW1899 microanalysis + csl-atlas project for @gasyoun (CDSL
member; sanskrit-lexicon GitHub org).

Read these in this order before doing anything:
1. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/HANDOFF.md
2. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/DOUBTS.md
3. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md
4. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/README.md
5. C:/Users/user/.claude/projects/D--claude/memory/feedback_issue_links.md

Local working clone: D:/claude/mws_repo/ on the docs-pass branch.
Data files at /tmp/ on Linux paths = C:/Users/user/AppData/Local/Temp/ on Windows.

Conventions: every verifiable claim hyperlinked; commit with docs-pass: prefix;
Co-Authored-By: Claude Opus 4.7 trailer.

Now: address DOUBTS D2's remaining open item. Read the 1891 Cappeller, 1866
Benfey, and 1832 Wilson print prefaces and check whether any predates MW's
<ls>L.</ls> with an analogous "lexicographer-only" hedge convention. Update
PAPER.md Appendix C with findings; soften or keep the "MW innovation" claim.
Then resolve the Cappeller asterisk + dagger markers (1,370× and 903×) — is
either an entry-level hedge? After that, run analysis/make_supplement.py to
produce the IJL supplementary-materials ZIP per Decision 16.
```

### Sample 2 — "Phase 4 Wave 1 rollout" (Sonnet 4.6)

```
Continue the MW1899 microanalysis + csl-atlas project for @gasyoun.

Read first:
1. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/HANDOFF.md (esp. §6a, §10)
2. D:/claude/sanskrit-lexicon-docs-review/runbooks/dict-docs-pass.md
3. D:/claude/mws_repo/DICT_PROFILE.md (the MWS template to follow)

Conventions: every verifiable claim hyperlinked; docs-pass: commit prefix;
Co-Authored-By: Claude Sonnet 4.6 trailer.

Now: apply the docs-pass pattern to wave 1 of Phase 4. Pull the next 15 dict
repos from the sanskrit-lexicon org (skip the 5 already-done pilots: MWS,
csl-sqlite, csl-inflect, hwnorm1, COLOGNE; skip also the 4 temp_corrections_*
repos). For each repo: create docs-pass branch, run the runbook, open a
tracking issue with @-mentions to @funderburkjim and @Andhrabharati, every
filename in the issue body linked per the linking rule.
```

### Sample 3 — "Russian translation review" (Opus 4.7, with @gasyoun in the loop)

```
Continue the MW1899 project for @gasyoun.

Read:
1. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/HANDOFF.md
2. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/decisions/I18N.md
3. https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/locales/ru.json

Conventions: every claim hyperlinked; docs-pass: commit prefix; Opus 4.7 trailer.

Now: walk @gasyoun through papers/microanalysis/figures/locales/ru.json
section by section. For each Russian string, flag your confidence
(high/medium/low). The bootstrap drew on Zaliznyak's grammatical terminology
and Indoevropeyskoe yazykoznanie conventions; verify each term against modern
usage. Sanskrit terms stay in IAST italics per Decision 6 — do not transliterate
to Cyrillic. Update the JSON file in commits after @gasyoun reviews each batch.
```

---

## 5. When NOT to start a new chat

A new chat session costs you the in-conversation context. Sometimes you want to **stay in the existing chat** rather than handoff:

- The current task is a small follow-up (< 30 min of work) on what was just done
- The user is mid-conversation and would lose conversational state
- You need to refer to a recent tool result that hasn't been committed yet
- The compaction summary from your current chat is still fresh

A new chat is the right move when:
- A long break has elapsed (> 1 day)
- The context window is full or near-full
- The previous chat's conclusion was an explicit handoff
- The task changes scope substantially (Thread A → Thread D)
- Switching model tiers (e.g. dropping from Opus to Sonnet for routine work)

---

## 6. Quick reference card

```
NEW CHAT? COPY-PASTE STEP-BY-STEP:
  1. From §1 above, paste the kickoff block
  2. From §2 above, append one task line
  3. Pick the right model from §3 ("Opus for judgment, Sonnet for pattern, Haiku for mechanics")
  4. Hit send

EXISTING CHAT? READ:
  HANDOFF.md   for state
  DOUBTS.md    for known-unknowns
  PAPER.md     for the canonical claim set
  this file    for templates
```

---

*Maintained alongside [HANDOFF.md](HANDOFF.md). Updated when new threads, sample prompts, or model-selection heuristics emerge from real usage.*
