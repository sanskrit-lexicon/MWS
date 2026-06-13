# 3-way verbal-root crosswalk: MW ↔ Whitney ↔ DCS

## MW side
- MW genuine-root records (`verb="genuineroot"`): **750**
- …with a Whitney anchor (`<info whitneyroots>`): 813
- …with a Westergaard anchor (`<info westergaard>`): 1,362
- Distinct MW-anchored roots matched to the hub: 734;
  **unmatched (candidate anchor errors): 3** → `mw_whitney_unmatched.csv`

## Coverage of the 935-root Whitney hub
- Attested in **MW**: **809** (86.5%)
- Attested in **DCS** corpus: **590** (63.1%)
- **In BOTH MW and DCS (fully triangulated): 550** (58.8%)
- MW+Whitney but **DCS-absent** (grammarian/lexical roots): 259
- DCS+Whitney but **MW-unanchored** (anchoring gap to close): 40
- In neither MW nor DCS: 86

## Why it matters
- The fully-triangulated roots (MW gloss + Whitney grammar + DCS frequency)
  are the ready core of the grammar-corpus-dict crosswalk: a root you can
  define, conjugate, and frequency-rank at once.
- Roots in Whitney+DCS but NOT anchored in MW are the gap to close (add the
  `<info whitneyroots>` anchor); roots in MW+Whitney but DCS-unmatched are
  corpus-absent (lexical/grammarian roots) — a P3/P4 signal.

## Notes
- Join is on homonym-normalised root string (MW `akz1`/`akz2` ↔ hub `1 akṣ`).
- The number in `whitneyroots="root,N"` is Whitney's 1885 root-appendix page
  (max 210, many roots share a page), NOT a root id — decoded here.
- `mw_whitney_unmatched.csv` are MW anchors with no hub root after
  normalisation: either MW-side typos or roots absent from the hub.
