#!/usr/bin/env python3
"""Independent exact rerun for L3 claims PD-T?...-305/306 and PD-N?...-301.

Reviewer: L3 adversarial reconstruction (Claude Opus 5.5, xhigh), 2026-10-31.
Written from the mathematical statements only; does NOT import any module of
tracks/bivariate-lanczos/code/L3/.  The developer's published certificates
(p* for Padua n = 3; A_i for Padua n = 1, 2) are read as DATA from the
developer's log directions/L3/logs/exact_certificates.log (sha256 printed).

Exact arithmetic: sympy's algebraic field QQ<sqrt(2)> (ANP elements) and
sympy DomainMatrix (exact rank / nullspace).  Signs of a + b*sqrt(2) are
decided exactly (squaring), and cross-checked with rational enclosures of
sqrt(2).  Ball positivity: (1) full exact Taylor expansion at every node with
a rational coefficient-sum bound on each homogeneous part (rigorous), and
(2) rigorous rational interval arithmetic on q(r, v) = p*(z + r v)/r^2 over
the boundary of the unit square of directions (|v|_inf = 1), which certifies
p* > 0 on the punctured square of half-width R (contains the disc of radius R).

Usage: python3 -I indep_exact_check.py <path to exact_certificates.log>
"""
import sys
import re
import hashlib
from fractions import Fraction as Fr
from sympy import QQ, sqrt, cos, pi, Rational
from sympy.polys.matrices import DomainMatrix

K = QQ.algebraic_field(sqrt(2))
KZ, K1 = K.zero, K.one


def k(v):
    from sympy import sympify
    return K.from_sympy(sympify(v))


def ab(e):
    """e = a + b*sqrt2 -> (a, b) as Fractions."""
    L = e.to_list()
    conv = lambda q: Fr(int(q.numerator), int(q.denominator))
    if len(L) == 0:
        return Fr(0), Fr(0)
    if len(L) == 1:
        return conv(L[0]), Fr(0)
    return conv(L[1]), conv(L[0])


def sgn(e):
    a, b = ab(e)
    sa = (a > 0) - (a < 0)
    sb = (b > 0) - (b < 0)
    if sb == 0:
        return sa
    if sa == 0:
        return sb
    if sa == sb:
        return sa
    # opposite signs: |a| vs |b| sqrt2
    return sa if a * a > 2 * b * b else sb


S2LO, S2HI = Fr(141421356237, 10 ** 11), Fr(141421356238, 10 ** 11)
assert S2LO * S2LO < 2 < S2HI * S2HI


def enclose(e):
    a, b = ab(e)
    if b >= 0:
        return a + b * S2LO, a + b * S2HI
    return a + b * S2HI, a + b * S2LO


def sgn_check(e):
    """exact sign, cross-checked against the rational enclosure."""
    s = sgn(e)
    lo, hi = enclose(e)
    if lo > 0:
        assert s == 1
    elif hi < 0:
        assert s == -1
    return s


def padua(n):
    pts = []
    for j in range(n + 1):
        for kk in range(n + 2):
            if (j + kk) % 2 == 0:
                pts.append((k(cos(j * pi / n)), k(cos(kk * pi / (n + 1)))))
    return pts


def monos(d):
    return [(a, t - a) for t in range(d + 1) for a in range(t + 1)]


def ff(m, r):
    out = 1
    for t in range(r):
        out *= (m - t)
    return out


def kpow(v, e):
    out = K1
    for _ in range(e):
        out = out * v
    return out


def deriv_at(poly, z, dx, dy):
    """poly: dict (a,b) -> K element; returns d^dx_x d^dy_y poly at z (exact)."""
    X, Y = z
    s = KZ
    for (a, b), c in poly.items():
        if a >= dx and b >= dy:
            s = s + c * k(ff(a, dx) * ff(b, dy)) * kpow(X, a - dx) * kpow(Y, b - dy)
    return s


def jet_matrix(nodes, d):
    E = monos(d)
    rows = []
    for z in nodes:
        for (dx, dy) in [(0, 0), (1, 0), (0, 1)]:
            rows.append([deriv_at({m: K1}, z, dx, dy) for m in E])
    return DomainMatrix(rows, (len(rows), len(E)), K), E


def hess(poly, z):
    return deriv_at(poly, z, 2, 0), deriv_at(poly, z, 1, 1), deriv_at(poly, z, 0, 2)


def is_pd(h):
    hxx, hxy, hyy = h
    return sgn_check(hxx) > 0 and sgn_check(hxx * hyy - hxy * hxy) > 0


def lam_min_lower(h, iters=40):
    """largest rational L (bisection) with H - L I PD, exact test."""
    hxx, hxy, hyy = h
    lo, hi = Fr(0), Fr(enclose(hxx)[1]) + 1
    for _ in range(iters):
        mid = (lo + hi) / 2
        L = k(Rational(mid.numerator, mid.denominator))
        if sgn_check(hxx - L) > 0 and sgn_check((hxx - L) * (hyy - L) - hxy * hxy) > 0:
            lo = mid
        else:
            hi = mid
    return lo


def taylor_parts(poly, z, dmax):
    """homogeneous parts of h -> poly(z + h): list over degree t of dict (a,b)->K."""
    parts = []
    for t in range(dmax + 1):
        P = {}
        for a in range(t + 1):
            b = t - a
            c = deriv_at(poly, z, a, b) * k(Rational(1, ff(a, a) * ff(b, b)))
            if c != KZ:
                P[(a, b)] = c
        parts.append(P)
    return parts


def abs_upper(e):
    lo, hi = enclose(e)
    return max(abs(lo), abs(hi))


def radius_coefsum(parts, lam_lb):
    """rigorous: p(z+h) >= lam/2 r^2 - sum_{t>=3} B_t r^t, B_t = sum |coef|; returns
    the largest dyadic-bisected R with lam/2 - sum B_t R^(t-2) > 0."""
    B = [sum((abs_upper(c) for c in P.values()), Fr(0)) for P in parts]
    g = lambda R: lam_lb / 2 - sum((B[t] * R ** (t - 2) for t in range(3, len(B))), Fr(0))
    lo, hi = Fr(0), Fr(1)
    for _ in range(40):
        mid = (lo + hi) / 2
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return lo, B, g


# ---------- rigorous rational interval arithmetic for q(r, s) on square edges ----------

def ipow(lo, hi, e):
    if e == 0:
        return Fr(1), Fr(1)
    if lo >= 0:
        return lo ** e, hi ** e
    if hi <= 0:
        a, b = (-hi) ** e, (-lo) ** e
        return (a, b) if e % 2 == 0 else (-b, -a)
    m = max(-lo, hi) ** e
    return (Fr(0), m) if e % 2 == 0 else (lo ** e, hi ** e)


def imul(a, b):
    c = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return min(c), max(c)


def q_edge_coeffs(parts, edge):
    """q(r, s) = sum_t r^(t-2) P_t(v(s)) as dict (i, j) -> (lo, hi) coefficient of r^i s^j.
    edge: 'R' v=(1,s), 'L' v=(-1,s), 'T' v=(s,1), 'B' v=(s,-1)."""
    out = {}
    for t in range(2, len(parts)):
        for (a, b), c in parts[t].items():
            lo, hi = enclose(c)
            # v_x^a v_y^b
            if edge in ('R', 'L'):
                sign = 1 if (edge == 'R' or a % 2 == 0) else -1
                key = (t - 2, b)
            else:
                sign = 1 if (edge == 'T' or b % 2 == 0) else -1
                key = (t - 2, a)
            clo, chi = (lo, hi) if sign == 1 else (-hi, -lo)
            plo, phi = out.get(key, (Fr(0), Fr(0)))
            out[key] = (plo + clo, phi + chi)
    return out


def q_lower(coeffs, r0, r1, s0, s1):
    tot_lo = Fr(0)
    for (i, j), c in coeffs.items():
        tot_lo += imul(imul(c, ipow(r0, r1, i)), ipow(s0, s1, j))[0]
    return tot_lo


def certify_square(parts, R, max_boxes=200000):
    """True if q > 0 on [0,R] x [-1,1] for all four edges (adaptive bisection)."""
    nbox = 0
    for edge in 'RLTB':
        co = q_edge_coeffs(parts, edge)
        stack = [(Fr(0), R, Fr(-1), Fr(1))]
        while stack:
            r0, r1, s0, s1 = stack.pop()
            nbox += 1
            if nbox > max_boxes:
                return False, nbox
            if q_lower(co, r0, r1, s0, s1) > 0:
                continue
            if r1 - r0 < Fr(1, 10 ** 6) and s1 - s0 < Fr(1, 10 ** 6):
                return False, nbox
            if (r1 - r0) / R >= (s1 - s0) / 2:
                rm = (r0 + r1) / 2
                stack += [(r0, rm, s0, s1), (rm, r1, s0, s1)]
            else:
                sm = (s0 + s1) / 2
                stack += [(r0, r1, s0, sm), (r0, r1, sm, s1)]
    return True, nbox


def parse_log(path):
    txt = open(path).read()
    h = hashlib.sha256(txt.encode()).hexdigest()
    # p* coefficients
    pstar = {}
    sec = txt.split('p* monomial coefficients')[1].split('node 0')[0]
    for m in re.finditer(r"x\^(\d+) y\^(\d+): \((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r2\)", sec):
        a, b = int(m.group(1)), int(m.group(2))
        pstar[(a, b)] = k(Rational(m.group(3)) + Rational(m.group(4)) * sqrt(2))
    # A_i for n = 1, 2
    certs = {}
    for n in (1, 2):
        blk = txt.split(f'Padua n={n}:')[1].split('=> (H)')[0]
        A = []
        for m in re.finditer(r"A = \[\[\((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r2\),\((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r2\)\],"
                             r"\[\((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r2\),\((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r2\)\]\]", blk):
            g = [Rational(v) for v in m.groups()]
            e11 = k(g[0] + g[1] * sqrt(2)); e12 = k(g[2] + g[3] * sqrt(2))
            e21 = k(g[4] + g[5] * sqrt(2)); e22 = k(g[6] + g[7] * sqrt(2))
            assert e12 == e21
            A.append((e11, e12, e22))
        certs[n] = A
    return h, pstar, certs


def s1_basis(nodes, d):
    J, E = jet_matrix(nodes, d)
    rk = J.rank()
    ns = J.nullspace().to_Matrix()          # exact, sympy expressions in sqrt(2)
    basis = []
    for i in range(ns.rows):
        r = [k(ns[i, c]) for c in range(ns.cols)]
        basis.append({E[c]: v for c, v in enumerate(r) if v != KZ})
    # exact verification that every basis vector annihilates the jet matrix
    for p in basis:
        for z in nodes:
            assert deriv_at(p, z, 0, 0) == KZ and deriv_at(p, z, 1, 0) == KZ and deriv_at(p, z, 0, 1) == KZ
    assert len(basis) == len(E) - rk
    return basis, rk, E


def hess_map_rank(basis, nodes):
    rows = []
    for z in nodes:
        H = [hess(p, z) for p in basis]
        for q in range(3):
            rows.append([H[c][q] for c in range(len(basis))])
    return DomainMatrix(rows, (len(rows), len(basis)), K).rank()


def check_dual(n, A):
    nodes = padua(n)
    d = 2 * n + 1
    basis, rk, E = s1_basis(nodes, d)
    hr = hess_map_rank(basis, nodes)
    print(f"[dual n={n}] M={len(nodes)} dim Pi_{d}={len(E)} rank J={rk} dim S1={len(basis)} "
          f"(n(n+1)/2={n*(n+1)//2}) rank Hess|S1={hr} injective={hr == len(basis)}")
    assert len(A) == len(nodes)
    allzero = True
    for p in basis:
        s = KZ
        for z, (a11, a12, a22) in zip(nodes, A):
            hxx, hxy, hyy = hess(p, z)
            s = s + a11 * hxx + k(2) * a12 * hxy + a22 * hyy
        allzero &= (s == KZ)
    pd = [is_pd(Ai) for Ai in A]
    lam = [float(lam_min_lower(Ai)) for Ai in A]
    print(f"   sum_i <A_i, Hess p(z_i)> = 0 for every S1 basis element: {allzero}; "
          f"A_i PD: {pd}; min lam_min(A_i) >= {min(lam):.6g}")
    ok = allzero and all(pd) and hr == len(basis)
    print(f"   => dual certificate for (H) at Padua n={n}: {'PASS' if ok else 'FAIL'}")
    return ok, basis, nodes


def check_n1_structure():
    nodes = padua(1)
    (x1, y1), (x2, y2), (x3, y3) = nodes
    # l_ij(x,y) = (y_j - y_i)(x - x_i) - (x_j - x_i)(y - y_i) as polynomial dict
    def line(zi, zj):
        (xi, yi), (xj, yj) = zi, zj
        return {(1, 0): yj - yi, (0, 1): -(xj - xi), (0, 0): -(yj - yi) * xi + (xj - xi) * yi}

    def mul(p, q):
        out = {}
        for (a, b), c in p.items():
            for (a2, b2), c2 in q.items():
                out[(a + a2, b + b2)] = out.get((a + a2, b + b2), KZ) + c * c2
        return {m: c for m, c in out.items() if c != KZ}
    cub = mul(mul(line(nodes[0], nodes[1]), line(nodes[0], nodes[2])), line(nodes[1], nodes[2]))
    basis, rk, E = s1_basis(nodes, 3)
    # cub in span(basis)? basis has 1 element; compare proportionality
    b0 = basis[0]
    ratio = None
    prop = True
    for m in set(cub) | set(b0):
        c1, c2 = cub.get(m, KZ), b0.get(m, KZ)
        if c2 == KZ:
            prop &= (c1 == KZ)
        else:
            r = c1 / c2
            prop &= (ratio is None or r == ratio)
            ratio = r
    hs = []
    for z in nodes:
        hxx, hxy, hyy = hess(cub, z)
        hs.append(sgn_check(hxx * hyy - hxy * hxy))
    print(f"[n=1 structure] dim S1={len(basis)}; S1 = span(l12 l13 l23): {prop}; "
          f"sign det Hess at the 3 nodes: {hs} (all -1 => indefinite)")


def main():
    path = sys.argv[1]
    h, pstar, certs = parse_log(path)
    print(f"certificate source: {path}\n  sha256 {h}")
    print(f"sympy field: {K}")
    # ---------------- n = 1 and n = 2 dual certificates ----------------
    check_n1_structure()
    check_dual(1, certs[1])
    check_dual(2, certs[2])
    # ---------------- n = 3 primal certificate p* ----------------
    n = 3
    nodes = padua(n)
    print(f"[primal n=3] p* has {len(pstar)} nonzero monomials; total degree = "
          f"{max(a + b for (a, b) in pstar)}; all coefficients rational: "
          f"{all(ab(c)[1] == 0 for c in pstar.values())}; even in y: {all(b % 2 == 0 for (a, b) in pstar)}")
    vals = [deriv_at(pstar, z, 0, 0) == KZ for z in nodes]
    grads = [deriv_at(pstar, z, 1, 0) == KZ and deriv_at(pstar, z, 0, 1) == KZ for z in nodes]
    H = [hess(pstar, z) for z in nodes]
    pds = [is_pd(hh) for hh in H]
    lams = [lam_min_lower(hh) for hh in H]
    print(f"   p*(z_i) = 0 exactly at all 10 nodes: {all(vals)}; grad p*(z_i) = 0: {all(grads)}; "
          f"Hess p*(z_i) PD (exact): {all(pds)} {pds}")
    for z, hh, lm in zip(nodes, H, lams):
        print(f"     node ({float(K.to_sympy(z[0])):+.4f},{float(K.to_sympy(z[1])):+.4f}): "
              f"hxx={K.to_sympy(hh[0])}, hxy={K.to_sympy(hh[1])}, hyy={K.to_sympy(hh[2])}, lam_min >= {float(lm):.6g}")
    basis, rk, E = s1_basis(nodes, 2 * n + 1)
    hr = hess_map_rank(basis, nodes)
    print(f"   exact S1 for Padua n=3: rank J={rk}, dim S1={len(basis)}, rank Hess|S1={hr}")
    # ---------------- rigorous radii ----------------
    dev_d0 = Fr(30117029139000, 77370908310949543)
    Rs = []
    gmins = []
    for z, lm in zip(nodes, lams):
        parts = taylor_parts(pstar, z, 7)
        assert all(c == KZ for c in parts[0].values()) and all(c == KZ for c in parts[1].values())
        R, B, g = radius_coefsum(parts, lm)
        Rs.append(R)
        gmins.append(g(dev_d0))
    print(f"   rigorous radius (coefficient-sum Taylor bound, full expansion): min_i R_i = {float(min(Rs)):.6g} "
          f"(per node: {[round(float(r), 5) for r in Rs]})")
    print(f"   developer delta_0 = {dev_d0} ~ {float(dev_d0):.6g}: lam/2 - sum B_t d0^(t-2) > 0 at every node: "
          f"{all(gv > 0 for gv in gmins)} => p* >= 0 on all closed balls B(z_i, delta_0): "
          f"{all(gv > 0 for gv in gmins) and dev_d0 <= min(Rs)}")
    for Rtry in (Fr(1, 50), Fr(3, 100), Fr(4, 100)):
        res = []
        for z in nodes:
            parts = taylor_parts(pstar, z, 7)
            ok, nb = certify_square(parts, Rtry)
            res.append((ok, nb))
        print(f"   interval certificate p* > 0 on punctured squares |h|_inf <= {float(Rtry)} (contain discs of that radius): "
              f"{all(r[0] for r in res)}  boxes per node {[r[1] for r in res]}")
    # an explicit perturbation point zeta with p*(zeta) > 0
    zeta = (nodes[0][0] - k(Rational(1, 100)), nodes[0][1])
    pz = deriv_at(pstar, zeta, 0, 0)
    print(f"   example zeta = node0 + (-0.01, 0) = {K.to_sympy(zeta[0])},{K.to_sympy(zeta[1])}: p*(zeta) = "
          f"{K.to_sympy(pz)} (sign {sgn_check(pz)}); zeta lies in K_delta0? "
          f"{Fr(1, 100) <= dev_d0}")


if __name__ == '__main__':
    main()
