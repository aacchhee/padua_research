#!/usr/bin/env python3
"""Independent checker for the C-MP certificate (Path B, mpmath interval arithmetic mpmath.iv).

Usage: python3 cmp_check.py [--cert ../../evidence/mp-cmp-certificate.json] [--out ../../evidence/mp-cmp-check.json] [--dps 70]
Self-contained: imports neither mp_exact nor mp_kernel.  For every row (even n) it recomputes
lambda_n at the four vertices with interval arithmetic from the sum-form kernel
   l_{m,k}(P) = omega_{m,k} sum_{i+j<=n} U_i(x_m) U_j(y_k) U_i(P_x) U_j(P_y),  1/omega = sum U_i(x_m)^2 U_j(y_k)^2
(omega from its SUM form; the closed form 8 sin^2 sin^2/((n+2)(n+3)) is evaluated too and must overlap),
and checks (i) each recomputed interval intersects the certificate interval and the two enclosures
agree to within 1e-40, (ii) the certified claims: lam(1,1) != lam(1,-1) (disjoint intervals),
lam(+-1,-1) interval contains n+1, sign of lam(1,1)-(n+1)(n+2)/2.
"""
import argparse, json, sys, time, platform
import mpmath as mp
from mpmath import iv, mpf


def Uiv(x, n):
    u = [iv.mpf(1), 2 * x]
    for i in range(2, n + 1):
        u.append(2 * x * u[-1] - u[-2])
    return u[:n + 1]


def lam_vertices_iv(n, verts):
    idx = [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]
    Uv = {s: Uiv(iv.mpf(s), n) for s in (1, -1)}        # U_i(+-1) = (+-1)^i (i+1), computed by recurrence
    lam = {v: iv.mpf(0) for v in verts}
    om_overlap = True
    for m in range(1, n + 2):
        for k in range(1, n // 2 + 2):
            q = 2 * k if m % 2 else 2 * k - 1
            w = iv.pi * m / (n + 2)
            v = iv.pi * q / (n + 3)
            Ux, Uy = Uiv(iv.cos(w), n), Uiv(iv.cos(v), n)
            inv_om = iv.mpf(0)
            for (i, j) in idx:
                inv_om += Ux[i] ** 2 * Uy[j] ** 2
            om = 1 / inv_om
            om_c = 8 * iv.sin(w) ** 2 * iv.sin(v) ** 2 / ((n + 2) * (n + 3))
            if not (om.a <= om_c.b and om_c.a <= om.b):
                om_overlap = False
            for (sx, sy) in verts:
                s = iv.mpf(0)
                for (i, j) in idx:
                    s += Ux[i] * Uy[j] * Uv[sx][i] * Uv[sy][j]
                lam[(sx, sy)] += abs(om * s)
    return lam, om_overlap


def LO(x):
    return mp.mpf(x._mpi_[0])


def HI(x):
    return mp.mpf(x._mpi_[1])


def parse(lo, hi):
    return iv.mpf([mpf(lo), mpf(hi)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cert", default="../../evidence/mp-cmp-certificate.json")
    ap.add_argument("--out", default="../../evidence/mp-cmp-check.json")
    ap.add_argument("--dps", type=int, default=70)
    ap.add_argument("--nmax", type=int, default=None)
    a = ap.parse_args()
    mp.mp.dps = a.dps
    iv.dps = a.dps
    cert = json.load(open(a.cert))
    names = {"(1,1)": (1, 1), "(-1,1)": (-1, 1), "(1,-1)": (1, -1), "(-1,-1)": (-1, -1)}
    out_rows = []
    t0 = time.time()
    for row in cert["rows"]:
        n = row["n"]
        if a.nmax and n > a.nmax:
            continue
        lam, om_ok = lam_vertices_iv(n, list(names.values()))
        ok_int, widths, gap = True, [], None
        for nm, v in names.items():
            c = parse(*row["lambda"][nm])
            L = lam[v]
            widths.append(float(HI(L) - LO(L)))
            inter_ok = (L.a <= c.b) and (c.a <= L.b)                       # intervals intersect
            close = (abs((LO(L) + HI(L)) / 2 - (LO(c) + HI(c)) / 2) < mpf(10) ** -40)                  # enclosures consistent
            ok_int = ok_int and inter_ok and close
        L11, L1m = lam[(1, 1)], lam[(1, -1)]
        disjoint = bool(L11.a > L1m.b or L1m.a > L11.b)
        gap = float(LO(L11) - HI(L1m))
        n1 = iv.mpf(n + 1)
        cont = all((lam[v].a <= n + 1 <= lam[v].b) for v in ((1, -1), (-1, -1)))
        T = (n + 1) * (n + 2) // 2
        sign = "gt" if L11.a > T else ("lt" if L11.b < T else "undecided")
        mirror = bool(lam[(1, 1)].a <= lam[(-1, 1)].b and lam[(-1, 1)].a <= lam[(1, 1)].b)
        r = {"n": n, "intersects_and_close_to_certificate": bool(ok_int), "omega_sum_vs_closed_overlap": bool(om_ok),
             "max_iv_width": max(widths), "lam11_ne_lam1m1_disjoint_B": disjoint, "gap_lower_bound": gap,
             "n_plus_1_in_lam(+-1,-1)_B": bool(cont), "lam11_vs_T": sign,
             "matches_cert_claims": bool(disjoint == row["claim_lam(1,1)_ne_lam(1,-1)"] and cont == row["claim_lam(+-1,-1)_contains_n+1"]
                                         and (sign == "gt") == (row["claim_lam(1,1)_gt_(n+1)(n+2)/2"] is True)),
             "lam11_eq_lam-11_overlap": mirror}
        out_rows.append(r)
        print(n, r["intersects_and_close_to_certificate"], disjoint, cont, sign, "%.1e" % r["max_iv_width"], flush=True)
    res = {"checker": "code/mp/cmp_check.py", "command": "python3 " + " ".join(sys.argv),
           "versions": {"python": platform.python_version(), "mpmath": mp.__version__, "mp.iv.dps": a.dps},
           "rows": out_rows,
           "ALL_rows_consistent": all(r["intersects_and_close_to_certificate"] and r["matches_cert_claims"] and r["omega_sum_vs_closed_overlap"] for r in out_rows),
           "symmetry_refuted_at_all_n": all(r["lam11_ne_lam1m1_disjoint_B"] for r in out_rows),
           "n_plus_1_contained_all": all(r["n_plus_1_in_lam(+-1,-1)_B"] for r in out_rows),
           "wall_seconds": round(time.time() - t0, 1)}
    json.dump(res, open(a.out, "w"), indent=0)
    print("ALL_rows_consistent", res["ALL_rows_consistent"], "wall", res["wall_seconds"])


if __name__ == "__main__":
    main()
