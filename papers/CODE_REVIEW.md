# Code review — 2026-06-13 extra-high-effort pass over the MW analysis scripts

> **✅ All 15 fixed 2026-06-13** (numbers re-verified by an adversarial pass). Corrected
> figures: Register-B kośa share **46.7% → 40.5%**, SKD grounding **50.3% → 51.3%**;
> root crosswalk **label fixed** (the 813 anchors are all verbal roots — in-MW stays
> **809 / 86.5%**, triangulated **550**); class conflicts **32 → 26** (homonym-dedup +
> `verb="root"` inclusion). The numbers inside each finding are the pre-fix values it describes.

An extra-high-effort line-by-line review of this session's MW analysis scripts —
the ones whose output feeds P3 memos and crosswalk papers. Findings are numbered
stably #1..#15 in array order. **All 15 were FIXED 2026-06-13** (this began as a
document-only pass; the fixes followed). Severity follows RED_TEAM.md: 🔴 changes a
**published number** · 🟠 latent drift / self-contradiction on re-run · 🟡 miscount /
misclassification in a supporting figure · 🟢 cleanup / future-break / divergence.

## Verdict at a glance

| # | file | finding | tier |
|---|---|---|---|
| 1 | [register_b_dcs.py:35](p3_citation_registers/register_b/register_b_dcs.py#L35) | `ITI_RE` char class eats a literal hyphen → `rAja-` fails KOSA test | 🔴 |
| 2 | [register_b_dcs.py:35](p3_citation_registers/register_b/register_b_dcs.py#L35) | `ITI_RE` needs a leading space → body-line-start `iti` dropped | 🔴 |
| 3 | [register_b_dcs.py:58](p3_citation_registers/register_b/register_b_dcs.py#L58) | `attested()` strips final SLP1 `M` unconditionally → `kiM` false-matches | 🔴 |
| 4 | [root_crosswalk.py:67](../root_crosswalk/root_crosswalk.py#L67) | anchors built from ALL whitneyroots, not `verb=genuineroot` → 813 > 750 | 🟡 |
| 5 | [class_concordance.py:94](../root_crosswalk/class_concordance.py#L94) | `N = len(records)` double-counts ~50 homonym roots | 🟡 |
| 6 | [ls_L_dcs2026.py:118](../lexicographer_dcs/ls_L_dcs2026.py#L118) | 2026 side of stability line hardcodes `31.4%` while 2021 is computed | 🟠 |
| 7 | [register_b_dcs.py:159](p3_citation_registers/register_b/register_b_dcs.py#L159) | prose numbers hardcoded literals next to live-computed table cells | 🟠 |
| 8 | [ib_resolve.py:14](../relative_refs/ib_resolve.py#L14) | docstring describes OLD k1-cluster algorithm; code resolves globally | 🟡 |
| 9 | [phw_audit.py:95](../phw_graph/phw_audit.py#L95) | one broken pair counted as two issues (asymmetric + orphan_backlink) | 🟡 |
| 10 | [phw_audit.py:81](../phw_graph/phw_audit.py#L81) | missing-backlink bucketed as `asymmetric`, same as wrong-parent MISMATCH | 🟡 |
| 11 | [build_packets.py:143](../review_packets/build_packets.py#L143) | Packet C `setdefault` keeps FIRST homonym; conflict sits on a later one | 🟡 |
| 12 | [ib_resolve.py:39](../relative_refs/ib_resolve.py#L39) | `re.split(..., 1)` positional maxsplit → DeprecationWarning on 3.14 | 🟢 |
| 13 | [register_b_dcs.py:91](p3_citation_registers/register_b/register_b_dcs.py#L91) | `n_records` re-reads source file to count `<L>`; leaks bare `open()` handle | 🟢 |
| 14 | [ls_L_dcs2026.py:44](../lexicographer_dcs/ls_L_dcs2026.py#L44) | IAST→SLP1 `_MAP` diverged from `link_candidates.py` copy | 🟢 |
| 15 | [ib_resolve.py:36](../relative_refs/ib_resolve.py#L36) | META `non-text citation` set defined inconsistently across siblings | 🟢 |

## 🔴 Changes a published number

**1. `ITI_RE` hyphen capture.** [register_b_dcs.py:35](p3_citation_registers/register_b/register_b_dcs.py#L35) —
the `ITI_RE` char class includes a literal hyphen, so a line-broken/compound kośa
ref like `iti rAja-` is captured as `rAja-` and fails the KOSA membership test.
*Failure:* this deflates `iti_kosa` and the headline **46.7%** "constitutively
lexicographic" figure — a published number drops because legitimate hits are
silently rejected on a trailing `-`. *Fix sketch:* drop `-` from the capture class
(or `rstrip('-')` the captured token) before the KOSA lookup. **Status: FIXED (2026-06-13).**

**2. `ITI_RE` leading-space requirement.** [register_b_dcs.py:35](p3_citation_registers/register_b/register_b_dcs.py#L35) —
`ITI_RE` requires a literal leading space, so an `iti` that begins a record
body-line (preceded by a newline, not a space) is dropped from `iti_total`,
`iti_kosa`, and the lex-flag entirely. *Failure:* the **46.7%** numerator and
denominator are computed over a partial subsample of citations — every record-
or line-initial `iti` is invisible to the count. *Fix sketch:* anchor on
`(?:^|\s)` / a word boundary instead of a mandatory space, matching at
line start under `re.M`. **Status: FIXED (2026-06-13).**

**3. `attested()` over-strips final anusvāra.** [register_b_dcs.py:58](p3_citation_registers/register_b/register_b_dcs.py#L58) —
`attested()` strips a final SLP1 `M` (anusvāra) unconditionally as de-inflection,
but final `M` is part of indeclinables (`kiM`=*kim*, `svayaM`) whose lemma is the
full form. *Failure:* `kiM` is matched via its `ki` stem → falsely DCS-attested →
inflates the SKD **~50.3%** corpus-grounding figure with spurious hits. *Fix
sketch:* gate the final-`M` strip on a stop-list of indeclinables (or require the
de-inflected stem to actually be DCS-attested as a nominal, not any token).
**Status: FIXED (2026-06-13).**

## 🟠 Latent drift / self-contradiction on re-run

**6. Hardcoded 2026 stability figure.** [ls_L_dcs2026.py:118](../lexicographer_dcs/ls_L_dcs2026.py#L118) —
the 2026 side of the stability line hardcodes the literal `31.4% (DCS-2026)`
while the 2021 side is computed live. *Failure:* on a DCS refresh the computed
headline moves but the hardcoded stability line does not, so the script
contradicts itself within the same output. *Fix sketch:* compute the 2026 rate
from the loaded data and interpolate it into the string, exactly as the 2021 side
already does. **Status: FIXED (2026-06-13).**

**7. Hardcoded prose numbers beside a live table.** [register_b_dcs.py:159](p3_citation_registers/register_b/register_b_dcs.py#L159) —
the prose numbers `28.2%` / `194k` / `50.3%` / `46.7%` and the context-table row
are hardcoded literals while the adjacent table cells are computed live. *Failure:*
a re-run updates the live cells but leaves the prose stale, so the memo
contradicts its own table. *Fix sketch:* format the prose from the same computed
variables that fill the table cells; keep a single source of truth per number.
**Status: FIXED (2026-06-13).**

## 🟡 Miscount / misclassification in a supporting figure

**4. Anchors not filtered to genuine roots.** [root_crosswalk.py:67](../root_crosswalk/root_crosswalk.py#L67) —
`mw_anchor_bare` / `has_wr` are built from ALL whitneyroots records, not only
`verb=genuineroot`, so 203 non-verbal anchors leak into the verbal-root
crosswalk. *Failure:* 813 anchored > 750 genuine roots, yet the summary presents
813 as a sub-count of genuine roots and inflates the **809 / 86.5%** in-MW
coverage. *Fix sketch:* filter to `verb == 'genuineroot'` before building the
anchor sets. **Status: FIXED (2026-06-13)** — *correction: an adversarial pass showed the 203 surplus anchors are `verb="root"` records, which ARE verbal roots; the fix INCLUDES `verb="root"` (not filter to `genuineroot`), so in-MW stays 809 and only the 750→2,113 verbal-root label changed.*

**5. Concordance N counts records, not roots.** [class_concordance.py:94](../root_crosswalk/class_concordance.py#L94) —
`N = len(records)` counts MW records rather than distinct roots, so the ~50
homonym roots that carry two records each are scored twice. *Failure:* this
double-counts agree/overlap/conflict and the "comparable" denominator behind the
**94.4%** concordance rate. *Fix sketch:* deduplicate to distinct bare roots (or
count per resolved homonym) before computing N. **Status: FIXED (2026-06-13).**

**8. Stale docstring vs global resolver.** [ib_resolve.py:14](../relative_refs/ib_resolve.py#L14) —
the module docstring still describes the OLD k1-cluster-scoped algorithm, but the
code now resolves over the global document stream and crosses headwords. *Failure:*
a maintainer is misled about scope; "unresolvable" is ~always 0, which
contradicts the docstring's premise. *Fix sketch:* rewrite the docstring to
describe the global document-order walk, and note the cross-headword behaviour
explicitly. **Status: FIXED (2026-06-13).**

**9. One broken pair double-counted.** [phw_audit.py:95](../phw_graph/phw_audit.py#L95) —
a single broken phw pair is recorded as two issues: `asymmetric` from the parent
pass and `orphan_backlink` from the child pass. *Failure:* the **31 integrity
issues** headline overstates the distinct-defect count. *Fix sketch:* deduplicate
issues by the unordered pair key before tallying. **Status: FIXED (2026-06-13).**

**10. Missing-backlink mislabelled as asymmetric.** [phw_audit.py:81](../phw_graph/phw_audit.py#L81) —
a child with NO `phwparent` (`no_backlink`) is bucketed as `asymmetric`, the same
bucket as a child naming the WRONG parent (a genuine MISMATCH). *Failure:*
`phw_integrity.csv` mislabels a missing-backlink as a wrong-link, pointing the
maintainer at the wrong fix. *Fix sketch:* split the bucket into `no_backlink`
vs `mismatch` so the CSV distinguishes "absent" from "wrong." **Status: FIXED (2026-06-13).**

**11. Packet C shows the wrong homonym.** [build_packets.py:143](../review_packets/build_packets.py#L143) —
Packet C indexes genuine-root records by `s2i(bare root)` and `setdefault` keeps
the FIRST homonym, but conflicts often sit on a later homonym. *Failure:* the
packet shows the wrong homonym's gloss/Dhātupāṭha next to the conflict's class
numbers (e.g. the `as` row), misleading the verdict. *Fix sketch:* key by the
resolved homonym id (e.g. `as1`/`as2`) rather than the bare root, or carry all
homonyms and select the one the conflict references. **Status: FIXED (2026-06-13).**

## 🟢 Cleanup / future-break / divergence

**12. Positional `maxsplit` deprecation.** [ib_resolve.py:39](../relative_refs/ib_resolve.py#L39) —
`re.split(r'[ ,]', s.strip(), 1)` passes `maxsplit` positionally, which raises a
DeprecationWarning on Python 3.14 (observed) and is slated to become an error;
the sibling script already uses the keyword form. *Failure:* on a future Python
it raises `TypeError` and `ib_resolve` stops producing output. *Fix sketch:* pass
`maxsplit=1` as a keyword. **Status: FIXED (2026-06-13).**

**13. Redundant re-read + leaked handle.** [register_b_dcs.py:91](p3_citation_registers/register_b/register_b_dcs.py#L91) —
`n_records` re-opens and fully re-reads `skd.txt` / `vcp.txt` just to count `<L>`
lines the main loop already visited, and the bare `open()` inside a generator
expression leaks the file handle. *Failure:* doubled I/O on multi-MB files plus a
leaked file handle. *Fix sketch:* count `<L>` during the existing single pass, or
use a `with` block; drop the second read entirely. **Status: FIXED (2026-06-13).**

**14. Diverged IAST→SLP1 map.** [ls_L_dcs2026.py:44](../lexicographer_dcs/ls_L_dcs2026.py#L44) —
the IAST→SLP1 `_MAP` is copy-pasted into `link_candidates.py` with a diverged row
set (`ls_L_dcs2026` carries the H-mappings that `link_candidates` lacks).
*Failure:* the two scripts transcode a lemma containing those chars to different
SLP1 and therefore disagree on the same data. *Fix sketch:* extract `_MAP` into a
single shared module imported by both. **Status: FIXED (2026-06-13).**

**15. Inconsistent META citation set.** [ib_resolve.py:36](../relative_refs/ib_resolve.py#L36) —
the META "non-text citation" set is hardcoded inconsistently: `ib_resolve` omits
`ib.` / `id.` while `link_candidates` includes them. *Failure:* "meta vs real
source" is defined differently by sibling scripts analysing the same apparatus.
*Fix sketch:* define the META set once in a shared constants module and import it
in both. **Status: FIXED (2026-06-13).**

## Meta note

The single highest-value fix is the `register_b` `iti` regex (#1 / #2): both
sit on line 35 of the same file and both directly move the published **46.7%**
headline, so one regex correction retires two 🔴 findings at once. Note that
**none of the 15 findings is a crash** — every one is a quiet wrong-number bug
(deflated/inflated rate, double-count, stale literal, mislabelled bucket). That is
exactly the failure mode that matters most when the output feeds papers: the
script runs clean, prints a plausible figure, and the error only surfaces under a
referee's scrutiny — or never.
