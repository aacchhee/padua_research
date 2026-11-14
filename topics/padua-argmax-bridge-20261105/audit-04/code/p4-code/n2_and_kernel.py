# P4 audit: (1) degree-two four-leaf example of Section 5.1 recomputed from
# Lemma 2.1 by exact rational arithmetic (sympy); (2) numerical checks of
# Section 2-4 kernel identities and of Lambda_c expansion (mpmath, MEASURED).
import sympy as sp
import mpmath as mp
from fractions import Fraction as F

x, y, s, t = sp.symbols('x y s t')

def cardinals(n):
    m = n+1
    nodes = []
    for j in range(n+1):
        for k in range(m+1):
            if (j+k) % 2 == 0:
                nodes.append((j, k))
    T = lambda r, z: sp.chebyshevt(r, z)
    nu = lambda r: 1 if r == 0 else 2
    Ls = []
    for (j, k) in nodes:
        B1 = sp.cos(sp.pi*j/n); B2 = sp.cos(sp.pi*k/m)
        eps = sp.Rational(1, 2) if j in (0, n) else 1
        eta = sp.Rational(1, 2) if k in (0, m) else 1
        w = 2*eps*eta/(n*m)
        K = sum(nu(p)*nu(q)*T(p, x)*T(p, B1)*T(q, y)*T(q, B2)
                for p in range(n+1) for q in range(n+1-p))
        L = sp.expand(sp.nsimplify(w*(K-T(n, x)*T(n, B1))))
        Ls.append(((sp.nsimplify(B1), sp.nsimplify(B2)), sp.simplify(L)))
    return Ls

def bern_coeffs(poly, n, xr, yr):
    # tensor Bernstein coefficients of degree (n,n) on [xr]x[yr]
    x0, x1 = xr; y0, y1 = yr
    P = sp.Poly(sp.expand(poly.subs({x: x0+(x1-x0)*s, y: y0+(y1-y0)*t})), s, t)
    C = [[0]*(n+1) for _ in range(n+1)]
    for (a, b), c in P.terms():
        for i in range(a, n+1):
            for j in range(b, n+1):
                C[i][j] += c*sp.binomial(i, a)/sp.binomial(n, a)*sp.binomial(j, b)/sp.binomial(n, b)
    return C

Ls = cardinals(2)
print('n=2 nodes:', [nd for nd, _ in Ls])
# check cardinality
for nd, L in Ls:
    vals = [sp.nsimplify(L.subs({x: a, y: b})) for (a, b), _ in Ls]
    assert sorted(vals) == [0]*5+[1], (nd, vals)
lam = lambda X, Y: sum(abs(L.subs({x: X, y: Y})) for _, L in Ls)
print('Lambda_c(2) at (-1,-1):', sp.nsimplify(lam(-1, -1)), ' at (1,-1):', sp.nsimplify(lam(1, -1)),
      ' at (-1,1):', sp.nsimplify(lam(-1, 1)), ' at (1,1):', sp.nsimplify(lam(1, 1)))
for name, xr, yr in [('lower-left', (-1, 0), (-1, 0)), ('lower-right', (0, 1), (-1, 0)),
                     ('upper-left', (-1, 0), (0, 1)), ('upper-right', (0, 1), (0, 1))]:
    tot = [[0]*3 for _ in range(3)]
    for _, L in Ls:
        C = bern_coeffs(L, 2, xr, yr)
        for i in range(3):
            for j in range(3):
                tot[i][j] += abs(C[i][j])
    print(name, [[sp.nsimplify(v) for v in row] for row in tot])

# (2) kernel identity G_n via P_n=T_{n+1}+T_n, and n=7 lambda formula vs cardinal sum
mp.mp.dps = 30
def Gn_sum(n, u, v):
    s_ = mp.mpf(0)
    for p in range(n+1):
        for q in range(n+1-p):
            s_ += (1 if p == 0 else 2)*(1 if q == 0 else 2)*mp.cos(p*u)*mp.cos(q*v)
    return s_-mp.cos(n*u)
def Gn_P(n, u, v):
    P = lambda c: mp.chebyt(n+1, c)+mp.chebyt(n, c)
    return (P(mp.cos(u))-P(mp.cos(v)))/(mp.cos(u)-mp.cos(v))-mp.cos(n*u)
mx = 0
for n in [5, 8, 13]:
    for (u, v) in [(0.3, 1.1), (2.0, 0.4), (1.234, 2.9)]:
        mx = max(mx, abs(Gn_sum(n, u, v)-Gn_P(n, u, v)))
print('max |G_n(sum) - G_n(P_n form)| =', mp.nstr(mx, 5))

# corner value from (cu:positive) vs the four-term expansion, illustrative
def Lc(n):
    m = n+1; tot = mp.mpf(0)
    for j in range(n+1):
        for k in range(n+1):
            if (j+k) % 2 == 1:
                e = mp.mpf(1)/2 if j in (0, n) else 1
                h = mp.mpf(1)/2 if k == 0 else 1
                th = mp.pi*j/n; ph = mp.pi*k/m
                tot += e*h*(1+mp.cos(ph))/abs(mp.cos(th)-mp.cos(ph))
    return 4*tot/(n*m)+mp.mpf(1)/m
a = 2/mp.pi; d = mp.euler+mp.log(8/mp.pi); kap = mp.mpf('0.919710118388493')
for n in [2, 3, 10, 64, 200]:
    N = n+mp.mpf(1)/2
    exp4 = (a*(mp.log(N)+d))**2+kap-1/N
    v = Lc(n)
    print(f'n={n} Lambda_c={mp.nstr(v,15)} expansion={mp.nstr(exp4,15)} resid*N^2/logN={mp.nstr((v-exp4)*N**2/mp.log(N),6)}')
