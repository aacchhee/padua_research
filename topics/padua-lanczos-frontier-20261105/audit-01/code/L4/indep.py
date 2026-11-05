#!/usr/bin/env python3
"""Claude L4 auditor's own independent reconstruction (no FLINT, no repository code).

Arithmetic: CPython integers / fractions.Fraction only.  Vectors are stored as
(list of integer numerators, positive common denominator), reduced by gcd.

Builds from the written definitions (PD-T136/138, L4 record):
  * rotQ24 nodes, graded order, alt/BJ parent rules, exact monic full GS basis;
  * complete local amplitude radius rho_hi (PD-T138 table);
  * BJ: adjoint row g_{90,h}(z_i) (backward recurrence), frozen same-sign
    witness f_h = s_i sign(g_90h) rho_h, full V by the frozen forward
    recurrence V_k = A_k V_p - sum_l alpha_kl V_l + f_k;
  * alt: S_ki = sum_h |g_kh| rho_hi by per-source propagation (optional).
Then checks the committed fixed integer vectors exactly.
"""
import sys, json, math, time, hashlib, pickle, argparse
from fractions import Fraction as F

M = 625
sys.set_int_max_str_digits(0)

def norm(num, den):
    g = math.gcd(den, *num) if any(num) else den
    if g > 1:
        num = [x // g for x in num]; den //= g
    return num, den

class V:
    __slots__ = ("n", "d")
    def __init__(self, n, d=1, reduce=True):
        if reduce: n, d = norm(n, d)
        self.n, self.d = n, d
    def frac(self, i): return F(self.n[i], self.d)
    def scale(self, c):  # c Fraction
        return V([x * c.numerator for x in self.n], self.d * c.denominator)
    def __add__(self, o):
        L = self.d * o.d // math.gcd(self.d, o.d); a, b = L // self.d, L // o.d
        return V([x * a + y * b for x, y in zip(self.n, o.n)], L)
    def __sub__(self, o):
        L = self.d * o.d // math.gcd(self.d, o.d); a, b = L // self.d, L // o.d
        return V([x * a - y * b for x, y in zip(self.n, o.n)], L)
    def pmul(self, o):
        return V([x * y for x, y in zip(self.n, o.n)], self.d * o.d)
    def absv(self): return V([abs(x) for x in self.n], self.d, reduce=False)
    def dot(self, o): return F(sum(x * y for x, y in zip(self.n, o.n)), self.d * o.d)
    def is_zero(self): return not any(self.n)

def lincomb(terms):
    """sum c_j * v_j with Fractions c_j, using a single common denominator."""
    terms = [(c, v) for c, v in terms if c]
    if not terms: return V([0] * M, 1)
    L = 1
    for c, v in terms:
        dd = c.denominator * v.d; L = L * dd // math.gcd(L, dd)
    acc = [0] * M
    for c, v in terms:
        f = c.numerator * (L // (c.denominator * v.d))
        n = v.n
        for i in range(M): acc[i] += f * n[i]
    return V(acc, L)

def nodes():
    X, Y = [], []
    for i in range(25):
        for j in range(25):
            xi, yj = i - 12, j - 12        # x=(i-12)/12, y=(j-12)/12
            X.append(3 * xi - 4 * yj)      # (3x-4y)/5 = (3xi-4yj)/60
            Y.append(4 * xi + 3 * yj)
    return V(X, 60, reduce=False), V(Y, 60, reduce=False)

def basis(rule, coords):
    """Monic exact full-projection basis in graded order; returns b,d,rec,mono."""
    b = [V([1] * M, 1)]; d = [F(M)]; rec = [None]; idx = {(0, 0): 0}; mono = [(0, 0)]
    for t in range(1, 13):
        for j in range(t + 1):
            if rule == 'alt': ax = 0 if 2 * j < t else 1
            elif rule == 'bj': ax = 0 if j == 0 else 1
            else: raise ValueError(rule)
            assert (ax == 0 and j < t) or (ax == 1 and j > 0)
            p = idx[(t - 1, j - (ax == 1))]
            u = b[p].pmul(coords[ax])
            alpha = [u.dot(bl) / dl for bl, dl in zip(b, d)]
            r = u - lincomb([(a, bl) for a, bl in zip(alpha, b)])
            dk = r.dot(r); assert dk > 0
            idx[(t, j)] = len(b); mono.append((t, j)); b.append(r); d.append(dk)
            rec.append((ax, p, alpha))
    assert len(b) == 91
    return b, d, rec, mono

def radius(h, b, rec, coords):
    ax, p, alpha = rec[h]
    u = b[p].pmul(coords[ax])
    terms_abs = []  # |A b_p| + sum_l |alpha b_l| + sum_{l>=1} |partial_l| + 3|b_h|
    acc = u.absv() + b[h].absv().scale(F(3))
    partial = None
    for l, a in enumerate(alpha):
        term = b[l].scale(a)
        acc = acc + term.absv()
        partial = term if partial is None else partial + term
        if l >= 1: acc = acc + partial.absv()
    return acc

def sgn(x): return (x > 0) - (x < 0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--certificate', required=True)
    ap.add_argument('--frozen-multinode', required=True)
    ap.add_argument('--frozen-scalar', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--do-alt', action='store_true')
    a = ap.parse_args(); t0 = time.time(); res = {}
    cert = json.load(open(a.certificate))
    tvec = cert['lower_monic_coefficients']; vvec = cert['upper_positive_vector']
    B = cert['upper_integer_B']; L = cert['lower_integer_floor_L']
    low = json.load(open(a.frozen_multinode)); old = json.load(open(a.frozen_scalar))
    lrow = next(r for r in low['witnesses'] if r['set'] == 'rotated' and r['rule'] == 'bj')
    orow = next(r for r in old['full_graph_upper_runs'] if r['set'] == 'rotated' and r['rule'] == 'alt')
    G = F(lrow['explicit_greedy_sign_lower_squared']['exact']); Uold = F(orow['upper_squared']['exact'])
    s = lrow['node_signs']; assert len(s) == M and set(s) <= {-1, 1}
    coords = nodes()
    # ---------------- BJ lower ----------------
    b, d, rec, mono = basis('bj', coords)
    res['bj_basis_seconds'] = time.time() - t0
    gram_ok = all((b[i].dot(b[j]) == (d[i] if i == j else 0)) for i in range(91) for j in range(i, 91))
    res['bj_gram_diag_exact'] = gram_ok; assert gram_ok
    rho = [None] + [radius(h, b, rec, coords) for h in range(1, 91)]
    res['bj_rho_seconds'] = time.time() - t0
    # adjoint row y_h(i) = g_{90,h}(z_i): y_h = delta_{h,90} + sum_{k>h} y_k L_{k,h}
    y = [None] * 91; y[90] = V([1] * M, 1)
    for h in range(89, 0, -1):
        terms = []
        acc = None
        for k in range(h + 1, 91):
            ax, p, alpha = rec[k]
            c = -alpha[h]
            if c: terms.append((c, y[k]))
            if p == h:
                pk = y[k].pmul(coords[ax]); acc = pk if acc is None else acc + pk
        lc = lincomb(terms)
        y[h] = lc if acc is None else acc + lc
    res['bj_adjoint_seconds'] = time.time() - t0
    f = [None] + [V([s[i] * sgn(y[h].n[i]) * rho[h].n[i] for i in range(M)], rho[h].d) for h in range(1, 91)]
    # forward frozen recurrence
    Vk = [V([0] * M, 1)]
    for k in range(1, 91):
        ax, p, alpha = rec[k]
        w = Vk[p].pmul(coords[ax]) - lincomb([(al, Vk[l]) for l, al in enumerate(alpha)]) + f[k]
        Vk.append(w)
    res['bj_forward_seconds'] = time.time() - t0
    # independent consistency: V_90 = s * S_90 (S_90 = sum_h |g_90h| rho_h)
    S90 = lincomb([(F(1), y[h].absv().pmul(rho[h])) for h in range(1, 91)])
    s_vec = V(list(s), 1, reduce=False)
    res['V90_equals_s_times_S90'] = (Vk[90] - S90.pmul(s_vec)).is_zero()
    def Qgain(x):
        assert len(x) == 91 and x[0] == 0 and any(x[1:])
        yv = lincomb([(F(xk), Vk[k]) for k, xk in enumerate(x) if xk])
        energy = yv.dot(yv)
        removed = sum((yv.dot(b[l]) ** 2 / d[l] for l in range(91)), F(0))
        den = sum((d[k] * xk * xk for k, xk in enumerate(x)), F(0))
        assert den > 0 and energy >= removed
        return (energy - removed) / den, energy, removed, den
    q90 = Qgain([0] * 90 + [1])[0]
    res['old_target90_equals_frozen_G_R'] = (q90 == G)
    q, en, rm, den = Qgain(tvec)
    res['Q_floor'] = q.numerator // q.denominator
    res['L_le_Q_lt_L_plus_1'] = (L <= q < L + 1)
    res['Q_gt_100B_exact'] = (q > 100 * B)
    res['Q_exact_sha256_str'] = hashlib.sha256(str(q).encode()).hexdigest()
    # Readout normalisation: unit output direction a = D^{1/2} x / sqrt(x^T D x)
    res['denominator_xTDx_float'] = float(den)
    res['denominator_xTDx_exact_digits'] = (len(str(den.numerator)), len(str(den.denominator)))
    res['nonzero_readout_coeffs'] = sum(1 for x in tvec if x)
    res['readout_maxabs'] = max(abs(x) for x in tvec)
    res['readout_support_monomials'] = [mono[k] for k, x in enumerate(tvec) if x][:5]
    res['bj_seconds'] = time.time() - t0
    # save BJ arrays for comparison with producer output
    with open(a.out + '.bj.pkl', 'wb') as fh:
        pickle.dump({'b': [(v.n, v.d) for v in b], 'd': [(x.numerator, x.denominator) for x in d],
                     'V': [(v.n, v.d) for v in Vk]}, fh)
    print(json.dumps(res), flush=True)
    # ---------------- alt upper ----------------
    if a.do_alt:
        b, d, rec, mono = basis('alt', coords)
        rho = [None] + [radius(h, b, rec, coords) for h in range(1, 91)]
        Sabs = [V([0] * M, 1) for _ in range(91)]
        for h in range(1, 91):
            g = {h: V([1] * M, 1)}
            Sabs[h] = Sabs[h] + rho[h]
            for k in range(h + 1, 91):
                ax, p, alpha = rec[k]
                terms = [(-alpha[l], g[l]) for l in range(h, k) if alpha[l]]
                w = lincomb(terms)
                if p >= h: w = g[p].pmul(coords[ax]) + w
                g[k] = w
                Sabs[k] = Sabs[k] + w.absv().pmul(rho[h])
            if h % 10 == 0: print(json.dumps({'alt_source': h, 'sec': time.time() - t0}), flush=True)
        trace = sum((Sabs[k].dot(Sabs[k]) / d[k] for k in range(1, 91)), F(0))
        res['alt_trace_equals_frozen_U_R'] = (trace == Uold)
        # z = S^T D^{-1} S v  (exact, pure Python)
        w = [F(0)] + [F(sum(x * vi for x, vi in zip(Sabs[k].n, vvec)), Sabs[k].d) for k in range(1, 91)]
        cc = [F(0)] + [w[k] / d[k] / Sabs[k].d for k in range(1, 91)]
        Lc = 1
        for k in range(1, 91): Lc = Lc * cc[k].denominator // math.gcd(Lc, cc[k].denominator)
        fac = [0] + [cc[k].numerator * (Lc // cc[k].denominator) for k in range(1, 91)]
        z = [F(sum(fac[k] * Sabs[k].n[i] for k in range(1, 91)), Lc) for i in range(M)]
        res['all_z_le_Bv'] = all(z[i] <= B * vvec[i] for i in range(M))
        U = max(z[i] / vvec[i] for i in range(M))
        res['U_exact_float'] = float(U)
        res['ceil_U_equals_B'] = (-(-U.numerator // U.denominator) == B)
        Rq = sum((z[i] * vvec[i] for i in range(M)), F(0)) / sum(x * x for x in vvec)
        res['rayleigh_floor'] = Rq.numerator // Rq.denominator
        res['100_rayleigh_floor_ge_G'] = 100 * res['rayleigh_floor'] >= G
        res['alt_seconds'] = time.time() - t0
        with open(a.out + '.alt.pkl', 'wb') as fh:
            pickle.dump({'S': [(v.n, v.d) for v in Sabs[1:]], 'd': [(x.numerator, x.denominator) for x in d]}, fh)
    res['L_gt_100B_int'] = L > 100 * B
    res['elapsed'] = time.time() - t0
    json.dump(res, open(a.out, 'w'), indent=1, default=str)
    print(json.dumps(res, default=str), flush=True)

if __name__ == '__main__':
    main()
