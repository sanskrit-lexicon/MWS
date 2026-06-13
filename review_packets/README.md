# Verification review-packets

Turnkey sheets so a Sanskritist can **verify** the session's *mechanical* findings
with yes/no judgements — no lookups required. They attack the red-team's central
gap ([RED_TEAM.md](../papers/RED_TEAM.md) M2): `resolvable` / `attested` /
`triangulated` are algorithm outputs, not verified facts. Each packet is a readable
`.md` sheet (with a blank `Verdict:` per item) plus a `.csv` (blank `verdict`
column) for spreadsheet entry. **Analysis only — nothing is written back.**

## The three packets

| Packet | Items | The judgement | Files |
|---|--:|---|---|
| **B — band-3 `L.`→DCS** | 167 | Does the **DCS example sentence** use MW's word in MW's sense (confirm) or a **homograph** (reject)? | [PACKET_B_band3.md](PACKET_B_band3.md) / `.csv` |
| **A — `ib.` resolution** | 50 | Is the resolved source the one MW *meant*? (35 high-confidence + 15 to scrutinise) | [PACKET_A_ib.md](PACKET_A_ib.md) / `.csv` |
| **C — class conflicts** | 32 | Which conjugation class is right — MW / Whitney / both / other? | [PACKET_C_classconflicts.md](PACKET_C_classconflicts.md) / `.csv` |

**Packet B is the one to start with** — it supplies *sense-level* evidence (a real
corpus sentence per lemma), which is exactly what settles the homograph question
the lemma-level join cannot. 166 of 167 lemmas have a DCS sentence. Example:

> **agnijāra** — MW (L.-only): *N. of a frothy substance on the sea*.
> DCS: *…so'gnijāra iti smṛtaḥ* → the corpus **defines** the word → **confirm**.

vs.

> **abāla** — MW (L.-only): *cocoa-nut*. DCS: *bālo 'pyabālacaritaḥ…* → a different
> word (*a-bāla* "not-child") → likely **homograph, reject**.

## What a verdict unlocks

- **B confirmed** band-3 lemmas → the publication-ready core of the P3 `L.`-recoverability
  claim (currently lemma-level only).
- **A confirmed** sample → lets the `ib.` resolver's 57.1% be reported as *verified*,
  not just *resolvable*.
- **C resolved** conflicts → real grammar findings for P4 / the crosswalk; note many
  are homonym-conflation artefacts (e.g. `√as` cl. 2 vs 4 = the two homonyms), which
  the sheet exposes.

## Notes

- Packet C shows the Dhātupāṭha (Westergaard) reference where MW records one — the
  indigenous tiebreaker (18 of 32 have it).
- Sanskrit in glosses is SLP1 (as in the source); headwords are shown in IAST.
- Built by [`build_packets.py`](build_packets.py) from the committed module outputs +
  `dcs_full.sqlite`. Re-runnable.
