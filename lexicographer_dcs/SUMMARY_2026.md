# `<ls>L.</ls>` -> DCS-**2026** verification — results

Same 18,930 strict purely-lexicographic MW lemmas, re-joined against the full
DCS-2026 token corpus (5.69M tokens, 270 texts) instead of the DCS-2021 summary.

## Headline
- **5,935 of 18,930 (31.4%) attested in DCS-2026** — up from 5,723 (30.2%) on DCS-2021.
- Net new refutations vs 2021: **+212**.

| DCS-2026 freq band | attested |
|---|--:|
| 5 very-common(1000+) | 1 |
| 4 common(100-999) | 5 |
| 3 uncommon(10-99) | 174 |
| 2 rare(2-9) | 2,150 |
| 1 hapax(1) | 3,605 |

- Strong tier (bands ≥2, non-hapax): **2,330**
- Uncommon-or-better (bands ≥3): **180**

## Cross-snapshot stability
- The headline barely moves across two DCS snapshots:
  **30.2% (DCS-2021) -> 31.4% (DCS-2026)**. NB these are two versions of
  the *same* corpus project (one annotator, Hellwig) — so this controls for
  corpus *version*, not for DCS's own lemmatisation conventions. It is not a
  snapshot artefact, which supports (does not prove) the P3 claim.
- Transcoder validated: only **11 of 5,723** 2021 hits are absent in 2026
  (0.2%, all plain-ASCII SLP1 so not a transcode failure — DCS lemmatization
  drift), against **+223 gross new gains**. A broken IAST->SLP1 join would
  have dropped hundreds, not 11.

## Notes
- Join: DCS-2026 IAST lemma -> SLP1 (greedy longest-match), token-count freq,
  same log10 banding as 2021 -> directly comparable.
- Caveats from the 2021 run still hold: band-1 hapax is weak; top-band
  short strings are homograph collisions; this is lemma-level (lemma-now).
- DCS-2026 has ~90,349 distinct occurring lemmas vs 83,273 in the 2021
  summary, so coverage rises; the delta is the value of the corpus refresh.

_DCS-2026: Oliver Hellwig / DCS, CoNLL-U snapshot in VisualDCS, CC BY._
