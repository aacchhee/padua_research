#!/usr/bin/env python3
"""Independent exact arithmetic U1 checks; measurements, not a finite reduction."""
from fractions import Fraction
from itertools import permutations, product
import hashlib
import json
import platform
import random
from pathlib import Path


class Field:
    def __init__(self, name, p=0, polynomial=0):
        self.name, self.p, self.polynomial = name, p, polynomial
        self.q = (1 << (polynomial.bit_length() - 1)) if polynomial else p

    def n(self, x):
        return Fraction(x) if not self.p else x % self.p

    def add(self, x, y):
        return x ^ y if self.polynomial else self.n(x + y)

    def neg(self, x):
        return x if self.polynomial else self.n(-x)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        if not self.polynomial:
            return self.n(x * y)
        result = 0
        while y:
            if y & 1:
                result ^= x
            y >>= 1
            x <<= 1
            if x & self.q:
                x ^= self.polynomial
        return result

    def pow(self, x, n):
        result = self.n(1)
        while n:
            if n & 1:
                result = self.mul(result, x)
            x = self.mul(x, x)
            n >>= 1
        return result

    def inv(self, x):
        assert x != 0
        return 1 / x if not self.p else self.pow(x, self.q - 2)

    def total(self, items):
        result = self.n(0)
        for x in items:
            result = self.add(result, x)
        return result

    def prod(self, items):
        result = self.n(1)
        for x in items:
            result = self.mul(result, x)
        return result


def det(A, F):
    A = [list(row) for row in A]
    result = F.n(1)
    for j in range(len(A)):
        pivot = next((i for i in range(j, len(A)) if A[i][j]), None)
        if pivot is None:
            return F.n(0)
        if pivot != j:
            A[pivot], A[j] = A[j], A[pivot]
            result = F.neg(result)
        v = A[j][j]
        result = F.mul(result, v)
        vi = F.inv(v)
        for i in range(j + 1, len(A)):
            scale = F.mul(A[i][j], vi)
            if scale:
                for k in range(j + 1, len(A)):
                    A[i][k] = F.sub(A[i][k], F.mul(scale, A[j][k]))
                A[i][j] = F.n(0)
    return result


def axis(H, F):
    L = len(H)
    w = [F.inv(F.prod(F.sub(h, t) for j, t in enumerate(H) if i != j))
         for i, h in enumerate(H)]
    mu = [F.total(F.mul(F.mul(F.n((-1) ** i), w[i]), F.pow(h, t))
                  for i, h in enumerate(H)) for t in range(2 * L - 1)]
    eta = [F.total(F.mul(w[i], F.pow(h, t))
                   for i, h in enumerate(H) if i % 2 == 0)
           for t in range(2 * (L // 2) - 1)]
    delta = [F.n(1)] + [det([[mu[a + b] for b in range(r)] for a in range(r)], F)
                        for r in range(1, L + 1)]
    hankel = [F.n(1)] + [det([[eta[a + b] for b in range(r)] for a in range(r)], F)
                         for r in range(1, L // 2 + 1)]
    assert delta[L] == F.n(1), (F.name, H, "full determinant", delta)
    assert all(delta[r] == delta[L - r] for r in range(L + 1)), (F.name, H, "complement")
    assert all(delta[r] == F.mul(F.pow(F.n(2), r), hankel[r])
               for r in range(L // 2 + 1)), (F.name, H, "normalization")
    assert hankel[L // 2] != 0, (F.name, H, "central factor")
    k = L // 2
    C = F.mul(F.pow(hankel[k], 1 if L % 2 == 0 else 2),
              F.prod(F.pow(hankel[r], 2) for r in range(1, k)))
    return w, delta, hankel, C


def check(X, Y, F):
    m = len(X) - 1
    assert len(Y) == m + 2
    wx, dx, hx, cx = axis(X, F)
    wy, dy, hy, cy = axis(Y, F)
    prediction = all(hx[1:(len(X) - 2) // 2 + 1]) and all(hy[1:(len(Y) - 2) // 2 + 1])
    original = all(dx[1:-1]) and all(dy[1:-1])
    mon = [(a, d - a) for d in range(m + 1) for a in range(d + 1)]
    determinants = []
    for e in (0, 1):
        nodes = [(i, j) for i in range(m + 1) for j in range(m + 2) if (i + j) % 2 == e]
        assert len(nodes) == len(mon)
        E = [[F.mul(F.pow(X[i], a), F.pow(Y[j], b)) for a, b in mon] for i, j in nodes]
        d = det(E, F)
        determinants.append(d)
        lhs = F.mul(F.mul(F.n((-1) ** (e * len(mon))), F.pow(d, 2)),
                    F.prod(F.mul(wx[i], wy[j]) for i, j in nodes))
        assert lhs == F.mul(cx, cy), (F.name, X, Y, e, "allchar identity", lhs, cx, cy)
        assert bool(d) == bool(prediction), (F.name, X, Y, e, "corrected iff")
        if F.p != 2:
            assert bool(d) == bool(original), (F.name, X, Y, e, "odd iff")
    assert bool(determinants[0]) == bool(determinants[1])
    return bool(determinants[0]), original


def main():
    print("INDEPENDENT U1 EXACT CHECK; all aggregate coverage is MEASURED")
    print("python", platform.python_version(), "platform", platform.platform())
    print("source_sha256", hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    seed = 20261031071
    rng = random.Random(seed)
    print("seed", seed)
    fields = [Field("F2", 2), Field("F3", 3), Field("F5", 5), Field("F7", 7),
              Field("F11", 11), Field("F17", 17), Field("GF4", 2, 0b111),
              Field("GF8", 2, 0b1011), Field("GF16", 2, 0b10011), Field("Q")]
    for F in fields:
        if F.p:
            for x in range(1, F.q):
                assert F.mul(x, F.inv(x)) == 1
    print("finite-field inverse checks passed; extension basis moduli: GF4=7 GF8=11 GF16=19")
    total = 0
    for F in fields:
        for m in range(min(6, F.q - 2) + 1 if F.p else 7):
            exhaustive = (F.q <= 4 and F.p) or (F.name == "F5" and m == 2)
            count, singular, false_original = 0, 0, 0
            digest = hashlib.sha256()
            if exhaustive:
                cases = product(permutations(range(F.q), m + 1), permutations(range(F.q), m + 2))
            elif F.p:
                cases = [(rng.sample(range(F.q), m + 1), rng.sample(range(F.q), m + 2)) for _ in range(30)]
            else:
                cases = [(list(map(F.n, rng.sample(range(-20, 21), m + 1))),
                          list(map(F.n, rng.sample(range(-20, 21), m + 2)))) for _ in range(8)]
            for X, Y in cases:
                digest.update((str(tuple(X)) + str(tuple(Y)) + "\n").encode())
                good, original = check(X, Y, F)
                count += 1
                singular += not good
                false_original += good != original
            total += count
            print(json.dumps({"field": F.name, "m": m, "mode": "exhaustive" if exhaustive else "seeded",
                              "labelled_axis_pairs": count, "singular_both_parities": singular,
                              "original_iff_mismatches": false_original, "input_sha256": digest.hexdigest()}, sort_keys=True))
    print("PASS axis pairs", total, "checkerboards", 2 * total)
    print("Each case checked both parity determinants, allchar normalized squared identity, odd-char iff,")
    print("allchar shortened iff, full alt determinant=1, complementary minors, normalization, central nonvanishing.")


if __name__ == "__main__":
    main()
