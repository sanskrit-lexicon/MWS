# MW block detector — gold-standard scores

Sample: 200 stratified entries (seed 2026). Annotated: 0 (both annotators: 0).

Precision/recall are the detector against the adjudicated gold (blocks both annotators agree on); `disagree` counts block calls where A and B differ (excluded from P/R pending adjudication). `kappa` is Cohen's κ for inter-annotator agreement on that block.

| block | name | TP | FP | FN | disagree | precision | recall | F1 | κ |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F01 | record header | 0 | 0 | 0 | 0 | — | — | — | — |
| F02 | display headword | 0 | 0 | 0 | 0 | — | — | — | — |
| F03 | homophone disambiguator | 0 | 0 | 0 | 0 | — | — | — | — |
| F04 | grammatical category | 0 | 0 | 0 | 0 | — | — | — | — |
| F05 | verb inflection class | 0 | 0 | 0 | 0 | — | — | — | — |
| F06 | etymology root marker | 0 | 0 | 0 | 0 | — | — | — | — |
| F07 | IE cognate | 0 | 0 | 0 | 0 | — | — | — | — |
| F08 | inflection form | 0 | 0 | 0 | 0 | — | — | — | — |
| F09 | editorial commentary | 0 | 0 | 0 | 0 | — | — | — | — |
| F10 | sense gloss | 0 | 0 | 0 | 0 | — | — | — | — |
| F11 | sense division | 0 | 0 | 0 | 0 | — | — | — | — |
| F12 | source citation | 0 | 0 | 0 | 0 | — | — | — | — |
| F13 | hedge marker (L.) | 0 | 0 | 0 | 0 | — | — | — | — |
| F14 | botanical name | 0 | 0 | 0 | 0 | — | — | — | — |
| F15 | biographical content | 0 | 0 | 0 | 0 | — | — | — | — |
| F16 | cross-reference | 0 | 0 | 0 | 0 | — | — | — | — |
| F17 | machine annotation | 0 | 0 | 0 | 0 | — | — | — | — |
| F18 | correction record | 0 | 0 | 0 | 0 | — | — | — | — |

_No annotations yet: fill `annotations.A` / `annotations.B` in `GOLD_SAMPLE.json` and re-run. The table above is the empty harness._
