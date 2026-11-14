#!/usr/bin/env python3
"""X2 round 2: rigorous ball-arithmetic (python-flint arb) enclosures used by theory/X2-25, X2-26, X2-N30 (record IDs renamed 2026-11-14: former X2-N31/N32 drafts).

What is enclosed (all formulas are PROVED in the theory records; this script only evaluates them):
  (1) lambda_n(1,1) for even n <= NMAX from the closed form of theory/X2-23 (statement part (c)):
        lambda_n(1,1) = (16/N) * sum over nodes of  X(1-X)Y(1-Y) |(M-1/2)X - (M+3/2)Y| / |X-Y|^3,
        M = n+2, N = M(M+1), X = sin^2(pi p'/(2M)), Y = sin^2(pi q'/(2M+2)), 1<=p'<=M-1, 1<=q'<=M, p' = q' mod 2,
        with X - Y = sin(pi s/(2N)) sin(pi r/(2N)), r = p'(M+1) - q'M, s = p'(M+1) + q'M  (no cancellation).
  (2) c* = (4/pi) sum_{j>=0} [Phi(a_j) - Phi(b_j)]  (theory/X2-25, Lemma C) with the proved tail bound
        0 <= tail_J <= 2/(pi^6 J^4);  a_j = root of tan t = t in (j pi, j pi + pi/2), enclosed by a certified sign change.
  (3) the finite-range inequalities quoted in the records:
        lambda_n(1,1) > n+1 (all n <= NMAX);  lambda_n(1,1) < dim for n = 2, 4;  > dim for 6 <= n <= NMAX;
        lambda_n(1,1) > c* n^2  (all n <= NMAX);  the two-sided bound of X2-25 (all n <= NMAX);
        the threshold evaluations f(44) > 0, g(20) > 0 used for the analytic ranges.
Usage:  python3 x2_corner_arb.py [--nmax 60] [--prec 256] [--out /tmp/x2r2/x2_corner_arb.json]
"""
import sys, json, time, os, platform
import flint
from flint import arb, fmpq, ctx


def lam11_arb(n):
    M = n + 2; N = M * (M + 1)
    half = arb(1) / 2
    tot = arb(0); signed = arb(0); nzero_excluded = True; nband = 0
    for pp in range(1, M):
        sx = arb.sin_pi_fmpq(fmpq(pp, 2 * M)); X = sx * sx
        for qq in range(1 + (pp + 1) % 2, M + 1, 2):          # q' = p' (mod 2)
            sy = arb.sin_pi_fmpq(fmpq(qq, 2 * M + 2)); Y = sy * sy
            r = pp * (M + 1) - qq * M; s = pp * (M + 1) + qq * M
            D = arb.sin_pi_fmpq(fmpq(s, 2 * N)) * arb.sin_pi_fmpq(fmpq(r, 2 * N))      # X - Y
            A = 16 * X * (1 - X) * Y * (1 - Y) * ((M - half) * X - (M + 3 * half) * Y) / (N * D ** 3)
            if A.contains(0):
                nzero_excluded = False
            if A < 0:
                nband += 1
            tot += abs(A); signed += A
    return tot, signed, nzero_excluded, nband


def Phi(t):
    s, c = t.sin_cos()
    s2, c2 = (2 * t).sin_cos()
    return s2 * s * s / (t * t) + 2 * c2 * s * s / t + 2 * (2 * t).si() - 2 * (4 * t).si()


def root_a(j):
    """ball containing the unique root of f(t) = sin t - t cos t in (j pi, j pi + pi/2), j >= 1 (certified sign change)."""
    f = lambda t: t.sin() - t * t.cos()
    pi = arb.pi()
    x = j * pi + pi / 2 - 1 / (j * pi + pi / 2)
    for _ in range(60):                       # Newton on midpoints: f' = t sin t
        xm = arb(x.mid())
        x = xm - f(xm) / (xm * xm.sin())
    xm = arb(x.mid())
    rad = arb(2) ** (-(ctx.prec - 40))
    lo, hi = xm - rad, xm + rad
    flo, fhi = f(lo), f(hi)
    # on (j pi, j pi + pi/2): f' = t sin t has the sign (-1)^j, so f is strictly monotone there
    ok = (flo * fhi < 0) and (lo > j * pi) and (hi < j * pi + pi / 2)
    return lo.union(hi), bool(ok)


def cstar_arb(J):
    pi = arb.pi()
    tot = -Phi(pi / 2)
    allok = True
    for j in range(1, J + 1):
        a, ok = root_a(j)
        allok &= ok
        tot += Phi(a) - Phi(j * pi + pi / 2)
    lo = 4 / pi * tot
    tail = 2 / (pi ** 6 * arb(J) ** 4)
    return lo, lo + tail, allok          # c* in [lo, lo + tail]


def main():
    nmax, prec, out = 60, 256, "/tmp/x2r2/x2_corner_arb.json"
    a = sys.argv[1:]
    if "--nmax" in a: nmax = int(a[a.index("--nmax") + 1])
    if "--prec" in a: prec = int(a[a.index("--prec") + 1])
    if "--out" in a: out = a[a.index("--out") + 1]
    ctx.prec = prec
    t0 = time.time()
    c_lo, c_hi, roots_ok = cstar_arb(200)
    cs = c_lo.union(c_hi)                 # ball containing c*
    res = {"script": "code/mp/research/x2_corner_arb.py", "command": "python3 " + " ".join(sys.argv),
           "versions": {"python": platform.python_version(), "python-flint": flint.__version__}, "prec_bits": prec,
           "cstar_enclosure_J200": [c_lo.str(40, radius=False), c_hi.str(40, radius=False)],
           "cstar_width": (c_hi - c_lo).str(5, radius=False), "roots_certified": roots_ok,
           "cstar_ge_0.51695": bool(cs > arb("0.51695")), "cstar_le_0.51696": bool(cs < arb("0.51696"))}
    print("c* in [%s, %s]  roots_certified=%s" % (c_lo.str(30, radius=False), c_hi.str(30, radius=False), roots_ok), flush=True)
    rows = []
    flags = {"gt_n+1": True, "lt_dim_n2_n4": True, "gt_dim_n>=6": True, "gt_cstar_n^2": True, "two_sided_X2-25": True,
             "signed_sum_contains_-(n+1)": True, "no_term_contains_0": True}
    for n in range(2, nmax + 1, 2):
        lam, signed, nz, nband = lam11_arb(n)
        M = n + 2; dim = (n + 1) * (n + 2) // 2
        L = arb(M).log()
        R = lam + (n + 1) - cs * (arb(2 * n + 5) / 2) ** 2
        lower = -(arb("0.4053") * L * L + arb("2.9833") * L + arb("15.82")); upper = arb("7.66")
        flags["gt_n+1"] &= bool(lam > n + 1)
        if n in (2, 4): flags["lt_dim_n2_n4"] &= bool(lam < dim)
        else: flags["gt_dim_n>=6"] &= bool(lam > dim)
        flags["gt_cstar_n^2"] &= bool(lam > cs * n * n)
        flags["two_sided_X2-25"] &= bool(R > lower) and bool(R < upper)
        flags["signed_sum_contains_-(n+1)"] &= bool(signed.contains(-(n + 1)))
        flags["no_term_contains_0"] &= nz
        rows.append({"n": n, "lam11": lam.str(30), "lam11-dim": (lam - dim).str(8), "R_n": R.str(8), "n_band": nband})
        if n <= 12 or n % 10 == 0:
            print(" n=%3d lam11=%s  lam-dim=%s  R_n=%s  band=%d" % (n, lam.str(28), (lam - dim).str(8), R.str(8), nband), flush=True)
    # threshold evaluations for the analytic ranges (c* >= 0.51695 is certified above)
    c = arb("0.51695"); ell = lambda M: arb("0.4053") * arb(M).log() ** 2 + arb("2.9833") * arb(M).log() + arb("15.82")
    f = lambda M: (c - arb(1) / 2) * M * M + (c - arb(1) / 2) * M + c / 4 + 1 - ell(M)      # lam > dim  for M >= 44
    g = lambda M: (5 * c - 1) * M - arb("3.75") * c + 1 - ell(M)                              # lam > c n^2 (c = 0.51695..c*) -- see X2-26
    # for the c* n^2 statement the worst case over c in [0.51695, 0.51696] of (5c-1)M - 3.75c + 1 is at c = 0.51695 (M >= 1)
    res["threshold_f(44)>0"] = bool(f(44) > 0); res["threshold_f(42)"] = f(42).str(6)
    res["threshold_g(20)>0"] = bool(g(20) > 0); res["threshold_g(18)"] = g(18).str(6)
    res["flags_all_even_n_le_%d" % nmax] = flags
    res["rows"] = rows
    res["wall_seconds"] = round(time.time() - t0, 1)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    main()
