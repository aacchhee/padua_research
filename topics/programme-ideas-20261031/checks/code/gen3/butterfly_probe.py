"""Probe: complementary low-rank (butterfly) structure of the value matrix Q (M x N)
of graded discrete orthonormal bivariate polynomials, versus the HSS structure that is
known to fail (padua RESULTS: top-level off-diagonal ranks ~430/517 at N=1035).
Rows ordered by a 2D quadtree (Morton) on the nodes; columns in graded order.
At butterfly level l (0..L): row blocks = 2^l quadtree boxes, column blocks = 2^(L-l)
consecutive degree ranges. Report the max numerical rank (tol 1e-8 relative) over blocks.
Node sets: Padua n=44 (N=1035) and uniform random M=N=1035, random positive weights.
"""
import numpy as np
rng = np.random.default_rng(0)

def padua(n):
    pts = [(np.cos(j*np.pi/n), np.cos(k*np.pi/(n+1))) for j in range(n+1) for k in range(n+2) if (j+k) % 2 == 0]
    return np.array(pts)

def cheb_vander(x, y, n):
    Tx = np.polynomial.chebyshev.chebvander(x, n); Ty = np.polynomial.chebyshev.chebvander(y, n)
    cols = [Tx[:, d-j]*Ty[:, j] for d in range(n+1) for j in range(d+1)]
    return np.column_stack(cols)

def morton_order(P, depth):
    u = ((P+1)/2*(2**depth-1e-9)).astype(int)
    key = np.zeros(len(P), dtype=np.int64)
    for b in range(depth):
        key |= ((u[:, 0] >> b) & 1) << (2*b+1)
        key |= ((u[:, 1] >> b) & 1) << (2*b)
    return np.argsort(key, kind="stable")

def numrank(B, tol=1e-8):
    if min(B.shape) == 0: return 0
    s = np.linalg.svd(B, compute_uv=False)
    return int(np.sum(s > tol*s[0])) if s[0] > 0 else 0

def butterfly_ranks(Q, L):
    M, N = Q.shape
    out = []
    for l in range(L+1):
        rb, cb = 2**l, 2**(L-l)
        rs = np.array_split(np.arange(M), rb); cs = np.array_split(np.arange(N), cb)
        mx = max(numrank(Q[np.ix_(r, c)]) for r in rs for c in cs)
        out.append((l, len(rs[0]), len(cs[0]), mx))
    return out

n = 44
for name in ["padua44", "random"]:
    if name == "padua44":
        P = padua(n); w = np.ones(len(P))
    else:
        P = rng.uniform(-1, 1, size=(1035, 2)); w = rng.uniform(0.5, 1.5, 1035)
    P = P[morton_order(P, 6)]
    V = cheb_vander(P[:, 0], P[:, 1], n) * np.sqrt(w)[:, None]
    Q, R = np.linalg.qr(V); Q, R = np.linalg.qr(Q)   # twice is enough
    M, N = Q.shape
    print(f"\n{name}: M={M}, N={N}, levels L=5 (row boxes x column degree-ranges)")
    print(" level | rows/block | cols/block | max numerical rank (1e-8)")
    for l, rbs, cbs, mx in butterfly_ranks(Q, 5):
        print(f"  {l:2d}   | {rbs:5d}      | {cbs:5d}      | {mx:4d}")
    # HSS-type reference: top-level off-diagonal block rank, same row order
    h = M//2
    print("  HSS reference, top-level off-diag rank:", numrank(Q[:h, h:]), "of", min(h, N-h))
