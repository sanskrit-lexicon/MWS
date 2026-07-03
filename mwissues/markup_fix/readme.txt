MWS markup-fixer drop, counterpart of PWG issue #175 and PWK issue #113.

Files:
  08_markup_fix.py        the fixer + audit, runnable against mw.txt
  test_markup_fix.py      synthetic-input tests (7/7 pass)
  markup_audit.txt        human-review list produced by the run on mw.txt
  markup_fix_changes.txt  change log (updateByLine format) — populated with 9 actual whitespace fixes
  mw_fixed.txt            output file
  ISSUE_COMMENT.md        GitHub opening-issue comment
  readme.txt              this file

Run:
  python 08_markup_fix.py
  python test_markup_fix.py
