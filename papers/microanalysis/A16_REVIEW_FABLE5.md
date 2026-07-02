# A16 — referee-style hostile review (pre-submission)

_Created: 02-07-2026 · Last updated: 02-07-2026_

Substantive review of
[PAPER.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md)
("The microstructure of *Monier-Williams 1899*") by Fable 5 (`claude-fable-5`), 02-07-2026,
Fable window session S2 — the final hostile-review pass reserved for Fable in
[ROADMAP.md §W2](https://github.com/sanskrit-lexicon/MWS/blob/master/ROADMAP.md). Target venue:
**International Journal of Lexicography** (OUP), submission target end of August 2026. Format
modeled on
[A44_review_fable5.md](https://github.com/drdhaval2785/SanskritSpellCheck/blob/master/papers/A44_review_fable5.md).
Every number-check below was re-run against the live artefacts this session, not taken from the
paper's own self-reports.

**Overall verdict: the paper is genuinely IJL-shaped — it speaks lexicography, not NLP, and its
two lasting assets (the 8×3 profile table and the three-stage genealogy of the `L.` hedge) are
exactly what IJL publishes. But it currently rests every percentage on an unvalidated detector
while promising, in its own §9, a validation that exists only as two rival half-built
instruments; and its reference list contains the same class of unverifiable citation that D20
already caught once. The August target holds only if G5 Pass B runs within ~2 weeks. Two
revision sessions after G5 closes, plus a citation-verification pass, reach submittable.**

## Major (must fix before submission)

1. **The G5 gold sample is the submission blocker, and the paper says so itself.** §9.1 and
   §9.6 admit the per-entry validation "still awaits per-entry Sanskritist review" and ask the
   reader to trust "±2–4 pts". An IJL referee will not: the two *known* over-counts are not
   small (36.5 % of F08 hits are compound members, not inflected forms; 66.7 % of F09 hits fire
   outside any philological context — the paper's own SPOTCHECK numbers), yet §4's headline
   table still prints F08 = 21 % and F09 = 6 % uncorrected, and §5.3's root profile prints
   F08 = 99.9 % / F09 = 78.1 % from the same detector. Until measured precision/recall per
   block exists, every table in §4–§5 is exposed. **Status as of this review: Pass A is done
   (200/200, [PR #221](https://github.com/sanskrit-lexicon/MWS/pull/221), unmerged); Pass B
   has not run; adjudication therefore cannot happen yet. G5 remains open and is the single
   item that can sink the August date.** Once scored, either fold corrected rates into §4/§5
   or print detector-raw + measured-precision side by side — do not leave known-inflated
   numbers as headlines with the correction buried in §9.

2. **There are two rival gold-standard instruments in the repo; the paper must end up citing
   exactly one.**
   [analysis/GOLD_SAMPLE.json](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/GOLD_STANDARD.md)
   (merged to docs-pass via [PR #207](https://github.com/sanskrit-lexicon/MWS/pull/207):
   seed 2026, 15-type round-robin, error-only marking, **0 annotations**) versus
   [review_packets/g5/](https://github.com/sanskrit-lexicon/MWS/tree/master/review_packets/g5)
   (seed 20260702, the 8 spec strata, full block-list annotation, Pass A complete). Different
   200 records, different schema. **Ruling (Fable S2): `review_packets/g5/` is canonical** —
   it has the pinned source commit (`392ed6b`, 286,525 records), the spec lineage
   ([G5_GOLD_SAMPLE_SPEC.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/G5_GOLD_SAMPLE_SPEC.md)
   + [addendum](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/g5/G5_SAMPLING_ADDENDUM.md)),
   and a completed pass. Mark the `analysis/` harness superseded (banner in GOLD_STANDARD.md),
   but **port its scoring design** — per-block precision/recall/F1 *plus Cohen's κ*
   ([gold_score.py](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/gold_score.py))
   — onto the g5 CSV: the G5 spec's own scoring section stops at P/R, and the κ column is
   what lets the paper state inter-annotator reliability, which IJL referees increasingly ask
   for.

3. **Pass A is not an annotation in the referee's sense — plan Pass B accordingly.** Pass A
   ([CODEBOOK_A.md](https://github.com/sanskrit-lexicon/MWS/blob/g5-pass-a/review_packets/g5/pass_a/CODEBOOK_A.md))
   was a from-scratch *rule set executed once* (`annotate_a.py`), zero per-record judgment —
   honestly self-flagged, and defensible as one arm of the design. But if Pass B is built the
   same way, the "gold standard" is two regex families agreeing with each other, and κ between
   two rule systems measures nothing a referee will accept as ground truth. **Ruling: Pass B
   must be a per-record *reading* pass — the annotator reads each of the 200 records and
   assigns blocks by judgment, codebook allowed as a checklist but no blanket script, and must
   flag hard cases in `notes`.** The final design is then: one auditable rule-based arm + one
   reading arm + Fable adjudication of disagreements — describable honestly in the paper. (The
   [Pass B handoff](https://github.com/gasyoun/Uprava/blob/main/handoffs/SONNET_MWS_SPEC2_g5_pass_b.md)
   has been amended with this constraint in the same session as this review.)

4. **Verifiable-number defects found this session (all re-measured against `mw.txt`):**
   - §5.2 says lex-hedged = "40,212 **distinct entries**". 40,212 is the *instance* count;
     the distinct-record count is **39,962** (250 records carry the hedge more than once).
     §9.4's "appears 40,212×" is the correct usage; §5.2 needs the entry-level number (and
     14.0 % → 13.9 %).
   - §5.1 defines compounds as 126,360 = 44.10 % (`<e>3*` + em-dash) while Appendix B.1 says
     "50.4 % are compounds (`<e>3*`)" — re-measured: 144,443 = 50.4 % on the bare-`<e>3`
     predicate. Both are defensible; printing both without a one-line reconciliation is a
     referee catch. State once that the *type* uses the narrower predicate and B.1 the raw
     hierarchy code.
   - **8 vs 9 primary types.** The title framing, abstract, and Construct 3 all say "8 primary
     article types"; §5.1's table has **9** (verbal lemma added per D18) plus a residual; and
     §5.4's profile table has neither a verbal-lemma row nor consistent row count (encyclopedic
     split into two rows). Pick one number, propagate it everywhere, and add the missing
     verbal-lemma profile row to §5.4 — as it stands the paper's central table omits one of its
     own types.
   - **Record count / reproducibility pin.** The paper says 286,561 (fetched 2026-05-23);
     live `mw.txt` is now 286,525 (the G5 pinned commit). "All numerical claims are
     reproducible from the published mw.txt" is false without a commit hash — pin
     `csl-orig` @ the snapshot used in §2, and stamp every figure caption's "CDSL 2026-05-24"
     consistently with it.

5. **Citation integrity — the Reichmann-1999 class of problem is still present.** D20 caught
   and removed one unverifiable citation; this pass finds more of the same class:
   - Appendix A.1 cites "Wiegand (1989: 416–425)" for the additive/semi-integrated/integrated
     microstructure distinction, but the reference list's Wiegand 1989 is the *Makrostruktur*
     article, HSK 5.1: **371–409** — the cited pages fall outside the cited article. The
     microstructure-types source is a different HSK 5.1 piece (Wiegand's microstructure survey
     or Hausmann & Wiegand's "Component parts", already in the list). Fix the pointer.
   - A.2 cites "Wiegand 1995" — **no such entry in the references.**
   - "Hausmann, F. J. (1985). *Lexikographie*. In HSK" is incomplete (no volume/pages) and
     chronologically suspicious — the HSK dictionary volumes began 1989; Hausmann 1985 is
     likely *Lexikographie* in a different handbook. Verify against the physical source.
   - "Schreyer, R. (1985). *Sanskrit Dictionary-Making: A Critical Bibliography of the European
     Tradition*. Brill", "Scharf & Hyman (2009–2011). *Encoding Sanskrit dictionaries: report
     from the Cologne project*", and "Funderburk, Malten & Scharf (2014)" — none of these could
     be verified this session; the first has no trace I can find and reads like a phantom
     (Vogel 1979 *Indian Lexicography* is the real critical survey of the field and is oddly
     absent). **Verify each against library records or remove — a fabricated reference in an
     OUP journal is a desk-reject with reputational tail.**
   - Apresjan 2002, Hanks 2013, Hartmann 2001 are in the references but never cited in the
     body; IJL copy-editing will strip them — cite or cut.
   - The four Atkins & Rundell page cites (2008: 168, 199, 263, 386) need one human pass with
     the book open; they carry load-bearing claims (run-on-compound policy, learner-density
     4–5, register-tracking recommendation).

6. **Figures are numbered 5 and 6; there are no Figures 1–4 in the paper.** Either renumber to
   1–2 or pull in the four missing figures (the heatmap/sankey/treemap set exists in
   [figures/](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass/papers/microanalysis/figures)
   and §5.4 would genuinely benefit from the block-by-type heatmap). Also note IJL wants
   figures as separate files with captions, not inline markdown.

7. **The paper's own consistency gate is red.** `analysis/check_docs.py` currently reports
   **22 broken links, 4 of them in PAPER.md itself** (all `DOUBTS.md#d…` anchors that drifted
   when DOUBTS headings were edited). W2 step 2 says "re-run check_docs.py"; it must pass
   before formatting. Trivial to fix, embarrassing to ship.

8. **Repo voice must become journal voice.** Relative links (`MICROANALYSIS.md`,
   `analysis/SPOTCHECK.md`, `DOUBTS D5`) cannot survive submission: the supplement pipeline
   ([make_supplement.py](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/make_supplement.py)
   + manifest) exists — cite an archived, DOI'd supplement (Zenodo) and convert every repo link
   to a supplement pointer. Kill the lab-notebook register where it leaks: "exactly as feared"
   (§9.3), "docs-pass build artefacts" (§2), the D-number cross-references. And the §1
   salami-slicing paragraph *defends against an accusation no referee has made yet* while the
   closing note (line 325) advertises that four parallel drafts exist — move that provenance to
   the supplement README; in the paper it plants the very doubt it argues against.

## Minor

- The abstract is ~280 words, one paragraph, and contains raw XML (`<ls>L.</ls>`). IJL
  abstracts run tighter (~150–250); write the hedge as "the *L.* hedge" and save markup for §2.
  Its final sentence also has a dangling antecedent ("an organising principle distinguishing
  19th-century scholarly dictionaries…" — the hedge distinguishes *MW*; block economy is what
  generalises).
- Title drift: ROADMAP W2 calls the paper "The block economy of Monier-Williams"; the draft's
  title is "The microstructure of Monier-Williams 1899…". The block-economy title is the
  quotable one; the current title promises a generic microstructure study and hides the thesis.
- §4's F13 row says 13 %; §5.2 says ≈ 14.0 % (really 13.9 %) — same construct, two numbers.
- The self-description "~7.4K words" (line 3) is stale: the file measures ≈ 8.6K words with
  appendices and references (body ≈ 6.2K). Still inside IJL's window, but re-measure after
  revision and update the cover letter.
- "Three witnesses" / "three *independent* framings" (§1, §7.4) overclaims: the three
  traditions are independent of each other, but all three applications were performed by the
  same analyst on the same data. Convergence is still evidence — of category-fit, not of
  independent replication. One honest sentence disarms the referee who would otherwise write
  this paragraph for you.
- B.2's "a remarkable forward-compatibility, perhaps not by design" — either make the point
  (print adjacency-compression turns out to be digital-retrieval-ready) or cut the aside.
- Glaser & Strauss 1967 is cited to license "grounded" — a lexicography referee may bristle at
  the sociology import. One sentence ("grounded in the loose, not doctrinal, sense") suffices.
- The em-dash example in B.1 (`aMSu—jAla`) renders SLP1 to a lexicographer audience with no
  gloss — add IAST in parentheses at first SLP1 use, and say once that SLP1 is the
  transliteration of the digital edition.

## What is genuinely strong — keep and foreground

The **8×3 profile table (§5.4)** is the paper's deliverable and the abstract should say so in
one sentence — it is reproducible for any CDSL dictionary and is the piece a working
lexicographer will actually reuse. The **three-stage hedge genealogy** (Benfey 1866 dagger →
MW 1872 preface declaration → Cappeller 1891 systematic asterisk → MW 1899 tagged citation,
§7.2(ii)/C.2, verified against the prefaces in LS_HEDGE_CHECK) is real philology and the
paper's most citable scholarly finding; the attribution-honesty paragraph on Benfey's asterisk
is exactly the tone IJL rewards. The **pre-registered ≥ 5 pt + FDR relevance threshold**
(§9.2) is referee-proofing rarely seen in digital-humanities submissions — keep it prominent.
The **infrastructure construct** (§6) is a genuinely novel, transferable category, and the
paper is right to claim it as such. The D20 footnote publicly removing an unverifiable
citation is a credibility asset — extend that same standard to the references flagged in
Major 5.

## G5 adjudication status (assigned to Fable by name, ROADMAP §W2)

**Cannot run yet: only one pass exists.** What exists as of 02-07-2026: the pinned sampler +
skeleton (merged, [#220](https://github.com/sanskrit-lexicon/MWS/pull/220)); Pass A 200/200
rule-based ([#221](https://github.com/sanskrit-lexicon/MWS/pull/221), correctly unmerged
pending Pass B); the Pass B spec and one-line-start handoff (amended this session per Major 3).
**G5 is the submission blocker — plainly: no Pass B, no adjudication, no measured
precision/recall, no submission.** The adjudication itself is one Fable session once
`disagreements.csv` exists, and the scorer port (Major 2) can be done by the same session.

## Ruling on [#195](https://github.com/sanskrit-lexicon/MWS/issues/195) (docs-pass merge)

Recommend **merge docs-pass → master before IJL formatting**, with a courtesy deadline: the
branch has been open for maintainer review since 2026-05; if no objection from
@funderburkjim/@Andhrabharati by end of July, merge. Reasons: (i) the paper's §2 cites
"docs-pass build artefacts" — cited URLs must be stable before the supplement is cut (W2 step
3 says exactly this); (ii) the H1–H10 maintenance pass has run, so the branch is at its most
mergeable; (iii) a long-lived docs branch rots with every master commit. MWS is our repo — this
is not a csl-orig-style write restriction — but the merge stays maintainer-gated as a courtesy,
not as a hard block.

## Does end-of-August hold?

**Yes, conditionally.** The critical path is: G5 Pass B (1 Sonnet session, runnable today) →
Pass A/B merge + disagreements.csv (mechanical) → Fable adjudication + scorer + fold numbers
into §4/§5/§9 (1 session) → revision session for Major 4–8 + Minor (1–2 sessions) → citation
verification (human, with the A&R book and library access — **longest human lead time, start
now**) → #195 merge → IJL formatting + supplement DOI → submit. That is ~4 agent sessions plus
two human actions (citation check, submission), comfortably inside July–August **iff Pass B
runs within ~2 weeks**. If Pass B slips past mid-July, the August date slips with it.

## Priority order

(1) Pass B — schedule first, longest dependency chain. (5) citation verification — start in
parallel, longest *human* lead time. (7) check_docs fixes and (4) number fixes are one
mechanical session each and can ride the next revision commit. (2)/(3) are rulings — done in
this review, execute during adjudication. (6), (8) and all Minor items belong to the
IJL-formatting session after G5 numbers land.

_Review: Fable 5 (`claude-fable-5`) · paper: Dr. Mārcis Gasūns_
