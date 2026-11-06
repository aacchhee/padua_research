#!/usr/bin/env python3
"""Independent auditor check of the finite Hahn normality theorem (D1-05).

Written from the definitions (PD-T286, PD-T290); imports NO developer code.
Reads only the committed theory table (to compare digests), parsed by split.

Methods (all exact):
  A  'moment'   : literal PD-T286 -- Fraction Gaussian elimination of every
                  mixed moment matrix M_nu, |nu|<=N (determinant != 0), and
                  coefficient vectors of P_nu from M_nu c = -v for |nu|<=N-1;
                  h, t, a, b from the PD-T286 formulas.
  B  'modp'     : integer-scaled moment matrices (variable y=M z=2k-M, weights
                  scaled by positive integers) with determinant mod two primes;
                  det != 0 mod p  ==>  det != 0 over Q (rigorous sufficient).
  C  'recur'    : P_nu built in node-value form by the PD-T286 NN identity
                  (a from h ratios, b fixed by the new orthogonality condition),
                  with full orthogonality re-verification of every P_nu
                  (optional) -- uniqueness then identifies P_nu given normality.
Payload/input digests use the exact JSON layout described in the theory file
(nodes/weights str(Fraction); [[n,m,a1,a2,b1,b2],...] sorted, |nu|<=N-2).
"""
import sys, json, hashlib, time, math
from fractions import Fraction as F
from pathlib import Path
import numpy as np

REPO = Path('/home/user/padua_research')
TABLE = REPO/'topics/nn-mop-stability-20261105/theory/conditioning-hahn-normality-finite.md'


def hahn_inputs(N):
    M = N-1
    z = [F(2*k, M) - 1 for k in range(N)]
    def rising_over_fact(a, k):          # (a)_k / k!
        r = F(1)
        for i in range(k):
            r = r*(a+i)/(i+1)
        return r
    gamma = F(1)
    w = [[rising_over_fact(beta+1, k)*rising_over_fact(gamma+1, M-k) for k in range(N)]
         for beta in (F(1), F(3, 2))]
    return z, w


def committed_table():
    rows = {}
    for line in TABLE.read_text().splitlines():
        parts = [p.strip().strip('`') for p in line.split('|')]
        if len(parts) == 6 and parts[1].isdigit():
            rows[int(parts[1])] = (int(parts[2]), parts[3], parts[4])
    return rows


def input_sha(z, w):
    ident = json.dumps(dict(nodes=[str(v) for v in z], weights=[[str(v) for v in r] for r in w]), sort_keys=True)
    return hashlib.sha256(ident.encode()).hexdigest()


def payload_sha(coef, N):
    sites = sorted(nu for nu in coef if sum(nu) <= N-2)
    payload = json.dumps([[n, m, *[str(coef[(n, m)][f]) for f in ('a1', 'a2', 'b1', 'b2')]] for n, m in sites],
                         separators=(',', ':'))
    return hashlib.sha256(payload.encode()).hexdigest()


def moments(z, w, rmax):
    out = []
    for ws in w:
        mu = []
        p = [F(1)]*len(z)
        for r in range(rmax+1):
            mu.append(sum(a*b for a, b in zip(ws, p)))
            p = [a*b for a, b in zip(p, z)]
        out.append(mu)
    return out


def frac_solve(A, b):
    """Exact Gaussian elimination; returns (det, x) with x=None if singular."""
    n = len(A)
    A = [list(r)+[y] for r, y in zip(A, b)]
    det = F(1)
    for j in range(n):
        p = next((i for i in range(j, n) if A[i][j] != 0), None)
        if p is None:
            return F(0), None
        if p != j:
            A[j], A[p] = A[p], A[j]
            det = -det
        det *= A[j][j]
        for i in range(j+1, n):
            if A[i][j] != 0:
                q = A[i][j]/A[j][j]
                A[i] = [a-q*c for a, c in zip(A[i], A[j])]
    x = [F(0)]*n
    for j in reversed(range(n)):
        x[j] = (A[j][n]-sum(A[j][h]*x[h] for h in range(j+1, n)))/A[j][j]
    return det, x


def method_moment(N):
    z, w = hahn_inputs(N)
    mu = moments(z, w, 2*N)
    P, dets = {(0, 0): [F(1)]}, {(0, 0): F(1)}
    for k in range(1, N+1):
        for n in range(k+1):
            m = k-n
            rows = [(0, i) for i in range(n)]+[(1, i) for i in range(m)]
            A = [[mu[s][i+j] for j in range(k)] for s, i in rows]
            v = [-mu[s][i+k] for s, i in rows]
            det, c = frac_solve(A, v)
            dets[n, m] = det
            if k <= N-1:
                assert c is not None
                P[n, m] = c+[F(1)]
    def h(nu, s):
        return sum(a*mu[s][nu[s]+j] for j, a in enumerate(P[nu]))
    def t(nu):
        return P[nu][-2] if sum(nu) else F(0)
    coef = {}
    for k in range(N-1):            # sites |nu|<=N-2 only (payload domain)
        for n in range(k+1):
            m = k-n
            coef[n, m] = dict(a1=h((n, m), 0)/h((n-1, m), 0) if n else F(0),
                              a2=h((n, m), 1)/h((n, m-1), 1) if m else F(0),
                              b1=t((n, m))-t((n+1, m)), b2=t((n, m))-t((n, m+1)))
    return z, w, dets, coef


def method_recur(N, verify=True):
    z, w = hahn_inputs(N)
    Nn = len(z)
    L = lambda s, vals, i: sum(ws*(zl**i)*v for ws, zl, v in zip(w[s], z, vals))
    val, t = {(0, 0): [F(1)]*Nn}, {(0, 0): F(0)}
    def hh(nu, s):
        return L(s, val[nu], nu[s])
    a = {}
    def acoef(nu):
        if nu not in a:
            n, m = nu
            a[nu] = (hh(nu, 0)/hh((n-1, m), 0) if n else F(0), hh(nu, 1)/hh((n, m-1), 1) if m else F(0))
        return a[nu]
    for k in range(N-1):          # build degree k+1 <= N-1
        for n in range(k+2):
            m = k+1-n
            base, j = ((n-1, m), 0) if n else ((n, m-1), 1)
            a1, a2 = acoef(base)
            bn, bm = base
            Q = [zl*v for zl, v in zip(z, val[base])]
            if bn:
                Q = [q-a1*v for q, v in zip(Q, val[(bn-1, bm)])]
            if bm:
                Q = [q-a2*v for q, v in zip(Q, val[(bn, bm-1)])]
            b = L(j, Q, base[j])/hh(base, j)
            val[n, m] = [q-b*v for q, v in zip(Q, val[base])]
            t[n, m] = t[base]-b
    nverified = 0
    if verify:
        for (n, m), vals in val.items():
            for s, cnt in ((0, n), (1, m)):
                pv = [ws*v for ws, v in zip(w[s], vals)]
                for i in range(cnt):
                    assert sum(pv) == 0, ('orthogonality failed', n, m, s, i)
                    pv = [p*zl for p, zl in zip(pv, z)]
                    nverified += 1
    coef = {}
    for k in range(N-1):
        for n in range(k+1):
            m = k-n
            a1, a2 = acoef((n, m))
            coef[n, m] = dict(a1=a1, a2=a2, b1=t[n, m]-t[n+1, m], b2=t[n, m]-t[n, m+1])
    return z, w, coef, nverified


PRIMES = (2147483629, 2147483587)   # primes < 2^31


def int_scaled_moments(N):
    """Integer moments in y=2k-M with integer-scaled weights (positive scaling)."""
    z, w = hahn_inputs(N)
    M = N-1
    y = [2*k-M for k in range(N)]
    assert all(F(yy, M) == zz for yy, zz in zip(y, z))
    out = []
    for ws in w:
        c = math.lcm(*[v.denominator for v in ws])
        W = [int(v*c) for v in ws]
        assert all(F(Wi, c) == v for Wi, v in zip(W, ws)) and all(Wi > 0 for Wi in W)
        out.append([sum(Wi*yy**r for Wi, yy in zip(W, y)) for r in range(2*N+1)])
    return out


def det_nonzero_modp(A, p):
    A = A.copy() % p
    n = A.shape[0]
    for j in range(n):
        piv = np.nonzero(A[j:, j])[0]
        if piv.size == 0:
            return False
        r = j+piv[0]
        if r != j:
            A[[j, r]] = A[[r, j]]
        inv = pow(int(A[j, j]), p-2, p)
        if j+1 < n:
            f = (A[j+1:, j]*inv) % p
            A[j+1:, j:] = (A[j+1:, j:] - (f[:, None]*A[j, j:][None, :]) % p) % p
    return True


def method_modp(N):
    mu = int_scaled_moments(N)
    mus = {p: [np.array([v % p for v in row], dtype=np.int64) for row in mu] for p in PRIMES}
    status = {}
    for k in range(1, N+1):
        for n in range(k+1):
            m = k-n
            ok_any = False
            for p in PRIMES:
                mp_ = mus[p]
                rows = [mp_[0][i:i+k] for i in range(n)]+[mp_[1][i:i+k] for i in range(m)]
                A = np.array(rows, dtype=np.int64)
                if det_nonzero_modp(A, p):
                    ok_any = True
                    break
            status[n, m] = ok_any
    return status


def main():
    mode = sys.argv[1]
    sizes = [int(s) for s in sys.argv[2:]]
    table = committed_table()
    assert sorted(table) == list(range(4, 65))
    for N in sizes:
        t0 = time.monotonic()
        cnt, in_sha, pay_sha = table[N]
        rec = dict(N=N, mode=mode, committed_count=cnt, formula_count=N*(N-1)//2)
        if mode == 'moment':
            z, w, dets, coef = method_moment(N)
            rec['normal_all_deg_le_N'] = all(d != 0 for d in dets.values())
            rec['n_dets'] = len(dets)
            rec['n_mixed_dets_nonzero'] = sum(1 for (n, m), d in dets.items() if n and m and d != 0)
        elif mode == 'recur':
            verify = True
            z, w, coef, nv = method_recur(N, verify=verify)
            rec['orthogonality_conditions_verified'] = nv
        elif mode == 'modp':
            st = method_modp(N)
            z, w = hahn_inputs(N)
            rec['normal_all_deg_le_N_modp'] = all(st.values())
            rec['n_dets'] = len(st)+1
            rec['n_mixed_nonzero'] = sum(1 for (n, m), ok in st.items() if n and m and ok)
            coef = None
        rec['input_sha_match'] = input_sha(z, w) == in_sha
        if coef is not None:
            d = [c['b2']-c['b1'] for c in coef.values()]
            rec['n_sites_le_N-2'] = len(d)
            rec['n_d_nonzero'] = sum(1 for v in d if v != 0)
            rec['min_abs_d'] = str(min(abs(v) for v in d))
            rec['payload_sha_match'] = payload_sha(coef, N) == pay_sha
        rec['seconds'] = round(time.monotonic()-t0, 3)
        print(json.dumps(rec), flush=True)


if __name__ == '__main__':
    main()
