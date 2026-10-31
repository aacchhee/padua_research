import numpy as np, sys
sys.path.insert(0, '.')
from butterfly_probe import cheb_vander, morton_order, numrank, butterfly_ranks
rng = np.random.default_rng(1)
for n, M in [(30, 3000), (30, 8000)]:
    N = (n+1)*(n+2)//2
    P = rng.uniform(-1, 1, size=(M, 2)); P = P[morton_order(P, 6)]
    V = cheb_vander(P[:,0], P[:,1], n)
    Q, R = np.linalg.qr(V); Q, R = np.linalg.qr(Q)
    print(f"\nrandom uniform M={M}, N={N} (M/N={M/N:.1f}), L=5")
    for l, rbs, cbs, mx in butterfly_ranks(Q, 5):
        print(f"  level {l}: rows/block {rbs}, cols/block {cbs}, max rank {mx} (min dim {min(rbs,cbs)})")
    h = M//2
    print("  HSS top-level off-diag rank:", numrank(Q[:h, h:]), "of", min(h, N-h) if N-h>0 else N)
