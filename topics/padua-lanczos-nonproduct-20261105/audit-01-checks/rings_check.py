#!/usr/bin/env python3
"""Independent exact checks of the D36x9 / D65x9 admission facts.

Auditor-authored (not derived from developer code). Exact Fraction / integer
arithmetic; matrix ranks modulo large primes (rank mod p <= rank over Q, and
explicit kernel polynomial gives the matching upper bound at degree 18).
"""
from fractions import Fraction as F
from math import lcm, gcd
import hashlib, json, sys, time
import flint


def d36_dirs():
    D = {(F(1), F(0)), (F(-1), F(0)), (F(0), F(1)), (F(0), F(-1))}
    for a, b, c in [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]:
        for u, v in [(F(a, c), F(b, c)), (F(b, c), F(a, c))]:
            for sx in (-1, 1):
                for sy in (-1, 1):
                    D.add((sx * u, sy * v))
    return D


def d65_dirs():
    # all integer points on the circle of radius 65, then filter to the named set
    pts = set()
    for a in range(-65, 66):
        for b in range(-65, 66):
            if a * a + b * b == 65 * 65:
                pts.add((a, b))
    named = {(65, 0), (-65, 0), (0, 65), (0, -65)}
    for a, b in [(16, 63), (25, 60), (33, 56), (39, 52)]:
        for u, v in [(a, b), (b, a)]:
            for sx in (-1, 1):
                for sy in (-1, 1):
                    named.add((sx * u, sy * v))
    assert named <= pts
    return {(F(a, 65), F(b, 65)) for a, b in named}, len(pts)


def grid(D):
    return {(F(k, 9) * u, F(k, 9) * v) for k in range(1, 10) for u, v in D}


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull_vertices(points):
    P = sorted(points)
    lower, upper = [], []
    for p in P:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(P):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]  # strict vertices (collinear removed)


def rank_mod_p(G, s, p):
    q = lcm(*(v.denominator for z in G for v in z))
    pts = [(int(x * q), int(y * q)) for x, y in G]
    mons = [(d - j, j) for d in range(s + 1) for j in range(d + 1)]
    M = flint.nmod_mat(len(pts), len(mons),
                       [pow(X, a, p) * pow(Y, b, p) % p for X, Y in pts for a, b in mons], p)
    return M.rank(), len(mons)


def symmetries(G):
    """All linear maps L with L(G)=G (affine bijections fix the centroid 0)."""
    Gs = set(G)
    pts = sorted(G)
    centroid = (sum(x for x, _ in pts) / len(pts), sum(y for _, y in pts) / len(pts))
    assert centroid == (0, 0)
    e1, e2 = (F(1), F(0)), (F(0), F(1))
    assert e1 in Gs and e2 in Gs
    found = []
    test = pts[:: max(1, len(pts) // 40)]
    for u in pts:
        for v in pts:
            det = u[0] * v[1] - u[1] * v[0]
            if det == 0:
                continue
            # L e1 = u, L e2 = v  -> L(x,y) = x u + y v
            ok = True
            for x, y in test:
                if (x * u[0] + y * v[0], x * u[1] + y * v[1]) not in Gs:
                    ok = False
                    break
            if not ok:
                continue
            if all((x * u[0] + y * v[0], x * u[1] + y * v[1]) in Gs for x, y in pts):
                found.append(((u[0], v[0]), (u[1], v[1])))
    return found


def frac(x):
    return str(x.numerator) if x.denominator == 1 else str(x)


def main():
    out = {}
    t0 = time.time()
    D36 = d36_dirs()
    D65, n_int65 = d65_dirs()
    for name, D in [("D36x9", D36), ("D65x9", D65)]:
        G = grid(D)
        r = {}
        r["directions"] = len(D)
        r["unit_directions"] = all(u * u + v * v == 1 for u, v in D)
        r["nodes"] = len(G)
        r["radii_sq"] = sorted(str(x * x + y * y) for x, y in {(F(k, 9), F(0)) for k in range(1, 10)})
        r["distinct_radii_on_grid"] = len({x * x + y * y for x, y in G})
        q = lcm(*(v.denominator for z in G for v in z))
        r["least_common_denominator"] = q
        r["max_individual_denominator"] = max(v.denominator for z in G for v in z)
        H = hull_vertices(G)
        r["hull_vertices"] = len(H)
        r["hull_vertices_all_on_unit_circle"] = all(x * x + y * y == 1 for x, y in H)
        syms = symmetries(G)
        r["linear_symmetry_count"] = len(syms)
        r["symmetries_are_signed_permutations"] = all(
            sorted(abs(e) for row in L for e in row) == [0, 0, 1, 1] for L in syms)
        ranks = {}
        for s in (16, 17, 18):
            rk = [rank_mod_p(G, s, p) for p in (2**61 - 1, 1000000007)]
            ranks[s] = {"rank_mod_p": [a for a, _ in rk], "columns": rk[0][1]}
        r["evaluation_rank"] = ranks
        # explicit degree-18 annihilator: product of nine circle factors
        r["deg18_annihilator_vanishes"] = all(
            eval_prod(x, y) == 0 for x, y in G)
        r["N16_lt_M"] = (17 * 18 // 2) < len(G)
        if name == "D36x9":
            txt = '\n'.join(f'{frac(x)} {frac(y)}' for x, y in sorted(G)) + '\n'
            r["grid_sha256_p2probe_format"] = hashlib.sha256(txt.encode()).hexdigest()
        else:
            txt = ''.join(f'{x} {y}\n' for x, y in sorted(G))
            r["node_sha256_p2_04_format"] = hashlib.sha256(txt.encode()).hexdigest()
            r["integer_points_on_circle_65"] = n_int65
        out[name] = r
    G36, G65 = grid(D36), grid(D65)
    out["supports_differ"] = G36 != G65
    out["shared_directions"] = len(D36 & D65)
    out["lcd_ratio"] = out["D36x9"]["least_common_denominator"] / out["D65x9"]["least_common_denominator"]
    out["elapsed_s"] = round(time.time() - t0, 2)
    out["python"] = sys.version.split()[0]
    out["flint"] = flint.__version__
    print(json.dumps(out, indent=1))


def eval_prod(x, y):
    v = F(1)
    for k in range(1, 10):
        v *= x * x + y * y - F(k * k, 81)
    return v


if __name__ == "__main__":
    main()
