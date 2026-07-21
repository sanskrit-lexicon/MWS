#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resolve <ls>ib.</ls> ("ibidem") citations to their antecedent source.

MW has 10,094 <ls>ib.</ls> citations = "in the same work just cited". They count
as unlinkable "meta" citations (part of the 22.3% scan-link ceiling), but most
point at a recoverable real source: the nearest preceding <ls> in reading order.
Resolving them reclassifies linkable citations and feeds paper P3.

Algorithm (deterministic):
  - Build one GLOBAL stream of <ls> citations in document order, tagging each with
    the headword cluster (a maximal run of consecutive same-<k1> records) it sits in.
  - Each ib. resolves to the nearest preceding <ls> in that stream; if that is
    itself ib., chain back to the first non-ib. citation (terminal). Resolution
    therefore CAN cross a headword boundary — flagged 'crossed-headword' (lower
    confidence) vs 'same-cluster' (high confidence) in the output. (Earlier drafts
    were cluster-scoped; the code now walks the whole document — CODE_REVIEW #8.)
  - "Recovered as linkable" = terminal is a real text source, i.e. NOT one of the
    meta/relative markers in META below.
  - Unresolvable = no preceding <ls> earlier in the dictionary at all (≈never).

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
META  = {'L.', 'ib.', 'MW.', 'W.', 'Cat.', 'id.'}   # non-text markers; aligned with
                                                    # link_candidates (CODE_REVIEW #15 — ideally one shared constant)
def is_ib(s):   return s.strip() == 'ib.'
def base(s):    # strip locator to bare siglum for kind reporting
    return re.split(r'[ ,]', s.strip(), maxsplit=1)[0]   # CODE_REVIEW #12: keyword maxsplit

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
S.append('> **These figures are *resolvable*, not *verified*.** The walk mechanically')
S.append('> finds an antecedent; whether it is the source MW *meant* has not been checked')
S.append('> against the print. No ground-truth sample has been hand-validated — that is the')
S.append('> required next step before any paper or write-back.\n')
S.append(f'- Total `<ls>ib.</ls>` citations: **{total_ib:,}**')
S.append(f'- **Same-cluster resolutions (high confidence — antecedent in the same headword): '
         f'{same_cluster:,} ({pct(same_cluster):.1f}%)** — the defensible core.')
S.append(f'- Crossed-headword resolutions (lower confidence; compound runs chaining `ib.` to a')
S.append(f'  shared source): {crossed:,} ({pct(crossed):.1f}%) — need a spot-check before use.')
S.append(f'- Combined, resolved to a real text source (mechanical upper bound): '
         f'{resolved_real:,} ({pct(resolved_real):.1f}%); to a meta marker {resolved_meta:,} '
         f'({pct(resolved_meta):.1f}%); unresolvable {unresolvable:,}.\n')
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
