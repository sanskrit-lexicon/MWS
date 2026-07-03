"""Synthetic-input tests for 08_markup_fix.py."""

import sys
import importlib.util
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("mfix", HERE / "08_markup_fix.py")
mfix = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mfix)

cases = [
    # nested <ab>
    ("<ab><ab>vor.</ab> W.</ab>", "<ab>vor. W.</ab>"),
    ('<ab n="x"><ab>St.</ab></ab>', '<ab n="x">St.</ab>'),
    ("<ab>foo<ab>bar</ab>baz</ab>", "<ab>foobarbaz</ab>"),
    ("<ab>N. pr.</ab> <ab>u. s. w.</ab>", "<ab>N. pr.</ab> <ab>u. s. w.</ab>"),
    # whitespace trim
    ("<ls> GORR. 1,69,9 </ls>", "<ls>GORR. 1,69,9</ls>"),
    ("<lex> mf. </lex>", "<lex>mf.</lex>"),
    ("<ab> priv. </ab>", "<ab>priv.</ab>"),
]

ok = 0
fail = 0
for src, want in cases:
    line, _ = mfix.fix_nested_ab(src)
    line, _ = mfix.fix_trim_whitespace(line)
    if line == want:
        ok += 1
        print(f"  PASS  {src!r}  →  {line!r}")
    else:
        fail += 1
        print(f"  FAIL  {src!r}")
        print(f"        got:  {line!r}")
        print(f"        want: {want!r}")

print(f"\n{ok} passed, {fail} failed")
sys.exit(0 if fail == 0 else 1)
