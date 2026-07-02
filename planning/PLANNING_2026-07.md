# MWS July 2026 planning session — monthly Fable pass

_Created: 02-07-2026 · Last updated: 02-07-2026_

The monthly frontier-tier planning session scheduled by
[ROADMAP.md](https://github.com/sanskrit-lexicon/MWS/blob/master/ROADMAP.md) §Model-tier policy.
Session: **Fable 5 (`claude-fable-5`)**, 02-07-2026 (window-plan S1,
[handoff](https://github.com/gasyoun/Uprava/blob/main/handoffs/FABLE_S1_MWS_planning.md)).
Outputs: the adjudications below, the re-sequenced July cadence row in ROADMAP.md,
five executable Sonnet specs in [planning/specs/2026-07/](https://github.com/sanskrit-lexicon/MWS/tree/master/planning/specs/2026-07),
and the siglum adjudication batch delivered to csl-atlas
([PR #185](https://github.com/sanskrit-lexicon/csl-atlas/pull/185)).

## State drift since the June pass (what actually happened)

- **W1(a) phases 1–2 DONE 30-06** ([#217](https://github.com/sanskrit-lexicon/MWS/issues/217)):
  537 → 620 linked sigla; 3 high-confidence + 46 medium items pending maintainer calls;
  @Andhrabharati flagged unspecified errors in the phase-2 "definite wrong suggestions" table.
- **W1(b) DONE 30-06** ([#218](https://github.com/sanskrit-lexicon/MWS/issues/218), commit
  [`4c20222`](https://github.com/sanskrit-lexicon/MWS/commit/4c20222)): all 568 authority
  records now carry `<expandNorm>` (was 230).
- **W3 Phase 1 MERGED 20-06** ([csl-apidev#46](https://github.com/sanskrit-lexicon/csl-apidev/pull/46)
  — entries, ids, **and graphql** controllers landed together).
- **W2**: G5 gold-sample spec exists
  ([review_packets/G5_GOLD_SAMPLE_SPEC.md](https://github.com/sanskrit-lexicon/MWS/blob/master/review_packets/G5_GOLD_SAMPLE_SPEC.md));
  **no annotation pass has run** — still the submission blocker. `papers/` now lives on
  master (A16 cover letter fixed to master links, commit `20a19b2`), so the old
  "PAPER.md home: master vs docs-pass" flag is resolved by events;
  [#195](https://github.com/sanskrit-lexicon/MWS/issues/195) (docs-pass merge) remains open.
- New maintainer input: [#215](https://github.com/sanskrit-lexicon/MWS/issues/215)
  (@funderburkjim delegates the `lex type=` value review), [#86](https://github.com/sanskrit-lexicon/MWS/issues/86)
  (@drdhaval2785 approves adding `<ab>` markup in mw.txt).

## Adjudications (queued/deferred/Fable-marked items)

1. **W1 layer priority** (was "awaiting M.G."): **overtaken by events** — layers (a) and (b)
   shipped 30-06. July W1 = **layer (c) scan-link targets**, opening with the
   citation-weight leaders that have unambiguous editions (Suśr., Kathās., ŚBr.), and
   honoring the cross-repo decision-master recommendation to **build the per-work
   page-index first**, then per-citation links → [SPEC-1](https://github.com/sanskrit-lexicon/MWS/blob/master/planning/specs/2026-07/SPEC-1-w1c-scanlink.md).
   Pāṇ. stays excluded until the August sūtra-scheme decision (working recommendation from
   the 02-07 decisions-master triage: ashtadhyayi.com URLs, which would make it agent-doable).
2. **[#217](https://github.com/sanskrit-lexicon/MWS/issues/217) residual identity calls** —
   re-audited against live mw.txt + the authority file; verdicts posted in one comment on
   the issue (02-07). Highlights: `Dharmaś.` = **Dharmaśarmābhyudaya** (kāvya word-gloss
   contexts; `DarmaSarm` record exists; the phase-2 "= Dharmaśāstra" identification was
   wrong — the likely error @Andhrabharati noticed), distinct from `Dharmas.`+section-number
   = **Dharmasaṃgraha** (`Darmas` record); `DevīP.` = **Devī-Purāṇa proper** (MW cites
   `DevībhP.` separately 13×) → needs a NEW authority record; `Vratar.` = **Vratarāja**
   (context: `jñāna-mudrā … Vratar. (AgSaṃh.)` — vrata digest quoting an āgama), not
   Vrata-Prakāśa; `Alaṃkāras.` relink `alaMkAras2` → **`alaMkAras1` (Ruyyaka)** — the
   commentarial tradition (Pratāparudrīya co-cite) attaches to Ruyyaka's text, and the two
   records are rival attributions of the SAME work (record-merge candidate for maintainers);
   `ŚāntiP.` = Śānti-parvan **confirmed by the markup itself** (`<ls n="MBh. xii,">2638</ls>`);
   `Rājyat.` and bare `Pār.` stay **uncertain — print-scan check** (single citations,
   phase-2 rationales unsupported). Application of acknowledged links = [SPEC-5](https://github.com/sanskrit-lexicon/MWS/blob/master/planning/specs/2026-07/SPEC-5-w1a-residuals-hygiene.md).
3. **[#215](https://github.com/sanskrit-lexicon/MWS/issues/215) `lex type=` review** (delegated
   by Jim): decision **criteria fixed now, ruling deferred to the August pass** pending the
   inventory. Keep a `type=` value if (a) an existing consumer reads it (phw graph, display,
   MWlexnorm lineage) or (b) it encodes structure not derivable from `<info lex=>`/`<lex>`
   content (the `phw`/`hwifc`/`hwalt`/`nhw`/`hwinfo`/`part` family per
   [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DATA_DICTIONARY.md));
   drop-candidates = values fully redundant with `<info lex=>`. Inventory = SPEC-5 §3;
   any deletion is a csl-orig change → correction-queue discipline.
4. **[#86](https://github.com/sanskrit-lexicon/MWS/issues/86)**: Dhaval approved `<ab>`
   markup for `&c.` in mw.txt → prepare via `/cologne-correction-queue` (monthly batch;
   csl-orig untouched between batches) — SPEC-5 §2.
5. **Alternate-form markup bundle** ([#178](https://github.com/sanskrit-lexicon/MWS/issues/178)/[#147](https://github.com/sanskrit-lexicon/MWS/issues/147)/[#73](https://github.com/sanskrit-lexicon/MWS/issues/73)):
   **deferred with reason** — display-policy questions owned by the maintainers, no queued
   work depends on them, and adjudicating unprompted would violate the noise discipline.
   Re-surface only if a maintainer engages or W4 track 2 needs the answer.
6. **[#98](https://github.com/sanskrit-lexicon/MWS/issues/98) `id.` resolution**: unchanged —
   sense-level, display-policy-gated; spec-only ([relative_refs/IDEM_NOTE.md](https://github.com/sanskrit-lexicon/MWS/blob/master/relative_refs/IDEM_NOTE.md)).
7. **G5 gold sample**: run the two independent Sonnet annotation passes NOW
   ([SPEC-2](https://github.com/sanskrit-lexicon/MWS/blob/master/planning/specs/2026-07/SPEC-2-g5-annotation.md));
   disagreement adjudication is reserved for the A16 review session (window-plan S2), per
   ROADMAP §W2. G5 remains the sole hard blocker for the end-of-August IJL submission.
8. **W4 siglum batch 1**: **executed this session** (it IS the judgment work) —
   50 families adjudicated + 57 MW layer rulings + editorial reclassification of
   `IW`/`RTL`/`MWB`/`IndSt`, shipped as [csl-atlas PR #185](https://github.com/sanskrit-lexicon/csl-atlas/pull/185)
   with rationale in [SIGLUM_ADJUDICATION_2026-07.md](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/SIGLUM_ADJUDICATION_2026-07.md).
   Integration (fold-rule fix, generator honors the curated table) = [SPEC-4](https://github.com/sanskrit-lexicon/MWS/blob/master/planning/specs/2026-07/SPEC-4-siglum-apply.md).
9. **Quick-win queue**: #192/#183/#179 have agent research posted (27-06), awaiting
   maintainer reaction — no action; [#168](https://github.com/sanskrit-lexicon/MWS/issues/168)/[#90](https://github.com/sanskrit-lexicon/MWS/issues/90)
   close-as-superseded goes to SPEC-5 §4.
10. **Local checkout hygiene**: untracked `prefaces/mwepref01–11.md` + scan crops sit in the
    working tree (leftover of a preface-OCR session that never committed the MW-English
    prefaces). M.G. decides commit-vs-discard — mirrored to GTD; agents must not delete.

## July cadence (resequenced — supersedes the Jun-12 row)

| W1 authority | W2 paper | W3 Salt API | W4 template |
|---|---|---|---|
| Layer (c): per-work scan+page index, then records for Suśr., Kathās., ŚBr. (SPEC-1); apply #217 links on maintainer ack (SPEC-5) | G5 annotation pass ×2 (SPEC-2); S2 Fable hostile review + G5 adjudication; #195 docs-pass merge decision in S2 | C-SALT parity report; Phase-2 closeout + clean-URL start (SPEC-3) | Batch-1 verdicts shipped (PR #185); fold-rule fix + curated-table integration + candidates regen (SPEC-4) |

## Model provenance

Planning + all adjudications this session: **Fable 5 (`claude-fable-5`)**. Specs are written
for **Sonnet 5 (`claude-sonnet-5`)** execution (SPEC-2 explicitly two independent sessions);
Haiku-tier only where a spec marks a step mechanical. Prior candidate generation:
Haiku-tier `siglum_families.py` run (csl-atlas).

_Dr. Mārcis Gasūns_
