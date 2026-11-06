#!/usr/bin/env python3
"""Claude audit B: independent exact Hahn NN data, full Jacobian and kappa.

Written from the definitions in PD-T286/PD-T432 only; imports nothing from the
topic code. Works directly in z coordinates z_k = 2k/M - 1 with the
unnormalized PD-T290 weights W_(s,k) = (beta_s+1)_k/k! * (2)_(M-k)/(M-k)!.
"""
from fractions import Fraction as F
from math import factorial, comb, prod
import json, sys, time

BETAS = (F(1), F(3, 2))


def rising(a, r):
    out = F(1)
    for j in range(r):
        out *= a + j
    return out


def hahn(N):
    M = N - 1
    z = [F(2 * k, M) - 1 for k in range(N)]
    W = [[rising(b + 1, k) / factorial(k) * rising(F(2), M - k) / factorial(M - k)
          for k in range(N)] for b in BETAS]
    return z, W


def gauss_multi(A, B):
    """Solve A X = B (B list of columns) exactly; also return det(A)."""
    n = len(A)
    R = [list(A[i]) + [B[c][i] for c in range(len(B))] for i in range(n)]
    det = F(1)
    for j in range(n):
        p = next((i for i in range(j, n) if R[i][j] != 0), None)
        if p is None:
            return None, F(0)
        if p != j:
            R[j], R[p] = R[p], R[j]
            det = -det
        piv = R[j][j]
        det *= piv
        inv = 1 / piv
        R[j] = [a * inv for a in R[j]]
        for i in range(n):
            if i != j and R[i][j] != 0:
                f = R[i][j]
                R[i] = [a - f * b for a, b in zip(R[i], R[j])]
    X = [[R[i][n + c] for i in range(n)] for c in range(len(B))]
    return X, det


def nn_with_jacobian(N, z, W, directions):
    """Return NN fields and their derivatives along each direction.

    directions: list of (dz, dW) with dz list len N, dW = [dW1, dW2].
    """
    M = N - 1
    R = 2 * N + 2
    mu = [[sum(W[s][k] * z[k] ** r for k in range(N)) for r in range(R)] for s in range(2)]
    dmu = []
    for dz, dW in directions:
        dmu.append([[sum(dW[s][k] * z[k] ** r + (r * W[s][k] * z[k] ** (r - 1) * dz[k] if r else 0)
                          for k in range(N)) for r in range(R)] for s in range(2)])
    P, dP, dets = {}, {}, {}
    for t in range(N + 1):
        for n in range(t + 1):
            m = t - n
            if t == 0:
                P[n, m] = [F(1)]
                dP[n, m] = [[F(0)] for _ in directions]
                dets[n, m] = F(1)
                continue
            rows = [(0, i) for i in range(n)] + [(1, i) for i in range(m)]
            A = [[mu[s][i + j] for j in range(t)] for s, i in rows]
            v = [mu[s][i + t] for s, i in rows]
            X, det = gauss_multi(A, [[-a for a in v]])
            dets[n, m] = det
            if det == 0:
                raise RuntimeError(('singular', N, n, m))
            c = X[0] + [F(1)]
            P[n, m] = c
            # derivative: A dc + dA c' = -dv
            rhs = []
            for d in dmu:
                col = []
                for s, i in rows:
                    val = -d[s][i + t] - sum(d[s][i + j] * c[j] for j in range(t))
                    col.append(val)
                rhs.append(col)
            Xd, _ = gauss_multi(A, rhs)
            dP[n, m] = [x + [F(0)] for x in Xd]

    def h(nu, s, ell):
        c = P[nu]
        val = sum(c[j] * mu[s][nu[s] + j] for j in range(len(c)))
        if ell is None:
            return val
        d = dmu[ell]
        dc = dP[nu][ell]
        return sum(dc[j] * mu[s][nu[s] + j] + c[j] * d[s][nu[s] + j] for j in range(len(c)))

    def tsub(nu, ell=None):
        if sum(nu) == 0:
            return F(0)
        return P[nu][-2] if ell is None else dP[nu][ell][-2]

    fields, dfields = {}, {}
    for t in range(N):
        for n in range(t + 1):
            nu = (n, t - n)
            vals, ders = {}, {}
            for s, name in ((0, 'a1'), (1, 'a2')):
                if nu[s] >= 1:
                    prev = (n - 1, t - n) if s == 0 else (n, t - n - 1)
                    hn, hp = h(nu, s, None), h(prev, s, None)
                    vals[name] = hn / hp
                    ders[name] = [(h(nu, s, e) * hp - hn * h(prev, s, e)) / hp ** 2
                                  for e in range(len(directions))]
            for j, name in ((0, 'b1'), (1, 'b2')):
                up = (n + 1, t - n) if j == 0 else (n, t - n + 1)
                vals[name] = tsub(nu) - tsub(up)
                ders[name] = [tsub(nu, e) - tsub(up, e) for e in range(len(directions))]
            fields[nu], dfields[nu] = vals, ders
    return fields, dfields, P, dets


def unit_directions(N, W):
    """3N ordinary coordinate directions, pre-multiplied by mixed scales."""
    dirs = []
    for k in range(N):  # nodes, scale ||z||_inf = 1
        dz = [F(0)] * N; dz[k] = F(1)
        dirs.append((dz, [[F(0)] * N, [F(0)] * N]))
    for s in range(2):
        for k in range(N):
            dW = [[F(0)] * N, [F(0)] * N]
            dW[s][k] = W[s][k]  # relative scale
            dirs.append(([F(0)] * N, dW))
    return dirs


def kappa_exact(N):
    z, W = hahn(N)
    dirs = unit_directions(N, W)
    fields, dfields, P, dets = nn_with_jacobian(N, z, W, dirs)
    scales = {}
    for f in ('a1', 'a2', 'b1', 'b2'):
        scales[f] = max(abs(v[f]) for v in fields.values() if f in v)
    best = {}
    for f in scales:
        bestval, bestnu = F(0), None
        for nu, d in dfields.items():
            if f not in d:
                continue
            row = sum(abs(x) for x in d[f])
            if row > bestval:
                bestval, bestnu = row, nu
        best[f] = (bestval / scales[f], bestnu)
    kappa = max(v[0] for v in best.values())
    return dict(N=N, kappa=kappa, by_field=best, scales=scales, fields=fields,
                dfields=dfields, P=P, dets=dets, z=z, W=W)


def tau_formula(M, n, m):
    t = n + m
    if t == M + 1:
        return -F(M * (M + 1), 2)
    Rr = (t + F(2)) * (t + F(5, 2)) / ((t + n + F(2)) * (t + m + F(5, 2)))
    return -F(t * (t - 1), 2) + (M - t + 1) * (1 - (t + 1) * Rr)


def A_M(M):
    T = [sum(comb(k, h) * comb(M + k + 3 - h, M - k) for h in range(k + 1)) for k in range(M + 1)]
    return sum(T[k] * sum(comb(M - 1, 2 * i + 1) * comb(k + i, k) for i in range(M // 2)) for k in range(M + 1))


def main():
    maxN = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    out = dict(status='Claude audit B independent exact check (finite scope only)', cases=[])
    t0 = time.time()
    for N in range(2, maxN + 1):
        M = N - 1
        r = kappa_exact(N)
        # (a) normality: all |nu|<=N moment determinants nonzero (else RuntimeError above)
        nz = all(d != 0 for d in r['dets'].values())
        # (b) b fields vs formula (2) using formula (1), in z coordinates
        bok = True
        for nu, v in r['fields'].items():
            n, m = nu
            for j, name in ((0, 'b1'), (1, 'b2')):
                up = (n + 1, m) if j == 0 else (n, m + 1)
                pred = 2 * (tau_formula(M, n, m) - tau_formula(M, *up)) / M - 1
                if pred != v[name]:
                    bok = False
        # (c) field scale bound and b1_(0,1)
        sc = r['scales']
        scale_ok = 0 < sc['b1'] <= 2 * M + 3 and 0 < sc['b2'] <= 2 * M + 3 and sc['a1'] > 0 and sc['a2'] > 0
        b101 = r['fields'][(0, 1)]['b1'] if M >= 1 else None
        b101_ok = b101 == F(36 - 91 * M, 495 * M)
        # (d) lower bounds
        base2 = F(2 ** (M + 1), M * (2 * M + 3) * comb(M + 4, 4) * (M + 1) * (2 * M + 1))
        rec = dict(N=N, M=M, all_moment_dets_nonzero=nz, b_formula_matches=bok,
                   scales={k: str(v) for k, v in sc.items()}, scale_bound_ok=scale_ok,
                   b1_01=str(b101), b1_01_formula_ok=b101_ok,
                   kappa_exact=str(r['kappa']), kappa_float=float(r['kappa']),
                   by_field={k: [float(v[0]), list(v[1])] for k, v in r['by_field'].items()},
                   base2_lower=float(base2), base2_ok=r['kappa'] >= base2)
        if M >= 2:
            A = A_M(M)
            lowH = F(A, 27 * M * (2 * M + 3))
            rec.update(A_M=A, rhoH_lower=float(lowH), rhoH_lower_ok=r['kappa'] >= lowH)
            # parity response along the balanced terminal b2 row, directly from Jacobian
            nu = ((M + 1) // 2, M // 2)
            d = r['dfields'][nu]['b2']
            w2 = d[2 * N:3 * N]  # relative second-weight coordinates
            parity = sum((-1) ** k * w2[k] for k in range(N))
            l1w2 = sum(abs(x) for x in w2)
            rec.update(parity_dot_b2=str(parity), l1_w2_row=str(l1w2),
                       sign_coherent=abs(parity) == l1w2,
                       D_M_from_jacobian=str(abs(parity) * M / 2),
                       full_row_l1=float(sum(abs(x) for x in d)),
                       parity_relative=float(abs(parity) / sc['b2']))
            # fixed-mass direction: subtract normalized weighted mean
            Z2 = sum(r['W'][1]); c0 = sum(r['W'][1][k] * (-1) ** k for k in range(N)) / Z2
            eta = [((-1) ** k - c0) / (1 + abs(c0)) for k in range(N)]
            mass = sum(r['W'][1][k] * eta[k] for k in range(N))
            fm = sum(eta[k] * w2[k] for k in range(N))
            rec.update(fixed_mass_zero=mass == 0, fixed_mass_box=max(abs(e) for e in eta) <= 1,
                       fixed_mass_response=float(abs(fm) / sc['b2']),
                       fixed_mass_ok=abs(fm) / sc['b2'] >= lowH / 2)
            # null directions: constant relative weight in each channel
            null_ok = all(sum(r['dfields'][nu2][f][N * (s + 1) + k] for k in range(N)) == 0
                          for nu2 in r['dfields'] for f in r['dfields'][nu2] for s in range(2))
            rec['scaling_null_directions_ok'] = null_ok
        out['cases'].append(rec)
        print(json.dumps({k: v for k, v in rec.items() if k not in ('scales',)}, default=str), file=sys.stderr, flush=True)
    out['elapsed_seconds'] = time.time() - t0
    print(json.dumps(out, indent=1, default=str))


if __name__ == '__main__':
    main()
