#!/usr/bin/env python3
"""Auditor C: independent exact-Fraction NN reference (PD-T286 moment systems)
and comparison of developer native_mixed.py outputs (LU/QR/SVD/nodeqr).

The input family is rebuilt here from the written definitions
(nodes z=2k/M-1; Krawtchouk p=2/5,1/2; Hahn beta=1,3/2 with alpha=1),
then compared with the frozen c4.inputs for identity only.
Reference: monic type-II P_nu from M_nu c = -rhs, a=h_nu/h_(nu-e_s), b=t_nu-t_(nu+e_j).
"""
import sys, math, importlib.util, json, time
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path('/home/user/padua_research')


def my_inputs(N, family):
    M = N - 1
    x = [Q(2 * k, M) - 1 for k in range(N)]
    if family == 'krawtchouk':
        W = [[Q(math.comb(M, k)) * p ** k * (1 - p) ** (M - k) for k in range(N)] for p in (Q(2, 5), Q(1, 2))]
    else:
        def poch(a, n):
            r = Q(1)
            for i in range(n):
                r *= a + i
            return r
        # Hahn weight with alpha=1: (beta+1)_k/k! * (alpha+1)_(M-k)/(M-k)!
        W = [[poch(b + 1, k) / math.factorial(k) * poch(Q(2), M - k) / math.factorial(M - k) for k in range(N)]
             for b in (Q(1), Q(3, 2))]
    return x, W


def solve(A, b):
    n = len(A)
    A = [row[:] + [bb] for row, bb in zip(A, b)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c] / piv
                A[r] = [u - f * v for u, v in zip(A[r], A[c])]
    return [A[i][n] / A[i][i] for i in range(n)]


def det_nonzero(A):
    n = len(A)
    A = [r[:] for r in A]
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return False
        A[c], A[p] = A[p], A[c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / A[c][c]
                A[r] = [u - f * v for u, v in zip(A[r], A[c])]
    return True


def exact_nn(x, W):
    N = len(x)
    mom = [[sum(w * xi ** k for w, xi in zip(Wr, x)) for k in range(2 * N + 1)] for Wr in W]
    P = {}
    for s in range(N + 1):
        for n in range(s + 1):
            m = s - n
            rows = [[mom[0][i + j] for j in range(s)] for i in range(n)] + [[mom[1][i + j] for j in range(s)] for i in range(m)]
            rhs = [-mom[0][i + s] for i in range(n)] + [-mom[1][i + s] for i in range(m)]
            c = solve(rows, rhs) if s else []
            P[n, m] = c + [Q(1)]  # ascending coefficients, monic
    # check terminal = node polynomial
    F = [Q(1)]
    for xi in x:
        F = [Q(0)] + F
        for k in range(len(F) - 1):
            F[k] -= xi * F[k + 1]
    for n in range(N + 1):
        assert P[n, N - n] == F, 'terminal not node polynomial'

    def h(nu, sidx):
        k = nu[sidx]
        c = P[nu]
        return sum(c[j] * mom[sidx][k + j] for j in range(len(c)))

    def t(nu):
        return P[nu][-2] if sum(nu) else Q(0)
    out = {}
    for s in range(N):
        for n in range(s + 1):
            m = s - n
            nu = (n, m)
            a1 = h(nu, 0) / h((n - 1, m), 0) if n else Q(0)
            a2 = h(nu, 1) / h((n, m - 1), 1) if m else Q(0)
            out[nu] = dict(a1=a1, a2=a2, b1=t(nu) - t((n + 1, m)), b2=t(nu) - t((n, m + 1)))
    return out, P


def verify_recurrence(x, P, out):
    """Check the NN identities exactly as polynomial identities."""
    N = len(x)
    def add(u, v, f=Q(1)):
        L = max(len(u), len(v))
        u = u + [Q(0)] * (L - len(u)); v = v + [Q(0)] * (L - len(v))
        return [a + f * b for a, b in zip(u, v)]
    worst = 0
    for nu, r in out.items():
        n, m = nu
        xp = [Q(0)] + P[nu]
        for j, succ in ((0, (n + 1, m)), (1, (n, m + 1))):
            R = add(xp, P[succ], -1)
            R = add(R, P[nu], -r['b1' if j == 0 else 'b2'])
            if n: R = add(R, P[n - 1, m], -r['a1'])
            if m: R = add(R, P[n, m - 1], -r['a2'])
            assert all(c == 0 for c in R), (nu, j)
    return True


def errE(got, ref):
    es = {}
    for key in ('a1', 'a2', 'b1', 'b2'):
        scale = max(abs(r[key]) for r in ref.values())
        es[key] = max(abs(Q(got[nu][key]) - r[key]) for nu, r in ref.items()) / scale
    return max(es.values()), es


def main():
    spec = importlib.util.spec_from_file_location('nm', ROOT / 'topics/nn-mop-stability-20261105/code/native_mixed.py')
    nm = importlib.util.module_from_spec(spec); spec.loader.exec_module(nm)
    sizes = [int(a) for a in sys.argv[1:]] or [4, 8]
    res = []
    for fam in ('krawtchouk', 'hahn'):
        for N in sizes:
            t0 = time.time()
            x, W = my_inputs(N, fam)
            fx, fW = nm.c4.inputs(N, fam)
            assert x == fx and W == fW, 'input mismatch vs frozen family'
            ref, P = exact_nn(x, W)
            verify_recurrence(x, P, ref)
            row = dict(family=fam, N=N, ref_seconds=round(time.time() - t0, 2))
            for meth in ('lu', 'qr', 'svd', 'nodeqr'):
                co, _ = nm.compute(N, fam, meth)
                E, _ = errE(co, ref)
                row[meth] = float(E)
            # C4 binary64 also
            c4o, _ = nm.c4.compute(N, fam)
            row['c4'] = float(errE(c4o, ref)[0])
            row['gain_lu_digits'] = math.log10(row['c4'] / row['lu'])
            row['gain_nodeqr_digits'] = math.log10(row['c4'] / row['nodeqr'])
            res.append(row)
            print(json.dumps(row), flush=True)


if __name__ == '__main__':
    main()
