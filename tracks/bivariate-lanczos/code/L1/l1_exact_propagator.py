"""R03: is the non-product amplification a property of the exact recurrence?  Build the exact-arithmetic
window coefficients (long double, full reorthogonalisation against all previous columns, same graded order),
then drive the IDEALISED per-node propagator L*(z_i) (exact coefficients, PD-T?...-104/-105) with iid forcing of
size u/sqrt(M), u = 2^-52, in long double.  Compare its response P*(n) with the response P(n) of the double run's
computed coefficients and with the measured double loss.  Also: rotation scan of the triangle.
MEASURED only.  Usage: python3 -I l1_exact_propagator.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, l1_recurrence as L

LD = np.longdouble
EPS = 2.0 ** -52


def exact_coefficients(x, y, w, nmax):
    idx, pos, parent, op, start = L.tables(nmax)
    N = len(idx); M = len(x)
    xl, yl = x.astype(LD), y.astype(LD)
    Q = np.zeros((M, N), dtype=LD)
    v = np.sqrt(w.astype(LD)); Q[:, 0] = v / np.sqrt(np.sum(v * v))
    coef = [None] * N
    for k in range(1, N):
        p = parent[k]; a = xl if op[k] == 'J' else yl
        u0 = a * Q[:, p]; u = u0.copy()
        for _ in range(3):
            u = u - Q[:, :k] @ (Q[:, :k].T @ u)
        beta = np.sqrt(np.sum(u * u)); Q[:, k] = u / beta
        W = L.window(k, idx, start, 'block')
        coef[k] = (W, Q[:, W].T @ u0, beta)          # exact (to long-double accuracy) window coefficients
    return coef, (idx, pos, parent, op, start), Q


def response(x, y, coef, tab, N, dtype, seed=0):
    idx, pos, parent, op, start = tab
    M = len(x); rng = np.random.default_rng(seed)
    xx, yy = x.astype(dtype), y.astype(dtype)
    g = np.zeros((M, N), dtype=dtype)
    g[:, 0] = (rng.standard_normal(M) * EPS / np.sqrt(M)).astype(dtype)
    for k in range(1, N):
        W, h, beta = coef[k]; p = parent[k]
        a = xx if op[k] == 'J' else yy
        g[:, k] = (a * g[:, p] - g[:, W] @ np.asarray(h, dtype=dtype)
                   + (rng.standard_normal(M) * EPS / np.sqrt(M)).astype(dtype)) / dtype(beta)
    return np.sqrt(np.sum(g * g, axis=0)).astype(float)


def compare(name, P, w, nmax):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    cstar, tab, Qs = exact_coefficients(x, y, w, nmax)
    N = len(tab[0])
    Pstar = response(x, y, cstar, tab, N, LD)
    Qd, cd, tabd = L.recurrence(x, y, w, nmax, win='block', orth='cgs')
    Pd = response(x, y, cd, tabd, N, float)
    G = Qd.T @ Qd
    hdev = max(float(np.abs(np.asarray(cd[k][1], dtype=LD) - cstar[k][1]).max()) for k in range(1, N))
    out = []
    for n in range(4, nmax + 1, 4):
        Nn = (n + 1) * (n + 2) // 2
        out.append(f"n{n}: L={np.abs(G[:Nn, :Nn] - np.eye(Nn)).max():.0e} P={Pd[:Nn].max():.0e} P*={Pstar[:Nn].max():.0e}")
    print(f"{name:24s} " + " | ".join(out) + f" | max|h_computed - h_exact|={hdev:.0e}", flush=True)


if __name__ == '__main__':
    rng = np.random.default_rng(11)
    M = 1681
    sq = rng.uniform(-1, 1, (M, 2)); one = np.ones(M)
    compare('square', sq, one, 20)
    compare('square rot pi/4', L.rotate(sq, np.pi / 4), one, 20)
    dk = []
    while len(dk) < M:
        p = rng.uniform(-1, 1, 2)
        if p @ p <= 1: dk.append(p)
    compare('disk', np.array(dk), one, 20)
    tr = []
    while len(tr) < M:
        p = rng.uniform(0, 1, 2)
        if p.sum() <= 1: tr.append(2 * p - 1)
    tr = np.array(tr)
    compare('triangle', tr, one, 16)
    # rotation scan of the triangle with the double recurrence (loss at n = 12)
    print("triangle rotation scan (double bj, loss at n = 12 and n = 16):")
    for th in np.linspace(0, np.pi, 13)[:-1]:
        Pt = L.rotate(tr, th)
        Qd, _, _ = L.recurrence(Pt[:, 0], Pt[:, 1], one, 16, win='block', orth='cgs')
        G = Qd.T @ Qd
        l12 = np.abs(G[:91, :91] - np.eye(91)).max(); l16 = np.abs(G - np.eye(G.shape[0])).max()
        print(f"   theta={th:.3f}: loss n12 {l12:.1e}  n16 {l16:.1e}", flush=True)
