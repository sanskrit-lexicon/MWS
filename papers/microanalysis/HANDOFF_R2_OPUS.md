# HANDOFF_R2_OPUS — Round 2 Opus session (atlas chapters 2–9)

**Purpose:** let a fresh Claude Opus chat pick up Round 2 atlas authoring without losing context.

## Goal

Author the 8 remaining csl-atlas dict chapters following [Decision 29 ordering and template tiers](decisions/MICROSITE.md#decision-29--phase-4-dictionary-ordering-chapter-templates-minimum-data-added-2026-05-27). MW chapter (position 1) is already done as the worked example.

## Working dirs

- **Atlas source:** `D:/claude/csl-atlas/src/dicts/` — one `.md` per chapter; commit to `main`; push triggers GitHub Pages deploy
- **MWS docs:** `D:/claude/mws_repo/papers/microanalysis/` — paper, decisions, analysis
- **Live atlas:** https://sanskrit-lexicon.github.io/csl-atlas/

## Worked example

**[csl-atlas/src/dicts/mw.md](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/dicts/mw.md)** — 8-section Tier A chapter for MW. Use as template; copy and adapt per dict.

## Run order + status

| # | Code | Tier | Status | Source data |
|--:|---|---|---|---|
| 1 | MW | A | ✅ done (worked example) | `csl-atlas/src/dicts/mw.md` |
| **2** | **PWG** | **A** | **next** | [PWG/DICT_PROFILE.md](https://github.com/sanskrit-lexicon/PWG/blob/docs-pass/DICT_PROFILE.md) + [analysis/CROSS_DICT_PROFILES.md](analysis/CROSS_DICT_PROFILES.md) PWG block + [analysis/LS_HEDGE_CHECK.md](analysis/LS_HEDGE_CHECK.md) PWG section |
| 3 | CAE | B | pending | [LS_HEDGE_CHECK.md §"Print-preface read"](analysis/LS_HEDGE_CHECK.md#print-preface-read-added-2026-05-27-closes-the-digital-only-gap); D21 three-stage lineage |
| 4 | BEN | B | pending | LS_HEDGE_CHECK.md (Benfey 1866); D22 marker-distinction table |
| 5 | PWK | A | pending | CROSS_DICT_PROFILES.md PWK block; LS_HEDGE_CHECK.md PWK |
| 6 | AP | A | pending | CROSS_DICT_PROFILES.md AP block; AP has 1× `<ls>L.</ls>` (the only non-MW occurrence) |
| 7 | WIL | B | pending | LS_HEDGE_CHECK.md WIL section; D21 "no clear preface convention" |
| 8 | SKD | C | pending | CROSS_DICT_PROFILES.md Part B (genre-bound) |
| 9 | VCP | C | pending | CROSS_DICT_PROFILES.md Part B |
| O9 | — | — | after 1–8 | cross-chapter consistency pass |
| O10 | — | — | after O9 | atlas index.md refresh |

Authoring order (Decision 29 §29.4): PWG → CAE → BEN → PWK → AP → WIL → SKD → VCP. CAE/BEN drafted *before* AP because the typographic-precedent finding from O1/D21 is freshest.

## Template tiers (Decision 29 §29.2)

- **Tier A** (PWG, PWK, AP): full 8-section template — Overview · Profile table · Citation density · Hedge analysis · Lineage · Cross-refs · Decisions log · Data dictionary
- **Tier B** (BEN, CAE, WIL): compact — replace §2 with structural-features, add §3a typography for BEN/CAE
- **Tier C** (SKD, VCP): genre-bound — §2–4 become prose-pattern analysis; explicit "framework does not transfer" section

## Per-chapter must-include facts

### PWG (Tier A)
- Boehtlingk + Roth 1855–75; 7 volumes; 123,366 records; 570,817 `<ls>` tags (4.6/record, ~4× MW)
- Top sigla: `<ls>ŚKDR.</ls>` 20K · `<ls>MED.</ls>` 7K · `<ls>H. an.</ls>` 7K · `<ls>RĀJAN.</ls>` 6K · `<ls>ŚABDAR.</ls>` 3K
- 0 `<ls>L.</ls>` hedges — PWG's design choice was differentiation
- Type-citation spread: 0.4 pts (uniform)
- §6 next=PWK, prior=MW

### CAE (Tier B + typography)
- Cappeller 1891; 40,069 records; 0 `<ls>` apparatus
- Asterisk `*` 1,370× = "word taught only by grammarians or lexicographers" — systematic typographic precedent for `<ls>L.</ls>`
- Dagger `†` 903× = "word occurs only in translation from Prakrit"
- Cappeller co-edited MW 1899 → direct lineage
- §6 next=WIL, prior=BEN

### BEN (Tier B + typography)
- Benfey 1866; 5,186 records; 14,708 `<ls>` tags, 0 `<ls>L.</ls>`
- Top sigla: `<ls>MBh.</ls>` 2.5K · `<ls>Rām.</ls>` 2.3K · `<ls>Man.</ls>` 2.2K
- Typography (per D22 disambiguation): `*` = "fictitious forms" (Proto-IE, NOT hedge precedent); `†` = "no authoritative references" (weaker hedge precedent); `§` = compound position
- §6 next=CAE, prior=AP

### PWK (Tier A)
- Boehtlingk *kürzeres* PW 1879–89; 170,556 records; 86,750 `<ls>` tags; 0 `<ls>L.</ls>`
- Top sigla: `<ls>GAL.</ls>` 1.7K · `<ls>OPP. CAT. 1</ls>` 1.7K · `<ls>BURNELL, T.</ls>` 1K
- Dropped PWG's kosha apparatus: PWG `H. an.` 6.6K → PWK 0; PWG `ŚKDR.` 20K → PWK 0
- Type-citation spread: 7.7 pts (between PWG 0.4 and MW 11.3 — single-volume effect)
- §6 next=AP, prior=BEN

### AP (Tier A)
- Apte 1957; 90,654 records; 62,656 `<ls>` tags; **1× `<ls>L.</ls>`** (only AP and MW have any)
- Type-citation spread: **15.2 pts** (largest in CDSL)
- Top sigla: `<ls>Mb.</ls>` 485 · `<ls>L. D. B.</ls>` 393 · `<ls>Sk.</ls>` 391
- §6 next=BEN, prior=PWK

### WIL (Tier B; typography optional)
- Wilson 1832; 44,577 records; 230 `<ls>` tags total — 224 are `<ls>Rox.</ls>`
- No systematic hedge convention in digital record OR (per D2/D21) preface
- Calcutta College, Amarakośa-derived base
- §6 next=SKD, prior=AP

### SKD (Tier C — genre-bound)
- *Śabdakalpadruma* 1822–58; Raja Radhakanta Deva; 42,531 records
- **No `<lex>`, no `<ls>` tags at all** — gender inline ("X iti puṁsi"), inline-iti citation at **1.70/record**
- §2–4 prose-pattern analysis (NOT block matrix)
- Lineage: encyclopedic synthesis of Amarakośa / Hemachandra tradition
- §6 next=VCP, prior=WIL

### VCP (Tier C — final chapter)
- *Vācaspatya* 1873–84; Tārānātha Tarkavācaspati; 50,135 records (largest)
- Same no-tags structure; inline-iti at 0.26/record (sparser than SKD)
- **FINAL chapter** — close with "framework stops here" linking back to PAPER.md §8, §10
- §6 next=(none), prior=SKD

## Run loop per chapter

```bash
cd D:/claude/csl-atlas
# 1. cp src/dicts/mw.md src/dicts/<code>.md   (then edit per spec)
# 2. Edit substantively — replace MW-specific text, update tables, add tier-specific sections
# 3. git add src/dicts/<code>.md
# 4. git -c commit.gpgsign=false commit -m "atlas: <CODE> chapter (Tier X)"
# 5. git push origin main   # triggers GitHub Pages deploy (~2 min)
```

After each chapter: update task status via TaskUpdate; update this handoff §"Run order + status" table.

## Existing data on disk (do NOT re-derive)

- **Per-dict block JSONs**: `csl-atlas/src/data/{mw,pwg,pwk,ap,wil,ben,cae,skd,vcp}_blocks.json` — already exist from prior Sonnet work
- **Cross-dict aggregate**: `csl-atlas/src/data/cross-dict.json`
- **Locale strings**: `csl-atlas/src/data/locales/{en,ru}.json` (Russian reviewed in Round 1 O4)

## Cross-references between chapters

Each chapter's §6 "Cross-references — divergence/convergence" must agree with the *adjacent* chapter's §6. After all 8 are authored, O9 runs a consistency audit.

## Acceptance criteria per chapter

- [ ] 8 sections per Tier (or modified for Tier B/C)
- [ ] All `<ls>` tags + counts hyperlinked to `analysis/LS_HEDGE_CHECK.md`
- [ ] Lineage statement links to `DICT_PROFILE.md` of the same repo
- [ ] Decisions log references D17, D18, D19, D21 where relevant
- [ ] Data-dictionary §8 lists script paths + JSON file paths
- [ ] Plot.barX block uses `cross.dicts.find(d => d.code === "X")` pattern
- [ ] Committed + pushed to `csl-atlas/main`

## Key linkable docs (paste into any prompt)

- [MWS PAPER.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md)
- [MWS DOUBTS.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/DOUBTS.md)
- [analysis/LS_HEDGE_CHECK.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/LS_HEDGE_CHECK.md)
- [analysis/CROSS_DICT_PROFILES.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/CROSS_DICT_PROFILES.md)
- [Decision 29](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/decisions/MICROSITE.md#decision-29--phase-4-dictionary-ordering-chapter-templates-minimum-data-added-2026-05-27)
- [MW chapter (worked example)](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/dicts/mw.md)

## When stuck

- Section structure unclear → re-read MW chapter
- Per-dict facts unclear → re-read `analysis/CROSS_DICT_PROFILES.md` + `analysis/LS_HEDGE_CHECK.md`
- Atlas not rendering → `cd csl-atlas && npm run build` locally
- GitHub Pages deploy failing → check `csl-atlas/.github/workflows/build-and-deploy.yml`

## End-of-session

After all chapters done (or session running out):

1. Update §"Run order + status" table here
2. Commit + push `papers/microanalysis/HANDOFF_R2_OPUS.md` to MWS docs-pass
3. The next chat starts by reading this file top to bottom

---

*Last updated: 2026-05-27 (session start). Authoring begins with O1 PWG.*
