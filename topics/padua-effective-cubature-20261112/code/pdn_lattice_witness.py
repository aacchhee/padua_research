"""Lattice witnesses for the finite torus-LP limitation (record -06, PD-N).

For each degree n and exactness E in {2n-2, 2n-1}, search for an integer
lattice L = A Z^3 (A integer, columns = basis) whose nonzero vectors all have
l1-norm >= E+1, with index |det A| <= 8*binom(n+3,3).  By record -04 (b) such
an L caps every torus (plain or Delsarte, any K) LP value at |det A|, so the
torus LP combined with M <= 8N cannot exclude a Padua package at n.

Candidates: A = round(t*B) for the Minkowski/Betke-Henk octahedron lattice B
(record -04), t on a grid, plus the integral scalings s*B (3 | s) and any
explicit bases supplied with --extra (JSON list of {"n":..,"basis":rows}),
and with --perturb all +-1 entry perturbations of round(t*B), t in [n-1/2, n+1],
when the base candidates do not reach 8P.
Every reported witness is re-verified by exact integer enumeration:
for k = A c with |k|_1 <= E, |c_i| <= max_j |(A^-1)_ij| * E, so enumerating
that coefficient box is exhaustive.

Usage: python3 -B pdn_lattice_witness.py --nmax 140 --out witness.json
"""
import argparse, hashlib, itertools, json, sys
from fractions import Fraction
from math import comb, floor

B = [[Fraction(2, 3), Fraction(-1, 3), Fraction(-1)],
     [Fraction(1), Fraction(-2, 3), Fraction(1, 3)],
     [Fraction(1, 3), Fraction(1), Fraction(-2, 3)]]  # columns (2/3,1,1/3),(-1/3,-2/3,1),(-1,1/3,-2/3)


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def inv3(A):
    d = Fraction(det3(A))
    C = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m = [[A[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            C[j][i] = Fraction((-1) ** (i + j) * (m[0][0] * m[1][1] - m[0][1] * m[1][0])) / d
    return C


def min_l1_at_most(A, E):
    """Return True iff some nonzero vector of A Z^3 has l1-norm <= E (exhaustive)."""
    Ai = inv3(A)
    bounds = [floor(max(abs(x) for x in row) * E) for row in Ai]
    for c in itertools.product(*[range(-b, b + 1) for b in bounds]):
        if c == (0, 0, 0):
            continue
        k = [A[r][0] * c[0] + A[r][1] * c[1] + A[r][2] * c[2] for r in range(3)]
        if abs(k[0]) + abs(k[1]) + abs(k[2]) <= E:
            return True
    return False


def candidates(n):
    out = []
    t = n - 1.0
    while t <= n + 3.0:
        A = [[round(float(B[r][c]) * t) for c in range(3)] for r in range(3)]
        out.append(A)
        t += 0.005
    s = 3
    while s <= n + 6:
        out.append([[int(B[r][c] * s) for c in range(3)] for r in range(3)])
        s += 3
    return out


def perturbed(n, P8):
    """Integer perturbations Delta in {-1,0,1}^9 of round(t*B), t near n, with |det| <= P8."""
    out = []
    bases = set()
    t = n - 0.5
    while t <= n + 1.0:
        bases.add(tuple(tuple(round(float(B[r][c]) * t) for c in range(3)) for r in range(3)))
        t += 0.05
    for A0 in bases:
        for D in itertools.product((-1, 0, 1), repeat=9):
            A = [[A0[r][c] + D[3 * r + c] for c in range(3)] for r in range(3)]
            d = abs(det3(A))
            if 0 < d <= P8:
                out.append(A)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmin", type=int, default=2)
    ap.add_argument("--nmax", type=int, default=140)
    ap.add_argument("--extra", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--perturb", action="store_true",
                    help="if the base candidates miss 8P, also try +-1 perturbations")
    a = ap.parse_args()
    extra = {}
    if a.extra:
        for row in json.load(open(a.extra))["rows"]:
            extra.setdefault(row["n"], []).append(row["basis"])
    rows = []
    for n in range(a.nmin, a.nmax + 1):
        P8 = 8 * comb(n + 3, 3)
        rec = {"n": n, "8P": P8}
        for E in (2 * n - 2, 2 * n - 1):
            cands = candidates(n)
            for m, bl in extra.items():  # supplied bases (rows = basis vectors) for any n
                for b in bl:
                    cands.append([[b[c][r] for c in range(3)] for r in range(3)])
            seen = {}
            for A in cands:
                d = abs(det3(A))
                if d == 0:
                    continue
                key = tuple(map(tuple, A))
                if key not in seen:
                    seen[key] = d
            best = None
            for key, d in sorted(seen.items(), key=lambda kv: kv[1]):
                if best is not None and d >= best[0]:
                    break
                A = [list(r) for r in key]
                if not min_l1_at_most(A, E):
                    best = (d, A)
                    break
            if a.perturb and (best is None or best[0] > P8):
                pc = {}
                for A in perturbed(n, P8):
                    pc[tuple(map(tuple, A))] = abs(det3(A))
                for key, d in sorted(pc.items(), key=lambda kv: kv[1]):
                    if best is not None and d >= best[0]:
                        break
                    A = [list(r) for r in key]
                    if not min_l1_at_most(A, E):
                        best = (d, A)
                        break
            tag = "E=2n-2" if E == 2 * n - 2 else "E=2n-1"
            rec[tag] = {"index": best[0], "basis_columns": best[1],
                        "covered": best[0] <= P8} if best else None
        rows.append(rec)
        print(n, rec["8P"], rec["E=2n-2"]["index"], rec["E=2n-2"]["covered"],
              rec["E=2n-1"]["index"], rec["E=2n-1"]["covered"], flush=True)
    code_sha = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    cov = {tag: [r["n"] for r in rows if r[tag] and r[tag]["covered"]] for tag in ("E=2n-2", "E=2n-1")}
    json.dump({"script_sha256": code_sha, "python": sys.version.split()[0], "argv": sys.argv[1:],
               "covered": cov, "rows": rows}, open(a.out, "w"), indent=0)


if __name__ == "__main__":
    main()
