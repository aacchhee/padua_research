"""L5 R03 diagnostic: does the Givens run itself detect near non-unisolvent prefixes?  After inserting point i (1-based count K=i+1),
record the 'new pivot' h_K = |H_{V(K)}[K, p(K)]| (the pivot that will be used for monomial K by later rotations) of the scheme rule,
and compare with the exact sigma_min of the K x K prefix block of the orthogonal Chebyshev matrix (prefix.py).
usage: python3 -I diag_pivot_vs_sigma.py n [order ...]   (orders: given sortx rand1 rand2 rand3 gepp rpiv1)"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5_lib as L, prefix as PF
F = L.F

def run(x, y, v):
    M = len(x); ms, prim, alt = F.parents(M)
    Hx = np.zeros((M, M)); Hy = np.zeros((M, M)); w = np.zeros(M)
    w[0] = v[0]; Hx[0, 0] = x[0]; Hy[0, 0] = y[0]
    piv = np.zeros(M); piv[0] = abs(w[0]); pmin = np.zeros(M); pmin[0] = abs(w[0])
    for i in range(1, M):
        w[i] = v[i]; Hx[i, i] = x[i]; Hy[i, i] = y[i]; n = i + 1
        for j in range(i):
            if j == 0: a, b = w[0], w[i]
            else:
                p, var = prim[j]; H = Hx if var == 0 else Hy; a, b = H[j, p], H[i, p]
            if b == 0.0: continue
            r = np.hypot(a, b); c, s = a / r, b / r
            for A in (Hx, Hy):
                rj = A[j, :n].copy(); ri = A[i, :n].copy(); A[j, :n] = c * rj + s * ri; A[i, :n] = -s * rj + c * ri
                cj = A[:n, j].copy(); ci = A[:n, i].copy(); A[:n, j] = c * cj + s * ci; A[:n, i] = -s * cj + c * ci
            wj, wi = w[j], w[i]; w[j] = c * wj + s * wi; w[i] = -s * wj + c * wi
        p, var = prim[i]; H = Hx if var == 0 else Hy
        piv[i] = abs(H[i, p])        # new pivot of monomial i (0-based) after point i inserted
        mp = abs(w[0])               # smallest pivot over all monomials 0..i (monomial 0 pivot is |w_0| = norm of v prefix)
        for jj in range(1, i + 1):
            pp, vv = prim[jj]; HH = Hx if vv == 0 else Hy; mp = min(mp, abs(HH[jj, pp]))
        pmin[i] = mp
    return piv, pmin

if __name__ == "__main__":
    n = int(sys.argv[1]); orders = sys.argv[2:] or ["given", "rand1", "rand2", "gepp", "rpiv1"]
    P, wc, Qc = PF.padua_orthogonal_basis(n); M = len(P)
    rng = np.random.default_rng(5)
    od = {"given": np.arange(M), "sortx": np.lexsort((P[:, 1], P[:, 0])), "rand1": np.random.default_rng(10 * n + 1).permutation(M),
          "rand2": np.random.default_rng(10 * n + 2).permutation(M), "rand3": np.random.default_rng(10 * n + 3).permutation(M),
          "gepp": PF.gepp_order(Qc), "rpiv1": PF.threshold_pivot_order(Qc, 0.1, np.random.default_rng(20 * n + 1))}
    for lab in orders:
        perm = od[lab]
        piv0, piv = run(P[perm, 0].copy(), P[perm, 1].copy(), np.sqrt(wc[perm]))
        res = PF.prefix_scan(Qc[perm], use_comb=None, exhaustive=(M <= 140))
        sig = res["hi"] if M > 140 else res["lo"]
        K = np.arange(1, M + 1)
        # pivot for monomial K-1 (0-based index K-1) after K points: piv[K-1]
        ok = K >= 4
        lp, ls = np.log10(np.maximum(piv[ok], 1e-20)), np.log10(np.maximum(sig[ok], 1e-20))
        from scipy import stats
        print(f"n={n} {lab:6s} Spearman(log min-pivot, log sigma_min)={stats.spearmanr(lp, ls)[0]:.3f}  "
              f"singular prefixes: {int((sig<1e-11).sum())}; of those min-pivot<1e-10: {int(((sig<1e-11)&(piv<1e-10)).sum())}; "
              f"unisolvent prefixes with min-pivot<1e-10: {int(((sig>=1e-11)&(piv<1e-10)).sum())}; min over j<K of pivot among sigma>=1e-8: {piv[(sig>=1e-8)&(K>=2)].min():.1e}", flush=True)
