#!/usr/bin/env python3
"""Claude audit-01, A4(a) sub-audit: floating-point (float64) exploration of the
central-edge envelope R_cen(n) and of the quantities used in theories 74-77.

SUPPORTING NUMERICS ONLY (no outward rounding, finite grids + local refinement;
R_cen values are lower estimates of the true cell maximum up to the optimizer
tolerance).  Independent of developer code.

Edge values use the all-edge identity 70.(1), validated against direct Vandermonde
cardinals for n<=9 by audit_a4_identity.py, and here additionally cross-checked
against an independent O(N n^2) evaluation of the accepted A1 kernel
L_B(z)=w_B(K_n(z,B)-T_n(z1)T_n(B1)) at a few points for moderate n.

For each n (both parities) records:
  Lambda_c (max of the four corner values), C_n (72's concrete point), the 71
  right-hand side at C_n's point, R_cen (max over both x edges, |t-pi/2|<=pi/m),
  argmax edge/angle, whether the argmax is at a cell endpoint, nearest
  complementary phase beta_n and s_n, S_n(s_n), Delta_n(beta_n,s_n),
  sup_{|s|<=pi/6} S_n(s)-Lambda_c (grid+refine), and
  max_{|s|<=pi} [S_n(s)-cos^2(s/2)Lambda_c]/log(n+1) (grid).
"""
import json, sys, time
import numpy as np
from scipy.optimize import minimize_scalar

PI = np.pi
G_CONST = 0.548514842399558   # supporting value from audit_a4_g.py (quadrature)

def U(mm, x):
    l = np.rint(x / PI)
    d = x - l * PI
    sgn = np.where(((mm - 1) * l.astype(np.int64)) % 2 == 0, 1.0, -1.0)
    small = np.abs(d) < 1e-9
    ds = np.where(small, 1.0, d)
    val = np.where(small, mm * (1.0 - (mm * mm - 1.0) * d * d / 6.0), np.sin(mm * ds) / np.sin(ds))
    return sgn * val

def D(n, u, v):
    S = 0.5 * (u + v); T = 0.5 * (v - u)
    return U(n + 1, S) * U(n + 1, T) + U(n, S) * U(n, T)

class Padua:
    def __init__(self, n):
        self.n = n; m = n + 1; self.m = m; self.N = n * m
        J, K = np.meshgrid(np.arange(n + 1), np.arange(m + 1), indexing="ij")
        mask = (J + K) % 2 == 0
        self.j = J[mask].astype(float); self.k = K[mask].astype(float)
        ej = np.where((self.j == 0) | (self.j == n), 0.5, 1.0)
        ek = np.where((self.k == 0) | (self.k == m), 0.5, 1.0)
        self.ej, self.ek = ej, ek
        self.w = 2 * ej * ek / self.N
        self.a = self.j * PI / n; self.b = self.k * PI / m
        self.sgnj = np.where(self.j % 2 == 0, 1.0, -1.0)
        # periodic odd board for S_n
        Jp, Rp = np.meshgrid(np.arange(2 * n), np.arange(2 * m), indexing="ij")
        mk = (Jp + Rp) % 2 == 1
        self.pj = Jp[mk].astype(float); self.pr = Rp[mk].astype(float)
        self.psgn = np.where(self.pj % 2 == 0, 1.0, -1.0)

    def lam_xedge(self, eps, t):
        th = 0.0 if eps == 1 else PI
        n = self.n
        ker = 0.5 * (D(n, th + self.a, t + self.b) + D(n, th + self.a, t - self.b)) \
            - np.cos(n * th) * self.sgnj
        return float(np.sum(self.w * np.abs(ker)))

    def lam_yedge(self, phc, t):
        n = self.n
        ker = 0.5 * (D(n, t + self.a, phc + self.b) + D(n, t - self.a, phc + self.b)) \
            - np.cos(n * t) * self.sgnj
        return float(np.sum(self.w * np.abs(ker)))

    def S(self, s):
        n, m = self.n, self.m
        H = 0.5 * (self.psgn * D(n, self.pj * PI / n, self.pr * PI / m + s / m) - 1.0)
        return float(np.sum(np.abs(H)) / self.N)

    def Delta(self, eps, q, s):
        n, m = self.n, self.m
        phi = q * PI / m + s / m
        jp = self.j if eps == 1 else n - self.j
        tau = np.where(jp % 2 == 0, 1.0, -1.0)
        Hp = 0.5 * (tau * D(n, jp * PI / n, phi + self.b) - 1.0)
        Hm = 0.5 * (tau * D(n, jp * PI / n, phi - self.b) - 1.0)
        return float(np.sum(self.w * (np.abs(Hp) + np.abs(Hm) - np.abs(Hp + Hm))))

def kernel_direct_lambda(n, x, y):
    """Independent O(N n^2) evaluation from the accepted A1 kernel formula."""
    m = n + 1; N = n * m
    tot = 0.0
    p = np.arange(n + 1)
    cp = np.where(p == 0, 1.0, 2.0)
    Tx = np.cos(p * np.arccos(np.clip(x, -1, 1)))
    Ty = np.cos(p * np.arccos(np.clip(y, -1, 1)))
    for j in range(n + 1):
        for k in range(m + 1):
            if (j + k) % 2: continue
            ej = 0.5 if j in (0, n) else 1.0
            ek = 0.5 if k in (0, m) else 1.0
            w = 2 * ej * ek / N
            TB1 = np.cos(p * j * PI / n); TB2 = np.cos(p * k * PI / m)
            A = cp * Tx * TB1; B = cp * Ty * TB2
            # sum_{p+q<=n} A_p B_q
            cumB = np.cumsum(B)
            Kv = float(np.sum(A * cumB[n - p]))
            Kv -= Tx[n] * TB1[n]
            tot += w * abs(Kv)
    return tot

def maximize_on(f, lo, hi, G):
    ts = np.linspace(lo, hi, G)
    vals = np.array([f(t) for t in ts])
    best_t, best_v = ts[np.argmax(vals)], vals.max()
    # refine around the top local maxima of the grid
    idx = [i for i in range(G) if (i == 0 or vals[i] >= vals[i - 1]) and (i == G - 1 or vals[i] >= vals[i + 1])]
    idx = sorted(idx, key=lambda i: -vals[i])[:4]
    h = (hi - lo) / (G - 1)
    for i in idx:
        a_, b_ = max(lo, ts[i] - h), min(hi, ts[i] + h)
        r = minimize_scalar(lambda t: -f(t), bounds=(a_, b_), method="bounded",
                            options={"xatol": 1e-12 * max(1.0, hi - lo)})
        if -r.fun > best_v:
            best_v, best_t = -r.fun, r.x
    return best_t, best_v

def run(n, G, Gs=61, Gr=121):
    P = Padua(n); m = P.m
    corners = {"(1,1)": P.lam_xedge(1, 0.0), "(1,-1)": P.lam_xedge(1, PI),
               "(-1,1)": P.lam_xedge(-1, 0.0), "(-1,-1)": P.lam_xedge(-1, PI)}
    # y-edge corner consistency
    cy = {"(1,1)": P.lam_yedge(0.0, 0.0), "(-1,1)": P.lam_yedge(0.0, PI),
          "(1,-1)": P.lam_yedge(PI, 0.0), "(-1,-1)": P.lam_yedge(PI, PI)}
    corner_consistency = max(abs(corners[k] - cy[k]) for k in corners)
    Lc = max(corners.values())
    # 72's concrete point
    if n % 2 == 1:
        q = m // 2; eps = (-1) ** (q + 1)
    else:
        q = (m - 1) // 2 if ((m - 1) // 2) % 2 == 1 else (m + 1) // 2
        eps = 1
    beta = q * PI / m
    Cn = P.lam_xedge(eps, beta)
    # 71 rhs at that point
    A = eps * np.cos(P.a); zp = np.cos(beta + P.b); zm = np.cos(beta - P.b)
    inside = (zp < A) & (A < zm)
    with np.errstate(divide="ignore", invalid="ignore"):
        hv = np.where(inside, np.minimum((1 + zp) / (A - zp), (1 + zm) / (zm - A)), 0.0)
    rhs71 = float(4 * np.sum(P.ej * P.ek * hv) / P.N + 2.0 / P.N)
    # R_cen
    lo, hi = PI / 2 - PI / m, PI / 2 + PI / m
    best = None
    for e in (1, -1):
        t_, v_ = maximize_on(lambda t: P.lam_xedge(e, t), lo, hi, G)
        if best is None or v_ > best[2]:
            best = (e, t_, v_)
    e, tmax, Rcen = best
    at_endpoint = bool(min(abs(tmax - lo), abs(tmax - hi)) < 1e-9)
    # nearest complementary phase on that edge
    r_eps = n if e == -1 else 0
    qs = [qq for qq in range(-2, m + 3) if (r_eps + qq) % 2 == 1]
    qn = min(qs, key=lambda qq: abs(qq * PI / m - tmax))
    s_n = (tmax - qn * PI / m) * m
    Ssn = P.S(s_n); Dsn = P.Delta(e, qn, s_n)
    decomp_err = abs(Rcen - (Ssn - Dsn))
    S0 = P.S(0.0)
    # sup over |s|<=pi/6 of S_n(s)-Lambda_c
    ss_t, ss_v = maximize_on(lambda s: P.S(s), 0.0, PI / 6, Gs)
    # 74-type ratio on [0,pi] (S even)
    sgrid = np.linspace(0, PI, Gr)
    ratio = max((P.S(s) - np.cos(s / 2) ** 2 * Lc) for s in sgrid) / np.log(n + 1)
    rec = {"n": n, "Lambda_c": Lc, "corner_values": corners, "corner_x_vs_y_edge_consistency": corner_consistency,
           "S0_minus_Lambda_c": S0 - Lc,
           "C_point": {"eps": eps, "q": q, "beta_minus_pi_over_2": beta - PI / 2},
           "C_n": Cn, "Lambda_c_minus_C_n": Lc - Cn, "rhs71_at_C_point": rhs71, "err71": abs((Lc - Cn) - rhs71),
           "R_cen": Rcen, "Lambda_c_minus_R_cen": Lc - Rcen, "gap_minus_g": Lc - Rcen - G_CONST,
           "n_times_gap_minus_g": n * (Lc - Rcen - G_CONST),
           "R_cen_minus_C_n": Rcen - Cn,
           "argmax_eps": e, "argmax_t_minus_pi_over_2": tmax - PI / 2, "argmax_in_units_pi_over_m": (tmax - PI / 2) * m / PI,
           "argmax_at_cell_endpoint": at_endpoint,
           "nearest_q": qn, "s_n": s_n, "S_n_at_s_n": Ssn, "S_n_at_s_n_minus_Lambda_c": Ssn - Lc,
           "Delta_n_at_s_n": Dsn, "Delta_minus_g": Dsn - G_CONST, "decomposition_err": decomp_err,
           "sup_small_s_S_minus_Lambda_c": ss_v - Lc, "argsup_small_s": ss_t,
           "max_over_s_S_minus_cos2_Lc_over_log": ratio}
    return rec

def main():
    t0 = time.time()
    out = {"script": "audit_a4_rcen.py", "g_supporting_value": G_CONST, "records": [], "cross_checks": []}
    # independent cross-check of the edge formula against the A1 kernel at moderate n
    for n in (12, 13):
        P = Padua(n)
        for (e, t) in ((1, 1.234), (-1, 1.6), (1, PI / 2), (-1, PI / 2 + PI / (2 * (n + 1)))):
            v70 = P.lam_xedge(e, t); vk = kernel_direct_lambda(n, float(e), np.cos(t))
            out["cross_checks"].append({"n": n, "eps": e, "t": t, "edge70": v70, "A1kernel": vk, "diff": abs(v70 - vk)})
        for (phc, t) in ((0.0, 0.77), (PI, 2.2)):
            v70 = P.lam_yedge(phc, t); vk = kernel_direct_lambda(n, np.cos(t), np.cos(phc))
            out["cross_checks"].append({"n": n, "yedge_phi": phc, "t": t, "edge70": v70, "A1kernel": vk, "diff": abs(v70 - vk)})
    ns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 20, 21, 26, 27, 40, 41, 50, 51, 63, 64, 98, 99, 127, 128,
          199, 200, 255, 256, 399, 400]
    for n in ns:
        G = 401 if n <= 64 else (161 if n <= 200 else 81)
        Gs, Gr = (61, 121) if n <= 200 else (31, 41)
        rec = run(n, G, Gs, Gr)
        rec["grid_points"] = [G, Gs, Gr]
        out["records"].append(rec)
        print(f"n={n} gap={rec['Lambda_c_minus_R_cen']:.6f} Rcen-Cn={rec['R_cen_minus_C_n']:.2e} "
              f"s_n={rec['s_n']:.3f} Delta-g={rec['Delta_minus_g']:.3e} supS-L={rec['sup_small_s_S_minus_Lambda_c']:.2e} "
              f"t={time.time()-t0:.0f}s", file=sys.stderr, flush=True)
    out["elapsed_seconds"] = round(time.time() - t0, 2)
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
