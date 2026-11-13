import itertools as it, json, sys, numpy as np
sys.path.insert(0, __file__.rsplit('/',1)[0])
from aud_exact import H_from_upper_hnf, nodes
from aud_misc import lam
cert = json.load(open(sys.argv[1]))
res = {}
for q in (21, 41):
    g = np.cos(np.linspace(0, np.pi, q)); mesh = np.array(list(it.product(g, repeat=3)))
    vals = {}
    for h in [r['hnf'] for r in cert['nonprime_survivors']] + cert['prime_survivors_HNF']:
        m, pts = H_from_upper_hnf(h); nd = nodes(m, pts)
        X = np.cos(2*np.pi*np.array(nd)/m)
        vals[str(h)] = lam(X, 2, mesh)[0]
    v16 = [vals[str(r['hnf'])] for r in cert['nonprime_survivors']]
    v19 = [vals[str(h)] for h in cert['prime_survivors_HNF']]
    res[q] = {'order16': sorted(set(np.round(v16, 9))), 'order19_min': min(v19), 'order19_max': max(v19), 'order19_distinct': sorted(set(np.round(v19, 9)))}
m, pts = H_from_upper_hnf([1,4,4,1,1,0]); res['order16_nodes'] = [list(map(float, np.round(np.cos(2*np.pi*np.array(q)/16), 12))) for q in nodes(16, pts)]
print(json.dumps(res, indent=0, default=float))
