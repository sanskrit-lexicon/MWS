# Adversarial red-team — 2026-06-13 session findings

A hostile-reviewer pass over the session's eight deliverables: where would a
*Dictionaries* / IJL referee break each? Severity: 🔴 **needs work** (a referee
would catch it — fix before any paper) · 🟡 **survives with a wording fix** · 🟢
**survives** (well-controlled, or an explicit worklist that makes no claim).

## Verdict at a glance

| Finding | Sharpest attack | Verdict |
|---|---|---|
| Sense-as-record (P1 §4.1) | "92,670 senses" conflated compound/derived **sub-entries** with senses | 🔴 → **fixed** (now 20,152 base-continuation senses; 72,518 reframed as macrostructure) |
| `ib.` resolver 74.7% | "resolvable" ≠ "correctly resolved"; no ground-truth sample | 🔴 needs a validation sample |
| `L.`→DCS 31% | "two **independent** corpora" overstates — both are DCS (one annotator) | 🟡 reword |
| Root crosswalk 550 / class 32 | bare-root union conflates homonyms; "agree" inflated by lenient union | 🟡 reword (already half-caveated) |
| Register-B 50.3% / 46.7% | SKD de-inflection is lossy; kośa/text binary is fuzzy | 🟡 frame as approximate |
| phw 31 broken links | might be parser artifacts (missed decimal records) | 🟢 **verified real** (targets grep to 0) |
| Botanical 1,528 | residual homograph risk | 🟢 controlled; clean band-2/3 |
| `<ls>` link candidates 340 | tail (low-freq) false positives unvalidated | 🟢 explicit worklist, no claim |

## 🔴 Needs work

**1. Sense-as-record (P1 §4.1).** The claim cited **92,670** letter-`<e>` records
as "continuation senses." Breakdown: `<e>1*` = 20,152 (true base-headword sense
runs), `<e>2*` = 39,619 (derived), `<e>3*` = 32,278 (**compound sub-entries —
distinct lemmas, not senses**). Citing 92,670 as senses conflated MW's
*macrostructure* (deep-headword promotion of compounds/derivatives) with
*polysemy*. **Fixed in §4.1**: senses = the 20,152 `<e>1*` runs; the 72,518
derived/compound records are reframed as the macrostructural strategy. Residual,
minor: "one `¦` per record" = one *gloss-zone*, and a gloss-zone can still hold
multiple `;`-separated prose senses — so the strongest honest claim is
"record-granular sense **promotion**," not "one record = exactly one sense."

**2. `ib.` resolver.** "74.7% resolve to a real source" is a **mechanical**
outcome — the document-order walk *finds* an antecedent; whether that antecedent
is the source MW *meant* is unverified. No hand-checked sample was committed, and
42.9% cross a headword boundary (weaker). Fix before any P3 use: hand-verify ~50
`ib.` against the print/antecedent, and lead with the same-cluster **57.1%** as
the high-confidence core, not the 74.7% headline.

## 🟡 Survives with a wording fix

**3. `L.`→DCS 31%.** Solid, but: (a) "stable across two **independent** corpus
snapshots" overstates — DCS-2021 and DCS-2026 share one annotator (Hellwig) and
one lemmatisation convention; say "two DCS snapshots," drop "independent." (b)
"corpus-attested" should be "DCS-attested" (one corpus, not the textual record at
large). (c) band-1 hapax (3,485 of 5,723) remain weak — already flagged, keep it
load-bearing.

**4. Root crosswalk / class concordance.** "550 fully triangulated" is **bare-root**
coverage — the homonym-collapsing join (`akz1`/`akz2` → `akṣ`) does not prove the
three sources mean the *same* homonym. The class "94.4% agree/overlap" is inflated
by unioning hub classes over homonyms (lenient). Fix: frame 550 as "roots present
in all three by bare-root match," and the 32 conflicts as *candidates*, not
confirmed disagreements. (Both partly caveated already.)

**5. Register-B.** The qualitative headline (constitutively lexicographic, SKD
46.7% `iti`→kośa) is robust. Two soft spots: the **50.3%** depends on a lossy
visarga/anusvāra de-inflection (the VCP-unchanged control validates *direction*,
not *precision* — treat as ±a few pts); and the lexicon/text binary is fuzzy
(`Bhāvaprakāśa` is a medical *text* with a nighaṇṭu section). State 46.7% as a
floor *and* a soft-edged one.

## 🟢 Survives

**6. phw 31 broken links** — verified real (the dangling targets `167759.1`,
`95539.11`, `134516.1` grep to 0 records); 99.3% reciprocal is clean.
**7. Botanical 1,528** — homograph-controlled (botanical-only headwords); band-2/3
examples are unambiguous plant lemmas.
**8. `<ls>` link candidates** — an explicit *review worklist* with a self-validation
gate (0 false positives in top-40); the unvalidated low-frequency tail is disclosed,
and it makes no standalone claim.
**9. DATA_DICTIONARY** — documentation, low attack surface; minor unverified glosses
to hedge: `hui` ("role not confirmed" — good), the `<div n="P">` reading, and
`<ns>` = "community label" (my gloss from the values, not a maintainer source).

## Meta-findings (the systemic risks)

- **M1 — scrutiny was inversely correlated with destination.** The *weakest*
  finding (sense-as-record) is the one that went **into the paper**, because it
  felt obviously true and got the least adversarial check. Lesson: paper-bound
  claims need *more* pre-scrutiny, not less. (Now corrected.)
- **M2 — "mechanical" is being read as "verified."** `resolvable` / `attested` /
  `triangulated` / `agree` are all *algorithm outputs*. Only one (phw) has a
  spot-check. **Every headline needs a small hand-checked sample before it is
  referee-proof** — this is the single biggest gap across the session, and most of
  it needs a Sanskritist, not a model.
- **M3 — the homograph / form-mismatch artifact family was caught 4× reactively**
  (L.→DCS, botanical, SKD nominative, legacy `<ls>` encoding) — always by noticing
  a *surprising number*, never by design. Where it was **not** surprising, it may
  still lurk (the root bare-root union; SKD de-inflection precision). A clean
  finding is not proof the control was unnecessary.
