#!/usr/bin/env python3
"""Exact verification of U1 identities. Finite tests support, but do not prove, scope.

No external finite-field package is trusted: prime fields and binary extensions
are implemented below. Optional symbolic factorization uses SymPy and is separate.
"""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import random
import sys


class Field:
    def __init__(self, p, modulus=None):
        self.p, self.modulus = p, modulus
        self.q = p if modulus is None else 1 << (modulus.bit_length() - 1)
        self.name = f"F{p}" if modulus is None else f"F{self.q}[mod={modulus:#b}]"

    def add(self, a, b):
        return (a + b) % self.p if self.modulus is None else a ^ b

    def neg(self, a):
        return (-a) % self.p if self.modulus is None else a

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.modulus is None:
            return a * b % self.p
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.modulus
        return out

    def pow(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def inv(self, a):
        assert a
        return self.pow(a, self.q - 2)

    def prod(self, xs):
        out = 1
        for x in xs:
            out = self.mul(out, x)
        return out

    def sum(self, xs):
        out = 0
        for x in xs:
            out = self.add(out, x)
        return out


def determinant(F, A):
    A = [row[:] for row in A]
    n, out = len(A), 1
    assert all(len(row) == n for row in A)
    for j in range(n):
        pivot = next((i for i in range(j, n) if A[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            out = F.neg(out)
        out = F.mul(out, A[j][j])
        inv = F.inv(A[j][j])
        for i in range(j + 1, n):
            scale = F.mul(A[i][j], inv)
            for k in range(j + 1, n):
                A[i][k] = F.sub(A[i][k], F.mul(scale, A[j][k]))
    return out


def monomials(m):
    return [(a, d - a) for d in range(m + 1) for a in range(d, -1, -1)]


def moments(F, H, even_only=False):
    bare = [F.inv(F.prod(F.sub(h, t) for j, t in enumerate(H) if j != i))
            for i, h in enumerate(H)]
    weights = [w if i % 2 == 0 else F.neg(w) for i, w in enumerate(bare)]
    selected = [(h, bare[i]) for i, h in enumerate(H) if i % 2 == 0] if even_only else list(zip(H, weights))
    mu = [F.sum(F.mul(w, F.pow(h, k)) for h, w in selected) for k in range(2 * len(H))]
    minors = [1] + [determinant(F, [[mu[i + j] for j in range(r)] for i in range(r)])
                    for r in range(1, len(H) + 1)]
    return weights, minors


def one_case(F, m, X, Y):
    wx, dx = moments(F, X)
    wy, dy = moments(F, Y)
    _, hx = moments(F, X, True)
    _, hy = moments(F, Y, True)
    assert dx[-1] == dy[-1] == 1
    for H, d, h in ((X, dx, hx), (Y, dy, hy)):
        L = len(H)
        for r in range(L + 1):
            assert d[r] == d[L - r]
        for r in range(1, L // 2 + 1):
            assert d[r] == F.mul(F.pow(F.add(1, 1), r), h[r])
        if L % 2:
            assert h[L // 2] != 0
    Hminors = [h[r] for H, h in ((X, hx), (Y, hy))
               for r in range(1, (len(H) - 2) // 2 + 1)]
    corrected = all(Hminors)
    original = all(dx[1:-1]) and all(dy[1:-1])
    E, he = (X, hx) if len(X) % 2 == 0 else (Y, hy)
    A = he[len(E) // 2]
    assert A
    Q = F.prod(h[r] for H, h in ((X, hx), (Y, hy))
               for r in range(1, (len(H) - 1) // 2 + 1))
    N = (m + 1) * (m + 2) // 2
    ds = []
    for e in (0, 1):
        ijs = [(i, j) for i in range(len(X)) for j in range(len(Y)) if (i + j) % 2 == e]
        assert len(ijs) == N
        V = [[F.mul(F.pow(X[i], a), F.pow(Y[j], b)) for a, b in monomials(m)] for i, j in ijs]
        d = determinant(F, V)
        ds.append(d)
        W = F.prod(F.mul(wx[i], wy[j]) for i, j in ijs)
        lhs = F.mul(F.mul(d, d), W)
        rhs = F.mul(A, F.mul(Q, Q))
        assert lhs == rhs, (F.name, m, X, Y, e, "divided identity", lhs, rhs)
        assert bool(d) == corrected, (F.name, m, X, Y, e, "corrected iff")
        if F.p != 2:
            raw = F.prod(dx[1:m + 2] + dy[1:m + 2])
            assert lhs == F.mul(F.inv(F.pow(2, N)), raw)
            assert bool(d) == original
    assert bool(ds[0]) == bool(ds[1])
    return {"determinants": ds, "original_qd": original, "corrected": corrected}


def finite_run(samples, seed):
    rng = random.Random(seed)
    fields = [Field(p) for p in (2, 3, 5, 7, 11, 13, 31)]
    fields += [Field(2, z) for z in (0b111, 0b1011, 0b10011)]
    scopes, total, agreements = [], 0, 0
    for F in fields:
        for m in range(min(7, F.q - 2) + 1):
            good = bad_original = overlap = 0
            for _ in range(samples):
                X = rng.sample(range(F.q), m + 1)
                Y = rng.sample(range(F.q), m + 2)
                overlap += bool(set(X) & set(Y))
                result = one_case(F, m, X, Y)
                good += result["corrected"]
                bad_original += result["original_qd"] != result["corrected"]
                agreements += 1
            total += samples
            scopes.append({"field": F.name, "m": m, "labellings": samples,
                           "unisolvent": good, "original_iff_mismatches": bad_original,
                           "cross_axis_overlap": overlap})
    # All labelled X,Y at the smallest nontrivial binary extension edge.
    F = Field(2, 0b111)
    exhaustive = 0
    for X in itertools.permutations(range(4), 2):
        for Y in itertools.permutations(range(4), 3):
            result = one_case(F, 1, X, Y)
            assert result["corrected"] and not result["original_qd"]
            exhaustive += 1
    explicit = []
    for F, m, X, Y in [(Field(2, 0b111), 1, [0, 1], [0, 1, 2]),
                        (Field(2, 0b1011), 2, [0, 1, 2], [0, 1, 2, 4])]:
        explicit.append({"field": F.name, "m": m, "X": X, "Y": Y, **one_case(F, m, X, Y)})
    return {"seed": seed, "samples_per_setting": samples, "random_labellings": total,
            "parity_checks": 2 * total, "settings": scopes,
            "exhaustive_F4_m1_labellings": exhaustive,
            "exhaustive_F4_m1_parity_checks": 2 * exhaustive,
            "explicit_examples": explicit, "all_assertions": "PASS"}


def symbolic_run():
    import sympy as s
    result = []
    for m in (2, 3, 4):
        X, Y = s.symbols(f"x0:{m+1}"), s.symbols(f"y0:{m+2}")
        # Axis minors are rational functions with only node-difference denominators.
        axis = []
        minor_expressions = []
        for H in (X, Y):
            E, O = H[::2], H[1::2]
            u = s.Symbol("u")
            c = s.prod(u-z for z in O)
            VE = s.prod(E[j]-E[i] for i in range(len(E)) for j in range(i+1,len(E)))
            resultant = s.prod(c.subs(u,z) for z in E)
            for r in range(1, (len(H) - 1) // 2 + 1):
                # Exact Laplace/Cauchy--Binet bridge, with sign fixed:
                # H_r=(-1)^(r(a-r)+r(r-1)/2) D_r/(V(E)*prod_E c).
                # Each D_r is a polynomial determinant of size <=3 here.
                columns = [u**j for j in range(r)] + [u**j*c for j in range(len(E)-r)]
                D = s.det(s.Matrix([[f.subs(u,z) for f in columns] for z in E]))
                numerator = s.factor(D/VE)
                sign = (-1)**(r*(len(E)-r)+r*(r-1)//2)
                minor = s.factor(sign*numerator/resultant)
                axis.append({"axis": "X" if H == X else "Y", "r": r, "minor": str(minor)})
                minor_expressions.append(minor)
        E = X if len(X) % 2 == 0 else Y
        for e in (0, 1):
            ijs = [(i,j) for i in range(len(X)) for j in range(len(Y)) if (i+j)%2 == e]
            # Assemble the already-factored rational identity without expanding
            # a high-degree multivariate numerator and denominator together.
            # In canonical differences d_ij=h_i-h_j (i<j), w_i=1/prod_j d_ij.
            powers = {}
            coeff = s.Integer(1)
            def add(base, power):
                powers[base] = powers.get(base, 0) + power
            for H, other in ((X,Y),(Y,X)):
                counts = [sum((i+j)%2 == e for j in range(len(other))) for i in range(len(H))]
                for i in range(len(H)):
                    for j in range(i+1,len(H)):
                        add(H[i]-H[j], counts[i]+counts[j])  # W^(-1)
            for i in range(len(E)):
                for j in range(i+1,len(E)):
                    if (i+j)%2:
                        add(E[i]-E[j], -1)  # A_even
            for minor in minor_expressions:
                numer, denom = s.fraction(minor)
                for expr, sign in ((numer,1),(denom,-1)):
                    c, ff = s.factor_list(expr)
                    coeff *= c**(2*sign)
                    for base,power in ff:
                        add(base, 2*sign*power)
            factors = sorted([(f,p) for f,p in powers.items() if p], key=lambda z:str(z[0]))
            assert all(power >= 0 for _,power in factors)
            assert all(power % 2 == 0 for _, power in factors)
            assert coeff in (1, -1)
            assert coeff == 1
            candidate = s.prod(base**(power//2) for base,power in factors)
            # Verify sign and the entire polynomial on an exact one-variable slice.
            t = s.Symbol("t")
            xv = [0, 1, 3, 7, 11][:m+1]
            yv = [0, 2, 5, 9, 14, t][:m+2]
            yv[-1] = t
            subs = dict(zip(X,xv)) | dict(zip(Y,yv))
            V = s.Matrix([[xx**a*yy**b for a,b in monomials(m)]
                          for i,xx in enumerate(xv) for j,yy in enumerate(yv) if (i+j)%2==e])
            direct_slice = s.factor(V.det(method="domain-ge"))
            expected_slice = s.factor(candidate.subs(subs))
            ratio = s.cancel(direct_slice/expected_slice)
            assert ratio in (1,-1), (m,e,ratio)
            candidate *= ratio
            # m=2 additionally compute the fully multivariate direct determinant.
            direct_full = None
            if m == 2:
                direct_full = s.factor(s.Matrix([[X[i]**a*Y[j]**b for a,b in monomials(m)] for i,j in ijs]).det(method="domain-ge"))
                assert s.expand(direct_full-candidate) == 0
            result.append({"m":m,"parity":e,"axis_minors":axis,"determinant":str(candidate),
                           "square_factors":[[str(f),p] for f,p in factors],
                           "direct_full_symbolic_computed": direct_full is not None,
                           "slice_X":xv,"slice_Y":list(map(str,yv)),"direct_slice":str(direct_slice),
                           "slice_identity":"PASS"})
    return {"sympy_version":s.__version__,"records":result,"all_assertions":"PASS"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20261031)
    ap.add_argument("--symbolic", action="store_true")
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    report = symbolic_run() if args.symbolic else finite_run(args.samples,args.seed)
    report["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report["python"] = sys.version
    out = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(out+"\n")
    print(out)


if __name__ == "__main__":
    main()
