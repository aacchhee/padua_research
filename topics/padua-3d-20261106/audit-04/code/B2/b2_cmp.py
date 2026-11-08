"""Auditor B2: compare rerun receipts with committed receipts: node hashes and fresh-refined norms."""
import json, sys
a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
def rows(d):
    return {(r[0], r[1]): dict(zip(d['row_columns'], r)) for r in d['rows']}
ra, rb = rows(a), rows(b)
same_hash = same_norm = 0; diffs = []
for k, r in rb.items():
    q = ra.get(k)
    if q is None: diffs.append(('missing', k)); continue
    if q['node_sha256'] == r['node_sha256']: same_hash += 1
    else: diffs.append(('hash', k))
    if q.get('norms') == r.get('norms') and q.get('errors') == r.get('errors') and q.get('noise') == r.get('noise'): same_norm += 1
    else: diffs.append(('norm/err/noise', k, q.get('norms'), r.get('norms')))
loc = {n: r['norms'][5] for (n, f), r in rb.items() if f == 'localdet'}
jn = {n: r['norms'][5] for (n, f), r in rb.items() if f == 'joint_norm'}
print(json.dumps({'rows_rerun': len(rb), 'same_node_hash': same_hash, 'same_norms_errors_noise': same_norm, 'diffs': diffs[:6],
  'fresh_refined_localdet_vs_joint': {n: [loc[n], jn[n], jn[n]/loc[n]] for n in sorted(jn)},
  'opt': [(o['n'], o['termination']['status'], o['termination']['iterations'], o['fallback'], round(o['extra_cpu'], 3)) for o in b['optimizations']]}, indent=0))
