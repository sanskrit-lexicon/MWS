# SPEC-3 — W3: C-SALT parity report + Phase-2 closeout

_Created: 02-07-2026 · Last updated: 02-07-2026_

**Tier:** Sonnet 5 (`claude-sonnet-5`). **Repo:** [csl-apidev](https://github.com/sanskrit-lexicon/csl-apidev)
(PR-only). Phase 1 (+ the graphql controller) already merged in
[PR #46](https://github.com/sanskrit-lexicon/csl-apidev/pull/46).

## Objective

Prove MW parity against the live C-SALT API and close out the remaining Phase-2 items, so
September's Phase-3 memo (expand to 7 vs ~40 dicts — Jim's call) argues from evidence.

## Steps

1. **Parity script**: for a fixed sample (500 headwords stratified by first letter + the
   `salt_ids` edge cases in [doc/](https://github.com/sanskrit-lexicon/csl-apidev/tree/master/doc)),
   query local `salt_entries.php`/`salt_ids.php` and the live C-SALT MW endpoints; diff
   field-by-field; emit `reports/salt_parity_mw_2026-07.md` — a loss table (field, sample
   count, match %, worst 5 diffs verbatim).
2. **GraphQL**: run the same sample through the merged graphql controller vs
   [salt_graphql doc](https://github.com/sanskrit-lexicon/csl-apidev/blob/master/doc/salt_graphql.md)
   contract; note gaps (don't silently fix contract questions — log them for the planning
   session).
3. **Clean-URL start**: `/MW/{ref}` content negotiation per
   [cleanurl doc](https://github.com/sanskrit-lexicon/csl-apidev/tree/master/doc), dict-code
   whitelist hardcoded to `mw` for now.
4. PR with the report + any code; auto-merge NOT enabled (Jim reviews API-shape changes).

## Acceptance

- Parity report exists with per-field match rates; any field <99% has its diff class named.
- No deployment steps attempted (Cologne server is Jim's; local work stops at tested PR).

## Guardrails

Semgrep echoed-request findings in this repo are taint-mode noise once `htmlspecialchars`
is applied — fix real reflections, dismiss the rest with justification (org playbook).

_Dr. Mārcis Gasūns_
