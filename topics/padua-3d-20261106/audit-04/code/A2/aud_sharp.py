"""NOTE check: is the t=2 ceiling N-|D2-f|/2 attained at n6/n8? modular rank is a lower bound."""
import sys, math, random, json
import numpy as np
sys.path.insert(0, sys.argv[1])
from aud_common import fold_nodes, split_prime, total_modes
def np_rank(A, p):
    A = np.array(A, dtype=np.int64) % p; r = 0; nr, nc = A.shape
    for c in range(nc):
        nz = np.flatnonzero(A[r:, c])
        if not len(nz): continue
        k = r + int(nz[0]); A[[r, k]] = A[[k, r]]
        A[r] = A[r] * pow(int(A[r, c]), -1, p) % p
        A[r + 1:] = (A[r + 1:] - A[r + 1:, c, None] * A[r]) % p
        r += 1
        if r == nr: break
    return r
res = {}
for n, ceil_ in ((6, 82), (8, 163)):
    N = math.comb(n + 3, 3); M = 2 * N
    p, w = split_prime(2 * M, 1_000_000_000)
    assert p < 3_000_000_000
    rng = random.Random(20261108 + n); best = 0; tried = 0
    while tried < 40 and best < ceil_:
        b = rng.randrange(1, M); c = rng.randrange(1, M)
        if (b % 2) + (c % 2) != 1 or b == c: continue
        z = (1, b, c); L, nodes = fold_nodes(z, z, 2 * M, M); assert len(nodes) == N
        i2 = pow(2, -1, p)
        X = [[(pow(w, v, p) + pow(w, (-v) % L, p)) * i2 % p for v in r] for r in nodes]
        A = [[math.prod(pow(x, e, p) for x, e in zip(row, al)) % p for al in total_modes(n)] for row in X]
        rk = np_rank(A, p); tried += 1
        if rk > ceil_: raise SystemExit('COUNTEREXAMPLE %s %s' % (n, z))
        if rk > best: best, bz = rk, z
    res[n] = {'prime': p, 'tried': tried, 'best_modular_rank': best, 'at': bz, 'ceiling': ceil_}
    print(json.dumps(res[n]), flush=True)
