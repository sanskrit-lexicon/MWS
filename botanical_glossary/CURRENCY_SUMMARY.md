# MW botanical crosswalk — GBIF nomenclatural-currency pass

Resolved **1,223** canonical species against the GBIF Backbone Taxonomy (`/species/match`, kingdom Plantae; folds POWO + IPNI + Catalogue of Life).

## Taxonomic status of MW's names
| GBIF status | species | % of all |
|---|--:|--:|
| ACCEPTED | 829 | 67.8% |
| SYNONYM | 387 | 31.6% |
| DOUBTFUL | 7 | 0.6% |

- Of the **1,216** names GBIF resolves to a taxon (ACCEPTED or SYNONYM), **829 (68.2%) are still accepted** names and **387 (31.8%) are historical synonyms** of a currently accepted name.
- **Restricted to the 726 MW binomials GBIF matched at species rank** (the honest currency figure — genus-only tags always resolve accepted at genus rank): **377 (52.1%) accepted, 346 (47.9%) historical synonyms.** Nearly half of MW's identifiable binomials are superseded names (e.g. *Acacia arabica* → *Vachellia nilotica*).

## Match rank (many MW tags are genus-only)
| rank | species |
|---|--:|
| SPECIES | 726 |
| GENUS | 272 |
| KINGDOM | 164 |
| FAMILY | 51 |
| PHYLUM | 4 |
| CLASS | 4 |
| VARIETY | 2 |

## Match quality
| matchType | species |
|---|--:|
| EXACT | 701 |
| HIGHERRANK | 392 |
| FUZZY | 130 |

## Top families
| family | species |
|---|--:|
| Fabaceae | 142 |
| Poaceae | 55 |
| Apocynaceae | 43 |
| Malvaceae | 41 |
| Lamiaceae | 41 |
| Cucurbitaceae | 40 |
| Asteraceae | 39 |
| Rubiaceae | 26 |
| Euphorbiaceae | 25 |
| Zingiberaceae | 21 |
| Apiaceae | 20 |
| Arecaceae | 20 |
| Combretaceae | 19 |
| Convolvulaceae | 19 |
| Acanthaceae | 18 |

## Notes
- `/species/match` is the GBIF fuzzy-matching endpoint; `matchType` EXACT/FUZZY/HIGHERRANK/NONE records how each name resolved. Genus-only MW tags (e.g. *Sesamum*, *Abrus*) match at genus rank and are counted here as resolved at that rank.
- `accepted_name` is filled only when GBIF marks the MW name a SYNONYM; it is the GBIF `species` field of the accepted taxon.
- Reproduce: `python gbif_currency.py` (uses `species_currency_cache.json`; delete it to refetch from GBIF).
