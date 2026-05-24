# Decisions — cross-dictionary normalisation strategy

Covers decision **4** — the most substantive single decision, with seven normalisation options enumerated. See [decisions/README.md](README.md) for the full index.

This document is the **canonical reference** for which normalisation to use in which figure. All percentages and counts here are computed against the live data files (2026-05-23) — see [VISUALISATIONS.md §Decision 4](../VISUALISATIONS.md#decision-4--cross-dictionary-normalisation-detailed-analysis) for the full data with caveats.

---

## Summary recommendation

**No single normalisation is correct.** Different visualisations should use different normalisations. Each figure caption must state which normalisation it uses.

Recommended mapping:

| Visualisation | Normalisation | Why |
|---|---|---|
| Multi-bar size comparison (Tier 1 treemap, [3.1] multi-bar) | **A** Raw counts | Establishes scale; honest about MW's size |
| Citation-density per dict (any density chart) | **B** Per-entry | Reveals editorial citation choice |
| Lineage Sankey (Tier 1 #2) | **F** Coverage % | Direct editorial-policy comparison |
| Microstructure fingerprints (Tier 2 #7) | **G** Z-score | Pure pattern visibility |
| Per-headword density argument | **C** Per-headword or **E** Per-unique-k1 | When discussing lemma inventory choice |

---

## The seven options at a glance

### A — Raw absolute counts

| Dict | Entries | `<ls>` tags | Unique `<ls>` | `<ls>L.</ls>` |
|---|--:|--:|--:|--:|
| MW | 286,561 | 311,932 | 821 | 40,212 |
| PWG | 123,366 | 570,817 | 2,420 | 0 |
| PWK | 170,556 | 86,750 | 915 | 0 |
| AP | 90,654 | 62,656 | 608 | 1 |
| VCP | 50,135 | 0 | 0 | 0 |
| WIL | 44,577 | 230 | 5 | 0 |
| SKD | 42,531 | 0 | 0 | 0 |

**Tells:** "MW is the biggest single-volume; PWG is the most citation-dense in absolute terms."
**Hides:** PWG's density partly is an artefact of having no `L.` hedge.
**Use for:** scale comparisons.

### B — Per-entry (cites/entry)

| Dict | `<ls>`/entry |
|---|--:|
| PWG | **4.63** |
| MW | 1.09 |
| AP | 0.69 |
| PWK | 0.51 |
| WIL | 0.01 |
| VCP, SKD | 0 |

**Tells:** "PWG is 4.25× denser per entry than MW."
**Hides:** penalises MW for many compound sub-entries that don't need citations.
**Use for:** editorial-density comparisons.

### C — Per-headword (top-level only)

Only MW and AP have `<e>1` top-level markup. Other dicts use different conventions.

| Dict | `<e>1` count | `<ls>`/`<e>1` |
|---|--:|--:|
| MW | 32,116 | 9.71 |
| AP | 49,452 | 1.27 |
| PWG/PWK/WIL/VCP/SKD | (no `<e>` markup) | — |

**Use for:** MW vs AP only.

### D — Per-million-words

| Dict | Words | `<ls>`/10⁶ w |
|---|--:|--:|
| MW | 4,781,977 | 65,229 |
| PWG | 3,581,113 | **159,395** |
| VCP | 2,898,025 | 0 |
| SKD | 2,937,417 | 0 |
| PWK | 2,305,786 | 37,623 |
| AP | 1,781,226 | 35,176 |
| WIL | 1,104,886 | 208 |

**Tells:** "PWG packs 2.4× more citation per word than MW."
**Use for:** textual-artefact comparison.

### E — Per-unique-k1

| Dict | Unique `<k1>` | `<ls>`/unique |
|---|--:|--:|
| MW | 194,084 | 1.61 |
| PWK | 151,349 | 0.57 |
| PWG | 106,083 | **5.38** |
| AP | 88,701 | 0.71 |
| VCP | 48,636 | 0 |
| WIL | 43,938 | 0.01 |
| SKD | 40,817 | 0 |

**Use for:** truest "per-word" comparison across heterogeneous macrostructures.

### F — Coverage % (% of entries citing X) — THE RECOMMENDED LINEAGE NORMALISATION

Per [@gasyoun](https://github.com/gasyoun)'s request: WIL excluded (always 0%); PWK included as middle term between PWG and MW.

| Source | MW | PWG | PWK | AP |
|---|--:|--:|--:|--:|
| RV. | 4.63% | **8.96%** | 0.80% | 0.00% |
| MBh. | 8.93% | **13.84%** | 2.19% | 0.00% |
| R. | 3.59% | 8.71% | 0.94% | 4.89% |
| Pāṇ. | 2.79% | **11.72%** | 0.18% | 1.32% |
| **H.** (Hemacandra) | **0.00%** | **12.18%** | **0.59%** | 0.73% |
| **AK.** (Amarakośa) | **0.08%** | **8.35%** | **0.03%** | 0.00% |
| **MED.** (Medinīkośa) | **0.00%** | **4.20%** | **0.04%** | 0.06% |
| **TRIK.** (Trikāṇḍaśeṣa) | **0.00%** | **4.99%** | **0.03%** | 0.01% |
| **HALĀY.** (Halāyudha) | **0.00%** | **3.46%** | **0.01%** | 0.00% |
| ŚBr. | 2.31% | 4.75% | 0.67% | 0.00% |
| Suśr. | 2.13% | 5.59% | 0.36% | 0.20% |
| Mn. | 2.33% | 5.14% | 0.30% | 0.63% |
| **L.** (Lexicographers) | **13.95%** | **0.00%** | **0.01%** | **0.42%** |

**The killer finding:** The bold rows show the kosha-citation collapse. PWG → PWK already drops the named kosha apparatus; PWK → MW completes the collapse by replacing it with `L.` at 13.95%.

**Use for:** the lineage Sankey + any editorial-policy comparison.

### G — Z-score (standardised)

Standardise each metric per-dict to mean 0, sd 1 across the comparison set.

**Use for:** microstructure-fingerprint visualisations (Tier 2 #7) where the goal is pattern visibility across 5–6 dimensions at once.

---

## Why no single normalisation suffices

| If you ask… | Use… |
|---|---|
| "Which is the biggest dictionary?" | A — Raw |
| "Which is the most citation-dense?" | B — Per-entry |
| "Does this dict cite the koshas?" | F — Coverage |
| "How dense per page of print?" | D — Per-million-words |
| "Which has more unique lemmas?" | E — Per-unique-k1 |
| "What pattern across dimensions?" | G — Z-score |

The figure caption must state the normalisation. Worked examples:

> Figure 2. **Normalisation: F — Coverage % (entries citing source X)**.
> Six PWG kośa-citation labels flow through the named kośa works and converge into MW's `<ls>L.</ls>` hedge…

> Figure 3. **Normalisation: B — Per-entry**.
> PWG averages 4.63 `<ls>` citations per entry, vs MW's 1.09…

---

## Implementation status (2026-05-23)

- [x] All 7 options documented with REAL counts (no estimates) computed from data files
- [x] Recommendation table for figure → normalisation mapping
- [x] PWK substituted for WIL in Option F per user request
- [x] Lineage Sankey (Tier 1 #2) uses Option F
- [x] Treemap (Tier 1 #4) uses Option A
- [ ] Caption normalisation-statement convention not yet enforced in built figures (TODO)

## Cross-links

- [VISUALISATIONS.md §Decision 4](../VISUALISATIONS.md#decision-4--cross-dictionary-normalisation-detailed-analysis) — full discussion with "what it obscures" notes per option
- [FIGURES.md](FIGURES.md) — figure design conventions
- [DICT_PROFILE Lineage section](../../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) — qualitative narrative of the kosha-collapse
- [Lineage Sankey](../figures/sankey-en.svg) — the visualisation that uses Option F
