# Register-B corpus test (the indigenous `iti` register)

Extends the P3 [synthesis](../SYNTHESIS.md) to **Register B** — the in-prose
`iti <source>` quotative of the Sanskrit-Sanskrit dictionaries **SKD**
(Śabdakalpadruma) and **VCP** (Vācaspatya), which carry ~0 `<ls>` tags. The
genuinely novel extension flagged in the synthesis.

## Two findings

1. **Register B is constitutively lexicographic.** Of SKD's 45,193 `iti`
   citations, **40.5%** (a floor) target a named kośa / nighaṇṭu — `rājanighaṇṭu`
   (4,095), `medinī` (3,186), `hemacandra` (2,601), `śabdaratnāvalī`,
   `kavikalpadruma`, … — not literary texts. Where MW marks lexicographer-only
   material with the *exceptional* `<ls>L.</ls>` hedge (13%), the indigenous
   register cites lexicons by **default**. The hedge flags as exceptional what is
   Register B's norm. *(This is the qualitative, robust result; it needs no corpus.)*

2. **That vocabulary is, nonetheless, ~half corpus-grounded.** **SKD 51.3%**,
   **VCP 48.9%** of headwords occur in DCS. So the lexical *citation style* does
   not imply a corpus-detached *vocabulary*.

## Method & the artifact caught

Headwords (`<k1>`) and DCS-2021 lemma keys are both SLP1. But **SKD cites
headwords in nominative-singular form** (`aMSaH`, `aMSakaM`, `aMSuH`) while DCS
lemmas are bare stems — a naive match scored SKD at a spurious **13.8%**. A
stem-aware match (strip visarga / anusvāra) recovers the real **51.3%**; the same
de-inflection leaves bare-stem VCP **unchanged (48.9%→48.9%)**, which is the
control proving it corrects rather than inflates.

## Caveats (load-bearing)

- **MW is context, not a benchmark.** Its 29.5% is over 194k headwords (~4× the
  indigenous inventories) and diluted by compound-heavy macrostructure — do *not*
  read "indigenous > MW".
- Lemma-level; attestation is for *any* sense (homograph exposure); SKD depends on
  the stem-recovery heuristic.
- VCP's lexical-citation share is **unmeasured** — the kośa list is SKD-derived and
  VCP's source vocabulary differs (its 0.0% is an artifact, not a finding).

## Files

| File | What |
|---|---|
| [`register_b_dcs.py`](register_b_dcs.py) | the test (`python register_b_dcs.py`) |
| `register_b_summary.csv` | per-dict records, headwords, `iti`→kośa %, DCS % |
| [`REGISTER_B_SUMMARY.md`](REGISTER_B_SUMMARY.md) | findings + caveats |

Cross-dict work — conceptual home is **csl-atlas**; kept here with the P3 evidence
for now (placement deferred, per [ANALYSIS.md](../../../ANALYSIS.md)).
