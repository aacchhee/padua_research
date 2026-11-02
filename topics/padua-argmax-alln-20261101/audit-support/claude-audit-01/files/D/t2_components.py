"""Measured checks of the intermediate quantities of theory14 (sampled suprema; MEASURED only).

 - B-family factorization D_n=(-1)^n[V_n(X)U_m(T)+U_n(X)V_n(T)] at random/near-collision arguments
 - (5): F = a f - (sin al/2) g_u + (sin be/2) g_v on R
 - F0(n,m)=n ; |F0|<=2n and max phase Hessian entry <=4n on B (sampled)
 - normalized sampled sums: (1/N) sum_R ef |sum4 E| / (rho^2 H)  vs 118000
                             (1/N) sum_B ef |sum4 E| / rho^2      vs 10
                             (1/N) sum_R max_s |E''| / (rho^2 H)   vs 59000 (per path)
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from padlib import *

rng = np.random.default_rng(7)
out = {"factorization": [], "formula5": [], "B": [], "sums": []}


def V(n, z):
    return np.cos((2 * n + 1) * z / 2) / np.cos(z / 2)


for n in [2, 3, 4, 7, 10, 21, 40, 64, 101]:
    m = n + 1
    xb = rng.uniform(-0.05, 1.1, 200); yb = xb + rng.uniform(-0.02, 0.02, 200) * rng.choice([1, 1e-3, 1e-6, 0], 200)
    X = (xb + yb) / 2; T = (xb - yb) / 2
    lhs = Rn(n, PI - xb, PI - yb)
    rhs = (-1) ** n * (V(n, X) * U(m, T) + U(n, X) * V(n, T))
    out["factorization"].append([n, float(np.abs(lhs - rhs).max()), float(np.abs(lhs).max())])

for n in [5, 20, 51, 100]:
    m = n + 1
    J, R, e, f = odd_board(n)
    Bmask = (R == J + 1) & (J >= 2 * n / 3)
    al, be = 0.011, -0.004
    u = (J * PI + al) / n; v = (R * PI + be) / m
    a = (np.cos(al) + np.cos(be)) / 2
    den = np.cos(u) - np.cos(v)
    F5 = a * (1 + np.cos(v)) / den - np.sin(al) / 2 * np.sin(u) / den + np.sin(be) / 2 * np.sin(v) / den
    Fp = Fjr(n, J, R, al, be)
    rel = np.abs(F5 - Fp)[~Bmask] / (1 + np.abs(Fp[~Bmask]))
    out["formula5"].append([n, float(rel.max()), float(np.abs(den[~Bmask]).min())])

# B family checks and component sums
dirs = [(np.cos(t), np.sin(t)) for t in np.linspace(0, 2 * PI, 16, endpoint=False)]
for n in [2, 3, 4, 5, 8, 16, 21, 32, 50, 64, 101, 128, 200, 201]:
    m = n + 1; N = n * m; H = 1 + np.log(m)
    J, R, e, f = odd_board(n)
    Bm = (R == J + 1) & (J >= 2 * n / 3)
    F0 = Fjr(n, J, R, 0.0, 0.0)
    F0nm = F0[(J == n) & (R == m)][0]
    # sampled phase Hessian on B over diamond |al|+|be|<=1/64
    hh = 1e-3
    maxH = 0.0
    for (ca, cb) in [(0, 0)] + [(c[0], c[1]) for c in dirs]:
        for r in (1 / 128, 1 / 64):
            s1 = abs(ca) + abs(cb)
            al0, be0 = (r * ca / s1, r * cb / s1) if s1 > 0 else (0.0, 0.0)
            JB, RB = J[Bm], R[Bm]
            f00 = Fjr(n, JB, RB, al0, be0)
            faa = (Fjr(n, JB, RB, al0 + hh, be0) - 2 * f00 + Fjr(n, JB, RB, al0 - hh, be0)) / hh**2
            fbb = (Fjr(n, JB, RB, al0, be0 + hh) - 2 * f00 + Fjr(n, JB, RB, al0, be0 - hh)) / hh**2
            fab = (Fjr(n, JB, RB, al0 + hh, be0 + hh) - Fjr(n, JB, RB, al0 + hh, be0 - hh)
                   - Fjr(n, JB, RB, al0 - hh, be0 + hh) + Fjr(n, JB, RB, al0 - hh, be0 - hh)) / (4 * hh**2)
            maxH = max(maxH, float(np.max(np.abs(np.concatenate([faa, fbb, fab])))))
    out["B"].append({"n": n, "F0(n,m)": float(F0nm), "max|F0|/n on B": float(np.abs(F0[Bm]).max() / n),
                     "min F0/n on B": float(F0[Bm].min() / n),
                     "sampled max|F_ij|/n on B": maxH / n, "|B|": int(Bm.sum())})
    # component sums for a few (al,be) at rho=1/64 and rho=1e-2
    worstR = 0; worstB = 0; worstE2 = 0
    for rho in (1e-2, 1 / 64):
        for t in np.linspace(0, 1, 9):
            al, be = rho * t, rho * (1 - t)
            a = (np.cos(al) + np.cos(be)) / 2
            S4 = sum(Fjr(n, J, R, sa * al, sb * be) for sa in (1, -1) for sb in (1, -1))
            Esum = S4 - 4 * a * F0
            cR = (e * f * np.abs(Esum))[~Bm].sum() / N / (rho**2 * H)
            cB = (e * f * np.abs(Esum))[Bm].sum() / N / rho**2
            worstR = max(worstR, cR); worstB = max(worstB, cB)
            # E'' along the two paths, sampled in s
            for (pa, pb) in ((al, be), (al, -be)):
                def E(s):
                    aa = (np.cos(s * pa) + np.cos(s * pb)) / 2
                    return Fjr(n, J, R, s * pa, s * pb) - aa * F0
                hs = 1e-2
                mx = np.zeros(len(J))
                for s in np.linspace(-1, 1, 9):
                    e2 = (E(s + hs) - 2 * E(s) + E(s - hs)) / hs**2
                    mx = np.maximum(mx, np.abs(e2))
                worstE2 = max(worstE2, mx[~Bm].sum() / N / (rho**2 * H))
    out["sums"].append({"n": n, "max (1/N)sum_R ef|sum4E|/(rho^2 H) [claim<=118000]": worstR,
                        "max (1/N)sum_B ef|sum4E|/rho^2 [claim<=10]": worstB,
                        "max (1/N)sum_R max_s|E''|/(rho^2 H) [claim<=59000]": worstE2})
    print(n, out["B"][-1], out["sums"][-1], flush=True)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "t2_components.json"), "w"), indent=1)
print(json.dumps({k: out[k] for k in ("factorization", "formula5")}, indent=0))
