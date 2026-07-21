# SPEC-5 — W1(a) residuals + issue hygiene (gated items)

_Created: 02-07-2026 · Last updated: 02-07-2026_

**Tier:** Sonnet 5 (`claude-sonnet-5`); §4 is Haiku-grade. **Repos:** MWS (authority files),
csl-orig via `/cologne-correction-queue` ONLY (nothing committed to csl-orig outside the
monthly batch PR).

## §1 — Apply the 02-07 identity verdicts on #217 (GATED on maintainer ack)

Wait for @funderburkjim / @Andhrabharati to react to the 02-07 adjudication comment on
[#217](https://github.com/sanskrit-lexicon/MWS/issues/217). Then, for each acknowledged verdict:

- Variant links into [linkmwauthorities_init.txt](https://github.com/sanskrit-lexicon/MWS/blob/master/mwauthorities/linkmwauthorities_init.txt):
  `Dharmaś.` → `DarmaSarm`; `TaittĀr.` → the Taittirīya-Āraṇyaka record; `Taitt. Up.` → the
  Taittirīya-Up. record; `BṛĀr.` → the Bṛhadāraṇyaka record; `Alaṃkāras.` **relink** to
  `alaMkAras1` (Ruyyaka).
- NEW authority records (follow the existing record grammar): Devī-Purāṇa (`DevīP.`, 39
  cites), Pañcadaśī (Vidyāraṇya, 2), Vratarāja (`Vratar.`, 1), Dharma-Purāṇa (`DharmaP.`, 1),
  Gāruḍopaniṣad (`GārUp.`, 1).
- `Rājyat.` and bare `Pār.`: NO link — open one print-verification note listing both under
  #217 (scan page from `<pc>`), category printchange-candidate.
- Then work the 46 medium-confidence queue in #217 phase-2 comment: apply only items the
  maintainers marked correct; anything contested goes to the August planning list.

## §2 — #86 `&c.` abbreviation correction

[#86](https://github.com/sanskrit-lexicon/MWS/issues/86): @drdhaval2785 approved `<ab>`
tagging in mw.txt. Draft the change (all `&c.` instances per his comment scope), validate +
park via `/cologne-correction-queue mw <changefile>`. Issue comment only AFTER the monthly
batch PR merges.

## §3 — #215 `lex type=` inventory (evidence for the August ruling)

Produce `planning/specs/2026-07/lex_type_inventory.md`: every `<lex type=X>` value in
mw.txt with count, 3 sample records each, and per value: (a) which tools read it
(grep csl-pywork display code, [phw_graph/](https://github.com/sanskrit-lexicon/MWS/tree/master/phw_graph),
funderburkjim/MWlexnorm step0), (b) whether its content is derivable from `<info lex=>`.
**No deletions** — the keep/drop ruling is the August planning session's, per the criteria
in [PLANNING_2026-07.md](https://github.com/sanskrit-lexicon/MWS/blob/master/planning/PLANNING_2026-07.md) §3.

## §4 — Standing-queue hygiene (mechanical)

Close [#168](https://github.com/sanskrit-lexicon/MWS/issues/168) and
[#90](https://github.com/sanskrit-lexicon/MWS/issues/90) as superseded, each with ONE
one-line comment pointing at
[DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DATA_DICTIONARY.md) /
[ENTRY_GUIDE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ENTRY_GUIDE.md)
(ruled in ROADMAP standing queue since 12-06; re-confirmed 02-07). Close
[#218](https://github.com/sanskrit-lexicon/MWS/issues/218) if the maintainers haven't already.

_Dr. Mārcis Gasūns_
