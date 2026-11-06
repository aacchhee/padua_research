#!/usr/bin/env python3
"""Independent exact checks of the P5 Padua admission (auditor-authored).

Arithmetic: group ring Q[Z/2L] reduced modulo the cyclotomic polynomial
Phi_{2L}, with zeta = exp(i*pi/L), L = m(m+1).  cos(t*pi/L) = (z^t+z^-t)/2.
Exact zero tests by reduction; nonzero signs certified by arb evaluation.
Does not reuse the developer's code.
"""
import json, sys, time
from fractions import Fraction as Fr
from math import comb
from flint import fmpq_poly, fmpq, arb, ctx, fmpz_poly

ctx.prec = 300


def cyclotomic(n):
    # Phi_n via fmpz_poly
    return fmpq_poly(fmpz_poly.cyclotomic(n).coeffs())


class Field:
    def __init__(self, L):
        self.L = L
        self.N = 2 * L
        self.phi = cyclotomic(self.N)

    def vec(self):
        return [Fr(0)] * self.N

    def cosvec(self, t, c=Fr(1)):
        v = self.vec()
        v[t % self.N] += c / 2
        v[(-t) % self.N] += c / 2
        return v

    def reduce(self, v):
        p = fmpq_poly([fmpq(x.numerator, x.denominator) for x in v])
        return p % self.phi

    def is_zero(self, v):
        return self.reduce(v) == 0

    def equals_const(self, v, c):
        w = list(v)
        w[0] -= Fr(c)
        return self.is_zero(w)

    def numeric(self, v):
        # real value: sum c_t cos(t pi/L) (v is symmetric in our use, but take real part anyway)
        s = arb(0)
        for t, c in enumerate(v):
            if c:
                s += arb(fmpq(c.numerator, c.denominator)) * (arb.pi() * t / self.L).cos()
        return s

    def mul(self, u, v):
        w = self.vec()
        nzu = [(i, a) for i, a in enumerate(u) if a]
        nzv = [(j, b) for j, b in enumerate(v) if b]
        for i, a in nzu:
            for j, b in nzv:
                w[(i + j) % self.N] += a * b
        return w

    def add(self, u, v, c=Fr(1)):
        return [a + c * b for a, b in zip(u, v)]

    def sign(self, v):
        if self.is_zero(v):
            return 0
        x = self.numeric(v)
        if x > 0:
            return 1
        if x < 0:
            return -1
        raise RuntimeError("uncertified sign")


def padua(m):
    lam = lambda j, r: Fr(1, 2 * r) if j in (0, r) else Fr(1, r)
    nodes = []
    for j in range(m + 1):
        for k in range(m + 2):
            if (j + k) % 2 == 0:
                nodes.append((j, k, 2 * lam(j, m) * lam(k, m + 1)))
    return nodes


def check_order(m):
    L = m * (m + 1)
    F = Field(L)
    nodes = padua(m)
    M = len(nodes)
    out = {"m": m, "M": M, "N_m": (m + 1) * (m + 2) // 2}
    assert M == out["N_m"]
    assert sum(w for _, _, w in nodes) == 1 and all(w > 0 for _, _, w in nodes)
    tx = lambda j: (m + 1) * j  # x_j = cos(tx*pi/L)
    ty = lambda k: m * k

    # moments nu(T_a(x)T_b(y)) = sum w cos(a*tx) cos(b*ty), exactly, a+b<=2m+1
    def moment(a, b, parity_only=None):
        v = F.vec()
        for j, k, w in nodes:
            # cos A cos B = (cos(A+B)+cos(A-B))/2
            A, B = a * tx(j), b * ty(k)
            for t in (A + B, A - B):
                v[t % F.N] += w / 4
                v[(-t) % F.N] += w / 4
        return v

    def moment_discrete_product(a, b):
        lam = lambda j, r: Fr(1, 2 * r) if j in (0, r) else Fr(1, r)
        v = F.vec()
        for j in range(m + 1):
            for k in range(m + 2):
                w = lam(j, m) * lam(k, m + 1)
                A, B = a * tx(j), b * ty(k)
                for t in (A + B, A - B):
                    v[t % F.N] += w / 4
                    v[(-t) % F.N] += w / 4
        return v

    fails = {}
    dp_fails = {}
    count = 0
    for d in range(0, 2 * m + 2):
        for a in range(d + 1):
            b = d - a
            v = moment(a, b)
            target = 1 if a == b == 0 else 0
            ok = F.equals_const(v, target)
            # formula (1)
            A = lambda aa, r: 1 if aa % (2 * r) == 0 else 0
            Bf = lambda aa, r: 1 if aa % (2 * r) == r else 0
            pred = A(a, m) * A(b, m + 1) + Bf(a, m) * Bf(b, m + 1)
            assert F.equals_const(v, pred), (m, a, b)
            count += 1
            if not ok:
                fails.setdefault(d, []).append((a, b))
            vd = moment_discrete_product(a, b)
            if not F.is_zero(F.add(v, vd, Fr(-1))):
                dp_fails.setdefault(d, []).append((a, b))
    out["moments_checked_deg_le_2m+1"] = count
    out["continuous_failures_by_degree"] = {str(k): v for k, v in fails.items()}
    out["discrete_product_failures_by_degree"] = {str(k): v for k, v in dp_fails.items()}
    assert min(fails) == 2 * m and fails[2 * m] == [(2 * m, 0)]
    assert min(dp_fails) == 2 * m + 1

    # convex hull, exact predicates. point coords as vectors.
    pts = [(j, k, F.cosvec(tx(j)), F.cosvec(ty(k))) for j, k, _ in nodes]
    # sort by x ascending (j descending), then y ascending (k descending)
    pts.sort(key=lambda p: (-p[0], -p[1]))

    def orient(o, a, b):
        ax = F.add(a[2], o[2], Fr(-1)); ay = F.add(a[3], o[3], Fr(-1))
        bx = F.add(b[2], o[2], Fr(-1)); by = F.add(b[3], o[3], Fr(-1))
        return F.sign(F.add(F.mul(ax, by), F.mul(ay, bx), Fr(-1)))

    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    out["hull_vertices"] = len(hull)
    out["hull_vertex_indices_jk"] = [(p[0], p[1]) for p in hull]
    # parallelogram check: are opposite sides parallel? (only relevant if 4)
    return out, F, nodes


def gram_and_witness(m, F, nodes):
    """Exact Gram of q_ab=p_a(x)p_b(y) for a+b<=s, s=m-1 and s=m; normality of T_m(x)."""
    L = m * (m + 1)
    tx = lambda j: (m + 1) * j
    ty = lambda k: m * k
    res = {}

    def pnorm(a):
        return Fr(1) if a == 0 else Fr(2)  # p_a^2 = 2 T_a^2 ; use squared factor

    # inner product <p_a p_b, p_c p_d> = c_ac c_bd * nu(T_a T_c(x) T_b T_d(y)) with c = sqrt2 factors
    # products of T: T_a T_c = (T_{a+c}+T_{|a-c|})/2. Use moment closed formula via exact sum instead.
    def nu_TT(a, c, b, d):
        v = F.vec()
        for j, k, w in nodes:
            for A in ((a + c) * tx(j), (a - c) * tx(j)):
                for B in ((b + d) * ty(k), (b - d) * ty(k)):
                    for t in (A + B, A - B):
                        v[t % F.N] += w / 16
                        v[(-t) % F.N] += w / 16
        return v

    import math
    for s in (m - 1, m):
        idx = [(dd - b, b) for dd in range(s + 1) for b in range(dd + 1)]
        bad = 0
        for i, (a, b) in enumerate(idx):
            for (c, d) in idx[: i + 1]:
                # scale factor: sqrt(2)^{[a>0]+[b>0]+[c>0]+[d>0]} -> must be rational on diagonal
                k = (a > 0) + (b > 0) + (c > 0) + (d > 0)
                v = nu_TT(a, c, b, d)
                target = 1 if (a, b) == (c, d) else 0
                # value = 2^{k/2} * v ; test 2^{k/2} v == target
                if k % 2 == 0:
                    vv = [x * 2 ** (k // 2) for x in v]
                    ok = F.equals_const(vv, target)
                else:
                    ok = F.is_zero(v) and target == 0
                bad += (not ok)
        res[f"gram_s={s}_entries"] = len(idx) * (len(idx) + 1) // 2
        res[f"gram_s={s}_mismatches"] = bad
    # normality of e_m = T_m(x) to Pi_s (s=m-1): nu(T_m(x) T_a(x) T_b(y)) = 0 for a+b<=m-1
    s = m - 1
    nbad = 0
    for dd in range(s + 1):
        for a in range(dd + 1):
            b = dd - a
            v = F.vec()
            for j, k, w in nodes:
                for A in ((m + a) * tx(j), (m - a) * tx(j)):
                    B = b * ty(k)
                    for t in (A + B, A - B):
                        v[t % F.N] += w / 8
                        v[(-t) % F.N] += w / 8
            nbad += not F.is_zero(v)
    res["e_m_normal_to_Pi_s_mismatches"] = nbad
    # e_m norm and readouts nu(T_m^2 U_{a-1}(x)), U_{a-1}(cos t)=sum_{i} cos((a-1-2i) t)
    readouts = []
    for a in range(1, s + 1):
        v = F.vec()
        for j, k, w in nodes:
            for i in range(a):
                fr = (a - 1 - 2 * i)
                for base in (2 * m + fr, fr, -2 * m + fr):  # T_m^2 = (1+T_2m)/2 times exp sum
                    coef = w * (Fr(1, 2) if base == fr else Fr(1, 4))
                    t = base * tx(j)
                    v[t % F.N] += coef / 2
                    v[(-t) % F.N] += coef / 2
        val = 1 if F.equals_const(v, 1) else (0 if F.is_zero(v) else None)
        readouts.append(val)
    res["readouts_e_m^T V_a0"] = readouts
    assert readouts == [1 if a % 2 else 0 for a in range(1, s + 1)]
    return res


def main():
    t0 = time.monotonic()
    rows = []
    for m in range(1, 8):
        out, F, nodes = check_order(m)
        if m >= 2:
            out.update(gram_and_witness(m, F, nodes))
        rows.append(out)
        print(json.dumps(out), flush=True)
    expect = {1: 3, 2: 5}
    for r in rows:
        assert r["hull_vertices"] == expect.get(r["m"], 6), r
    json.dump({"rows": rows, "elapsed": time.monotonic() - t0}, open(sys.argv[1], "w"), indent=1)
    print("ALL PASS", time.monotonic() - t0)


if __name__ == "__main__":
    main()
