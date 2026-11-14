#!/usr/bin/env python3
"""X2 round 3: first variation of the Morrow-Patterson Lebesgue function at the vertex (1,1), in ball arithmetic.

Certifies, for every even n in [nmin, nmax] (M = n+2, N = M(M+1)), the two inequalities of theory/X2-32:

    D_x(n) := sum_a sgn(l_a(1,1)) d/dx l_a(1,1) > 0,      D_y(n) := sum_a sgn(l_a(1,1)) d/dy l_a(1,1) > 0,

through the band representation proved in theory/X2-31:

    D_x = -n(n+1)(n+2)/3 + 2 sum_{a in B} Tx_a,     D_y = 2 sum_{a in B} Ty_a,
    Tx_a = -(omega_a/4) Nx_a / d^5,   Ty_a = -(omega_a/4) Ny_a / d^5,          (d = x_a - y_a, s = 2 + x_a + y_a)
    Nx = M(M+1)(M+2)/3 d^3 - (2M^2 + (2M^2+8M+4) x) d^2 + (6 x s - (8M+6)(1-x^2)) d + 8 (1-x^2) s,
    Ny = (M-1)M(M+1)/3 d^3 + (y(6M+2) - 2(M+1)^2 - 2M(M+1) y) d^2 - (6 y s + (8M+2)(1-y^2)) d + 8 (1-y^2) s,
    omega_a = 8 (1-x^2)(1-y^2)/N,   B = {a : Y < X < kappa Y},  X=(1+x)/2, Y=(1+y)/2, kappa=(2M+3)/(2M-1).

Node bookkeeping (theory/X2-23 (d), X2-25 Step A): p' = M-p in [1,M-1], q' = M+1-q in [1,M], p' = q' (mod 2),
X = sin^2(pi p'/(2M)), Y = sin^2(pi q'/(2M+2)), X - Y = sin(pi S/(2N)) sin(pi R/(2N)), R = p'(M+1) - q'M, S = p'(M+1) + q'M.
A node is in B only if q' <= p' (X > Y), and for fixed p' the quantity (M-1/2)X - (M+3/2)Y increases when q' decreases,
so for fixed p' the band is {q' = p', p'-2, ..., q'_min(p')}: the scan stops at the first q' with a certified
(M-1/2)X - (M+3/2)Y > 0.  Every sign used is certified (a ball containing 0 aborts the run for that n).

Modes
  --band   (default) band representation above, even n in [nmin, nmax].
  --full   independent path for small n: all nodes, defining kernel sums
           K = sum (i+1)(j+1) U_i(x_a)U_j(y_a), K_x = sum i(i+1)(i+2)/3 (j+1) U_i U_j, K_y likewise, no closed form,
           D_x = sum_a sgn(K_a) omega_a K_x,a ; also checks the closed forms Nx, Ny node by node (ball overlap).
Output: JSON summary (per n: lower/upper bounds of D_x, D_y, D_x/M^4, D_y/M^4, band size, flags).

Usage: python3 x2r3_first_variation_arb.py [--band|--full] [--nmin 2] [--nmax 400] [--prec 192] [--out /tmp/x2r3/fv.json]
Requires python-flint >= 0.6.
"""
import sys, json, os, time
from flint import arb, fmpq, ctx


def sin2_pi(num, den):
    """sin^2(pi*num/den) as an arb."""
    s = arb.sin_pi_fmpq(fmpq(num, den))
    return s * s


def band_terms(M, pp, qq, N):
    """For the node (p', q'): returns (bandtest, A, Tx, Ty) as arbs; bandtest = (M-1/2)X - (M+3/2)Y."""
    X = sin2_pi(pp, 2 * M)
    Y = sin2_pi(qq, 2 * M + 2)
    R = pp * (M + 1) - qq * M
    S = pp * (M + 1) + qq * M
    XmY = arb.sin_pi_fmpq(fmpq(S, 2 * N)) * arb.sin_pi_fmpq(fmpq(R, 2 * N))
    test = (arb(2 * M - 1) / 2) * X - (arb(2 * M + 3) / 2) * Y
    x = 2 * X - 1
    y = 2 * Y - 1
    d = 2 * XmY
    s = 2 * (X + Y)
    omx = 4 * X * (1 - X)          # 1 - x^2
    omy = 4 * Y * (1 - Y)          # 1 - y^2
    om4 = 2 * omx * omy / N        # omega/4
    d2 = d * d
    d3 = d2 * d
    d5 = d3 * d2
    # (-1)^p l(1,1) = A = (omega/4) [(2M+1) d - 2 s] / d^3
    A = om4 * ((2 * M + 1) * d - 2 * s) / d3
    Nx = arb(M * (M + 1) * (M + 2)) / 3 * d3 - (2 * M * M + (2 * M * M + 8 * M + 4) * x) * d2 \
        + (6 * x * s - (8 * M + 6) * omx) * d + 8 * omx * s
    Ny = arb((M - 1) * M * (M + 1)) / 3 * d3 + (y * (6 * M + 2) - 2 * (M + 1) ** 2 - 2 * M * (M + 1) * y) * d2 \
        - (6 * y * s + (8 * M + 2) * omy) * d + 8 * omy * s
    Tx = -om4 * Nx / d5
    Ty = -om4 * Ny / d5
    return test, A, Tx, Ty


def run_band(n):
    M = n + 2
    N = M * (M + 1)
    sumA = arb(0)
    sumTx = arb(0)
    sumTy = arb(0)
    nband = 0
    neg_Tx = 0
    neg_Ty = []
    ok = True
    for pp in range(1, M):
        qq = pp
        while qq >= 1:
            test, A, Tx, Ty = band_terms(M, pp, qq, N)
            if test < 0:
                if not (A < 0):
                    ok = False
                sumA += -A
                sumTx += Tx
                sumTy += Ty
                nband += 1
                if not (Tx > 0):
                    neg_Tx += 1
                if not (Ty > 0):
                    neg_Ty.append((M - pp, M + 1 - qq))
            elif test > 0:
                break
            else:
                ok = False
                break
            qq -= 2
    Dx = 2 * sumTx - arb(n * (n + 1) * (n + 2)) / 3
    Dy = 2 * sumTy
    lam = 2 * sumA - (n + 1)
    return {"n": n, "M": M, "band_size": nband, "signs_certified": ok,
            "lam11": lam.str(25), "Dx": Dx.str(20), "Dy": Dy.str(20),
            "Dx_over_M4_lower": float((Dx / arb(M) ** 4).lower()), "Dy_over_M4_lower": float((Dy / arb(M) ** 4).lower()),
            "Dx_pos": bool(Dx > 0), "Dy_pos": bool(Dy > 0),
            "band_nodes_with_Tx_not_certified_positive": neg_Tx,
            "band_nodes_(p,q)_with_Ty_not_certified_positive": neg_Ty[:6]}


def U_list(x, n):
    u = [arb(1), 2 * x]
    for i in range(2, n + 1):
        u.append(2 * x * u[-1] - u[-2])
    return u[:n + 1]


def run_full(n):
    """Independent path: all nodes, defining sums; compares with the closed forms."""
    M = n + 2
    N = M * (M + 1)
    Dx = arb(0)
    Dy = arb(0)
    lam = arb(0)
    ok = True
    closed_ok = True
    w1 = [arb(i + 1) for i in range(n + 1)]
    w3 = [arb(i * (i + 1) * (i + 2)) / 3 for i in range(n + 1)]
    for p in range(1, M):
        x = arb.cos_pi_fmpq(fmpq(p, M))
        Ux = U_list(x, n)
        for q in range(1, M + 1):
            if (p + q) % 2 == 0:
                continue
            y = arb.cos_pi_fmpq(fmpq(q, M + 1))
            Uy = U_list(y, n)
            # prefix sums in j
            c1 = [arb(0)] * (n + 2)
            c3 = [arb(0)] * (n + 2)
            for j in range(n + 1):
                c1[j + 1] = c1[j] + w1[j] * Uy[j]
                c3[j + 1] = c3[j] + w3[j] * Uy[j]
            K = arb(0); Kx = arb(0); Ky = arb(0)
            for i in range(n + 1):
                K += w1[i] * Ux[i] * c1[n + 1 - i]
                Kx += w3[i] * Ux[i] * c1[n + 1 - i]
                Ky += w1[i] * Ux[i] * c3[n + 1 - i]
            om = 8 * (1 - x * x) * (1 - y * y) / N
            if K > 0:
                sg = 1
            elif K < 0:
                sg = -1
            else:
                ok = False
                sg = 0
            lam += sg * om * K
            Dx += sg * om * Kx
            Dy += sg * om * Ky
            # closed forms (theory/X2-31): (-1)^p 4 K_x = Nx/d^5, (-1)^p 4 K_y = Ny/d^5
            e = -1 if p % 2 else 1
            d = x - y
            s = 2 + x + y
            Nx = arb(M * (M + 1) * (M + 2)) / 3 * d ** 3 - (2 * M * M + (2 * M * M + 8 * M + 4) * x) * d ** 2 \
                + (6 * x * s - (8 * M + 6) * (1 - x * x)) * d + 8 * (1 - x * x) * s
            Ny = arb((M - 1) * M * (M + 1)) / 3 * d ** 3 + (y * (6 * M + 2) - 2 * (M + 1) ** 2 - 2 * M * (M + 1) * y) * d ** 2 \
                - (6 * y * s + (8 * M + 2) * (1 - y * y)) * d + 8 * (1 - y * y) * s
            if not (e * Nx / d ** 5 / 4).overlaps(Kx) or not (e * Ny / d ** 5 / 4).overlaps(Ky):
                closed_ok = False
    return {"n": n, "M": M, "signs_certified": ok, "closed_forms_overlap_defining_sums": closed_ok,
            "lam11": lam.str(25), "Dx": Dx.str(20), "Dy": Dy.str(20),
            "Dx_pos": bool(Dx > 0), "Dy_pos": bool(Dy > 0)}


def main():
    a = sys.argv
    mode = "full" if "--full" in a else "band"
    nmin = int(a[a.index("--nmin") + 1]) if "--nmin" in a else 2
    nmax = int(a[a.index("--nmax") + 1]) if "--nmax" in a else 400
    ctx.prec = int(a[a.index("--prec") + 1]) if "--prec" in a else 192
    out = a[a.index("--out") + 1] if "--out" in a else "/tmp/x2r3/fv_%s_%d_%d.json" % (mode, nmin, nmax)
    t0 = time.time()
    rows = []
    for n in range(nmin + (nmin % 2), nmax + 1, 2):
        rows.append(run_full(n) if mode == "full" else run_band(n))
    res = {"script": "code/mp/research/x2r3_first_variation_arb.py", "mode": mode, "prec_bits": ctx.prec,
           "range": [nmin, nmax], "count": len(rows),
           "all_signs_certified": all(r["signs_certified"] for r in rows),
           "all_Dx_pos": all(r["Dx_pos"] for r in rows), "all_Dy_pos": all(r["Dy_pos"] for r in rows),
           "wall_seconds": round(time.time() - t0, 1)}
    if mode == "band":
        res["min_Dx_over_M4_lower"] = min(r["Dx_over_M4_lower"] for r in rows)
        res["min_Dy_over_M4_lower"] = min(r["Dy_over_M4_lower"] for r in rows)
        res["all_band_Tx_positive"] = all(r["band_nodes_with_Tx_not_certified_positive"] == 0 for r in rows)
        res["Ty_nonpositive_only_at_(1,2)"] = all(r["band_nodes_(p,q)_with_Ty_not_certified_positive"] in ([], [(1, 2)]) for r in rows)
    else:
        res["all_closed_forms_overlap"] = all(r["closed_forms_overlap_defining_sums"] for r in rows)
    print(json.dumps(res, indent=1))
    sel = rows if len(rows) <= 12 else rows[:6] + rows[len(rows) // 2:len(rows) // 2 + 2] + rows[-4:]
    for r in sel:
        print(r)
    res["rows"] = rows
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"), indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
