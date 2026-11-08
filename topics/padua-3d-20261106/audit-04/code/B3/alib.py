"""Auditor's own exact/modular helpers (no producer/checker imports)."""
from fractions import Fraction as F
import math
import numpy as np


def modes(n):
    # inherited total-degree order (definition reproduced from the record)
    out = []
    for d in range(n + 1):
        for a in range(d + 1):
            for b in range(d - a + 1):
                out.append((a, b, d - a - b))
    return out


def is_prime(p):
    if p < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if p % q == 0:
            return p == q
    d, s = p - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, p)
        if x in (1, p - 1):
            continue
        for _ in range(s - 1):
            x = x * x % p
            if x == p - 1:
                break
        else:
            return False
    return True


def trial_prime(p):
    # deterministic trial division (slow but independent of Miller-Rabin)
    if p < 2:
        return False
    r = math.isqrt(p)
    if p % 2 == 0:
        return p == 2
    f = 3
    while f <= r:
        if p % f == 0:
            return False
        f += 2
    return True


def factor(L):
    out = []; m = L; f = 2
    while f * f <= m:
        if m % f == 0:
            out.append(f)
            while m % f == 0:
                m //= f
        f += 1
    if m > 1:
        out.append(m)
    return out


def root_of_order(L, p):
    assert (p - 1) % L == 0
    pf = factor(L)
    for g in range(2, p):
        w = pow(g, (p - 1) // L, p)
        if pow(w, L, p) == 1 and all(pow(w, L // q, p) != 1 for q in pf):
            return w
    raise ValueError


def split_prime(L, start):
    p = (start // L) * L + 1
    while p < start or not is_prime(p):
        p += L
    assert p < 2 ** 31
    return p


def rank_mod(A, p):
    """rank and det (if square full) mod p, numpy int64, p<2^31."""
    A = np.array(A, dtype=np.int64) % p
    m, n = A.shape; r = 0; det = 1
    for j in range(n):
        if r == m:
            break
        nz = np.nonzero(A[r:, j])[0]
        if len(nz) == 0:
            det = 0
            continue
        k = r + int(nz[0])
        if k != r:
            A[[r, k]] = A[[k, r]]; det = -det
        piv = int(A[r, j]); det = det * piv % p
        inv = pow(piv, p - 2, p)
        A[r] = A[r] * inv % p
        col = A[r + 1:, j].copy()
        if len(col):
            A[r + 1:] = (A[r + 1:] - (col[:, None] * A[r][None, :]) % p) % p
        r += 1
    return r, (det % p if (m == n == r) else 0)


def bareiss_rank(M):
    """exact rank of an integer matrix by fraction-free elimination."""
    A = [list(map(int, row)) for row in M if any(row)]
    if not A:
        return 0
    m, n = len(A), len(A[0]); r = 0; prev = 1
    for j in range(n):
        piv = None
        for i in range(r, m):
            if A[i][j]:
                piv = i; break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pr = A[r]; a = pr[j]
        for i in range(r + 1, m):
            row = A[i]; b = row[j]
            if b:
                A[i] = [(a * row[k] - b * pr[k]) // prev for k in range(n)]
            else:
                A[i] = [(a * row[k]) // prev for k in range(n)]
        prev = a; r += 1
        if r == m:
            break
    return r


def frac_inverse(M):
    n = len(M)
    A = [[F(x) for x in row] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for j in range(n):
        p = next(i for i in range(j, n) if A[i][j] != 0)
        A[j], A[p] = A[p], A[j]
        pv = A[j][j]; A[j] = [x / pv for x in A[j]]
        for i in range(n):
            if i != j and A[i][j] != 0:
                f = A[i][j]; A[i] = [x - f * y for x, y in zip(A[i], A[j])]
    return [row[n:] for row in A]


def perfect_matching(adj, n):
    """Kuhn augmenting paths; adj[row] = list of cols. returns col->row or None"""
    import sys
    sys.setrecursionlimit(10000)
    match_col = [-1] * n
    def aug(r, seen):
        for c in adj[r]:
            if not seen[c]:
                seen[c] = True
                if match_col[c] == -1 or aug(match_col[c], seen):
                    match_col[c] = r
                    return True
        return False
    for r in range(n):
        if not aug(r, [False] * n):
            return None
    return match_col


def has_alternating_cycle(adj, match_col, n):
    """digraph on rows: r -> match_col[c] for each c in adj[r], c not matched to r."""
    row_of = match_col
    col_of = [None] * n
    for c, r in enumerate(row_of):
        col_of[r] = c
    g = [[row_of[c] for c in adj[r] if c != col_of[r]] for r in range(n)]
    color = [0] * n
    for s in range(n):
        if color[s]:
            continue
        stack = [(s, 0)]; color[s] = 1
        while stack:
            u, i = stack[-1]
            if i < len(g[u]):
                stack[-1] = (u, i + 1); v = g[u][i]
                if color[v] == 1:
                    return True
                if color[v] == 0:
                    color[v] = 1; stack.append((v, 0))
            else:
                color[u] = 2; stack.pop()
    return False


def sparse_gcd_rank(M):
    """exact Q-rank: sparse integer elimination; each row update a*row-b*piv then gcd-normalize."""
    rows = []
    for row in M:
        d = {j: int(v) for j, v in enumerate(row) if v}
        if d:
            rows.append(d)
    rank = 0
    while rows:
        # pick pivot: row with fewest entries, its smallest column
        k = min(range(len(rows)), key=lambda i: len(rows[i]))
        pr = rows.pop(k)
        j = min(pr); a = pr[j]
        new = []
        for row in rows:
            b = row.get(j)
            if not b:
                new.append(row); continue
            g0 = math.gcd(a, b); aa, bb = a // g0, b // g0
            out = {c: aa * v for c, v in row.items()}
            for c, v in pr.items():
                out[c] = out.get(c, 0) - bb * v
            out = {c: v for c, v in out.items() if v}
            if out:
                g = 0
                for v in out.values():
                    g = math.gcd(g, v)
                    if g == 1:
                        break
                if g > 1:
                    out = {c: v // g for c, v in out.items()}
                new.append(out)
        rows = new
        rank += 1
    return rank
