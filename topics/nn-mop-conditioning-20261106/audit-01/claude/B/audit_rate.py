#!/usr/bin/env python3
"""Claude audit B: terminal parity-row rate, generating function, saddle,
envelope and comparison with the predecessor MEASURED kappa table.
Imports nothing from the topic code."""
from fractions import Fraction as F
from math import comb, factorial
import json, re, sys, time
import mpmath as mp

import sys
B = sys.argv[1] if len(sys.argv) > 1 else '.'


def rising(a, r):
    out = F(1)
    for j in range(r):
        out *= a + j
    return out


def solve(A, cols):
    n = len(A)
    R = [list(A[i]) + [c[i] for c in cols] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if R[i][j] != 0)
        R[j], R[p] = R[p], R[j]
        inv = 1 / R[j][j]
        R[j] = [a * inv for a in R[j]]
        for i in range(n):
            if i != j and R[i][j] != 0:
                f = R[i][j]
                R[i] = [a - f * b for a, b in zip(R[i], R[j])]
    return [[R[i][n + c] for i in range(n)] for c in range(len(cols))]


def A_M(M):
    T = [sum(comb(k, h) * comb(M + k + 3 - h, M - k) for h in range(k + 1)) for k in range(M + 1)]
    return sum(T[k] * sum(comb(M - 1, 2 * i + 1) * comb(k + i, k) for i in range(M // 2)) for k in range(M + 1)), T


def D_formula7(M):
    _, T = A_M(M)
    K = F(M * (M + 1) * (2 * M + 4) * (2 * M + 5), (3 * M + 4) * (3 * M + 5))
    s = sum(T[k] * comb(M - 1, 2 * i + 1) * rising(F(5, 2) + i, k) / factorial(k)
            / ((2 * M + 5 + 2 * i) * (M + F(7, 2) + i)) for k in range(M + 1) for i in range(M // 2))
    return K * s


def terminal_direct(M):
    """Integer-node terminal balanced system; all relative w2 coordinates."""
    N = M + 1
    n, m = (M + 1) // 2, M // 2
    W = [[rising(b + 1, k) / factorial(k) * (M - k + 1) for k in range(N)] for b in (F(1), F(3, 2))]
    mu = [[sum(W[s][k] * k ** r for k in range(N)) for r in range(2 * M + 1)] for s in range(2)]
    rows = [(0, i) for i in range(n)] + [(1, i) for i in range(m)]
    A = [[mu[s][i + j] for j in range(M)] for s, i in rows]
    c = solve(A, [[-mu[s][i + M] for s, i in rows]])[0] + [F(1)]
    Pk = [sum(c[j] * k ** j for j in range(M + 1)) for k in range(N)]
    cols = []
    for k in range(N):
        cols.append([-(W[1][k] * k ** i * Pk[k]) if s == 1 else F(0) for s, i in rows])
    X = solve(A, cols)
    grad = [x[-1] for x in X]  # derivative of coefficient of k^(M-1) = tau
    return Pk, grad, W


def main():
    out = {}
    t0 = time.time()
    # 1. direct terminal rows
    direct = []
    for M in range(2, 25):
        Pk, grad, W = terminal_direct(M)
        parity = sum((-1) ** k * g for k, g in enumerate(grad))
        A, _ = A_M(M)
        D7 = D_formula7(M)
        sign_alt = all(((-1) ** (M + k)) * Pk[k] > 0 for k in range(M + 1))
        coherent = abs(parity) == sum(abs(g) for g in grad)
        comp = F(A, 54) <= abs(parity) <= 3 * (M + 1) ** 2 * A
        direct.append(dict(M=M, D_equals_formula7=abs(parity) == D7, alternating=sign_alt,
                           coherent=coherent, comparison=comp, D=float(abs(parity)), A=A,
                           D_over_A=float(abs(parity) / A)))
    out['direct_terminal'] = direct
    print('direct done', time.time() - t0, all(d['D_equals_formula7'] and d['alternating'] and d['coherent'] and d['comparison'] for d in direct), file=sys.stderr, flush=True)

    # 2. generating function identity (8),(9), independent series, M<=80
    deg = 80
    q = [F(1), F(-4), F(2)] + [F(0)] * (deg)
    # g = q^(-1/2): 2 q g' = -q' g
    g = [F(1)] + [F(0)] * deg
    qp = [F(-4), F(4)] + [F(0)] * deg
    for nn in range(1, deg + 1):
        # coefficient of z^(nn-1): 2*sum_j q_j (nn-j) g_(nn-j) = -sum_j qp_j g_(nn-1-j)
        lhs_rest = 2 * sum(q[j] * (nn - j) * g[nn - j] for j in range(1, min(2, nn) + 1))
        rhs = -sum(qp[j] * g[nn - 1 - j] for j in range(0, min(1, nn - 1) + 1))
        g[nn] = (rhs - lhs_rest) / (2 * nn)
    mul = lambda a, b: [sum(a[i] * b[j - i] for i in range(j + 1)) for j in range(deg + 1)]
    Y = mul([F(1), F(-1)] + [F(0)] * (deg - 1), g)
    inv4 = [F(comb(j + 3, 3)) for j in range(deg + 1)]
    f = [a / 2 for a in mul(Y, inv4)]
    H = Y[:]; H[0] += 1
    oneMinusY = [-a for a in Y]; oneMinusY[0] += 1
    gf_ok = []
    Hp = [F(1)] + [F(0)] * deg
    Lp = [F(1)] + [F(0)] * deg
    pos_ok = all(a > 0 for a in H) and all(a > 0 for a in f)
    for M in range(1, deg + 1):
        if M >= 2:
            bM = mul(f, Hp)[M]
            alt = mul(f, Lp)[M]
            A, _ = A_M(M)
            gf_ok.append(bM - alt == A and alt == F((-1) ** (M - 1) * (3 * M + 2), 2))
        Hp = mul(Hp, H)
        Lp = mul(Lp, oneMinusY)
    out['gf_identity_M2_80'] = all(gf_ok)
    out['H_f_positive_coeffs_to_80'] = pos_ok
    out['Y_first'] = [str(a) for a in Y[:4]]
    print('gf done', time.time() - t0, all(gf_ok), file=sys.stderr, flush=True)

    # 3. A_M growth, large M
    mp.mp.dps = 60
    rho = (7 + 3 * mp.sqrt(3) + mp.sqrt((7 + 3 * mp.sqrt(3)) ** 2 - 4)) / 2
    growth = []
    Ms = [50, 51, 100, 101, 150, 151, 200, 201, 300, 301]
    Avals = {M: A_M(M)[0] for M in Ms}
    for M in Ms[::2]:
        ratio = mp.mpf(Avals[M + 1]) / Avals[M]
        root = mp.mpf(Avals[M]) ** (mp.mpf(1) / M)
        growth.append(dict(M=M, ratio=mp.nstr(ratio, 15), root=mp.nstr(root, 15),
                           ratio_times_1_plus_half_over_M=mp.nstr(ratio * (1 + mp.mpf(1) / (2 * M)), 15)))
    out['A_growth'] = growth
    # Richardson on ratio: r_M = rho(1 + c1/M + c2/M^2...)
    r = {M: mp.mpf(Avals[M + 1]) / Avals[M] for M in Ms[::2]}
    rich1 = (200 * r[200] - 100 * r[100]) / 100
    rich1b = (300 * r[300] - 150 * r[150]) / 150
    out['richardson_ratio'] = [mp.nstr(rich1, 12), mp.nstr(rich1b, 12)]
    out['rho_H'] = mp.nstr(rho, 40)
    print('growth done', time.time() - t0, file=sys.stderr, flush=True)

    # 4. saddle from the definition of H, without the w substitution
    Hf = lambda a: 1 + (1 - a) / mp.sqrt(1 - 4 * a + 2 * a * a)
    Rad = 1 - 1 / mp.sqrt(2)
    rs = mp.findroot(lambda a: a * mp.diff(Hf, a) - Hf(a), (mp.mpf('0.1'), mp.mpf('0.28')), solver='illinois')
    out['saddle_r'] = mp.nstr(rs, 40)
    out['H_over_r'] = mp.nstr(Hf(rs) / rs, 40)
    out['saddle_matches_rho'] = abs(Hf(rs) / rs - rho) < mp.mpf(10) ** -45
    out['saddle_in_0_R'] = bool(0 < rs < Rad)
    grid = [Hf(Rad * j / 2000) / (Rad * j / 2000) for j in range(1, 2000)]
    out['grid_min_H_over_a'] = mp.nstr(min(grid), 15)
    out['quartic_residual'] = mp.nstr(rho ** 4 - 14 * rho ** 3 + 24 * rho ** 2 - 14 * rho + 1, 5)

    # 5. compare with predecessor MEASURED table N=4..64
    txt = open('/workspace/padua_research/topics/nn-mop-stability-20261105/attempts/D1.md').read()
    table = {}
    for line in txt.splitlines():
        mm = re.match(r'\|\s*(\d+)\s*\|\s*([0-9.e+]+)\s*\|\s*([0-9.e+]+)\s*\|', line)
        if mm and 4 <= int(mm.group(1)) <= 64:
            table[int(mm.group(1))] = float(mm.group(3))

    def tau(M, n, m):
        t = n + m
        if t == M + 1:
            return -F(M * (M + 1), 2)
        Rr = (t + F(2)) * (t + F(5, 2)) / ((t + n + F(2)) * (t + m + F(5, 2)))
        return -F(t * (t - 1), 2) + (M - t + 1) * (1 - (t + 1) * Rr)

    cmp = []
    for N in sorted(table):
        M = N - 1
        A, _ = A_M(M)
        low = F(A, 27 * M * (2 * M + 3))
        base2 = F(2 ** (M + 1), M * (2 * M + 3) * comb(M + 4, 4) * (M + 1) * (2 * M + 1))
        b2scale = max(abs(2 * (tau(M, n, t - n) - tau(M, n, t - n + 1)) / M - 1)
                      for t in range(M + 1) for n in range(t + 1))
        D = D_formula7(M)
        row = 2 * D / (M * b2scale)
        cmp.append(dict(N=N, kappa_table=table[N], rhoH_lower=float(low), base2_lower=float(base2),
                        exact_row_response=float(row), b2_scale=float(b2scale),
                        lower_ok=table[N] >= float(low), row_ok=table[N] >= float(row),
                        kappa_over_row=table[N] / float(row)))
    out['table_comparison'] = cmp
    print('table done', time.time() - t0, file=sys.stderr, flush=True)

    # 6. envelope E_M vs D_M
    env = []
    for M in list(range(2, 31)) + [42, 62, 82, 102, 122, 142]:
        N = M + 1
        y = -M - 1
        x = [F(2 + j, 2) for j in range(M)]
        L = 2 * M + 4
        ell = [(-1) ** j * rising(F(L), M) / ((L + j) * factorial(j) * factorial(M - 1 - j)) for j in range(M)]
        _, T = A_M(M)
        C = F(factorial(M + 1)) / rising(F(2 * M + 6, 2), M) / 1  # placeholder replaced below
        prodx = F(1)
        for u in x:
            prodx *= (M + 2 + u)
        C = F(factorial(M + 1)) / prodx
        P = [C * (-1) ** (M + k) * F(factorial(M), 2 ** M) * T[k] / (M - k + 1) for k in range(N)]
        Q2 = [sum(ell[2 * i + 1] * rising(F(k) + F(5, 2), i) / (rising(F(5, 2), i) * (M + F(7, 2) + i))
                  for i in range(M // 2)) for k in range(N)]
        W2 = [rising(F(5, 2), k) / factorial(k) * (M - k + 1) for k in range(N)]
        D = sum(W2[k] * abs(P[k] * Q2[k]) for k in range(N)) / factorial(M)
        E = sum(W2) * max(abs(p) for p in P) * max(abs(qq) for qq in Q2) / factorial(M)
        rec = dict(M=M, D_le_E=D <= E, E_over_D=float(E / D),
                   E_root=float(mp.mpf(E.numerator) / E.denominator) ** (1.0 / M))
        if M <= 24:
            rec['D_matches_formula7'] = D == D_formula7(M)
        if M % 4 == 2:
            l = (M - 2) // 4
            j = M // 2
            lowE = sum(W2) * abs(P[M // 2]) * abs(ell[j]) * rising(F(M) + F(5, 2), l) / (rising(F(5, 2), l) * (M + F(7, 2) + l)) / factorial(M)
            rec['subseq_lower_root'] = float(mp.mpf(lowE.numerator) / lowE.denominator) ** (1.0 / M)
            rec['subseq_le_E'] = lowE <= E
        env.append(rec)
    out['envelope'] = env
    beta = 2 * mp.sqrt((11 + 5 * mp.sqrt(5)) / 2) * mp.power(mp.mpf(3125) / 256, mp.mpf(1) / 4)
    out['beta'] = mp.nstr(beta, 20)
    out['elapsed_seconds'] = time.time() - t0
    print(json.dumps(out, indent=1, default=str))


if __name__ == '__main__':
    main()
