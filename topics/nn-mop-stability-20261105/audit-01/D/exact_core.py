"""Independent exact Fraction machinery (auditor D, written from the definitions
in PD-T286; does not import any repository code).

Moment rows: (s=1, i=0..n-1) then (s=2, i=0..m-1); columns exponents 0..k-1.
"""
from fractions import Fraction as Q


def moments(x, w, K):
    return [sum(wl * xl**k for xl, wl in zip(x, w)) for k in range(K + 1)]


def det(A):
    A = [list(r) for r in A]
    n = len(A)
    d = Q(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return Q(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            if f:
                for k in range(c, n):
                    A[r][k] -= f * A[c][k]
    return d


def solve(A, b):
    n = len(A)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            raise ZeroDivisionError('singular')
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                for k in range(c, n + 1):
                    M[r][k] -= f * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]


def moment_matrix(mom, nu):
    n, m = nu
    k = n + m
    rows = [(0, i) for i in range(n)] + [(1, i) for i in range(m)]
    return [[mom[s][i + j] for j in range(k)] for s, i in rows], rows


def mop(mom, nu):
    """Monic type-II P_nu, coefficient list low->high, via moment solve."""
    A, rows = moment_matrix(mom, nu)
    k = sum(nu)
    if k == 0:
        return [Q(1)]
    rhs = [-mom[s][i + k] for s, i in rows]
    return solve(A, rhs) + [Q(1)]


def peval(p, z):
    v = Q(0)
    for c in reversed(p):
        v = v * z + c
    return v


def functional(x, w, p, shift=0):
    """L(x^shift p)."""
    return sum(wl * xl**shift * peval(p, xl) for xl, wl in zip(x, w))


def indices(K):
    return [(n, k - n) for k in range(K + 1) for n in range(k + 1)]


def nn_exact(x, W):
    """Return (P, D, coeff) with coeff[nu]={'a1','a2','b1','b2'} for |nu|<=N-1.

    Raises if any index of total degree <= N is nonnormal.
    """
    N = len(x)
    mom = [moments(x, w, 2 * N + 1) for w in W]
    P, D = {}, {}
    for nu in indices(N):
        A, _ = moment_matrix(mom, nu)
        D[nu] = det(A) if A else Q(1)
        if D[nu] == 0:
            raise ArithmeticError(('nonnormal', nu))
        P[nu] = mop(mom, nu)
    h = {(nu, s): functional(x, W[s], P[nu], nu[s]) for nu in indices(N - 1) for s in range(2)}
    t = {nu: (P[nu][-2] if sum(nu) else Q(0)) for nu in indices(N)}
    co = {}
    for nu in indices(N - 1):
        r = {}
        for s in range(2):
            up = tuple(v + (i == s) for i, v in enumerate(nu))
            dn = tuple(v - (i == s) for i, v in enumerate(nu))
            r['a%d' % (s + 1)] = h[nu, s] / h[dn, s] if nu[s] else Q(0)
            r['b%d' % (s + 1)] = t[nu] - t[up]
        co[nu] = r
    return P, D, co


def check_nn(x, P, co):
    """Verify the NN identities as polynomial identities (exact)."""
    N = len(x)
    def add(p, q, f=1):
        L = max(len(p), len(q))
        p = p + [Q(0)] * (L - len(p)); q = q + [Q(0)] * (L - len(q))
        return [a + f * b for a, b in zip(p, q)]
    for nu, r in co.items():
        xp = [Q(0)] + P[nu]
        for j in range(2):
            up = tuple(v + (i == j) for i, v in enumerate(nu))
            rhs = add(P[up], P[nu], r['b%d' % (j + 1)])
            for s in range(2):
                if nu[s]:
                    dn = tuple(v - (i == s) for i, v in enumerate(nu))
                    rhs = add(rhs, P[dn], r['a%d' % (s + 1)])
            L = max(len(xp), len(rhs))
            assert xp + [Q(0)] * (L - len(xp)) == rhs + [Q(0)] * (L - len(rhs)), (nu, j)
    return True
