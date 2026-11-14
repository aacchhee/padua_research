#!/usr/bin/env python3
"""Independent rigorous finite-range check (Opus 5.5 checker, 2026-11-14) for theory/X2-26 and X2-N30.

Own implementation of X2-23(a) in the ORIGINAL node indexing (p = m, q = 2k or 2k-1, p + q odd):
   A_{p,q} = 16 X(1-X) Y(1-Y) [ (M-1/2) X - (M+3/2) Y ] / ( N (X-Y)^3 ),  X = cos^2(p pi/(2M)), Y = cos^2(q pi/(2M+2)),
   lambda_n(1,1) = sum |A_{p,q}|.
X - Y = (x - y)/2 with x - y = cos w - cos v = -2 sin((w+v)/2) sin((w-v)/2),  (w +- v)/2 = pi (p(M+1) +- qM) / (2N),
so each factor is sin_pi of an exact rational (no cancellation, tight balls).
c* enters only through a rigorous enclosure passed on the command line (default: this checker's own
acb.integral enclosure from ic_x2_cstar.py, outward rounded).

Checks for even n <= NMAX:
  X2-26 :  lambda_n(1,1) - c* n^2 > 0                       (record claims computer-assisted part n <= 16)
  X2-N30:  lambda_n(1,1) < d_n for n = 2, 4;  > d_n for 6 <= n <= NMAX  (record: n <= 40)
  X2-24 :  lambda_n(1,1) > n + 1;  no term's ball contains 0 (X2-23 f);  sum A contains -(n+1) (X2-23 c)
  X2-25 :  R_n = lambda + (n+1) - c*(n+5/2)^2 in [-(0.4053 L^2 + 2.9833 L + 15.82), 7.66], L = log(n+2)
  thresholds of X2-26 / X2-N30: g(20) > 0, f(44) > 0, g(18) < 0, f(42) < 0, and the derivative values used.
Usage: python3 ic_x2_arb_finite.py [--nmax 60] [--extra 100,200,400,1000] [--out /tmp/ic-x2/arb_finite.json]
"""
import sys, json, time
import flint
from flint import arb, fmpq, ctx

CSTAR_LO, CSTAR_HI = "0.5169536533667", "0.5169536533670"   # own enclosure (ic_x2_cstar.py part 2), outward rounded


def lam11(n):
    M = n + 2; N = M * (M + 1)
    tot = arb(0); sgn = arb(0); zero_free = True; nneg = 0
    a1 = arb(M) - arb(1) / 2; a2 = arb(M) + arb(3) / 2
    for p in range(1, M):
        cx = arb.cos_pi_fmpq(fmpq(p, 2 * M)); X = cx * cx
        for q in range(1 + (p % 2), M + 1, 2):           # p + q odd
            cy = arb.cos_pi_fmpq(fmpq(q, 2 * M + 2)); Y = cy * cy
            u = p * (M + 1) + q * M; v = p * (M + 1) - q * M
            XmY = -arb.sin_pi_fmpq(fmpq(u, 2 * N)) * arb.sin_pi_fmpq(fmpq(v, 2 * N))   # = (x - y)/2
            A = 16 * X * (1 - X) * Y * (1 - Y) * (a1 * X - a2 * Y) / (N * XmY ** 3)
            if A.contains(0): zero_free = False
            if A < 0: nneg += 1
            tot += abs(A); sgn += A
    return tot, sgn, zero_free, nneg


def main():
    a = sys.argv[1:]
    nmax = int(a[a.index("--nmax") + 1]) if "--nmax" in a else 60
    extra = [int(s) for s in a[a.index("--extra") + 1].split(",")] if "--extra" in a else []
    out = a[a.index("--out") + 1] if "--out" in a else "/tmp/ic-x2/arb_finite.json"
    ctx.prec = 200
    cs = arb(CSTAR_LO).union(arb(CSTAR_HI))
    t0 = time.time()
    flags = {"X2-26_lam>c*n^2": True, "X2-N30_lt_dim_n2_4": True, "X2-N30_gt_dim_6..nmax": True,
             "X2-24_lam>n+1": True, "X2-23f_no_zero_term": True, "X2-23c_sumA_contains_-(n+1)": True,
             "X2-25_bracket": True}
    rows = []
    for n in list(range(2, nmax + 1, 2)) + extra:
        lam, sg, zf, nneg = lam11(n)
        M = n + 2; d = (n + 1) * (n + 2) // 2; L = arb(M).log()
        R = lam + (n + 1) - cs * (arb(2 * n + 5) / 2) ** 2
        lower = -(arb("0.4053") * L * L + arb("2.9833") * L + arb("15.82"))
        okb = bool(R > lower) and bool(R < arb("7.66"))
        if n <= nmax:
            flags["X2-26_lam>c*n^2"] &= bool(lam - cs * n * n > 0)
            if n in (2, 4): flags["X2-N30_lt_dim_n2_4"] &= bool(lam < d)
            else: flags["X2-N30_gt_dim_6..nmax"] &= bool(lam > d)
        flags["X2-24_lam>n+1"] &= bool(lam > n + 1)
        flags["X2-23f_no_zero_term"] &= zf
        flags["X2-23c_sumA_contains_-(n+1)"] &= bool(sg.contains(-(n + 1)))
        flags["X2-25_bracket"] &= okb
        row = {"n": n, "lam11": lam.str(25), "lam-dim": (lam - d).str(8), "lam-c*n^2": (lam - cs * n * n).str(8),
               "R_n": R.str(10), "lower": lower.str(6), "band_size": nneg}
        rows.append(row)
        print(json.dumps(row), flush=True)
    c = arb("0.51695")
    ell = lambda M: arb("0.4053") * arb(M).log() ** 2 + arb("2.9833") * arb(M).log() + arb("15.82")
    f = lambda M: (c - arb(1) / 2) * M * M + (c - arb(1) / 2) * M + c / 4 + 1 - ell(M)
    g = lambda M: (5 * c - 1) * M - arb(15) / 4 * c + 1 - ell(M)
    gp = lambda M: 5 * c - 1 - (arb("0.8106") * arb(M).log() + arb("2.9833")) / M
    fp = lambda M: 2 * (c - arb(1) / 2) * M + (c - arb(1) / 2) - (arb("0.8106") * arb(M).log() + arb("2.9833")) / M
    thr = {"g(18)": g(18).str(6), "g(20)": g(20).str(6), "g(20)>0": bool(g(20) > 0), "g'(20)": gp(20).str(6),
           "f(42)": f(42).str(6), "f(44)": f(44).str(6), "f(44)>0": bool(f(44) > 0), "f'(44)": fp(44).str(6)}
    # brute-force sanity of the analytic tails on a range (not a proof; the monotonicity is argued in the audit)
    thr["g>0_on_M=20..4000_even"] = all(bool(g(M) > 0) for M in range(20, 4001, 2))
    thr["f>0_on_M=44..4000_even"] = all(bool(f(M) > 0) for M in range(44, 4001, 2))
    res = {"script": "code/mp/independent/ic_x2_arb_finite.py", "python-flint": flint.__version__, "prec_bits": 200,
           "cstar_enclosure_used": [CSTAR_LO, CSTAR_HI], "nmax": nmax, "extra": extra, "flags": flags,
           "thresholds": thr, "rows": rows, "wall_s": round(time.time() - t0, 1)}
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1))


if __name__ == "__main__":
    main()
