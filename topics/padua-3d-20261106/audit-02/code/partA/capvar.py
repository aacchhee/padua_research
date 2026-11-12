import math, sys, json
import indep_t1_points as M
orig = math.comb
def run_cap(n, cap):
    # monkeypatch cap by temporarily redefining N-based cap: reimplement call with explicit cap
    src = M.run.__code__
    N = math.comb(n + 3, 3)
    M_cap = cap
    import itertools, numpy as np
    codes = [S for S in M.subspaces() if not any((1 << j) in S for j in range(3))]
    tc = 0
    for S in codes:
        Bb = M.basis(S); k = len(Bb)
        active = [j for j in range(3) if any(v >> j & 1 for v in S)]
        inactive = [j for j in range(3) if j not in active]
        for m in itertools.product(range(1, cap + 1), repeat=3):
            if any(m[j] % 2 for j in active): continue
            if m[0]*m[1]*m[2] // (1 << k) > 8 * N: continue
            I = np.indices(m).reshape(3, -1).astype(np.int64)
            for synd in itertools.product((0, 1), repeat=k):
                mask = np.ones(I.shape[1], dtype=bool)
                for b, s in zip(Bb, synd):
                    mask &= (sum(I[j] for j in range(3) if b >> j & 1) % 2 == s)
                J = I[:, mask]
                for ph in itertools.product((0, 1), repeat=len(inactive)):
                    eps = [0, 0, 0]
                    for j, e in zip(inactive, ph): eps[j] = e
                    K = [np.minimum((2*J[j]+eps[j]) % (2*m[j]), 2*m[j]-(2*J[j]+eps[j]) % (2*m[j])) for j in range(3)]
                    code = (K[0]*(8*cap+1)+K[1])*(8*cap+1)+K[2]
                    if len(np.unique(code)) == N: tc += 1
    return tc
print("cap12:", [run_cap(n, 12) for n in range(2, 7)])
print("n=2 cap 2N+12=32:", run_cap(2, 32), " n=3 cap 2N+8=48:", run_cap(3, 48))
