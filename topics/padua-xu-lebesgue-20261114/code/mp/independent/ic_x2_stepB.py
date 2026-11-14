#!/usr/bin/env python3
"""Independent spot check (Opus 5.5 checker, 2026-11-14) of the node-wise sandwich (B6) of theory/X2-25 with the
explicit majorants (B2), (B5), and of the Step C block totals, using only the checker's own transcription:
   [-A]_+  from X2-23(a) directly;   c_M hhat(tau~)  with tau~ = eta r, mu = tau~ - j pi;
   e1 <= (2/M) sin mu cos^3 mu / tau~ * 1[tau~ < S* tan mu];
   L_c <= (2/M) sin^3 mu / (cos mu tau~) * 1[tau~ < tan mu];   L_s <= (4/M) sin mu cos mu / tau~ * 1[tau~ < tan mu].
Checks  c_M hhat - Lc_bd - Ls_bd <= [-A]_+ <= c_M hhat + e1_bd  at every node of N_+, and
sum e1_bd <= 2.012, sum Ls_bd <= 4.28, sum Lc_bd <= 0.2027 L^2 + 1.0864 L + 0.5505.  float64, MEASURED.
"""
import math, json, sys

def hhat(t):
    v = 4 * math.sin(t) ** 2 * math.cos(t) * (math.sin(t) - t * math.cos(t)) / t ** 3
    return max(v, 0.0)

out = {}
allok = True
for M in (4, 6, 8, 10, 20, 50, 100, 200, 400):
    N = M * (M + 1); eta = math.pi * (2 * M + 1) / (4 * N); cM = (M + 0.5) ** 3 / N
    Ss = (1 - (M + 0.5) ** -2) ** -0.5
    se = sl = sc = 0.0; ok = True; worst = 0.0
    for pp in range(1, M):
        for qq in range(1 + ((pp + 1) % 2), pp + 1, 2):       # q' <= p', same parity
            t = math.pi * pp / (2 * M); th = math.pi * qq / (2 * M + 2)
            X, Y = math.sin(t) ** 2, math.sin(th) ** 2
            r = pp * (M + 1) - qq * M; s = pp * (M + 1) + qq * M
            D = math.sin(math.pi * s / (2 * N)) * math.sin(math.pi * r / (2 * N))
            A = 16 * X * (1 - X) * Y * (1 - Y) * ((M - 0.5) * X - (M + 1.5) * Y) / (N * D ** 3)
            negA = max(-A, 0.0)
            tau = eta * r; j = (pp - qq) // 2; mu = tau - j * math.pi
            assert abs(mu - (t + th) / 2) < 1e-12
            main = cM * hhat(tau)
            e1 = (2 / M) * math.sin(mu) * math.cos(mu) ** 3 / tau * (tau < Ss * math.tan(mu))
            Lc = (2 / M) * math.sin(mu) ** 3 / (math.cos(mu) * tau) * (tau < math.tan(mu))
            Ls = (4 / M) * math.sin(mu) * math.cos(mu) / tau * (tau < math.tan(mu))
            se += e1; sl += Ls; sc += Lc
            tol = 1e-12 * (1 + main)
            if not (main - Lc - Ls - tol <= negA <= main + e1 + tol):
                ok = False
            worst = max(worst, negA - main - e1, main - Lc - Ls - negA)
    L = math.log(M)
    okC = se <= 2.012 and sl <= 4.28 and sc <= 0.2027 * L * L + 1.0864 * L + 0.5505
    allok &= ok and okC
    out[M] = {"B6_ok": ok, "max_violation(<=0 expected)": worst, "sum_e1_bd": round(se, 4), "sum_Ls_bd": round(sl, 4),
              "sum_Lc_bd": round(sc, 4), "Lc_bound": round(0.2027 * L * L + 1.0864 * L + 0.5505, 4), "C_ok": okC}
    print(M, out[M], flush=True)
print("all_ok", allok)
json.dump({"script": "code/mp/independent/ic_x2_stepB.py", "rows": out, "all_ok": allok},
          open(sys.argv[1] if len(sys.argv) > 1 else "/tmp/ic-x2/stepB.json", "w"), indent=1)
