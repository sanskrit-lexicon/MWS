# W1 (a) — unlinked `<ls>` siglum candidates

Enumerates the distinct `<ls>` source abbreviations in live `mw.txt` that have
**no authority link yet**, and proposes a mechanical match to an existing
canonical authority. A **review candidate generator** — it writes
`link_candidates.csv` only and **touches no authority file**.

## Result

- **877** distinct live `<ls>` bare sigla (meta `L.`/`ib.`/`W.`/`MW.`/`Cat.` and
  roman-numeral locators excluded).
- **537 linked**, **340 candidate unlinked**.
- Of the unlinked: **20 high** + **112 medium** confidence are spelling/punctuation
  variants of an existing record (the mechanical wins, e.g. `AV.Pariś.`→`av.pariS`,
  `Ratnāv.`→`ratnA`); **140 no-match** are candidate *new* authorities.
- Self-validation: **0 false positives** among the 40 highest-frequency sigla.

## Method

The linked-check is **dual**, which avoids decoding the legacy digit-encoding in
`linkmwauthorities_init.txt`:
- ASCII sigla (`RV.`, `MBh.`) — matched **verbatim** against the link file's text
  column (col1);
- diacritic sigla (`Pāṇ.`) — transcoded IAST→SLP1 and matched against the canonical
  keys (auth col1 ∪ link col3, e.g. `Pāṇ.`→`pAR`).

Mechanical match = closest canonical key by `difflib` ratio; banded high (≥0.90) /
medium (0.80–0.89) / low (0.70–0.79) / no-match.

## Files

| File | What |
|---|---|
| [`link_candidates.py`](link_candidates.py) | the generator (`python link_candidates.py`) |
| `link_candidates.csv` | siglum, citation count, SLP1, suggested canonical, score, confidence |
| [`LINK_CANDIDATES_SUMMARY.md`](LINK_CANDIDATES_SUMMARY.md) | counts, validation, tiers |

## How to use

`link_candidates.csv` is sorted by citation count. A maintainer reviews; accepted
**high/medium** rows become spelling-variant links to existing records, **no-match**
rows are triaged as candidate new authorities. Adding any of them to
`linkmwauthorities_init.txt` goes through the normal authority workflow — **not
automated here.**

## Known limits

- Compound sigla (`R. (B.)`, `Yājñ., Sch.`) are folded to their base work; a few
  page-style self-citations (`RTL. p.`) and generic sigla (`ŚrS.`) land in
  no-match and need a human call.
- "linked" means *a link row exists*, not that the linked record has a scan target
  (that's layer (c)).
