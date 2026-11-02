"""MEASURED cross-check of the 90-sample E-P float screen with own float cardinals."""
import json, sys
import numpy as np
sys.path.insert(0, '/tmp/claude-0/-home-user-padua-research/efec27fb-ede8-54e4-a9c8-12b8741cbbba/scratchpad/audit01/E')
import indep_padua as ip
ep = json.load(open('/home/user/padua_research/topics/padua-argmax-alln-20261101/outputs/gated/d3_ep_screen.json'))
lam = {}
def get(n, j):
    if (n, j) not in lam:
        inv = ip.verified_inverse(n)
        Rf = np.array(inv['R_float']); x = 1.0 if j == 0 else -1.0
        D = np.zeros((len(inv['nodes']), n + 1))
        for al, (p, q) in enumerate(inv['basis']):
            D[:, q] += Rf[al, :] * x ** p
        lam[n, j] = lambda th, D=D, n=n: np.abs(np.cos(np.arange(n + 1) * th) @ D.T).sum()
    return lam[n, j]
maxdev = 0; rev = []
from fractions import Fraction as F
for r in ep['samples']:
    n, j, k, kp, u = r['n'], r['j'], r['source'], r['target'], F(r['phase'])
    f = get(n, j); m = n + 1
    s = f(float(k + u) * np.pi / m); t = f(float(kp + u) * np.pi / m)
    maxdev = max(maxdev, abs(s - r['source_value']), abs(t - r['target_value']))
    if t - s < -1e-6: rev.append((n, j, k, kp, str(u), t - s))
print(json.dumps({'samples': len(ep['samples']), 'dev_reversal_count': ep['reversal_count'],
                  'own_reversal_count': len(rev), 'own_reversals': rev,
                  'max_abs_value_difference_vs_dev_screen': maxdev}, indent=1))
