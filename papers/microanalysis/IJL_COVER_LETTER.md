---
to: Editor-in-Chief, *International Journal of Lexicography*
from: Mārcis Gasūns (corresponding author) and the CDSL collaboration
date: 2026-05-27
re: Single-paper submission — *The microstructure of Monier-Williams 1899: a data-grounded framework, triangulated against three metalexicographic traditions*
---

# Cover letter

Dear Editor,

We submit one consolidated paper of ~7,700 words ([PAPER.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md)) for consideration in IJL. Four points justify the form of the submission.

## 1. Why a data-grounded framework

Monier-Williams 1899 (henceforth MW) is the most-used Sanskrit-English dictionary in scholarship; it is also one of the few major bilingual dictionaries available in a fully tagged digital edition (the Cologne Digital Sanskrit Lexicon, [CDSL](https://www.sanskrit-lexicon.uni-koeln.de/)). Recent metalexicographic work has, however, analysed MW almost entirely through frameworks built on European mid-to-late-20th-century dictionaries — Wiegand (1989, 2002), Hausmann (1977, 1985), Atkins & Rundell (2008). Each of these frameworks risks imposing categories the lexicographer himself did not recognise.

Our paper inverts the standard order: we build a descriptive apparatus *from the artefact outward*, treating MW's 18 formal blocks, 8 primary article types, and 3 orthogonal article-properties as the primary data, and consulting the three external frameworks only afterward — as **convergent witnesses** rather than as the primary lens. The framework that emerges has five constructs (block, slot, profile, hedge, infrastructure) and a single central empirical claim: **MW is a block-economical scholarly dictionary**, reusing a small kernel across 286,561 entries with type-driven enrichment.

Every numerical claim is reproducible from the published `mw.txt` (48.9 MB, one file, one branch, one commit) using the scripts in [analysis/](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis/analysis/). The audit pipeline is described in PAPER.md §9 and runs in under five minutes on a laptop.

## 2. Why one paper and not four

An earlier version of this work consisted of four parallel papers — one per framework (Wiegand, Atkins-Rundell, Hausmann-Wiegand, plus a grounded paper). After internal critique ([DOUBTS D4](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking)) we judged that four papers on the same dataset would be salami-slicing. The present consolidation makes the **grounded reading primary** (§§1–6, 8–10) and uses the three external readings as **triangulation** (§7, with the full single-framework treatments condensed to [Appendices A–C](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md#appendix-a--the-wiegand-theoretic-reading-condensed)). The methodological move is explicit at §1 ¶3: a finding that surfaces independently under Wiegand, Atkins-Rundell, and Hausmann is a finding *about MW*, not *about any one theory*. Triangulation is the consolidated paper's methodological backbone.

The four original framework-specific drafts are retained in the [docs-pass branch](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis) as `paper-wiegand.md`, `paper-atkins-rundell.md`, `paper-hausmann.md`, and `paper-grounded.md` for reproducibility. None is submitted; they are preserved only as the analytical raw material from which the present paper was distilled.

## 3. Why empirical-audit supplementary materials

§9 of the paper lists six methodological limitations. Five of the six have been **audited in advance of submission** with reproducible scripts:

- [LS_HEDGE_CHECK.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/LS_HEDGE_CHECK.md) verifies the `<ls>L.</ls>` claim across all nine CDSL dictionaries (MW, PWG, PWK, AP, WIL, BEN, CAE, SKD, VCP) and incorporates a 2026 print-preface read of Cappeller 1891 and Benfey 1866.
- [SPOTCHECK.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/SPOTCHECK.md) reproduces the headline 286,561 record count and quantifies F08 and F09 over-counts.
- [SIGNIFICANCE.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/SIGNIFICANCE.md) and [SIGNIFICANCE_FULL.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/SIGNIFICANCE_FULL.md) provide chi-square and Benjamini-Hochberg-adjusted tests across 270 block × type cells (217/270 survive at q = 0.05).
- [CROSS_DICT.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/CROSS_DICT.md) and [CROSS_DICT_PROFILES.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/CROSS_DICT_PROFILES.md) test block-economy generality and per-type profile differentiation across all nine dictionaries.
- [SUPPLEMENT_MANIFEST.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/SUPPLEMENT_MANIFEST.md) packages the audit outputs as a versioned reproducibility supplement.

The sixth limitation — per-entry Sanskritist validation of a labelled 100-record sample — is documented in [SPOTCHECK_SAMPLE.txt](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/SPOTCHECK_SAMPLE.txt) and remains open for reviewer-driven verification.

We also commit, by parallel deposit, to a recorded hostile peer-review pass ([DOUBTS D16-D22](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/DOUBTS.md#hostile-peer-review-pass--d16d22-added-2026-05-27-o7)) that surfaces seven self-critical doubts, one of them rated *blocking* and gating publication. We will address D21 (an MW 1872 preface check that could reverse the §7.2(ii) lineage claim) before camera-ready and disclose the outcome.

## 4. Why IJL

IJL is the natural venue for three independent reasons. **First**, the paper's methodological centre is the comparison of one grounded reading against three named metalexicographic traditions; IJL is the field's primary venue for theoretical-framework work on actual dictionaries. **Second**, IJL's readership includes both lexicographers in the European tradition (who will recognise Wiegand, Hausmann, Atkins-Rundell) and historians of dictionary-making (who will care about MW's 1899 print + 21st-century digital double-identity). **Third**, the paper's central typological-signature proposal (*block-economy as the structural property distinguishing 19th-century scholarly bilingual dictionaries*) extends most naturally into work on other historical dictionaries in IJL's scope — Grimm's *Deutsches Wörterbuch*, the *Oxford English Dictionary* historical editions, the *Trésor de la langue française*. A future companion paper on the indigenous Sanskrit-Sanskrit lexica (*Śabdakalpadruma*, *Vācaspatya*) — which our cross-dict audit shows fall outside the bilingual-dictionary framework — would also be a natural IJL submission.

A Russian-language companion paper covering kosha lineage and 19th-century European Indology ([PAPER_RU.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER_RU.md), in preparation) is being drafted for a Russian indological venue. It does not overlap with the present submission on findings, only on background.

The dataset, audit scripts, and supplementary documents are at the [`docs-pass` branch of sanskrit-lexicon/MWS](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis). The CDSL data underlying the paper is CC-BY-SA-4.0; the audit scripts are CC-BY-SA-4.0. Reviewer access requires no registration.

We thank the editors for their consideration and welcome reviewer engagement on the seven hostile-review doubts; we expect that surface honesty about known weaknesses will be more useful than rhetorical confidence.

Sincerely,

**Mārcis Gasūns** (corresponding author) <gasyoun@gmail.com>
*on behalf of the CDSL collaboration*

---

*Submission status: ~7,700 words, 18 references, 6 figures (4 generated by reproducible scripts in [`figures/scripts/`](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis/figures/scripts/), 2 cross-dictionary), Appendices A–C condensed, supplementary audit suite in [`analysis/`](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis/analysis/). The paper draft is on the [`docs-pass` branch](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass) at [commit `5c5e4c4`](https://github.com/sanskrit-lexicon/MWS/commit/5c5e4c4) (2026-05-27); the final version will be tagged `submission-v1` at submission time.*
