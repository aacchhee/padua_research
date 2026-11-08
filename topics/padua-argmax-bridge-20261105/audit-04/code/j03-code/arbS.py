"""J3 audit: independent Arb enclosures of the phase primitive S_n and the actual Lebesgue function.
Formula used (paper localization-unified.tex, line 21): G_n(u,v)=[P(cos u)-P(cos v)]/(cos u-cos v)-cos(nu),
P=T_{n+1}+T_n; at a collision cos u=cos v the divided difference is P'(cos u). This differs from I25's
product formula R_{n+1}R_{n+1}+R_nR_n-cos(nu). Collisions are decided in exact integer arithmetic.
Arithmetic: FLINT Arb balls (python-flint), not binary64/Taylor. Exact Fraction endpoints via man_exp."""
from fractions import Fraction as F
from math import lcm
import flint
from flint import arb
flint.ctx.prec = 256
def q(x): x = F(x); return arb(x.numerator) / x.denominator
def exact(x):  # exact dyadic endpoint -> Fraction
    m, e = x.man_exp(); return F(int(m)) * (F(2) ** int(e))
def lo(x): return exact(x.lower())
def hi(x): return exact(x.upper())
def need(ok, why):
    if not ok: raise ValueError(why)
def tprime(k, U):
    """T_k'(cos(pi U)) for exact rational U."""
    if U.denominator == 1: return arb(k * k * (1 if (U.numerator * (k - 1)) % 2 == 0 else -1))
    return k * (k * q(U)).sin_pi() / q(U).sin_pi()
def P(n, U): return ((n + 1) * q(U)).cos_pi() + (n * q(U)).cos_pi()
def G(n, U, V, xU=None, PU=None, xV=None, PV=None):
    """G_n(pi U, pi V) for exact rationals U, V."""
    cnu = (n * q(U)).cos_pi()
    d, s = U - V, U + V
    if (d / 2).denominator == 1 or (s / 2).denominator == 1:   # cos(pi U) == cos(pi V) exactly
        return tprime(n + 1, U) + tprime(n, U) - cnu
    xU = q(U).cos_pi() if xU is None else xU; xV = q(V).cos_pi() if xV is None else xV
    PU = P(n, U) if PU is None else PU; PV = P(n, V) if PV is None else PV
    g = (PU - PV) / (xU - xV) - cnu; need(g.is_finite(), 'nonfinite ball'); return g
def S(n, a, b):
    """Ball for S_n(pi a, pi b) = (1/2nm) sum_{0<=r<2n,0<=s<2m,r+s odd} |G_n((r pi+pi a)/n,(s pi+pi b)/m)|."""
    a, b = F(a), F(b); m = n + 1; Q = lcm(a.denominator, b.denominator)
    pa, pb = a.numerator * (Q // a.denominator), b.numerator * (Q // b.denominator); D = 2 * n * m * Q
    rows = []
    for r in range(2 * n):
        U = (r + a) / n; rows.append((U, q(U).cos_pi(), P(n, U), q(r + a).cos_pi(), (r * Q + pa) * m))
    cols = []
    for s in range(2 * m):
        V = (s + b) / m; cols.append((V, q(V).cos_pi(), P(n, V), (s * Q + pb) * n))
    tot = arb(0)
    for r, (U, xU, PU, cnu, X) in enumerate(rows):
        for s in range(1 - r % 2, 2 * m, 2):
            V, xV, PV, Y = cols[s]
            if (X - Y) % D == 0 or (X + Y) % D == 0:
                g = tprime(n + 1, U) + tprime(n, U) - cnu
            else:
                g = (PU - PV) / (xU - xV) - cnu
            tot += abs(g)
    need(tot.is_finite(), 'nonfinite S'); return tot / (2 * n * m)
def actual_lambda(n, xi, zeta):
    """Ball for lambda_n(cos(pi(1-xi)), cos(pi(1-zeta))) via the four-term cardinal reflection,
    weights e_j f_k/(2nm), four signed G values added before the absolute value."""
    m = n + 1; A0, B0 = 1 - F(xi), 1 - F(zeta)
    us = {(sg, j): A0 + F(sg * j, n) for sg in (-1, 1) for j in range(n + 1)}
    vs = {(et, k): B0 + F(et * k, m) for et in (-1, 1) for k in range(m + 1)}
    cu = {key: (q(U).cos_pi(), P(n, U)) for key, U in us.items()}
    cv = {key: (q(V).cos_pi(), P(n, V)) for key, V in vs.items()}
    tot = arb(0)
    for j in range(n + 1):
        for k in range(j % 2, m + 1, 2):
            g = arb(0)
            for sg in (-1, 1):
                for et in (-1, 1):
                    U, V = us[sg, j], vs[et, k]
                    g += G(n, U, V, cu[sg, j][0], cu[sg, j][1], cv[et, k][0], cv[et, k][1])
            w = (F(1, 2) if j in (0, n) else F(1)) * (F(1, 2) if k in (0, m) else F(1))
            tot += abs(g) * q(w)
    need(tot.is_finite(), 'nonfinite lambda'); return tot / (2 * n * m)
def diamond_G(n, U, V):
    """Definition eq:angular-kernel: sum_{p+q<=n} nu_p nu_q cos(p u)cos(q v) - cos(n u), nu_0=1, nu_p=2."""
    nu = lambda p: 1 if p == 0 else 2
    cu = [(p * q(U)).cos_pi() for p in range(n + 1)]; cv = [(p * q(V)).cos_pi() for p in range(n + 1)]
    t = arb(0)
    for p in range(n + 1):
        for qq in range(n + 1 - p): t += nu(p) * nu(qq) * cu[p] * cv[qq]
    return t - cu[n]
def product_G(n, U, V):
    """J03/I25 form R_{n+1}(s)R_{n+1}(t)+R_n(s)R_n(t)-cos(nu), s=(u+v)/2, t=(v-u)/2, exact removable values."""
    def R(k, Z):
        if Z.denominator == 1: return arb(k * (1 if (Z.numerator * (k - 1)) % 2 == 0 else -1))
        return (k * q(Z)).sin_pi() / q(Z).sin_pi()
    s, t = (U + V) / 2, (V - U) / 2
    return R(n + 1, s) * R(n + 1, t) + R(n, s) * R(n, t) - (n * q(U)).cos_pi()
