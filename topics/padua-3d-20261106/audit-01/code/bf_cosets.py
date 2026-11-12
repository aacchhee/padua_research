#!/usr/bin/env python3
"""Independent brute force (auditor): all subgroups of (Z/M)^3 via HNF lattices,
reflection-invariant cosets tested directly, exact folding, exact rank of the
Pi_n evaluation map over Q(zeta_2M) for |X| = binom(n+3,3).

mode 'all'  : coset invariant under every coordinate negation R_1,R_2,R_3
mode 'R1'   : coset invariant under R_1 only (exploratory, hypothesis necessity)
mode 'cent' : coset invariant under t -> -t only (exploratory)
"""
import sys, itertools as it, math, random
import numpy as np
from sympy import cyclotomic_poly, Poly, symbols, totient, isprime
from sympy.polys.matrices import DomainMatrix
from sympy import ZZ

def divisors(M):
    return [d for d in range(1, M + 1) if M % d == 0]

def subgroups(M, maxsize):
    """All subgroups H of (Z/M)^3 with |H|<=maxsize, via row-HNF of preimage lattice."""
    out = []
    D = divisors(M)
    for h11 in D:
        for h22 in D:
            for h33 in D:
                size = M ** 3 // (h11 * h22 * h33)
                if size > maxsize:
                    continue
                for h12 in range(h22):
                    for h13 in range(h33):
                        for h23 in range(h33):
                            B = np.array([[h11, h12, h13], [0, h22, h23], [0, 0, h33]])
                            ok = True
                            for k in range(3):
                                v = [0, 0, 0]; v[k] = M
                                # solve x B = v with triangular B (rows)
                                x1 = v[0] / h11
                                if x1 != int(x1): ok = False; break
                                r = v[1] - x1 * h12
                                x2 = r / h22
                                if x2 != int(x2): ok = False; break
                                r = v[2] - x1 * h13 - x2 * h23
                                if r % h33: ok = False; break
                            if not ok:
                                continue
                            pts = set()
                            for i in range(M // h11):
                                for j in range(M // h22):
                                    for k in range(M // h33):
                                        p = (i * B[0] + j * B[1] + k * B[2]) % M
                                        pts.add(tuple(int(c) for c in p))
                            # close under addition (safety), check size
                            assert len(pts) == size, (B, len(pts), size)
                            out.append(frozenset(pts))
    assert len(out) == len(set(out))
    return out

def proj_orders(H, M):
    return tuple(len({h[j] for h in H}) for j in range(3))

def negj(p, j, N):
    q = list(p); q[j] = (-q[j]) % N; return tuple(q)

def neg_all(p, N):
    return tuple((-c) % N for c in p)

def find_prime(N):
    p = (1 << 40) // N * N + 1
    while not isprime(p):
        p += N
    return p

def prim_root_of_unity(N, p):
    # element of exact order N in F_p
    for g in range(2, 10 ** 6):
        z = pow(g, (p - 1) // N, p)
        if all(pow(z, N // q, p) != 1 for q in set(primefactors(N))):
            return z

def primefactors(n):
    f, d = [], 2
    while d * d <= n:
        while n % d == 0:
            f.append(d); n //= d
        d += 1
    if n > 1: f.append(n)
    return f

def basis(n):
    return [(a, b, c) for a in range(n + 1) for b in range(n + 1 - a) for c in range(n + 1 - a - b)]

def rank_modp(rows, p):
    A = [r[:] for r in rows]
    rk, ncol = 0, len(A[0])
    for c in range(ncol):
        piv = next((r for r in range(rk, len(A)) if A[r][c] % p), None)
        if piv is None: continue
        A[rk], A[piv] = A[piv], A[rk]
        inv = pow(A[rk][c], p - 2, p)
        for r in range(len(A)):
            if r != rk and A[r][c] % p:
                f = A[r][c] * inv % p
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[rk])]
        rk += 1
    return rk

class Cyclo:
    def __init__(self, N):
        x = symbols('x')
        self.N = N
        self.phi = int(totient(N))
        self.Phi = [int(c) for c in Poly(cyclotomic_poly(N, x), x).all_coeffs()][::-1]  # low->high
        # reduction of x^e, e<N, to basis 1..x^{phi-1}
        self.red = []
        cur = [0] * self.phi; cur[0] = 1
        for e in range(N):
            self.red.append(cur[:])
            # multiply by x
            nxt = [0] + cur[:-1]
            top = cur[-1]
            if top:
                for i in range(self.phi):
                    nxt[i] -= top * self.Phi[i]
            cur = nxt
    def vec(self, coeffs):  # coeffs: dict exponent->int
        v = [0] * self.phi
        for e, c in coeffs.items():
            r = self.red[e % self.N]
            for i in range(self.phi):
                v[i] += c * r[i]
        return v
    def mulmat(self, v):  # phi x phi integer matrix of multiplication by element v (column = image of basis)
        cols = []
        for k in range(self.phi):
            # v * x^k
            coeffs = {}
            for i, c in enumerate(v):
                if c: coeffs[i + k] = coeffs.get(i + k, 0) + c
            cols.append(self.vec(coeffs))
        return [[cols[k][i] for k in range(self.phi)] for i in range(self.phi)]

def entry_coeffs(mode, node):
    # 8*T_a(x)T_b(y)T_c(z) at x_j = cos(2 pi k_j / N): sum over signs of zeta^{+-a k1 +- b k2 +- c k3}
    d = {}
    for s in it.product((1, -1), repeat=3):
        e = sum(si * mi * ki for si, mi, ki in zip(s, mode, node))
        d[e] = d.get(e, 0) + 1
    return d

def exact_rank(cy, nodes, modes):
    big = []
    blocks = [[cy.mulmat(cy.vec(entry_coeffs(m, x))) for m in modes] for x in nodes]
    phi = cy.phi
    for bi in range(len(nodes)):
        for r in range(phi):
            row = []
            for bj in range(len(modes)):
                row.extend(blocks[bi][bj][r])
            big.append(row)
    dm = DomainMatrix([[ZZ(v) for v in row] for row in big], (len(big), len(big[0])), ZZ)
    rq = dm.convert_to(ZZ.get_field()).rank()
    assert rq % phi == 0
    return rq // phi

def modp_rank(N, p, z, nodes, modes):
    rows = []
    for x in nodes:
        row = []
        for m in modes:
            s = 0
            for e, c in entry_coeffs(m, x).items():
                s += c * pow(z, e % N, p)
            row.append(s % p)
        rows.append(row)
    return rank_modp(rows, p)

def run(M, mode, degrees=(1, 2, 3)):
    N = 2 * M
    targets = {n: math.comb(n + 3, 3) for n in degrees}
    maxsize = 8 * max(targets.values())
    Hs = subgroups(M, maxsize)
    p = find_prime(N); z = prim_root_of_unity(N, p)
    cy = Cyclo(N)
    stats = {"M": M, "mode": mode, "subgroups": len(Hs), "inv_subgroups": 0, "cosets": 0}
    hits = {n: {"target_cases": 0, "unisolvent": 0, "deficient_exact": 0} for n in degrees}
    examples = {n: [] for n in degrees}
    classif = {}
    for H in Hs:
        if mode == "all":
            if not all(negj(h, j, M) in H for h in H for j in range(3)):
                continue
        elif mode == "R1":
            if not all(negj(h, 0, M) in H for h in H):
                continue
            if all(negj(h, j, M) in H for h in H for j in range(3)):
                continue  # only genuinely R1-but-not-all
        elif mode == "cent":
            if all(negj(h, j, M) in H for h in H for j in range(3)):
                continue
        stats["inv_subgroups"] += 1
        P = [tuple(2 * c for c in h) for h in H]  # in (Z/N)^3
        seen = set()
        ncos = 0
        for a in it.product(range(N), repeat=3):
            A = frozenset(tuple((ai + pi) % N for ai, pi in zip(a, pp)) for pp in P)
            key = min(A)
            if key in seen:
                continue
            seen.add(key)
            if mode == "all":
                inv = all(negj(u, j, N) in A for u in A for j in range(3))
            elif mode == "R1":
                inv = all(negj(u, 0, N) in A for u in A)
            else:
                inv = all(neg_all(u, N) in A for u in A)
            if not inv:
                continue
            ncos += 1
            X = sorted({tuple(min(c, N - c) for c in u) for u in A})
            stats["cosets"] += 1
            for n, tgt in targets.items():
                if len(X) != tgt:
                    continue
                hits[n]["target_cases"] += 1
                modes = basis(n)
                r = modp_rank(N, p, z, X, modes)
                if r == tgt:
                    hits[n]["unisolvent"] += 1
                    if len(examples[n]) < 3:
                        examples[n].append({"orders": proj_orders(H, M), "Hsize": len(H), "a": a, "X": X})
                else:
                    re = exact_rank(cy, X, modes)
                    if re == tgt:
                        hits[n]["unisolvent"] += 1
                        examples[n].append({"orders": proj_orders(H, M), "Hsize": len(H), "a": a, "X": X, "note": "modp false-singular"})
                    else:
                        hits[n]["deficient_exact"] += 1
        if mode == "all":
            classif.setdefault(proj_orders(H, M), []).append(ncos)
    return stats, hits, examples, classif

if __name__ == "__main__":
    M = int(sys.argv[1]); mode = sys.argv[2]
    degs = tuple(int(x) for x in sys.argv[3].split(",")) if len(sys.argv) > 3 else (1, 2, 3)
    stats, hits, ex, classif = run(M, mode, degs)
    print(stats)
    print(hits)
    for n, e in ex.items():
        for x in e[:2]:
            print("EX n=%d" % n, x)
    if mode == "all":
        # predicted: number of invariant subgroups with orders m = number of unit-free binary codes on E;
        # cosets per subgroup = 2^(#inactive + dim B)
        print("inv subgroups by projection orders (orders: list of #invariant cosets per subgroup)")
        for m in sorted(classif):
            print(" ", m, sorted(classif[m]))

def predicted(m):
    E = [j for j in range(3) if m[j] % 2 == 0]
    vecs = list(range(1, 8))
    subs = {frozenset({0})}
    todo = [frozenset({0})]
    while todo:
        s = todo.pop()
        for v in vecs:
            if any(not ((v >> j) & 1) or j in E for j in range(3)) and all(((v >> j) & 1) == 0 or j in E for j in range(3)):
                t = s | frozenset(x ^ v for x in s)
                if t not in subs:
                    subs.add(t); todo.append(t)
    out = []
    for s in subs:
        if any((1 << j) in s for j in range(3)):
            continue
        dim = len(s).bit_length() - 1
        active = {j for j in range(3) if any((b >> j) & 1 for b in s)}
        out.append((2 ** (3 - len(active) + dim), (m[0]*m[1]*m[2]) // 2**dim))
    return out
