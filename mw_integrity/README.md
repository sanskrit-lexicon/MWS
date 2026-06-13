# mw.txt structural-integrity review

A single-pass structural check of the canonical
[`csl-orig/v02/mw/mw.txt`](../../csl-orig/v02/mw/mw.txt) — the *dictionary data*,
not the tooling. Analysis only; mutates nothing.

## Verdict: structurally sound

286,560 records, perfectly `<L>`/`<LEND>`-balanced, **no BOM**, **no duplicate
L-numbers**, **no replacement chars**, and every paired tag + brace marker
(`{# #}`, `{% %}`, `{{ }}`) balanced within every record. See
[INTEGRITY_REPORT.md](INTEGRITY_REPORT.md).

**One** cosmetic flag in 286,560 records: **L27713.2** has two trailing spaces
after `<e>2` (a supplement entry, page 1320,2). Not structure-breaking, but a
strict parser expecting `<e>N\n` could trip — a one-line trailing-whitespace trim,
maintainer-gated like any `mw.txt` edit.

## Checks

| check | result |
|---|---|
| `<L>`/`<LEND>` balance | ✅ 286,560 = 286,560 |
| UTF-8 BOM | ✅ none |
| duplicate L-numbers | ✅ 0 |
| header fields (k1/k2/e/pc present, k1 non-empty) | ✅ |
| `<e>` code valid (`^[1-9][0-9]*[A-Z]?$`) | ⚠️ 1 (trailing space) |
| per-record paired-tag balance (s, ls, lex, ab, …) | ✅ |
| brace-marker balance | ✅ |
| U+FFFD replacement chars | ✅ 0 |

## Scope / limits

- The paired-tag check validates **count** balance per record, not nesting order
  (a separate, deeper check). The phw cross-reference graph — a different integrity
  layer — is audited in [phw_graph/](../phw_graph/) (31 broken links).
- The open-tag regex allows attributes (`<ab n="…">`, `<lex type="phw">`); an
  earlier version that didn't produced 25,670 false positives — a reminder that a
  "finding" should be sanity-checked before it's believed.

## Files

| File | What |
|---|---|
| [`mw_integrity.py`](mw_integrity.py) | the checker (`python mw_integrity.py`) |
| `integrity_issues.csv` | every flagged record (currently 1) |
| [`INTEGRITY_REPORT.md`](INTEGRITY_REPORT.md) | the report |
