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

## ROUND-2 status banner (2026-05-27 → next session)

**Round 1 (O1-O10 / S1-S12 / H1-H10) is complete** — see the historical sections further down. All 10 Opus prompts and the 7 follow-up hostile-review doubts (D16-D22) closed in a single autonomous session 2026-05-27. Submission-v1 tag pushed. csl-atlas MW chapter live.

**Round 2 focuses on the atlas**: 8 remaining dict chapters (PWG, PWK, AP, BEN, CAE, WIL, SKD, VCP) authored per [Decision 29](decisions/MICROSITE.md#decision-29--phase-4-dictionary-ordering-chapter-templates-minimum-data-added-2026-05-27). All three model tiers feed this:

```
Haiku (refresh data + figures)
  ↓
Sonnet (per-dict block-matrix exports → atlas/data/*.json)
  ↓
Opus (author each chapter from the exports + Decision 29 template tier)
```

Run order is **Haiku first** (clean data), **Sonnet next** (per-dict JSON), **Opus last** (the chapters consume the JSON).

---

## 2A. OPUS — Round 2: atlas chapters 2–9

**Authoring order** per [Decision 29 §29.4](decisions/MICROSITE.md): MW (done) → PWG → CAE → BEN → PWK → AP → WIL → SKD → VCP. Each chapter follows the [Tier A / B / C template](decisions/MICROSITE.md#292--chapter-template-variants-three-tiers) appropriate to the dict. Each chapter ~2–3 h; the MW chapter at [`csl-atlas/src/dicts/mw.md`](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/dicts/mw.md) is the worked example.

### O1 · PWG chapter (Tier A — full template)

**Effort: ~3h** ([Decision 29 #2](decisions/MICROSITE.md), position 2 in the atlas)

```
Author csl-atlas/src/dicts/pwg.md as Tier A (full template, 8 sections).
Use the MW chapter (csl-atlas/src/dicts/mw.md) as the worked example.
Key PWG-specific facts to surface:
- 7 volumes, Boehtlingk+Roth 1855-75, ~570K <ls> citations, 4.6/record
  (~4x MW's density) - the contrast that motivates *block-economy the
  morphology* in PAPER.md §4.
- Named-kosha apparatus (top tags: SKDR. 20K, MED. 7K, H.an. 7K) - PWG
  is what MW collapsed into <ls>L.</ls>.
- 0 <ls>L.</ls> hedges - PWG's design choice was differentiation, not
  collapse.
- Type-citation spread 0.4 pts (uniform); MW spread 11.3 pts (selective).
- Successor: PWK is PWG's own abridgement.
- §6 cross-references: next=PWK, prior=MW.
Pull stats from analysis/CROSS_DICT_PROFILES.md PWG block; pull top sigla
from analysis/LS_HEDGE_CHECK.md.
```

**↓ Downshift to Sonnet when:** the chapter renders cleanly with no broken anchors and the Observable JS bar chart loads. Subsequent typo/link fixes are Haiku.

### O2 · CAE chapter (Tier B — compact + typography)

**Effort: ~2h** ([Decision 29 #6](decisions/MICROSITE.md), position 6 in the atlas)

```
Author csl-atlas/src/dicts/cae.md as Tier B (compact + typography
section). Key CAE-specific facts:
- Cappeller 1891, "A Sanskrit-English Dictionary, Based Upon the
  St. Petersburg Lexicons" (Strassburg, Truebner).
- 40,069 records, single-volume, 0 <ls> apparatus in digitisation.
- Uses asterisk * (1,370x) for "word taught only by grammarians or
  lexicographers" - the systematic typographic precedent for MW's
  <ls>L.</ls> per D21 three-stage lineage.
- Dagger † (903x) for "word that occurs only in a translation from
  Prakrit"; double-dagger combines both.
- Cappeller co-edited MW 1899 - direct lineage to position 1.
- §3a typography section is mandatory for this tier - quote Cappeller's
  preface verbatim from analysis/LS_HEDGE_CHECK.md §"Print-preface read".
- §6 cross-references: next=WIL, prior=BEN.
```

**↓ Downshift to Sonnet when:** the chapter renders. Authoring CAE *before* BEN per Decision 29 §29.4 (typographic-precedent finding is fresher).

### O3 · BEN chapter (Tier B — compact + typography)

**Effort: ~2h** ([Decision 29 #5](decisions/MICROSITE.md), position 5 in the atlas)

```
Author csl-atlas/src/dicts/ben.md as Tier B. Key BEN facts:
- Benfey 1866, "A Sanskrit-English Dictionary" (London, Longmans).
- 5,186 records, IE-cognate-heavy.
- Tagged source apparatus: 14,708 <ls> tags but 0 generic <ls>L.</ls>
  hedges (top: MBh. 2.5K, Ram. 2.3K, Man. 2.2K).
- §3a typography: 3 marker meanings - asterisk * = "fictitious forms"
  (Proto-IE convention, NOT a hedge precedent); dagger † = "verbs or
  meanings for which there are no authoritative references" (the actual
  weaker hedge precedent to MW); section § = compound position.
  Per D22 honesty: explicitly distinguish BEN * from CAE *.
- §6 cross-references: next=CAE, prior=AP.
```

**↓ Downshift to Sonnet when:** chapter complete + Plot bar renders.

### O4 · PWK chapter (Tier A — full template)

**Effort: ~2.5h** ([Decision 29 #3](decisions/MICROSITE.md), position 3 in the atlas)

```
Author csl-atlas/src/dicts/pwk.md as Tier A. Key PWK facts:
- Boehtlingk's *kuerzeres* PW 1879-89, the abridgement of PWG.
- 170,556 records (more than PWG's 123,366 - macrostructure expansion
  despite citation contraction).
- 86,750 <ls> tags, 0 <ls>L.</ls>, top tags GAL. 1.7K / OPP.CAT.1 1.7K /
  BURNELL,T. 1K - completely different sigla profile from PWG.
- Already dropped most kosha citations vs PWG (PWG H.an. 6.6K → PWK 0;
  PWG SKDR. 20.1K → PWK 0). The "missing link" between PWG (kosha-rich)
  and MW (<ls>L.</ls>-collapsed).
- Single-volume; type-citation spread 7.7 pts (between PWG 0.4 and
  MW 11.3) - confirms single-volume drives type-differentiation.
- §6 cross-references: next=AP, prior=BEN.
```

**↓ Downshift to Sonnet when:** chapter renders.

### O5 · AP chapter (Tier A — full template)

**Effort: ~2.5h** ([Decision 29 #4](decisions/MICROSITE.md), position 4 in the atlas)

```
Author csl-atlas/src/dicts/ap.md as Tier A. Key AP facts:
- Apte 1957 "Practical Sanskrit-English Dictionary" (modern successor;
  most recent in the CDSL bilingual set).
- 90,654 records, 62,656 <ls> tags, 1 <ls>L.</ls> (only AP and MW have
  any L. hedge at all in CDSL).
- Largest type-citation spread of any dict: 15.2 pts - the most
  selective differentiation.
- Sigla profile mixed: scholarly (MBh. 485, Pt.1 251, Subhas. 268) +
  Apte-specific (L.D.B. 393, Nm. 221, Tv. 304).
- Successor to MW conceptually but methodologically distinct (more
  prescriptive, fewer encyclopedic entries).
- §6 cross-references: next=BEN, prior=PWK.
```

**↓ Downshift to Sonnet when:** chapter renders.

### O6 · WIL chapter (Tier B — compact + typography)

**Effort: ~2h** ([Decision 29 #7](decisions/MICROSITE.md), position 7 in the atlas)

```
Author csl-atlas/src/dicts/wil.md as Tier B. Key WIL facts:
- Wilson 1832, "A Dictionary in Sanscrit and English" (Calcutta, 2nd
  edn). EARLIEST CDSL dict; the BASE from which European tradition
  departs.
- 44,577 records.
- 230 <ls> tags total, 224 of which are <ls>Rox.</ls> (Roxburgh
  botanical catalogue). NO systematic hedge convention attested in
  digital record OR (per D2/D21 audits) in print preface.
- Calcutta College compilation, Amarakosha-derived base word list.
- §3a typography (optional - the marker landscape is largely Roxburgh
  only, no hedge to discuss). Frame as "the base before the European
  apparatus was added."
- §6 cross-references: next=SKD, prior=AP.
```

**↓ Downshift to Sonnet when:** chapter renders.

### O7 · SKD chapter (Tier C — genre-bound)

**Effort: ~2.5h** ([Decision 29 #8](decisions/MICROSITE.md), position 8 in the atlas)

```
Author csl-atlas/src/dicts/skd.md as Tier C (genre-bound). Key SKD facts:
- Sabdakalpadruma 1822-58, Raja Radhakanta Deva's Calcutta encyclopedia.
  First Sanskrit-Sanskrit lexicon in the atlas - GENRE BOUNDARY.
- 42,531 records but NO <lex>, NO <ls> tags at all.
- Marks gender inline in Sanskrit ("X iti pumsi"); cites via inline
  "iti <source>" prose at 1.70 iti/record (MW ~0).
- §2-4 must replace the standard structure with prose-pattern analysis
  - the 18-block framework DOES NOT APPLY (the central finding of
  PAPER.md §8 cross-dict generalisation).
- §5 lineage: relation to Amarakosha, Hemachandra (the kosha tradition
  MW collapses into L.); SKD is the encyclopedic synthesis of the
  indigenous tradition.
- §6 cross-references: next=VCP, prior=WIL.
- Explicit "why-framework-does-not-transfer" section.
```

**↓ Downshift to Sonnet when:** chapter renders.

### O8 · VCP chapter (Tier C — genre-bound)

**Effort: ~2h** ([Decision 29 #9](decisions/MICROSITE.md), position 9 in the atlas)

```
Author csl-atlas/src/dicts/vcp.md as Tier C. Key VCP facts:
- Vacaspatya 1873-84, Taranatha Tarkavacaspati's encyclopedia. Second
  Sanskrit-Sanskrit lexicon - closes the atlas.
- 50,135 records (largest of the 9 dicts) but again no <lex>/<ls>.
- iti/record = 0.26 (less prose-heavy than SKD's 1.70 but same genre).
- §6 cross-references: next=(none), prior=SKD. FINAL chapter - close
  with an explicit "the framework stops here" summary linking back to
  PAPER.md §8 and §10 (CDSL framework is genre-bound to structured
  bilingual dicts).
- §7 decisions log should note that VCP being the *final* chapter
  carries the framework's outer limit (per Decision 29 ordering
  rationale).
```

**↓ Downshift to Sonnet when:** chapter renders and the atlas index.md is updated to reflect all 9 chapters being complete.

### O9 · Cross-chapter consistency pass

**Effort: ~1.5h** (after O1-O8 all complete)

```
After all 9 atlas chapters are authored, run a consistency pass:
- Every chapter's §6 ("Cross-references — divergence/convergence")
  table should match its adjacent chapter's §6.
- Every chapter's §7 (Decisions log) should consistently cite the same
  doubt resolutions (D17 kernel, D18 verbal-lemma promotion, D19
  effect-size, D21 three-stage lineage).
- Every chapter's §8 (data dictionary + reproducibility) should list
  matching script + JSON file paths.
- Numerical claims across chapters should agree (e.g. PWG's
  4.6 <ls>/record cited in MW chapter must match PWG's own chapter).
Produce a single audit report and apply fixes inline.
```

**↓ Downshift to Sonnet when:** the audit produces no findings on re-run.

### O10 · Atlas index.md + landing-page narrative refresh

**Effort: ~1.5h** (after all chapters)

```
Update csl-atlas/src/index.md to reflect the complete 9-chapter atlas:
- Landing-page narrative now includes the three-stage L.-hedge lineage
  finding (D21) as a teaser; previously the index had vague text.
- 9-dict grid (currently 9 cards but content is stub-quality) gets
  refreshed with one-line summaries from each chapter's §1 overview.
- Add a "How to read this atlas" 1-paragraph section: framework-fit
  first → typographic precedents → genre limit.
- Cross-link to the IJL paper (PAPER.md) and IJL_COVER_LETTER.md.
- Update the Russian locale routes if PAPER_RU.md gives an RU entry
  point (defer the RU-side rendering to Sonnet).
```

**↓ Downshift to Sonnet when:** index renders correctly and the 9-card grid pulls real data from each chapter.

---

## 3A. SONNET — Round 2: per-dict block-matrix exports

Each prompt produces or refreshes one `{code}_blocks.json` file in `csl-atlas/src/data/` and the corresponding per-dict block-heatmap PNG/SVG. Run after Haiku has refreshed the underlying data, before Opus uses the JSON to author the chapter.

### S1 · PWG block-matrix export

**Effort: ~45min**

```
Run papers/microanalysis/figures/scripts/export_dict_blocks.py for PWG.
Expected output: figures/data/pwg_blocks.json (already exists; verify
freshness against current csl-orig PWG data). Then copy to
csl-atlas/src/data/pwg_blocks.json and run render_heatmap.py with
--dict=PWG to produce a per-dict heatmap. Verify Plot.barX in
csl-atlas/src/dicts/pwg.md renders correctly with the new data.
```

### S2 · PWK block-matrix export

**Effort: ~45min**

```
Same as S1 but for PWK. NOTE the long-standing bug: csl_code='pw' but
file is pwk_blocks.json (per S6 of Round 1; bug fixed in load_blocks_json
to use meta['blocks_json']). Verify the filename is correct.
```

### S3 · AP90 block-matrix export

**Effort: ~45min**

```
Same as S1 but for AP90. NOTE: csl_code='ap90' but file is ap_blocks.json
(per S6 of Round 1 bug fix). Verify.
```

### S4 · BEN block-matrix export

**Effort: ~45min**

```
Same as S1 but for BEN. BEN has 14,708 <ls> tags but no <lex>; the
profile will look very different from MW/PWG. Expected: only "other"
type populated.
```

### S5 · CAE block-matrix export

**Effort: ~45min**

```
Same as S1 but for CAE. CAE has 0 <ls> tags (the typographic precedent
markers * and † are not tagged). Expected: zero citation column.
```

### S6 · WIL block-matrix export

**Effort: ~45min**

```
Same as S1 but for WIL. WIL has only 230 <ls> tags total (224 <ls>Rox.</ls>).
Expected: 0.9 pt type-citation spread (effectively no apparatus).
```

### S7 · SKD block-matrix export

**Effort: ~30min**

```
Same as S1 but for SKD. SKD has NO <lex>/<ls> tags at all - the
canonical export will produce mostly empty cells. Output should be
flagged as "framework-not-applicable" rather than zero-filled. Add a
field to the JSON: {"applicable": false, "reason": "Sanskrit-Sanskrit
lexicon; uses inline iti citation instead of tagged <ls>"}.
```

### S8 · VCP block-matrix export

**Effort: ~30min**

```
Same as S7 but for VCP. Same "applicable: false" flag. The Tier C
chapters (O7, O8) consume this differently from Tier A/B.
```

### S9 · Cross-dict aggregate refresh

**Effort: ~30min**

```
After S1-S8, re-run figures/scripts/export_cross_dict.py to refresh
csl-atlas/src/data/cross-dict.json. This is what the bar charts in
each chapter's §2 use. Verify the JSON has 9 dicts and all 9
common-block fields populated (zero for genre-bound dicts).
```

### S10 · Observable Plot rendering verification

**Effort: ~1h**

```
After all per-dict JSONs are refreshed, build the atlas locally
(npm run build in csl-atlas/) and verify every chapter's Plot.barX
loads. Specific check: SKD and VCP chapters render zero-bars
gracefully (not as broken charts). Push the build only if all 9
chapters render correctly.
```

---

## 4A. HAIKU — Round 2: manifest + figure regeneration for 9 dicts

All Haiku tasks are pure regeneration / verification. Run BEFORE Sonnet (cleans the source data Sonnet will export from).

### H1 · Re-run all per-dict figure renderers

**Effort: ~30min**

```
For each of the 9 dicts, run render_heatmap.py, render_treemap.py,
render_sankey.py (where applicable). Output: 9 sets of PNG + SVG +
.alt.txt + .desc.txt sidecars in figures/. Verify file counts vs
expected (9 dicts × 4 figure types × 4 file types = ~144 files).
```

### H2 · Regenerate alt-text + desc.txt sidecars

**Effort: ~20min**

```
For every figure in figures/, verify the .alt.txt and .desc.txt
sidecars exist. If missing or stale, regenerate via the *.py renderers
(they emit sidecars by default per Decision 14 accessibility policy).
```

### H3 · PNG ↔ SVG parity verification

**Effort: ~20min**

```
For each figure, verify the PNG and SVG render identically (same data,
same palette). The render scripts emit both; ensure no drift between
formats. Report any mismatches.
```

### H4 · Footer / version-stamp regeneration

**Effort: ~15min**

```
Per Decisions 26, 28: every figure has a footer with source + license +
Git SHA. After any docs-pass commit, the SHA in the footers is stale.
Re-run the renderers to refresh footers.
```

### H5 · Palette consistency check

**Effort: ~15min**

```
Verify figures/palette-tokens.json values match figures/palette.css and
figures/palette.py (the latter two are generated from the former).
Re-run figures/scripts/build_palette.py if drift detected.
```

### H6 · Locale string verification

**Effort: ~20min**

```
Verify figures/locales/en.json and figures/locales/ru.json have matching
key sets. Every chart label in en.json must have a corresponding ru.json
entry. Report missing keys; do NOT translate (that's Opus work).
```

### H7 · SUPPLEMENT_MANIFEST.md regeneration

**Effort: ~10min**

```
Run analysis/make_supplement.py. Verify ZIP integrity (file count,
size). Commit SUPPLEMENT_MANIFEST.md update if file list changed.
```

### H8 · ZIP integrity audit

**Effort: ~10min**

```
After H7, unzip the supplementary ZIP into /tmp and verify the unzipped
file count matches the manifest. Spot-check that paths in the manifest
resolve to real files.
```

### H9 · GitHub Actions status audit

**Effort: ~15min**

```
For sanskrit-lexicon/MWS and sanskrit-lexicon/csl-atlas, check the
most recent workflow runs. Report any failures, slow builds, or
deprecated action versions. One-page status table.
```

### H10 · Cross-repo link-rot scan

**Effort: ~30min**

```
Crawl every internal/external link in PAPER.md, IJL_COVER_LETTER.md,
PAPER_RU.md, DOUBTS.md, HANDOFF.md, all decisions/*.md, and all
csl-atlas chapter files. Report 404s and stale anchors. Do NOT fix
(that's Sonnet/Opus work); produce the audit report only.
```

---

## 2. OPUS 4.7 prompts — when judgment matters  *(Round 1 — complete 2026-05-27)*

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

## 3. SONNET 4.6 prompts — the workhorse tier  *(Round 1 — complete 2026-05-27)*

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

## 4. HAIKU 3.5 prompts — pure mechanics  *(Round 1 — complete 2026-05-27)*

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
