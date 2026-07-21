# `mw.txt` structural-integrity review

- Records: **286,560** `<L>` / **286,560** `<LEND>` ✅ balanced
- BOM: ✅ none
- Duplicate L-numbers: 0
- U+FFFD replacement chars: 0
- **Total issues flagged: 1**

## By class
| issue | count |
|---|--:|
| `bad_e_code` | 1 |

## Every flagged record
| kind | L | detail |
|---|---|---|
| `bad_e_code` | 27713.2 | <e>2   |

## Verdict
`mw.txt` is **structurally sound**: 286,560 records, perfectly `<L>`/`<LEND>`-balanced, no BOM, no duplicate L-numbers, no replacement chars, and all paired tags + brace markers balanced within every record.
The only flag is **1 record(s)** — listed above; cosmetic, not structure-breaking. Note: the per-record paired-tag check only validates *count* balance, not nesting order.

Analysis only — no `mw.txt` change.
