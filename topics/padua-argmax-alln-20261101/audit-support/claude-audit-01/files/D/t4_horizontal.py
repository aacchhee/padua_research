"""(c) theory16 identity F^h_jr(s) = -F_jr(s,0) termwise on the periodic odd board, both parities,
random s including collision-producing s; S^h(s)=S_n(s,0); S^h(0)=Lambda_c; and the codex-05
horizontal decomposition lambda_n(cos theta, eps) = S^h(s) - Delta^h >= ... with Delta^h>=0,
at complementary centers on both edges (independent implementation; MEASURED float64).
Also measures max_s (S_n(s,0)-cos^2(s/2)Lambda_c)/log(n+1) on |s|<=pi (the C of (4)).
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from padlib import *

rng = np.random.default_rng(20261103)
out = []
for n in [2, 3, 4, 5, 6, 7, 11, 12, 20, 21, 40, 41]:
    m = n + 1; N = n * m
    J, R = np.meshgrid(np.arange(2 * n), np.arange(2 * m), indexing="ij")
    J = J.ravel(); R = R.ravel(); sel = (J + R) % 2 == 1; J = J[sel]; R = R[sel]
    sj = np.where(J % 2 == 0, 1.0, -1.0); sr = np.where(R % 2 == 0, 1.0, -1.0)

    def F(al, be):
        return sj / 2 * (Rn(n, J * PI / n + al / n, R * PI / m + be / m) - np.cos(J * PI + al))

    def Fh(s):
        return (sr * Rn(n, J * PI / n + s / n, R * PI / m) + np.cos(s)) / 2

    svals = list(rng.uniform(-PI, PI, 30)) + list(rng.uniform(-20, 20, 10))
    # collision-producing s: j pi/n + s/n = r pi/m  ->  s = pi (n r/m - j)
    for _ in range(10):
        jj = rng.integers(0, 2 * n); rr = rng.integers(0, 2 * m)
        svals.append(PI * (n * rr / m - jj))
    svals.append(0.0)
    worst = 0.0; worstS = 0.0
    for s in svals:
        a = Fh(s); b = -F(s, 0.0)
        worst = max(worst, float(np.abs(a - b).max()))
        worstS = max(worstS, abs(np.abs(a).sum() / N - np.abs(F(s, 0.0)).sum() / N))
    Lc = corner_value(n)
    Sh0 = np.abs(Fh(0.0)).sum() / N
    # horizontal decomposition at complementary centers xi=q pi/n, q+m*l odd, theta=xi+s/n
    Jn, Kn, aj, bk, w = nodes(n)
    dec_err = 0.0; minDelta = np.inf
    for l in (0, 1):
        eps = (-1) ** l
        bprime = np.arccos(np.clip(eps * np.cos(bk), -1, 1))
        kap = np.where((Kn + m * l) % 2 == 0, 1.0, -1.0)
        for q in range(0, n + 1):
            if (q + m * l) % 2 == 0:
                continue
            for s in rng.uniform(-PI, PI, 3):
                th = q * PI / n + s / n
                if not (0 <= th <= PI):
                    continue
                Hp = (kap * Rn(n, th + aj, bprime) + np.cos(s)) / 2
                Hm = (kap * Rn(n, th - aj, bprime) + np.cos(s)) / 2
                Delta = (w * (np.abs(Hp) + np.abs(Hm) - np.abs(Hp + Hm))).sum()
                lam_direct = lebesgue(n, [th], [0.0 if l == 0 else PI])[0]
                Sh = np.abs(Fh(s)).sum() / N
                dec_err = max(dec_err, abs(lam_direct - (Sh - Delta)))
                minDelta = min(minDelta, Delta)
    ss = np.linspace(-PI, PI, 2001)
    Cmax = max((np.abs(F(s, 0.0)).sum() / N - np.cos(s / 2) ** 2 * Lc) / np.log(n + 1) for s in ss)
    rec = {"n": n, "parity": n % 2, "max|Fh+F(s,0)|": worst, "max|Sh-S(s,0)|": worstS,
           "|Sh(0)-Lc|": abs(Sh0 - Lc), "max|lambda-(Sh-Delta)|": dec_err, "min Delta^h": float(minDelta),
           "max_s (S(s,0)-cos^2(s/2)Lc)/log(n+1)": float(Cmax), "n_s_tested": len(svals)}
    out.append(rec)
    print(rec, flush=True)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "t4_horizontal.json"), "w"), indent=1)
