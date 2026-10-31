"""Reviewer (L3 reconstruction 02): independent exact check of PD-T?...-312/313 and PD-N?...-303.

Certificate (313): P_n = 9(g1^2 - g0 g2/2) + (g2^2 - g1 g3),
  g_m = T_{n-m}(x) T_m(y) - T_m(x) T_{n+1-m}(y),
Padua points {(cos j pi/n, cos k pi/(n+1)) : 0<=j<=n, 0<=k<=n+1, j+k even}.

Everything is built here from scratch (integer Chebyshev coefficients, own 2D polynomial arithmetic,
own exact reduction, own rational interval arithmetic in rigorous.py). No developer module imported.

Checks per n:
 (D)  deg(2 P_n) <= 2n+1 exactly (the degree-(2n+2) part cancels) and P_n != 0.
 (Z)  P_n, dP/dx, dP/dy vanish EXACTLY at every Padua node: interior nodes of parity class r are the
      common zero grid of hx_r(x) = gcd(T_n(x) - (-1)^r, U_{n-1}(x)) and hy_r(y) = gcd(T_{n+1}(y) - (-1)^r, U_n(y));
      F vanishes on that grid iff its normal form modulo the (Groebner) pair {hx_r(x), hy_r(y)} is 0.
      Edge nodes: substitute x = +-1 or y = +-1 exactly and reduce modulo the other parity factor;
      corners: exact rational evaluation.
 (G)  the boundary gradient formulas of 313 (E1-E4, corners) hold EXACTLY for m = 0..3 (same reductions).
 (H)  Hess P_n is positive definite at every node: rigorous rational-interval enclosures of the node
      coordinates (certified by sign changes of U_{n-1}, U_n) and of P_xx, P_xy, P_yy; accept iff
      lower bounds of P_xx and of det are > 0.
 (I)  312 equivalence on interior nodes: for c in a list, PD of Hess[(1-c)(g1^2 - g0g2/2) + c(g2^2 - g1g3)]
      versus the criterion 0 < c S T < 1/4 (S = 1-x^2, T = 1-y^2), both decided by rigorous intervals.
Usage: python3 -I padua_turan_check.py nmin nmax
"""
import sys
import os
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rigorous import Iv, eval_poly2, certified_cos_nodes  # noqa: E402

# ---------------------------------------------------------------- univariate integer/rational polys
def T_coeffs(k):
    a, b = [1], [0, 1]
    if k == 0:
        return a
    for _ in range(k - 1):
        c = [0] + [2 * v for v in b]
        for i, v in enumerate(a):
            c[i] -= v
        a, b = b, c
    return b


def U_coeffs(k):
    if k < 0:
        return [0]
    a, b = [1], [0, 2]
    if k == 0:
        return a
    for _ in range(k - 1):
        c = [0] + [2 * v for v in b]
        for i, v in enumerate(a):
            c[i] -= v
        a, b = b, c
    return b


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdivmod(a, b):
    a = [Fr(v) for v in trim(a)]; b = [Fr(v) for v in trim(b)]
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        c = a[-1] / b[-1]; d = len(a) - len(b)
        q[d] = c
        for i, v in enumerate(b):
            a[i + d] -= c * v
        a = trim(a)
        if len(a) == 1 and a[0] == 0:
            break
    return q, a


def pgcd(a, b):
    a, b = trim([Fr(v) for v in a]), trim([Fr(v) for v in b])
    while not (len(b) == 1 and b[0] == 0):
        _, r = pdivmod(a, b)
        a, b = b, r
    return [v / a[-1] for v in a]  # monic


def padd(a, b, sb=1):
    out = [Fr(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += sb * v
    return trim(out)


# ---------------------------------------------------------------- bivariate polys as dict {(a, b): c}
def outer(px, py, s=1):
    return {(i, j): s * a * b for i, a in enumerate(px) if a for j, b in enumerate(py) if b}


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}


def scal(c, p):
    return {k: c * v for k, v in p.items() if c * v != 0}


def mul(p, q):
    out = {}
    for (a, b), u in p.items():
        for (c, d), v in q.items():
            out[(a + c, b + d)] = out.get((a + c, b + d), 0) + u * v
    return {k: v for k, v in out.items() if v != 0}


def dx(p):
    return {(a - 1, b): a * c for (a, b), c in p.items() if a > 0}


def dy(p):
    return {(a, b - 1): b * c for (a, b), c in p.items() if b > 0}


def total_degree(p):
    return max((a + b for (a, b) in p), default=-1)


def subs_x(p, val):
    """p(val, y) as univariate list in y."""
    out = {}
    for (a, b), c in p.items():
        out[b] = out.get(b, 0) + c * Fr(val) ** a
    d = max(out, default=0)
    return trim([out.get(i, 0) for i in range(d + 1)])


def subs_y(p, val):
    out = {}
    for (a, b), c in p.items():
        out[a] = out.get(a, 0) + c * Fr(val) ** b
    d = max(out, default=0)
    return trim([out.get(i, 0) for i in range(d + 1)])


def reduce_xy(p, hx, hy):
    """Normal form of p modulo {hx(x), hy(y)} (both monic); zero iff p in the ideal."""
    dxh, dyh = len(hx) - 1, len(hy) - 1
    C = {}
    for (a, b), c in p.items():
        C[(a, b)] = C.get((a, b), 0) + Fr(c)
    # reduce x powers
    for a in range(max((k[0] for k in C), default=0), dxh - 1, -1):
        row = {b: c for (aa, b), c in C.items() if aa == a and c != 0}
        for b, c in row.items():
            for i, h in enumerate(hx):
                key = (a - dxh + i, b)
                C[key] = C.get(key, 0) - c * h
    C = {k: v for k, v in C.items() if v != 0}
    for b in range(max((k[1] for k in C), default=0), dyh - 1, -1):
        col = {a: c for (a, bb), c in C.items() if bb == b and c != 0}
        for a, c in col.items():
            for i, h in enumerate(hy):
                key = (a, b - dyh + i)
                C[key] = C.get(key, 0) - c * h
    return {k: v for k, v in C.items() if v != 0}


def reduce_univ(p, h):
    if len(h) == 1:
        return trim(p)
    _, r = pdivmod(p, h)
    return r


def is_zero_univ(p):
    return all(v == 0 for v in p)


# ---------------------------------------------------------------- the certificate
def generators(n):
    g = []
    for m in range(4):
        g.append(add(outer(T_coeffs(n - m), T_coeffs(m)), outer(T_coeffs(m), T_coeffs(n + 1 - m), -1)))
    return g


def certificate(n, c=Fr(1, 10)):
    """Returns 2*[(1-c)/... ] scaled: here P_c := (1-c)(g1^2 - g0 g2/2) + c(g2^2 - g1 g3);
    c = 1/10 gives P_n/10 (P_n of 313)."""
    g0, g1, g2, g3 = generators(n)
    A = add(mul(g1, g1), scal(Fr(-1, 2), mul(g0, g2)))
    B = add(mul(g2, g2), scal(-1, mul(g1, g3)))
    return add(scal(1 - c, A), scal(c, B)), (g0, g1, g2, g3)


def padua_nodes(n):
    return [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]


def node_class(n, j, k):
    if 0 < j < n and 0 < k < n + 1:
        return 'int'
    if j in (0, n) and k in (0, n + 1):
        return 'corner'
    if j in (0, n):
        return 'Ex'
    return 'Ey'


def check_n(n, cvals, log):
    t0 = time.time()
    Pc, (g0, g1, g2, g3) = certificate(n)
    Pn = scal(10, Pc)                      # exactly P_n of 313
    deg = total_degree(Pn)
    top = {k: v for k, v in add(scal(9, add(mul(g1, g1), scal(Fr(-1, 2), mul(g0, g2)))), add(mul(g2, g2), scal(-1, mul(g1, g3)))).items()}
    assert top == Pn
    okD = (deg <= 2 * n + 1) and bool(Pn)
    Px, Py = dx(Pn), dy(Pn)
    Pxx, Pxy, Pyy = dx(Px), dy(Px), dy(Py)
    # parity factors
    Tn, Tn1 = T_coeffs(n), T_coeffs(n + 1)
    HX = {r: pgcd(padd(Tn, [(-1) ** r], -1), U_coeffs(n - 1)) for r in (0, 1)}
    HY = {r: pgcd(padd(Tn1, [(-1) ** r], -1), U_coeffs(n)) for r in (0, 1)}
    for r in (0, 1):
        assert len(HX[r]) - 1 == sum(1 for i in range(1, n) if i % 2 == r)
        assert len(HY[r]) - 1 == sum(1 for i in range(1, n + 1) if i % 2 == r)
    # (Z) exact double zeros
    okZ = True
    for F in (Pn, Px, Py):
        for r in (0, 1):
            if len(HX[r]) > 1 and len(HY[r]) > 1:
                okZ &= not reduce_xy(F, HX[r], HY[r])
        okZ &= is_zero_univ(reduce_univ(subs_x(F, 1), HY[0]))           # x = 1, k even
        okZ &= is_zero_univ(reduce_univ(subs_x(F, -1), HY[n % 2]))      # x = -1, k = n mod 2
        okZ &= is_zero_univ(reduce_univ(subs_y(F, 1), HX[0]))           # y = 1, j even
        okZ &= is_zero_univ(reduce_univ(subs_y(F, -1), HX[(n + 1) % 2]))  # y = -1, j = n+1 mod 2
        for (j, k) in [(0, 0), (0, n + 1), (n, 0), (n, n + 1)]:
            if (j + k) % 2 == 0:
                xv, yv = (1 if j == 0 else -1), (1 if k == 0 else -1)
                okZ &= sum(cf * Fr(xv) ** a * Fr(yv) ** b for (a, b), cf in F.items()) == 0
    # (G) boundary gradient formulas of 313, exactly, m = 0..3
    okG = True
    Tm = lambda m: T_coeffs(m)
    Um1 = lambda m: U_coeffs(m - 1) if m >= 1 else [0]
    for m, gm in enumerate((g0, g1, g2, g3)):
        gx, gy = dx(gm), dy(gm)
        # E1: x = 1, k even:  (n(n-2m) T_m(t), (n+1) U_{m-1}(t))
        okG &= is_zero_univ(reduce_univ(padd(subs_x(gx, 1), [n * (n - 2 * m) * v for v in Tm(m)], -1), HY[0]))
        okG &= is_zero_univ(reduce_univ(padd(subs_x(gy, 1), [(n + 1) * v for v in Um1(m)], -1), HY[0]))
        # E2: x = -1, k = n mod 2: (-1)^(n+m) (-n(n-2m) T_m, (n+1) U_{m-1})
        sg = (-1) ** (n + m)
        okG &= is_zero_univ(reduce_univ(padd(subs_x(gx, -1), [-sg * n * (n - 2 * m) * v for v in Tm(m)], -1), HY[n % 2]))
        okG &= is_zero_univ(reduce_univ(padd(subs_x(gy, -1), [sg * (n + 1) * v for v in Um1(m)], -1), HY[n % 2]))
        # E3: y = 1, j even: (-n U_{m-1}(t), -(n+1)(n+1-2m) T_m(t))
        okG &= is_zero_univ(reduce_univ(padd(subs_y(gx, 1), [-n * v for v in Um1(m)], -1), HX[0]))
        okG &= is_zero_univ(reduce_univ(padd(subs_y(gy, 1), [-(n + 1) * (n + 1 - 2 * m) * v for v in Tm(m)], -1), HX[0]))
        # E4: y = -1, j = n+1 mod 2: (-1)^(n+m) (n U_{m-1}, -(n+1)(n+1-2m) T_m)
        okG &= is_zero_univ(reduce_univ(padd(subs_y(gx, -1), [sg * n * v for v in Um1(m)], -1), HX[(n + 1) % 2]))
        okG &= is_zero_univ(reduce_univ(padd(subs_y(gy, -1), [-sg * (n + 1) * (n + 1 - 2 * m) * v for v in Tm(m)], -1), HX[(n + 1) % 2]))
        ev = lambda F, xv, yv: sum(cf * Fr(xv) ** a * Fr(yv) ** b for (a, b), cf in F.items())
        okG &= (ev(gx, 1, 1), ev(gy, 1, 1)) == (n * (n - 2 * m), -(n + 1) * (n + 1 - 2 * m))
        if (n + 1) % 2 == 0:   # (1,-1)
            okG &= (ev(gx, 1, -1), ev(gy, 1, -1)) == ((-1) ** m * n * (n - 2 * m), (-1) ** m * (n + 1) * (n + 1 - 2 * m))
        if n % 2 == 0:         # (-1,1)
            okG &= (ev(gx, -1, 1), ev(gy, -1, 1)) == (-(-1) ** m * n * (n - 2 * m), -(-1) ** m * (n + 1) * (n + 1 - 2 * m))
    # (H) rigorous PD at every node
    X = certified_cos_nodes(n)
    Y = certified_cos_nodes(n + 1)
    worst = None; okH = True; nfail = 0; minlam = {}
    for (j, k) in padua_nodes(n):
        xi, yi = X[j], Y[k]
        a = eval_poly2(Pxx, xi, yi); b = eval_poly2(Pxy, xi, yi); d = eval_poly2(Pyy, xi, yi)
        det = a * d - b * b
        pd = a.lo > 0 and det.lo > 0
        am, bm, dm = float(a.mid()), float(b.mid()), float(d.mid())
        lam = (am + dm) / 2 - ((((am - dm) / 2) ** 2 + bm ** 2) ** 0.5)
        cl = node_class(n, j, k)
        minlam[cl] = min(minlam.get(cl, 1e300), lam)
        if not pd:
            okH = False; nfail += 1
        if worst is None or lam < worst[0]:
            worst = (lam, j, k, cl, pd)
    log(f"n={n:2d} N={len(padua_nodes(n)):3d} deg(P_n)={deg} (<= {2*n+1}: {okD})  exact double zeros: {okZ}  "
        f"boundary gradient formulas exact: {okG}  PD at all nodes (rigorous): {okH} (fails {nfail})  "
        f"min lambda_min(Hess P_n) = {worst[0]:.4e} at (j,k)=({worst[1]},{worst[2]}) [{worst[3]}]; "
        f"per class {', '.join(f'{c}:{v:.3e}' for c, v in sorted(minlam.items()))}  ({time.time()-t0:.1f}s)")
    # (I) 312 equivalence at interior nodes, rigorous both sides
    if cvals:
        A = add(mul(g1, g1), scal(Fr(-1, 2), mul(g0, g2)))
        B = add(mul(g2, g2), scal(-1, mul(g1, g3)))
        HA = (dx(dx(A)), dy(dx(A)), dy(dy(A))); HB = (dx(dx(B)), dy(dx(B)), dy(dy(B)))
        vals = {}
        for (j, k) in padua_nodes(n):
            if node_class(n, j, k) != 'int':
                continue
            xi, yi = X[j], Y[k]
            vals[(j, k)] = ([eval_poly2(h, xi, yi) for h in HA], [eval_poly2(h, xi, yi) for h in HB],
                            (Iv(1) - xi * xi) * (Iv(1) - yi * yi))
        res = []
        for c in cvals:
            agree = undecided = npd = 0
            for (j, k), (ha, hb, ST) in vals.items():
                a, b, d = [ha[i] * (1 - c) + hb[i] * c for i in range(3)]
                det = a * d - b * b
                if a.lo > 0 and det.lo > 0:
                    pd = True
                elif a.hi < 0 or det.hi < 0:
                    pd = False
                else:
                    undecided += 1; continue
                cst = ST * c
                if cst.lo > 0 and cst.hi < Fr(1, 4):
                    crit = True
                elif cst.lo > Fr(1, 4):
                    crit = False
                else:
                    undecided += 1; continue
                agree += (pd == crit); npd += pd
            res.append(f"c={c}: agree {agree}/{len(vals)} (PD at {npd}, undecided {undecided})")
        log(f"      312 equivalence (interior nodes): " + "; ".join(res))
    return okD and okZ and okG and okH


def selftest(log):
    """Required failures: the checks must reject inputs that are wrong."""
    import mpmath as mp
    n = 5
    Pc, (g0, g1, g2, g3) = certificate(n)
    Pn = scal(10, Pc)
    Tn, Tn1 = T_coeffs(n), T_coeffs(n + 1)
    HX = {r: pgcd(padd(Tn, [(-1) ** r], -1), U_coeffs(n - 1)) for r in (0, 1)}
    HY = {r: pgcd(padd(Tn1, [(-1) ** r], -1), U_coeffs(n)) for r in (0, 1)}
    r1 = bool(reduce_xy(add(Pn, {(1, 0): 1}), HX[0], HY[0]))          # P_n + x does not vanish
    r2 = bool(reduce_xy(dx(g0), HX[0], HY[0])) is False                # d/dx g0 = n U_{n-1}(x) vanishes at interior nodes
    r3 = bool(reduce_xy(g1, HX[0], HY[1]))                             # wrong parity grid: g1 must NOT vanish there
    # interval enclosure contains the high-precision value; PD test rejects -P_n
    X, Y = certified_cos_nodes(n), certified_cos_nodes(n + 1)
    mp.mp.dps = 50
    Pxx = dx(dx(Pn))
    a = eval_poly2(Pxx, X[2], Y[2])
    xv, yv = mp.cos(2 * mp.pi / n), mp.cos(2 * mp.pi / (n + 1))
    ref = sum(mp.mpf(c.numerator) / c.denominator * xv ** i * yv ** j if isinstance(c, Fr) else c * xv ** i * yv ** j for (i, j), c in Pxx.items())
    r4 = (mp.mpf(a.lo.numerator) / a.lo.denominator <= ref <= mp.mpf(a.hi.numerator) / a.hi.denominator)
    neg = scal(-1, Pn)
    nxx, nxy, nyy = dx(dx(neg)), dy(dx(neg)), dy(dy(neg))
    aa = eval_poly2(nxx, X[1], Y[1]); bb = eval_poly2(nxy, X[1], Y[1]); dd = eval_poly2(nyy, X[1], Y[1])
    r5 = not (aa.lo > 0 and (aa * dd - bb * bb).lo > 0)
    log(f"selftest (required outcomes): P_n+x rejected {r1}; d/dx g0 accepted {r2}; g1 on odd-y/even-x grid rejected {r3}; "
        f"interval contains 50-digit value {r4}; -P_n PD-rejected {r5}")
    assert r1 and r2 and r3 and r4 and r5


def main():
    nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
    cvals = [Fr(1, 10), Fr(1, 5), Fr(3, 10), Fr(1, 2), Fr(9, 10)]
    out = []
    log = lambda s: (print(s, flush=True), out.append(s))
    log(f"padua_turan_check.py nmin={nmin} nmax={nmax}; interval grid 2^-256; node enclosures half-width 1e-45")
    selftest(log)
    allok = {}
    for n in range(nmin, nmax + 1):
        allok[n] = check_n(n, cvals, log)
    log("SUMMARY: " + ", ".join(f"n={n}:{'PASS' if v else 'FAIL'}" for n, v in allok.items()))


if __name__ == '__main__':
    main()
