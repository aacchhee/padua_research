"""J3 audit R4 (exploratory, preregistered in PREREG-J3-02): replace every analytic far leaf 'f' by a numerical
leaf '.' in the produce witness and run the pinned I25 check; report acceptance and the far/near margins on the
former f leaves with I25's own W, M, L. Evidence for a proposal only; no claim about unchecked degrees.
Usage: python3 -I -B r4_fleaves.py PREREG2.json SHA OUTDIR"""
import hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
p2, sha, outdir = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
assert hashlib.sha256(p2.read_bytes()).hexdigest() == sha
P = json.loads(p2.read_bytes()); P1 = json.loads(Path(P['base_prereg']).read_bytes())
REPO = Path(P1['repo_checker_dir'])
assert hashlib.sha256((REPO / 'check.py').read_bytes()).hexdigest() == P1['trusted_source_sha256']['check.py']
sys.dont_write_bytecode = True; sys.path.insert(0, str(REPO)); import check
outdir.mkdir(parents=True, exist_ok=False); out = {}
for n in P['degrees']:
    name = 'n%d-produce.json' % n; b = (Path(P1['data_dir']) / name).read_bytes()
    assert hashlib.sha256(b).hexdigest() == P1['inputs_sha256'][name]
    doc = json.loads(b); pre = doc['tree']['preorder']
    fl = [r for t, r in check.parse(doc['tree'], n) if t == 'f']
    doc['tree']['preorder'] = pre.replace('f', '.'); cache = {}
    try: r = check.check(doc, cache); rec = {'outcome': 'ACCEPT', 'M': r['M'], 'far_min_all': float(F(r['far_min'])), 'near_min_all': float(F(r['near_min']))}
    except Exception as e: out[n] = {'outcome': 'REJECT', 'reason': repr(e), 'f_leaves': [[str(x) for x in r] for r in fl]}; continue
    W = {k[2:]: v[1] for k, v in cache.items() if k[0] == 'S'}; L = cache[('S', n, F(0), F(0))][0]; M = F(r['M']); k = F(n, n + 1)
    per = []
    for box in fl:
        ws = [W[check.fold(*p)] for p in check.vertices(box)]
        qf = check.maximum(box, ws, M, k, 'far'); qn = check.maximum(box, ws, M, k, 'near')
        per.append({'box': [str(x) for x in box], 'far_margin': None if qf is None else float(L - qf), 'near_proxy_nonempty': qn is not None})
    rec['former_f_leaves'] = per; out[n] = rec
    print(json.dumps({'n': n, 'outcome': rec['outcome'], 'min_far_on_former_f': min(x['far_margin'] for x in per)}), flush=True)
(outdir / 'results.json').write_text(json.dumps(out, indent=1) + '\n')
