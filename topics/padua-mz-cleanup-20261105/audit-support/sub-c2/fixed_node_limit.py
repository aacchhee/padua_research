#!/usr/bin/env python3
"""Auditor check (Claude subC2): fixed-node limit (1) of odd-weight-asymptotic.md,
  m^4 w_jk / log m -> -16 e_j e_k (-1)^j   (m odd),
using formula (3) evaluated in arb by the O(R) prefix-sum form
  S_R(t,s) = sum_a t_a cos(2a t) P_{R-a}(s),  P_n(s) = sum_{b<=n} t_b cos(2 b s).
Reports A(m)=m^4 w, A/log m and the discrete slope dA/dlog m between consecutive m."""
import sys
from flint import arb, fmpq, ctx
ctx.prec = 160

def t(a):
    return fmpq(2) if a == 0 else fmpq(-4, 4 * a * a - 1)

def weight(m, j, k):
    R = m // 2
    P = []
    acc = arb(0)
    for b in range(R + 1):
        acc += arb(t(b)) * arb.cos_pi_fmpq(fmpq(2 * b * k, m + 1))
        P.append(acc)
    S = arb(0)
    for a in range(R + 1):
        S += arb(t(a)) * arb.cos_pi_fmpq(fmpq(2 * a * j, m)) * P[R - a]
    hm = fmpq(0) if m % 2 else fmpq(2, 1 - m * m)
    S -= 2 * arb(hm) * arb.cos_pi_fmpq(fmpq(j, 1))
    e = fmpq(1, 2) if j in (0, m) else fmpq(1)
    g = fmpq(1, 2) if k in (0, m + 1) else fmpq(1)
    return arb(2 * e * g / (m * (m + 1))) * S

if __name__ == '__main__':
    ms = [int(x) for x in sys.argv[1:]] or [101, 1001, 10001, 100001]
    nodes = [(0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (3, 1), (1, 3), (3, 3), (4, 0), (5, 1), (0, 6)]
    for (j, k) in nodes:
        e = (0.5 if j == 0 else 1.0) * (0.5 if k == 0 else 1.0)
        pred = -16 * e * (-1) ** j
        prev = None
        line = []
        for m in ms:
            A = weight(m, j, k) * arb(m) ** 4
            lg = arb(m).log()
            s = f"m={m}: A/log m={float((A / lg).mid()):+.5f}"
            if prev is not None:
                slope = (A - prev[0]) / (lg - prev[1])
                s += f" slope={float(slope.mid()):+.5f}"
            line.append(s)
            prev = (A, lg)
        print(f"(j,k)=({j},{k}) predicted {pred:+.1f}: " + "; ".join(line), flush=True)
