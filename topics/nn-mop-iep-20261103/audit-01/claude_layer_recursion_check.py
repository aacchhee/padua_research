#!/usr/bin/env python3
"""Claude audit-01 check: which divisors does marginal-data NN reconstruction need?

Written by the auditor from scratch (imports nothing from the topic's code).
Standard library only; exact Fraction arithmetic; deterministic inputs.

For common nodes x_l and positive weights w_{1,l}, w_{2,l} it
 1. computes ground-truth monic type-II P_nu (|nu| <= N) by solving the
    orthogonality conditions written through node values, and the NN
    coefficients (|nu| <= N-1) by polynomial coefficient matching;
 2. computes the two marginal Jacobi recurrences (Stieltjes, exact) and
    checks they equal the axis NN coefficients;
 3. rebuilds every NN coefficient on |nu| <= N-1 from marginal data alone by
    the layer recursion derived in audit-01.md (A-relations and B-relations),
    recording the total degree of every divisor d_nu = b_{nu,2} - b_{nu,1};
 4. counts sites where b_{nu+e1,2} != b_{nu,2} (full-lattice operators
    H_1, H_2 then fail to commute; see audit-01.md).
Assertions are the checks; run without -O.
"""
from fractions import Fraction as Q
from math import comb
import hashlib
import json
import platform
import random
import sys
from pathlib import Path


def pmul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def padd(p, q, c=Q(1)):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + c * (q[i] if i < len(q) else 0) for i in range(n)]


def peval(p, t):
    v = Q(0)
    for c in reversed(p):
        v = v * t + c
    return v


def solve(a, rhs):
    """Exact Gauss-Jordan; returns None if singular."""
    n = len(rhs)
    m = [list(r) + [b] for r, b in zip(a, rhs)]
    for k in range(n):
        piv = next((i for i in range(k, n) if m[i][k] != 0), None)
        if piv is None:
            return None
        m[k], m[piv] = m[piv], m[k]
        inv = 1 / m[k][k]
        m[k] = [z * inv for z in m[k]]
        for i in range(n):
            if i != k and m[i][k] != 0:
                f = m[i][k]
                m[i] = [z - f * w for z, w in zip(m[i], m[k])]
    return [m[i][n] for i in range(n)]


def strip(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def ground_truth(nodes, w):
    N = len(nodes)
    P = {}
    for k in range(N + 1):
        for n in range(k + 1):
            m = k - n
            # unknown lower coefficients c_0..c_{k-1}; condition sum_l w x^i (x^k + sum c_j x^j) = 0
            rows, rhs = [], []
            for s, cnt in ((0, n), (1, m)):
                for i in range(cnt):
                    rows.append([sum(w[s][l] * nodes[l] ** (i + j) for l in range(N)) for j in range(k)])
                    rhs.append(-sum(w[s][l] * nodes[l] ** (i + k) for l in range(N)))
            c = solve(rows, rhs)
            assert c is not None, ('nonnormal', n, m)
            P[n, m] = c + [Q(1)]
    co = {}
    for (n, m), p in P.items():
        k = n + m
        if k > N - 1:
            continue
        basis = [p] + ([P[n - 1, m]] if n else []) + ([P[n, m - 1]] if m else [])
        sol = []
        for succ in ((n + 1, m), (n, m + 1)):
            r = padd(pmul([Q(0), Q(1)], p), P[succ], Q(-1))
            r = (r + [Q(0)] * (k + 1))[:k + 1]
            assert all(v == 0 for v in padd(pmul([Q(0), Q(1)], p), P[succ], Q(-1))[k + 1:])
            # square system: compare coefficients of x^0..x^k against basis (rank len(basis))
            # choose rows by least squares-free approach: use all k+1 rows via normal equations
            A = [[b[i] if i < len(b) else Q(0) for b in basis] for i in range(k + 1)]
            AtA = [[sum(A[i][u] * A[i][v] for i in range(k + 1)) for v in range(len(basis))] for u in range(len(basis))]
            Atr = [sum(A[i][u] * r[i] for i in range(k + 1)) for u in range(len(basis))]
            z = solve(AtA, Atr)
            assert z is not None
            chk = [sum(A[i][u] * z[u] for u in range(len(basis))) for i in range(k + 1)]
            assert chk == r, 'residual not in predecessor span'
            sol.append(z)
        b1, b2 = sol[0][0], sol[1][0]
        assert sol[0][1:] == sol[1][1:], 'lower coefficients differ between directions'
        a1 = sol[0][1] if n else Q(0)
        a2 = sol[0][-1] if m else Q(0)
        co[n, m] = dict(a1=a1, a2=a2, b1=b1, b2=b2)
    return P, co


def marginal_jacobi(nodes, ws):
    """Exact Stieltjes: monic OPs p_{n+1} = (x-beta_n) p_n - alpha_n p_{n-1}."""
    N = len(nodes)
    ip = lambda f, g: sum(wl * f[l] * g[l] for l, wl in enumerate(ws))
    prev, cur = [Q(0)] * N, [Q(1)] * N
    beta, alpha = [], []
    nrm_prev = None
    for n in range(N):
        nrm = ip(cur, cur)
        bn = ip([t * v for t, v in zip(nodes, cur)], cur) / nrm
        an = nrm / nrm_prev if n else Q(0)
        beta.append(bn)
        alpha.append(an)
        nxt = [(t - bn) * v - an * u for t, v, u in zip(nodes, cur, prev)]
        prev, cur, nrm_prev = cur, nxt, nrm
    return beta, alpha


def layer_recursion(N, mar1, mar2):
    """Rebuild NN coefficients on |nu|<=N-1 from marginal data; record divisor degrees."""
    (be1, al1), (be2, al2) = mar1, mar2
    c = {(0, 0): dict(a1=Q(0), a2=Q(0), b1=be1[0], b2=be2[0])}
    div_degrees = []

    def d(nu):
        return c[nu]['b2'] - c[nu]['b1']

    def div(num, nu):
        den = d(nu)
        div_degrees.append(sum(nu))
        assert den != 0, ('zero divisor', nu)
        return num / den

    for s in range(N - 1):  # build layer s+1 from layers s, s-1
        new = {}
        for p in range(s + 2):
            q = s + 1 - p
            e = {}
            # A-relations
            if p == 0:
                e['a1'] = Q(0)
            elif q == 0:
                e['a1'] = al1[p]
            else:
                nu = (p, q - 1)
                e['a1'] = div(c[nu]['a1'] * d(nu), (p - 1, q - 1))
            if q == 0:
                e['a2'] = Q(0)
            elif p == 0:
                e['a2'] = al2[q]
            else:
                nu = (p - 1, q)
                e['a2'] = div(c[nu]['a2'] * d(nu), (p - 1, q - 1))
            new[p, q] = e
        for p in range(s + 1):  # nu on layer s
            nu = (p, s - p)
            up1, up2 = (p + 1, s - p), (p, s - p + 1)
            lhs = new[up1]['a1'] - new[up2]['a2'] + new[up1]['a2'] - new[up2]['a1']
            new[up2]['b1'] = c[nu]['b1'] - div(lhs, nu)
            new[up1]['b2'] = new[up2]['b1'] + d(nu)
        new[s + 1, 0]['b1'] = be1[s + 1]
        new[0, s + 1]['b2'] = be2[s + 1]
        c.update(new)
    return c, div_degrees


def inputs():
    cases = []
    for N in range(2, 9):
        cases.append(('generic', N, [Q(k * k + k + 1, k + 2) for k in range(N)],
                      [[Q(2, 3) ** k for k in range(N)], [Q(3, 5) ** k for k in range(N)]]))
        cases.append(('binomial', N, [Q(k) for k in range(N)],
                      [[Q(comb(N - 1, k)) * Q(1, 3) ** k * Q(2, 3) ** (N - 1 - k) for k in range(N)],
                       [Q(comb(N - 1, k)) * Q(2, 3) ** k * Q(1, 3) ** (N - 1 - k) for k in range(N)]]))
    cases.append(('astra-N4', 4, [Q(v) for v in (-2, 0, 1, 3)],
                  [[Q(v) for v in (1, 2, 3, 5)], [Q(v) for v in (2, 3, 5, 11)]]))
    rng = random.Random(20261105)
    for N in range(2, 11):
        nodes = sorted(set(Q(rng.randint(-40, 40), rng.randint(1, 9)) for _ in range(3 * N)))
        nodes = rng.sample(nodes, N)
        w = [[Q(rng.randint(1, 30), rng.randint(1, 7)) for _ in range(N)] for _ in range(2)]
        cases.append(('seeded', N, nodes, w))
    return cases


def main():
    if not __debug__:
        raise RuntimeError('run without -O')
    out, tot = [], dict(cases=0, coeff_sites=0, axis_marginal_matches=0, divisions=0,
                        max_divisor_degree_minus_N=-10**9, lattice_noncommuting_sites=0,
                        terminal_d_zero=0)
    for fam, N, nodes, w in inputs():
        P, co = ground_truth(nodes, w)
        mar1, mar2 = marginal_jacobi(nodes, w[0]), marginal_jacobi(nodes, w[1])
        for n in range(N):
            assert co[n, 0]['b1'] == mar1[0][n] and co[n, 0]['a1'] == mar1[1][n]
            assert co[0, n]['b2'] == mar2[0][n] and co[0, n]['a2'] == mar2[1][n]
            tot['axis_marginal_matches'] += 2
        rec, degs = layer_recursion(N, mar1, mar2)
        assert set(rec) == set(co)
        for nu in co:
            assert rec[nu] == co[nu], (fam, N, nu)
        term = sum(1 for nu in co if sum(nu) == N - 1 and co[nu]['b1'] == co[nu]['b2'])
        assert term == N  # all N terminal sites have d = 0
        noncomm = sum(1 for (n, m) in co if n + m <= N - 2 and co[n + 1, m]['b2'] != co[n, m]['b2'])
        maxdeg = max(degs) if degs else None
        if degs:
            assert maxdeg <= N - 2
            tot['max_divisor_degree_minus_N'] = max(tot['max_divisor_degree_minus_N'], maxdeg - N)
        tot['cases'] += 1
        tot['coeff_sites'] += len(co)
        tot['divisions'] += len(degs)
        tot['lattice_noncommuting_sites'] += noncomm
        tot['terminal_d_zero'] += term
        ident = json.dumps({'nodes': [str(t) for t in nodes], 'weights': [[str(v) for v in r] for r in w]})
        out.append(dict(family=fam, N=N, input_sha256=hashlib.sha256(ident.encode()).hexdigest(),
                        sites=len(co), divisions=len(degs), max_divisor_degree=maxdeg,
                        terminal_d_zero=term, b2_shift_e1_differs=noncomm))
    print(json.dumps(dict(status='MEASURED finite exact audit check; no general proof',
                          python=platform.python_version(),
                          code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                          totals=tot, cases=out, all_passed=True), indent=1, sort_keys=True))


if __name__ == '__main__':
    sys.exit(main())
