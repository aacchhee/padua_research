#!/usr/bin/env python3
"""Independent rigorous check of the gamma_1 certificate for the DGOV octahedron function.

Written from the task specification only (independent code path; no other
project certificate code was read).

Input
-----
`octa_double.func.cpp` from the arXiv ancillary files of Dostert, Guzman,
de Oliveira Filho, Vallentin, arXiv:1510.02331v3 (third-party; not committed).
It defines P(x) = sum c_ijk s1^i s2^j s3^k with s1 = x^2+y^2+z^2,
s2 = x^4+y^4+z^4, s3 = x^6+y^6+z^6.  The decimal literals c_ijk are read as
EXACT rationals.  The parser checks the full structure of the function body
(the s1,s2,s3 definitions, the power recurrences, and that every accumulation
line is exactly `ret += c_i_j_k * x_pow[i] * y_pow[j] * z_pow[k];`).

Claims checked
--------------
 (G) G(u) >= 0 on R^3, where fhat(u) = G(u) exp(-pi|u|^2) for
     f(x) = P(x) exp(-pi|x|^2), fhat(u) = int f(x) exp(-2 pi i u.x) dx.
 (P) P(x) <= 0 for all x in R^3 with |x|_1 >= alpha := 1001/1000.
 (V) an enclosure of gamma_1 := 6 G(0) / (alpha^3 P(0)) - 1, compared with 1/36.

Derivation of G (exact)
-----------------------
In one variable FT[x^n e^{-pi x^2}](u) = (i/(2pi))^n d^n/du^n e^{-pi u^2}
= (-i/(2 sqrt(pi)))^n H_n(sqrt(pi) u) e^{-pi u^2} (physicists' Hermite H_n).
For n = 2m this gives g_m(u) e^{-pi u^2} with
    g_m(u) = sum_{l=0}^m (-1)^l (2m)! / ((2l)! (m-l)!) (4 pi)^{l-m} u^{2l}.
Since exp(-pi|x|^2) and e^{-2 pi i u.x} factor over coordinates,
P = sum p_ijk x^{2i} y^{2j} z^{2k} gives G(u) = sum p_ijk g_i(u1) g_j(u2) g_k(u3).
Coefficients of G are rational combinations of (4 pi)^{-d}, evaluated in arb
ball arithmetic (python-flint) at 256 bits and converted to a double plus a
rigorous radius (exact dyadic arithmetic on the arb midpoint/radius).
The formula is sanity-checked numerically (1D quadrature of the transform and a
3D Gauss-Hermite evaluation of fhat at sample points); these checks are not
part of the proof.

Symmetry reduction (proved)
---------------------------
P depends only on (s1,s2,s3), hence is invariant under coordinate permutations
and sign changes.  The exact monomial coefficient tensor p_ijk is checked to be
permutation symmetric, so G (same 1D map on each axis, even g_m) has the same
symmetry.  |x|_1 is invariant too.  It therefore suffices to treat the
fundamental region F = {x >= y >= z >= 0}.

Enclosure method (rigorous): tensor Bernstein bounds with a floating-point
error bound
-----------------------------------------------------------------------------
For a box [x0,x1]x[y0,y1]x[z0,z1] with x0,y0,z0 >= 0 the Bernstein
coefficients (degree n = 26 per axis) of a monomial t^m on [t0,t0+w] are
    B[m,l] = sum_{r<=min(l,m)} C(l,r) C(m,r)/C(n,r) t0^{m-r} w^r >= 0,
a sum of nonnegative terms, increasing in l with B[m,n] = (t0+w)^m.  The
Bernstein coefficients of the polynomial are
b[l1,l2,l3] = sum c[m1,m2,m3] B1[m1,l1] B2[m2,l2] B3[m3,l3], and
min b <= poly(box) <= max b (convex hull property).

Floating point (IEEE double, round to nearest, u = 2^-53, gamma_k = ku/(1-ku)):
box endpoints are dyadic multiples of 2^-40 below 8, so w = t1 - t0 is exact.
Each B entry is computed with relative error <= gamma_55 (all terms
nonnegative; <= 29 roundings per term, <= 26 additions).  The contraction is
three (two in 2D) batched matrix products of length <= 27; for any summation
order (BLAS, FMA allowed) a length-k dot product has error <= gamma_k * sum|terms|.
Propagating through the stages (B1,B2,B3 >= 0) gives
    |b_computed - b(c_float)| <= 3 (gamma_27 + gamma_56) A + u A <= 2.9e-14 A,
    A := sum |c| B1 B2 B3 <= sum |c| x1^m1 y1^m2 z1^m3 =: Cabs(hi corner).
The coefficient error |c - c_float| <= rho contributes <= sum rho * hi^m.
We use E := 1e-13 * Cabs_computed(hi) + 1.01 * Rho_computed(hi) + 1e-250,
where computed nonnegative sums of length <= 27^3 are >= (1 - 3e-12) times
exact.  Underflow: in the default IEEE environment (gradual underflow, which
numpy/OpenBLAS use) each product carries an extra absolute error <= 2^-1075
(additions are exact on underflow).  Such an error is later multiplied by at
most max|c| * max(1, max hi)^(sum of axis degrees), asserted <= 1e60 per call,
and there are < 1e7 such operations per box, so all underflow effects
(including on Cabs, Rho) are < 1e-256 < 1e-250.  Widths >= 2^-30 (asserted).
A box is VERIFIED for (P) if max b + E < 0 and for (G) if min b - E > 0.

Unbounded parts (proved reduction to finite checks)
---------------------------------------------------
Bounded/unbounded split by the max coordinate x of a point in F.
Tail x >= R: write the point as r (1,v,w), r >= R, 0 <= w <= v <= 1.  With
homogeneous parts P = sum_d P_d (deg 2d) and r^2 = R^2 (1+t), t >= 0:
    P(r(1,v,w)) = sum_n t^n K_n(v,w),  K_n = sum_{d>=n} C(d,n) R^{2d} P_d(1,v,w).
If every K_n < 0 on [0,1]^2 then P < 0 on the whole tail.  Each K_n is a
bivariate polynomial (exact rational coefficients) checked by the same
Bernstein method in 2D.  Same for G with K_n > 0.

Chart near the face |x|_1 = alpha (slab): for the part of F with
alpha <= x+y+z <= alpha + 1/8, use coordinates (sig, y, z) with
x = sig + alpha - y - z, sig in [0, 1/8], y,z >= 0.  Every point with sig >= 0
and y,z >= 0 has |x|_1 >= x+y+z >= alpha, so these boxes lie in the domain
(no straddling of the face).  Q(sig,y,z) = P(sig+alpha-y-z, y, z) is expanded
exactly in rationals.  The rest of F with x+y+z >= alpha + 1/8 and x <= R is
covered by x-space boxes in [0,R]^3; a box there is verified only if P < 0 on
the whole box (so boxes may straddle x+y+z = alpha + 1/8).

Coverage: initial boxes tile the chart rectangles; a box is discarded only if
a necessary condition for meeting the target set fails (x1 >= y0, y1 >= z0,
x1+y1+z1 >= s_c in x-space; y1 >= z0, s1 - 2 y0 - z0 >= 0 in the slab chart);
unverified boxes are bisected along every axis.

gamma_1 is computed in arb from exact rationals and pi:
G(0) = sum p_ijk prod_axes (2m)!/m! (4 pi)^{-m}.

Usage
-----
    python3 -I gamma_certificate_indep.py --input /path/octa_double.func.cpp \
        --out evidence/gamma-certificate-indep.json [--R 3] [--RG 3]
"""
import argparse
import hashlib
import json
import math
import platform
import re
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import flint
from flint import arb, fmpq, ctx

EXPECTED_SHA = "034a1aea4fafbf29743bded0812723ac8c9cf95274225213578145d016a7bc47"
ALPHA = Fr(1001, 1000)
NDEG = 26
KAPPA = 1e-13
ABS_UNDERFLOW = 1e-250
DYADIC = 2.0 ** 40
MIN_WIDTH = 2.0 ** -30

# ---------------------------------------------------------------- parsing


def parse(path):
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    src = raw.decode("ascii")
    lines = [ln.strip() for ln in src.splitlines() if ln.strip()]
    C = {}
    acc = []
    other = []
    rc = re.compile(r"^static const double c_(\d+)_(\d+)_(\d+) = (-?\d+\.\d+(?:[eE][-+]?\d+)?);$")
    ra = re.compile(r"^ret \+= c_(\d+)_(\d+)_(\d+) \* x_pow\[(\d+)\] \* y_pow\[(\d+)\] \* z_pow\[(\d+)\];$")
    for ln in lines:
        m = rc.match(ln)
        if m:
            key = (int(m[1]), int(m[2]), int(m[3]))
            assert key not in C
            C[key] = Fr(m[4])
            continue
        m = ra.match(ln)
        if m:
            i, j, k, a, b, c = map(int, m.groups())
            assert (i, j, k) == (a, b, c), ln
            acc.append((i, j, k))
            continue
        other.append(ln)
    expected_other = [
        "double __OctaDoubleFunction(const double& x, const double& y, const double& z) {",
        "double s1 = x * x + y * y + z * z;",
        "double s2 = x * x * x * x + y * y * y * y + z * z * z * z;",
        "double s3 = x * x * x * x * x * x + y * y * y * y * y * y + z * z * z * z * z * z;",
        "double x_pow[14], y_pow[7], z_pow[5];",
    ]
    for nm, s, top in (("x", "s1", 13), ("y", "s2", 6), ("z", "s3", 4)):
        expected_other.append("%s_pow[0] = 1;" % nm)
        for t in range(1, top + 1):
            expected_other.append("%s_pow[%d] = %s_pow[%d] * %s;" % (nm, t, nm, t - 1, s))
    expected_other += ["double ret = 0;", "return ret;", "}"]
    assert other == expected_other, "unexpected structure in input"
    assert sorted(acc) == sorted(C) and len(acc) == len(set(acc)), "accumulation mismatch"
    return sha, C


def expand_squares(C):
    """p[(i,j,k)]: coefficient of x^{2i} y^{2j} z^{2k} (exact)."""
    def mul(A, B):
        R = {}
        for ka, va in A.items():
            for kb, vb in B.items():
                key = (ka[0] + kb[0], ka[1] + kb[1], ka[2] + kb[2])
                R[key] = R.get(key, 0) + va * vb
        return R
    base = {t: {(t, 0, 0): 1, (0, t, 0): 1, (0, 0, t): 1} for t in (1, 2, 3)}
    pw = {}
    for t in (1, 2, 3):
        cur = {(0, 0, 0): 1}
        for n in range(14):
            pw[(t, n)] = cur
            cur = mul(cur, base[t])
    p = {}
    for (i, j, k), c in C.items():
        T = mul(mul(pw[(1, i)], pw[(2, j)]), pw[(3, k)])
        for key, v in T.items():
            p[key] = p.get(key, Fr(0)) + c * v
    return {k: v for k, v in p.items() if v != 0}


# ---------------------------------------------------- float conversion helpers


def fr_to_float_rad(q):
    f = float(q)
    err = abs(Fr(f) - q)
    return f, float(err) * (1 + 2.0 ** -50)


def arb_to_float_rad(x):
    m, e = x.mid().man_exp()
    rm, re_ = x.rad().man_exp()
    mid = Fr(int(m)) * (Fr(2) ** int(e))
    rad = Fr(int(rm)) * (Fr(2) ** int(re_))
    f = float(mid)
    err = abs(Fr(f) - mid) + rad
    return f, float(err) * (1 + 2.0 ** -50) + 1e-300


# ------------------------------------------------------------ Bernstein core


def wmat(exps, n):
    W = np.zeros((len(exps), n + 1, n + 1))
    for a, m in enumerate(exps):
        for l in range(n + 1):
            for r in range(min(l, m) + 1):
                W[a, l, r] = float(Fr(math.comb(l, r) * math.comb(m, r), math.comb(n, r)))
    return W


class Bern:
    """Rigorous Bernstein bounds for sum c[a,b,(c)] t1^E1[a] t2^E2[b] (t3^E3[c])."""

    def __init__(self, coef, rad, exps, n=NDEG):
        self.c = np.asarray(coef, dtype=float)
        self.cabs = np.abs(self.c)
        self.rho = np.asarray(rad, dtype=float)
        self.exps = [np.asarray(e) for e in exps]
        self.dim = len(exps)
        self.n = n
        self.W = [wmat(list(e), n) for e in exps]
        self.emax = [int(max(e)) for e in exps]
        self.cmax = float(np.max(self.cabs + self.rho))

    def _B(self, t0, w, ax):
        e = self.exps[ax]
        n = self.n
        N = t0.shape[0]
        p0 = np.ones((N, n + 1))
        pw = np.ones((N, n + 1))
        for k in range(1, n + 1):
            p0[:, k] = p0[:, k - 1] * t0
            pw[:, k] = pw[:, k - 1] * w
        Pw = np.zeros((N, len(e), n + 1))
        for a, m in enumerate(e):
            for r in range(m + 1):
                Pw[:, a, r] = p0[:, m - r] * pw[:, r]
        return np.einsum("nmr,mlr->nml", Pw, self.W[ax])

    def _hipow(self, t1, ax):
        e = self.exps[ax]
        p = np.ones((t1.shape[0], self.emax[ax] + 1))
        for k in range(1, self.emax[ax] + 1):
            p[:, k] = p[:, k - 1] * t1
        return p[:, e]

    def bounds(self, lo, hi):
        """Return (lower, upper) rigorous bounds per box. lo, hi: (N, dim)."""
        assert np.all(lo >= 0) and np.all(hi > lo)
        assert np.all(np.floor(lo * DYADIC) == lo * DYADIC) and np.all(np.floor(hi * DYADIC) == hi * DYADIC)
        assert np.all(hi <= 8)
        w = hi - lo
        assert np.all(w >= MIN_WIDTH)
        # multiplier bound for gradual-underflow error propagation (see module docstring)
        assert self.cmax * max(1.0, float(hi.max())) ** sum(self.emax) <= 1e60
        N = lo.shape[0]
        Bs = [self._B(lo[:, d], w[:, d], d) for d in range(self.dim)]
        L = self.n + 1
        if self.dim == 3:
            I, J, K = self.c.shape
            T1 = np.matmul(self.c.reshape(1, I * J, K), Bs[2])            # (N, I*J, L)
            T1 = T1.reshape(N, I, J, L)
            T2 = np.matmul(np.transpose(Bs[1], (0, 2, 1))[:, None], T1)    # (N, I, L, L)
            T3 = np.matmul(np.transpose(Bs[0], (0, 2, 1)), T2.reshape(N, I, L * L))  # (N, L, L*L)
            bmax = T3.max(axis=(1, 2))
            bmin = T3.min(axis=(1, 2))
            h = [self._hipow(hi[:, d], d) for d in range(3)]
            A = np.einsum("ijk,ni,nj,nk->n", self.cabs, h[0], h[1], h[2])
            Rr = np.einsum("ijk,ni,nj,nk->n", self.rho, h[0], h[1], h[2])
        else:
            I, J = self.c.shape
            T1 = np.matmul(self.c.reshape(1, I, J), Bs[1])                  # (N, I, L)
            T2 = np.matmul(np.transpose(Bs[0], (0, 2, 1)), T1)             # (N, L, L)
            bmax = T2.max(axis=(1, 2))
            bmin = T2.min(axis=(1, 2))
            h = [self._hipow(hi[:, d], d) for d in range(2)]
            A = np.einsum("ij,ni,nj->n", self.cabs, h[0], h[1])
            Rr = np.einsum("ij,ni,nj->n", self.rho, h[0], h[1])
        E = KAPPA * A + 1.01 * Rr + ABS_UNDERFLOW
        assert np.all(np.isfinite(bmax)) and np.all(np.isfinite(E))
        return bmin - E, bmax + E


def run_bb(bern, lo0, hi0, relevant, sign, batch=400, max_depth=24, max_boxes=5_000_000,
           log=None, label=""):
    """Branch and bound. sign=-1: prove poly < 0 on all relevant boxes; sign=+1: poly > 0.
    Returns a stats dict.  If some box cannot be verified within max_depth / max_boxes,
    returns ok=False with the failing box of worst bound (for an exact witness test)."""
    t0 = time.time()
    keep = relevant(lo0, hi0)
    pending_lo, pending_hi = lo0[keep], hi0[keep]
    pending_d = np.zeros(int(keep.sum()), dtype=int)
    verified = processed = maxdepth = 0
    worst = -np.inf if sign < 0 else np.inf
    lastlog = time.time()
    while pending_lo.shape[0]:
        lo, hi, d = pending_lo[-batch:], pending_hi[-batch:], pending_d[-batch:]
        pending_lo, pending_hi, pending_d = pending_lo[:-batch], pending_hi[:-batch], pending_d[:-batch]
        lb, ub = bern.bounds(lo, hi)
        processed += lo.shape[0]
        ok = (ub < 0) if sign < 0 else (lb > 0)
        verified += int(ok.sum())
        if ok.any():
            worst = max(worst, float(ub[ok].max())) if sign < 0 else min(worst, float(lb[ok].min()))
        bad = ~ok
        if bad.any():
            blo, bhi, bd = lo[bad], hi[bad], d[bad]
            if bd.max() >= max_depth or processed >= max_boxes:
                score = ub[bad] if sign < 0 else -lb[bad]
                j = int(np.argmax(score))
                return {"ok": False, "label": label, "processed": processed,
                        "reason": "max_depth" if bd.max() >= max_depth else "max_boxes",
                        "fail_box_lo": blo[j].tolist(), "fail_box_hi": bhi[j].tolist(),
                        "fail_bounds": [float(lb[bad][j]), float(ub[bad][j])],
                        "seconds": round(time.time() - t0, 1)}
            mid = (blo + bhi) / 2
            dim = blo.shape[1]
            clo, chi = [], []
            for corner in range(2 ** dim):
                bits = np.array([(corner >> q) & 1 for q in range(dim)])[None, :] == 1
                clo.append(np.where(bits, mid, blo))
                chi.append(np.where(bits, bhi, mid))
            clo = np.concatenate(clo)
            chi = np.concatenate(chi)
            cd = np.tile(bd + 1, 2 ** dim)
            rel = relevant(clo, chi)
            maxdepth = max(maxdepth, int(bd.max()) + 1)
            pending_lo = np.concatenate([pending_lo, clo[rel]])
            pending_hi = np.concatenate([pending_hi, chi[rel]])
            pending_d = np.concatenate([pending_d, cd[rel]])
        if log and time.time() - lastlog > 30:
            lastlog = time.time()
            log("  [%s] processed %d verified %d pending %d depth %d (%.0fs)"
                % (label, processed, verified, pending_lo.shape[0], maxdepth, time.time() - t0))
    return {"ok": True, "initial_boxes": int(keep.sum()), "processed": processed, "verified": verified,
            "max_depth": maxdepth, "worst_verified_bound": worst,
            "seconds": round(time.time() - t0, 1)}


def grid(ranges, steps):
    axes = []
    for (a, b), s in zip(ranges, steps):
        k = int(round((b - a) / s))
        assert abs(a + k * s - b) == 0
        axes.append([(a + i * s, a + (i + 1) * s) for i in range(k)])
    import itertools
    lo, hi = [], []
    for combo in itertools.product(*axes):
        lo.append([c[0] for c in combo])
        hi.append([c[1] for c in combo])
    return np.array(lo, dtype=float), np.array(hi, dtype=float)


# ------------------------------------------------------- polynomial builders


def dense_from_squares(p, keyfun=None):
    """Tensor over half-exponents 0..13 for x-space with exps [0,2,...,26]."""
    T = [[[Fr(0)] * 14 for _ in range(14)] for _ in range(14)]
    for (i, j, k), v in p.items():
        T[i][j][k] = v
    return T


def float_tensor(T, shape):
    c = np.zeros(shape)
    r = np.zeros(shape)
    for idx in np.ndindex(*shape):
        v = T[idx[0]][idx[1]][idx[2]] if len(shape) == 3 else T[idx[0]][idx[1]]
        if v != 0:
            c[idx], r[idx] = fr_to_float_rad(v)
    return c, r


def slab_poly(p, alpha):
    """Exact Q(sig,y,z) = P(sig + alpha - y - z, y, z) as dict (a,b,c)->Fr."""
    # group p by i: bivariate in y^2, z^2
    by_i = {}
    for (i, j, k), v in p.items():
        by_i.setdefault(i, {})[(0, 2 * j, 2 * k)] = v
    L = {(1, 0, 0): Fr(1), (0, 0, 0): alpha, (0, 1, 0): Fr(-1), (0, 0, 1): Fr(-1)}

    def mul(A, B):
        R = {}
        for ka, va in A.items():
            for kb, vb in B.items():
                key = (ka[0] + kb[0], ka[1] + kb[1], ka[2] + kb[2])
                R[key] = R.get(key, 0) + va * vb
        return R
    L2 = mul(L, L)
    Q = {}
    cur = {(0, 0, 0): Fr(1)}
    for i in range(14):
        if i in by_i:
            for key, v in mul(cur, by_i[i]).items():
                Q[key] = Q.get(key, Fr(0)) + v
        cur = mul(cur, L2)
    return {k: v for k, v in Q.items() if v != 0}


def tail_polys(hom, R):
    """hom[d]: dict (j,k)->coef of v^{2j} w^{2k} of P_d(1,v,w). Returns list of K_n dicts."""
    out = []
    for n in range(14):
        K = {}
        for d in range(n, 14):
            fac = math.comb(d, n) * R ** (2 * d)
            for key, v in hom.get(d, {}).items():
                K[key] = K.get(key, 0) + fac * v
        out.append(K)
    return out


# --------------------------------------------------------------------- G


def gamma_coef(m, l):
    """Coefficient of u^{2l} in g_m, as (rational, power d) meaning q * (4pi)^{-(m-l)}."""
    return Fr((-1) ** l * math.factorial(2 * m), math.factorial(2 * l) * math.factorial(m - l)), m - l


def G_exact(p):
    """G as dict (a,b,c) -> dict d -> rational r, meaning sum_d r (4 pi)^{-d}."""
    G = {}
    for (i, j, k), v in p.items():
        for a in range(i + 1):
            qa, da = gamma_coef(i, a)
            for b in range(j + 1):
                qb, db = gamma_coef(j, b)
                for c in range(k + 1):
                    qc, dc = gamma_coef(k, c)
                    dd = G.setdefault((a, b, c), {})
                    D = da + db + dc
                    dd[D] = dd.get(D, Fr(0)) + v * qa * qb * qc
    return G


def arb_eval_pi(dd, inv4pi_pows):
    s = arb(0)
    for D, r in dd.items():
        if r != 0:
            s += arb(fmpq(r.numerator, r.denominator)) * inv4pi_pows[D]
    return s


# --------------------------------------------------------------- sanity


def sanity_checks(p, Garb, log):
    """Numerical (non-proof) checks of the FT formula."""
    import mpmath as mp
    mp.mp.dps = 30
    res = {}
    # 1D: FT of x^{2m} e^{-pi x^2} at u
    maxerr = 0.0
    for m in (1, 3, 6, 13):
        for u in (0.0, 0.37, 1.1):
            num = 2 * mp.quad(lambda x: x ** (2 * m) * mp.e ** (-mp.pi * x * x) * mp.cos(2 * mp.pi * u * x), [0, 2, 4, 8, mp.inf])
            g = sum(mp.mpf(gamma_coef(m, l)[0].numerator) / gamma_coef(m, l)[0].denominator
                    * (4 * mp.pi) ** (-(m - l)) * mp.mpf(u) ** (2 * l) for l in range(m + 1))
            val = g * mp.e ** (-mp.pi * u * u)
            maxerr = max(maxerr, float(abs(num - val) / (abs(val) + 1e-30)))
    res["ft1d_max_rel_err"] = maxerr
    # 3D: Gauss-Hermite evaluation of fhat at sample points vs G(u) e^{-pi|u|^2}
    xs, ws = np.polynomial.hermite.hermgauss(90)
    xs = xs / math.sqrt(math.pi)
    ws = ws / math.sqrt(math.pi)
    keys = list(p)
    co = np.array([float(p[k]) for k in keys])
    E = np.array(keys)
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing="ij")
    Wt = ws[:, None, None] * ws[None, :, None] * ws[None, None, :]
    X2, Y2, Z2 = X * X, Y * Y, Z * Z
    Pv = np.zeros_like(X)
    for (a, b, c), v in zip(E, co):
        Pv += v * X2 ** a * Y2 ** b * Z2 ** c
    gk = list(Garb)
    gco = np.array([float(Garb[k].mid()) for k in gk])
    gE = np.array(gk)
    worst = 0.0
    for u in [(0, 0, 0), (0.3, 0.1, 0.0), (0.5, 0.5, 0.2), (0.9, 0.2, 0.4), (1.3, 0.0, 0.0)]:
        u = np.array(u)
        num = np.sum(Wt * Pv * np.cos(2 * np.pi * (u[0] * X + u[1] * Y + u[2] * Z)))
        Gu = np.sum(gco * u[0] ** (2 * gE[:, 0]) * u[1] ** (2 * gE[:, 1]) * u[2] ** (2 * gE[:, 2]))
        val = Gu * math.exp(-math.pi * float(u @ u))
        worst = max(worst, abs(num - val))
        log("  sanity 3D FT at u=%s: quadrature %.12g  formula %.12g" % (tuple(u), num, val))
    res["ft3d_max_abs_err"] = worst
    return res



# ------------------------------------------------------- exact witness tests


def P_exact_at(p, pt):
    x, y, z = (Fr(t) for t in pt)
    X, Y, Z = x * x, y * y, z * z
    return sum(v * X ** i * Y ** j * Z ** k for (i, j, k), v in p.items())


def G_arb_at(Garb, pt):
    X, Y, Z = (arb(fmpq(Fr(t).numerator, Fr(t).denominator)) ** 2 for t in pt)
    s = arb(0)
    for (a, b, c), g in Garb.items():
        s += g * X ** a * Y ** b * Z ** c
    return s


def witness_P(p, alpha, res, chart):
    lo, hi = res["fail_box_lo"], res["fail_box_hi"]
    c = [(Fr(a) + Fr(b)) / 2 for a, b in zip(lo, hi)]
    if chart == "slab":
        c = [c[0] + alpha - c[1] - c[2], c[1], c[2]]
    l1 = sum(abs(t) for t in c)
    val = P_exact_at(p, c)
    return {"point": [str(t) for t in c], "l1": float(l1), "in_domain": l1 >= alpha,
            "P_exact_at_point": float(val), "counterexample": bool(l1 >= alpha and val >= 0)}


# ------------------------------------------------------------------ checks


def check_P_bounded(p, alpha, R, log, max_boxes):
    out = {}
    T = dense_from_squares(p)
    c, r = float_tensor(T, (14, 14, 14))
    ex = list(range(0, 27, 2))
    bern = Bern(c, r, [ex, ex, ex])
    sc = float(alpha + Fr(1, 8)) - 1e-9   # conservative (keeps more boxes)

    def relX(lo, hi):
        return (hi[:, 0] >= lo[:, 1]) & (hi[:, 1] >= lo[:, 2]) & (hi.sum(1) >= sc)
    lo0, hi0 = grid([(0, R)] * 3, [0.25] * 3)
    log("P bulk: x-space boxes in [0,%d]^3 with x+y+z >= alpha+1/8 (straddling allowed)" % R)
    res = run_bb(bern, lo0, hi0, relX, -1, log=log, label="P bulk", max_boxes=max_boxes)
    if not res["ok"]:
        res["witness"] = witness_P(p, alpha, res, "x")
    out["P_bulk"] = res
    log("P bulk: %s" % res)

    assert (alpha + Fr(1, 8)) / 2 <= Fr(5, 8) and (alpha + Fr(1, 8)) / 3 <= Fr(1, 2) and alpha + Fr(1, 8) <= R
    Q = slab_poly(p, alpha)
    assert max(sum(k) for k in Q) <= NDEG
    Tq = [[[Fr(0)] * 27 for _ in range(27)] for _ in range(27)]
    for (a, b, cc), v in Q.items():
        Tq[a][b][cc] = v
    cq, rq = float_tensor(Tq, (27, 27, 27))
    ex = list(range(27))
    bq = Bern(cq, rq, [ex, ex, ex])
    al = float(alpha)

    def relS(lo, hi):
        return (hi[:, 1] >= lo[:, 2]) & ((hi[:, 0] + al) - 2 * lo[:, 1] - lo[:, 2] >= -1e-9)
    lo0, hi0 = grid([(0, 0.125), (0, 0.625), (0, 0.5)], [0.125, 0.125, 0.125])
    log("P slab chart: x = sig+alpha-y-z, sig in [0,1/8], y in [0,5/8], z in [0,1/2]; %d monomials" % len(Q))
    res = run_bb(bq, lo0, hi0, relS, -1, log=log, label="P slab", max_boxes=max_boxes)
    if not res["ok"]:
        res["witness"] = witness_P(p, alpha, res, "slab")
    res["slab_monomials"] = len(Q)
    out["P_slab"] = res
    log("P slab: %s" % res)
    return out


def check_tail(kind, p, Garb, R, log):
    ex = list(range(0, 27, 2))
    mats = []
    if kind == "P":
        hom = {}
        for (i, j, k), v in p.items():
            hom.setdefault(i + j + k, {})[(j, k)] = v
        for K in tail_polys(hom, Fr(R)):
            M = [[Fr(0)] * 14 for _ in range(14)]
            for (j, k), v in K.items():
                M[j][k] = v
            mats.append(float_tensor(M, (14, 14)))
    else:
        for n in range(14):
            M = [[arb(0)] * 14 for _ in range(14)]
            for (a, b, cc), g in Garb.items():
                dgr = a + b + cc
                if dgr >= n:
                    M[b][cc] = M[b][cc] + g * (math.comb(dgr, n) * R ** (2 * dgr))
            cf = np.zeros((14, 14))
            rf = np.zeros((14, 14))
            for j in range(14):
                for k in range(14):
                    if not M[j][k].is_zero():
                        cf[j, k], rf[j, k] = arb_to_float_rad(M[j][k])
            mats.append((cf, rf))
    per = []
    allok = True
    for n, (cf, rf) in enumerate(mats):
        assert np.any(cf)
        bt = Bern(cf, rf, [ex, ex])
        lo0, hi0 = grid([(0, 1), (0, 1)], [0.25, 0.25])
        st = run_bb(bt, lo0, hi0, lambda lo, hi: hi[:, 0] >= lo[:, 1], -1 if kind == "P" else 1,
                    batch=2000, max_depth=20, label="tail %s n=%d" % (kind, n))
        st["n"] = n
        allok &= st["ok"]
        per.append(st)
    res = {"ok": allok, "R": R, "processed": sum(s["processed"] for s in per),
           "worst_bound_per_n": [s.get("worst_verified_bound") for s in per]}
    if not allok:
        res["failures"] = [s for s in per if not s["ok"]]
    log("tail %s (R=%d): ok=%s, boxes %d" % (kind, R, allok, res["processed"]))
    return res


def check_G_bounded(Garb, RG, log, max_boxes):
    cg = np.zeros((14, 14, 14))
    rg = np.zeros((14, 14, 14))
    for (a, b, cc), g in Garb.items():
        cg[a, b, cc], rg[a, b, cc] = arb_to_float_rad(g)
    ex = list(range(0, 27, 2))
    bg = Bern(cg, rg, [ex, ex, ex])
    lo0, hi0 = grid([(0, RG)] * 3, [0.25] * 3)
    log("G bulk: u-space boxes in [0,%d]^3" % RG)
    res = run_bb(bg, lo0, hi0, lambda lo, hi: (hi[:, 0] >= lo[:, 1]) & (hi[:, 1] >= lo[:, 2]), +1,
                 log=log, label="G bulk", max_boxes=max_boxes)
    if not res["ok"]:
        c = [(Fr(a) + Fr(b)) / 2 for a, b in zip(res["fail_box_lo"], res["fail_box_hi"])]
        v = G_arb_at(Garb, c)
        res["witness"] = {"point": [str(t) for t in c], "G_at_point": v.str(15, radius=True),
                          "counterexample": bool(v < 0)}
    log("G bulk: %s" % res)
    return res


# ------------------------------------------------------------------ main


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--R", type=int, default=3, help="tail radius for P (max-norm)")
    ap.add_argument("--RG", type=int, default=3, help="tail radius for G (max-norm)")
    ap.add_argument("--only", default="VSPTG", help="subset of V,S(sanity),P,T(tails),G")
    ap.add_argument("--max-boxes", type=int, default=5_000_000)
    # negative/positive controls (non-default values => control run, not the certificate)
    ap.add_argument("--alpha", default="1001/1000")
    ap.add_argument("--pshift", default="0", help="test P + pshift < 0 instead of P < 0 (exact)")
    ap.add_argument("--gshift", default="0", help="test G - gshift > 0 instead of G > 0 (exact)")
    args = ap.parse_args()
    T0 = time.time()

    def log(s):
        print("[%7.1fs] %s" % (time.time() - T0, s), flush=True)

    alpha = Fr(args.alpha)
    pshift = Fr(args.pshift)
    gshift = Fr(args.gshift)
    control = (alpha != ALPHA) or pshift != 0 or gshift != 0

    sha, C = parse(args.input)
    assert sha == EXPECTED_SHA, sha
    log("input sha256 ok, %d coefficients" % len(C))
    p = expand_squares(C)
    import itertools
    for key, v in p.items():
        for perm in itertools.permutations(key):
            assert p.get(perm, 0) == v
    assert max(i + j + k for (i, j, k) in p) == 13
    log("expanded P: %d monomials, permutation symmetric (exact)" % len(p))
    receipt = {"input": "octa_double.func.cpp (arXiv:1510.02331v3 ancillary)", "input_sha256": sha,
               "alpha": args.alpha, "control_run": control, "pshift": args.pshift, "gshift": args.gshift,
               "kappa": KAPPA, "bernstein_degree": NDEG, "monomials_P": len(p)}

    ctx.prec = 256
    inv4pi = [arb(1)]
    q = 1 / (4 * arb.pi())
    for _ in range(40):
        inv4pi.append(inv4pi[-1] * q)
    Gex = G_exact(p)
    Gnz = {k: {d: r for d, r in dd.items() if r != 0} for k, dd in Gex.items()}
    for key in Gnz:
        for perm in itertools.permutations(key):
            assert Gnz.get(perm, {}) == Gnz[key]
    Garb = {k: arb_eval_pi(dd, inv4pi) for k, dd in Gex.items()}
    log("G derived: %d monomials (exact in Q[1/pi]), permutation symmetric" % len(Gex))

    # ---- (V), always on the unshifted data
    P0 = C[(0, 0, 0)]
    G0 = Garb[(0, 0, 0)]
    A3 = arb(fmpq(ALPHA.numerator ** 3, ALPHA.denominator ** 3))
    gam = 6 * G0 / (A3 * arb(fmpq(P0.numerator, P0.denominator))) - 1
    thr = arb(fmpq(1, 36))
    receipt["V"] = {"P0_exact": str(P0), "G0": G0.str(30, radius=True),
                    "gamma1": gam.str(30, radius=True), "gamma1_gt_1_36": bool(gam > thr),
                    "gamma1_minus_1_36": (gam - thr).str(12, radius=True)}
    log("G(0) = %s ; gamma1 = %s ; gamma1 > 1/36: %s" % (G0.str(25), gam.str(25), bool(gam > thr)))
    if "S" in args.only:
        receipt["sanity_nonproof"] = sanity_checks(p, Garb, log)
        log("sanity: %s" % receipt["sanity_nonproof"])

    pp = dict(p)
    pp[(0, 0, 0)] = pp.get((0, 0, 0), 0) + pshift
    Gs = dict(Garb)
    Gs[(0, 0, 0)] = Gs[(0, 0, 0)] - arb(fmpq(gshift.numerator, gshift.denominator))

    results = {}
    if "P" in args.only:
        results.update(check_P_bounded(pp, alpha, args.R, log, args.max_boxes))
    if "T" in args.only:
        results["tail_P"] = check_tail("P", pp, None, args.R, log)
        results["tail_G"] = check_tail("G", None, Gs, args.RG, log)
    if "G" in args.only:
        results["G_bulk"] = check_G_bounded(Gs, args.RG, log, args.max_boxes)

    def ok(k):
        return k in results and results[k]["ok"]
    receipt["results"] = results
    receipt["claims"] = {"G": ok("G_bulk") and ok("tail_G"),
                         "P": ok("P_bulk") and ok("P_slab") and ok("tail_P"),
                         "V": receipt["V"]["gamma1_gt_1_36"]}
    complete = all(k in args.only for k in "VPTG")
    receipt["verdict"] = ("PASS" if all(receipt["claims"].values()) and complete
                          else ("FAIL_TO_VERIFY" if any(k in results and not results[k]["ok"] for k in results)
                                else "INCOMPLETE"))
    receipt["script_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    receipt["versions"] = {"python": platform.python_version(), "numpy": np.__version__,
                           "python-flint": flint.__version__, "mpmath": __import__("mpmath").__version__,
                           "platform": platform.platform()}
    receipt["args"] = vars(args)
    receipt["total_seconds"] = round(time.time() - T0, 1)
    with open(args.out, "w") as fh:
        json.dump(receipt, fh, indent=1, default=str)
    log("claims %s; verdict %s; wrote %s" % (receipt["claims"], receipt["verdict"], args.out))


if __name__ == "__main__":
    main()
