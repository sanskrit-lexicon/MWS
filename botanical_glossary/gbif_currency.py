#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GBIF nomenclatural-currency pass for the MW botanical crosswalk (A45 §3.5/§4.6).

MW's binomials are 19th-century Linnaean names; many are now synonyms of accepted
names (e.g. Hedysarum gangeticum -> Pleurolobus gangeticus). This resolves every
canonical species in species_to_sanskrit.json against the GBIF Backbone Taxonomy
(the /species/match endpoint, which folds POWO + IPNI + Catalogue of Life) and
records, per species: the GBIF taxonomic status, the accepted name where the MW
name is a synonym, the family, and the match quality.

Outputs (this dir):
  species_currency.csv          one row per canonical species with GBIF resolution
  species_currency_cache.json   raw GBIF responses (resume-safe; delete to refetch)
  CURRENCY_SUMMARY.md           accepted-vs-synonym split + family/quality tallies

No API key required. Polite ~20 req/s; cached so reruns are free.
"""
import sys, os, json, csv, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
SPECIES = os.path.join(HERE, 'species_to_sanskrit.json')
CACHE = os.path.join(HERE, 'species_currency_cache.json')
API = 'https://api.gbif.org/v1/species/match'

def load_cache():
    if os.path.exists(CACHE):
        with open(CACHE, encoding='utf-8') as f:
            return json.load(f)
    return {}

def gbif_match(name):
    url = API + '?' + urllib.parse.urlencode({'name': name, 'kingdom': 'Plantae'})
    req = urllib.request.Request(url, headers={'User-Agent': 'csl-MWS-botanical/1.0 (github.com/sanskrit-lexicon/MWS)'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.load(r)
        except Exception as e:
            if attempt == 2:
                return {'_error': str(e)}
            time.sleep(0.5 + attempt)

def main():
    with open(SPECIES, encoding='utf-8') as f:
        species = sorted(json.load(f).keys())
    cache = load_cache()
    n = len(species)
    todo = [sp for sp in species if sp not in cache]
    print(f'{len(cache)}/{n} already cached; fetching {len(todo)} with a thread pool...', flush=True)
    done = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(gbif_match, sp): sp for sp in todo}
        for fut in as_completed(futures):
            sp = futures[fut]
            try:
                cache[sp] = fut.result()
            except Exception as e:
                cache[sp] = {'_error': str(e)}
            done += 1
            if done % 50 == 0:
                with open(CACHE, 'w', encoding='utf-8') as f:
                    json.dump(cache, f, ensure_ascii=False)
                print(f'  {len(cache)}/{n} cached...', flush=True)
    with open(CACHE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False)

    rows = []
    for sp in species:
        m = cache[sp]
        status = m.get('status', '') or ('NO_MATCH' if m.get('matchType') == 'NONE' else '')
        if '_error' in m:
            status = 'FETCH_ERROR'
        accepted = ''
        # For a synonym GBIF returns the accepted species in the `species` field
        # (and canonicalName is the matched synonym); acceptedUsageKey points at it.
        if status == 'SYNONYM':
            accepted = m.get('species', '') or ''
        rows.append({
            'species_canonical': sp,
            'gbif_matched_name': m.get('canonicalName', ''),
            'rank': m.get('rank', ''),
            'status': status,
            'accepted_name': accepted,
            'family': m.get('family', ''),
            'match_type': m.get('matchType', ''),
            'confidence': m.get('confidence', ''),
        })

    with open(os.path.join(HERE, 'species_currency.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # --- summary ---
    from collections import Counter
    st = Counter(r['status'] for r in rows)
    mt = Counter(r['match_type'] for r in rows)
    rk = Counter(r['rank'] for r in rows)
    fam = Counter(r['family'] for r in rows if r['family'])
    total = len(rows)
    accepted = st.get('ACCEPTED', 0)
    synonym = st.get('SYNONYM', 0)
    resolved = accepted + synonym

    S = []
    S.append('# MW botanical crosswalk — GBIF nomenclatural-currency pass\n')
    S.append(f'Resolved **{total:,}** canonical species against the GBIF Backbone Taxonomy '
             f'(`/species/match`, kingdom Plantae; folds POWO + IPNI + Catalogue of Life).\n')
    S.append('## Taxonomic status of MW\'s names')
    S.append('| GBIF status | species | % of all |')
    S.append('|---|--:|--:|')
    for k, v in st.most_common():
        label = k or '(blank)'
        S.append(f'| {label} | {v:,} | {100*v/total:.1f}% |')
    S.append('')
    if resolved:
        S.append(f'- Of the **{resolved:,}** names GBIF resolves to a taxon (ACCEPTED or SYNONYM), '
                 f'**{accepted:,} ({100*accepted/resolved:.1f}%) are still accepted** names and '
                 f'**{synonym:,} ({100*synonym/resolved:.1f}%) are historical synonyms** of a '
                 f'currently accepted name.')
    # The honest currency figure is at SPECIES rank: genus-only MW tags always resolve
    # "accepted" at genus rank and inflate the accepted share, so restrict to binomials
    # that GBIF matched to a species.
    sp_rows = [r for r in rows if r['rank'] == 'SPECIES']
    sp_acc = sum(1 for r in sp_rows if r['status'] == 'ACCEPTED')
    sp_syn = sum(1 for r in sp_rows if r['status'] == 'SYNONYM')
    if sp_acc + sp_syn:
        S.append(f'- **Restricted to the {len(sp_rows):,} MW binomials GBIF matched at species '
                 f'rank** (the honest currency figure — genus-only tags always resolve accepted at '
                 f'genus rank): **{sp_acc:,} ({100*sp_acc/(sp_acc+sp_syn):.1f}%) accepted, '
                 f'{sp_syn:,} ({100*sp_syn/(sp_acc+sp_syn):.1f}%) historical synonyms.** Nearly half '
                 f'of MW\'s identifiable binomials are superseded names (e.g. *Acacia arabica* → '
                 f'*Vachellia nilotica*).')
    S.append('')
    S.append('## Match rank (many MW tags are genus-only)')
    S.append('| rank | species |')
    S.append('|---|--:|')
    for k, v in rk.most_common():
        S.append(f'| {k or "(none)"} | {v:,} |')
    S.append('')
    S.append('## Match quality')
    S.append('| matchType | species |')
    S.append('|---|--:|')
    for k, v in mt.most_common():
        S.append(f'| {k or "(none)"} | {v:,} |')
    S.append('')
    S.append('## Top families')
    S.append('| family | species |')
    S.append('|---|--:|')
    for k, v in fam.most_common(15):
        S.append(f'| {k} | {v:,} |')
    S.append('')
    S.append('## Notes')
    S.append('- `/species/match` is the GBIF fuzzy-matching endpoint; `matchType` EXACT/FUZZY/'
             'HIGHERRANK/NONE records how each name resolved. Genus-only MW tags (e.g. *Sesamum*, '
             '*Abrus*) match at genus rank and are counted here as resolved at that rank.')
    S.append('- `accepted_name` is filled only when GBIF marks the MW name a SYNONYM; it is the '
             'GBIF `species` field of the accepted taxon.')
    S.append('- Reproduce: `python gbif_currency.py` (uses `species_currency_cache.json`; delete '
             'it to refetch from GBIF).')
    open(os.path.join(HERE, 'CURRENCY_SUMMARY.md'), 'w', encoding='utf-8').write('\n'.join(S) + '\n')

    print(f'\nspecies resolved: {total}')
    print(f'ACCEPTED {accepted} | SYNONYM {synonym} | other {total-accepted-synonym}')
    if resolved:
        print(f'of resolved: {100*accepted/resolved:.1f}% accepted, {100*synonym/resolved:.1f}% synonym')

if __name__ == '__main__':
    main()
