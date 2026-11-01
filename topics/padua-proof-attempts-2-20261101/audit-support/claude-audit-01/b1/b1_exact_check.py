"""Claude audit-01, B1 sub-audit: independent EXACT sanity checks of records 90-92.

Supporting evidence only; no audit verdict depends on it.  Written by the auditor
without importing or reading any developer code (there is none for B1).

Part A (exact rationals, python-flint fmpq_mat), for each configuration:
  * V_j = Pi_j / pi_j evaluated at fixed rational nodes, pi_j = prod_{r<=j}(x+y-a_r),
    weighted projectors P_j = A (A^T W A)^-1 A^T W, Q_j = P_j - P_{j-1}.
  * R_t = colspace of (I-Q_t-Q_{t-1}) D_{t+1}^-1 [Q_{t-1}, Q_t, D_x Q_t, D_y Q_t].
  * checks, for 2<=t<=T:
      rank R_t (record 90 bound <= 2t+1; generic = 2t+1);
      record 90 (1): <r, p/pi_k> = <r, tau_{a,k}(p)/pi_k> for all r in R_t, p in Pi_k;
      record 90 (2): detector W_k -> H_k, q -> tau(pi_k q) has rank k+1;
      record 90 (4): ordinary Top_j: W_j -> H_j has rank j+1;
      record 90 (3): {r in R_t : r perp W_{t-2}} is contained in W_{t+1};
      record 92: equality (kernel dimension t+2);
      nontriviality: constraint rank t-1, leakage into V_{t-3} nonzero (t>=3);
      controls: constraining with the WRONG block W_{t-3}, and the unconstrained
      three-block projection, are expected NOT to give W_{t+1}.
Part B (mod p, flint nmod_mat): rank lower bounds at source scale M=120, T=9, on the
  source's own random nodes (numpy default_rng(1) uniform, exact dyadic rationals),
  for random rational offsets and for RATIONALIZED near-source taper offsets.  A mod-p
  rank 2t+1 certifies rank_Q >= 2t+1 at that rational point (i.e. p_t != 0 there).  It
  does NOT certify the source's irrational stored parameter.
"""
import json, sys, time, random, math, hashlib
from fractions import Fraction as Fr
import flint

fq = flint.fmpq


def monos(j):
    return [(d - i, i) for d in range(j + 1) for i in range(d + 1)]


def N(j):
    return (j + 1) * (j + 2) // 2 if j >= 0 else 0


def mat(rows):
    r = len(rows)
    c = len(rows[0]) if r else 0
    return flint.fmpq_mat(r, c, [fq(v.numerator, v.denominator) if isinstance(v, Fr) else v for row in rows for v in row])


def hstack(ms):
    rows = [sum((m.tolist()[i] for m in ms), []) for i in range(ms[0].nrows())]
    return flint.fmpq_mat(len(rows), len(rows[0]), [v for row in rows for v in row])


def colspace(A):
    """basis (as columns) of the column space of A"""
    R, rk = A.transpose().rref()
    L = R.tolist()[:rk]
    if rk == 0:
        return None, 0
    return flint.fmpq_mat(rk, A.nrows(), [v for row in L for v in row]).transpose(), rk


def nullspace(A):
    """basis (columns) of the right null space of fmpq_mat A"""
    R, rk = A.rref()
    n = A.ncols()
    L = R.tolist()
    piv = []
    for i in range(rk):
        for j in range(n):
            if L[i][j] != 0:
                piv.append(j)
                break
    free = [j for j in range(n) if j not in piv]
    vecs = []
    for f in free:
        v = [fq(0)] * n
        v[f] = fq(1)
        for i, p in enumerate(piv):
            v[p] = -L[i][f]
        vecs.append(v)
    if not vecs:
        return None, 0
    return flint.fmpq_mat(len(vecs), n, [x for v in vecs for x in v]).transpose(), len(vecs)


def is_zero(A):
    return all(v == 0 for v in A.entries())


class Flag:
    def __init__(self, nodes, w, a, T):
        self.nodes, self.w, self.a, self.T = nodes, w, a, T
        M = len(nodes)
        self.M = M
        self.Wd = mat([[w[i] if i == j else 0 for j in range(M)] for i in range(M)])
        self.I = mat([[1 if i == j else 0 for j in range(M)] for i in range(M)])
        self.s = [x + y for (x, y) in nodes]
        self.A, self.P, self.Q = {}, {}, {}
        Z = mat([[0] * M for _ in range(M)])
        self.P[-1] = Z
        for j in range(T + 2):
            self.A[j] = self.evalA(j)
            G = self.A[j].transpose() * self.Wd * self.A[j]
            self.P[j] = self.A[j] * G.inv() * self.A[j].transpose() * self.Wd
            self.Q[j] = self.P[j] - self.P[j - 1]

    def pi(self, i, j):
        p = Fr(1)
        for r in range(j):
            p *= self.s[i] - self.a[r]
        return p

    def evalA(self, j):
        rows = []
        for i, (x, y) in enumerate(self.nodes):
            pij = self.pi(i, j)
            rows.append([x ** u * y ** v / pij for (u, v) in monos(j)])
        return mat(rows)

    def diag(self, vals):
        M = self.M
        return mat([[vals[i] if i == j else 0 for j in range(M)] for i in range(M)])

    def Rgen(self, t, nproj=2):
        Dinv = self.diag([1 / (self.s[i] - self.a[t]) for i in range(self.M)])
        Dx = self.diag([x for (x, y) in self.nodes])
        Dy = self.diag([y for (x, y) in self.nodes])
        C = Dinv * hstack([self.Q[t - 1], self.Q[t], Dx * self.Q[t], Dy * self.Q[t]])
        Pr = self.I - self.Q[t] - self.Q[t - 1]
        if nproj == 3:
            Pr = Pr - self.Q[t - 2]
        return Pr * C

    def block_basis(self, j):
        B, rk = colspace(self.Q[j])
        return B, rk

    def numer_coeffs(self, j, B):
        """numerator coefficients (over monos(j)) of vectors B (columns) lying in V_j"""
        A = self.A[j]
        G = A.transpose() * self.Wd * A
        C = G.inv() * A.transpose() * self.Wd * B
        assert A * C == B, "vector not in V_j"
        return C

    def tau_matrix(self, k, a):
        """(k+1) x N_k matrix of tau_{a,k} in the H_k basis x^(k-i) y^i"""
        rows = [[fq(0)] * N(k) for _ in range(k + 1)]
        for col, (u, v) in enumerate(monos(k)):
            d = u + v
            e = k - d
            for i in range(e + 1):  # (x+y)^e = sum C(e,i) x^(e-i) y^i
                xp = u + e - i
                yp = v + i
                rows[yp][col] += fq(math.comb(e, i)) / fq(a.numerator, a.denominator) ** e
        return flint.fmpq_mat(k + 1, N(k), [v for r in rows for v in r])

    def top_matrix(self, j):
        rows = [[fq(0)] * N(j) for _ in range(j + 1)]
        for col, (u, v) in enumerate(monos(j)):
            if u + v == j:
                rows[v][col] = fq(1)
        return flint.fmpq_mat(j + 1, N(j), [v for r in rows for v in r])

    def vec_poly_over_pi(self, coeffs_by_mono, k):
        """sampled vector of p/pi_k, p given as dict (u,v)->Fraction"""
        out = []
        for i, (x, y) in enumerate(self.nodes):
            val = sum(c * x ** u * y ** v for (u, v), c in coeffs_by_mono.items())
            out.append([val / self.pi(i, k)])
        return mat(out)


def tau_poly(u, v, k, a):
    """tau_{a,k}(x^u y^v) as dict"""
    e = k - u - v
    return {(u + e - i, v + i): Fr(math.comb(e, i)) / a ** e for i in range(e + 1)}


def check_config(name, nodes, w, a, T, expect_generic=True, out_of_class=False):
    t0 = time.time()
    F = Flag(nodes, w, a, T)
    res = {"name": name, "M": len(nodes), "T": T, "offsets": [str(v) for v in a],
           "nodes_in_square": all(-1 <= x <= 1 and -1 <= y <= 1 for x, y in nodes),
           "all_ell_negative": all(s - aj < 0 for s in F.s for aj in a), "t": {}}
    # flag dimensions
    res["dims_V_full"] = all(F.A[j].rank() == N(j) for j in range(T + 2))
    for j in range(T + 2):
        Bj, rk = F.block_basis(j)
        assert rk == j + 1, (name, j, rk)
        if j >= 1:
            C = F.numer_coeffs(j, Bj)
            res.setdefault("Top_rank_ok", True)
            res["Top_rank_ok"] &= (F.top_matrix(j) * C).rank() == j + 1
    for t in range(2, T + 1):
        k = t - 2
        a_new = a[t]  # a_{t+1} (0-based list)
        Rg = F.Rgen(t)
        B, r = colspace(Rg)
        d = {"rank_R": r, "rank_bound_ok": r <= 2 * t + 1, "rank_generic": r == 2 * t + 1}
        # record 90 (1): <r,p/pi_k> = <r,tau(p)/pi_k>
        ok1 = True
        for (u, v) in monos(k):
            vp = F.vec_poly_over_pi({(u, v): Fr(1)}, k)
            vt = F.vec_poly_over_pi(tau_poly(u, v, k, a_new), k)
            if not is_zero(B.transpose() * F.Wd * (vp - vt)):
                ok1 = False
        d["topform_factorization_ok"] = ok1
        # record 90 (2): detector rank
        Bk, _ = F.block_basis(k)
        Ck = F.numer_coeffs(k, Bk)
        d["detector_rank"] = (F.tau_matrix(k, a_new) * Ck).rank()
        d["detector_iso"] = d["detector_rank"] == k + 1
        # constraint
        Ncon = Bk.transpose() * F.Wd * B
        d["constraint_rank"] = Ncon.rank()
        K, nk = nullspace(Ncon)
        if nk:
            KV = B * K
            d["kernel_in_W_t+1"] = (F.Q[t + 1] * KV == KV)
        else:
            d["kernel_in_W_t+1"] = True
        d["kernel_dim"] = nk
        d["equality_B1"] = d["kernel_in_W_t+1"] and nk == t + 2
        # nontrivial leakage into V_{t-3}
        if t >= 3:
            d["leak_into_V_t-3_nonzero"] = not is_zero(F.P[t - 3] * B)
            # control 1: wrong constraint block W_{t-3}
            Bw, _ = F.block_basis(t - 3)
            Kw, nkw = nullspace(Bw.transpose() * F.Wd * B)
            in_w = (F.Q[t + 1] * (B * Kw) == B * Kw) if nkw else True
            d["control_wrong_block_gives_W_t+1"] = bool(in_w and nkw == t + 2)
            # control 2: unconstrained three-block projection
            r3 = F.Rgen(t, nproj=3).rank()
            d["control_three_block_rank"] = r3
        if expect_generic and not out_of_class:
            # in coalescent case also check R_t = W_{t+1} (+) W_{t-2}
            pass
        if len(set(a)) == 1:
            d["coalescent_R_in_Wt+1_plus_Wt-2"] = ((F.Q[t + 1] + F.Q[t - 2]) * B == B)
        res["t"][t] = d
    res["seconds"] = round(time.time() - t0, 2)
    return res


def rnd_rat(rng, lo, hi, den):
    return Fr(rng.randint(int(lo * den), int(hi * den)), den)


def random_nodes(rng, M, den=97):
    pts = set()
    while len(pts) < M:
        pts.add((rnd_rat(rng, -1, 1, den), rnd_rat(rng, -1, 1, den)))
    return sorted(pts)


def distinct_offsets(rng, n, lo, hi, den=89):
    vals = set()
    while len(vals) < n:
        v = rnd_rat(rng, lo, hi, den)
        if v > 2:
            vals.add(v)
    vals = list(vals)
    rng.shuffle(vals)
    return vals


def partA():
    rng = random.Random(20261101)
    out = []
    for T in (3, 4, 5):
        M0 = N(T + 1)
        for extra in (0, 3):
            nodes = random_nodes(rng, M0 + extra)
            w = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in nodes]
            a = distinct_offsets(rng, T + 1, 2, 5)
            out.append(check_config(f"random T{T} M=N+{extra}", nodes, w, a, T))
    # tensor grid including the corner (1,1), non-uniform weights, T=4
    T = 4
    g = [Fr(-1), Fr(-3, 4), Fr(-1, 3), Fr(0), Fr(2, 5), Fr(5, 6), Fr(1)]
    nodes = [(x, y) for x in g for y in g]
    w = [Fr(1 + (i % 4), 1 + (i % 3)) for i in range(len(nodes))]
    out.append(check_config("tensor7x7 with corner, T4, offsets near 2", nodes, w,
                            [Fr(2) + Fr(1, 10 ** (j + 1)) for j in range(T + 1)][::-1], T))
    out.append(check_config("tensor7x7 with corner, T4, offsets spread", nodes, w,
                            [Fr(2) + Fr(1, 1000), Fr(100), Fr(3), Fr(21, 10), Fr(7)], T))
    # coalescent and partially coincident offsets (record 90 all outward offsets; record 91 witness)
    rng2 = random.Random(7)
    for T in (3, 4):
        nodes = random_nodes(rng2, N(T + 1) + 2)
        w = [Fr(rng2.randint(1, 9), rng2.randint(1, 5)) for _ in nodes]
        out.append(check_config(f"coalescent c=5/2 T{T}", nodes, w, [Fr(5, 2)] * (T + 1), T))
        out.append(check_config(f"coalescent c=7 T{T}", nodes, w, [Fr(7)] * (T + 1), T))
        pc = [Fr(3), Fr(3), Fr(9, 4), Fr(9, 4), Fr(3), Fr(9, 4)][:T + 1]
        out.append(check_config(f"partially coincident T{T}", nodes, w, pc, T))
    # out-of-class probe: lines crossing the square (sign-changing ratios); hypotheses of 90 fail
    rng3 = random.Random(11)
    T = 4
    nodes = random_nodes(rng3, N(T + 1) + 3, den=101)
    w = [Fr(1)] * len(nodes)
    a = [Fr(1, 7), Fr(-3, 11), Fr(5, 13), Fr(-1, 17), Fr(2, 19)]
    assert all(x + y != aj for x, y in nodes for aj in a)
    out.append(check_config("OUT-OF-CLASS crossing lines T4", nodes, w, a, T, out_of_class=True))
    return out


# ------------------------------------------------------------------ mod p, source scale
def modp_ranks(nodes, a, T, p, ts):
    M = len(nodes)
    inv = lambda z: pow(z % p, -1, p)

    def fr(v):
        return (v.numerator % p) * inv(v.denominator) % p

    s = [x + y for x, y in nodes]
    xs = [fr(x) for x, y in nodes]
    ys = [fr(y) for x, y in nodes]
    ell = [[fr(s[i] - a[r]) for r in range(T + 1)] for i in range(M)]
    Id = flint.nmod_mat(M, M, [1 if i == j else 0 for i in range(M) for j in range(M)], p)
    P = {-1: flint.nmod_mat(M, M, [0] * (M * M), p)}
    Q = {}
    for j in range(T + 2):
        rows = []
        for i in range(M):
            pij = 1
            for r in range(j):
                pij = pij * ell[i][r] % p
            ip = inv(pij)
            rows += [pow(xs[i], u, p) * pow(ys[i], v, p) % p * ip % p for (u, v) in monos(j)]
        A = flint.nmod_mat(M, N(j), rows, p)
        G = A.transpose() * A          # unit weights (source window_exact)
        P[j] = A * G.inv() * A.transpose()
        Q[j] = P[j] - P[j - 1]
    out = {}
    for t in ts:
        Dinv = flint.nmod_mat(M, M, [inv(ell[i][t]) if i == j else 0 for i in range(M) for j in range(M)], p)
        Dx = flint.nmod_mat(M, M, [xs[i] if i == j else 0 for i in range(M) for j in range(M)], p)
        Dy = flint.nmod_mat(M, M, [ys[i] if i == j else 0 for i in range(M) for j in range(M)], p)
        blocks = [[[int(v) for v in row] for row in b.tolist()] for b in (Q[t - 1], Q[t], Dx * Q[t], Dy * Q[t])]
        rows = []
        for i in range(M):
            for b in blocks:
                rows += b[i]
        C = Dinv * flint.nmod_mat(M, 4 * M, rows, p)
        R2 = (Id - Q[t] - Q[t - 1]) * C
        R3 = (Id - Q[t] - Q[t - 1] - Q[t - 2]) * C
        out[t] = {"rank_R_modp": R2.rank(), "target_2t+1": 2 * t + 1,
                  "three_block_rank_modp": R3.rank(), "dim_W_t+1": t + 2}
    return out


def partB():
    import numpy as np
    rng = np.random.default_rng(1)          # the source's random_nodes(120, 1)
    xs, ys = rng.uniform(-1, 1, 120), rng.uniform(-1, 1, 120)
    nodes = [(Fr(float(x)), Fr(float(y))) for x, y in zip(xs, ys)]
    T = 9
    m = T + 1
    res = []
    primes = [2305843009213693951, 2147483647]
    rr = random.Random(99)
    configs = {"random rational offsets": distinct_offsets(rr, m, 2, 5, den=1009)}
    sig = -math.log(1e-2) / (math.sqrt(m) - 1)
    eps = [math.exp(-sig * (math.sqrt(m) - math.sqrt(j))) for j in range(1, m + 1)]
    near = [Fr(2) + Fr(math.sqrt(2) * e).limit_denominator(10 ** 12) for e in eps]
    configs["rationalized taper eps_min=1e-2 near"] = near
    configs["rationalized taper eps_min=1e-2 far"] = near[::-1]
    configs["coalescent c=2+1/2"] = [Fr(5, 2)] * m
    for name, a in configs.items():
        for p in primes:
            t0 = time.time()
            try:
                r = modp_ranks(nodes, a, T, p, range(2, T + 1))
                ok = all(v["rank_R_modp"] == 2 * t + 1 for t, v in r.items())
                res.append({"config": name, "p": p, "ranks": r, "all_full_rank_modp": ok,
                            "seconds": round(time.time() - t0, 1)})
            except ZeroDivisionError as e:
                res.append({"config": name, "p": p, "error": "singular mod p: " + str(e)})
    return {"nodes": "numpy default_rng(1).uniform(-1,1,120) x then y (source random_nodes(120,1)), exact dyadics",
            "T": T, "results": res}


if __name__ == "__main__":
    t0 = time.time()
    A = partA()
    summary = []
    for r in A:
        ts = r["t"]
        summary.append({
            "name": r["name"],
            "in_class": r["all_ell_negative"],
            "all_rank_bound": all(d["rank_bound_ok"] for d in ts.values()),
            "all_generic_rank": all(d["rank_generic"] for d in ts.values()),
            "all_topform_factorization": all(d["topform_factorization_ok"] for d in ts.values()),
            "all_detector_iso": all(d["detector_iso"] for d in ts.values()),
            "Top_iso": r.get("Top_rank_ok"),
            "all_detection_inclusion": all(d["kernel_in_W_t+1"] for d in ts.values()),
            "all_equality": all(d["equality_B1"] for d in ts.values()),
            "ranks": {t: d["rank_R"] for t, d in ts.items()},
            "constraint_ranks": {t: d["constraint_rank"] for t, d in ts.items()},
            "leak_older_nonzero": {t: d.get("leak_into_V_t-3_nonzero") for t, d in ts.items() if t >= 3},
            "wrong_block_control_gives_W": {t: d.get("control_wrong_block_gives_W_t+1") for t, d in ts.items() if t >= 3},
            "three_block_ranks": {t: d.get("control_three_block_rank") for t, d in ts.items() if t >= 3},
            "coalescent_split": {t: d.get("coalescent_R_in_Wt+1_plus_Wt-2") for t, d in ts.items()} if len(set(r["offsets"])) == 1 else None,
            "seconds": r["seconds"],
        })
        print(json.dumps(summary[-1]), flush=True)
    B = partB()
    for r in B["results"]:
        print(json.dumps({k: v for k, v in r.items() if k != "ranks"} | {"ranks": {t: v["rank_R_modp"] for t, v in r.get("ranks", {}).items()}, "three_block": {t: v["three_block_rank_modp"] for t, v in r.get("ranks", {}).items()}}), flush=True)
    out = {"partA_summary": summary, "partA_detail": A, "partB": B, "total_seconds": round(time.time() - t0, 1),
           "python": sys.version, "flint": flint.__version__}
    path = sys.argv[1] if len(sys.argv) > 1 else "b1_exact_check.json"
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("wrote", path, "total_seconds", out["total_seconds"])
