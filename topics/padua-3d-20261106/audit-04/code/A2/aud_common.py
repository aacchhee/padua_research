"""Auditor's own exact helpers (Claude audit04-A2). Imports no project code."""
import math, itertools as it
from fractions import Fraction
from sympy.polys.matrices import DomainMatrix
from sympy import ZZ, QQ, isprime as sp_isprime

def total_modes(n):
    # my own ordering: reverse-lex over total degree, different from producer/checker
    out = []
    for d in range(n, -1, -1):
        for a in range(d, -1, -1):
            for b in range(d - a, -1, -1):
                out.append((a, b, d - a - b))
    return out

def mono_dct_matrix(n, z):
    """Integer matrix C' with monomial-evaluation V_mono = B C' D^{-1},
    B_{k,r}=cos(r theta_k), theta_k=(2k+1)pi/M, M=2N, D=diag(2^(|alpha|+3)).
    Expansion: cos(u)^a = 2^-a sum_i binom(a,i) cos((a-2i)u)."""
    N = math.comb(n + 3, 3); M = 2 * N; P = 2 * M
    modes = total_modes(n)
    C = [[0] * N for _ in range(N)]
    for col, al in enumerate(modes):
        terms = [[(math.comb(a, i), (a - 2 * i) * zj) for i in range(a + 1)] for a, zj in zip(al, z)]
        for (c1, m1), (c2, m2), (c3, m3) in it.product(*terms):
            w = c1 * c2 * c3
            for e2 in (1, -1):
                for e3 in (1, -1):
                    for e1 in (1, -1):
                        m = (e1 * m1 + e2 * m2 + e3 * m3) % P
                        r = min(m, P - m)
                        s = 1
                        if r > N:
                            r, s = M - r, -1
                        if r == N:
                            continue
                        C[r][col] += s * w
    return C, modes

def exact_rank(C):
    return DomainMatrix([[ZZ(x) for x in row] for row in C], (len(C), len(C[0])), ZZ).convert_to(QQ).rank()

def exact_det(C):
    return int(DomainMatrix([[ZZ(x) for x in row] for row in C], (len(C), len(C)), ZZ).det())

def fold_nodes(z, nums, D, Mord):
    L = math.lcm(Mord, D)
    s = set()
    for k in range(Mord):
        s.add(tuple(min(v, L - v) for v in ((k * zj * (L // Mord) + aj * (L // D)) % L for zj, aj in zip(z, nums))))
    return L, sorted(s)

def prime_factors(n):
    out, q = [], 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1: out.append(n)
    return out

def split_prime(L, floor):
    p = (floor // L + 1) * L + 1
    while not sp_isprime(p):
        p += L
    fac = prime_factors(L)
    g = 2
    while True:
        w = pow(g, (p - 1) // L, p)
        if all(pow(w, L // q, p) != 1 for q in fac):
            assert pow(w, L, p) == 1
            return p, w
        g += 1

def modrank_det(A, p):
    """pure Python ints; returns rank and det (if square full rank)"""
    A = [[x % p for x in row] for row in A]
    nr, nc = len(A), len(A[0]); r = 0; det = 1
    for c in range(nc):
        piv = next((i for i in range(r, nr) if A[i][c]), None)
        if piv is None:
            det = 0; continue
        if piv != r:
            A[r], A[piv] = A[piv], A[r]; det = -det
        pv = A[r][c]; det = det * pv % p
        inv = pow(pv, -1, p)
        prow = [x * inv % p for x in A[r]]
        A[r] = prow
        for i in range(r + 1, nr):
            f = A[i][c]
            if f:
                Ai = A[i]
                A[i] = [(x - f * y) % p for x, y in zip(Ai, prow)]
        r += 1
        if r == nr: break
    return r, (det % p if (nr == nc and r == nc) else None)
