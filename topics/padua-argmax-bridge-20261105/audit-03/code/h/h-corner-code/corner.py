# Independent auditor evaluator (Claude Opus 5.5) for the Padua corner value
# Lambda_c(n) = lambda_n(-1,-1), exact Padua convention (see brute.py).
#
# Auditor-derived exact reduction (checked against brute.py at n=2..12):
#   Lambda_c = -1 + 2/m + (4/(n m)) sum_{r=1}^{n} cot(pi r/(2m)) S_r,
#   S_r = sum_{l=0}^{r-1} cot(pi (l+theta_r)/n),  theta_r=(1-r/m)/2,  m=n+1.
# 'direct'  : evaluates S_r term by term (O(n^2)), Arb balls.
# 'fast'    : splits cot(pi t) = 1/(pi t) - 1/(pi(1-t)) + B(t); the two
#             harmonic parts are exact digamma differences, the analytic B part
#             uses Euler-Maclaurin with K Bernoulli terms (truncation NOT
#             rigorously bounded; validated empirically against 'direct').
# Arb arithmetic is outward-rounded; EM truncation is the only non-rigorous step.
import sys
from flint import arb, ctx
from fractions import Fraction
from math import comb

ctx.prec = 128

def bernoulli_numbers(K):
    Bn = [Fraction(0)] * (K + 1)
    Bn[0] = Fraction(1)
    for k in range(1, K + 1):
        Bn[k] = -sum(comb(k + 1, j) * Bn[j] for j in range(k)) / (k + 1)
    return Bn  # B_1 = -1/2 convention

KMAX = 30
BN = bernoulli_numbers(KMAX)
FACT = [1]
for i in range(1, KMAX + 2):
    FACT.append(FACT[-1] * i)

def bernpoly(k, th):  # th Fraction -> Fraction
    return sum(comb(k, i) * BN[i] * th ** (k - i) for i in range(k + 1))

PI = arb.pi()

def Bfun(y):  # y arb in [0,1]; closed form, endpoints by limits
    if y == 0:
        return 1 / PI
    if y == 1:
        return -1 / PI
    return (PI * y).cot() - 1 / (PI * y) + 1 / (PI * (1 - y))

def Bder(j, y):  # j>=1 derivative of B at y in [0,1], via Hurwitz zeta
    s = arb(j + 1)
    val = (y + 1) ** (-(j + 1)) + s.zeta(y + 2) + (-1) ** (j + 1) * s.zeta(2 - y)
    return (-1) ** j * FACT[j] * val / PI

def Gfun(y):  # integral_0^y B
    if y == 0 or y == 1:
        return arb(0)
    return ((PI * y).sin() / (PI * y * (1 - y))).log() / PI

def lam_direct(n):
    m = n + 1
    tot = arb(0)
    for r in range(1, n + 1):
        th = arb(m - r) / (2 * m)
        S = arb(0)
        for l in range(r):
            S += ((arb(l) + th) / n).cot_pi()
        tot += (arb(r) / (2 * m)).cot_pi() * S
    return -1 + arb(2) / m + 4 * tot / (n * m)

def lam_fast(n, K=16):
    m = n + 1
    Bd0 = [None] + [Bder(j, arb(0)) for j in range(1, K)]
    tot_h = arb(0)
    tot_b = arb(0)
    for r in range(1, n + 1):
        s = m - r
        w = (arb(r) / (2 * m)).cot_pi()
        q = arb(s) / (2 * m)
        D = (r + q).digamma() + (s - q).digamma() - (m - q).digamma() - q.digamma()
        tot_h += w * D
        th = Fraction(s, 2 * m)
        y = arb(r) / n
        # EM: sum_{l=0}^{r-1} g(l+th), g(t)=B(t/n)
        Gy = arb(0) if r == n else Gfun(y)
        By = -1 / PI if r == n else Bfun(y)
        em = n * Gy
        b1 = bernpoly(1, th)
        em += arb(b1.numerator) / b1.denominator * (By - 1 / PI)
        npow = arb(1)
        for k in range(2, K + 1):
            npow = npow / n
            bk = bernpoly(k, th)
            if bk == 0:
                continue
            j = k - 1
            dif = Bder(j, y) - Bd0[j]
            em += arb(bk.numerator) / (bk.denominator * FACT[k]) * npow * dif
        tot_b += w * em
    return -1 + arb(2) / m + 4 * tot_h / (PI * m) + 4 * tot_b / (n * m), \
        4 * tot_h / (PI * m), 4 * tot_b / (n * m)

if __name__ == "__main__":
    mode = sys.argv[1]
    ns = [int(v) for v in sys.argv[2:]]
    for n in ns:
        if mode == "direct":
            print(n, lam_direct(n).str(35, radius=True)); sys.stdout.flush()
        else:
            K = 16 if n < 2000 else (8 if n < 6400 else 6)
            L, H, V = lam_fast(n, K=K)
            print(n, K, L.str(36, radius=True), H.str(36, radius=True), V.str(36, radius=True)); sys.stdout.flush()
