# Pass A codebook — F01–F18 block-detection rules

_Created: 02-07-2026 · Last updated: 02-07-2026_

Annotator: Sonnet 5 (`claude-sonnet-5`), session `g5-pass-a`. Ground rules
per [G5_GOLD_SAMPLE_SPEC.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/G5_GOLD_SAMPLE_SPEC.md)
§Reviewer Instructions. Sources consulted: the G5 spec itself, `PAPER.md`
§4/§5 (block inventory + kernel/enrichment table), and
[DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DATA_DICTIONARY.md)
(tag family reference). **Not consulted:** any file under
`papers/microanalysis/analysis/` (the detector implementation and its
outputs) — per the isolation rule, this pass reasons from the tag inventory
and the paper's prose block definitions only, not from the existing
classifier's code or numbers.

This is a from-scratch reading of the markup, not a re-implementation of the
existing detector — `annotate_a.py` in this directory is the executable form
of the rules below, run once over the 200-record sample with zero
per-record hand edits (see self-report for why, and for the known
approximation risk this carries).

## Rule table

| Block | Rule | Basis |
|---|---|---|
| F01 Record header | always true | every row has `<L>…<e>` by construction |
| F02 Display headword | a display `<s>` or `<s1>` span appears before the `¦` separator | PAPER.md: 76% carry a rendered display form |
| F03 Homophone marker | `<hom>` tag present | DATA_DICTIONARY `<hom>` |
| F04 Grammatical category | `<lex>` tag present (any form) | DATA_DICTIONARY `<lex>` |
| F05 Verb inflection class | `<ab>cl.</ab>`/`<ab>P.</ab>`/`<ab>Ā.</ab>`, or `info verb="genuineroot\|root\|gati\|nom\|pre"` | DATA_DICTIONARY `verb=` family + abbreviations table (`cl.`/`P.`/`Ā.`) |
| F06 Etymology root | `√` glyph or `<etym>` tag present | DATA_DICTIONARY `<etym>`; `√` is MW's inline root marker |
| F07 IE cognate | `<lang>` or `<gk>` tag present | DATA_DICTIONARY `<lang>`, `<gk>` |
| F08 Inflection form | `info lexcat=` present, **or** more than one display `<s>` span before `¦` (extra principal-part/variant forms), **or** a `Caus./Desid./Intens.` abbreviation | **approximation** — no single tag marks "extra inflected form" outside the lexcat packet; see Limitations |
| F09 Editorial commentary | `<div n="vp"/>` present, or a `cf./prob./fr.` hedge abbreviation | **approximation** — no dedicated commentary tag; see Limitations |
| F10 Sense gloss | non-empty text after `¦`, or a `<div n="to"/>` verbal sense marker | PAPER.md: ~100% |
| F11 Sense division | `<div n="P"\|"p"\|"1"/>` present | DATA_DICTIONARY: `n="P"` (512) is the nominal sub-entry/sense block, distinct from `to`/`vp` |
| F12 Source citation | any `<ls>` tag whose text is **not** `L.` | reviewer rule 4 |
| F13 Hedge L. | any `<ls>L.</ls>` occurrence | reviewer rule 4 |
| F14 Botanical | `<bot>` tag present | DATA_DICTIONARY `<bot>` |
| F15 Biographical | `<bio>` tag present, or `<s1>` present without `<bot>` | DATA_DICTIONARY `<bio>`, `<s1>`; PAPER.md footnote: F15 counts `<bio>` **or** `<s1>` |
| F16 Cross-reference | `<ab>id.</ab>`, `<lex type="phw">`, `phwchild=`/`phwparent=`, or `<pcol>` | reviewer rule 3 (phw digital-graph attrs still count as the *print-visible* cross-ref block, distinct from F17) |
| F17 Machine annotation | any `<info …/>` tag | reviewer rule 3: "treat `<info>` as F17 digital infrastructure" — applied to every `<info>` occurrence, including the `verb=`/`phwchild=` attributes also used as F05/F16 triggers above (a record can be both F05/F16 *and* F17 from the same underlying `<info>` tag — these are independent block presences, not exclusive categories) |
| F18 Correction record | `<chg` tag present | DATA_DICTIONARY `<chg>` structured-correction markup |

## F12/F13 independence (design decision)

The spec's rule 4 disambiguates what a **given** `<ls>L.</ls>` occurrence
means; it does not make F12 and F13 mutually exclusive at the record level.
A record with a named citation for one sense and an `L.` hedge for another
(e.g. `G5-040`, L=9618: `<ls>L.</ls>` on the nominal sense, `<ls>MBh.</ls>`
on the verbal-derivative sense) carries **both** F12 and F13. An earlier
draft of this codebook tried to force a single choice per record and
produced two internally-inconsistent flagged rows; the fix was to treat
every `Fxx` as an independent boolean, matching the spec's own "a row may
carry multiple blocks" instruction.

## Limitations / self-known false-positive-risk (read before scoring)

- **F08 and F09 have no dedicated tag** in `mw.txt` the way F03/F06/F14/F18
  do. The rules above are structural proxies (extra `<s>` spans, specific
  `<div n=>` values, specific `<ab>` hedges) chosen from the tag inventory
  without reference to the existing detector's logic. They likely
  **undercount** both blocks relative to a closer reading of the free-text
  prose (e.g. a parenthetical editorial aside with no `cf./prob./fr.`
  abbreviation would be missed by F09's rule here). This is a known
  precision/recall risk for those two blocks specifically, not the other 16.
- **F11** distinguishes `<div n="P"/>` (nominal sub-entry) from `n="to"`/`n="vp"`
  (folded into F10/F09) per the DATA_DICTIONARY's own gloss of what each `n=`
  value means — not verified against the paper's own <1% headline figure by
  a second, independent read.
- No record in the 200-sample was left blank — every row resolves at least
  F01/F10/F17 mechanically, so there are no missing-value blanks to report.
- This pass was NOT hand-adjusted per-record; it is the codebook's rules
  applied literally and uniformly. That is a deliberate choice (documented
  in the self-report) given session scope, and it is exactly the kind of
  systematic-rule divergence a genuinely independent Pass B — using its own
  reading of the same reviewer instructions — should be able to surface
  against.

_Dr. Mārcis Gasūns_
