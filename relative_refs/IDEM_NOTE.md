# `<ab>id.</ab>` (idem) — sibling task, scoped for issue #98

`<ab>id.</ab>` (**4,401** instances) is the *sense*-level analog of `ib.`: it
means "same meaning as the immediately preceding entry/sense." It is the subject
of open issue [#98](https://github.com/sanskrit-lexicon/MWS/issues/98).

Examples (from `mw.txt`):
- `a-tandrin ¦ mfn. <ab>id.</ab>` → same meaning as the preceding `a-tandra`.
- `adamuy-aYc ¦ <ab>id.</ab>` → same meaning as the preceding headword.

## Resolution approach (deterministic, document order)

For each record whose gloss is `<ab>id.</ab>` (optionally after a `<lex>`):
the resolved meaning = the **gloss of the immediately preceding record** (the
nearest preceding `¦`-gloss that is itself not `id.`; chain `id.`→`id.` like
`ib.`). This is the same antecedent walk as `ib_resolve.py`, but the antecedent
is a gloss span rather than an `<ls>`.

## Why it's not built here

Unlike `ib.` (antecedent is a self-contained siglum), an `id.` resolution must
**copy a gloss**, which raises display/markup questions a maintainer should rule
on first:
- materialize the borrowed gloss inline, or render it live from the antecedent?
- how to show provenance ("= prev.") so the borrow stays visible?

These are display-policy decisions, not mechanical ones — so this is parked as a
spec for #98, not auto-applied. The mechanical half (building the
record→antecedent-gloss map) is a ~1-session job once the policy is set.

## Quick stats

| marker | count | antecedent | resolver |
|---|--:|---|---|
| `<ls>ib.</ls>` | 10,094 | preceding `<ls>` | **built** — `ib_resolve.py` (57.1% same-cluster high-confidence; 74.7% upper bound, resolvable not verified) |
| `<ab>id.</ab>` | 4,401 | preceding gloss | spec only (this note), issue #98 |
