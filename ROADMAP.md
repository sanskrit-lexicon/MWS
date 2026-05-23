# MWS Roadmap

Distillation of (a) the 34 open issues in [MWS](https://github.com/sanskrit-lexicon/MWS/issues),
(b) the 157 historically closed issues for velocity context, and (c) the gaps
surfaced by the [2026-05 markup-fix audit](https://github.com/sanskrit-lexicon/MWS/blob/markup-fix-audit/mwissues/markup_fix/markup_audit.txt)
and the [2026-05-23 docs-pass review](https://github.com/sanskrit-lexicon/MWS/issues/195),
into one planning document.

---

## Status snapshot (2026-05-23)

| Metric | Value |
|---|--:|
| Records in [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) | [286,561](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#entry-hierarchy-distribution) |
| Open issues | [34](https://github.com/sanskrit-lexicon/MWS/issues) |
| Closed issues (historical) | [157](https://github.com/sanskrit-lexicon/MWS/issues?q=is%3Aclosed) |
| Closed in last 12 months (velocity signal) | **4** |
| `<ls>` citations | [311,932](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#coverage-of-ls-citations) |
| Unique `<ls>` abbreviations | [821](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#coverage-of-ls-citations) |
| With [authority record](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) | 232 (28.3%) — covering 64.0% of citations |
| Vedic accent coverage | [16.6% of `<k2>` fields](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#vedic-accent-coverage) |
| `<ls>L.</ls>` lexicographer hedges | [40,213 (12.9% of all citations)](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md#citation-markers--not-all-are-literary-works) |

**Velocity note:** Only 4 issues closed in the last 12 months. Roadmap throughput
assumes ≤ 1 issue/month routinely + bursts when a maintainer is active. Long-running
items must be self-contained and resumable.

---

## Task subtypes — 10 categories

Each subtype maps to an existing GitHub issue template (or proposes a new one).
Effort buckets: **micro** (single entry, ~10 min) · **small** (batch, 1–3 h) ·
**medium** (subsystem, 1–5 d) · **large** (months) · **xl** (years).

### 1. Text correction — typos, wrong glosses

| Field | Value |
|---|---|
| Template | [text-correction.yml](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/.github/ISSUE_TEMPLATE/text-correction.yml) |
| Effort per item | **micro** |
| Historical closed | 46 |
| Open | [#192](https://github.com/sanskrit-lexicon/MWS/issues/192), [#183](https://github.com/sanskrit-lexicon/MWS/issues/183) |
| Workflow | [Multi-step temp_mw_N.txt](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/CONTRIBUTING.md#correction-workflow-per-issue) |

**Backlog beyond open issues:** the markup-fix audit catalogue (mwissues/markup_fix/markup_audit.txt) has dozens more candidates already documented. Pull from the audit file for steady work.

### 2. Markup refinement — tag content / structure

| Field | Value |
|---|---|
| Template | [markup.yml](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/.github/ISSUE_TEMPLATE/markup.yml) |
| Effort per item | **small** (one tag-class at a time) |
| Historical closed | 44 |
| Open | [#194](https://github.com/sanskrit-lexicon/MWS/issues/194), [#181](https://github.com/sanskrit-lexicon/MWS/issues/181), [#178](https://github.com/sanskrit-lexicon/MWS/issues/178), [#172](https://github.com/sanskrit-lexicon/MWS/issues/172), [#168](https://github.com/sanskrit-lexicon/MWS/issues/168), [#162](https://github.com/sanskrit-lexicon/MWS/issues/162), [#147](https://github.com/sanskrit-lexicon/MWS/issues/147), [#73](https://github.com/sanskrit-lexicon/MWS/issues/73) |

**Sub-categories:**
| Sub-category | Open issues | Notes |
|---|---|---|
| Alternate-form tagging | [#178 (AB3)](https://github.com/sanskrit-lexicon/MWS/issues/178), [#147 (new markup)](https://github.com/sanskrit-lexicon/MWS/issues/147), [#73 (display variant 2)](https://github.com/sanskrit-lexicon/MWS/issues/73) | Probably a single coordinated proposal |
| Titular abbreviation | [#172](https://github.com/sanskrit-lexicon/MWS/issues/172) | Distinguish title-citations from textual citations |
| `<ab n="…">` / `<ls>` side-effects | [#162](https://github.com/sanskrit-lexicon/MWS/issues/162) | Tooling issue — affects display |
| Grassmanizing / Vedic | [#181](https://github.com/sanskrit-lexicon/MWS/issues/181) | Cross-reference with [GRA](https://github.com/sanskrit-lexicon/GRA); link to [Vedic accent coverage section](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#vedic-accent-coverage) |
| Tag inventory | [#168](https://github.com/sanskrit-lexicon/MWS/issues/168) | Now partially answered by [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DATA_DICTIONARY.md) and [ENTRY_GUIDE common tags](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#common-tags) — can be closed or rescoped |
| Minor mw.txt oddities | [#194](https://github.com/sanskrit-lexicon/MWS/issues/194) | Catch-all bucket |

### 3. Encoding / transcoding

| Field | Value |
|---|---|
| Template | [encoding.yml](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/.github/ISSUE_TEMPLATE/encoding.yml) |
| Effort per item | **small** |
| Historical closed | 8 |
| Open | [#155](https://github.com/sanskrit-lexicon/MWS/issues/155) (IAST → ISO 15919 migration?), [#90](https://github.com/sanskrit-lexicon/MWS/issues/90) (transcoding versions doc) |

[#155](https://github.com/sanskrit-lexicon/MWS/issues/155) is large if accepted — affects every Sanskrit display. Probably a decision-issue, not a code-issue. [#90](https://github.com/sanskrit-lexicon/MWS/issues/90) is a docs item now partly addressed by the docs-pass branch.

### 4. Link target — scan URLs for `<ls>` citations

| Field | Value |
|---|---|
| Template | [link-target.yml](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/.github/ISSUE_TEMPLATE/link-target.yml) |
| Effort per item | **small–medium** (locate scan, verify pagination) |
| Historical closed | 7 |
| Open | [#187 (Mālavikāgnimitra)](https://github.com/sanskrit-lexicon/MWS/issues/187), [#185 (Pañcatantra)](https://github.com/sanskrit-lexicon/MWS/issues/185), [#186 (Śākuntala)](https://github.com/sanskrit-lexicon/MWS/issues/186), [#129 (RV ib. viii, 103, 10)](https://github.com/sanskrit-lexicon/MWS/issues/129) |

**Strategic gap (NEW from docs-pass analysis):** 589 of 821 unique `<ls>` abbreviations have **no authority record at all**. The [top orphans by citation count](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#top-orphan-abbreviations) — Pāṇ. (8,527), ŚBr. (7,029), Kathās. (6,757), Suśr. (6,200), Kāv. (4,667), VarBṛS. (3,467), Rājat. (3,410), Pañcat. (2,670), Ragh. (2,654), KātyŚr. (2,537), Yājñ. (2,249) — would, if completed, jump authority coverage from 64.0% to ~85% of citations.

This is **the highest-leverage open work** because each new authority record unlocks scan-link click-through for thousands of citations at once.

### 5. Scholarly question — needs research

| Field | Value |
|---|---|
| Template | [question.yml](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/.github/ISSUE_TEMPLATE/question.yml) |
| Effort per item | **variable** (research-heavy) |
| Historical closed | 17 |
| Open | [#189 (Mn. links oddity)](https://github.com/sanskrit-lexicon/MWS/issues/189), [#179 (RV. viii, 85, 3 author identity)](https://github.com/sanskrit-lexicon/MWS/issues/179), [#45 (cf. accord. to some)](https://github.com/sanskrit-lexicon/MWS/issues/45) |

### 6. Bug fix

| Field | Value |
|---|---|
| Template | [bug.yml](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/.github/ISSUE_TEMPLATE/bug.yml) |
| Effort per item | **small** |
| Historical closed | 17 |
| Open | [#86 (&c. abbreviation)](https://github.com/sanskrit-lexicon/MWS/issues/86), [#61 (PDF page in Firefox)](https://github.com/sanskrit-lexicon/MWS/issues/61) |

### 7. Content enhancement — new tagging, navigation, display

| Field | Value |
|---|---|
| Template | enhancement label + content-enhancement label (no dedicated template) |
| Effort per item | **medium–large** |
| Historical closed | 14 |
| Open | [#180](https://github.com/sanskrit-lexicon/MWS/issues/180), [#170](https://github.com/sanskrit-lexicon/MWS/issues/170), [#163](https://github.com/sanskrit-lexicon/MWS/issues/163), [#154](https://github.com/sanskrit-lexicon/MWS/issues/154), [#108](https://github.com/sanskrit-lexicon/MWS/issues/108), [#98](https://github.com/sanskrit-lexicon/MWS/issues/98), [#76](https://github.com/sanskrit-lexicon/MWS/issues/76), [#75](https://github.com/sanskrit-lexicon/MWS/issues/75), [#74](https://github.com/sanskrit-lexicon/MWS/issues/74), [#64](https://github.com/sanskrit-lexicon/MWS/issues/64), [#37](https://github.com/sanskrit-lexicon/MWS/issues/37), [#24](https://github.com/sanskrit-lexicon/MWS/issues/24) |

**Sub-categories:**

| Sub-category | Open issues | Effort | Notes |
|---|---|---|---|
| Inflection & morphology | [#76 (kāraka dependency)](https://github.com/sanskrit-lexicon/MWS/issues/76), [#75 (verbs01)](https://github.com/sanskrit-lexicon/MWS/issues/75) | **large** | Multi-month projects; depends on [csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect) |
| Cross-entry navigation | [#64 (cross-entry links)](https://github.com/sanskrit-lexicon/MWS/issues/64), [#98 (resolving idems)](https://github.com/sanskrit-lexicon/MWS/issues/98) | **medium** | "Resolve `id.` to the preceding sense" — would close 4,401 `id.` instances |
| Display improvements | [#170 (web font for IAST)](https://github.com/sanskrit-lexicon/MWS/issues/170), [#108 (genders in bold)](https://github.com/sanskrit-lexicon/MWS/issues/108), [#37 (UI)](https://github.com/sanskrit-lexicon/MWS/issues/37), [#180 (vertical scrolls)](https://github.com/sanskrit-lexicon/MWS/issues/180) | **medium** | Most are CDSL-wide; coordinate with [csl-app](https://github.com/sanskrit-lexicon/csl-app) |
| Headword expansion | [#154 (feminine of masculine)](https://github.com/sanskrit-lexicon/MWS/issues/154), [#163 (grouped entries like GRA)](https://github.com/sanskrit-lexicon/MWS/issues/163) | **medium** | Mirrors [GRA](https://github.com/sanskrit-lexicon/GRA) headword-grouping pattern |
| Source-data exports | [#74 (bot listing)](https://github.com/sanskrit-lexicon/MWS/issues/74), [#24 (proper names in SLP1)](https://github.com/sanskrit-lexicon/MWS/issues/24) | **medium** | The [8,923 `<bot>` tags](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#botanical--biographical-tag-stats) are ripe for export as a standalone botanical glossary |

### 8. NEW — Authority record completion

| Field | Value |
|---|---|
| Template | **proposed new: `authority-record.yml`** |
| Effort per item | small (one record per work) |
| Open | 0 (this is a *new* category — not yet ticketed) |
| Scope | 589 orphan abbreviations; top-25 covers ~80% of citations |

See section 4 above for the top-orphan list. Each record fills the three [`linkmwauthorities_init.txt`](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/linkmwauthorities_init.txt) columns (in-text abbreviation · occurrence count · authority abbreviation) and ideally adds a scan URL.

**Recommended:** open one issue per top-orphan, each with a `link-target` + new `authority-record` label.

### 9. NEW — Vedic accent expansion

| Field | Value |
|---|---|
| Effort | **large** — page-by-page proof-checking |
| Current coverage | [16.6% of `<k2>` fields](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#vedic-accent-coverage) (47,598 of 286,561) |
| Open | none directly, but [#181 Grassmanizing](https://github.com/sanskrit-lexicon/MWS/issues/181) is adjacent |

Many more accents are visible in the 1899 print (verifiable against [archive.org facsimile](https://archive.org/details/sanskritenglish00moniuoft)) but not transcribed. Compare against [Grassmann's RV-Wörterbuch (GRA)](https://github.com/sanskrit-lexicon/GRA) for Vedic-specific entries.

### 10. NEW — `<ls>L.</ls>` verification — crowd candidate

| Field | Value |
|---|---|
| Effort | **xl** — text-by-text verification |
| Scope | [40,213 lexicographer-only citations (12.9%)](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md#citation-markers--not-all-are-literary-works) |
| Crowd potential | high (each citation is independent; small unit of work) |
| Open | none directly, but [#74 (bot listing crowd)](https://github.com/sanskrit-lexicon/MWS/issues/74) labels with `crowd` |

Each `<ls>L.</ls>` entry could in principle be checked against (a) [BHS](https://github.com/sanskrit-lexicon/BHS) for Buddhist Hybrid Sanskrit attestations MW didn't have, (b) recent corpora (DCS, GRETIL) for any textual attestation, (c) other indigenous lexicons. Verified citations get upgraded to a real `<ls>` source.

---

## Cross-repo dependencies

| Repo | Why it affects MWS roadmap |
|---|---|
| [csl-orig](https://github.com/sanskrit-lexicon/csl-orig) | Canonical [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) lives here — all text corrections eventually commit here |
| [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork) | Build pipeline ([sqlite.py](https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/makotemplates/pywork/sqlite/sqlite.py), [generate_dict.sh](https://github.com/sanskrit-lexicon/csl-pywork)) — schema/output changes affect MW |
| [csl-app](https://github.com/sanskrit-lexicon/csl-app) | Web display — UI improvements ([#37](https://github.com/sanskrit-lexicon/MWS/issues/37), [#170](https://github.com/sanskrit-lexicon/MWS/issues/170)) land here |
| [csl-sqlite](https://github.com/sanskrit-lexicon/csl-sqlite) | Distribution — release cadence matters for downstream users |
| [csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect) | Inflection tables — [#75](https://github.com/sanskrit-lexicon/MWS/issues/75), [#76](https://github.com/sanskrit-lexicon/MWS/issues/76) depend on this |
| [csl-homepage](https://github.com/sanskrit-lexicon/csl-homepage) | Where the [docs hub](https://github.com/sanskrit-lexicon/csl-homepage) for org-wide docs lives |
| [mwauthorities/](https://github.com/sanskrit-lexicon/MWS/tree/master/mwauthorities) | Subdirectory of this repo — work in section 8 lands here |

---

## Quarterly view (suggested cadence at ~1 issue/month)

### Q1 (next 3 months — 2026 Jun–Aug)

**Focus: close the docs-pass review and tackle high-leverage authority records.**

- [ ] Review and merge docs-pass branch ([#195](https://github.com/sanskrit-lexicon/MWS/issues/195))
- [ ] Add 2–3 top-orphan authority records (Pāṇ., ŚBr., Kathās.) — each unlocks ~7K+ citations
- [ ] Close [#168 (tag inventory)](https://github.com/sanskrit-lexicon/MWS/issues/168) — superseded by [DATA_DICTIONARY](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DATA_DICTIONARY.md)
- [ ] Close [#90 (transcoding versions doc)](https://github.com/sanskrit-lexicon/MWS/issues/90) — superseded by [ENTRY_GUIDE Encoding section](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md#encoding)
- [ ] Address [#192](https://github.com/sanskrit-lexicon/MWS/issues/192) and [#183](https://github.com/sanskrit-lexicon/MWS/issues/183) (text corrections — quick wins)
- [ ] Address [#86 (&c. abbreviation bug)](https://github.com/sanskrit-lexicon/MWS/issues/86) (single-abbreviation fix)

### Q2 (2026 Sep–Nov)

**Focus: markup refinement consolidation.**

- [ ] Resolve markup cluster: [#178](https://github.com/sanskrit-lexicon/MWS/issues/178), [#147](https://github.com/sanskrit-lexicon/MWS/issues/147), [#73](https://github.com/sanskrit-lexicon/MWS/issues/73) (alternate-form proposal) — single coordinated decision
- [ ] [#172 (titular abbreviation)](https://github.com/sanskrit-lexicon/MWS/issues/172) — decision + apply
- [ ] [#194 (minor mw.txt oddities)](https://github.com/sanskrit-lexicon/MWS/issues/194) — sweep the catalogue
- [ ] Add 3 more authority records (Suśr., Kāv., VarBṛS.)
- [ ] Add link-targets: [#185](https://github.com/sanskrit-lexicon/MWS/issues/185), [#186](https://github.com/sanskrit-lexicon/MWS/issues/186), [#187](https://github.com/sanskrit-lexicon/MWS/issues/187)

### Q3 (2026 Dec – 2027 Feb)

**Focus: scholarly questions + Grassmanizing.**

- [ ] [#189 (Mn. links oddity)](https://github.com/sanskrit-lexicon/MWS/issues/189)
- [ ] [#179 (RV. viii, 85, 3 author)](https://github.com/sanskrit-lexicon/MWS/issues/179)
- [ ] [#45 (cf. accord. to some)](https://github.com/sanskrit-lexicon/MWS/issues/45)
- [ ] [#181 (Grassmanizing)](https://github.com/sanskrit-lexicon/MWS/issues/181) — coordinate with [GRA](https://github.com/sanskrit-lexicon/GRA)
- [ ] Add 3 more authority records (Rājat., Pañcat., Ragh.)
- [ ] [#129](https://github.com/sanskrit-lexicon/MWS/issues/129) link-target

### Long-running (multi-quarter)

- [ ] **#98 (resolve `id.` to preceding sense)** — would close 4,401 unresolved cross-references; needs algorithmic approach
- [ ] **#64 (cross-entry links in MW)** — needs algorithm + display work in [csl-app](https://github.com/sanskrit-lexicon/csl-app)
- [ ] **#76 (kāraka dependency)** — research project; depends on [csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect)
- [ ] **#75 (verbs01)** — verbal-form expansion; large
- [ ] **#163 (grouped entries like GRA)** — restructure
- [ ] **#108, #170, #37, #180 (display improvements)** — bundle into a single UX pass in [csl-app](https://github.com/sanskrit-lexicon/csl-app)
- [ ] **#74 (botanical listing)** — crowd-friendly; 8,923 `<bot>` tags ready for extraction
- [ ] **#24 (proper names in SLP1)** — affects all `<s1>` and `<bio>` tags
- [ ] **#154 (feminine of masculine)** — headword expansion

### Strategic / undated

- [ ] **Authority record completion** — top-25 covers ~80% of citations (sections 4, 8)
- [ ] **Vedic accent expansion** beyond 16.6% (section 9)
- [ ] **`<ls>L.</ls>` verification** at 40,213 citations (section 10)
- [ ] **[#155 IAST → ISO 15919 migration](https://github.com/sanskrit-lexicon/MWS/issues/155)** — large, decision-blocked

---

## Issue → roadmap map (complete)

| Issue | Title (truncated) | Category | Effort | Quarter |
|---|---|---|---|---|
| [#195](https://github.com/sanskrit-lexicon/MWS/issues/195) | docs-pass | Documentation | small | Q1 |
| [#194](https://github.com/sanskrit-lexicon/MWS/issues/194) | Minor mw.txt markup oddities | Markup | small | Q2 |
| [#192](https://github.com/sanskrit-lexicon/MWS/issues/192) | kararudh / karagṛhīti correction | Text correction | micro | Q1 |
| [#189](https://github.com/sanskrit-lexicon/MWS/issues/189) | Mn. links oddity | Question | medium | Q3 |
| [#187](https://github.com/sanskrit-lexicon/MWS/issues/187) | Mālavikāgnimitra link target | Link target | small | Q2 |
| [#186](https://github.com/sanskrit-lexicon/MWS/issues/186) | Śākuntala link target | Link target | small | Q2 |
| [#185](https://github.com/sanskrit-lexicon/MWS/issues/185) | Pañcatantra link target | Link target | small | Q2 |
| [#183](https://github.com/sanskrit-lexicon/MWS/issues/183) | tādṛśī / tādṛśa f. headword | Text correction | micro | Q1 |
| [#181](https://github.com/sanskrit-lexicon/MWS/issues/181) | Grassmanizing | Markup (Vedic) | medium | Q3 |
| [#180](https://github.com/sanskrit-lexicon/MWS/issues/180) | Eliminate vertical scrolls | Content (display) | medium | Long |
| [#179](https://github.com/sanskrit-lexicon/MWS/issues/179) | RV. viii, 85, 3 poet | Question | medium | Q3 |
| [#178](https://github.com/sanskrit-lexicon/MWS/issues/178) | AB3 alternate form | Markup (alt-form) | small | Q2 |
| [#172](https://github.com/sanskrit-lexicon/MWS/issues/172) | Titular abbreviations | Markup | small | Q2 |
| [#170](https://github.com/sanskrit-lexicon/MWS/issues/170) | Web font for IAST | Content (display) | medium | Long |
| [#168](https://github.com/sanskrit-lexicon/MWS/issues/168) | Tag inventory | Markup (docs) | micro | Q1 (close) |
| [#163](https://github.com/sanskrit-lexicon/MWS/issues/163) | Grouped entries like GRA | Content (headword) | large | Long |
| [#162](https://github.com/sanskrit-lexicon/MWS/issues/162) | `<ab n=>`/`<ls>` side-effects | Markup (tooling) | medium | Q2 |
| [#155](https://github.com/sanskrit-lexicon/MWS/issues/155) | IAST → ISO 15919 | Encoding | large | Strategic |
| [#154](https://github.com/sanskrit-lexicon/MWS/issues/154) | siṃhī for siṃha | Content (headword) | medium | Long |
| [#147](https://github.com/sanskrit-lexicon/MWS/issues/147) | New markup for alternates | Markup (alt-form) | small | Q2 |
| [#129](https://github.com/sanskrit-lexicon/MWS/issues/129) | Missing link ib. viii, 103, 10 | Link target | small | Q3 |
| [#108](https://github.com/sanskrit-lexicon/MWS/issues/108) | Genders in bold | Content (display) | medium | Long |
| [#98](https://github.com/sanskrit-lexicon/MWS/issues/98) | Resolving idems | Content (xref) | large | Long |
| [#90](https://github.com/sanskrit-lexicon/MWS/issues/90) | Transcoding versions | Documentation | micro | Q1 (close) |
| [#86](https://github.com/sanskrit-lexicon/MWS/issues/86) | &c. abbreviation | Bug | small | Q1 |
| [#76](https://github.com/sanskrit-lexicon/MWS/issues/76) | kāraka dependency | Content (inflect) | large | Long |
| [#75](https://github.com/sanskrit-lexicon/MWS/issues/75) | verbs01 | Content (inflect) | large | Long |
| [#74](https://github.com/sanskrit-lexicon/MWS/issues/74) | bot listing | Content (export) | medium | Long (crowd) |
| [#73](https://github.com/sanskrit-lexicon/MWS/issues/73) | MW display variant pt 2 | Markup (alt-form) | small | Q2 |
| [#64](https://github.com/sanskrit-lexicon/MWS/issues/64) | Cross-entry links | Content (xref) | large | Long |
| [#61](https://github.com/sanskrit-lexicon/MWS/issues/61) | PDF page in Firefox | Bug | small | Q2 |
| [#45](https://github.com/sanskrit-lexicon/MWS/issues/45) | cf. accord. to some | Question | medium | Q3 |
| [#37](https://github.com/sanskrit-lexicon/MWS/issues/37) | UI improvements | Content (display) | medium | Long |
| [#24](https://github.com/sanskrit-lexicon/MWS/issues/24) | Proper names in SLP1 | Content (display) | medium | Long |

---

## Possible new issue templates

Based on the categories that recur in the open backlog but lack a dedicated template:

| Proposed template | Replaces what's currently labelled… | Why |
|---|---|---|
| `content-enhancement.yml` | `enhancement` + `content-enhancement` (mixed) | 12 open + 14 historical: needs a structured form (scope, affected entries, display vs data, crowd-friendly y/n) |
| `authority-record.yml` | (no current label) | High-leverage work surfaced by docs-pass; 589 orphan abbreviations |
| `inflection.yml` | `enhancement` (#75, #76) | Distinct from general content; depends on [csl-inflect](https://github.com/sanskrit-lexicon/csl-inflect) |

---

## How this roadmap is maintained

- **Updated:** after every wave of issue closures or new strategic finding.
- **Source of truth for status:** GitHub issues themselves (this doc *summarizes*).
- **Effort estimates:** intentionally coarse — they're for planning, not commitments.
- **Velocity assumption:** ≤ 1 issue/month sustained; bursts when a maintainer is active.
- **Owners:** @funderburkjim and @Andhrabharati are the primary maintainers; @gasyoun coordinates with related repos and the docs-pass project.

Cross-link: this roadmap is part of the [org-wide docs-pass](https://github.com/sanskrit-lexicon/COLOGNE) and complements [DICT_PROFILE.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md), [ENTRY_GUIDE.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md), and [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DATA_DICTIONARY.md).
