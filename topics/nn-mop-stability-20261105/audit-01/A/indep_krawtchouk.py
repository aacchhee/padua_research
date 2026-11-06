#!/usr/bin/env python3
"""Independent auditor checks for D1-02 (coarse Krawtchouk bound) and the
mixed-input/fieldwise-output convention of D1-01.  Imports no developer code.

For small N (exact Fraction arithmetic, from PD-T286 definitions):
  * every mixed moment determinant |nu|<=N nonzero; D^k*det integral;
    |det|<=k^(k/2) (Hadamard); |det|>=D^-k; sign pattern recorded;
  * ||M^-1||_inf <= k (k-1)^((k-1)/2) D^k; ||c||_inf <= B;
  * |h| bounds  1/B <= |h| <= H;
  * field-scale lemma values a1_(1,0), a2_(0,1), b1_(0,0), b2_(1,0), b2_(0,0);
  * exact mixed-input fieldwise kappa from differentiated defining systems,
    compared with the closed-form coarse bound (log10 shown).
Also checks the Hahn family kappa at N=4 against the D1 table.
"""
import sys, math, json
from fractions import Fraction as F


def inputs(N, family):
    M = N-1
    x = [F(2*l, M)-1 for l in range(N)]
    if family == 'krawtchouk':
        w = [[math.comb(M, l)*p**l*(1-p)**(M-l) for l in range(N)] for p in (F(2, 5), F(1, 2))]
    else:
        def r(a, k):
            v = F(1)
            for i in range(k):
                v = v*(a+i)/(i+1)
            return v
        w = [[r(b+1, l)*r(F(2), M-l) for l in range(N)] for b in (F(1), F(3, 2))]
    return x, w


def inv(A):
    n = len(A)
    A = [list(r)+[F(int(i == j)) for j in range(n)] for i, r in enumerate(A)]
    det = F(1)
    for j in range(n):
        p = next(i for i in range(j, n) if A[i][j] != 0)
        if p != j:
            A[j], A[p] = A[p], A[j]; det = -det
        det *= A[j][j]
        piv = A[j][j]
        A[j] = [a/piv for a in A[j]]
        for i in range(n):
            if i != j and A[i][j] != 0:
                q = A[i][j]
                A[i] = [a-q*c for a, c in zip(A[i], A[j])]
    return det, [r[n:] for r in A]


def matvec(A, v):
    return [sum(a*b for a, b in zip(r, v)) for r in A]


def analyse(N, family, do_kappa=True):
    M = N-1
    x, w = inputs(N, family)
    R2 = 2*N
    mu = [[sum(ws[l]*x[l]**r for l in range(N)) for r in range(R2+1)] for ws in w]
    nin = 3*N
    # unit mixed-scale directions: node l -> dx_l = 1 ; weight (s,l) -> dw = w_(s,l)
    def dmu(i):
        out = [[F(0)]*(R2+1) for _ in range(2)]
        if i < N:
            l = i
            for s in range(2):
                for r in range(1, R2+1):
                    out[s][r] = r*w[s][l]*x[l]**(r-1)
        else:
            s, l = divmod(i-N, N)
            for r in range(R2+1):
                out[s][r] = w[s][l]*x[l]**r
        return out
    dmus = [dmu(i) for i in range(nin)] if do_kappa else []
    D = 10**M*M**(2*N)
    B = N**N*D**N
    H = N*B+1
    info = dict(N=N, family=family)
    P, dP, dets, signs = {}, {}, {}, {}
    worst = dict(inv_ratio=0, c_ratio=0)
    P[(0, 0)] = [F(1)]; dP[(0, 0)] = [[F(0)] for _ in range(nin)]
    for k in range(1, N+1):
        for n in range(k+1):
            m = k-n
            rows = [(0, i) for i in range(n)]+[(1, i) for i in range(m)]
            A = [[mu[s][i+j] for j in range(k)] for s, i in rows]
            v = [mu[s][i+k] for s, i in rows]
            det, Ai = inv(A)
            assert det != 0
            dets[n, m] = det; signs[n, m] = 1 if det > 0 else -1
            if family == 'krawtchouk':
                assert (det*D**k).denominator == 1, 'denominator claim'
                assert abs(det) >= F(1, D**k)
                assert abs(det)**2 <= k**k, 'Hadamard'
                invnorm = max(sum(abs(a) for a in r) for r in Ai)
                bound = k*(math.isqrt(1) if k == 1 else 1)*F(1)
                hb = F(k)*((k-1)**(k-1))  # compare squares: invnorm^2 <= k^2 (k-1)^(k-1) D^(2k)
                assert invnorm**2 <= k*k*(k-1)**(k-1)*D**(2*k) if k > 1 else invnorm <= D
                worst['inv_ratio'] = max(worst['inv_ratio'], float(invnorm**2/(k*k*max(1, (k-1)**(k-1))*D**(2*k))))
            c = [-a for a in matvec(Ai, v)]
            if family == 'krawtchouk':
                assert max(abs(a) for a in c) <= B
            P[n, m] = c+[F(1)]
            if do_kappa:
                dPl = []
                for i in range(nin):
                    dA = [[dmus[i][s][ii+j] for j in range(k)] for s, ii in rows]
                    dv = [dmus[i][s][ii+k] for s, ii in rows]
                    rhs = [a+b for a, b in zip(dv, matvec(dA, c))]
                    dc = [-a for a in matvec(Ai, rhs)]
                    dPl.append(dc+[F(0)])
                dP[n, m] = dPl
    def h(nu, s):
        return sum(a*mu[s][nu[s]+j] for j, a in enumerate(P[nu]))
    def dh(nu, s, i):
        return sum(da*mu[s][nu[s]+j]+a*dmus[i][s][nu[s]+j] for j, (a, da) in enumerate(zip(P[nu], dP[nu][i])))
    def t(nu):
        return P[nu][-2] if sum(nu) else F(0)
    def dt(nu, i):
        return dP[nu][i][-2] if sum(nu) else F(0)
    coef, dcoef = {}, {}
    hmin = None
    for k in range(N):
        for n in range(k+1):
            m = k-n; nu = (n, m)
            for s in range(2):
                hv = h(nu, s)
                if family == 'krawtchouk':
                    assert abs(hv) <= H and (abs(hv) >= F(1, B))
                hmin = abs(hv) if hmin is None else min(hmin, abs(hv))
            a1 = h(nu, 0)/h((n-1, m), 0) if n else F(0)
            a2 = h(nu, 1)/h((n, m-1), 1) if m else F(0)
            coef[nu] = dict(a1=a1, a2=a2, b1=t(nu)-t((n+1, m)), b2=t(nu)-t((n, m+1)))
            if do_kappa:
                g = dict(a1=[], a2=[], b1=[], b2=[])
                for i in range(nin):
                    g['a1'].append((dh(nu, 0, i)-a1*dh((n-1, m), 0, i))/h((n-1, m), 0) if n else F(0))
                    g['a2'].append((dh(nu, 1, i)-a2*dh((n, m-1), 1, i))/h((n, m-1), 1) if m else F(0))
                    g['b1'].append(dt(nu, i)-dt((n+1, m), i))
                    g['b2'].append(dt(nu, i)-dt((n, m+1), i))
                dcoef[nu] = g
    scales = {f: max(abs(coef[nu][f]) for nu in coef) for f in ('a1', 'a2', 'b1', 'b2')}
    info['field_scales'] = {f: str(v) for f, v in scales.items()}
    info['min_field_scale_ge_1/(5M)'] = all(v >= F(1, 5*M) for v in scales.values())
    if family == 'krawtchouk':
        info['lemma_values_ok'] = (coef[(1, 0)]['a1'] == F(24, 25*M) if N >= 2 else None,
                                   coef[(0, 1)]['a2'] == F(1, M),
                                   coef[(0, 0)]['b1'] == F(-1, 5),
                                   coef[(1, 0)]['b2'] == F(1, 5*M),
                                   coef[(0, 0)]['b2'] == 0)
        info['inv_bound_worst_ratio_sq'] = worst['inv_ratio']
        info['det_sign_set'] = sorted(set(signs.values()))
    if do_kappa:
        best, arg = F(0), None
        for nu, g in dcoef.items():
            for f, row in g.items():
                val = sum(abs(r) for r in row)/scales[f]
                if val > best:
                    best, arg = val, (nu, f)
        info['kappa_mixed_exact'] = str(best)
        info['kappa_float'] = float(best)
        info['argmax'] = [list(arg[0]), arg[1]]
        # coarse bound
        R = 2*N+1
        C = B*(N*B+1)*R; T = N*C+H*R
        bnd = 5*M*max(2*C, B*T*(1+H*B))
        info['log10_bound'] = round(math.log10(bnd), 2)
        info['kappa_le_bound'] = best <= bnd
        # mixed numerator bound check, field-wise
        num_a = max(sum(abs(r) for r in g[f]) for g in dcoef.values() for f in ('a1', 'a2'))
        num_b = max(sum(abs(r) for r in g[f]) for g in dcoef.values() for f in ('b1', 'b2'))
        info['num_a_le_BT(1+HB)'] = num_a <= B*T*(1+H*B)
        info['num_b_le_2C'] = num_b <= 2*C
    return info


if __name__ == '__main__':
    fam = sys.argv[1]
    for Ns in sys.argv[2:]:
        N = int(Ns)
        print(json.dumps(analyse(N, fam, do_kappa=N <= 7)), flush=True)
