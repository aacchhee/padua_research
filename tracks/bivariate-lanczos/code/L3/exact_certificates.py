"""Exact-arithmetic certificates for condition (H) on Padua points, n = 1, 2, 3.

Field: Q(sqrt2) implemented with fractions.Fraction (elements a + b*sqrt2),
exact sign test. Padua points (j+k even family) for n <= 3 have coordinates in
Q(sqrt2): cos(j pi/n), cos(k pi/(n+1)).

Basis: monomials x^a y^b of Pi_{2n+1} in graded order (exact). For each n:
  1. exact jet matrix J (values + gradients at the nodes), exact nullspace
     S_1 (dimension printed; expected n(n+1)/2);
  2. exact Hessian map on S_1 and its rank (injectivity);
  3. n in {1, 2}: DUAL certificate for (H): PD matrices A_i (entries in
     Q(sqrt2)) with sum_i <A_i, Hess_i s> = 0 for every basis element s of
     S_1.  Built from a floating SDP solution (cvxpy, only as a guess),
     rounded to rationals and then corrected EXACTLY onto the linear
     constraints by a least-norm correction; PD-ness then checked exactly.
     n = 3: PRIMAL certificate for robust failure: p* in S_1 (exact) with
     Hess p*(z_i) PD at every node, checked exactly.
The floating SDP only proposes candidates; every accepted certificate is
verified in exact arithmetic (a wrong guess is reported as FAIL, never
accepted).

Usage: python3 exact_certificates.py   (prints a verdict per n)
"""
from fractions import Fraction as F
import numpy as np


class Q2:
    """a + b*sqrt(2), a, b rational."""
    __slots__ = ('a', 'b')

    def __init__(self, a, b=0):
        self.a = F(a); self.b = F(b)

    def __add__(s, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __neg__(s):
        return Q2(-s.a, -s.b)

    def __sub__(s, o):
        return s + (-(o if isinstance(o, Q2) else Q2(o)))

    def __rsub__(s, o):
        return Q2(o) - s

    def __mul__(s, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__

    def inv(s):
        den = s.a * s.a - 2 * s.b * s.b
        if den == 0:
            raise ZeroDivisionError
        return Q2(s.a / den, -s.b / den)

    def __truediv__(s, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return s * o.inv()

    def iszero(s):
        return s.a == 0 and s.b == 0

    def sign(s):
        a, b = s.a, s.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if (a > 0) == (b > 0):
            return 1 if a > 0 else -1
        # opposite signs: compare a^2 with 2 b^2
        if a * a > 2 * b * b:
            return 1 if a > 0 else -1
        return 1 if b > 0 else -1

    def __float__(s):
        return float(s.a) + float(s.b) * 2 ** 0.5

    def __repr__(s):
        return f"({s.a}+{s.b}r2)"


ZERO, ONE = Q2(0), Q2(1)
R2H = Q2(0, F(1, 2))  # sqrt2/2


def cos_exact(num, den):
    """cos(num*pi/den) for den in {1,2,3,4}; exact in Q(sqrt2)."""
    num %= 2 * den
    table = {
        1: {0: ONE, 1: -ONE},
        2: {0: ONE, 1: ZERO, 2: -ONE, 3: ZERO},
        3: {0: ONE, 1: Q2(F(1, 2)), 2: Q2(F(-1, 2)), 3: -ONE, 4: Q2(F(-1, 2)), 5: Q2(F(1, 2))},
        4: {0: ONE, 1: R2H, 2: ZERO, 3: -R2H, 4: -ONE, 5: -R2H, 6: ZERO, 7: R2H},
    }
    return table[den][num]


def padua_exact(n):
    pts = []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                pts.append((cos_exact(j, n), cos_exact(k, n + 1)))
    return pts


def exps(d):
    return [(s, k - s) for k in range(d + 1) for s in range(k + 1)]


def qpow(x, e):
    r = ONE
    for _ in range(e):
        r = r * x
    return r


def mono_der(x, y, a, b, dx, dy):
    """d^{dx}/dx^{dx} d^{dy}/dy^{dy} of x^a y^b at (x,y)."""
    if dx > a or dy > b:
        return ZERO
    ca = 1
    for t in range(dx):
        ca *= (a - t)
    cb = 1
    for t in range(dy):
        cb *= (b - t)
    return Q2(ca * cb) * qpow(x, a - dx) * qpow(y, b - dy)


def nullspace(A, ncols):
    """Exact nullspace basis over Q(sqrt2) by Gauss-Jordan elimination."""
    A = [row[:] for row in A]
    m = len(A)
    piv_cols = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, m):
            if not A[i][c].iszero():
                p = i; break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = A[r][c].inv()
        A[r] = [v * inv for v in A[r]]
        for i in range(m):
            if i != r and not A[i][c].iszero():
                f = A[i][c]
                A[i] = [vi - f * vr for vi, vr in zip(A[i], A[r])]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [ZERO] * ncols
        v[fc] = ONE
        for i, pc in enumerate(piv_cols):
            v[pc] = -A[i][fc]
        basis.append(v)
    return basis, len(piv_cols)


def rank(A, ncols):
    _, r = nullspace(A, ncols)
    return r


def hess_entries(z, s, E):
    x, y = z
    hxx = sum((c * mono_der(x, y, a, b, 2, 0) for c, (a, b) in zip(s, E)), ZERO)
    hxy = sum((c * mono_der(x, y, a, b, 1, 1) for c, (a, b) in zip(s, E)), ZERO)
    hyy = sum((c * mono_der(x, y, a, b, 0, 2) for c, (a, b) in zip(s, E)), ZERO)
    return hxx, hxy, hyy


def is_pd(h):
    hxx, hxy, hyy = h
    return hxx.sign() > 0 and (hxx * hyy - hxy * hxy).sign() > 0


def rat(x, den=10 ** 9):
    return F(round(x * den), den)


def dual_certificate(nodes, S, E, Hs):
    """Find PD A_i with sum_i <A_i, Hess_i s_k> = 0 for all k (exactly)."""
    import cvxpy as cp
    M = len(nodes); K = len(S)
    Hf = [[tuple(float(v) for v in Hs[i][k]) for k in range(K)] for i in range(M)]
    A = [cp.Variable((2, 2), symmetric=True) for _ in range(M)]
    t = cp.Variable()
    cons = [A[i] - t * np.eye(2) >> 0 for i in range(M)]
    cons.append(sum(cp.trace(A[i]) for i in range(M)) == 1)
    for k in range(K):
        cons.append(sum(A[i][0, 0] * Hf[i][k][0] + 2 * A[i][0, 1] * Hf[i][k][1] + A[i][1, 1] * Hf[i][k][2]
                        for i in range(M)) == 0)
    cp.Problem(cp.Maximize(t), cons).solve(solver=cp.CLARABEL)
    # unknown vector a = (a_i11, a_i12, a_i22)_i ; constraint rows G a = 0 (exact)
    a0 = []
    for i in range(M):
        v = A[i].value
        a0 += [Q2(rat(v[0, 0])), Q2(rat(v[0, 1])), Q2(rat(v[1, 1]))]
    G = []
    for k in range(K):
        row = []
        for i in range(M):
            hxx, hxy, hyy = Hs[i][k]
            row += [hxx, Q2(2) * hxy, hyy]
        G.append(row)
    # least-norm exact correction: a = a0 - G^T (G G^T)^{-1} G a0
    GG = [[sum((G[r][c] * G[s][c] for c in range(len(a0))), ZERO) for s in range(K)] for r in range(K)]
    Ga0 = [sum((G[r][c] * a0[c] for c in range(len(a0))), ZERO) for r in range(K)]
    # solve GG y = Ga0 exactly
    aug = [GG[r][:] + [Ga0[r]] for r in range(K)]
    for c in range(K):
        p = next(i for i in range(c, K) if not aug[i][c].iszero())
        aug[c], aug[p] = aug[p], aug[c]
        inv = aug[c][c].inv()
        aug[c] = [v * inv for v in aug[c]]
        for i in range(K):
            if i != c and not aug[i][c].iszero():
                f = aug[i][c]
                aug[i] = [vi - f * vc for vi, vc in zip(aug[i], aug[c])]
    yv = [aug[r][K] for r in range(K)]
    a = [a0[c] - sum((G[r][c] * yv[r] for r in range(K)), ZERO) for c in range(len(a0))]
    resid = [sum((G[r][c] * a[c] for c in range(len(a))), ZERO) for r in range(K)]
    assert all(v.iszero() for v in resid)
    Ai = [(a[3 * i], a[3 * i + 1], a[3 * i + 2]) for i in range(M)]
    ok = all(is_pd(h) for h in Ai)
    return ok, Ai, float(t.value)


def primal_certificate(nodes, S, E, Hs):
    """Find p* in S_1 (exact combination of the exact basis) with all Hessians PD."""
    import cvxpy as cp
    M = len(nodes); K = len(S)
    Hf = [[tuple(float(v) for v in Hs[i][k]) for k in range(K)] for i in range(M)]
    c = cp.Variable(K); lam = cp.Variable()
    cons = [cp.norm(c, 'inf') <= 1]
    for i in range(M):
        hxx = sum(Hf[i][k][0] * c[k] for k in range(K))
        hxy = sum(Hf[i][k][1] * c[k] for k in range(K))
        hyy = sum(Hf[i][k][2] * c[k] for k in range(K))
        Hi = cp.bmat([[hxx, hxy], [hxy, hyy]])
        cons.append(0.5 * (Hi + Hi.T) - lam * np.eye(2) >> 0)
    cp.Problem(cp.Maximize(lam), cons).solve(solver=cp.CLARABEL)
    cr = [Q2(rat(v, 10 ** 6)) for v in c.value]
    pstar = [sum((cr[k] * S[k][j] for k in range(K)), ZERO) for j in range(len(E))]
    H = []
    for i in range(M):
        H.append(tuple(sum((cr[k] * Hs[i][k][q] for k in range(K)), ZERO) for q in range(3)))
    ok = all(is_pd(h) for h in H)
    return ok, pstar, H, cr, float(lam.value)


def run(n):
    d = 2 * n + 1
    E = exps(d)
    nodes = padua_exact(n)
    J = []
    for (x, y) in nodes:
        for (dx, dy) in [(0, 0), (1, 0), (0, 1)]:
            J.append([mono_der(x, y, a, b, dx, dy) for (a, b) in E])
    S, rk = nullspace(J, len(E))
    # verify exactly that each basis vector annihilates J
    for s in S:
        for row in J:
            assert sum((u * v for u, v in zip(row, s)), ZERO).iszero()
    Hs = [[hess_entries(z, s, E) for s in S] for z in nodes]
    Hmat = []
    for i in range(len(nodes)):
        for q in range(3):
            Hmat.append([Hs[i][k][q] for k in range(len(S))])
    hr = rank(Hmat, len(S))
    print(f"Padua n={n}: M={len(nodes)} D={len(E)} rank J={rk} dim S1={len(S)} (expected {n*(n+1)//2}); "
          f"rank Hess|S1={hr} (injective: {hr == len(S)})")
    return nodes, E, S, Hs, hr


def main():
    for n in (1, 2):
        nodes, E, S, Hs, hr = run(n)
        ok, Ai, t = dual_certificate(nodes, S, E, Hs)
        print(f"  DUAL certificate for (H): exact PD check {'PASS' if ok else 'FAIL'} (float SDP margin t={t:.4g})")
        for i, (z, A) in enumerate(zip(nodes, Ai)):
            print(f"    node {i} ({float(z[0]):+.4f},{float(z[1]):+.4f}): A = [[{A[0]},{A[1]}],[{A[1]},{A[2]}]]")
        print(f"  => (H) holds for Padua n={n}: {'PROVED (exact)' if ok and hr == len(S) else 'NOT CERTIFIED'}")
    n = 3
    nodes, E, S, Hs, hr = run(n)
    ok, pstar, H, cr, lam = primal_certificate(nodes, S, E, Hs)
    print(f"  PRIMAL certificate (robust failure of (H)): exact PD check at all nodes {'PASS' if ok else 'FAIL'} "
          f"(float margin {lam:.4g})")
    print("    coordinates of p* in the exact S1 basis (rational):", [str(v.a) for v in cr])
    print("    p* monomial coefficients (x^a y^b: a + b*sqrt2):")
    for (a, b), c in zip(E, pstar):
        if not c.iszero():
            print(f"      x^{a} y^{b}: {c}")
    for i, (z, h) in enumerate(zip(nodes, H)):
        det = h[0] * h[2] - h[1] * h[1]
        print(f"    node {i} ({float(z[0]):+.4f},{float(z[1]):+.4f}): hxx={float(h[0]):.6g} det={float(det):.6g} "
              f"[sign hxx {h[0].sign()}, sign det {det.sign()}]")
    print(f"  => Padua n=3: S1 contains p* with PD Hessians at all nodes: {'PROVED (exact)' if ok else 'NOT CERTIFIED'}")
    # Rigorous explicit radius delta_0 with p* >= 0 on every closed ball B(z_i, delta_0):
    # p*(z+h) >= 1/2 lam_i |h|^2 - (1/6) C3 |h|^3, lam_i >= det_i/tr_i, C3 >= sup over the box
    # |x|,|y| <= 1 + rmax of |D^3 p*(xi)[u,u,u]| (|u| = 1), bounded by
    # sum_{a+b=3} binom(3,a) sum_m |c_m| ff(m_x,a) ff(m_y,b) Rb^(m_x-a+m_y-b).
    s_lo, s_hi = F(14142135, 10 ** 7), F(14142136, 10 ** 7)  # bounds for sqrt2

    def lower(v):
        return v.a + (v.b * s_lo if v.b >= 0 else v.b * s_hi)

    def upper(v):
        return v.a + (v.b * s_hi if v.b >= 0 else v.b * s_lo)

    rmax = F(1, 10)
    Rb = 1 + rmax
    coef_abs = [max(abs(lower(c)), abs(upper(c))) for c in pstar]

    def ff(m, k):
        r = 1
        for t in range(k):
            r *= max(m - t, 0)
        return r
    C3 = F(0)
    binom3 = {0: 1, 1: 3, 2: 3, 3: 1}
    for a in range(4):
        b = 3 - a
        C3 += binom3[a] * sum((ca * ff(mx, a) * ff(my, b) * Rb ** max(mx - a + my - b, 0)
                               for ca, (mx, my) in zip(coef_abs, E) if mx >= a and my >= b), F(0))
    lam_lb = []
    for h in H:
        det = h[0] * h[2] - h[1] * h[1]
        tr = h[0] + h[2]
        lam_lb.append(lower(det) / upper(tr))
    d0 = min(rmax, min(3 * l / C3 for l in lam_lb))
    print(f"  rigorous radius: min lambda_min lower bound = {float(min(lam_lb)):.6g}, C3 upper bound = {float(C3):.6g}, "
          f"delta_0 = {d0} ~ {float(d0):.4e}  (p* >= 0 on all closed balls B(z_i, delta_0))")


if __name__ == '__main__':
    main()
