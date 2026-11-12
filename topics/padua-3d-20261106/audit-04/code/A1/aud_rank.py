#!/usr/bin/env python3
"""Auditor's independent exact rank / fold / admissibility certificates.

No producer or Codex-checker code is imported.  For an HNF (a,b,c,d,e,f)
(rows (a,b,c),(0,d,e),(0,0,f)) of L and degree n:

* H = {x in (Z/q)^3 : B x = 0 mod q}, by the generator parametrization,
  asserted to have q distinct elements all satisfying B x = 0 (mod q).
* |X| computed twice: distinct coordinatewise min(x,q-x) keys, and the
  fibre sum  sum_{h in H} 1/#{sigma h : sigma in {+-1}^3, sigma h in H}.
* shortest l1 norm of L by brute-force box enumeration.
* rank LOWER bound: evaluation matrix T_alpha(x) over F_p, p = 1 mod q,
  omega of exact order q (ring map Z[1/2][zeta_q] -> F_p), Gaussian
  elimination mod p.  rank_p <= rank_R, so rank_p = N proves full rank.
* rank UPPER bound: N-r rational coefficient vectors c (from a rational
  nullspace of a character-incidence matrix built here), each verified to
  give a polynomial sum_alpha c_alpha T_alpha vanishing at EVERY node of X
  by exact cyclotomic arithmetic (Phi_q divides the integer Laurent
  polynomial obtained at that node), plus exact linear independence.
  Hence rank_R <= r.  Both bounds equal => exact rank r.
"""
import itertools, math, json, sys, random, hashlib
from fractions import Fraction
import numpy as np
import sympy
from sympy.polys.matrices import DomainMatrix
from sympy import QQ, ZZ

def exps(n):
    return [(i, j, k) for i in range(n + 1) for j in range(n + 1 - i) for k in range(n + 1 - i - j)]

def dual(h):
    a, b, c, d, e, f = h; q = a * d * f
    g1 = (d * f, 0, 0); g2 = ((-b * f) % q, a * f, 0); g3 = ((b * e - c * d) % q, (-a * e) % q, a * d)
    H = set()
    for j1 in range(a):
        for j2 in range(d):
            for j3 in range(f):
                x = tuple((j1 * g1[i] + j2 * g2[i] + j3 * g3[i]) % q for i in range(3))
                assert (a * x[0] + b * x[1] + c * x[2]) % q == 0 and (d * x[1] + e * x[2]) % q == 0 and (f * x[2]) % q == 0
                H.add(x)
    assert len(H) == q
    return q, H

def folded(q, H):
    X = {}
    for x in H:
        k = tuple(min(t, q - t) for t in x)
        X[k] = X.get(k, 0) + 1
    return X

def fold_fibre_sum(q, H):
    tot = Fraction(0)
    for x in H:
        imgs = set()
        for s in itertools.product((1, -1), repeat=3):
            y = tuple((s[i] * x[i]) % q for i in range(3))
            if y in H: imgs.add(y)
        tot += Fraction(1, len(imgs))
    assert tot.denominator == 1
    return int(tot)

def shortest_brute(h, n):
    a, b, c, d, e, f = h; R = 2 * n
    # any vector with l1 < R has |u|<=R, |v|<=2R, |w|<=4R (b<d, c,e<f)
    u = np.arange(-R, R + 1)[:, None, None]; v = np.arange(-2 * R, 2 * R + 1)[None, :, None]; w = np.arange(-4 * R, 4 * R + 1)[None, None, :]
    k1 = a * u + 0 * v + 0 * w; k2 = b * u + d * v + 0 * w; k3 = c * u + e * v + f * w
    l1 = np.abs(k1) + np.abs(k2) + np.abs(k3)
    l1[R, 2 * R, 4 * R] = 10 ** 9
    m = int(l1.min())
    return m  # exact when < R; m >= R certifies admissibility

def prime_1modq(q, start=2 ** 30):
    t = start // q + 1
    while True:
        p = q * t + 1
        if sympy.isprime(p): return p
        t += 1

def root_of_order(q, p):
    fac = sympy.factorint(q)
    rng = random.Random(12345 + q)
    while True:
        g = rng.randrange(2, p - 1)
        w = pow(g, (p - 1) // q, p)
        if all(pow(w, q // l, p) != 1 for l in fac) and pow(w, q, p) == 1:
            return w

def rank_mod_p(rows, p):
    M = [r[:] for r in rows]; rank = 0; ncol = len(M[0]) if M else 0
    for col in range(ncol):
        piv = None
        for i in range(rank, len(M)):
            if M[i][col] % p: piv = i; break
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], -1, p)
        M[rank] = [(x * inv) % p for x in M[rank]]
        for i in range(len(M)):
            if i != rank and M[i][col] % p:
                t = M[i][col]; M[i] = [(x - t * y) % p for x, y in zip(M[i], M[rank])]
        rank += 1
    return rank

def fp_rank(h, n, X, q, p=None):
    p = p or prime_1modq(q)
    w = root_of_order(q, p); inv2 = pow(2, -1, p)
    nodes = sorted(X)
    def T(m, x):
        return ((pow(w, (m * x) % q, p) + pow(w, (-m * x) % q, p)) * inv2) % p
    rows = [[T(al[0], x[0]) * T(al[1], x[1]) % p * T(al[2], x[2]) % p for x in nodes] for al in exps(n)]
    return rank_mod_p(rows, p), p, w

def canon(h, k):
    """canonical representative of k modulo the row lattice L (triangular division)."""
    a, b, c, d, e, f = h; k1, k2, k3 = k
    u = k1 // a; k1 -= u * a; k2 -= u * b; k3 -= u * c
    v = k2 // d; k2 -= v * d; k3 -= v * e
    k3 %= f
    return (k1, k2, k3)

def nullvectors(h, n):
    al_list = exps(n); cols = {}; entries = []
    for i, al in enumerate(al_list):
        s = sum(1 for t in al if t)
        cnt = {}
        for sg in itertools.product((1, -1), repeat=3):
            k = tuple(sg[j] * al[j] for j in range(3))
            cnt[k] = 1  # distinct sign variants (repeats when a coordinate is 0)
        row = {}
        for k in cnt:
            cl = canon(h, k); row[cl] = row.get(cl, 0) + 1
        for cl, m in row.items():
            j = cols.setdefault(cl, len(cols)); entries.append((i, j, Fraction(m, 2 ** s)))
    N = len(al_list); C = len(cols)
    A = [[QQ(0)] * N for _ in range(C)]  # A^T : C x N
    for i, j, val in entries: A[j][i] = QQ(val.numerator, val.denominator)
    DM = DomainMatrix(A, (C, N), QQ)
    ns = DM.nullspace().to_Matrix()
    vecs = [[sympy.Rational(x) for x in ns.row(r)] for r in range(ns.rows)]
    return vecs

def cyclo_vanish(vec, n, X, q):
    """exact check: polynomial sum c_alpha T_alpha vanishes at every node of X."""
    al_list = exps(n)
    den = 1
    for x in vec: den = math.lcm(den, sympy.Rational(x).q)
    ci = [int(sympy.Rational(x) * den) for x in vec]
    Phi = sympy.Poly(sympy.cyclotomic_poly(q, sympy.Symbol('z')), sympy.Symbol('z'))
    phicoef = [int(t) for t in Phi.all_coeffs()[::-1]]  # low->high, monic
    deg = len(phicoef) - 1
    for x in X:
        P = [0] * q
        for c, al in zip(ci, al_list):
            if not c: continue
            for sg in itertools.product((1, -1), repeat=3):
                P[(sg[0] * al[0] * x[0] + sg[1] * al[1] * x[1] + sg[2] * al[2] * x[2]) % q] += c
        # remainder of P(z) mod Phi_q(z)
        r = P[:]
        for top in range(q - 1, deg - 1, -1):
            t = r[top]
            if t:
                for i in range(deg + 1): r[top - deg + i] -= t * phicoef[i]
        if any(r[:deg]): return False
    return True

def certify(h, n, want_rank=None):
    h = tuple(h); q, H = dual(h); X = folded(q, H)
    fs = fold_fibre_sum(q, H)
    assert fs == len(X), (fs, len(X))
    sh = shortest_brute(h, n)
    N = math.comb(n + 3, 3)
    rp, p, w = fp_rank(h, n, X, q)
    rec = {'hnf': list(h), 'q': q, 'fold': len(X), 'fold_fibre_sum': fs, 'admissible': sh >= 2 * n, 'box_min_l1': sh,
           'N': N, 'rank_Fp': rp, 'p': p, 'omega': w}
    if rp == N:
        rec['rank_exact'] = N; rec['method'] = 'Fp lower bound = N'
    else:
        vecs = nullvectors(h, n)
        indep = sympy.Matrix(vecs).rank() == len(vecs) if vecs else True
        ok = all(cyclo_vanish(v, n, X, q) for v in vecs)
        rec['nullity_certified'] = len(vecs) if (ok and indep) else None
        if ok and indep and rp == N - len(vecs):
            rec['rank_exact'] = rp; rec['method'] = 'Fp lower bound + cyclotomic-verified null vectors'
        else:
            rec['rank_exact'] = None; rec['method'] = 'UNRESOLVED'
            rec['rank_upper'] = N - len(vecs) if (ok and indep) else None
    return rec, X

if __name__ == '__main__':
    pass
