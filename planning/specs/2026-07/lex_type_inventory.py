#!/usr/bin/env python3
# coding: utf-8
"""lex_type_inventory.py — SPEC-5 §3 evidence build (MWS issue #215).

Inventories every `<lex type="X">` value found in mw.txt: count, 3 sample
records each (L number, headword, one-line context), and whether the same
record also carries an `<info lex="...">` attribute (the derivability
question SPEC-5 §3 asks). Read-only against csl-orig; writes only the
markdown report next to this script.

Usage:
    python lex_type_inventory.py <path-to-mw.txt> <path-to-output.md>
"""
from __future__ import print_function
import sys
import re
import io
from collections import OrderedDict

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

LEX_TYPE_RE = re.compile(r'<lex type="([^"]*)">(.*?)</lex>')
INFO_LEX_RE = re.compile(r'<info[^>]*\blex="([^"]*)"')
L_RE = re.compile(r'^<L>([^<]*)')
K1_RE = re.compile(r'<k1>([^<]*)')


def iter_records(path):
    """Yield (metaline, body_lines) for each <L>...<LEND> record."""
    with io.open(path, encoding='utf-8') as f:
        metaline = None
        body = []
        in_record = False
        for line in f:
            line = line.rstrip('\r\n')
            if line.startswith('<L>'):
                in_record = True
                metaline = line
                body = []
            elif line.startswith('<LEND>'):
                if in_record:
                    yield metaline, body
                in_record = False
                metaline = None
                body = []
            elif in_record:
                body.append(line)


def main():
    if len(sys.argv) != 3:
        print("usage: lex_type_inventory.py <mw.txt> <output.md>", file=sys.stderr)
        sys.exit(1)
    mw_path, out_path = sys.argv[1], sys.argv[2]

    # type -> {count, samples: [(L, key1, context)], with_info_lex: count}
    stats = OrderedDict()
    total_records_scanned = 0
    total_lex_type_records = 0

    for metaline, body in iter_records(mw_path):
        total_records_scanned += 1
        m_l = L_RE.match(metaline)
        m_k1 = K1_RE.search(metaline)
        lnum = m_l.group(1) if m_l else '?'
        key1 = m_k1.group(1) if m_k1 else '?'
        record_text = '\n'.join(body)

        type_matches = LEX_TYPE_RE.findall(record_text)
        if not type_matches:
            continue
        total_lex_type_records += 1
        has_info_lex = bool(INFO_LEX_RE.search(record_text))

        for typ, content in type_matches:
            entry = stats.setdefault(typ, {'count': 0, 'samples': [], 'with_info_lex': 0})
            entry['count'] += 1
            if has_info_lex:
                entry['with_info_lex'] += 1
            if len(entry['samples']) < 3:
                snippet = record_text.strip()
                if len(snippet) > 160:
                    snippet = snippet[:157] + '...'
                entry['samples'].append((lnum, key1, content, snippet))

    write_report(out_path, stats, total_records_scanned, total_lex_type_records)
    print("Wrote %s" % out_path)
    print("Records scanned: %d; records with <lex type=>: %d" % (
        total_records_scanned, total_lex_type_records))
    for typ, entry in stats.items():
        print("  %-8s count=%-6d with_info_lex=%d" % (typ, entry['count'], entry['with_info_lex']))


TOOL_USAGE = {
    'phw': "Read by phw_graph/phw_audit.py (this repo) to reconstruct the "
           "phrasal-headword parent/child graph via the companion "
           "`<info phwchild=>`/`<info phwparent=>` attributes; no consumer "
           "found in csl-pywork display code or the funderburkjim/MWlexnorm "
           "step0 script (external repo, not present in this checkout — "
           "verify against its source before ruling it unread).",
    'hw': "No consumer found in csl-pywork display code (grepped v02/ for "
          "the literal attribute string) or in this repo's own scripts; "
          "funderburkjim/MWlexnorm step0 not present locally — unverified.",
    'hwifc': "No consumer found in csl-pywork display code or this repo's "
             "scripts; funderburkjim/MWlexnorm step0 not present locally — "
             "unverified.",
    'hwalt': "No consumer found in csl-pywork display code or this repo's "
             "scripts; funderburkjim/MWlexnorm step0 not present locally — "
             "unverified.",
    'nhw': "No consumer found in csl-pywork display code or this repo's "
           "scripts; funderburkjim/MWlexnorm step0 not present locally — "
           "unverified.",
    'hwinfo': "No consumer found in csl-pywork display code or this repo's "
              "scripts; funderburkjim/MWlexnorm step0 not present locally — "
              "unverified.",
    'part': "No consumer found in csl-pywork display code or this repo's "
            "scripts; funderburkjim/MWlexnorm step0 not present locally — "
            "unverified.",
}

DEFINITIONS = {
    'phw': "Phrasal headword — an inline phrase promoted to an addressable sub-entry",
    'hw': "Headword form",
    'hwifc': "Headword in fine compositi (compound-final form)",
    'hwalt': "Alternate headword form",
    'nhw': "Nominal headword form",
    'hwinfo': "Headword annotation",
    'part': "Participle",
}

ALL_TAXONOMY_TYPES = ['phw', 'hw', 'hwifc', 'hwalt', 'nhw', 'hwinfo', 'part']


def write_report(out_path, stats, total_records_scanned, total_lex_type_records):
    lines = []
    lines.append("# `<lex type=X>` inventory — SPEC-5 §3 evidence (MWS issue #215)")
    lines.append("")
    lines.append("_Generated by [`lex_type_inventory.py`](lex_type_inventory.py) against "
                  "csl-orig `mw.txt`. Re-run to refresh: "
                  "`python lex_type_inventory.py <path-to-mw.txt> lex_type_inventory.md`._")
    lines.append("")
    lines.append("Evidence only, per SPEC-5 §3 — **no keep/drop ruling here**; that is "
                  "the August planning session's call, per "
                  "[PLANNING_2026-07.md](../../PLANNING_2026-07.md) §3.")
    lines.append("")
    lines.append("**Scope note:** the handoff that requested this inventory framed it as "
                  "\"215 MW lexicographic entry types\" — that count does not occur anywhere "
                  "in the committed data. `#215` is "
                  "[MWS issue #215](https://github.com/sanskrit-lexicon/MWS/issues/215), "
                  "which asks for exactly this table: every `<lex type=X>` value, not "
                  "a taxonomy of 215 grammatical categories. The real distinct-value count "
                  "is reported below.")
    lines.append("")
    lines.append("Records scanned: **%d**. Records containing at least one `<lex type=>` tag: "
                  "**%d**. Distinct `type` values found: **%d**." % (
                      total_records_scanned, total_lex_type_records, len(stats)))
    lines.append("")
    lines.append("## Inventory")
    lines.append("")
    lines.append("| type | definition | count | derivable from `<info lex=>`? | example key |")
    lines.append("|---|---|--:|---|---|")

    seen = set()
    for typ in ALL_TAXONOMY_TYPES:
        entry = stats.get(typ)
        seen.add(typ)
        definition = DEFINITIONS.get(typ, '*(undocumented type — new since last audit)*')
        if entry is None:
            lines.append("| `%s` | %s | 0 | n/a — zero attestations | — |" % (typ, definition))
            continue
        count = entry['count']
        with_info = entry['with_info_lex']
        pct = (100.0 * with_info / count) if count else 0.0
        derivable = "%d/%d (%.1f%%) co-occur with `<info lex=>`" % (with_info, count, pct)
        example_key = entry['samples'][0][1] if entry['samples'] else '—'
        lines.append("| `%s` | %s | %d | %s | `%s` |" % (
            typ, definition, count, derivable, example_key))

    # Any type value found in the data but not in the known taxonomy above.
    for typ, entry in stats.items():
        if typ in seen:
            continue
        definition = '*(undocumented type — not in the prior DATA_DICTIONARY.md table)*'
        count = entry['count']
        with_info = entry['with_info_lex']
        pct = (100.0 * with_info / count) if count else 0.0
        derivable = "%d/%d (%.1f%%) co-occur with `<info lex=>`" % (with_info, count, pct)
        example_key = entry['samples'][0][1] if entry['samples'] else '—'
        lines.append("| `%s` | %s | %d | %s | `%s` |" % (
            typ, definition, count, derivable, example_key))

    lines.append("")
    lines.append("## Which tools read each type")
    lines.append("")
    lines.append("Checked: csl-pywork display code (`v02/`, grepped for the literal "
                  "`type=\"X\"` attribute string), this repo's own `phw_graph/` scripts. "
                  "`funderburkjim/MWlexnorm` step0 is referenced in SPEC-5 §3 as a "
                  "tool to check but is not cloned in this GitHub directory — its "
                  "usage is reported as unverified, not absent.")
    lines.append("")
    for typ in ALL_TAXONOMY_TYPES:
        lines.append("- **`%s`**: %s" % (typ, TOOL_USAGE.get(typ, 'not checked.')))
    lines.append("")
    lines.append("## Sample records")
    lines.append("")
    for typ in ALL_TAXONOMY_TYPES:
        entry = stats.get(typ)
        lines.append("### `%s`" % typ)
        lines.append("")
        if not entry or not entry['samples']:
            lines.append("_Zero attestations in the current data._")
            lines.append("")
            continue
        for lnum, key1, content, snippet in entry['samples']:
            lines.append("- `L=%s` key1=`%s` content=`%s`" % (lnum, key1, content))
            lines.append("  ```")
            lines.append("  %s" % snippet)
            lines.append("  ```")
        lines.append("")

    with io.open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
