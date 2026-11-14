#!/usr/bin/env python3
"""Independent check (Opus 5.5 checker, 2026-11-14) of theory/X2-21, X2-22, X2-23 vertex values.

Path: build the Morrow-Patterson nodes directly from the literature (m, k) convention
(literature-xu-mp.md section 2), solve the Chebyshev-T product Vandermonde system
    V[z, (i,j)] = T_i(x_z) T_j(y_z),  i + j <= n
in mpmath at DPS digits, so that the Lagrange values at a point P are  l(P) = V^{-T} b(P), b(P)_{(i,j)} = T_i(P_x) T_j(P_y).
No kernel, no U-polynomials, no closed form is used to obtain l.  Then compare with the closed forms of
X2-21 part 3 (own transcription) node by node, and lambda_n at the four vertices.

Also checks: U_n(x_m) = (-1)^{m+1} at every abscissa; the sign rules of X2-22 and X2-23(b) using the
Vandermonde values (not the closed forms).

Usage: python3 ic_x2_vandermonde.py [--nmax 20] [--dps 60] [--out /tmp/ic-x2/vandermonde.json]
"""
import sys, json, time
import mpmath as mp


def mp_nodes(n):
    """(m, k, x, y) for the MP set, literature convention."""
    out = []
    for m in range(1, n + 2):
        x = mp.cos(m * mp.pi / (n + 2))
        for k in range(1, n // 2 + 2):
            num = 2 * k if m % 2 == 1 else 2 * k - 1
            y = mp.cos(num * mp.pi / (n + 3))
            out.append((m, num, x, y))
    return out


def cheb_T(t, n):
    T = [mp.mpf(1), t]
    for i in range(2, n + 1):
        T.append(2 * t * T[-1] - T[-2])
    return T[:n + 1]


def main():
    a = sys.argv[1:]
    nmax = int(a[a.index("--nmax") + 1]) if "--nmax" in a else 20
    dps = int(a[a.index("--dps") + 1]) if "--dps" in a else 60
    out = a[a.index("--out") + 1] if "--out" in a else "/tmp/ic-x2/vandermonde.json"
    mp.mp.dps = dps
    rows = []
    t0 = time.time()
    for n in range(2, nmax + 1, 2):
        M = n + 2
        nd = mp_nodes(n)
        idx = [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]
        D = len(idx)
        assert len(nd) == D == (n + 1) * (n + 2) // 2
        V = mp.matrix(D, D)
        for r, (m, q, x, y) in enumerate(nd):
            Tx, Ty = cheb_T(x, n), cheb_T(y, n)
            for c, (i, j) in enumerate(idx):
                V[r, c] = Tx[i] * Ty[j]
        Vt = V.T
        verts = {(1, 1): None, (-1, 1): None, (1, -1): None, (-1, -1): None}
        res = {"n": n, "dim": D}
        max_node_err = mp.mpf(0)
        sign_lower_ok = True; sign_upper_ok = True; Un_ok = True
        for (ex, ey) in verts:
            b = mp.matrix(D, 1)
            for c, (i, j) in enumerate(idx):
                b[c] = mp.mpf(ex) ** i * mp.mpf(ey) ** j        # T_i(+-1) = (+-1)^i
            ell = mp.lu_solve(Vt, b)
            lam = mp.fsum(abs(ell[r]) for r in range(D))
            # closed forms of X2-21 part 3 (own transcription)
            cf_sum = mp.mpf(0)
            for r, (m, q, x, y) in enumerate(nd):
                om = 8 * (1 - x ** 2) * (1 - y ** 2) / ((n + 2) * (n + 3))
                s = (-1) ** m
                if (ex, ey) == (1, 1):
                    cf = s * om * ((2 * M + 1) / (4 * (x - y) ** 2) - (2 + x + y) / (2 * (x - y) ** 3))
                elif (ex, ey) == (-1, 1):
                    cf = s * om * ((2 * M + 1) / (4 * (x + y) ** 2) + (2 - x + y) / (2 * (x + y) ** 3))
                elif (ex, ey) == (1, -1):
                    cf = -s * om / (4 * (x + y) ** 2)
                else:
                    cf = -s * om / (4 * (x - y) ** 2)
                max_node_err = max(max_node_err, abs(cf - ell[r]))
                cf_sum += abs(cf)
                if ey == -1 and mp.sign(ell[r]) != (-1) ** (m + 1):
                    sign_lower_ok = False
                if (ex, ey) == (1, 1):
                    pred = s * mp.sign((x - y) * ((2 * n + 3) * x - (2 * n + 7) * y - 4))
                    if mp.sign(ell[r]) != pred:
                        sign_upper_ok = False
            key = "%+d,%+d" % (ex, ey)
            res["lam" + key] = mp.nstr(lam, 30)
            res["lam" + key + "_minus_closedform_sum"] = mp.nstr(lam - cf_sum, 3)
            verts[(ex, ey)] = lam
        # U_n(x_m) = (-1)^{m+1}
        for m in range(1, n + 2):
            w = m * mp.pi / M
            Un = mp.sin((n + 1) * w) / mp.sin(w)
            if abs(Un - (-1) ** (m + 1)) > mp.mpf(10) ** (-(dps - 10)):
                Un_ok = False
        res["max_node_err_vs_closed_forms"] = mp.nstr(max_node_err, 3)
        res["lam(1,-1)-(n+1)"] = mp.nstr(verts[(1, -1)] - (n + 1), 3)
        res["lam(-1,-1)-(n+1)"] = mp.nstr(verts[(-1, -1)] - (n + 1), 3)
        res["lam(-1,1)-lam(1,1)"] = mp.nstr(verts[(-1, 1)] - verts[(1, 1)], 3)
        res["lam(1,1)-dim"] = mp.nstr(verts[(1, 1)] - D, 12)
        res["sign_lower_(-1)^(m+1)_ok"] = sign_lower_ok
        res["sign_upper_band_rule_ok"] = sign_upper_ok
        res["U_n(x_m)=(-1)^(m+1)_ok"] = Un_ok
        rows.append(res)
        print(json.dumps(res), flush=True)
    summ = {"script": "code/mp/independent/ic_x2_vandermonde.py", "dps": dps, "nmax": nmax,
            "mpmath": mp.__version__, "wall_s": round(time.time() - t0, 1), "rows": rows}
    json.dump(summ, open(out, "w"), indent=1)
    print("wall", summ["wall_s"], "s; wrote", out)


if __name__ == "__main__":
    main()
