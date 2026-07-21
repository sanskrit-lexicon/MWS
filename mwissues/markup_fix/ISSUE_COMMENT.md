### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 (PWG) and https://github.com/sanskrit-lexicon/PWK/issues/113 (PWK) for `mw.txt`.

I ran Claude over `csl-orig/v02/mw/mw.txt` with the same two-job recipe: auto-fix the few things with a single safe resolution; audit everything else with line refs. Added `08_markup_fix.py` plus outputs to a new `mwissues/markup_fix/` folder on the branch https://github.com/sanskrit-lexicon/MWS/pull/new/markup-fix-audit.

@funderburkjim @Andhrabharati — would value a look at the 9,313 adjacent `</ab> <ab>` list and the 6 nested `<ls>` cases inside `{{…}}` correction blocks.

## Markup fixer + audit for `mw.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>vor.</ab> W.</ab>` | `<ab>vor. W.</ab>` |
| `<ab n="X"><ab>St.</ab></ab>` | `<ab n="X">St.</ab>` |
| `<ab>foo<ab>bar</ab>baz</ab>` | `<ab>foobarbaz</ab>` |
| `<ls> GORR. 1,69,9 </ls>` | `<ls>GORR. 1,69,9</ls>` |
| `<lex> mf. </lex>` | `<lex>mf.</lex>` |
| `<etym> root </etym>` | `<etym>root</etym>` |

Whitespace trimming applies to all 19 paired tags that actually occur in `mw.txt`: `<s>`, `<ls>`, `<lex>`, `<ab>`, `<s1>`, `<hom>`, `<bot>`, `<lang>`, `<etym>`, `<ns>`, `<pcol>`, `<gk>`, `<bio>`, `<i>`, `<arab>`, `<old>`, `<chg>`, `<new>`, `<is>`. The original file is never modified — output goes to `mw_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format).

### Closing-tag inventory in current `mw.txt`

| Tag | Count |
|---|---:|
| `</s>` | 350,610 |
| `</ls>` | 320,827 |
| `</lex>` | 201,941 |
| `</ab>` | 194,879 |
| `</s1>` | 54,666 |
| `</hom>` | 11,517 |
| `</bot>` | 8,923 |
| `</lang>` | 3,968 |
| `</etym>` | 2,637 |
| `</ns>` | 2,210 |
| `</pcol>` | 1,553 |
| `</gk>` | 1,127 |
| `</bio>` | 358 |
| `</i>` | 197 |
| `</arab>` | 97 |
| `</old>` | 39 |
| `</chg>` | 39 |
| `</new>` | 35 |
| `</is>` | 2 |
| `<srs/>` (self-closing) | 37,041 |
| `<br/>` (self-closing) | 1 |

mw.txt is much richer than PWG/PWK: 22 paired tag types vs PWG's 5 and PWK's 12. Every open/close count matches at the file level (tag-balanced).

### What it found in current `mw.txt`

- **0** nested `<ab>` — clean.
- **9** whitespace trims — applied across <lex>, <s>, <s1>, <bot>, <bio>, <arab>, <old>, <new>. Unlike PWK's 0 trims, mw.txt had minor leading/trailing spaces in 9 lines; all fixed.
- **0** `<ab n="?">` placeholders (unlike PWG's 91). Instead, mw.txt has 12,779 `<ab n="…">` entries with 1,747 unique German expansions (top values: "great" 371, "one" 285, "hundred" 280).
- **6** nested `<ls>` — all inside `{{ … }}` correction records (correction-record format from prior work). Flagged informationally; not touched.
- **0** boundary collisions — mw.txt is clean on `{%…%}<is>`, `{#…#}<ab>/<ls>/<is>`, and `</ls>.[Page…]` patterns.
- **9,313** adjacent `</ab> <ab>` — listed for verification. Spot checks show mostly intentional pairs (`<ab>Nom.</ab> <ab>pl.</ab>`, `<ab>cf.</ab> <ab>perf.</ab>`, etc.); not auto-merged.

### Broader cleanup checklist (in `markup_audit.txt`)

1. **Adjacent `</ab> <ab>`** — 9,313 occurrences (much higher than PWG's 9, PWK's 4,171). Nearly all are two-abbreviation combinations; only flag if a pair *should* collapse into a single `<ab>`.
2. **Nested `<ls>` inside `{{ … }}`** — 6 occurrences. Informational; part of the correction-record format.
3. **Whitespace-inside-tag cleanups** — 9 auto-fixed. Unlike the thousands in PWK, mw.txt needed only minor touches.
4. **`<ab n="?">` placeholders** — 0. mw.txt is fully typed with real German values (unlike PWG's 91 un-expanded placeholders).
5. **Specialized tag content** — `<s>` (Sanskrit text) 350K, `<s1>` 54K, `<etym>` 2.6K, `<ns>` 2.2K, `<pcol>` 1.5K, `<bio>` 358. Low enough that visual review is cheap; not addressed here.
6. **Self-closing tags** — `<srs/>` (Sanskrit syllable references) 37K, `<br/>` 1. No action needed.

### Usage

```sh
cd mwissues/markup_fix
python 08_markup_fix.py
# default in:  ../../../csl-orig/v02/mw/mw.txt
# default out: mw_fixed.txt

# Or on a wrapped output:
python 08_markup_fix.py mw_with_abs.txt mw_with_abs_fixed.txt
```

Synthetic-input tests of the nesting fixer and trim fixer all pass (`python test_markup_fix.py` — 7/7).

### Summary

mw.txt is in excellent shape: tag-balanced, no nested `<ab>`, no `<ab n="?">` placeholders, minimal whitespace issues (only 9 auto-fixes vs. thousands in PWK). The single biggest finding is 9,313 adjacent `</ab> <ab>` patterns — intentional two-abbreviation pairs, mostly; listed for review.

The markup structure is much richer than PWG/PWK: 22 paired tags plus specialized semantic tags (`<etym>`, `<bio>`, `<pcol>`) and record-change tags (`<old>`, `<chg>`, `<new>`) support fine-grained documentation of the 1899 print edition.

### Severity

minor — a handful of whitespace fixes, hundreds of singletons to audit, no structural problems.
