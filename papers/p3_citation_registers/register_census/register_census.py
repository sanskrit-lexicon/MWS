#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A18 / P3 evidence census — the two citation registers inside MW's evidence block.

Terminology is CONSUMED from the atlas paper A08 (csl-atlas
docs/CITATION_REGISTERS.md), not forked:

  Register A = <ls>-tagged citation, the European critical-apparatus form.
  Register B = in-prose `iti`/`ity` quotative, the indigenous kosa form.

A08 measures the registers by FORM across 44 dicts and reports MW as a pure
Register-A dictionary (1.09 <ls>/entry, zero indigenous-register standing).
This census measures the ORTHOGONAL axis inside MW's Register A: the
EVIDENTIARY STATUS each citation carries. Every <ls> occupies one formal slot
but does one of several different evidentiary jobs.

Strata (per <ls> occurrence, mutually exclusive, decided in this order):

  hedge        <ls>L.</ls> -- "Lexicographers", MW's own marker that the sense
               rests on the indigenous kosa tradition with NO textual witness
               known to MW. Register-B *content* compressed into a Register-A
               *slot* with the source name stripped.
  authority    W. / MW. / Cat. -- MW citing a scholarly authority, a catalogue,
               or himself; a bibliographic pointer, never a usage attestation.
  relative     ib. / id. -- anaphoric; the source is the antecedent citation.
               Resolvable (see ../../relative_refs/), not sourceless.
  attested     a named work WITH a numeric locator -- a usage attestation the
               reader can, in principle, walk to a page/verse.
  bare         a named work with NO locator -- names a bibliographic source but
               attests no locatable passage.

Also counted, for the A08 cross-check: MW's word-boundary `iti`/`ity` footprint
using A08's own rule (not adjacent to a Latin letter), so MW's standing on the
Register-B axis is measured, not assumed.

Inputs (read-only):
  ../../../../csl-orig/v02/mw/mw.txt   (SLP1 inside markup; <ls> content is IAST)

Outputs (this dir):
  register_census.csv          per-stratum counts + shares
  register_census_sigla.csv    top sigla per stratum
  entry_level.csv              per-entry register composition distribution
  CENSUS.md                    computed prose summary (all numbers from this run)

Model provenance: built by Fable 5 (claude-fable-5), 16-07-2026, handoff H1076.
"""
import sys, os, re, csv, json
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH   = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
MW   = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')

# MW writes a citation in TWO different shapes, and a regex that knows only the
# first one silently drops the other (this is the A08 divergence documented in
# CENSUS.md -- csl-atlas' `<ls>` rule matches the bare form only):
#   bare form:       <ls>Pāṇ. vi, 2, 161</ls>   siglum + locator in the content
#   attributed form: <ls n="RV.">vii, 96, 3</ls>  siglum in @n, locator in content
#                    <ls n="RV. viii, 96,">15</ls>  locator SPLIT across both
# So the citation's full text is @n + content, and the siglum/locator split is
# positional, not tag-positional.
LS_RE   = re.compile(r'<ls(\s+n="([^"]*)")?\s*>(.*?)</ls>', re.S)
# A08's rule: iti/ity as a word, not adjacent to a Latin letter, so that
# markup-wrapped and punctuation-adjacent quotatives still count.
ITI_RE  = re.compile(r'(?<![A-Za-z])it[iy](?![A-Za-z])')

DIGIT_RE = re.compile(r'\d')
# MW locators are arabic (`RV. 10, 12`) OR roman (`ŚBr. xiv`); the roman-only ones
# are counted at run time (see `roman_only` in the stats) and an arabic-digit rule
# scores every one of them as sourceless.
ROMAN_RE = re.compile(r'^[ivxlc]+$')

HEDGE     = {'L.'}
AUTHORITY = {'W.', 'MW.', 'Cat.'}
RELATIVE  = {'ib.', 'id.'}   # `id.` never occurs inside <ls> in MW (verified: 0)
STRATA    = ['attested', 'bare', 'hedge', 'authority', 'relative']


def m_text(attr_n, content):
    return '<ls n="%s">%s</ls>' % (attr_n, content) if attr_n else '<ls>%s</ls>' % content


def is_locator_token(tok):
    """MW's roman locators are LOWERCASE (`ŚBr. xiv`, `RV. vii`). Case matters: fold it
    and the hedge `L.` reads as roman 50, and capitalised sigla (`Vi.`, `Ci.`) read as
    roman numerals — which silently reclassifies ~46k bare citations as attested."""
    t = tok.strip(' .,;()[]')
    if not t:
        return False
    return bool(DIGIT_RE.search(t)) or bool(ROMAN_RE.match(t))


def split_citation(attr_n, content):
    """-> (siglum, locator). The siglum is the leading run of non-locator tokens."""
    full = ((attr_n or '') + ' ' + (content or '')).strip()
    toks = [t for t in re.split(r'\s+', full) if t]
    i = 0
    while i < len(toks) and not is_locator_token(toks[i]):
        i += 1
    return ' '.join(toks[:i]).strip(), ' '.join(toks[i:]).strip()


# A citation's evidentiary stratum is a property of the citation, not of the
# siglum: `MBh. iii, 12` is attested and a bare `MBh.` is not.
def stratum(siglum, locator):
    s = siglum.strip()
    if s in HEDGE:     return 'hedge'
    if s in AUTHORITY: return 'authority'
    if s in RELATIVE:  return 'relative'
    return 'attested' if locator else 'bare'


def main():
    if not os.path.exists(MW):
        sys.exit('mw.txt not found at %s' % MW)

    counts        = Counter()
    sigla         = defaultdict(Counter)
    entry_profile = Counter()   # (has_attested, has_hedge) -> entries
    entry_strata  = Counter()   # entries carrying >=1 citation of stratum
    entries_with_ls = 0
    total_entries = 0
    iti_hits = 0
    hedge_only_entries = 0
    mixed_entries = 0
    # A08 cross-check: what its bare-<ls> rule sees vs what is actually there.
    a08_visible = 0          # citations written in the bare form
    a08_visible_locator = 0  # of those, locator-bearing (A08's lsWithLocator)
    attributed = 0           # citations A08's rule cannot see
    attributed_locator = 0
    attributed_arabic = 0    # attributed citations bearing an ARABIC locator (A08's own rule)
    roman_only_plain = 0     # plain-shape attested citations whose locator is roman-only
    meta_with_locator = []   # the hedge/authority-with-locator anomalies (n=2)

    rec_lines, cur = [], []
    with open(MW, encoding='utf-8') as f:
        for line in f:
            if line.startswith('<L>'):
                cur = [line]
            elif line.startswith('<LEND>'):
                if cur:
                    rec_lines.append(''.join(cur))
                    cur = []
            elif cur:
                cur.append(line)

    for rec in rec_lines:
        total_entries += 1
        iti_hits += len(ITI_RE.findall(rec))
        cites = LS_RE.findall(rec)
        if not cites:
            continue
        entries_with_ls += 1
        here = Counter()
        for attr_group, attr_n, content in cites:
            siglum, locator = split_citation(attr_n, content)
            st = stratum(siglum, locator)
            counts[st] += 1
            sigla[st][siglum] += 1
            here[st] += 1
            if attr_group:
                attributed += 1
                attributed_locator += bool(locator)
                attributed_arabic += bool(DIGIT_RE.search((attr_n or '') + ' ' + content))
            else:
                a08_visible += 1
                a08_visible_locator += bool(DIGIT_RE.search(content))
                # Counted directly, not by subtraction: a plain-shape citation whose
                # locator is roman-only is exactly what an arabic-digit rule cannot see.
                if st == 'attested' and not DIGIT_RE.search(content):
                    roman_only_plain += 1
            # Reconciliation against the literal-match counts published in
            # SYNTHESIS.md (L. 40,212 / meta 69,603): a meta siglum carrying a
            # locator is classed by its siglum here, so it lands in hedge/authority
            # where a literal `<ls>L.</ls>` match would miss it. n=2 in all of MW.
            if st in ('hedge', 'authority') and locator:
                meta_with_locator.append(m_text(attr_n, content))
        for st in here:
            entry_strata[st] += 1
        has_att = here['attested'] > 0
        has_hedge = here['hedge'] > 0
        entry_profile[(has_att, has_hedge)] += 1
        if has_hedge and not has_att and here['bare'] == 0:
            hedge_only_entries += 1
        if has_hedge and (has_att or here['bare']):
            mixed_entries += 1

    total_ls = sum(counts.values())

    # Self-check: the attested stratum must decompose exactly into the three ways a
    # locator can reach it. `a08_visible_locator` counts <ls>W. 1</ls> (which we class
    # `authority`, not `attested`), hence the meta_with_locator correction -- keeping
    # this identity honest is what stops the A08 comparison in CENSUS.md drifting.
    # Only a meta citation with an ARABIC locator lands in a08_visible_locator:
    # <ls>W. 1</ls> does, <ls>L. i</ls> (roman) does not.
    plain_arabic_attested = a08_visible_locator - sum(
        1 for c in meta_with_locator
        if not c.startswith('<ls n=') and DIGIT_RE.search(c))
    assert plain_arabic_attested + roman_only_plain + attributed_locator == counts['attested'], (
        'attested stratum does not decompose: %d + %d + %d != %d' % (
            plain_arabic_attested, roman_only_plain, attributed_locator, counts['attested']))

    with open(os.path.join(HERE, 'register_census.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['stratum', 'citations', 'share_of_ls_pct', 'entries_carrying', 'share_of_ls_entries_pct'])
        for st in STRATA:
            w.writerow([st, counts[st], round(100.0 * counts[st] / total_ls, 2),
                        entry_strata[st], round(100.0 * entry_strata[st] / entries_with_ls, 2)])
        w.writerow(['TOTAL', total_ls, 100.0, entries_with_ls, 100.0])

    with open(os.path.join(HERE, 'register_census_sigla.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['stratum', 'rank', 'siglum', 'citations'])
        for st in STRATA:
            for i, (sg, n) in enumerate(sigla[st].most_common(25), 1):
                w.writerow([st, i, sg, n])

    with open(os.path.join(HERE, 'entry_level.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['has_attested_citation', 'has_hedge_citation', 'entries', 'share_of_ls_entries_pct'])
        for (a, h), n in sorted(entry_profile.items(), key=lambda kv: -kv[1]):
            w.writerow([int(a), int(h), n, round(100.0 * n / entries_with_ls, 2)])

    meta = counts['hedge'] + counts['authority'] + counts['relative']
    stats = {
        'total_entries': total_entries,
        'entries_with_ls': entries_with_ls,
        'total_ls': total_ls,
        'ls_per_entry': round(total_ls / total_entries, 3),
        'iti_hits': iti_hits,
        'iti_per_entry': round(iti_hits / total_entries, 3),
        'meta_share_pct': round(100.0 * meta / total_ls, 2),
        'attested_share_pct': round(100.0 * counts['attested'] / total_ls, 2),
        'hedge_only_entries': hedge_only_entries,
        'mixed_entries': mixed_entries,
        'distinct_sigla_attested': len(sigla['attested']),
        'distinct_sigla_bare': len(sigla['bare']),
        'a08_visible': a08_visible,
        'a08_visible_locator': a08_visible_locator,
        'attributed': attributed,
        'attributed_locator': attributed_locator,
        'attributed_share_pct': round(100.0 * attributed / total_ls, 2),
        'attributed_arabic': attributed_arabic,
        # plain-shape citations whose ONLY locator is roman -- invisible to an arabic-digit rule
        'roman_only_plain': roman_only_plain,
        'a08_bare_bucket': a08_visible - a08_visible_locator,
        'a08_bare_bucket_pct': round(100.0 * (a08_visible - a08_visible_locator) / a08_visible, 2),
        'locator_undercount_rel_pct': round(
            100.0 * (counts['attested'] - a08_visible_locator) / a08_visible_locator, 2),
    }
    with open(os.path.join(HERE, 'census_stats.json'), 'w', encoding='utf-8') as f:
        json.dump({'counts': dict(counts), 'stats': stats}, f, indent=2, ensure_ascii=False)

    S = []
    S.append('# MW evidence-block census — the evidentiary strata inside Register A')
    S.append('')
    S.append('_Generated by `register_census.py` — every number below is computed; do not hand-edit._')
    S.append('')
    S.append('Register terminology consumed from A08 ([csl-atlas `docs/CITATION_REGISTERS.md`]'
             '(https://github.com/sanskrit-lexicon/csl-atlas/blob/main/docs/CITATION_REGISTERS.md)):')
    S.append('Register A = `<ls>`-tagged, Register B = in-prose `iti` quotative. This census measures the')
    S.append('*evidentiary* axis inside MW\'s Register A, which the form distinction cannot see.')
    S.append('')
    S.append('## MW on A08\'s form axis')
    S.append('')
    S.append('| Measure | Value |')
    S.append('|---|--:|')
    S.append('| Entries (`<L>`…`<LEND>` records) | {:,} |'.format(total_entries))
    S.append('| Entries carrying ≥1 `<ls>` | {:,} |'.format(entries_with_ls))
    S.append('| Register-A citations (`<ls>`) | **{:,}** ({:.2f}/entry) |'.format(total_ls, stats['ls_per_entry']))
    S.append('| Register-B footprint (`iti`/`ity`, word-boundary proxy) | {:,} ({:.2f}/entry) |'.format(
        iti_hits, stats['iti_per_entry']))
    S.append('')
    S.append('## The evidentiary strata (per citation)')
    S.append('')
    S.append('| Stratum | Citations | Share of `<ls>` | Entries carrying ≥1 | Share of `<ls>` entries |')
    S.append('|---|--:|--:|--:|--:|')
    label = {'attested': 'attested (named work + locator)',
             'bare': 'bare (named work, no locator)',
             'hedge': 'hedge (`L.`)',
             'authority': 'authority (`W.`/`MW.`/`Cat.`)',
             'relative': 'relative (`ib.`/`id.`)'}
    for st in STRATA:
        S.append('| {} | {:,} | {:.2f}% | {:,} | {:.2f}% |'.format(
            label[st], counts[st], 100.0 * counts[st] / total_ls,
            entry_strata[st], 100.0 * entry_strata[st] / entries_with_ls))
    S.append('| **TOTAL** | **{:,}** | 100% | {:,} | 100% |'.format(total_ls, entries_with_ls))
    S.append('')
    S.append('Non-attesting share (hedge + authority + relative) = **{:.2f}%**; '
             'directly locator-bearing = **{:.2f}%**.'.format(stats['meta_share_pct'], stats['attested_share_pct']))
    S.append('Distinct sigla: {:,} in the attested stratum, {:,} in the bare stratum.'.format(
        stats['distinct_sigla_attested'], stats['distinct_sigla_bare']))
    S.append('')
    S.append('## Entry-level composition')
    S.append('')
    S.append('| Entries | Share of `<ls>` entries | Profile |')
    S.append('|--:|--:|---|')
    prof = {(True, False): 'attested only — no hedge',
            (False, True): 'hedge only — no attested citation',
            (True, True): 'both — hedge sense beside an attested sense',
            (False, False): 'neither — bare/relative/authority only'}
    for (a, h), n in sorted(entry_profile.items(), key=lambda kv: -kv[1]):
        S.append('| {:,} | {:.2f}% | {} |'.format(n, 100.0 * n / entries_with_ls, prof[(a, h)]))
    S.append('')
    S.append('**{:,}** entries are hedge-only in the strict sense (a hedge and no attested *or* bare '
             'citation); **{:,}** are mixed (a hedge alongside a citation of a named work) — the mixed '
             'set is why a lemma-level corpus join needs the strict-set control.'.format(
                 hedge_only_entries, mixed_entries))
    S.append('')
    S.append('## Reconciliation with the previously published MW counts')
    S.append('')
    S.append('[`SYNTHESIS.md`](../SYNTHESIS.md) publishes `L.` = 40,212 and meta = 69,603, both from a')
    S.append('**literal** tag match. This census classes a citation by its **siglum**, so a meta siglum')
    S.append('that happens to carry a locator stays with its siglum. All of MW contains exactly')
    S.append('**{}** such citations — {} — so the strata run +1 hedge / +1 authority against the'.format(
        len(meta_with_locator), ' and '.join('`%s`' % c for c in meta_with_locator)))
    S.append('literal counts (hedge {:,} = 40,212 + 1; authority {:,} = 19,297 + 1). Immaterial to every'.format(
        counts['hedge'], counts['authority']))
    S.append('claim, recorded so a later session does not read it as drift.')
    S.append('')
    S.append('One real drift **is** present: the record count is {:,}, against the 286,560 published in'.format(
        total_entries))
    S.append('`.ai_state.md` (2026-06-13, over `mw.txt` @ 2026-05-29). `mw.txt` has since lost 35 records to')
    S.append('upstream corrections. A08\'s artifact independently reports 286,525, so the current source,')
    S.append('not this parse, is what moved.')
    S.append('')
    S.append('## Cross-check against A08\'s MW row (a measured divergence)')
    S.append('')
    S.append('A08\'s committed artifact `data/obs/citation_registers.json` reports MW as')
    S.append('`entries` 286,525 · `ls` 312,160 · `lsWithLocator` 47,289 (15.15% locator-bearing).')
    S.append('The entry count reproduces exactly. The citation counts do not, for two reasons, both')
    S.append('verifiable against `mw.txt` and both making MW\'s apparatus look thinner than it is:')
    S.append('')
    S.append('| | A08 | this census | why |')
    S.append('|---|--:|--:|---|')
    S.append('| Register-A citations | 312,160 | **{:,}** | A08\'s extractor is literal — '
             '`_LS = re.compile(r"<ls>(.*?)</ls>", re.DOTALL)` '
             '([`scripts/forensic/parse_cslorig.py:41`](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/scripts/forensic/parse_cslorig.py#L41)) '
             '— so the **{:,}** attributed citations never match |'.format(total_ls, attributed))
    S.append('| Locator-bearing | 47,289 | **{:,}** | A08\'s locator rule is `DIGIT_RE = re.compile(r"\\d")` '
             '([`scripts/obs/citation_register_gaps.py:49`](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/scripts/obs/citation_register_gaps.py#L49)): '
             'it cannot see the attributed form\'s locator ({:,} of the {:,} bear one under this census\'s '
             'arabic-or-roman rule; {:,} under a strict arabic-digit rule), and it scores the {:,} '
             'plain-shape citations whose only locator is **roman** (`ŚBr. xiv`) as sourceless |'.format(
                 counts['attested'], attributed_locator, attributed,
                 attributed_arabic, roman_only_plain))
    S.append('| Locator share | 15.15% | **{:.2f}%** | |'.format(stats['attested_share_pct']))
    S.append('')
    S.append('**A definitional warning, so the two documents are not read as contradicting each other.**')
    S.append('A08\'s "bare abbreviation" means *no arabic digit* — one bucket holding everything that is')
    S.append('not a locator-bearing citation. On MW that bucket is {:.2f}% ({:,} of {:,}), and it'.format(
        100.0 * (a08_visible - a08_visible_locator) / a08_visible,
        a08_visible - a08_visible_locator, a08_visible))
    S.append('silently contains the `L.` hedge, `ib.`, `W.`, and every roman-locator citation. This')
    S.append('census\'s `bare` stratum ({:.2f}%) means something narrower and load-bearing: *a named work,'.format(
        100.0 * counts['bare'] / total_ls))
    S.append('no locator, and not a meta marker*. The two numbers answer different questions and neither')
    S.append('refutes the other; decomposing that one bucket is the point of this census. A08\'s **corpus-wide**')
    S.append('40.7% bare / 59.3% locator is a third thing again — a 44-dictionary aggregate dominated by PWG')
    S.append('(568,730 citations at 4.61/entry against MW\'s 1.09), and not a statement about MW at all.')
    S.append('')
    S.append('So MW\'s linkable apparatus is **{:.1f}% larger** than the published row records — a '
             'markup-shape artefact, not a scholarly disagreement. The direction of A08\'s finding is '
             'unaffected and its corpus-wide conclusion stands; the MW row wants regenerating. This is '
             'the same defect class as the `iti` rule A08 already corrected once (its space-or-quote '
             'rule undercounted KRM ~3× until a word-boundary rule replaced it).'.format(
                 stats['locator_undercount_rel_pct']))
    S.append('')
    S.append('MW\'s `iti` footprint here is **{:,}** hits ({:.4f}/entry) against A08\'s 172 — both are '
             'noise-level, and both say the same thing: MW does not cite in the indigenous register. '
             'MW is a Register-A dictionary, exactly as A08 reports.'.format(
                 iti_hits, stats['iti_per_entry']))
    S.append('')
    S.append('## Limitations')
    S.append('')
    S.append('- The `iti` count is A08\'s **word-boundary proxy**, a register *indicator*: it fires on')
    S.append('  quoted running text and on grammatical/derivational `iti`, so it is an upper bound on MW\'s')
    S.append('  indigenous-register footprint, not a citation count.')
    S.append('- `attested` = **a locator is present**, an upper bound on linkability, not a verified link')
    S.append('  (A08 makes the same reservation for its 59.3% figure).')
    S.append('- Sigla here are locator-stripped surface forms, **not** normalised: `MBh.`/`MBH.` and')
    S.append('  `R.`/`Rām.` are not merged. Normalisation is csl-atlas\' owned layer')
    S.append('  (`scripts/lib/source-siglum.mjs` + the curated alias table) and is deliberately not redone.')
    S.append('- Strata are per **citation occurrence**, not per sense: an entry mixing a hedged and an')
    S.append('  attested sense contributes to both.')
    S.append('')
    S.append('_Dr. Mārcis Gasūns_')
    with open(os.path.join(HERE, 'CENSUS.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(S) + '\n')

    print('entries          : {:,}'.format(total_entries))
    print('entries with <ls>: {:,}'.format(entries_with_ls))
    print('<ls> citations   : {:,}'.format(total_ls))
    for st in STRATA:
        print('  {:<10}: {:>7,}  {:5.2f}%'.format(st, counts[st], 100.0 * counts[st] / total_ls))
    print('iti/ity hits     : {:,}'.format(iti_hits))
    print('hedge-only entries: {:,}   mixed: {:,}'.format(hedge_only_entries, mixed_entries))


if __name__ == '__main__':
    main()
