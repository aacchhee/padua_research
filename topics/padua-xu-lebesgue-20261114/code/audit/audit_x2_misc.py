#!/usr/bin/env python3
"""Auditor's spot checks for X2-33 and X2-N35 (audit-01, padua-xu-lebesgue-20261114).  Own code, defining sums only.

  farfield : X2-33 (d) lattice-sum lemma at random offsets (float64), and X2-33 (a), (b) at random points (float64,
             Lagrange values from the defining kernel sum  omega * sum_{i+j<=n} U_i(x)U_i(x_p)U_j(y)U_j(y_q)).
             MEASURED sanity only (the record's proof is analytic).
  xi       : X2-N35 in ball arithmetic: Xi_n(a) = (8/N) sum_nodes sin w sin v |Gt(w+a1, v+a2)|,
             Gt(al,be) = sum_{k,l>=1,k+l<=M} k l sin(k al) sin(l be) (defining sum), at a = 0 and a = (0.9/M, -0.9/M),
             for M = 62, 102, 202.  Certifies Xi_n(a) > Xi_n(0) if the balls separate.
Usage: python3 audit_x2_misc.py farfield|xi --out FILE
"""
import sys, json, math
import numpy as np


def nodes(M):
    return [(p, q) for p in range(1, M) for q in range(1, M + 1) if (p + q) % 2 == 1]


def farfield(rng):
    out = {"lemma_d": [], "bounds_ab": []}
    for M in (4, 6, 10, 20, 52, 102):
        N = M * (M + 1); h = math.pi / (2 * N); L = math.log(M)
        bound = (M + 1) ** 2 * (2 + L) * (5 + 2 * L)
        r = np.arange(2 * N)
        worst = 0.0
        for _ in range(200):
            u0, v0 = rng.uniform(-4, 4, size=2)
            mu = np.minimum(M + 1, 1 / np.abs(np.sin(u0 - (2 * M + 1) * h * r)))
            mv = np.minimum(M + 1, 1 / np.abs(np.sin(v0 - h * r)))
            worst = max(worst, float((mu * mv).sum() / bound))
        out["lemma_d"].append({"M": M, "max_ratio_sum_over_bound": worst})
    for n in (4, 10, 20, 40):
        M = n + 2; N = M * (M + 1); L = math.log(M)
        Gam = (1 + 1 / M) * (2 + L) * (5 + 2 * L)
        nd = nodes(M)
        w = np.array([p * math.pi / M for p, q in nd]); v = np.array([q * math.pi / (M + 1) for p, q in nd])
        om = 8 * np.sin(w) ** 2 * np.sin(v) ** 2 / N
        i = np.arange(n + 1)
        Uw = np.sin(np.outer(i + 1, w)) / np.sin(w)          # (n+1) x nodes
        Uv = np.sin(np.outer(i + 1, v)) / np.sin(v)
        mask = (i[:, None] + i[None, :]) <= n
        ra = rb = 0.0
        for _ in range(300):
            t1, t2 = rng.uniform(0.01, math.pi - 0.01, size=2)
            U1 = np.sin((i + 1) * t1) / math.sin(t1); U2 = np.sin((i + 1) * t2) / math.sin(t2)
            A = (U1[:, None] * Uw)                            # i x nodes
            B = (U2[:, None] * Uv)                            # j x nodes
            K = np.einsum("ia,ij,ja->a", A, mask.astype(float), B)
            lam = float(np.abs(om * K).sum())
            ra = max(ra, lam / (Gam / (math.sin(t1) * math.sin(t2))))
            rb = max(rb, lam / ((math.pi / 2) * (2 * M + 1) * Gam / max(math.sin(t1), math.sin(t2))))
        out["bounds_ab"].append({"n": n, "max_lambda_over_bound_a": ra, "max_lambda_over_min_bound_b": rb})
    out["ok"] = all(d["max_ratio_sum_over_bound"] <= 1 for d in out["lemma_d"]) and \
        all(d["max_lambda_over_bound_a"] <= 1 and d["max_lambda_over_min_bound_b"] <= 1 for d in out["bounds_ab"])
    return out


def xi(Ms):
    from flint import arb, fmpq, ctx
    ctx.prec = 128
    pi = arb.pi()
    res = []
    for M in Ms:
        N = M * (M + 1)
        nd = nodes(M)
        vals = {}
        for tag, (s1, s2) in {"zero": (0, 0), "shift": (fmpq(9, 10 * M), fmpq(-9, 10 * M))}.items():
            a1 = arb(s1); a2 = arb(s2)
            # prefix sums in l for each q: S_q[m] = sum_{l<=m} l sin(l (v_q + a2))
            pref = {}
            for q in range(1, M + 1):
                be = pi * q / (M + 1) + a2
                S = [arb(0)] * M; acc = arb(0)
                for l in range(1, M):
                    acc = acc + l * (l * be).sin()
                    S[l] = acc
                pref[q] = S
            tot = arb(0)
            for p, q in nd:
                al = pi * p / M + a1
                G = arb(0); S = pref[q]
                for k in range(1, M):
                    G += k * (k * al).sin() * S[M - k]
                tot += arb.sin_pi_fmpq(fmpq(p, M)) * arb.sin_pi_fmpq(fmpq(q, M + 1)) * abs(G)
            vals[tag] = 8 * tot / N
        ratio = vals["shift"] / vals["zero"]
        res.append({"M": M, "n": M - 2, "Xi0": vals["zero"].str(15), "Xi_shift": vals["shift"].str(15),
                    "ratio": ratio.str(8), "Xi0_over_M2": (vals["zero"] / M ** 2).str(6),
                    "Xishift_over_M2": (vals["shift"] / M ** 2).str(6),
                    "certified_Xi_shift_gt_Xi0": bool(vals["shift"] > vals["zero"])})
        print(res[-1], flush=True)
    return res


def main():
    a = sys.argv
    out = a[a.index("--out") + 1]
    rng = np.random.default_rng(20261114)
    if a[1] == "farfield":
        r = farfield(rng)
    else:
        r = xi([62, 102, 202])
    json.dump({"script": "code/audit/audit_x2_misc.py", "mode": a[1], "result": r}, open(out, "w"), indent=1)
    print(json.dumps(r)[:1500])


if __name__ == "__main__":
    main()
