#!/usr/bin/env python3
"""Push ROADMAP.md to PWG docs-pass branch (S7)."""
import base64, json, os, subprocess, sys, tempfile
sys.stdout.reconfigure(encoding='utf-8')

ORG = 'sanskrit-lexicon'
REPO = 'PWG'
BRANCH = 'docs-pass'

ROADMAP = """\
# PWG Roadmap

Distillation of (a) the ~53 open issues in [PWG](https://github.com/sanskrit-lexicon/PWG/issues),
(b) the ~125 historically closed issues for velocity context, and (c) the gaps
surfaced by the [2026-05-27 docs-pass review](https://github.com/sanskrit-lexicon/PWG/issues/179),
into one planning document.

---

## Status snapshot (2026-05-27)

| Metric | Value |
|---|--:|
| Records in [pwg.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt) | 123,366 |
| Open issues | [~53](https://github.com/sanskrit-lexicon/PWG/issues) |
| Closed issues (historical) | [~125](https://github.com/sanskrit-lexicon/PWG/issues?q=is%3Aclosed) |
| Closed in last 12 months (velocity signal) | **~18** |
| `<ls>` citations/record | 4.63 (highest among CDSL structured bilingual dicts) |
| Block profile data | [`pwg_blocks.json`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/data/pwg_blocks.json) |

**Velocity note:** ~18 issues closed in the last 12 months, primarily link-targets.
PWG is actively maintained by @funderburkjim and @Andhrabharati with a steady rhythm
of ~1–2 link-target completions per month. The large content-enhancement items (#163, #61, #37)
require maintainer consensus before work begins.

---

## Task subtypes — 9 categories

### 1. Link target — scan URLs for `<ls>` citations

| Field | Value |
|---|---|
| Effort per item | **small** (locate scan, verify pagination) |
| Historical closed | ~60 |
| Open | [#173](https://github.com/sanskrit-lexicon/PWG/issues/173), [#167](https://github.com/sanskrit-lexicon/PWG/issues/167), [#162](https://github.com/sanskrit-lexicon/PWG/issues/162), [#159](https://github.com/sanskrit-lexicon/PWG/issues/159), [#158](https://github.com/sanskrit-lexicon/PWG/issues/158), [#156](https://github.com/sanskrit-lexicon/PWG/issues/156), [#150](https://github.com/sanskrit-lexicon/PWG/issues/150), [#139](https://github.com/sanskrit-lexicon/PWG/issues/139), [#137](https://github.com/sanskrit-lexicon/PWG/issues/137), [#118](https://github.com/sanskrit-lexicon/PWG/issues/118), [#94](https://github.com/sanskrit-lexicon/PWG/issues/94), [#60](https://github.com/sanskrit-lexicon/PWG/issues/60), [#57](https://github.com/sanskrit-lexicon/PWG/issues/57), [#49](https://github.com/sanskrit-lexicon/PWG/issues/49), [#42](https://github.com/sanskrit-lexicon/PWG/issues/42), [#41](https://github.com/sanskrit-lexicon/PWG/issues/41) |

**This is the dominant work type for PWG.** With 4.63 `<ls>` citations/record (highest among all
structured bilingual CDSL dicts), PWG has hundreds of source abbreviations requiring scan-link
resolution. The link-target pattern is well-established: each issue covers one or a few sources,
locates the scan, and patches the link authority file.

Most link-target work is **self-contained and independently resumable** — ideal for a contributor
picking up a single issue.

### 2. Link splitting — combined-page references

| Field | Value |
|---|---|
| Effort per item | **small** (regex pattern + batch apply) |
| Historical closed | ~10 |
| Open | [#172](https://github.com/sanskrit-lexicon/PWG/issues/172), [#145](https://github.com/sanskrit-lexicon/PWG/issues/145), [#142](https://github.com/sanskrit-lexicon/PWG/issues/142), [#133](https://github.com/sanskrit-lexicon/PWG/issues/133), [#74](https://github.com/sanskrit-lexicon/PWG/issues/74) |

References in PWG often cite multiple pages as combined strings (e.g. `YĀJÑ. I, 3; II, 7`).
These need splitting into individual per-page links so each citation is independently clickable.

### 3. Markup refinement — tag content / structure

| Field | Value |
|---|---|
| Effort per item | **small–medium** |
| Historical closed | ~20 |
| Open | [#175](https://github.com/sanskrit-lexicon/PWG/issues/175), [#178](https://github.com/sanskrit-lexicon/PWG/issues/178), [#116](https://github.com/sanskrit-lexicon/PWG/issues/116), [#111](https://github.com/sanskrit-lexicon/PWG/issues/111), [#107](https://github.com/sanskrit-lexicon/PWG/issues/107), [#106](https://github.com/sanskrit-lexicon/PWG/issues/106), [#91](https://github.com/sanskrit-lexicon/PWG/issues/91), [#85](https://github.com/sanskrit-lexicon/PWG/issues/85), [#51](https://github.com/sanskrit-lexicon/PWG/issues/51), [#47](https://github.com/sanskrit-lexicon/PWG/issues/47) |

**Sub-categories:**

| Sub-category | Open issues | Notes |
|---|---|---|
| `<ls>` markup | [#51](https://github.com/sanskrit-lexicon/PWG/issues/51), [#116](https://github.com/sanskrit-lexicon/PWG/issues/116), [#91](https://github.com/sanskrit-lexicon/PWG/issues/91), [#85](https://github.com/sanskrit-lexicon/PWG/issues/85) | Largest class — `<ls>` tag normalization across the 7-vol corpus |
| Titular references | [#107](https://github.com/sanskrit-lexicon/PWG/issues/107), [#106](https://github.com/sanskrit-lexicon/PWG/issues/106) | Unresolved questions about commentarial + titular citation style |
| Minor markup oddities | [#175](https://github.com/sanskrit-lexicon/PWG/issues/175), [#178](https://github.com/sanskrit-lexicon/PWG/issues/178) | General catch-all; #178 = part 2 of earlier batch |
| `<lex>` gaps | [#91](https://github.com/sanskrit-lexicon/PWG/issues/91) | Instrumental/genitive dual forms missing `<lex>` |
| `<ls>?` bug | [#47](https://github.com/sanskrit-lexicon/PWG/issues/47) | Malformed `<ls>?` tags → `<ls>` |
| VOP finding | [#111](https://github.com/sanskrit-lexicon/PWG/issues/111) | wontfix — no action needed |

### 4. Text correction — German definitions, Sanskrit headwords

| Field | Value |
|---|---|
| Effort per item | **micro–small** |
| Historical closed | ~5 |
| Open | [#171](https://github.com/sanskrit-lexicon/PWG/issues/171), [#128](https://github.com/sanskrit-lexicon/PWG/issues/128), [#90](https://github.com/sanskrit-lexicon/PWG/issues/90), [#85](https://github.com/sanskrit-lexicon/PWG/issues/85), [#67](https://github.com/sanskrit-lexicon/PWG/issues/67), [#63](https://github.com/sanskrit-lexicon/PWG/issues/63), [#58](https://github.com/sanskrit-lexicon/PWG/issues/58), [#44](https://github.com/sanskrit-lexicon/PWG/issues/44) |

PWG text corrections require German language competence — Böhtlingk's definitions are in German,
and most corrections are either typographical (`Page6` → `Page 6` in [#63](https://github.com/sanskrit-lexicon/PWG/issues/63))
or abbreviation normalizations. Issue [#67](https://github.com/sanskrit-lexicon/PWG/issues/67)
(German word corrections) is the main catchall.

### 5. Content enhancement — new data, display upgrades

| Field | Value |
|---|---|
| Effort per item | **medium–hard** |
| Historical closed | ~10 |
| Open | [#163](https://github.com/sanskrit-lexicon/PWG/issues/163), [#61](https://github.com/sanskrit-lexicon/PWG/issues/61), [#37](https://github.com/sanskrit-lexicon/PWG/issues/37), [#88](https://github.com/sanskrit-lexicon/PWG/issues/88), [#72](https://github.com/sanskrit-lexicon/PWG/issues/72), [#59](https://github.com/sanskrit-lexicon/PWG/issues/59), [#52](https://github.com/sanskrit-lexicon/PWG/issues/52), [#49](https://github.com/sanskrit-lexicon/PWG/issues/49), [#94](https://github.com/sanskrit-lexicon/PWG/issues/94) |

**Three major strategic enhancements:**

| Issue | Title | Effort | Notes |
|---|---|---|---|
| [#163](https://github.com/sanskrit-lexicon/PWG/issues/163) | Merge AB's version of PWG | **hard** | A community-contributed fork with additional data; requires merge strategy |
| [#61](https://github.com/sanskrit-lexicon/PWG/issues/61) | Weber's Nachlass | **hard** | Historical supplement; requires digitization + alignment |
| [#37](https://github.com/sanskrit-lexicon/PWG/issues/37) | Cologne Additions to PWG | **hard** | Org-wide content enhancement; long-running |

[#52](https://github.com/sanskrit-lexicon/PWG/issues/52) (Apply VN) and
[#49](https://github.com/sanskrit-lexicon/PWG/issues/49) (HarivaMSa links via MBH Calcutta)
are medium-effort additions that can proceed independently.

### 6. Scholarly question — needs research before action

| Field | Value |
|---|---|
| Effort per item | **variable** |
| Historical closed | ~5 |
| Open | [#132](https://github.com/sanskrit-lexicon/PWG/issues/132), [#131](https://github.com/sanskrit-lexicon/PWG/issues/131), [#128](https://github.com/sanskrit-lexicon/PWG/issues/128), [#118](https://github.com/sanskrit-lexicon/PWG/issues/118), [#107](https://github.com/sanskrit-lexicon/PWG/issues/107), [#106](https://github.com/sanskrit-lexicon/PWG/issues/106), [#72](https://github.com/sanskrit-lexicon/PWG/issues/72) |

Several open issues are primarily interpretive questions about PWG editorial conventions —
how to handle commentarial citations, titular references, UTTARAR, etc. These need
a maintainer decision before any code change.

### 7. Bug fix

| Field | Value |
|---|---|
| Effort per item | **small** |
| Historical closed | ~5 |
| Open | [#79](https://github.com/sanskrit-lexicon/PWG/issues/79) (Hariv. link bug), [#47](https://github.com/sanskrit-lexicon/PWG/issues/47) (`<ls>?`) |

### 8. Scan quality — missing or blurry pages

| Field | Value |
|---|---|
| Effort per item | **small–medium** |
| Historical closed | ~2 |
| Open | [#76](https://github.com/sanskrit-lexicon/PWG/issues/76) (VN missing pages, continued), [#39](https://github.com/sanskrit-lexicon/PWG/issues/39) (VN missing pages) |

Both open scan-quality issues concern the VN (Vernaleken?) scans. These are blocked
on obtaining replacement scans.

### 9. Encoding

| Field | Value |
|---|---|
| Effort per item | **small–medium** |
| Historical closed | ~3 |
| Open | [#78](https://github.com/sanskrit-lexicon/PWG/issues/78) (Transcoding vowel-marker characters) |

---

## Cross-repo dependencies

| Repo | Why it affects PWG roadmap |
|---|---|
| [csl-orig](https://github.com/sanskrit-lexicon/csl-orig) | Canonical [pwg.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt) lives here — all corrections commit here |
| [csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork) | Build pipeline — `generate_dict.sh pwg` for validation |
| [csl-app](https://github.com/sanskrit-lexicon/csl-app) | Web display — any display-layer changes land here |
| [MWS](https://github.com/sanskrit-lexicon/MWS) | Principal scholarly downstream user of PWG; block-profile analysis at [`pwg_blocks.json`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/data/pwg_blocks.json) |
| [GRA](https://github.com/sanskrit-lexicon/GRA) | Grassmann's RV-Wörterbuch — coordinate on RV. citation links (#133, #173) |
| [COLOGNE](https://github.com/sanskrit-lexicon/COLOGNE) | Org-wide docs hub — PWG's roadmap feeds into the org tracker |

---

## Quarterly view (suggested cadence ~1–2 issues/month)

### Q1 (2026 Jun–Aug)

**Focus: close docs-pass review; clear quick-win markup/text issues.**

- [ ] Review and merge docs-pass branch ([#179](https://github.com/sanskrit-lexicon/PWG/issues/179))
- [ ] [#175](https://github.com/sanskrit-lexicon/PWG/issues/175) Minor markup oddities — sweep and apply
- [ ] [#171](https://github.com/sanskrit-lexicon/PWG/issues/171) Few text corrections — apply batch
- [ ] [#63](https://github.com/sanskrit-lexicon/PWG/issues/63) Page6 → Page 6 — micro fix
- [ ] [#167](https://github.com/sanskrit-lexicon/PWG/issues/167) YĀSKA'S NIRUKTA link target
- [ ] [#159](https://github.com/sanskrit-lexicon/PWG/issues/159) AITAREYABRĀHMAṆA link target
- [ ] Resolve #107 and #106 (commentarial / titular question) — decision, then close or escalate

### Q2 (2026 Sep–Nov)

**Focus: link-splitting batch; `<ls>` markup cluster.**

- [ ] [#172](https://github.com/sanskrit-lexicon/PWG/issues/172) YĀJÑ. link splitting
- [ ] [#145](https://github.com/sanskrit-lexicon/PWG/issues/145) KĀTYĀYANA'S ŚRAUTASŪTRĀṆI splitting
- [ ] [#142](https://github.com/sanskrit-lexicon/PWG/issues/142) RAGH. Calc. changes
- [ ] [#133](https://github.com/sanskrit-lexicon/PWG/issues/133) ṚV. links — coordinate with [GRA](https://github.com/sanskrit-lexicon/GRA)
- [ ] [#116](https://github.com/sanskrit-lexicon/PWG/issues/116) Abhidhānacintāmaṇi missing references
- [ ] [#91](https://github.com/sanskrit-lexicon/PWG/issues/91) `<lex>` gaps in Instr/Gen Du.
- [ ] [#158](https://github.com/sanskrit-lexicon/PWG/issues/158) MBH Bombay-Calcutta concordance link target
- [ ] [#150](https://github.com/sanskrit-lexicon/PWG/issues/150) CAURAPAÑCĀŚIKĀ link target

### Q3 (2026 Dec – 2027 Feb)

**Focus: Prātiśākhya cluster; content questions.**

- [ ] [#41](https://github.com/sanskrit-lexicon/PWG/issues/41) Prātiśākhya ls references + [#42](https://github.com/sanskrit-lexicon/PWG/issues/42) Taittirīya Prātiśākhya + [#139](https://github.com/sanskrit-lexicon/PWG/issues/139) VS. PRĀT. — address as a cluster
- [ ] [#173](https://github.com/sanskrit-lexicon/PWG/issues/173) RigVeda, Uebersetzung des Prâtisâkhya link target
- [ ] [#137](https://github.com/sanskrit-lexicon/PWG/issues/137) NĀRADA PAÑCARĀTRA link target
- [ ] [#131](https://github.com/sanskrit-lexicon/PWG/issues/131), [#132](https://github.com/sanskrit-lexicon/PWG/issues/132) interpretation questions — decision
- [ ] [#78](https://github.com/sanskrit-lexicon/PWG/issues/78) Transcoding vowel-marker characters — scoped fix
- [ ] [#67](https://github.com/sanskrit-lexicon/PWG/issues/67) German word corrections — batch apply

### Long-running (multi-quarter)

- [ ] **[#163](https://github.com/sanskrit-lexicon/PWG/issues/163) Merge AB's version of PWG** — needs merge strategy; maintainer consensus required
- [ ] **[#61](https://github.com/sanskrit-lexicon/PWG/issues/61) Weber's Nachlass** — large content addition; digitization-dependent
- [ ] **[#37](https://github.com/sanskrit-lexicon/PWG/issues/37) Cologne Additions to PWG** — org-wide content initiative
- [ ] **[#74](https://github.com/sanskrit-lexicon/PWG/issues/74) Manu link standardization** — affects many combined refs
- [ ] **[#76](https://github.com/sanskrit-lexicon/PWG/issues/76), [#39](https://github.com/sanskrit-lexicon/PWG/issues/39) VN missing pages** — blocked on scan availability
- [ ] **[#47](https://github.com/sanskrit-lexicon/PWG/issues/47) `<ls>?` → `<ls>` fix** — `bug`; needs regex sweep across corpus
- [ ] **[#79](https://github.com/sanskrit-lexicon/PWG/issues/79) Hariv. link bug** — `bug`; unresolved after #80 closed as duplicate
- [ ] **[#52](https://github.com/sanskrit-lexicon/PWG/issues/52) Apply VN** — medium enhancement; independent
- [ ] **[#49](https://github.com/sanskrit-lexicon/PWG/issues/49) HarivaMSa links via MBH Calcutta** — medium; link-target + content

---

## Issue → roadmap map (open issues)

| Issue | Title (truncated) | Category | Effort | Quarter |
|---|---|---|---|---|
| [#179](https://github.com/sanskrit-lexicon/PWG/issues/179) | docs-pass review | Documentation | small | Q1 |
| [#178](https://github.com/sanskrit-lexicon/PWG/issues/178) | enhance PWG markup, part 2 | Markup | small | Q1 |
| [#175](https://github.com/sanskrit-lexicon/PWG/issues/175) | Minor markup oddities | Markup | small | Q1 |
| [#173](https://github.com/sanskrit-lexicon/PWG/issues/173) | RigVeda Prâtisâkhya link | Link target | small | Q3 |
| [#172](https://github.com/sanskrit-lexicon/PWG/issues/172) | YĀJÑ. refs inconsistent | Link splitting | small | Q2 |
| [#171](https://github.com/sanskrit-lexicon/PWG/issues/171) | Few text corrections | Text correction | micro | Q1 |
| [#167](https://github.com/sanskrit-lexicon/PWG/issues/167) | YĀSKA'S NIRUKTA link | Link target | small | Q1 |
| [#166](https://github.com/sanskrit-lexicon/PWG/issues/166) | Commentarial link investigation | Question/Enhancement | medium | Q2 |
| [#163](https://github.com/sanskrit-lexicon/PWG/issues/163) | Merge AB's version | Content enhancement | hard | Long |
| [#162](https://github.com/sanskrit-lexicon/PWG/issues/162) | Links to Introductions | Link target/Enhancement | medium | Q2 |
| [#159](https://github.com/sanskrit-lexicon/PWG/issues/159) | AITAREYABRĀHMAṆA link | Link target | small | Q1 |
| [#158](https://github.com/sanskrit-lexicon/PWG/issues/158) | MBH Bombay-Calcutta concordance | Link target | small | Q2 |
| [#156](https://github.com/sanskrit-lexicon/PWG/issues/156) | Link target README improvement | Documentation | micro | Q1 |
| [#150](https://github.com/sanskrit-lexicon/PWG/issues/150) | CAURAPAÑCĀŚIKĀ link | Link target | small | Q2 |
| [#145](https://github.com/sanskrit-lexicon/PWG/issues/145) | KĀTYĀYANA refs splitting | Link splitting | small | Q2 |
| [#142](https://github.com/sanskrit-lexicon/PWG/issues/142) | RAGH. Calc. changes | Link splitting | small | Q2 |
| [#139](https://github.com/sanskrit-lexicon/PWG/issues/139) | VS. PRĀT. link target | Link target | small | Q3 |
| [#137](https://github.com/sanskrit-lexicon/PWG/issues/137) | NĀRADA PAÑCARĀTRA link | Link target | small | Q3 |
| [#133](https://github.com/sanskrit-lexicon/PWG/issues/133) | ṚV. links | Link splitting | small | Q2 |
| [#132](https://github.com/sanskrit-lexicon/PWG/issues/132) | how to interpret? | Question | micro | Q3 |
| [#131](https://github.com/sanskrit-lexicon/PWG/issues/131) | UTTARAR interpretation | Question | micro | Q3 |
| [#128](https://github.com/sanskrit-lexicon/PWG/issues/128) | Miscellaneous corrections | Text correction + Question | small | Q1 |
| [#118](https://github.com/sanskrit-lexicon/PWG/issues/118) | ŚKDR. how to link | Link target + Question | small | Q2 |
| [#116](https://github.com/sanskrit-lexicon/PWG/issues/116) | Abhidhānacintāmaṇi refs | Markup | small | Q2 |
| [#111](https://github.com/sanskrit-lexicon/PWG/issues/111) | VOP missing tags | Markup | — | wontfix |
| [#107](https://github.com/sanskrit-lexicon/PWG/issues/107) | Commentarial refs | Question/Markup | small | Q1 |
| [#106](https://github.com/sanskrit-lexicon/PWG/issues/106) | Titular refs | Question/Markup | small | Q1 |
| [#94](https://github.com/sanskrit-lexicon/PWG/issues/94) | Link target admin | Link target + Admin | small | Q1–Q2 |
| [#91](https://github.com/sanskrit-lexicon/PWG/issues/91) | `<lex>` Instr/Gen Du gaps | Markup | small | Q2 |
| [#90](https://github.com/sanskrit-lexicon/PWG/issues/90) | Ṛv. PRĀTIŚ. wrongly | Text correction | micro | Q1 |
| [#88](https://github.com/sanskrit-lexicon/PWG/issues/88) | Lingânuçâsana word list | Content enhancement | small | Q2 |
| [#85](https://github.com/sanskrit-lexicon/PWG/issues/85) | `<ls>MÜLLER</ls>?'S` | Markup + Text | small | Q1 |
| [#79](https://github.com/sanskrit-lexicon/PWG/issues/79) | Hariv. link bug | Bug | small | Long |
| [#78](https://github.com/sanskrit-lexicon/PWG/issues/78) | Vowel-marker transcoding | Encoding | medium | Q3 |
| [#76](https://github.com/sanskrit-lexicon/PWG/issues/76) | VN missing pages (cont.) | Scan quality | medium | Long |
| [#74](https://github.com/sanskrit-lexicon/PWG/issues/74) | Manu link standardization | Link splitting | medium | Long |
| [#72](https://github.com/sanskrit-lexicon/PWG/issues/72) | INDOLOGY upgrade question | Question/Enhancement | medium | Long |
| [#67](https://github.com/sanskrit-lexicon/PWG/issues/67) | German word corrections | Text correction | medium | Q3 |
| [#63](https://github.com/sanskrit-lexicon/PWG/issues/63) | Page6 → Page 6 | Text correction | micro | Q1 |
| [#61](https://github.com/sanskrit-lexicon/PWG/issues/61) | Weber's Nachlass | Content enhancement | hard | Long |
| [#60](https://github.com/sanskrit-lexicon/PWG/issues/60) | Bombay Ramayana link | Link target | small | Q2 |
| [#59](https://github.com/sanskrit-lexicon/PWG/issues/59) | Additional source links | Link target + Enhancement | medium | Long |
| [#58](https://github.com/sanskrit-lexicon/PWG/issues/58) | Minor abbrev suggestions | Text correction | micro | Q1 |
| [#57](https://github.com/sanskrit-lexicon/PWG/issues/57) | Ramayana link markup | Link target | small | Q2 |
| [#52](https://github.com/sanskrit-lexicon/PWG/issues/52) | Apply VN | Content enhancement | medium | Long |
| [#51](https://github.com/sanskrit-lexicon/PWG/issues/51) | PWG ls markup | Markup | medium | Q2 |
| [#49](https://github.com/sanskrit-lexicon/PWG/issues/49) | HarivaMSa via MBH Calcutta | Link target + Enhancement | medium | Long |
| [#47](https://github.com/sanskrit-lexicon/PWG/issues/47) | `<ls>?` → `<ls>` | Bug/Markup | medium | Long |
| [#44](https://github.com/sanskrit-lexicon/PWG/issues/44) | Preverb corrections | Text correction | medium | Q3 |
| [#42](https://github.com/sanskrit-lexicon/PWG/issues/42) | Taittirīya Prātiśākhya link | Link target | small | Q3 |
| [#41](https://github.com/sanskrit-lexicon/PWG/issues/41) | Prātiśākhya ls refs | Link target + Markup | small | Q3 |
| [#39](https://github.com/sanskrit-lexicon/PWG/issues/39) | VN missing pages | Scan quality | medium | Long |
| [#37](https://github.com/sanskrit-lexicon/PWG/issues/37) | Cologne Additions | Content enhancement | hard | Long |

---

## How this roadmap is maintained

- **Updated:** after every wave of issue closures or new strategic finding.
- **Source of truth for status:** [GitHub issues](https://github.com/sanskrit-lexicon/PWG/issues) (this doc *summarises*).
- **Effort estimates:** intentionally coarse — planning, not commitments.
- **Velocity assumption:** ~1–2 link-targets/month sustained; bursts when a maintainer is active.
- **Owners:** @funderburkjim and @Andhrabharati are the primary maintainers.

Cross-link: this roadmap is part of the [org-wide docs-pass](https://github.com/sanskrit-lexicon/COLOGNE)
and complements [`DICT_PROFILE.md`](https://github.com/sanskrit-lexicon/PWG/blob/docs-pass/DICT_PROFILE.md)
(on this branch). Block-profile analysis cross-dict data at
[`papers/microanalysis/figures/data/pwg_blocks.json`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/data/pwg_blocks.json).
"""

def run_gh(args):
    result = subprocess.run(['gh'] + args, capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
    return result.stdout.strip(), result.returncode

def push_file(repo, path, content_str, msg, branch='docs-pass'):
    content_b64 = base64.b64encode(content_str.encode('utf-8')).decode('ascii')
    payload = {'message': msg, 'content': content_b64, 'branch': branch}
    out, rc = run_gh(['api', f'repos/{ORG}/{repo}/contents/{path}?ref={branch}',
                      '-H', 'Accept: application/vnd.github.v3+json', '--jq', '.sha'])
    if rc == 0 and out:
        payload['sha'] = out
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False)
        tmp = f.name
    try:
        _, rc = run_gh(['api', f'repos/{ORG}/{repo}/contents/{path}', '-X', 'PUT', '--input', tmp])
        return rc == 0
    finally:
        os.unlink(tmp)

if __name__ == '__main__':
    msg = ('docs-pass: add ROADMAP.md for PWG (S7)\n\n'
           'Synthesises ~53 open + ~125 closed GitHub issues into a quarterly roadmap.\n'
           'Dominant work type: link-target (scan URLs for 4.63 ls/rec citation apparatus).\n\n'
           'Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>')
    ok = push_file(REPO, 'ROADMAP.md', ROADMAP, msg)
    if ok:
        print(f'Pushed ROADMAP.md to {REPO}/{BRANCH} ({len(ROADMAP):,} chars)')
    else:
        print('ERROR: push failed')
        sys.exit(1)
