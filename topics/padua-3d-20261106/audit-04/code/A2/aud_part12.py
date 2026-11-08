"""Part 1: exact counterexample search for the even-degree half-shift bound at n=2,4.
Part 2: own exact cubic census (monomial-DCT reduction, sympy DomainMatrix rank/det)."""
import sys, math, json, time, itertools as it
from collections import Counter
import numpy as np
sys.path.insert(0, sys.argv[1])
from aud_common import *

def ceiling(n, z):
    N = math.comb(n + 3, 3); f = N % 2
    odd = [zj % 2 for zj in z]
    D = sum((-1) ** sum(a for a, o in zip(al, odd) if o) for al in total_modes(n))
    return N - abs(D - f) // 2, D, f

def numeric_check_reduction(n, z):
    N = math.comb(n + 3, 3); M = 2 * N
    th = (2 * np.arange(N) + 1) * np.pi / M
    B = np.cos(np.outer(th, np.arange(N)))
    C, modes = mono_dct_matrix(n, z)
    X = np.cos(np.outer(th, z))
    V = np.array([[np.prod(X[k] ** np.array(al)) for al in modes] for k in range(N)])
    Dg = np.array([2.0 ** (sum(al) + 3) for al in modes])
    return float(np.max(np.abs(V - B @ np.array(C, float) / Dg)))

def modular_actual_rank(n, z, p, w):
    N = math.comb(n + 3, 3); M = 2 * N
    L, nodes = fold_nodes(z, z, 2 * M, M)
    assert len(nodes) == N and L == 2 * M
    inv2 = pow(2, -1, p)
    X = [[(pow(w, v, p) + pow(w, (-v) % L, p)) * inv2 % p for v in row] for row in nodes]
    A = [[math.prod(pow(x, a, p) for x, a in zip(row, al)) % p for al in total_modes(n)] for row in X]
    return modrank_det(A, p)[0]

out = {}
t0 = time.time()
# ---- Part 1
for n in (2, 4):
    N = math.comb(n + 3, 3); M = 2 * N
    p, w = split_prime(2 * M, 3_000_000_000)
    hist = Counter(); viol = 0; attain = 0; maxerr = 0.0; tested = 0
    for b in range(0, M + 1):
        for c in range(b, M + 1):
            z = (1, b, c)
            L, nodes = fold_nodes(z, z, 2 * M, M)
            assert len(nodes) == N, (n, z)
            C, _ = mono_dct_matrix(n, z)
            r = exact_rank(C)
            rm = modular_actual_rank(n, z, p, w)
            cap, D, f = ceiling(n, z)
            assert rm <= r
            viol += r > cap
            attain += r == cap
            hist[(sum(x % 2 for x in z), r)] += 1
            tested += 1
            if tested % 400 == 1:
                maxerr = max(maxerr, numeric_check_reduction(n, z))
    out['part1_n%d' % n] = {'N': N, 'M': M, 'prime': p, 'omega': w, 'tested_b<=c_in_[0,M]': tested,
        'violations_rank_gt_ceiling': viol, 'attain_ceiling': attain, 'max_rank': max(r for (_, r) in hist),
        'hist_t_rank': {'%d:%d' % k: v for k, v in sorted(hist.items())}, 'reduction_numeric_maxerr': maxerr}
    print(json.dumps(out['part1_n%d' % n]), flush=True)
# ---- Part 2
n, N, M = 3, 20, 40
p, w = split_prime(80, 2_500_000_000)
hist = Counter(); surv = []; dets = {}; agree = 0
K = sum(sum(a > 0 for a in al) for al in total_modes(n))
for b, c in it.combinations(range(1, M), 2):
    z = (1, b, c)
    C, _ = mono_dct_matrix(n, z)
    r = exact_rank(C)
    rm = modular_actual_rank(n, z, p, w)
    agree += rm == r
    hist[r] += 1
    if r == N:
        d = exact_det(C)
        surv.append(list(z)); dets[str(z)] = d
absd = {abs(d) for d in dets.values()}
out['part2'] = {'pairs': sum(hist.values()), 'hist': dict(sorted(hist.items())), 'survivors': surv,
    'abs_det_mono_dct': sorted(absd), 'K': K, 'implied_abs_det_cheb_C': [x / 2 ** K for x in absd],
    'log2': [math.log2(x / 2 ** K) for x in absd], 'modular_equal_exact': agree, 'prime': p, 'omega': w,
    'max_numeric_reduction_err_on_survivors': max(numeric_check_reduction(3, s) for s in surv)}
print(json.dumps(out['part2']), flush=True)
out['seconds'] = round(time.time() - t0, 2)
json.dump(out, open(sys.argv[2], 'w'), indent=1)
print('seconds', out['seconds'])
