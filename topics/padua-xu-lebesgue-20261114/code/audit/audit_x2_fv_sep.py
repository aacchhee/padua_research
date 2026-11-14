#!/usr/bin/env python3
"""Auditor's separate code path for X2-32 (audit-01, padua-xu-lebesgue-20261114).

Independent of the developer's closed forms N_x, N_y (X2-31 (a)) and of the closed form of
A_{p,q} (X2-23 (a)).  Everything here is computed from the DEFINING sums of the MP kernel,

    omega U_i(x_p) U_j(y_q) = (8/N) sin w sin v sin(a w) sin(b v),   a = i+1, b = j+1, a + b <= M,

with w = p pi/M, v = q pi/(M+1), N = M(M+1), M = n+2, in python-flint ball arithmetic
(sin(pi k/m) via arb.sin_pi_fmpq, tables indexed by k mod 2m; no three-term recurrence).

  l_a(1,1)      = (8/N) sw sv  sum_{a+b<=M} a b                 sin(aw) sin(bv)
  d_x l_a(1,1)  = (8/N) sw sv  sum_{a+b<=M} ((a-1)a(a+1)/3) b   sin(aw) sin(bv)   (U_i'(1) = i(i+1)(i+2)/3)
  d_y l_a(1,1)  = (8/N) sw sv  sum_{a+b<=M} a ((b-1)b(b+1)/3)   sin(aw) sin(bv)

Modes
  full : every node; the sign of l_a(1,1) is certified node by node from the defining sum and
         D_x = sum_a sgn(l_a(1,1)) d_x l_a(1,1), D_y likewise, directly (no band representation).
         Also lambda_n(1,1), lambda_n(1,-1), lambda_n(-1,-1) directly, and the band sizes.
  band : only the nodes with q >= p+1 (i.e. q' <= p', X > Y) are scanned, column by column
         (q = p+1, p+3, ...); a node is in the band iff (-1)^p l_a(1,1) < 0 (certified from the
         defining sum); the column scan stops at the first certified positive node and checks
         EXTRA further nodes for positivity (sanity only).  Nodes with q <= p-1 have A > 0 by the
         analytic sign rule X2-23 (b); nodes beyond the stop by the monotonicity in X2-32 (both
         developer results, used here only to bound the scan).  Then
            D_x = -n(n+1)(n+2)/3 + 2 sum_B T_a,  D_y = 2 sum_B T'_a  (X2-31 (c)),
         with T_a = -(-1)^p d_x l_a(1,1), T'_a = -(-1)^p d_y l_a(1,1) from the defining sums.

Usage: python3 audit_x2_fv_sep.py --mode full|band --ns 2,4,6 [--prec 192] [--extra 1] --out FILE
"""
import sys, json, time
from flint import arb, fmpq, ctx


def tables(M):
    Sw = [arb.sin_pi_fmpq(fmpq(k, M)) for k in range(2 * M)]          # sin(k pi / M)
    Sv = [arb.sin_pi_fmpq(fmpq(k, M + 1)) for k in range(2 * M + 2)]  # sin(k pi /(M+1))
    return Sw, Sv


def prefix_q(M, q, Sv):
    """P1[k] = sum_{b<=k} b sin(b v_q), P3[k] = sum_{b<=k} ((b-1)b(b+1)/3) sin(b v_q), k = 0..M-1."""
    m2 = 2 * M + 2
    P1 = [arb(0)] * M
    P3 = [arb(0)] * M
    s1 = arb(0); s3 = arb(0)
    for b in range(1, M):
        t = Sv[(b * q) % m2]
        s1 = s1 + b * t
        s3 = s3 + ((b - 1) * b * (b + 1) // 3) * t
        P1[b] = s1
        P3[b] = s3
    return P1, P3


def node_sums(M, p, q, Sw, P1, P3):
    m2 = 2 * M
    S0 = arb(0); Sx = arb(0); Sy = arb(0)
    for a in range(1, M):
        sa = Sw[(a * p) % m2]
        t1 = sa * P1[M - a]
        S0 += a * t1
        Sx += ((a - 1) * a * (a + 1) // 3) * t1
        Sy += a * (sa * P3[M - a])
    return S0, Sx, Sy


def run_full(n):
    M = n + 2; N = M * (M + 1)
    Sw, Sv = tables(M)
    pref = {q: prefix_q(M, q, Sv) for q in range(1, M + 1)}
    lam11 = arb(0); lam1m = arb(0); lammm = arb(0)
    Dx = arb(0); Dy = arb(0)
    ok = True; band = 0
    for p in range(1, M):
        for q in range(1, M + 1):
            if (p + q) % 2 == 0:
                continue
            P1, P3 = pref[q]
            S0, Sx, Sy = node_sums(M, p, q, Sw, P1, P3)
            pre = 8 * Sw[p] * Sv[q] / N
            l11 = pre * S0; lx = pre * Sx; ly = pre * Sy
            if l11 > 0:
                sg = 1
            elif l11 < 0:
                sg = -1
            else:
                ok = False; sg = 0
            e = -1 if p % 2 else 1
            if sg == -e:
                band += 1
            lam11 += sg * l11
            Dx += sg * lx
            Dy += sg * ly
            # lower vertices from the defining sums: U_i(-1) = (-1)^i (i+1), so sin factors pick up signs
            # l_a(1,-1) = (8/N) sw sv sum a b (-1)^(b-1) sin(aw) sin(bv); l_a(-1,-1): (-1)^(a+b)
            s1m = arb(0); smm = arb(0)
            for a in (range(1, M) if n <= 30 else []):
                sa = Sw[(a * p) % (2 * M)]
                for b in range(1, M - a + 1):
                    t = a * b * sa * Sv[(b * q) % (2 * M + 2)]
                    s1m += t if b % 2 == 1 else -t
                    smm += t if (a + b) % 2 == 0 else -t
            lam1m += abs(pre * s1m)
            lammm += abs(pre * smm)
    return {"n": n, "mode": "full", "signs_certified": ok, "band_size_from_signs": band,
            "lam11": lam11.str(22), "lam1m": lam1m.str(22), "lammm": lammm.str(22),
            "lam1m_contains_n+1": bool(lam1m.overlaps(arb(n + 1))) if n <= 30 else None,
            "lammm_contains_n+1": bool(lammm.overlaps(arb(n + 1))) if n <= 30 else None,
            "Dx": Dx.str(18), "Dy": Dy.str(18), "Dx_pos": bool(Dx > 0), "Dy_pos": bool(Dy > 0)}


def run_band(n, extra=1):
    M = n + 2; N = M * (M + 1)
    Sw, Sv = tables(M)
    cache = {}
    sumA = arb(0); sTx = arb(0); sTy = arb(0)
    ok = True; band = 0; extra_ok = True; Ty_nonpos = []
    for p in range(1, M):
        e = -1 if p % 2 else 1
        q = p + 1
        stopped = False; extra_left = extra
        while q <= M:
            if q not in cache:
                cache[q] = prefix_q(M, q, Sv)
            P1, P3 = cache[q]
            S0, Sx, Sy = node_sums(M, p, q, Sw, P1, P3)
            pre = 8 * Sw[p] * Sv[q] / N
            A = e * pre * S0
            if not stopped:
                if A < 0:
                    band += 1
                    sumA += -A
                    Tx = -e * pre * Sx; Ty = -e * pre * Sy
                    sTx += Tx; sTy += Ty
                    if not (Ty > 0):
                        Ty_nonpos.append((p, q))
                elif A > 0:
                    stopped = True
                else:
                    ok = False; break
            else:
                if not (A > 0):
                    extra_ok = False
                extra_left -= 1
                if extra_left <= 0:
                    break
            q += 2
    Dx = 2 * sTx - arb(n * (n + 1) * (n + 2)) / 3
    Dy = 2 * sTy
    lam = 2 * sumA - (n + 1)
    M4 = arb(M) ** 4
    return {"n": n, "mode": "band", "band_size": band, "signs_certified": ok, "extra_nodes_positive": extra_ok,
            "lam11": lam.str(22), "Dx": Dx.str(18), "Dy": Dy.str(18),
            "Dx_over_M4": (Dx / M4).str(10), "Dy_over_M4": (Dy / M4).str(10),
            "Dx_pos": bool(Dx > 0), "Dy_pos": bool(Dy > 0), "band_nodes_Ty_not_pos": Ty_nonpos[:4]}


def main():
    a = sys.argv
    mode = a[a.index("--mode") + 1]
    ns = [int(t) for t in a[a.index("--ns") + 1].split(",")]
    ctx.prec = int(a[a.index("--prec") + 1]) if "--prec" in a else 192
    extra = int(a[a.index("--extra") + 1]) if "--extra" in a else 1
    out = a[a.index("--out") + 1]
    rows = []
    t0 = time.time()
    for n in ns:
        t = time.time()
        r = run_full(n) if mode == "full" else run_band(n, extra)
        r["seconds"] = round(time.time() - t, 1)
        rows.append(r)
        print(json.dumps(r), flush=True)
    res = {"script": "code/audit/audit_x2_fv_sep.py", "mode": mode, "prec": ctx.prec, "ns": ns,
           "all_signs_certified": all(r["signs_certified"] for r in rows),
           "all_Dx_pos": all(r["Dx_pos"] for r in rows), "all_Dy_pos": all(r["Dy_pos"] for r in rows),
           "wall_seconds": round(time.time() - t0, 1), "rows": rows}
    json.dump(res, open(out, "w"), indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
