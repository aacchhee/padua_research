#!/usr/bin/env python3
"""Independent exact-rational kappa_N for the Krawtchouk NN map (audit A).

Works directly in the x variable, x_l=2l/M-1, from PD-T432's definition:
moment systems M_nu c=-v for every nu with |nu|<=N, implicit derivative
dot c=-M^-1(dot v+dot M c) for each of the 3N coordinates, then
h, a=h_nu/h_(nu-e_s), b=t_nu-t_(nu+e_j). kappa=max_(field,site)
sum_i |J_i| s_i / A_f, with node scale ||x||_inf=1, weight scale w.
Everything is exact Fractions; final values are printed as floats and the
exact rationals are hashed.  Does not import any repository code.
"""
import sys, json, hashlib, math
from fractions import Fraction as Fr
from math import comb

def solve_multi(A, Bs):
    """Solve A X = B for several right-hand sides, exact Gauss-Jordan."""
    n = len(A)
    if n == 0:
        return [[] for _ in Bs]
    rows = [list(A[i]) + [B[i] for B in Bs] for i in range(n)]
    for j in range(n):
        piv = next(i for i in range(j, n) if rows[i][j] != 0)
        rows[j], rows[piv] = rows[piv], rows[j]
        d = rows[j][j]
        rows[j] = [v / d for v in rows[j]]
        for i in range(n):
            if i != j and rows[i][j] != 0:
                f = rows[i][j]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[j])]
    return [[rows[i][n + r] for i in range(n)] for r in range(len(Bs))]

def run(N):
    M = N - 1
    ps = (Fr(2, 5), Fr(1, 2))
    x = [Fr(2 * l, M) - 1 for l in range(N)]
    w = [[Fr(comb(M, l)) * p**l * (1 - p)**(M - l) for l in range(N)] for p in ps]
    nc = 3 * N  # coordinates: x_0..x_M, w1_0..w1_M, w2_0..w2_M
    scale = [Fr(1)] * N + w[0] + w[1]
    # moments and their derivatives
    R = 2 * N + 2
    xp = [[xl**r for r in range(R)] for xl in x]
    mu = [[sum(w[s][l] * xp[l][r] for l in range(N)) for r in range(R)] for s in range(2)]
    def dmu(s, r, i):
        if i < N:  # node i
            l = i
            return w[s][l] * r * xp[l][r - 1] if r else Fr(0)
        ss, l = divmod(i - N, N)
        return xp[l][r] if ss == s else Fr(0)
    poly = {}   # nu -> (c list length t+1 with c[t]=1, dc[i] list)
    for t in range(0, N + 1):
        for n in range(t + 1):
            nu = (n, t - n)
            rows = [(s, j) for s in range(2) for j in range(nu[s])]
            A = [[mu[s][j + r] for r in range(t)] for s, j in rows]
            v = [-mu[s][j + t] for s, j in rows]
            sol = solve_multi(A, [v])[0]
            c = sol + [Fr(1)]
            # derivative RHS: -(dot v + dot M c) = -sum_r dmu(s,j+r) c_r (r=0..t)
            rhs = []
            for i in range(nc):
                rhs.append([-sum(dmu(s, j + r, i) * c[r] for r in range(t + 1)) for s, j in rows])
            dsol = solve_multi(A, rhs)
            dc = [d + [Fr(0)] for d in dsol]
            poly[nu] = (c, dc)
    def h(nu, s):
        c, dc = poly[nu]
        t = sum(nu)
        val = sum(c[r] * mu[s][nu[s] + r] for r in range(t + 1))
        der = [sum(dc[i][r] * mu[s][nu[s] + r] + c[r] * dmu(s, nu[s] + r, i) for r in range(t + 1)) for i in range(nc)]
        return val, der
    fields = {'a1': {}, 'a2': {}, 'b1': {}, 'b2': {}}
    for t in range(0, M + 1):
        for n in range(t + 1):
            nu = (n, t - n)
            c, dc = poly[nu]
            for s in range(2):
                if nu[s] >= 1:
                    pred = tuple(nu[q] - (q == s) for q in range(2))
                    hv, hd = h(nu, s)
                    gv, gd = h(pred, s)
                    a = hv / gv
                    da = [(hd[i] - a * gd[i]) / gv for i in range(nc)]
                    fields['a%d' % (s + 1)][nu] = (a, da)
                succ = tuple(nu[q] + (q == s) for q in range(2))
                c2, dc2 = poly[succ]
                tsub = c[t - 1] if t >= 1 else Fr(0)
                dtsub = [dc[i][t - 1] if t >= 1 else Fr(0) for i in range(nc)]
                b = tsub - c2[t]
                db = [dtsub[i] - dc2[i][t] for i in range(nc)]
                fields['b%d' % (s + 1)][nu] = (b, db)
    out = {}
    kappa = Fr(0); arg = None
    for f, entries in fields.items():
        Af = max(abs(v[0]) for v in entries.values())
        assert Af > 0
        best = Fr(0); bnu = None
        for nu, (val, der) in entries.items():
            rs = sum(abs(der[i]) * scale[i] for i in range(nc)) / Af
            if rs > best:
                best, bnu = rs, nu
        out[f] = dict(A=float(Af), A_exact=str(Af), kappa=float(best), site=bnu)
        if best > kappa:
            kappa, arg = best, (f, bnu)
    # base formula checks (PD-T437 (5),(6)) in x variable
    q = (Fr(6, 25), Fr(1, 4))
    for nu, (val, _) in fields['b1'].items():
        n, m = nu; t = n + m
        B1 = ps[0] * (M - t) + Fr(3, 5) * n + Fr(1, 2) * m
        assert val == 2 * B1 / M - 1
    for nu, (val, _) in fields['b2'].items():
        n, m = nu; t = n + m
        B2 = ps[1] * (M - t) + Fr(3, 5) * n + Fr(1, 2) * m
        assert val == 2 * B2 / M - 1
    for s in range(2):
        for nu, (val, _) in fields['a%d' % (s + 1)].items():
            n, m = nu; t = n + m
            A = q[s] * nu[s] * (M - t + 1)
            assert val == 4 * A / M**2
    # terminal equality b1=b2 including derivatives
    for n in range(M + 1):
        nu = (n, M - n)
        assert fields['b1'][nu][0] == fields['b2'][nu][0]
        assert fields['b1'][nu][1] == fields['b2'][nu][1]
    # mass-scaling null directions: sum_l w_s,l * d/dw_s,l F = 0 for all fields
    for f, entries in fields.items():
        for nu, (val, der) in entries.items():
            for s in range(2):
                assert sum(w[s][l] * der[N + s * N + l] for l in range(N)) == 0
    rho = 5 + 2 * math.sqrt(6)
    lower = 5 / (2 * M**2) * (rho**(M - 1) + rho**(-(M - 1)))
    upper_log10 = math.log10(3e6) + 13 * math.log10(N) + M * math.log10(rho)
    h_ = hashlib.sha256(str(kappa).encode()).hexdigest()[:16]
    return dict(N=N, kappa=float(kappa), kappa_exact_sha16=h_, argmax=[arg[0], list(arg[1])],
                lower_PD_T437_13=lower, lower_ok=bool(kappa >= Fr(lower) * (1 - Fr(1, 10**12))),
                log10_upper=upper_log10, log10_kappa=math.log10(float(kappa)),
                upper_ok=bool(math.log10(float(kappa)) < upper_log10),
                kappa_over_rho_M=float(kappa) / rho**M,
                kappa_root_N=float(kappa)**(1 / N), fields=out)

if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for N in range(lo, hi + 1):
        r = run(N)
        print(json.dumps(r), flush=True)
