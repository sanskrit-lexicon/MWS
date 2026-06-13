# 3-way verbal-root crosswalk: MW ↔ Whitney ↔ DCS

Joins MW's verbal roots to the [WhitneyRoots](../../WhitneyRoots) hub (935 roots)
and, through it, to the DCS corpus — Layer-1 of the grammar-corpus-dict crosswalk.
A root you can **define** (MW), **conjugate** (Whitney), and **frequency-rank**
(DCS) at once.

## How

MW anchors roots via `<info whitneyroots="root,page"/>` (the number is Whitney's
1885 root-appendix **page**, not a root id — decoded here; max 210, many roots per
page). The join is on the homonym-normalised root string (MW `akz1`/`akz2` ↔ hub
`1 akṣ`/`2 akṣ`), SLP1→IAST. The Whitney↔DCS half is already in
[`WhitneyRoots/src/dcs_freq.json`](../../WhitneyRoots/src/dcs_freq.json).

## Result — coverage of the 935 Whitney roots

| Layer | roots | % |
|---|--:|--:|
| In **MW** (anchored) | 809 | 86.5% |
| In **DCS** corpus | 590 | 63.1% |
| **Fully triangulated (MW+Whitney+DCS)** | **550** | **58.8%** |
| MW+Whitney, DCS-absent (grammarian/lexical roots → P3/P4 signal) | 259 | |
| DCS+Whitney, MW-unanchored (**anchoring gap to close**) | 40 | |
| neither | 86 | |

Anchoring integrity is near-perfect: only **3** MW anchors fail to match the hub
after normalisation (`jañj`, `thurv`, `riṅkh` — candidate typos/hub gaps,
`mw_whitney_unmatched.csv`).

## Two actionable gaps

- **40 anchoring-gap roots** — in DCS + Whitney but missing MW's `<info
  whitneyroots>` tag, including common verbs MW certainly has (`kath` "narrate"
  freq 57, `chad` freq 270, `ī` freq 192). A small markup-completeness batch.
- **259 corpus-absent roots** — MW + Whitney attest them but DCS has none: the
  grammarian/lexical roots, a direct signal for P3 (citation registers) / P4.

## Companion: conjugation-class concordance

[`class_concordance.py`](class_concordance.py) cross-checks the conjugation class
MW assigns (`cp="1P,1Ā"` → {1}) against Whitney's (`classes` roman → arabic), for
the 570 roots both anchor. **94.4% agree or overlap** (302 agree, 236 overlap);
only **32 genuine conflicts** (disjoint class sets) — research signals behind the
Whitney class-verdict review / P4. 18 of the 32 also carry a Westergaard/Dhātupāṭha
anchor, whose indigenous gaṇa can adjudicate. (`cp="0…"` = "no gaṇa assigned" is
treated as a sentinel, not a class. Homonym-rich roots like `kṛ`/`hṛ` may reflect
hub class-completeness rather than true disagreement — see the summary caveat.)

## Files

| File | What |
|---|---|
| [`root_crosswalk.py`](root_crosswalk.py) | builds the crosswalk (`python root_crosswalk.py`) |
| `root_crosswalk.csv` | per Whitney root: id, root, in_MW, mw_L, mw_classes, dcs_status, dcs_freq |
| `mw_whitney_unmatched.csv` | the 3 MW anchors with no hub match |
| [`ROOT_CROSSWALK_SUMMARY.md`](ROOT_CROSSWALK_SUMMARY.md) | the crosswalk numbers |
| [`class_concordance.py`](class_concordance.py) / `class_concordance.csv` | MW-vs-Whitney class check |
| [`CLASS_CONCORDANCE_SUMMARY.md`](CLASS_CONCORDANCE_SUMMARY.md) | concordance numbers + the 32 conflicts |

Analysis only — no `mw.txt` mutation. The Westergaard `GG.SSSS` third field
(range 01–35, not the 1–10 gaṇa) is left undecoded rather than guessed.
