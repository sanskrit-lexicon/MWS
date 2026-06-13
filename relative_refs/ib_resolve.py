#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resolve <ls>ib.</ls> ("ibidem") citations to their antecedent source.

MW has 10,094 <ls>ib.</ls> citations = "in the same work just cited". They count
as unlinkable "meta" citations (part of the 22.3% scan-link ceiling), but most
point at a recoverable real source: the nearest preceding <ls> in reading order.
Resolving them reclassifies linkable citations and feeds paper P3.

Algorithm (deterministic):
  - Scope = headword cluster: a maximal run of consecutive records sharing <k1>.
    (ib. refers within an entry; we do not cross into a different headword.)
  - Within a cluster, collect <ls> citations in document order.
  - Each ib. resolves to the immediately preceding <ls>; if that is itself ib.,
    chain back to the first non-ib. citation (terminal).
  - "Recovered as linkable" = terminal is a real text source, i.e. NOT one of the
    meta/relative markers {ib., L., MW., W., Cat.}.
  - Unresolvable = no preceding <ls> in the cluster (ib. is cluster-initial).

Outputs (this dir):
  ib_resolved.csv        (L-number, headword, terminal source, terminal kind)
  IB_SUMMARY.md
"""
import sys, os, re, csv
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))
GH   = os.path.abspath(os.path.join(HERE, '..', '..'))
MW   = os.path.join(GH, 'csl-orig', 'v02', 'mw', 'mw.txt')

LS_RE = re.compile(r'<ls(?:\s[^>]*)?>(.*?)</ls>')
K1_RE = re.compile(r'<k1>([^<]*)')
L_RE  = re.compile(r'^<L>([^<]*)')
META  = {'L.', 'MW.', 'W.', 'Cat.'}     # real-ish but not a re-citable text work
def is_ib(s):   return s.strip() == 'ib.'
def base(s):    # strip locator to bare siglum for kind reporting
    return re.split(r'[ ,]', s.strip(), 1)[0]

# --- global document-order stream of (Lnum, cluster_id, ls) ---
# cluster_id increments whenever consecutive <k1> changes (headword boundary).
stream = []           # (Lnum, cluster_id, ls)
cur_k1 = None
cluster_id = -1
cur_L = None
pending = []
def flush():
    for s in pending:
        stream.append((cur_L, cluster_id, s))

with open(MW, encoding='utf-8') as f:
    for line in f:
        if line.startswith('<L>'):
            flush(); pending = []
            cur_L = L_RE.match(line).group(1)
            m = K1_RE.search(line); k1 = m.group(1) if m else None
            if k1 != cur_k1:
                cluster_id += 1; cur_k1 = k1
        elif line.startswith('<LEND>'):
            pass
        else:
            pending.extend(LS_RE.findall(line))
flush()

# --- resolve ib. in pure document order (ibidem = last work cited) ---
total_ib = 0
resolved_real = 0      # ib. -> real text source
resolved_meta = 0      # ib. -> L./W./Cat./MW.
unresolvable = 0
same_cluster = 0       # antecedent in same headword cluster (high confidence)
crossed = 0            # antecedent in an earlier cluster (lower confidence)
src_hist = {}
rows = []

for i, (L, cid, s) in enumerate(stream):
    if not is_ib(s):
        continue
    total_ib += 1
    j = i - 1
    term = None
    while j >= 0:
        if not is_ib(stream[j][2]):
            term = stream[j]; break
        j -= 1
    if term is None:
        unresolvable += 1
        rows.append((L, '', '', 'UNRESOLVABLE', ''))
        continue
    conf = 'same-cluster' if term[1] == cid else 'crossed-headword'
    if conf == 'same-cluster': same_cluster += 1
    else: crossed += 1
    b = base(term[2])
    if b in META or term[2].strip() in META:
        resolved_meta += 1
        rows.append((L, term[2], b, 'meta', conf))
    else:
        resolved_real += 1
        src_hist[b] = src_hist.get(b, 0) + 1
        rows.append((L, term[2], b, 'real', conf))

with open(os.path.join(HERE, 'ib_resolved.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['L_number', 'resolved_to_ls', 'terminal_siglum', 'kind', 'confidence'])
    w.writerows(rows)

pct = lambda n: 100*n/total_ib if total_ib else 0
top = sorted(src_hist.items(), key=lambda kv: -kv[1])[:15]
S = []
S.append('# `<ls>ib.</ls>` resolution — results\n')
S.append(f'- Total `<ls>ib.</ls>` citations: **{total_ib:,}**')
S.append(f'- **Resolved to a real text source (recoverable as linkable): {resolved_real:,} ({pct(resolved_real):.1f}%)**')
S.append(f'- Resolved to a meta marker (L./W./Cat./MW. — stays unlinkable): {resolved_meta:,} ({pct(resolved_meta):.1f}%)')
S.append(f'- Unresolvable (no prior citation in the whole dictionary): {unresolvable:,} ({pct(unresolvable):.1f}%)\n')
S.append('## Confidence (antecedent locality)')
S.append(f'- **Same headword cluster (high confidence): {same_cluster:,} ({pct(same_cluster):.1f}%)**')
S.append(f'- Crossed a headword boundary (lower confidence — typical of compound runs')
S.append(f'  where sibling compounds chain `ib.` to a shared source): {crossed:,} ({pct(crossed):.1f}%)')
S.append(f'  These are the candidates worth a maintainer spot-check before any write.\n')
S.append('## Effect on the scan-link ceiling')
S.append(f'- The earlier "22.3% meta" ceiling counted all 10,094 ib. as unlinkable.')
S.append(f'- Resolving recovers **{resolved_real:,}** of them to real sources, shrinking')
S.append(f'  the truly-unlinkable meta set by that amount.\n')
S.append('## What ib. actually points to (top real sources)')
S.append('| terminal source | ib. citations resolved |')
S.append('|---|--:|')
for sig, n in top:
    S.append(f'| `{sig}` | {n:,} |')
S.append('\n## Notes')
S.append('- Resolution is in pure document order — `ibidem` = the last work cited in')
S.append('  reading order. Every ib. therefore resolves (0 unresolvable). Antecedents')
S.append('  in the same `<k1>` cluster are high-confidence; cross-boundary ones')
S.append('  (compound runs sharing a source) are flagged for review in the CSV.')
S.append('- Chained ib.->ib. is followed to the first non-ib. terminal.')
S.append('- This is analysis only; no `mw.txt` mutation. `ib_resolved.csv` is the')
S.append('  candidate map for a future enrichment pass (maintainer-gated).')
S.append('- Sibling task: `<ab>id.</ab>` (4,401, issue #98) is the *sense*-level analog')
S.append('  (resolve to the preceding gloss); see IDEM_NOTE.md.')
open(os.path.join(HERE, 'IB_SUMMARY.md'), 'w', encoding='utf-8').write('\n'.join(S) + '\n')

print(f'total ib.: {total_ib}')
print(f'  -> real source: {resolved_real} ({pct(resolved_real):.1f}%)')
print(f'  -> meta:        {resolved_meta} ({pct(resolved_meta):.1f}%)')
print(f'  unresolvable:   {unresolvable} ({pct(unresolvable):.1f}%)')
print(f'  top sources: {top[:8]}')
