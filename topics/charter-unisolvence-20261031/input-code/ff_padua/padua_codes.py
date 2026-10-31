"""Evaluation codes on finite-field Padua sets ('Padua codes'): C_k = {(f(A))_{A in Pad_n} : f in P_k}.
Length N = dim P_n, dimension dim P_k. Footprint (Gröbner) bound: the Padua ideal has an H-basis of degree
n+1 whose leading forms are all monomials of degree n+1, so the footprint is P_n and
    d(C_k) >= dim P_{n-k}  (same bound as for triangular-grid / lower-set codes).
Brute force minimum distance for small q; compare with the footprint bound and Singleton.
Dual: by discrete orthogonality, C_k^perp = W * span{T_aT_b : k < a+b <= n} (weights W, explicit).
Run: python3 -I padua_codes.py
"""
import sys, os, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from padua_ff import PaduaFF, basis_index
from ffield import rank_mod_p, matmul_mod, transpose

def min_distance(G, q):
    """G: dim x N generator matrix (numpy int). Enumerate projective message vectors."""
    k, N = G.shape; best = N
    G = G.astype(np.int64)
    # messages with first nonzero entry = 1
    for lead in range(k):
        rest = k - lead - 1
        if rest == 0:
            w = np.count_nonzero(G[lead] % q); best = min(best, w); continue
        tail = np.array(list(itertools.product(range(q), repeat=rest)), dtype=np.int64)
        for chunk in range(0, len(tail), 200000):
            T = tail[chunk:chunk + 200000]
            C = (G[lead][None, :] + T @ G[lead + 1:]) % q
            best = min(best, int(np.count_nonzero(C, axis=1).min()))
    return best

def dimP(m): return (m + 1) * (m + 2) // 2 if m >= 0 else 0

if __name__ == '__main__':
    for q, n in [(7, 3), (11, 5), (13, 6), (17, 8), (5, 2), (31, 4)]:
        P = PaduaFF(n, q); V = P.vandermonde_cheb(); N = len(V)
        for k in range(0, n):
            K = dimP(k)
            if q ** (K - 1) > 3e6: break
            G = np.array([[V[i][s] for i in range(N)] for s in range(K)])   # first K basis elems = P_k
            d = min_distance(G, q)
            print(f"q={q:2d} n={n} [N={N}, K={K}, d={d}]  footprint bound {dimP(n-k)}  Singleton {N-K+1}")
        # dual check for k = n-1
        k = n - 1; K = dimP(k)
        Gk = [[V[i][s] for i in range(N)] for s in range(K)]
        Hd = [[P.w[i] * V[i][s] % q for i in range(N)] for s in range(K, N)]
        ok = all(v == 0 for row in matmul_mod(Gk, transpose(Hd), q) for v in row)
        print(f"   dual of C_{k}: W*span{{T_aT_b: a+b={n}}} orthogonal to C_{k}: {ok}, ranks {rank_mod_p(Gk,q)}+{rank_mod_p(Hd,q)}={N}")
