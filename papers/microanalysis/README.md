# MW1899 microanalysis — four-framework comparative study

This directory contains a **multi-framework microstructural analysis** of the *Monier-Williams Sanskrit-English Dictionary* (1899) as digitized by the [Cologne Digital Sanskrit Lexicon](https://www.sanskrit-lexicon.uni-koeln.de/) ([`mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt)).

The same 286,561-record dataset is analysed through four different theoretical lenses, producing four parallel papers targeted at the [*International Journal of Lexicography*](https://academic.oup.com/ijl). The shared data backbone is a single working-notes document.

---

## Contents

| File | Purpose | Length target |
|---|---|--:|
| [MICROANALYSIS.md](MICROANALYSIS.md) | **Working notes** — exhaustive data file. The single source of truth: 18 formal blocks × 14 article types × 8 worked entry samples + co-occurrence matrix + fullness scale | ~10K words |
| [paper-wiegand.md](paper-wiegand.md) | **Wiegand microstructure theory** framing — integrated/semi-integrated/additive types, structural indicators, treatment units | ~8K words |
| [paper-atkins-rundell.md](paper-atkins-rundell.md) | **Atkins-Rundell practical lexicography** framing — headword inventory, sense division, definition style, examples, retrieval-dictionary typology | ~7.5K words |
| [paper-hausmann.md](paper-hausmann.md) | **Hausmann-Wiegand hybrid** framing — form-comment / semantic-comment / pragmatic-comment / source-comment, plus a proposed fifth comment-class (*Provenienz-Komment*) for MW's `<ls>L.</ls>` hedge | ~7K words |
| [paper-grounded.md](paper-grounded.md) | **Data-grounded** framing — five constructs (block, slot, profile, hedge, infrastructure) built from MW outward, with external-framework comparison at the end | ~8K words |
| [VISUALISATIONS.md](VISUALISATIONS.md) | **Visualisation catalogue** — all visualisation types the data supports (10 categories, ~40 visualisation ideas), prioritised by impact/effort into 3 tiers, with tool-choice notes and Phase-4 reusability pattern | ~3K words |
| [decisions/](decisions/) | **28 design decisions** split into 7 thematic sub-docs (PALETTE / I18N / MICROSITE / FIGURES / NORMALISATION / SUPPLEMENTARY / BUILD-ORDER) | ~6K words total |
| [DOUBTS.md](DOUBTS.md) | **Critical review** of 15 architectural doubts (per @gasyoun's "doubt everything" mandate) | ~3K words |
| [figures/](figures/) | **Built artefacts** — Tier-1 figures (heatmap, treemap, Sankey, Mermaid timeline) in EN + RU, palette tokens, locales, Python renderers, JSON data exports | — |

---

## Which paper should I read for which question?

| If you want to know… | Read |
|---|---|
| **The data** — what blocks exist, how often, in what combinations | [MICROANALYSIS.md](MICROANALYSIS.md) |
| What MW1899 looks like *as a Wiegandian object* — microstructure type, structural indicators, treatment units | [paper-wiegand.md](paper-wiegand.md) |
| What design decisions MW1899 reflects from a modern-lexicography-handbook perspective — and how a contemporary revision would address MW's gaps | [paper-atkins-rundell.md](paper-atkins-rundell.md) |
| How MW's comment-class apparatus compares to PWG's — and why we need to extend Hausmann's four-class system with a fifth class for MW's hedge | [paper-hausmann.md](paper-hausmann.md) |
| What MW's own design logic looks like before any external theory is consulted — the **block-economy** finding | [paper-grounded.md](paper-grounded.md) |
| **All four together** — to compare framework strengths and to triangulate findings | Read this README, then all four in order |

---

## Cross-paper findings — convergent and divergent

Three findings appear in **all four papers**:

1. **MW1899 has a small block kernel and large article-type-specific enrichments.** The Wiegand paper calls this *modal 6-block microstructure*; the Atkins-Rundell paper calls it *kernel-plus-extension policy*; the Hausmann paper identifies the *fivefold signature taxonomy*; the grounded paper names it *block economy*. Same finding, four terminologies.

2. **The `<ls>L.</ls>` lexicographer-hedge is MW's most distinctive structural feature.** All four papers identify it. Wiegand calls it a transverse structural indicator; Atkins-Rundell calls it a pragmatic register marker; Hausmann calls it a *Provenienz-Komment* (a fifth comment-class we propose); the grounded paper names it the *hedge construct*. All four agree it is **specific to MW**, absent from PWG, and represents a deliberate editorial compression of PWG's named-kosha citation system. See [DICT_PROFILE Lineage](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg).

3. **Continuation entries (`<e>1A`) are structurally distinctive.** All four papers note that MW's 9,294 continuation entries have suppressed display-headword and grammatical category (inherited from parent), forming what we variously call *adjacency-sub-entries* (Atkins-Rundell), *integrated micro-structure* (Wiegand), *headword-inherited articles* (Hausmann), or *kernel-reduced profile* (grounded).

Three findings appear in **only one paper**:

- **Wiegand only**: MW exhibits a coherent microstructure type that *fits Wiegand's framework better than its 1899 date suggests* — evidence that scholarly European lexicography has a long continuous tradition Wiegand's framework captures.
- **Hausmann only**: the *Provenienz-Komment* as a proposed fifth comment-class. This is the framework's only novel theoretical contribution.
- **Grounded only**: the **infrastructure construct** — recognising that F17 `<info>` and F18 correction records are *trace of digitisation*, not part of MW1899-as-print. No external framework recognises this distinction.

One finding appears in **only the Atkins-Rundell paper**:

- MW is a **retrieval dictionary** (not a production dictionary) in A&R's typology — and its apparent gaps (no examples, no register labels) are coherent under this brief.

---

## Methodological note

All four papers draw from the same [working-notes file](MICROANALYSIS.md), which was generated by parsing every `<L>...<LEND>` record in the live [`mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) (48.9 MB, 286,561 records). The block-detection Python source is in the [docs-pass build artefacts](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass). Counts are reproducible.

Each paper exists as a self-contained document with its own introduction, methodology, and references. None depends on the others having been read first; they are *parallel readings* of the same artefact. Cross-references between papers exist where convergent findings need joint citation.

---

## Cross-links to the broader docs-pass

This microanalysis directory **depends on and extends** the docs-pass content in the parent repo:

- [DICT_PROFILE.md Article types](../../DICT_PROFILE.md#article-types--what-youll-encounter) — the 14-type typology
- [DICT_PROFILE.md Citation markers](../../DICT_PROFILE.md#citation-markers--not-all-are-literary-works) — `L.`, `ib.`, `W.`, `MW.`, `Cat.` analysis
- [DICT_PROFILE.md Lineage: WIL ← Koshas, MW ← PWG](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) — quantitative evidence for the MW-vs-PWG hedge innovation
- [ENTRY_GUIDE.md Entry hierarchy distribution](../../ENTRY_GUIDE.md#entry-hierarchy-distribution) — `<e>` codes
- [ENTRY_GUIDE.md Top 25 sources](../../ENTRY_GUIDE.md#top-25-most-cited-sources) — `<ls>` citation distribution
- [ROADMAP.md](../../ROADMAP.md) — implications for editorial priorities (esp. authority records, L. verification)

---

## Status (2026-05-23)

Drafts complete. Not yet submitted. Internal review by @funderburkjim and @Andhrabharati is welcomed via [issue #195](https://github.com/sanskrit-lexicon/MWS/issues/195) before any external venue choice is finalised.

The four papers have **shared data** but **different framings**. If a single paper is preferred over four for submission, the [grounded paper](paper-grounded.md) is the most self-contained and would scale down to ~6K words; the [Wiegand paper](paper-wiegand.md) carries the strongest theoretical anchor for IJL audiences.

If accepted for IJL, this study would be a first: the first systematic microstructural analysis of a CDSL dictionary at this scale, and a first comparative application of four metalexicographic frameworks to the same dataset.
