# G5 gold-sample annotation — Pass B self-report

_Created: 02-07-2026 · Last updated: 02-07-2026_

**Annotator:** Sonnet 5 (`claude-sonnet-5`), single session, branch `g5-pass-b`.
**Isolation:** did not read `review_packets/g5/pass_a/`, branch `g5-pass-a` (including its PR),
or `papers/microanalysis/analysis/` at any point during this pass.

## Method — corrected mid-session per the Fable S2 ruling

**First attempt (superseded).** I initially built a regex-based extraction script against the
full source text and produced `gold_blocks_B` mechanically from marker presence/absence. While
verifying it, I pulled the latest [`Uprava`](https://github.com/gasyoun/Uprava) state and
discovered the handoff had been amended, mid-session, by a concurrent Fable S2 run: **Pass A
turned out to be script-based (a codebook executed by code, zero per-record judgment), and two
script-based passes would make the "gold standard" two regex families agreeing with each other —
worthless to a referee.** The ruling requires Pass B to be a genuine per-record **reading** pass:
a personal codebook/checklist as an aid is fine, but no blanket script may produce
`gold_blocks_B`.

**Final method (what actually produced this CSV).** I discarded the script's output and read all
200 full `<L>…<LEND>` records individually, pulled directly from
[csl-orig/v02/mw/mw.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt)
(not the clipped `record_excerpt` column, which truncates long entries). For each record I applied
judgment against MICROANALYSIS.md §1's published marker definitions, but did **not** apply them
mechanically — in particular, for every record with 2+ `<s>` tags I read whether the second tag was
a genuine inflected/conjugated form of the headword (→ `F08`) or something else entirely: a
cross-referenced *different* headword (`= X`, `cf. X`, `id.` targets), a bare etymological-root
citation (`√ X`, `fr. X` — captured by `F06`, not `F08`), a compound-member segmentation (`X + Y`
— the exact over-count pattern MICROANALYSIS.md's own §9 limitations documents), or a phw-child
illustration (`-tva <lex type="phw">…`). This single distinction is why `F08` moved from **37.5%**
(mechanical) to **22.5%** (read) across the sample — the single largest correction from doing this
properly.

**Result: 87/200 rows (43.5%) carry a `notes` entry** documenting a specific judgment call —
proof this is a reading pass, not a rule applied uniformly. Recurring judgment categories:

1. **`F08` over-count correction (largest category).** Distinguished genuine inflected/conjugated
   forms from cross-ref targets, etymological-source citations, compound-member segmentation, and
   phw-child illustrations — all of which carry a second `<s>` tag but are NOT inflections of the
   current headword.
2. **`F09` (editorial commentary) — both directions.** Corrected the earlier script's
   over-triggering on bare `= synonym`/`cf.` patterns (not commentary), but ALSO **found genuine
   commentary the script missed**: hedge phrases like "(said to consist of/in …)" reporting
   uncertain attributed description, "(for X?)" flagging an uncertain derivation with a literal
   `?`, and "(accord. to L. …)" where the trigger word sat inside an `<ab>` tag my regex couldn't
   see through. Final count: 7/200 (3.5%), up from the corrected script's 1/200 — reading caught
   real cases a keyword regex cannot.
3. **`F16` vs. `<info phwparent="…">`/`<info phwchild="…">` (the `crossref_phw` stratum's core
   question).** Consistently treated `F16` as requiring a *textual* cross-reference marker
   (`q.v.`, `<ab>cf.</ab>`, `<ab>id.</ab>`, `See`/`see`) and did **not** count a bare phw-parent/
   phw-child machine relation as `F16` — that relationship is `F17` (infrastructure), not
   discourse. Several `crossref_phw` records had NEITHER a textual marker NOR a phw relation that
   qualifies as `F16` by this reading; others (`id.`, `See X`) genuinely do. Flagging this
   distinction for adjudication throughout, since it is exactly what the stratum is designed to
   probe.
4. **One record (`G5-063`, root `vfz`) turned out far richer than either the excerpt or a
   mechanical scan suggested**: a nested `<hom>1.</hom>` inside a bracketed etymological note
   (missed by a leading-tag-only `F03` check), genuine `<lang>Gaëlic</lang>+<etym>pas</etym>`
   IE-cognate content (`F07`), and a `[For cognates See under …]` bracketed note that is
   simultaneously editorial commentary (`F09`) AND a textual cross-reference (`F16`). This record
   alone shows the value of reading the full text over trusting either the excerpt or a script.
5. **`F18` — two records use an inline `<chg><old>/<new>` tag**, not the `{{old->new||date|
   author|url}}` format MICROANALYSIS.md's table describes (`G5-111`/L=180503,
   `G5-198`/L=1730). Both are genuine machine-readable correction records by function; counted as
   `F18`, flagged for adjudication given the format mismatch with the published table.
6. **A borderline `F02` placement** (`G5-171`/L=43057): the rendered display form appears in
   parentheses immediately *after* `¦` rather than before it. Counted as `F02` by judgment — an
   annotator reading for "is there a display form" would say yes regardless of the unusual
   position.

## Records completed

**200/200.** No fields left blank. `F01`, `F10`, `F17` present in all 200 (matching the paper's
own claim that these are structurally universal).

## Judgment calls flagged for adjudication (see per-row `notes` for the full list)

- `F16` vs. phw-parent/phw-child machine relations (recurring across the `crossref_phw` stratum)
- `F18`'s alternate `<chg>` tag format vs. the documented `{{old->new}}` format
- A borderline `F07` case (`G5-105`/L=122887): a bare `<gk>` tag with Greek content but no
  accompanying `<lang>` tag — counted by semantic content, flagged for marker-table mismatch
- A borderline `F09` boundary (`G5-079`/L=96968): "(for `dogDf`?)" signals uncertainty but has no
  literal `√`/`fr.` marker, so not counted as `F06` despite being an etymological guess

## Wall-clock

Single continuous session. Includes: initial script attempt + spot-checks (discarded), discovery
of the Fable S2 amendment, and a full 200-record reading pass in five batches with per-record
judgment recorded live.

## Population-frequency comparison (this 200-record stratified sample, NOT representative of the
full 286,561-record corpus)

| Block | Mechanical (discarded) | Read (final) |
|---|--:|--:|
| F01 | 100.0% | 100.0% |
| F02 | 78.5% | 79.0% |
| F03 | 4.5% | 4.5% |
| F04 | 62.5% | 64.5% |
| F05 | 10.0% | 10.0% |
| F06 | 14.0% | 14.5% |
| F07 | 2.0% | 1.0% |
| **F08** | **37.5%** | **22.5%** |
| F09 | 0.5%* | 3.5% |
| F10 | 100.0% | 100.0% |
| F11 | 0.0% | 0.0% |
| F12 | 86.0% | 86.5% |
| F13 | 25.0% | 25.0% |
| F14 | 3.5% | 3.5% |
| F15 | 17.0% | 17.5% |
| F16 | 13.5% | 13.0% |
| F17 | 100.0% | 100.0% |
| F18 | 1.0% | 1.0% |

\* after an earlier regex fix mid-development; the very first pass over-fired at 2.5%.

`F08` is the one block where mechanical detection and genuine reading diverge sharply (37.5% →
22.5%) — exactly the kind of result the Fable ruling predicted a script would get wrong, and
exactly the reason two independent *readings* (not two regex families) are needed for a
meaningful precision/recall measurement against the paper's own detector.

_Dr. Mārcis Gasūns_
