# MW1899 microanalysis — a data-grounded microstructural study

This directory contains a **microstructural analysis** of the *Monier-Williams Sanskrit-English Dictionary* (1899) as digitized by the [Cologne Digital Sanskrit Lexicon](https://www.sanskrit-lexicon.uni-koeln.de/) ([`mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt)).

The 286,561-record dataset is analysed primarily through a **data-grounded** framework (built from MW outward), and that reading is then **triangulated** against the three dominant metalexicographic traditions — Wiegand, Atkins & Rundell, and Hausmann. The result is **one consolidated paper** ([PAPER.md](PAPER.md)) with the three external-framework treatments as condensed appendices. The shared data backbone is a single working-notes document.

> **Consolidation note (2026-05-23).** This study was originally drafted as **four parallel papers**, one per framework. Per [DOUBTS.md D4](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking) — the risk that four papers from one dataset reads as salami-slicing — they have been consolidated into the single [PAPER.md](PAPER.md): the grounded reading is the body, and the Wiegand / Atkins-Rundell / Hausmann readings are [Appendices A–C](PAPER.md#appendix-a--the-wiegand-theoretic-reading-condensed). The four fuller single-framework drafts are **retained in this directory as supplementary material** — [paper-wiegand.md](paper-wiegand.md), [paper-atkins-rundell.md](paper-atkins-rundell.md), [paper-hausmann.md](paper-hausmann.md), [paper-grounded.md](paper-grounded.md) — each banner-linked back to PAPER.md.

---

## Contents

| File | Purpose | Length |
|---|---|--:|
| [MICROANALYSIS.md](MICROANALYSIS.md) | **Working notes** — exhaustive data file. The single source of truth: 18 formal blocks × 14 article types × 8 worked entry samples + co-occurrence matrix + fullness scale | ~10K words |
| [PAPER.md](PAPER.md) | **The paper** — data-grounded framework (five constructs: block / slot / profile / hedge / infrastructure; the *block-economy* thesis), §7 triangulation against three external frameworks, three condensed appendices (A Wiegand · B Atkins-Rundell · C Hausmann), and a methodological-limitations section | ~5.7K words |
| [VISUALISATIONS.md](VISUALISATIONS.md) | **Visualisation catalogue** — all visualisation types the data supports (10 categories, ~40 ideas), prioritised by impact/effort into 3 tiers, with tool-choice notes and the Phase-4 reusability pattern | ~3K words |
| [decisions/](decisions/) | **28 design decisions** split into 7 thematic sub-docs (PALETTE / I18N / MICROSITE / FIGURES / NORMALISATION / SUPPLEMENTARY / BUILD-ORDER) | ~6K words total |
| [DOUBTS.md](DOUBTS.md) | **Critical review** of 15 architectural doubts (per @gasyoun's "doubt everything" mandate) | ~3K words |
| [figures/](figures/) | **Built artefacts** — Tier-1 figures (heatmap, treemap, Sankey, Mermaid timeline) in EN + RU, palette tokens, locales, Python renderers, JSON data exports | — |

---

## What the paper argues

The [paper](PAPER.md) builds a minimal, five-construct framework from MW itself and reaches one central empirical claim: **MW is a block-economical dictionary** — its 286,561 entries reuse the same ~6-block kernel (F01, F02, F04, F10, F12, F17) with type-driven enrichment. It then shows that three independently-motivated external frameworks **converge** on the same structural facts, which is the methodological reason the study is one paper rather than four.

| If you want to know… | Read |
|---|---|
| **The data** — what blocks exist, how often, in what combinations | [MICROANALYSIS.md](MICROANALYSIS.md) |
| **MW's own design logic** before any external theory — the *block-economy* finding | [PAPER.md §3–§6](PAPER.md#3-the-five-grounded-constructs) |
| How three external frameworks **corroborate** the grounded reading, and where each adds something unique | [PAPER.md §7](PAPER.md#7-triangulation-three-external-frameworks-converge) |
| MW1899 *as a Wiegandian object* — microstructure type, structural indicators, indicator load | [PAPER.md Appendix A](PAPER.md#appendix-a--the-wiegand-theoretic-reading-condensed) |
| MW from a modern practical-lexicography lens — headword inventory, examples, the retrieval-dictionary typology | [PAPER.md Appendix B](PAPER.md#appendix-b--the-atkins-rundell-practical-lexicography-reading-condensed) |
| MW's comment-class apparatus and the proposed fifth class (*Provenienz-Komment*) for its `<ls>L.</ls>` hedge | [PAPER.md Appendix C](PAPER.md#appendix-c--the-hausmann-wiegand-comment-class-reading-condensed) |
| What we are *not yet sure of* — regex limits, significance testing, cross-dict scope | [PAPER.md §9](PAPER.md#9-methodological-limitations) and [DOUBTS.md](DOUBTS.md) |

---

## The triangulation in one paragraph

Three findings surface independently under all three external frameworks (this is [PAPER.md §7.2](PAPER.md#72-three-findings-all-three-frameworks-reach)): **(1)** MW has a small block kernel plus large article-type-specific enrichments — Wiegand's *modal-6-block microstructure*, Atkins-Rundell's *kernel-plus-extension policy*, Hausmann's *form-comment economy*, and the grounded *block economy* are one finding in four terminologies; **(2)** the `<ls>L.</ls>` lexicographer-hedge is MW's most distinctive feature — a Wiegandian transverse indicator, an A&R register marker, a Hausmann *Provenienz-Komment* (a fifth class we propose), and the grounded *hedge construct*, all agreeing it is specific to MW and a deliberate compression of PWG's named-kosha system (see [DICT_PROFILE Lineage](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg)); **(3)** continuation entries (`<e>1A`) are structurally distinctive — *adjacency-integration* (Wiegand), *adjacency-sub-entries* (A&R), *semantic-only signatures* (Hausmann), *kernel-reduced profiles* (grounded). Each framework also adds exactly one thing the others miss — and the grounded view adds two (the *infrastructure layer* and *block economy*) that none of the three captures.

---

## Methodological note

The paper draws from the [working-notes file](MICROANALYSIS.md), generated by parsing every `<L>...<LEND>` record in the live [`mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) (48.9 MB, 286,561 records). The block-detection Python source is in the [docs-pass build artefacts](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass). Counts are reproducible. Block detection is regex-based and approximate; its limits are documented in [PAPER.md §9](PAPER.md#9-methodological-limitations).

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

Single consolidated draft complete. Not yet submitted. Internal review by @funderburkjim and @Andhrabharati is welcomed via [issue #195](https://github.com/sanskrit-lexicon/MWS/issues/195) before any external venue choice is finalised.

If accepted for IJL, this study would be a first: the first systematic microstructural analysis of a CDSL dictionary at this scale, with a data-grounded framework corroborated by three independent metalexicographic traditions.
