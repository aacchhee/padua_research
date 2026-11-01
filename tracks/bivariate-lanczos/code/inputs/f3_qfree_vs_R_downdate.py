"""F3 adversarial test: is Q-free bivariate downdating (EGK-1991 transcribed to 2D, state = (Hx,Hy))
anything more than classical Cholesky/QR downdating?

Observation (exact arithmetic): with A = sqrt(W) V (V = Chebyshev-product Vandermonde, graded order,
W points, N = dim Pi_n columns) = Q R, and C_x = Q^T sqrt(W) X V, C_y likewise,
      H_x = Q^T X Q = C_x R^{-1},   H_y = C_y R^{-1}.
So the state (R, C_x, C_y) is the textbook 'QR with right-hand sides' of sliding-window RLS, and a node
removal is LINPACK/Saunders Cholesky downdating (Stewart 1979; Bojanczyk-Brent-Van Dooren-de Hoog 1987),
whose sequential behaviour is covered by Stewart, IEEE TSP 43 (1995) 2642 ('relational stability':
final decomposition accurate if it is well conditioned, even if intermediate ones are not).
In OP coordinates R = I and the downdate is chol(I - u u^T): EGK-2D.

Test: same random sliding windows as qfree_bivariate_downdate.py; compare final (Hx,Hy) errors of
  (H)  Q-free OP-coordinate downdate (EGK-2D)
  (R)  R/C downdate with LINPACK/Saunders rotations, H = C R^{-1} formed at the end
and a 'recovery' scenario: run an almost-interpolatory window (W ~ N, tiny 1-leverage),
then only add points until W = 400 (well conditioned).  Stewart predicts (R) recovers.
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import qfree_bivariate_downdate as QF   # gl order, ref_H, evalp, modify

def cheb_row(z, n):
    x, y = z
    tx = np.cos(np.arange(n + 1) * np.arccos(np.clip(x, -1, 1)))
    ty = np.cos(np.arange(n + 1) * np.arccos(np.clip(y, -1, 1)))
    return np.array([tx[i] * ty[j] for (i, j) in QF.gl(n)])

def R_init(pts, w, n):
    V = np.array([cheb_row(z, n) for z in pts]); s = np.sqrt(w)[:, None]
    A = s * V; Q, R = np.linalg.qr(A); d = np.sign(np.diag(R)); Q = Q * d; R = d[:, None] * R
    return R, Q.T @ (pts[:, [0]] * A), Q.T @ (pts[:, [1]] * A)

def rot(a, b):
    r = np.hypot(a, b); return (1.0, 0.0) if r == 0 else (a / r, b / r)

def R_update(R, Cx, Cy, z, w, n):
    v = np.sqrt(w) * cheb_row(z, n); rows = [v.copy(), z[0] * v, z[1] * v]
    N = len(v)
    for k in range(N):
        c, s = rot(R[k, k], rows[0][k])
        for M_, r in ((R, rows[0]), (Cx, rows[1]), (Cy, rows[2])):
            mk = M_[k].copy(); M_[k] = c * mk + s * r; r[:] = -s * mk + c * r
    return R, Cx, Cy

def R_downdate(R, Cx, Cy, z, w, n):
    """LINPACK dchdd / Saunders: solve R^T p = a, alpha = sqrt(1-|p|^2), rotations U with
    U [p; alpha] = e_{N+1}; apply to [R C; 0 c*], c* = (a2 - p^T C)/alpha."""
    v = np.sqrt(w) * cheb_row(z, n); N = len(v)
    p = np.linalg.solve(R.T, v); lev = p @ p
    alpha = np.sqrt(max(1 - lev, 0.0))
    bx = (z[0] * v - p @ Cx) / alpha; by = (z[1] * v - p @ Cy) / alpha
    br, bxx, byy = np.zeros(N), bx.copy(), by.copy()
    # rotations k = N-1..0 combining (row k, extra row)
    t = alpha
    for k in range(N - 1, -1, -1):
        c, s = rot(t, p[k]); t = np.hypot(t, p[k])
        # transform so that p_k goes to the extra row: [p_k; t] -> [0; t']
        for M_, e in ((R, br), (Cx, bxx), (Cy, byy)):
            mk = M_[k].copy(); M_[k] = c * mk - s * e; e[:] = s * mk + c * e
    return R, Cx, Cy, lev

def H_from_R(R, Cx, Cy):
    Ri = np.linalg.inv(R); return Cx @ Ri, Cy @ Ri

def compare(seed, W, n, steps, grow_to=None):
    rng = np.random.default_rng(seed)
    M = W + steps + (grow_to or 0) + 10
    pts = rng.uniform(-1, 1, (M, 2)); w = rng.uniform(0.5, 1.5, M)
    Hx, Hy = QF.ref_H(pts[:W], w[:W], n); sw = w[:W].sum()
    R, Cx, Cy = R_init(pts[:W], w[:W], n)
    minlev = 1.0
    for k in range(steps):
        Hx, Hy, sw, _ = QF.modify(Hx, Hy, sw, pts[W + k], w[W + k], n, +1)
        Hx, Hy, sw, lev = QF.modify(Hx, Hy, sw, pts[k], w[k], n, -1)
        R, Cx, Cy = R_update(R, Cx, Cy, pts[W + k], w[W + k], n)
        R, Cx, Cy, lev2 = R_downdate(R, Cx, Cy, pts[k], w[k], n)
        minlev = min(minlev, 1 - lev)
    lo, hi = steps, W + steps
    if grow_to:
        for k in range(grow_to - W):
            z = pts[hi + k]
            Hx, Hy, sw, _ = QF.modify(Hx, Hy, sw, z, w[hi + k], n, +1)
            R, Cx, Cy = R_update(R, Cx, Cy, z, w[hi + k], n)
        hi = hi + grow_to - W
    Rx, Ry = QF.ref_H(pts[lo:hi], w[lo:hi], n)
    # sign-normalise R-approach to positive pivots like ref (diag R > 0 already gives that)
    Gx, Gy = H_from_R(R, Cx, Cy)
    eH = max(np.abs(Hx - Rx).max(), np.abs(Hy - Ry).max())
    eR = max(np.abs(Gx - Rx).max(), np.abs(Gy - Ry).max())
    kap = np.linalg.cond(R)
    return minlev, eH, eR, kap, hi - lo

if __name__ == "__main__":
    n = 12; N = (n + 1) * (n + 2) // 2
    print(f"n={n}, N={N}. columns: min(1-leverage) seen | final window size | err Q-free H (EGK-2D) | err R/C LINPACK | cond(R_final, Chebyshev basis)")
    for (W, steps, grow) in [(400, 400, None), (150, 400, None), (100, 300, None), (95, 200, None),
                             (100, 300, 400), (95, 200, 400), (93, 200, 400)]:
        for seed in (0, 1):
            ml, eH, eR, kap, Wf = compare(seed, W, n, steps, grow)
            tag = f"W={W} steps={steps}" + (f" then grow to {grow}" if grow else "")
            print(f"{tag:32s} seed={seed}  {ml:.1e} | {Wf} | {eH:.1e} | {eR:.1e} | {kap:.1e}", flush=True)
