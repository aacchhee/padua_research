#!/usr/bin/env python3
"""X2 round 2, T5 support (MEASURED only): four-term kernel formula and the conjectured corner scaling limits.

  (a) checks the exact four-term formula for l_{m,k}(cos th1, cos th2) (theory/X2-28, Lemma K) against the kernel sum (mpmath);
  (b) compares lambda_n(cos(xi/M), +-cos(ze/M)) / M^2, M = n+2, with the conjectured limits
        L_top(xi,ze) = (2/pi) int_0^inf |K_top| dtau,
        K_top = 2 sin^2(tau) cos(tau) [cos(a)(sinc(tau+b)+sinc(tau-b)) - cos(b)(sinc(tau+a)+sinc(tau-a))]/(a^2-b^2),
        L_bot(xi,ze) = (1/pi) int_R |K_bot| dtau,
        K_bot = 2 sin(tau) cos^2(tau) [sin(a)(sinc(tau+b)-sinc(tau-b)) - sin(b)(sinc(tau+a)-sinc(tau-a))]/(a^2-b^2),
      a = (xi+ze)/2, b = (xi-ze)/2  (heuristic derivation in theory/X2-28; NOT proved);
  (c) scans L_top and L_bot on a grid (quadrature: midpoint rule, step h, truncated at T; truncation error ~ O(1/T)).
Usage: python3 x2_corner_scaling_limits.py [--out /tmp/x2r2/x2_scaling.json]
"""
import sys, json, os, time
import numpy as np
import mpmath as mp

CSTAR = 0.516953653366806


def lam_angles(n, th1, th2):
    """lambda_n(cos th1, cos th2) from the four-term formula (float64)."""
    M = n + 2; N = M * (M + 1)
    p = np.arange(1, M)[:, None]; q = np.arange(1, M + 1)[None, :]
    mask = ((p + q) % 2 == 1)
    w = np.pi * p / M * np.ones_like(q); v = np.pi * q / (M + 1) * np.ones_like(p)
    tot = np.zeros(w.shape)
    for s1 in (1, -1):
        for s2 in (1, -1):
            num = np.cos((M + 1) * th1 - s1 * w) + np.cos(M * th1) + np.cos((M + 1) * th2) + np.cos(M * th2 + s2 * v)
            den = np.cos(th1 - s1 * w) - np.cos(th2 - s2 * v)
            tot += s1 * s2 * num / den
    val = np.sin(w) * np.sin(v) / (2 * N * np.sin(th1) * np.sin(th2)) * tot
    return float(np.abs(val[mask]).sum())


sinc = lambda x: np.sinc(x / np.pi)


def Ltop(xi, ze, T=600.0, h=0.004):
    tau = np.arange(h / 2, T, h)
    a = (xi + ze) / 2; b = (xi - ze) / 2
    G = np.cos(a) * (sinc(tau + b) + sinc(tau - b)) - np.cos(b) * (sinc(tau + a) + sinc(tau - a))
    return float(2 / np.pi * np.sum(np.abs(2 * np.sin(tau) ** 2 * np.cos(tau) * G / (a * a - b * b))) * h)


def Lbot(xi, ze, T=600.0, h=0.004):
    tau = np.arange(-T + h / 2, T, h)
    a = (xi + ze) / 2; b = (xi - ze) / 2
    G = np.sin(a) * (sinc(tau + b) - sinc(tau - b)) - np.sin(b) * (sinc(tau + a) - sinc(tau - a))
    return float(1 / np.pi * np.sum(np.abs(2 * np.sin(tau) * np.cos(tau) ** 2 * G / (a * a - b * b))) * h)


def main():
    out = "/tmp/x2r2/x2_scaling.json"
    if "--out" in sys.argv: out = sys.argv[sys.argv.index("--out") + 1]
    t0 = time.time(); res = {"script": "code/mp/research/x2_corner_scaling_limits.py", "label": "MEASURED; the limit formulas are conjectural"}
    # (a)
    mp.mp.dps = 30
    def U_list(x, n):
        u = [mp.mpf(1), 2 * x]
        for i in range(2, n + 1): u.append(2 * x * u[-1] - u[-2])
        return u[:n + 1]
    err = mp.mpf(0)
    for n in (2, 4, 6):
        M = n + 2; N = M * (M + 1)
        for m in range(1, n + 2):
            for k in range(1, n // 2 + 2):
                q = 2 * k if m % 2 else 2 * k - 1
                w = mp.pi * m / M; v = mp.pi * q / (M + 1)
                for (t1, t2) in ((0.3, 1.1), (2.0, 0.7), (1.234, 2.9)):
                    t1 = mp.mpf(t1); t2 = mp.mpf(t2)
                    a, b, c, d = U_list(mp.cos(t1), n), U_list(mp.cos(t2), n), U_list(mp.cos(w), n), U_list(mp.cos(v), n)
                    direct = 8 * mp.sin(w) ** 2 * mp.sin(v) ** 2 / N * mp.fsum(a[i] * c[i] * b[j] * d[j] for i in range(n + 1) for j in range(n + 1 - i))
                    tot = 0
                    for s1 in (1, -1):
                        for s2 in (1, -1):
                            tot += s1 * s2 * (mp.cos((M + 1) * t1 - s1 * w) + mp.cos(M * t1) + mp.cos((M + 1) * t2) + mp.cos(M * t2 + s2 * v)) / (mp.cos(t1 - s1 * w) - mp.cos(t2 - s2 * v))
                    four = (-1) ** m * mp.sin(w) * mp.sin(v) / (2 * N * mp.sin(t1) * mp.sin(t2)) * tot
                    err = max(err, abs(direct - four))
    res["four_term_formula_max_err"] = mp.nstr(err, 5)
    print("(a) four-term formula max err", res["four_term_formula_max_err"])
    # (b)
    rows = []
    for (xi, ze) in ((0.5, 0.5), (1.0, 0.3), (2.0, 2.0), (3.0, 0.01), (5.0, 5.0), (8.0, 1.0), (12.0, 0.01)):
        vals = [lam_angles(n, xi / (n + 2), ze / (n + 2)) / (n + 2) ** 2 for n in (100, 400)]
        rows.append({"corner": "top", "xi": xi, "ze": ze, "lam/M^2_n100": vals[0], "lam/M^2_n400": vals[1], "L": Ltop(xi, ze)})
    for (xi, ze) in ((0.01, 5.0), (5.0, 0.01), (3.0, 3.0), (2.0, 4.0), (0.01, 8.0)):
        vals = [lam_angles(n, xi / (n + 2), np.pi - ze / (n + 2)) / (n + 2) ** 2 for n in (100, 400)]
        rows.append({"corner": "bottom", "xi": xi, "ze": ze, "lam/M^2_n100": vals[0], "lam/M^2_n400": vals[1], "L": Lbot(xi, ze)})
    for r in rows: print("(b)", r)
    res["comparison"] = rows
    # (c)
    g = np.arange(0.25, 12.01, 0.5)
    top = np.array([[Ltop(x, z, T=200.0, h=0.01) if x >= z else np.nan for z in g] for x in g])   # symmetric in (xi,ze)
    i, j = np.unravel_index(np.nanargmax(top), top.shape)
    res["Ltop_grid_max"] = {"xi": float(g[i]), "ze": float(g[j]), "value": float(top[i, j]), "cstar": CSTAR,
                            "Ltop(0.01,0.011)": Ltop(0.01, 0.011, T=200.0, h=0.01)}
    res["Ltop_on_grid_decreasing_in_xi_for_fixed_ze"] = bool(all(np.all(np.diff(top[k:, k]) < 1e-9) for k in range(len(g) - 1)))
    res["Ltop_edge_ze0.01"] = [[float(x), Ltop(x, 0.01, T=200.0, h=0.01)] for x in (0.5, 1, 2, 4, 8, 16, 32)]
    bot_edge = [[float(z), Lbot(0.01, z, T=200.0, h=0.01)] for z in np.arange(0.5, 14.01, 0.5)]
    k = int(np.argmax([b[1] for b in bot_edge]))
    res["Lbot_edge_max"] = {"ze": bot_edge[k][0], "value": bot_edge[k][1], "ratio_to_cstar": bot_edge[k][1] / CSTAR}
    bot = np.array([[Lbot(x, z, T=200.0, h=0.01) for z in g] for x in g])
    i, j = np.unravel_index(np.argmax(bot), bot.shape)
    res["Lbot_grid_max"] = {"xi": float(g[i]), "ze": float(g[j]), "value": float(bot[i, j])}
    res["wall_seconds"] = round(time.time() - t0, 1)
    print(json.dumps({k: v for k, v in res.items() if k != "comparison"}, indent=1))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"), indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
