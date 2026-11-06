"""Auditor: measured n3 census size via own enumeration + Burnside (no rank)."""
import math, json, sys, time, numpy as np
sys.path.insert(0, __file__.rsplit('/',1)[0])
from aud_groups import groups, points
n, N = 3, 20; t0 = time.time(); tot = 0; ret = 0; strata = 0; prime = 0; bymask = [0]*8
for m in range(N, 8*N+1):
    isprime = all(m % d for d in range(2, int(m**.5)+1))
    for g in groups(m):
        tot += 1
        P = points(g); mj = [len(np.unique(P[:, j])) for j in range(3)]
        if min(mj) <= n or max(mj) > 2*N: continue
        ret += 1
        if isprime: prime += 1; continue
        tau = np.stack([(2*mj[j]*P[:, j]//m) % mj[j] for j in range(3)], axis=1)
        for mask in range(8):
            J = [j for j in range(3) if mask >> j & 1]
            if J:
                img = len(np.unique(tau[:, J] @ np.array([100**i for i in range(len(J))])))
                s = math.prod(mj[j] for j in J)//img
            else: s = 1
            strata += s; bymask[mask] += s
print(json.dumps({'n3_groups': tot, 'retained': ret, 'retained_prime': prime, 'quotient_strata_nonprime': strata, 'by_mask': bymask, 'secs': time.time()-t0}))
