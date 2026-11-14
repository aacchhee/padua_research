#!/usr/bin/env python3
"""MEASURED checks of the 1-D statements of theory/X1-02 and X1-06.
(a) X1-06 exact series: L_n = A_n + (4/pi) sum_{j>=1} (-1)^{j-1} G(n j), G(x) = psi(x+1/2) - log x
    (alternating series summed in pairs with an Euler-Maclaurin-free tail bound: partial sums bracket the limit);
(b) X1-06 enclosure: A_n + pi/(72 n^2) - 7/(240 pi n^4) < L_n < A_n + pi/(72 n^2) for n = 1..nmax;
(c) kernel inequalities 0 <= t/24 - phi0(t) <= 7 t^3/5760, phi0(t) = 1/t - 1/(2 sinh(t/2)), on a grid, and
    G(x) = int_0^inf e^{-xt} phi0(t) dt against psi(x+1/2) - log x for a few x;
(d) X1-02: omega_n(u) on [0, pi/(2n)] (odd class) equals P(cos u) = sum_k (-1)^{k-1} l_k(cos u) (Chebyshev-zero
    Lagrange polynomials), is decreasing in u there, omega_n(0) = L_n, omega_n(node) = 1, and omega_n is pi/n-periodic.
Usage: python3 code/xu/research/x1_1d_check.py [--nmax 2000] [--dps 40] [--out /tmp/x1r2/1d_check.json]
"""
import sys, os, json, argparse
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import x1_lift as X


def G(x):
    return mp.digamma(x + mp.mpf(1) / 2) - mp.log(x)


def series_bracket(n, J):
    """partial sums S_{2J} < S < S_{2J+1} of sum (-1)^{j-1} G(nj) (G positive decreasing)."""
    s = mp.fsum((-1) ** (j - 1) * G(n * j) for j in range(1, 2 * J + 1))
    return s, s + G(n * (2 * J + 1))


def omega_oddclass(n, u):
    return mp.fsum(abs(X.dker(n, u - mp.pi * p / (2 * n))) for p in range(1, 4 * n, 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=2000); ap.add_argument("--dps", type=int, default=40)
    ap.add_argument("--out", default="/tmp/x1r2/1d_check.json")
    a = ap.parse_args()
    mp.mp.dps = a.dps
    out = {}
    # (a)
    worst = mp.mpf(0)
    for n in list(range(1, 13)) + [20, 50, 101]:
        lo, hi = series_bracket(n, 4000)
        L = X.Lcheb(n); An = X.A(n)
        target = (L - An) * mp.pi / 4
        assert lo < target < hi, (n, lo, target, hi)
        worst = max(worst, hi - lo)
    out["a_series_bracket_ok"] = True; out["a_bracket_width_max"] = mp.nstr(worst, 5)
    print("(a) exact series brackets (L_n - A_n) pi/4 for n in 1..12,20,50,101; max bracket width", mp.nstr(worst, 5))
    # (b)
    minlo = None; minhi = None
    ns = list(range(1, min(a.nmax, 400) + 1)) + list(range(400, a.nmax + 1, 37))
    for n in ns:
        L = X.Lcheb(n); An = X.A(n)
        up = An + mp.pi / (72 * mp.mpf(n) ** 2); lo = up - 7 / (240 * mp.pi * mp.mpf(n) ** 4)
        assert lo < L < up, n
        r = (up - L) * mp.mpf(n) ** 4      # should lie in (0, 7/(240 pi)) ; limit 49 pi^3/172800
        minlo = r if minlo is None else min(minlo, r); minhi = r if minhi is None else max(minhi, r)
    out["b_enclosure_ok_n"] = [ns[0], ns[-1], len(ns)]
    out["b_n4_times_gap_range"] = [mp.nstr(minlo, 12), mp.nstr(minhi, 12)]
    print("(b) enclosure holds for %d values n in [1,%d]; n^4 (A_n + pi/(72n^2) - L_n) in [%s, %s]; 7/(240 pi) = %s; 49 pi^3/172800 = %s"
          % (len(ns), ns[-1], mp.nstr(minlo, 10), mp.nstr(minhi, 10), mp.nstr(7 / (240 * mp.pi), 10), mp.nstr(49 * mp.pi ** 3 / 172800, 10)))
    # (c)
    phi0 = lambda t: 1 / t - 1 / (2 * mp.sinh(t / 2))
    bad = 0
    for k in range(1, 4001):
        t = mp.mpf(k) / 100
        dlt = t / 24 - phi0(t)
        bad += not (0 < dlt < 7 * t ** 3 / 5760)
    gdev = mp.mpf(0)
    for x in (1, 2, 3.5, 10, 64):
        val = mp.quad(lambda t: mp.exp(-x * t) * phi0(t), [0, 1, 10, mp.inf])
        gdev = max(gdev, abs(val - G(mp.mpf(x))))
    out["c_kernel_ineq_failures"] = bad; out["c_G_integral_dev"] = mp.nstr(gdev, 5)
    print("(c) kernel inequality failures on t=0.01..40:", bad, "| max |int - (psi(x+1/2)-log x)|:", mp.nstr(gdev, 5))
    assert bad == 0
    # (d)
    dfail = 0; dev = mp.mpf(0)
    for n in range(2, 13):
        tz = [mp.cos((2 * k - 1) * mp.pi / (2 * n)) for k in range(1, n + 1)]
        def P(t):
            tot = mp.mpf(0)
            for k in range(n):
                num = mp.mpf(1); den = mp.mpf(1)
                for m in range(n):
                    if m != k:
                        num *= (t - tz[m]); den *= (tz[k] - tz[m])
                tot += (-1) ** k * num / den
            return tot
        prev = None
        for s in range(0, 21):
            u = mp.pi / (2 * n) * s / 20
            w = omega_oddclass(n, u)
            dev = max(dev, abs(w - P(mp.cos(u))), abs(w - omega_oddclass(n, u + mp.pi / n)))
            if prev is not None and not (w < prev):
                dfail += 1
            prev = w
        dev = max(dev, abs(omega_oddclass(n, mp.mpf(0)) - X.Lcheb(n)), abs(omega_oddclass(n, mp.pi / (2 * n)) - 1))
    out["d_monotonicity_failures"] = dfail; out["d_max_dev"] = mp.nstr(dev, 5)
    print("(d) omega = P(cos u), periodicity, endpoint values: max dev", mp.nstr(dev, 5), "| monotonicity failures:", dfail)
    assert dfail == 0
    json.dump(out, open(a.out, "w"), indent=0)


if __name__ == "__main__":
    main()
