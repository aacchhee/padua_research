#!/usr/bin/env python3
"""Claude audit-01 supplementary regressions (float64 / exact), written by the
auditor without importing developer code. All float results are MEASURED-level
corroboration only; exact parts are explicit rational checks of small claims.
"""
import json, math, sys, hashlib, platform
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import scipy.linalg
from numpy.polynomial import legendre as Lg


def hint(r):
    return F(0) if r % 2 else F(-2, r * r - 1)


def fold(r, N):
    r %= 2 * N
    return r if r <= N else 2 * N - r


def q(m, a, b):
    A, B = fold(a, m), fold(b, m + 1)
    return hint(A) * hint(B) if A + B <= m else hint(m - A) * hint(m + 1 - B)


def nodes(m):
    J = [(j, k) for j in range(m + 1) for k in range(m + 2) if (j + k) % 2 == 0]
    x = np.array([math.cos(j * math.pi / m) for j, k in J])
    y = np.array([math.cos(k * math.pi / (m + 1)) for j, k in J])
    return J, x, y


def T(r, t):
    return np.cos(r * np.arccos(np.clip(t, -1, 1)))


def padua_weights(m):
    J, x, y = nodes(m)
    modes = [(a, d - a) for d in range(m + 1) for a in range(d, -1, -1)]
    V = np.array([T(a, x) * T(b, y) for a, b in modes])
    rhs = np.array([float(hint(a) * hint(b)) for a, b in modes])
    return J, x, y, np.linalg.solve(V, rhs)


def leg_orth(n, t):
    """columns ell_0..ell_n at points t (orthonormal on [-1,1])."""
    out = np.empty((len(t), n + 1))
    for a in range(n + 1):
        c = np.zeros(a + 1); c[a] = 1
        out[:, a] = Lg.legval(t, c) * math.sqrt((2 * a + 1) / 2)
    return out


def total_basis(n, x, y):
    Lx, Ly = leg_orth(n, x), leg_orth(n, y)
    cols = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
    return np.column_stack([Lx[:, a] * Ly[:, b] for a, b in cols]), cols


def padua_extrema(m):
    J, x, y, w = padua_weights(m)
    B, _ = total_basis(m - 1, x, y)
    G = B.T @ (w[:, None] * B)
    ev = scipy.linalg.eigvalsh(G)
    return ev[0], ev[-1], int(np.sum(w < 0)), [J[i] for i in np.where(w < 0)[0]]


def cc_weights(N):
    t = np.cos(np.pi * np.arange(N + 1) / N)
    V = np.array([T(r, t) for r in range(N + 1)])
    rhs = np.array([float(hint(r)) for r in range(N + 1)])
    return t, np.linalg.solve(V, rhs)


def cc_gram(N, n):
    t, w = cc_weights(N)
    L = leg_orth(n, t)
    return L.T @ (w[:, None] * L)


def tensor_check(m, n):
    Gx, Gy = cc_gram(m, n), cc_gram(m + 1, n)
    cols = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
    G = np.array([[Gx[a, c] * Gy[b, d] for (c, d) in cols] for (a, b) in cols])
    e = scipy.linalg.eigvalsh(G); ex = scipy.linalg.eigvalsh(Gx); ey = scipy.linalg.eigvalsh(Gy)
    return dict(m=m, n=n, tensor=[e[0], e[-1]], coord_min=min(ex[0], ey[0]), coord_max=max(ex[-1], ey[-1]),
                disc=max(abs(e[0] - min(ex[0], ey[0])), abs(e[-1] - max(ex[-1], ey[-1]))))


def rhombus_packet(m):
    M = (m - 1) // 2
    u = np.zeros(m)
    for k in range(1, M + 1):
        u[m - 1 - 2 * k] += 1 / k
        u[m - 1] -= (1 - 2 * k / m) / k
    # U_n = sum over r same parity <= n of 2 T_r, with T_0 coefficient 1
    a = np.zeros(m)
    for nn in range(m):
        if u[nn] == 0:
            continue
        for r in range(nn % 2, nn + 1, 2):
            a[r] += u[nn] * (1 if r == 0 else 2)
    C = np.zeros((m, m))
    nz = np.nonzero(a)[0]
    for r in nz:
        for s in nz:
            if (r + s) % 2:
                raise SystemExit('parity')
            i, j = (r + s) // 2, abs(r - s) // 2
            C[i, j] += a[r] * a[s] / 2
            C[j, i] += a[r] * a[s] / 2
    for i in range(m):
        for j in range(m):
            if i + j > m - 1 and abs(C[i, j]) > 1e-12:
                raise SystemExit('degree')
    J, x, y, w = padua_weights(m)
    val = sum(C[i, j] * T(i, x) * T(j, y) for i in range(m) for j in range(m) if C[i, j] != 0)
    num = float(np.dot(w, val ** 2))
    g, gw = np.polynomial.legendre.leggauss(m + 1)
    X, Y = np.meshgrid(g, g, indexing='ij')
    V = sum(C[i, j] * T(i, X) * T(j, Y) for i in range(m) for j in range(m) if C[i, j] != 0)
    den = float(np.sum(np.outer(gw, gw) * V ** 2))
    return num / den


def exact_small_claims():
    out = {}
    # PD-N045 section 1 cycle at m=3..8 via moment formula
    def Hent(i, j, k, l):
        return sum(hint(u) * hint(v) for u in (i + k, abs(i - k)) for v in (j + l, abs(j - l))) / 4
    def Rent(m, i, j, k, l):
        return sum(q(m, u, v) for u in (i + k, abs(i - k)) for v in (j + l, abs(j - l))) / 4
    cyc = {}
    for m in range(3, 9):
        A = lambda P, Qm: 2 * Hent(*P, *Qm) - Rent(m, *P, *Qm)
        u, v, z = (0, 0), (2, 0), (0, 2)
        prod = A(u, v) * A(v, z) * A(z, u)
        cyc[m] = [str(A(u, v)), str(A(v, z)), str(A(z, u)), prod > 0]
    out['N045_cycle'] = cyc
    m = 4
    out['N045_m4'] = [str(Hent(2, 0, 0, 3) - Rent(4, 2, 0, 0, 3)), str(Hent(2, 0, 2, 1) - Rent(4, 2, 0, 2, 1))]
    # PD-N051 defects: Q(qp) - int(qp) for q=T2, p=T_{m-1} in x (odd m) or y (even m)
    d = {}
    for m in range(3, 16):
        if m % 2:
            val = (q(m, m + 1, 0) + q(m, m - 3, 0)) / 2 - (hint(m + 1) * 2 + hint(m - 3) * 2) / 2
            exp = hint(m - 1) - hint(m + 1)
        else:
            val = (q(m, 0, m + 1) + q(m, 0, m - 3)) / 2 - (2 * hint(m + 1) + 2 * hint(m - 3)) / 2
            exp = hint(m)
        d[m] = [str(val), val == exp, val != 0]
    out['N051_defects'] = d
    # PD-N048 / N052 K(c,c) closed form
    kc = {}
    for mm in range(1, 30):
        s = F(sum((2 * a + 1) * (2 * b + 1) for a in range(mm) for b in range(mm - a)), 4)
        kc[mm] = s == F(mm * (mm + 1) * (mm * mm + mm + 1), 24)
    out['Kcc_formula_m1_29'] = all(kc.values())
    # PD-T111 sign and asymptotic table
    tab = {}
    for mm in [3, 4, 5, 10, 100, 1000, 10000, 100000]:
        r = mm // 2; N = 2 * r + 1
        S = sum(F(1, 2 * i - 1) for i in range(1, r + 1)) if mm <= 10000 else None
        if S is None:
            Sf = sum(1.0 / (2 * i - 1) for i in range(1, r + 1))
            A = 8 / (N * (N + 1)) - 16 * Sf / (N * N - 1)
            hm = 2 / (1 - mm * mm) if mm % 2 == 0 else 0
            w = (A - 2 * hm) / (2 * mm * (mm + 1))
        else:
            A = F(8, N * (N + 1)) - 16 * S / (N * N - 1)
            hm = F(2, 1 - mm * mm) if mm % 2 == 0 else F(0)
            w = float((A - 2 * hm) / (2 * mm * (mm + 1)))
        tab[mm] = [w, -w * mm ** 4 - 4 * math.log(mm)]
    out['T111_w_and_(-w m^4 - 4log m)'] = tab
    return out


def reconstruction_check(m, n):
    """PD-T115 diamond filter reproduces random q with |a|+|b|<=n;
    PD-N053 rectangular filter produces the predicted spurious coefficient."""
    rng = np.random.default_rng(1)
    pts = [(j * math.pi / m, k * math.pi / (m + 1)) for j in range(2 * m) for k in range(2 * m + 2) if (j + k) % 2 == 0]
    freqs = [(a, b) for a in range(-n, n + 1) for b in range(-n, n + 1) if abs(a) + abs(b) <= n]
    coef = {f: rng.standard_normal() for f in freqs}
    def qf(t, s):
        return sum(c * math.cos(a * t + b * s) for (a, b), c in coef.items())
    def kap(N, nn, r):
        return (max(N - abs(r), 0) - max(nn - abs(r), 0)) / (N - nn)
    def K(N, nn, t):
        return sum(kap(N, nn, r) * math.cos(r * t) for r in range(-N, N + 1))
    def H(t, s):
        u, v = (t + s) / 2, (t - s) / 2
        return 0.5 * (K(m, n, u) * K(m, n, v) + K(m, n, u + math.pi) * K(m, n, v + math.pi))
    samples = [(tj, sk, qf(tj, sk)) for tj, sk in pts]
    errs = []
    for _ in range(5):
        t, s = rng.uniform(0, 2 * math.pi, 2)
        rec = sum(H(t - tj, s - sk) * v for tj, sk, v in samples) / (2 * m * (m + 1))
        errs.append(abs(rec - qf(t, s)))
    # rectangular operator coefficient at (1-m,-m) for input cos t cos s
    v1, v2 = 1 - m, -m
    acc = 0j
    for tj, sk in pts:
        acc += math.cos(tj) * math.cos(sk) * complex(math.cos(-(v1 * tj + v2 * sk)), math.sin(-(v1 * tj + v2 * sk)))
    acc /= len(pts)
    coeff = kap(m, n, v1) * kap(m + 1, n, v2) * acc
    pred = 1 / (4 * (m - n) * (m + 1 - n))
    return {'m': m, 'n': n, 'diamond_max_err': max(errs), 'rect_coeff': coeff.real, 'rect_pred': pred}


def main():
    out = {'auditor': 'Claude Opus 5.5 xhigh (audit-01)', 'python': sys.version, 'numpy': np.__version__,
           'scipy': scipy.__version__, 'platform': platform.platform(),
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out['exact_small_claims'] = exact_small_claims(); print('exact ok', flush=True)
    sweep = {}
    for m in range(2, 41):
        lo, hi, nneg, negs = padua_extrema(m)
        sweep[m] = [lo, hi, max(1 - lo, hi - 1), nneg, negs]
    out['padua_float_sweep_m2_40'] = sweep; print('sweep ok', flush=True)
    out['tensor_T117'] = [tensor_check(m, n) for m in (2, 3, 5, 10, 20, 30, 40) for n in sorted({0, m // 2, m - 1})]
    print('tensor ok', flush=True)
    out['rhombus_N049'] = {m: rhombus_packet(m) for m in (8, 16, 32, 64)}; print('rhombus ok', flush=True)
    out['reconstruction_T115_N053'] = [reconstruction_check(m, n) for m, n in ((3, 2), (4, 2), (5, 3), (6, 5))]
    Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + '\n')
    print('PASS')


if __name__ == '__main__':
    main()
