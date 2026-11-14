"""C1 audit: constants, quadrature, digamma estimates and the sharp expansion (Section 3)."""
import sys, os
sys.path.insert(0, os.environ.get("PYLIB", ""))
import mpmath as mp
import numpy as np
import sympy as sp
from scipy.special import digamma as dg
mp.mp.dps = 30
pi = mp.pi; a = 2 / pi; gam = mp.euler
d = gam + mp.log(8 / pi); d0 = gam + 2 * mp.log(2); q0 = pi**2 / 4 - 1
out = []
w = lambda x: mp.cot(pi * x / 2)
B = lambda x: mp.cot(pi * x) - 1 / (pi * x) + 1 / (pi * (1 - x))
# odd-l series in closed form via digamma (independent of the text's argument)
def oddsum(t):
    if t == 0: return 7 * mp.zeta(3) / 8
    return (2 * mp.digamma(0.5) - mp.digamma((1 - t) / 2) - mp.digamma((1 + t) / 2)) / (4 * t**2)
def kap_int(t):
    return 8 / pi * t**2 * w(t) * oddsum(t) if t > 0 else mp.mpf(0)
kappa = mp.quad(kap_int, [0, 0.5, 1])
out.append(f"kappa = {mp.nstr(kappa, 20)}  (positive: {kappa > 0})")
out.append(f"kappa integrand at t=1-1e-12: {mp.nstr(kap_int(1 - mp.mpf(10)**-12), 12)} (claimed limit 2); at 1e-8: {mp.nstr(kap_int(mp.mpf(10)**-8), 6)}")
out.append(f"intro limit t^2 cot(pi t/2)/(1-t^2) at 1-1e-15: {mp.nstr((lambda t: t**2*w(t)/(1-t**2))(1-mp.mpf(10)**-15), 15)} vs pi/4={mp.nstr(pi/4,15)}")
# check odd-sum formula against direct sum
t0 = mp.mpf('0.37')
out.append(f"odd-l sum closed form check: {mp.nstr(oddsum(t0) - mp.nsum(lambda k: 1/((2*k+1)*((2*k+1)**2 - t0**2)), [0, mp.inf]), 3)}")
# bound 1/(l(l^2-t^2)) <= 9/(8 l^3) for l>=3, sum bound
out.append(f"l>=3 bound worst ratio: {max(float((1/(l*(l*l-1)))/(9/(8*l**3))) for l in range(3, 200, 2))}")
# integrals
I1 = mp.quad(lambda x: w(x) / (1 - x) - a / x, [0, 0.5, 1])
I2 = mp.quad(lambda x: x * w(x), [0, 1])
IB = mp.quad(lambda x: x * w(x) * B(x), [0, 0.5, 1])
out.append(f"I1={mp.nstr(I1,18)} I2={mp.nstr(I2,18)} IB={mp.nstr(IB,18)}")
out.append(f"(cu:cancel) 2IB - a I1 = {mp.nstr(2*IB - a*I1, 18)} vs a^2-1+a^2 log(pi/2) = {mp.nstr(a**2 - 1 + a**2*mp.log(pi/2), 18)}")
out.append(f"int (w - a/x) = {mp.nstr(mp.quad(lambda x: w(x) - a/x, [0,1]),18)} vs a log(2/pi)={mp.nstr(a*mp.log(2/pi),18)}")
out.append(f"int (cot y - 1/y) on [0,pi/2] = {mp.nstr(mp.quad(lambda y: mp.cot(y) - 1/y, [0, pi/2]),15)} vs log(2/pi)={mp.nstr(mp.log(2/pi),15)}")
betaH = -2 - a**2 * d0 - a * (I1 + I2)
betaB = -a**2 + 2 * IB + a * I2
CB = 4 * mp.quad(lambda t: w(t) * mp.quad(B, [0, t]), [0, 1])
out.append(f"betaH={mp.nstr(betaH,15)} betaB={mp.nstr(betaB,15)} CB={mp.nstr(CB,15)} 2+bH+bB={mp.nstr(2+betaH+betaB,15)} vs -1-a^2 d={mp.nstr(-1-a**2*d,15)}")
# psi constants and S_u, S_e
out.append(f"psi(1/2)={mp.nstr(mp.digamma(0.5),15)} vs {mp.nstr(-gam-2*mp.log(2),15)}; psi'(1/2)={mp.nstr(mp.psi(1,0.5),15)} vs {mp.nstr(pi**2/2,15)}")
Su = mp.nsum(lambda r: (r * mp.psi(1, r + 0.5) - 1) / r, [1, mp.inf])
Se = mp.nsum(lambda r: (mp.digamma(r + 0.5) - mp.log(r)) / r, [1, mp.inf])
out.append(f"S_u={mp.nstr(Su,15)} vs 1+2log2-pi^2/4={mp.nstr(1+2*mp.log(2)-pi**2/4,15)}; S_e={mp.nstr(Se,15)}; q0+S_u={mp.nstr(q0+Su,15)} vs 2log2={mp.nstr(2*mp.log(2),15)}")
out.append("r^2 e_r, r^2 u_r (r=1,10,100,1000): " + str([(r, mp.nstr(r**2*(mp.digamma(r+0.5)-mp.log(r)),6), mp.nstr(r**2*(r*mp.psi(1,r+0.5)-1),6)) for r in (1,10,100,1000)]))
# finite recurrence identity
for R in (1, 2, 7):
    lhs = sum(mp.psi(1, r + 0.5) for r in range(1, R + 1))
    rhs = (R + 0.5) * mp.psi(1, R + 0.5) + mp.digamma(R + 0.5) - mp.digamma(0.5) - mp.psi(1, 0.5) / 2
    out.append(f"recurrence identity R={R}: dev {mp.nstr(lhs-rhs,3)}")
# midpoint bound for t^-2 sum: psi'(r+1/2) - 1/r <= 1/(3r^3)
out.append("psi'(r+1/2)-1/r vs 1/(3r^3): " + str([(r, mp.nstr((mp.psi(1,r+0.5)-1/mp.mpf(r))*3*r**3,6)) for r in (1, 2, 5, 50)]))
# psi estimates: z^2 (psi - log z + 1/(2z)), z^2(psi' - 1/z) for z>=1
out.append("z^2 psi err, z^2 psi' err: " + str([(z, mp.nstr(z**2*(mp.digamma(z)-mp.log(z)+1/(2*z)),5), mp.nstr(z**2*(mp.psi(1,z)-1/z),5)) for z in (1, 2, 10, 1000)]))
# R endpoint values
J = lambda x: mp.log(1 - x) - mp.digamma((1 - x) / 2)
F = lambda x: mp.log(x) + mp.log(1 - x) - mp.digamma((1 - x) / 2)
Rf = lambda x: w(x) * F(x) - a * (mp.log(x) + d0) / x
out.append(f"J(0)={mp.nstr(J(0),12)} d0={mp.nstr(d0,12)} J'(0)={mp.nstr(mp.diff(J,0),12)} q0={mp.nstr(q0,12)}")
out.append(f"R(1e-9)={mp.nstr(Rf(mp.mpf(10)**-9),10)} aq0={mp.nstr(a*q0,10)}; R(1-1e-9)={mp.nstr(Rf(1-mp.mpf(10)**-9),10)} pi-a d0={mp.nstr(pi-a*d0,10)}")
out.append(f"B(0+)={mp.nstr(B(mp.mpf(10)**-12),10)} 1/pi={mp.nstr(1/pi,10)}; B(1-)={mp.nstr(B(1-mp.mpf(10)**-12),10)}")
# w bounds
xs = np.linspace(1e-6, 1 - 1e-6, 200001)
wv = 1 / np.tan(np.pi * xs / 2)
out.append(f"w<=a/x max ratio {np.max(wv * xs * np.pi / 2):.6f}; w<=pi(1-x) on [1/2,1) max ratio {np.max((wv/(np.pi*(1-xs)))[xs>=0.5]):.6f}")
ys = np.linspace(0, 1, 100001)
out.append(f"sin(pi y) >= 2 min(y,1-y): min diff {np.min(np.sin(np.pi*ys) - 2*np.minimum(ys,1-ys)):.3e}")

# quadrature lemma example g = x log x: m^2 * err / log m
def lemma_err(g, ig, g0, g1, m):
    r = np.arange(1, m) / m
    return np.sum(g(r)) / m - (ig - (g0 + g1) / (2 * m))
g = lambda x: x * np.log(x)
out.append("x log x lemma: m^2 err/log m = " + str([(m, round(lemma_err(g, -0.25, 0, 0, m) * m * m / np.log(m), 5)) for m in (10, 100, 1000, 10000)]))

# Harmonic/psi expansions of (cu:center), (cu:row-expand)
worst_c = 0; worst_Q = 0
for m in (5, 17, 64, 301, 1500):
    for r in range(1, m):
        s = m - r; x = mp.mpf(r) / m; al = (1 - x) / 2
        D = mp.digamma(r + al) + mp.digamma(s - al) - mp.digamma(m - al) - mp.digamma(al)
        cen = (mp.digamma(r + 0.5) + mp.digamma(s) - mp.digamma(al) - mp.digamma(m)
               - (r * mp.psi(1, r + 0.5) + s * mp.psi(1, s) - s * mp.psi(1, m)) / (2 * m))
        worst_c = max(worst_c, abs(D - cen) * m * m)
        er = mp.digamma(r + 0.5) - mp.log(r); ur = r * mp.psi(1, r + 0.5) - 1
        rex = mp.log(m) + F(x) + er - 1 / (2 * m * (1 - x)) - (x + ur) / (2 * m)
        worst_Q = max(worst_Q, abs(D - rex) / (1 / s**2 + 1 / (m * s) + 1 / mp.mpf(m)**2))
    if m >= 301: break
out.append(f"(cu:center) max m^2|err| = {mp.nstr(worst_c,6)} (claimed O(1)); (cu:row-expand) max |Q|/(s^-2+(ms)^-1+m^-2) = {mp.nstr(worst_Q,6)}")

# sum log r / r expansion constant C_K and residual
def logsum(m): return mp.fsum(mp.log(r) / r for r in range(1, m))
CK_est = []
for m in (1000, 4000):
    CK_est.append(logsum(m) - (mp.log(m)**2 / 2 - mp.log(m) / (2 * m)))
out.append(f"C_K estimates m=1000,4000: {[mp.nstr(c,12) for c in CK_est]}; diff*m^2/log m = {mp.nstr((CK_est[0]-CK_est[1])*1000**2/mp.log(1000),5)}")
# smooth row expansion residual  n*|err|/t
worst_s = 0
for n in (50, 200, 800):
    m = n + 1
    Ivals = {}
    for r in range(1, m, max(1, m // 40)):
        t = mp.mpf(r) / m; al = (1 - t) / 2
        S = mp.fsum(B((l + al) / n) for l in range(r))
        It = mp.quad(B, [0, t])
        worst_s = max(worst_s, abs(S - n * It - t / 2 * (B(t) + 1 / pi)) * n / t)
out.append(f"smooth row: max n|err|/t = {mp.nstr(worst_s,6)} (claimed bounded)")

# Full corner value via (cu:positive), float64, large n; theorem check
def Lc(n):
    m = n + 1
    j = np.arange(n + 1)[:, None]; k = np.arange(n + 1)[None, :]
    ej = np.where((j == 0) | (j == n), 0.5, 1.0); ek = np.where(k == 0, 0.5, 1.0)
    u = j * np.pi / n; v = k * np.pi / m
    mask = ((j + k) % 2 == 1)
    with np.errstate(divide='ignore', invalid='ignore'):
        fv = (1 + np.cos(v)) / np.abs(np.cos(u) - np.cos(v))
    tot = np.sum(np.where(mask, ej * ek * fv, 0.0))
    return 4 * tot / (n * m) + 1 / m
kf = float(kappa); af = float(a); dfl = float(d)
rows = []
for n in (2, 3, 10, 11, 50, 51, 200, 201, 800, 801, 2000, 2001, 3000, 3001):
    N = n + 0.5; L = Lc(n)
    AN2 = af**2 * (np.log(N) + dfl)**2
    R = L - (AN2 + kf - 1 / N)
    rows.append((n, round(L, 10), round(N * (L - AN2 - kf), 6), round(R * N * N / np.log(N), 5)))
out.append("n, Lambda_c, N(Lc-A(N)^2-kappa) [->-1], R N^2/log N [bounded]:")
out += ["   " + str(r) for r in rows]
# separate Proposition checks: H_m and 4V_n/(nm) fits
def Hm(m):
    r = np.arange(1, m); x = r / m; s = m - r; al = (1 - x) / 2
    D = dg(r + al) + dg(s - al) - dg(m - al) - dg(al)
    return 4 / (np.pi * m) * np.sum(1 / np.tan(np.pi * x / 2) * D)
def Vn(n):
    m = n + 1; tot = 0.0
    Bf = lambda x: 1 / np.tan(np.pi * x) - 1 / (np.pi * x) + 1 / (np.pi * (1 - x))
    for r in range(1, m):
        al = (1 - r / m) / 2; l = np.arange(r)
        tot += 1 / np.tan(np.pi * r / m / 2) * np.sum(Bf((l + al) / n))
    return 4 * tot / (n * m)
ms = np.array([400, 600, 900, 1300, 1800, 2400, 3000])
Ham = np.array([Hm(m) - af**2 * (np.log(m) + dfl)**2 + af**2 * np.log(m) / m for m in ms])
X = np.vstack([np.ones_like(ms, dtype=float), 1 / ms, np.log(ms) / ms**2, 1 / ms**2]).T
coef = np.linalg.lstsq(X, Ham, rcond=None)[0]
out.append(f"H_m fit: C_H~{coef[0]:.10f}, beta_H fit {coef[1]:.6f} vs claimed {float(betaH):.6f}")
ns = np.array([300, 500, 800, 1200, 1700, 2300])
Vv = np.array([Vn(n) for n in ns])
X2 = np.vstack([np.ones_like(ns, dtype=float), 1 / ns, 1 / ns**2]).T
c2 = np.linalg.lstsq(X2, Vv, rcond=None)[0]
out.append(f"4V/(nm) fit: C_B~{c2[0]:.10f} vs {float(CB):.10f}; beta_B fit {c2[1]:.6f} vs claimed {float(betaB):.6f}")
out.append(f"C=-1+C_H+C_B ~ {-1+coef[0]+c2[0]:.10f} vs kappa {kf:.10f}")

# sympy: intro Taylor, P'' and A(m)^2-A(n)^2
nn, zz = sp.symbols('n z', positive=True)
ser = sp.series(sp.log(nn + sp.Rational(1, 2))**2 - sp.log(nn)**2 - sp.log(nn) / nn, nn, sp.oo, 3)
out.append(f"sympy log^2(n+1/2)-log^2 n - log n/n ~ {ser}")
aa, dd = sp.symbols('a d', positive=True)
P = aa**2 * (sp.log(zz) + dd)**2
out.append(f"P''-claimed = {sp.simplify(sp.diff(P, zz, 2) - 2*aa**2*(1 - sp.log(zz) - dd)/zz**2)}")
uu = sp.symbols('u', real=True)
out.append(f"cot(pi x)=(w-1/w)/2 check: {sp.simplify(sp.cot(2*uu) - (sp.cot(uu) - 1/sp.cot(uu))/2)}")
xx = sp.symbols('x', positive=True)
wexpr = sp.cot(sp.pi * xx / 2)
out.append(f"w' + (1+w^2)/a = {sp.simplify(sp.diff(wexpr, xx) + (1 + wexpr**2) * sp.pi / 2)}")
c, c0, c1 = sp.symbols('c c0 c1')
out.append(f"common denominator numerator check: {sp.expand((1+c1)*(c-c0)-(1+c0)*(c-c1) - (1+c)*(c1-c0))}")
p_, A_, B_ = sp.symbols('p A B')
out.append("w series at 0: " + str(sp.series(wexpr, xx, 0, 4)) + "; B series at 0: " + str(sp.series(sp.cot(sp.pi*xx) - 1/(sp.pi*xx) + 1/(sp.pi*(1-xx)), xx, 0, 2)))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_asym.out"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
