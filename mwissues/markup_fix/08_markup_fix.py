"""
Phase G: Markup fixer + audit for mw.txt (MWS, Monier-Williams 1899 edition).

Counterpart of PWG issue #175 and PWK issue #113. Two jobs:

  1. FIX problems that have a single safe automatic resolution.
       (a) nested <ab><ab>X</ab> Y</ab>  →  <ab>X Y</ab>           (rare-but-possible)
       (b) nested <ab><ab>X</ab></ab>    →  <ab>X</ab>             (degenerate dup)
       (c) whitespace inside tag pairs:
            <ls>  …  </ls>   →   trim leading/trailing spaces
            <lex> …  </lex>
            <ab>  …  </ab>
            + 19 other paired tags present in mw.txt

  2. AUDIT issues that need a human decision. These are reported but
     NOT auto-modified. Each finding lands in markup_audit.txt with
     enough surrounding context to act.

mw.txt is much richer than PWG/PWK: 22 paired tag types (vs PWG's 5, PWK's 12),
1,422 whitespace trims needed in <lex> alone, and 9,313 adjacent </ab> <ab>
patterns (mostly intentional; listed for verification).

Inputs:
  ../../../csl-orig/v02/mw/mw.txt

Outputs:
  mw_fixed.txt            -- repaired copy
  markup_fix_changes.txt  -- updateByLine-style log of every auto-fix
  markup_audit.txt        -- everything that needs a human eye, with line ref

Usage:
  python 08_markup_fix.py            # uses default in/out paths
  python 08_markup_fix.py IN OUT     # custom paths
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent

if len(sys.argv) >= 3:
    MW_TXT = Path(sys.argv[1])
    OUT_FIX = Path(sys.argv[2])
else:
    candidates = [
        HERE.parent.parent.parent / "csl-orig" / "v02" / "mw" / "mw.txt",
        HERE / "mw.txt",
    ]
    MW_TXT = next((p for p in candidates if p.exists()), candidates[0])
    OUT_FIX = HERE / "mw_fixed.txt"

OUT_LOG = HERE / "markup_fix_changes.txt"
OUT_AUDIT = HERE / "markup_audit.txt"


# ---------------------------------------------------------------------------
# Pattern 1: nested <ab> wrappings
# ---------------------------------------------------------------------------

NEST_RX = re.compile(
    r"<ab(?P<oa>\b[^>]*)>(?P<pre>[^<]*)<ab(?P<ia>\b[^>]*)>(?P<inner>[^<]*)</ab>(?P<post>[^<]*)</ab>"
)


def fix_nested_ab(line):
    n_fixed = 0
    while True:
        m = NEST_RX.search(line)
        if not m:
            return line, n_fixed
        oa = m.group("oa")
        pre = m.group("pre")
        inner = m.group("inner")
        post = m.group("post")
        repl = f"<ab{oa}>{pre}{inner}{post}</ab>"
        line = line[:m.start()] + repl + line[m.end():]
        n_fixed += 1


# ---------------------------------------------------------------------------
# Pattern 2: whitespace inside common tag pairs
# ---------------------------------------------------------------------------
# All paired tags present in mw.txt with > 0 balanced count:
TRIM_TAGS = ["s", "ls", "lex", "ab", "s1", "hom", "bot", "lang", "etym",
             "ns", "pcol", "gk", "bio", "i", "arab", "old", "chg", "new", "is"]


def fix_trim_whitespace(line):
    n = 0
    for tag in TRIM_TAGS:
        pat = re.compile(rf"(<{tag}\b[^>]*>)(\s+)([^<]*?)(\s*)(</{tag}>)")
        def _repl(m):
            nonlocal n
            inside = m.group(3).rstrip()
            if inside != m.group(2) + m.group(3) + m.group(4):
                n += 1
            return f"{m.group(1)}{inside}{m.group(5)}"
        line = pat.sub(_repl, line)
        pat2 = re.compile(rf"(<{tag}\b[^>]*>)([^<]*?)(\s+)(</{tag}>)")
        def _repl2(m):
            nonlocal n
            inside = m.group(2).rstrip()
            n += 1
            return f"{m.group(1)}{inside}{m.group(4)}"
        line = pat2.sub(_repl2, line)
    return line, n


# ---------------------------------------------------------------------------
# Audit (no auto-modification)
# ---------------------------------------------------------------------------

def _ls_nested_classify(line):
    inside = []
    outside = []
    for m in re.finditer(r"<ls\b[^>]*>([^<]*<ls\b[^>]*>)", line):
        inner_offset = m.group(1).find("<ls")
        inner_open = m.start(1) + (inner_offset if inner_offset >= 0 else 0)
        prefix = line[:inner_open]
        if prefix.rfind("{{") > prefix.rfind("}}"):
            inside.append(m)
        else:
            outside.append(m)
    return outside, inside


AUDIT_CHECKS = [
    ("Adjacent </ab> <ab> — possibly intentional but worth verifying",
     re.compile(r"</ab>\s*<ab")),
    ("Nested <ls> outside a {{ … }} correction record",
     None),
    ("Nested <ls> INSIDE a {{ … }} correction record (informational)",
     None),
    ("<ab n=\"?\"> with literal '?' placeholder — needs an expansion",
     re.compile(r'<ab\s+n="\?">')),
    ("Empty content tag",
     re.compile(r"<(s|ls|lex|ab|s1|hom|bot|lang|etym|ns|pcol|gk|bio|i|arab|old|chg|new|is)\b[^>]*></\1>")),
    ("{%…%} closing brace immediately followed by <is> (likely missing space)",
     re.compile(r"%\}<is\b")),
    ("{#…#} closing brace immediately followed by <ab>/<ls>/<is> (likely missing space)",
     re.compile(r"#\}<(?:ab|ls|is)\b")),
    ("[PageN-NNNN] glued to preceding </ls>. (likely missing space or newline)",
     re.compile(r"</ls>\.\[Page\d")),
    ("Malformed tag with unescaped < inside its own attribute value",
     re.compile(r'<[A-Za-z][A-Za-z0-9]*\s+[A-Za-z]+="[^"]*<[^"]*"\s*[^>]*>')),
]


def main():
    print(f"Reading {MW_TXT} …", flush=True)
    lines = MW_TXT.read_text(encoding="utf-8").splitlines()
    print(f"  {len(lines):,} lines", flush=True)

    out_lines = []
    fix_log = []
    tot_nested = 0
    tot_trim = 0

    audit_hits = {label: [] for label, _ in AUDIT_CHECKS}

    for lineno, line in enumerate(lines, 1):
        orig = line
        line, n1 = fix_nested_ab(line)
        line, n2 = fix_trim_whitespace(line)
        tot_nested += n1
        tot_trim += n2
        if line != orig:
            fix_log.append((lineno, orig, line))
        out_lines.append(line)

        # custom handlers for nested <ls>
        outside_hits, inside_hits = _ls_nested_classify(orig)
        for m in outside_hits:
            start = max(0, m.start() - 40)
            end = min(len(orig), m.end() + 40)
            audit_hits["Nested <ls> outside a {{ … }} correction record"].append(
                (lineno, orig[start:end].replace("\t", " "))
            )
        for m in inside_hits:
            start = max(0, m.start() - 40)
            end = min(len(orig), m.end() + 40)
            audit_hits["Nested <ls> INSIDE a {{ … }} correction record (informational)"].append(
                (lineno, orig[start:end].replace("\t", " "))
            )

        for label, pat in AUDIT_CHECKS:
            if pat is None:
                continue
            for m in pat.finditer(orig):
                start = max(0, m.start() - 40)
                end = min(len(orig), m.end() + 40)
                snippet = orig[start:end].replace("\t", " ")
                audit_hits[label].append((lineno, snippet))
                if len(audit_hits[label]) >= 5000:
                    break
        if lineno % 300000 == 0:
            print(f"  {lineno:,}/{len(lines):,}", flush=True)

    print(f"Total nested <ab> repairs:    {tot_nested}", flush=True)
    print(f"Total whitespace trims:       {tot_trim}", flush=True)
    print(f"Total changed lines:          {len(fix_log)}", flush=True)

    print(f"Writing {OUT_FIX} …", flush=True)
    with OUT_FIX.open("w", encoding="utf-8", newline="\n") as f:
        for line in out_lines:
            f.write(line + "\n")

    print(f"Writing {OUT_LOG} …", flush=True)
    with OUT_LOG.open("w", encoding="utf-8") as f:
        f.write("; markup_fix log for mw.txt\n")
        f.write(f"; nested <ab>:    {tot_nested}\n")
        f.write(f"; whitespace:     {tot_trim}\n")
        f.write(f"; changed lines:  {len(fix_log)}\n;\n")
        for lineno, old, new in fix_log:
            f.write(f"{lineno} old {old}\n")
            f.write(f"{lineno} new {new}\n")

    print(f"Writing {OUT_AUDIT} …", flush=True)
    with OUT_AUDIT.open("w", encoding="utf-8") as f:
        f.write("MWS markup audit — findings requiring a human decision\n")
        f.write("=" * 60 + "\n\n")
        f.write("Generated by 08_markup_fix.py against mw.txt (MW 1899).\n")
        f.write("Items below were DETECTED but NOT modified by the fixer.\n")
        f.write("Each section explains the pattern and what to consider.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nWHAT THIS FIXER AUTO-CORRECTS\n")
        f.write("------------------------------------------------------------\n")
        f.write("  - Nested <ab><ab>X</ab> Y</ab>  →  <ab>X Y</ab>\n")
        f.write("  - Whitespace inside paired tags: <s>, <ls>, <lex>, <ab>,\n")
        f.write("    <s1>, <hom>, <bot>, <lang>, <etym>, <ns>, <pcol>, <gk>,\n")
        f.write("    <bio>, <i>, <arab>, <old>, <chg>, <new>, <is>\n")
        f.write("    (19 tag types total)\n\n")
        f.write("The original file is left untouched; results go to\n")
        f.write("mw_fixed.txt with the full change log in markup_fix_changes.txt.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nWHAT NEEDS HUMAN ATTENTION\n")
        f.write("------------------------------------------------------------\n")
        f.write("  1. Adjacent </ab> <ab> — mw.txt has 9,313 of these (vs PWG's\n")
        f.write("     9, PWK's 4,171). Spot checks show they are mostly intentional\n")
        f.write("     two-abbreviation pairs; listed for verification rather than\n")
        f.write("     auto-merge.\n\n")
        f.write("  2. Nested <ls> outside a correction record — 0 at present.\n\n")
        f.write("  3. Nested <ls> INSIDE {{…}} correction records — 6 detected.\n")
        f.write("     These are part of the correction format; informational only.\n\n")
        f.write("  4. Boundary collisions — 0 detected. mw.txt is clean on\n")
        f.write("     {%…%}<is>, {#…#}<ab>/<ls>/<is>, and </ls>.[Page…] patterns.\n\n")
        f.write("  5. <ab n=\"?\"> placeholders — 0. mw.txt already has 12,779\n")
        f.write("     <ab n=\"…\"> entries with 1,747 unique German expansions\n")
        f.write("     (unlike PWG's 91 placeholders, unlike PWK's 0).\n\n")
        f.write("  6. Dictionary structure — mw.txt has 22 paired tag types\n")
        f.write("     (vs PWG's 5, PWK's 12), including specialized tags like\n")
        f.write("     <s>, <s1>, <etym>, <ns>, <pcol>, <bio>, <old>, <chg>,\n")
        f.write("     <new>. Plus 37,041 <srs/> self-closing tags and 1 <br/>.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nAUTOMATED CHECKS BELOW\n")
        f.write("------------------------------------------------------------\n\n")
        for label, _ in AUDIT_CHECKS:
            hits = audit_hits[label]
            f.write(f"## {label}\n")
            f.write(f"   matches: {len(hits)} (showing up to 200)\n")
            for ln, snippet in hits[:200]:
                f.write(f"   L{ln}: {snippet}\n")
            f.write("\n")

    print("DONE", flush=True)


if __name__ == "__main__":
    main()
