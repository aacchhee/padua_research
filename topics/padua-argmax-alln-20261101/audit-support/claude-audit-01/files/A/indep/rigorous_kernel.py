"""Auditor's independently implemented rigorous kernel (Claude Opus 5.5, audit01/A).

Purpose: replay every leaf predicate of the committed certificates with arithmetic that
shares no code with the developer's finite_bernstein.py / finite_general.py.

Route (different from the developer's PD-T101 kernel + Machin/Taylor + de Casteljau):
 1. V[i,m] = T_a(x_i) T_b(y_i) = cos(a j_i pi/n) cos(b k_i pi/(n+1)) enclosed with
    mpmath.iv (outward-rounded interval cos/pi; trusted dependency), then by integers.
 2. C~ = numerically inverted V (mpmath LU), *defined* as exact dyadic integers / 2^K.
 3. Rigorous residual R = V C~ - I, |R| <= |Vmid C~ - I| + Vrad |C~| exactly in integers;
    ||R||_inf < 1 proves V invertible (unisolvence at this n), and
    |C - C~|_max <= ||C~||_inf ||R||_inf / (1 - ||R||_inf) =: delta.
 4. Power coefficients via exact integer Chebyshev coefficients; Bernstein coefficients on
    each leaf box by the exact rational affine/Bernstein matrix of that box (no de Casteljau),
    with entrywise error <= delta*(|Mx| G |My|^T).
 5. Corner value lower bound C_- = min over the two designated corners of
    sum_l max(0, |L~_l(e)| - delta*#modes); designated corners recomputed from the node set.
 6. Bound leaf: every coefficient sum upper bound < C_-.  Corner leaf: same except the tensor
    vertex index of the box's square corner (whose exact coefficient is L_l(e)).
 7. Leaf geometry from the path strings only; complete partition by prefix-freeness and
    Kraft sum exactly 1.
Equality of the two non-node corner values is the node-reflection argument (not numerical).
"""
import argparse
import gzip
import json
import time
from fractions import Fraction as F
from math import comb, gcd

import mpmath
import numpy as np
from mpmath import iv, mp

REPO_OUT = "/home/user/padua_research/topics/padua-argmax-alln-20261101/outputs/part3/"
K = 320  # integer scale exponent


def raw_to_fraction(raw):
    """Exact value of a raw mpmath mpf tuple (no rounding)."""
    from mpmath.libmp import to_rational
    p, q = to_rational(raw)  # exact, signed
    return F(p, q)


def iv_endpoints(v):
    lo_raw, hi_raw = v._mpi_
    return raw_to_fraction(lo_raw), raw_to_fraction(hi_raw)


def floor_scaled(q, k):
    q = q * (1 << k)
    return q.numerator // q.denominator


def ceil_scaled(q, k):
    q = q * (1 << k)
    return -((-q.numerator) // q.denominator)


def nodes_of(n):
    return [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]


def modes_of(n):
    return [(a, b) for a in range(n + 1) for b in range(n + 1 - a)]


def cos_iv(num, den):
    """Interval enclosure of cos(num*pi/den) via mpmath.iv."""
    return iv.cos(iv.pi * num / den)


def enclose_V(n, nodes, md):
    N = len(nodes)
    lo = np.empty((N, N), dtype=object)
    hi = np.empty((N, N), dtype=object)
    mid_mp = mp.matrix(N, N)
    cx = {}
    cy = {}
    for i, (j, k) in enumerate(nodes):
        for m, (a, b) in enumerate(md):
            if (a, j) not in cx:
                cx[a, j] = cos_iv(a * j, n)
            if (b, k) not in cy:
                cy[b, k] = cos_iv(b * k, n + 1)
            v = cx[a, j] * cy[b, k]
            vlo, vhi = iv_endpoints(v)
            assert vlo <= vhi
            lo[i, m] = floor_scaled(vlo, K)
            hi[i, m] = ceil_scaled(vhi, K)
            # midpoint only seeds the numerical inverse; rigor comes from the residual bound
            mid_mp[i, m] = mp.mpf(vlo.numerator) / vlo.denominator / 2 + mp.mpf(vhi.numerator) / vhi.denominator / 2
    return lo, hi, mid_mp


def rigorous_inverse(n, nodes, md):
    lo, hi, mid_mp = enclose_V(n, nodes, md)
    N = len(nodes)
    Cmp = mp.inverse(mid_mp)
    Cint = np.empty((N, N), dtype=object)
    for r in range(N):
        for c in range(N):
            Cint[r, c] = int(mp.nint(Cmp[r, c] * mp.mpf(2) ** K))
    # V C~ in [ (lo+hi)/2 C~ +- (hi-lo)/2 |C~| ]; all at scale 2^(2K+1)
    absC = np.vectorize(abs, otypes=[object])(Cint)
    A = (lo + hi).dot(Cint)
    Rad = (hi - lo).dot(absC)
    I_s = 1 << (2 * K + 1)
    rowmax = 0
    for r in range(N):
        s = 0
        for c in range(N):
            s += abs(A[r, c] - (I_s if r == c else 0)) + Rad[r, c]
        rowmax = max(rowmax, s)
    normR = F(rowmax, I_s)
    normC = F(max(sum(abs(int(Cint[r, c])) for c in range(N)) for r in range(N)), 1 << K)
    assert normR < 1, "residual too large: unisolvence not certified"
    delta = normC * normR / (1 - normR)
    return Cint, delta, normR, normC


def cheb_int(deg):
    t = [[1] + [0] * deg, [0, 1] + [0] * (deg - 1)]
    for a in range(2, deg + 1):
        v = [0] * (deg + 1)
        for i in range(deg):
            v[i + 1] += 2 * t[-1][i]
        for i in range(deg + 1):
            v[i] -= t[-2][i]
        t.append(v)
    return t[:deg + 1]


def power_ints(n, md, Cint):
    """P~_l as integer matrices at scale 2^K (exact from C~) and G[i][j]=sum_m |t_a[i] t_b[j]|."""
    t = cheb_int(n)
    N = Cint.shape[1]
    T = np.zeros((len(md), (n + 1) * (n + 1)), dtype=object)
    T[:, :] = 0
    G = np.zeros((n + 1, n + 1), dtype=object)
    G[:, :] = 0
    for m, (a, b) in enumerate(md):
        for i in range(a + 1):
            for j in range(b + 1):
                v = t[a][i] * t[b][j]
                T[m, i * (n + 1) + j] = v
                G[i, j] += abs(v)
    # P[l, ij] = sum_m C[m,l] T[m, ij]
    P = Cint.T.dot(T)  # N x (n+1)^2
    return [P[l].reshape(n + 1, n + 1) for l in range(N)], G


def box_of_path(path):
    box = [[F(-1), F(1)], [F(-1), F(1)]]
    for d, ch in enumerate(path):
        ax = d % 2
        lo, hi = box[ax]
        mid = (lo + hi) / 2
        box[ax] = [lo, mid] if ch == "0" else [mid, hi]
    return box


def box_matrix(n, lo, hi):
    """Exact M[i][a]: Bernstein coefficient i on [lo,hi] of x^a (x = lo + (hi-lo) u)."""
    h = hi - lo
    M = [[F(0)] * (n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        for r in range(a + 1):
            c = comb(a, r) * lo ** (a - r) * h ** r
            if c:
                for i in range(r, n + 1):
                    M[i][a] += c * F(comb(i, r), comb(n, r))
    den = 1
    for row in M:
        for q in row:
            den = den * q.denominator // gcd(den, q.denominator)
    return np.array([[int(q * den) for q in row] for row in M], dtype=object), den


def leaf_upper_bounds(n, Pl_list, G, delta, box):
    """Rigorous upper bounds U[i,k] >= sum_l |b_{l,ik}| as Fractions."""
    Mx, dx = box_matrix(n, *box[0])
    My, dy = box_matrix(n, *box[1])
    absf = np.vectorize(abs, otypes=[object])
    MyT = My.T
    S = np.zeros((n + 1, n + 1), dtype=object)
    S[:, :] = 0
    stack = np.concatenate(Pl_list, axis=1)
    left = Mx.dot(stack)
    for l in range(len(Pl_list)):
        S = S + absf(left[:, l * (n + 1):(l + 1) * (n + 1)].dot(MyT))
    Eabs = absf(Mx).dot(G).dot(absf(My).T)  # scale dx*dy (integers)
    scale = dx * dy * (1 << K)
    N = len(Pl_list)
    U = [[F(int(S[i, k]), scale) + delta * N * F(int(Eabs[i, k]), dx * dy) for k in range(n + 1)]
         for i in range(n + 1)]
    return U


def corner_lower(n, md, Cint, delta, e):
    N = Cint.shape[1]
    q = [(e[0] ** a) * (e[1] ** b) for a, b in md]
    tot = F(0)
    up = F(0)
    for l in range(N):
        v = F(sum(int(Cint[m, l]) * q[m] for m in range(len(md))), 1 << K)
        err = delta * len(md)
        tot += max(F(0), abs(v) - err)
        up += abs(v) + err
    return tot, up


def run(n, certs):
    t0 = time.time()
    nodes = nodes_of(n)
    md = modes_of(n)
    # designated corners recomputed from the node set: corners that are not nodes
    nodeset = set(nodes)
    corner_index = {(1, 1): (0, 0), (1, -1): (0, n + 1), (-1, 1): (n, 0), (-1, -1): (n, n + 1)}
    nonnode = sorted(c for c, jk in corner_index.items() if jk not in nodeset)
    Cint, delta, normR, normC = rigorous_inverse(n, nodes, md)
    Pl, G = power_ints(n, md, Cint)
    cl = {c: corner_lower(n, md, Cint, delta, c) for c in nonnode}
    Cminus = min(v[0] for v in cl.values())
    out = {"n": n, "nonnode_corners": [list(c) for c in nonnode], "unisolvence_residual_inf_norm_upper": float(normR),
           "inverse_inf_norm": float(normC), "delta_entrywise": float(delta),
           "corner_value_enclosures": {str(c): [float(v[0]), float(v[1]), float(v[1] - v[0])] for c, v in cl.items()},
           "C_minus": float(Cminus), "certificates": {}}
    for cert in certs:
        d = json.loads(gzip.decompress(open(REPO_OUT + cert, "rb").read()))
        assert d["n"] == n
        paths = [row["path"] for row in d["leaves"]]
        assert all(isinstance(p, str) and set(p) <= {"0", "1"} for p in paths)
        assert len(set(paths)) == len(paths)
        prefix_free = all(not (p != q and q.startswith(p)) for p in paths for q in paths)
        kraft = sum(F(1, 2 ** len(p)) for p in paths)
        complete = prefix_free and kraft == 1 and not d["pending"]
        worst = None
        failures = []
        corner_cover = set()
        for row in d["leaves"]:
            box = box_of_path(row["path"])
            U = leaf_upper_bounds(n, Pl, G, delta, box)
            # which square corners of the designated set are vertices of this box?
            verts = [c for c in nonnode if (box[0][0] == c[0] or box[0][1] == c[0]) and
                     (box[1][0] == c[1] or box[1][1] == c[1])]
            allmax = max(max(r) for r in U)
            if allmax < Cminus:
                kind = "bound"
                m = allmax
            else:
                kind = None
                m = None
                for c in verts:
                    vi = 0 if box[0][0] == c[0] else n
                    vk = 0 if box[1][0] == c[1] else n
                    other = max(U[i][k] for i in range(n + 1) for k in range(n + 1) if (i, k) != (vi, vk))
                    if other < Cminus:
                        kind = "corner"
                        m = other
                        corner_cover.add(c)
                        break
            if kind is None:
                failures.append(row["path"])
                continue
            if kind != row["kind"]:
                # a leaf certified as bound by us but recorded as corner is still sound; record it
                failures.append(row["path"] + ":kind-" + kind)
            rel = 1 - m / Cminus
            worst = rel if worst is None else min(worst, rel)
        out["certificates"][cert] = {
            "leaves": len(paths), "prefix_free": prefix_free, "kraft_sum": str(kraft),
            "complete_partition": complete, "failures": failures,
            "corner_leaves_cover": sorted(list(c) for c in corner_cover),
            "all_leaf_predicates_rigorously_verified": not failures,
            "worst_relative_margin": float(worst) if worst is not None else None,
            "conclusion_holds": complete and not failures and corner_cover == set(nonnode),
        }
    out["seconds"] = time.time() - t0
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, nargs="+", required=True)
    ap.add_argument("--dps", type=int, default=130)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    mp.dps = args.dps
    iv.dps = args.dps
    for n in args.n:
        certs = {8: ["finite_n8_general.json.gz", "finite_n8_pilot.json.gz"],
                 12: ["finite_n12_pilot.json.gz"]}.get(n, [f"finite_n{n}_general.json.gz"])
        r = run(n, certs)
        r.update(mpmath_version=mpmath.__version__, dps=args.dps, K=K)
        print(json.dumps(r), flush=True)
        with open(f"{args.out}/rigorous_n{n}.json", "w") as fh:
            json.dump(r, fh, indent=1)


if __name__ == "__main__":
    main()
