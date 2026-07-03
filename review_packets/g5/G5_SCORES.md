# G5 gold sample — MW block detector scores

_Created: 03-07-2026 · Last updated: 03-07-2026_

Sample: 200 stratified records ([sampling addendum](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/g5/G5_SAMPLING_ADDENDUM.md)), source [mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) pinned @ `392ed6b`. Gold = Pass A (rule-based, Sonnet 5 `claude-sonnet-5`) × Pass B (reading pass, Sonnet 5 `claude-sonnet-5`), every disagreement adjudicated per-record by Fable 5 (`claude-fable-5`) — see [disagreements.csv](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/g5/disagreements.csv). Detector = `detect_blocks()` from `figures/scripts/export_data.py` (docs-pass @ `0901c81`), scorer ported from `analysis/gold_score.py` (docs-pass @ `d0270a4`).

Inter-annotator exact agreement (full block set per record): **85/200** (42.5%). Adjudicated records: 115.

| block | name | support | TP | FP | FN | precision | recall | F1 | κ (A vs B) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F01 | record header | 200 | 200 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 |
| F02 | display headword | 158 | 150 | 20 | 8 | 0.882 | 0.949 | 0.915 | 0.985 |
| F03 | homophone | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 |
| F04 | grammatical category | 129 | 125 | 0 | 4 | 1.000 | 0.969 | 0.984 | 1.000 |
| F05 | verb inflection class | 20 | 20 | 0 | 0 | 1.000 | 1.000 | 1.000 | 0.773 |
| F06 | etymology root | 29 | 28 | 0 | 1 | 1.000 | 0.966 | 0.982 | 0.980 |
| F07 | IE cognate | 2 | 1 | 2 | 1 | 0.333 | 0.500 | 0.400 | 0.662 |
| F08 | inflection form | 45 | 43 | 25 | 2 | 0.632 | 0.956 | 0.761 | 0.322 |
| F09 | editorial commentary | 7 | 6 | 18 | 1 | 0.250 | 0.857 | 0.387 | 0.189 |
| F10 | sense gloss | 200 | 200 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 |
| F11 | sense division | 0 | 0 | 0 | 0 | — | — | — | 1.000 |
| F12 | source citation | 125 | 124 | 48 | 1 | 0.721 | 0.992 | 0.835 | 0.406 |
| F13 | hedge marker (L.) | 50 | 50 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 |
| F14 | botanical | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 |
| F15 | biographical | 36 | 34 | 0 | 2 | 1.000 | 0.944 | 0.971 | 0.929 |
| F16 | cross-reference | 26 | 17 | 1 | 9 | 0.944 | 0.654 | 0.773 | 0.452 |
| F17 | machine annotation | 200 | 200 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 |
| F18 | correction record | 2 | 0 | 0 | 2 | — | 0.000 | — | 1.000 |

Macro precision 0.860, recall 0.870, F1 0.876, mean κ 0.817.

**Low-support warning** (support < 5, too sparse for stable claims): F07, F11, F18.

## Reading notes

- **F12 precision (0.721) is a definitional split, not a detection bug**: the detector counts ANY `<ls>` as F12 (so every `<ls>L.</ls>`-only hedge record fires both F12 and F13); the gold follows G5 spec reviewer rule 4, under which an entry whose only citation is the `L.` hedge is F13 *without* F12. All 48 F12 false positives are hedge-only records.
- **F09 (editorial commentary) is the weakest block measured** (precision 0.250, κ 0.189): no dedicated tag exists, and the detector proxy (any parenthetical ≥ 50 chars) over-fires on inflected-form inventories and identification glosses. This was the paper's own predicted weak spot (§9); it is now measured, not estimated.
- **F08 precision 0.632**: the extra-`<s>`-span proxy also fires on segmented-headword displays, etymon citations, and cross-referenced forms that are not inflections of the headword (κ 0.322 between passes — the reading pass corrected exactly this).
- **F02**: 20 false positives are continuation records whose later `<s>`/`<s1>` spans are not a display headword; all 8 false negatives are display headwords containing `<srs/>` (e.g. `<s>vizayE<srs/>zin</s>`), which the `[^<]+` regex rejects — a fixable detector bug.
- **F04 recall 0.969 / F15 recall 0.944 — literal-string misses**: the detector matches `'<lex>'` and `'<s1>'` literally, so `<lex type="phw">` (4 records) and `<s1 n="...">` (2 records) escape it — fixable detector bugs, same family as F02.
- **F05 measured perfect (P=R=1.000)** despite κ 0.773: the A/B disagreements were all `<info verb=>`-only records; adjudication ruled machine attributes are F17 (reviewer rule 3), which coincides with the detector's print-string rule (`cl.`/`P.`/`Ā.`).
- **F16 recall 0.654**: all 9 false negatives are bare `See X` prose references — the detector has `q.v.`/`cf.`/`id.` rules but no `See` rule. The 1 false positive is an entry-internal `cf. below` (self-reference, not a cross-reference).
- **F18 recall 0.000** (support 2): both correction records in the sample use the `<chg>` markup form; the detector only knows the `{{old -> new}}` inline form.

_Dr. Mārcis Gasūns_
