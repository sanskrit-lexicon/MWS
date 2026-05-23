# Decisions — figure design and conventions

Covers decisions **13**, **14**, **15**, **17**, **21**, **22**, **23**, **26**, **28**. See [decisions/README.md](README.md) for the full index.

---

## Decision 13 — Legend strategy: hover + brief inset + caption-key

- **Interactive microsite:** legend appears on hover; full key accessible via toggle.
- **Static SVG figures:** brief inset (≤ 5 entries) with note "see full key in caption."
- **Caption:** carries the complete colour key as a structured legend block.

Lets static figures preserve plot-space while remaining self-explanatory; interactive variant provides full richness.

## Decision 14 — Accessibility: triple coverage

Every figure carries:

1. **Short `alt` text** (~100 chars) — chart type + the single key takeaway. For screen readers, first contact. Stored in `figures/{figure}-{locale}.alt.txt`.
2. **Long SVG `<desc>` element** (~300–500 chars) — full description embedded inside the SVG. Screen readers can navigate inside the figure. Stored in `figures/{figure}-{locale}.desc.txt`.
3. **Long caption** — printed text alongside the figure with the full narrative + colour key + data-source citation.

Aligns with [W3C SVG accessibility spec](https://www.w3.org/TR/SVG2/struct.html#DescriptionAndTitleElements) and IJL's standard accessibility checklist.

## Decision 15 — Figure numbering: single continuous sequence + stable-slug manifest

The study is now **one paper** ([PAPER.md](../PAPER.md)), so figures use a single continuous sequence (Fig 1, Fig 2, …) across body and appendices; appendix figures may take an `A`/`B`/`C` prefix (Fig A1, Fig B1). The earlier per-paper numbering is retired with the consolidation ([DOUBTS.md D4](../DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking)).

A separate **stable figure-ID manifest** (`figures/manifest.json`, TBD) will map each figure's slug → its number. Survives reviewer-driven renumbering.

## Decision 17 — Dimensions: IJL full-page-width (~175 mm)

All four Tier-1 figures render at **IJL full-page-width (~175 mm)** spanning both columns.

Implementation: matplotlib `figsize=(7, 4.5)` to `(7, 5.5)` inches at 300 DPI for paper; SVG export for vectorisation.

## Decision 21 — Heatmap: blocks on Y, types on X, short codes

The 18 × 14 matrix:
- **Y-axis (vertical, 18 rows):** formal blocks F01–F18, full names (room for "F12 Source citation" etc.).
- **X-axis (horizontal, 14 columns):** article types as **short codes** rendered horizontally — no rotation needed.

Short-code mapping (in `figures/locales/{en,ru}.json` `article-type-short`):

| Article type | EN code | RU code |
|---|:---:|:---:|
| root | `root` | `корень` |
| noun_m | `n.m` | `сущ.м` |
| noun_f | `n.f` | `сущ.ж` |
| noun_n | `n.n` | `сущ.с` |
| noun_mn | `n.mn` | `сущ.мс` |
| adjective_mfn | `adj` | `прил` |
| indeclinable | `ind` | `нескл` |
| compound | `comp` | `комп` |
| derived | `deriv` | `произв` |
| continuation | `cont` | `прод` |
| lexicographer_only | `lex.` | `кош.` |
| etymological_ie | `IE.et` | `ИЕ.эт` |
| botanical | `bot` | `бот` |
| biographical | `bio` | `биогр` |
| vedic_accented | `V.acc` | `вед.уд` |
| other | `oth` | `проч` |

## Decision 22 — Sankey: three-stage flow

Stage 1 (leftmost) — **PWG `<ls>` indicators** (6 nodes):
- `H.` 17,337 cites
- `AK.` 14,473
- `MED.` 13,055
- `H. an.` 9,771
- `TRIK.` 8,365
- `HALĀY.` 5,114

Stage 2 (middle) — **the actual kosha works** (6 nodes, IAST italic):
- *Abhidhānacintāmaṇi* (Hemacandra)
- *Amarakośa*
- *Medinīkośa*
- *Anekārthasaṃgraha* (Hemacandra)
- *Trikāṇḍaśeṣa*
- *Abhidhānaratnamālā* (Halāyudha)

Stage 3 (rightmost) — **MW `<ls>L.</ls>`** (1 node, emphasised): 40,212 cites

All six PWG flows merge in stage 2 and collapse into the single MW `L.` node. Visually: six narrow ribbons left → six labelled intermediates → one fat ribbon right.

Plus, where data is available, the four CDSL koshas ([ARMH](https://github.com/sanskrit-lexicon/armh), [ABCH](https://github.com/sanskrit-lexicon/abch), [ACPH](https://github.com/sanskrit-lexicon/acph), [ACSJ](https://github.com/sanskrit-lexicon/acsj)) are annotated against their stage-2 nodes.

## Decision 23 — Citation style: Harvard + inline online DOIs

Print references in the paper use **author-date Harvard** for inline citations and an alphabetised reference list at paper end. Online resources (GitHub, archive.org, Wikipedia, CDSL web display) get inline Markdown links in running text, not separate reference-list entries.

Reference list entries carry DOIs where available.

## Decision 26 — Footer style: 7pt grey italic, bottom-right

Exact footer text format:
```
Source: CDSL mw.txt 2026-05-23 · CC-BY-SA-4.0 · build {SHA}
```

- Font: Noto Sans Italic, 7pt
- Colour: `--mw-color-muted` (#666666)
- Position: bottom-right corner of every figure
- For Mermaid: appended as a comment below the diagram (Mermaid can't position arbitrary text)

## Decision 28 — Figure versioning: SHA + date in footer

Footer text incorporates both Git short SHA and build date. Reviewer can `git show {sha}` to see the exact code that produced the figure. Currently using `subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])` at render time. For Mermaid (which can't carry runtime SHA), date alone.

---

## Implementation status (2026-05-23)

- [x] All four Tier-1 figures rendered in EN
- [x] All four Tier-1 figures rendered in RU
- [x] Alt + desc sidecar files written for all rendered figures (Decision 14)
- [x] Footer with SHA + date implemented (Decisions 26, 28)
- [x] Heatmap dimensions: 7×5.5 inches matplotlib figsize (Decision 17)
- [x] Heatmap layout: blocks Y, types X with short codes (Decision 21)
- [x] Sankey three-stage flow implemented (Decision 22)
- [ ] `figures/manifest.json` figure-ID manifest (Decision 15) not yet built
- [ ] Per-figure caption blocks not yet written into MICROANALYSIS.md (Decision 13)
- [ ] Static legend keys not yet inset into rendered SVGs (Decision 13)
- [ ] Citation style not enforced — the paper carries references but not yet in Harvard format (Decision 23)

## Cross-links

- [VISUALISATIONS.md](../VISUALISATIONS.md) — catalogue + tier prioritisation
- [PALETTE.md](PALETTE.md) — colour tokens used by figures
- [I18N.md](I18N.md) — bilingual labels
- [MICROSITE.md](MICROSITE.md) — interactive renditions
- [NORMALISATION.md](NORMALISATION.md) — captions need to state normalisation
- All rendered figures: [`figures/`](../figures/)
