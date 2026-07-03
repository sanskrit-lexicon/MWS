# A17 (Микроструктура, RU / PAPER_RU) — Hostile Pre-Submission Review

_Created: 03-07-2026 · Last updated: 03-07-2026_

**Paper:** [papers/microanalysis/PAPER_RU.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/PAPER_RU.md) (A17, Russian companion to A16; target Восток · Oriens)
**Reviewer:** Fable 5 (`claude-fable-5`), adversarial referee pass in the A10/A34/A36 mold; three parallel agents (also Fable 5, `claude-fable-5`): block/typology figures, cross-dictionary + hedge-history figures, A16↔A17 conclusion-overlap + link audit. External web checks: Scharf & Hyman, Kochergina.
**Verdict: MAJOR REVISION → all agent-doable findings fixed same pass.** The hedge-history core (three-stage 1872/1891/1899 lineage, kośa-grid collapse, all PWG/MW `<ls>` tag counts) verifies exactly. But the paper had gone stale against its own project (a resolved DOUBT presented as open, pre-audit block figures), carried three wrong numbers a referee recomputes in minutes (PWG distinct sources, the 85 % projection, MW entry length), misattributed measured counts to Benfey, and made a dual-submission claim ("не дублируют выводы") that reading both papers refutes.

---

## 1. Figure re-verification

**Confirmed exact:** 286,561 records / 2026-05-23 / 48.9 MB; typology counts for types 1–8; Vedic 47,598 (16.6 %); IE 2,099 (0.73 %, 35 % of roots); hedge-distribution table (71.5 / 64.7 / 21.1 / 4.4 / 7.2 / 13.1 / 16.2 / 0.4); density 140.33/1k; PWG 570,817 `<ls>` / zero generic L.; kośa tag counts (ŚKDR 20,109 … ŚABDAC 1,427); MW `<ls>` table (L. 40,212; MBh. 22,990; ib. 10,094; RV. 9,707; R. 9,049; BhP. 6,979; ŚBr. 5,493); Cappeller `*` 1,370 / `†` 903 (as Cappeller's); Wilson 230/224 Rox.; MW-1872 preface declaration + 17 mostly-Linnaean "L."; SKD 532 / VCP 494 chars; iti 1.70 / 0.26; 64.0 % current source coverage; the 6-of-18 modal core.

**Failed verification (all fixed):** M1–M7 below.

## 2. Major findings

**M1 — §5's typology was stale: DOUBTS D18 is resolved, the paper presented it as open.** [DOUBTS.md D18](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/DOUBTS.md) closed 2026-05-27 as *verbal-lemma promotion*: the EN paper has 9 primary types (verbal lemma 7,502 / 2.77 %) and a residual of ≈11,000 (≈4.0 %); the RU still had 8 types, a 19,460 (6.79 %) residual "needing analysis", and a dead D18 anchor. *Fix (applied):* 9-type typology, resolved-D18 framing, live anchor.

**M2 — §6.3 gave PWG "821 различное значение" — that is MW's number.** Per [decisions/NORMALISATION.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/decisions/NORMALISATION.md): MW 821 distinct normalised `<ls>` values, **PWG 2,420** (238,271 raw). The error understated PWG's named-source grid ~3× in the very sentence contrasting PWG's granularity with MW's collapse. *Fix (applied):* 2,420, with the "almost 3× MW" contrast now working *for* the argument.

**M3 — §8's "64 % → ~85 %" projection fails arithmetic.** (199,743 + 40,212)/311,932 = **76.9 %**; no document supports 85 %. *Fix (applied):* "с 64,0 % до ≈ 77 % (+12,9 п. п.)" — and marked as the RU-only number it is.

**M4 — §7's "≈ 80" mean MW entry length is roughly half the real value.** Recomputed with the same method as the SKD/VCP figures (`cross_dict_profiles.py` record regex over `mw.txt`): **≈ 171 chars**. *Fix (applied):* 171, with the honest note that the contrast survives (MW carries English glosses; kośa entries are Sanskrit-only).

**M5 — §6.6's comparison table assigned Cappeller's measured counts (903 `†` + 1,370 `*`) to Benfey.** No Benfey marker counts exist anywhere in the analysis docs (BEN's digital apparatus is 14,708 `<ls>` tags); the paper's own §6.5 attributes the counts to Cappeller correctly, so §6.6 also contradicted §6.5. *Fix (applied):* counts moved to the Cappeller column; Benfey cell says "not quantified in the digital edition". **Ground-truth note:** the same ~900 leak sits in [LS_HEDGE_CHECK.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/analysis/LS_HEDGE_CHECK.md)'s D21 lineage table (line ~228) — flagged for the analysis-doc sweep.

**M6 — The dual-version claim "не дублируют друг друга по выводам" is not defensible.** All four headline findings (block economy, structural hedge, three-stage lineage, kośa genre boundary) are conclusions in BOTH papers, with near-identical tables. An editor reading both would call that substantive overlap. *Fix (applied):* header + closing footer reframed to "shared empirical base and four shared core findings, disjoint analytical contributions" (EN: triangulation, infrastructure construct, Provenienz-Komment; RU: kośa→PWG→MW→CDSL line, Russian-lexicography programme); each §8 вывод now carries a "(общий; = PAPER.md §X)" or "(только в русской версии)" marker; disclosure-to-both-editors stated.

**M7 — Audit-superseded block-table figures.** The [SPOTCHECK.md](https://github.com/sanskrit-lexicon/MWS/blob/master/papers/microanalysis/analysis/SPOTCHECK.md) audit supersedes the early estimates the table used: F03 5 %→3.3 %, F05 <1 %→2.5 %, F16 9 %→6.5 %, F08 21 %→23.2 % (with the ~⅓ compound false-positive caveat), F06 6 %→7.1 %, F04 65 %→67.5 %, F13 →13.9 %; and "lex-hedged = 40 212 записей (14 %)" conflated tags with entries — the audited entry count is **39,962 (13.9 %)** (the value the A16 docs-pass G5 work also settled on; MICROANALYSIS's older 38,414 is superseded), tags 40,212. *Fix (applied):* audited values + a table provenance note + the entries/tags distinction.

## 3. Minor findings

**m1 — Fabricated-looking citation replaced.** "Scharf & Hyman (2009–2011). *Encoding Sanskrit dictionaries: report from the Cologne project*. In *Sanskrit Computational Linguistics*" does not verify as a publication; the verified work is Scharf & Hyman (2011), *Linguistic Issues in Encoding Sanskrit* ([Semantic Scholar](https://www.semanticscholar.org/paper/Linguistic-Issues-in-Encoding-Sanskrit-Scharf-Hyman/a442a7d20b018ab45fa5b4c84a9cde9c23844d5c)). *Fix (applied)* + in-text year synced.

**m2 — Kochergina title wrong.** «Сводный санскритский словарь» → **«Санскритско-русский словарь»**, 3-е изд., М.: Филология, 1996 (~30,000 слов; Зализняк grammar sketch) — verified ([ru.wikipedia](https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BD%D1%81%D0%BA%D1%80%D0%B8%D1%82%D1%81%D0%BA%D0%BE-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C), [URSS](http://urss.ru/cgi-bin/db.pl?blang=ru&id=206211&lang=Ru&page=Book)). *Fix (applied)* + reference entry added.

**m3 — Hausmann 1985 venue wrong** ("In HSK" → Schwarze & Wunderlich (eds.), *Handbuch der Lexikologie*, 367–411). *Fix (applied).*

**m4 — All four kosha "repo" links were 404** (ARMH/ABCH/ACPH/ACSJ are `csl-orig/v02/` subdirectories, not repos) — 8 link instances. *Fix (applied):* `csl-orig/tree/master/v02/…` targets.

**m5 — Broken anchors:** `#sources` ×2 (the section is «Источники» → `#источники`), plus the dead D18 anchor (covered in M1). *Fix (applied).*

**m6 — §6.2's "821 named sources" overcounted "named":** the 821 uniques include `L.` itself and editorial markers (`ib.` 10,094, `W.` 8,285, `Cat.` 5,302). *Fix (applied):* rephrased with the caveat.

**m7 — §4's density figures cited to a file that doesn't contain them** (CROSS_DICT.md → the actual source decisions/NORMALISATION.md). *Fix (applied).*

**m8 — ŚABDAC. expanded as "*Śabdacandra*"** — the kośa conventionally so abbreviated is the **Śabdacandrikā**. *Fix (applied);* verify against PWG's Verzeichniss before print (author check).

**m9 — Typo «kośa-лиинии»; byline email** gasyoun@gmail.com → gasyoun@ya.ru (standing byline); model attribution line updated (bare "Opus 4.X / Sonnet 4.X" kept as the historical sessions, this pass named as Fable 5 `claude-fable-5`). *Fix (applied).*

## 4. Queued sibling defects — A16 (PAPER.md, currently marked 5/5) and ground truth

**These were NOT fixed in this pass** (A16 is a separate manuscript pass; ground-truth docs need their own sweep), but several A17 defects are shared and A16 is "ready to send":

1. PAPER.md §4 block table: same stale F03 5 %, F05 <1 %, F16 9 %, F08 21 % (its own §9.1 quotes 23.2 %).
2. PAPER.md "40,212 distinct entries" — tags-vs-entries (38,414).
3. PAPER.md D18/D19 anchors dropped the "…now-closed" heading tails — dead fragments.
4. PAPER.md §8 + Appendices B.6/C.4: same four 404 kosha repo links.
5. PAPER.md References: same unverifiable Scharf & Hyman citation.
6. Ground truth: LS_HEDGE_CHECK D21 table's Benfey "~900 instances" leak; MICROANALYSIS.md 40,213-vs-40,212 off-by-one; MICROANALYSIS §3.2 same tags-as-entries wording; LS_HEDGE_CHECK says D21 "RESOLVED" where DOUBTS says "PARTIALLY RESOLVED".

## 5. Checked and sound (no action)

- The three-stage lineage (MW 1872 declared → Cappeller 1891 systematic-typographic → MW 1899 systematic-tagged) verifies in full, quotes included — it remains the paper's best contribution and is now correctly bounded.
- The kośa genre-boundary argument (§7) and the hedge-distribution empirics (§6.2) are exact.
- Venue (Восток · Oriens) fits the Russian-indology framing; no HOLD.

## 6. Remaining gates

- **Author/MG:** byline finalisation (shared with A16); the ŚABDAC/Verzeichniss spot-check; the dual-submission disclosure sentence in both cover letters when they exist.
- **Agent (queued):** the A16 shared-defect fix pass (item 4 above) — **A16 should not be sent before it**; the analysis-doc ground-truth sweep.

_Dr. Mārcis Gasūns_
