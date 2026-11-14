# M5A s1: independent checks of the restored Lemma 4.2 (uc:scalar-maximum) reasons.
# Exact parts use Fraction/sympy; analytic profile values use mpmath (MEASURED).
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
ok = True
def check(name, cond, info=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + str(info) if info else ""))

# 1. exact arithmetic of the f''' bound
val = Fr(3, 40) + Fr(44, 35 * 1024) - Fr(1, 16) - Fr(37, 2048)
check("3/40+44/(35*1024)-1/16-37/2048 = -311/71680", val == Fr(-311, 71680), val)
t = sp.symbols('t', real=True)
I1 = 2 * sp.integrate(sp.Rational(22, 7) * t**4 - sp.Rational(1, 8), (t, 0, sp.Rational(1, 4)))
check("2 int_0^{1/4}((22/7)t^4-1/8) = 44/(35*1024)-1/16", sp.simplify(I1 - (sp.Rational(44, 35 * 1024) - sp.Rational(1, 16))) == 0)
I2 = 2 * (sp.Rational(3, 8) - sp.Rational(1, 4)) * (sp.Rational(27, 512) - sp.Rational(1, 8))
check("2(3/8-1/4)(27/512-1/8) = -37/2048", I2 == sp.Rational(-37, 2048))
check("(3/8)^3 = 27/512", sp.Rational(3, 8)**3 == sp.Rational(27, 512))
# f(0)/8 < 3/40 from k0<9/5 and pi>3
check("(9/5)/(8*pi) < 3/40 <=> pi>3", Fr(9, 5) / 8 / 3 == Fr(3, 40))
# 2. polynomial step
poly = 3 + 34 * t**2 + 3 * t**4 - 20 * t
check("poly = 34(t-5/17)^2+1/17+3t^4", sp.expand(poly - (34 * (t - sp.Rational(5, 17))**2 + sp.Rational(1, 17) + 3 * t**4)) == 0)
check("3/40 - t(1/2-t)/(1-t^2)^2 = poly/(40(1-t^2)^2)",
      sp.simplify(sp.Rational(3, 40) - t * (sp.Rational(1, 2) - t) / (1 - t**2)**2 - poly / (40 * (1 - t**2)**2)) == 0)
check("10*pi*3/40 = 3pi/4", sp.simplify(10 * sp.pi * sp.Rational(3, 40) - 3 * sp.pi / 4) == 0)
ub = -mp.pi**2 / 12 + 2 * mp.pi + 19 / mp.pi
check("-pi^2/12+2pi+19/pi < 12", ub < 12, mp.nstr(ub, 10))
check("pi^4/40 <= pi^2/4 (pi^2<10)", mp.pi**4 / 40 <= mp.pi**2 / 4)
# 3. W(pi-w) >= w^2/4 : g'(s) symbolic, and numeric
s = sp.symbols('s', real=True)
g = sp.log(sp.cot((sp.pi - s) / 4))
gp = sp.simplify(sp.diff(g, s))
check("g'(s) = 1/(2 sin((pi-s)/2))", sp.simplify(gp - 1 / (2 * sp.sin((sp.pi - s) / 2))) == 0, gp)
def W(tt):
    tt = abs(tt)
    return mp.quad(lambda q: mp.log(mp.cot(q / 4)), [tt, mp.pi])
mn = min(W(mp.pi - w) - w**2 / 4 for w in [mp.mpf(k) / 20 * mp.pi for k in range(0, 21)])
check("W(pi-w)-w^2/4 >= 0 on 21 points", mn >= -mp.mpf('1e-30'), mp.nstr(mn, 5))
# 4. constants
gam = mp.euler
k0 = 2 * gam + 4 * mp.log(2) - 2 * mp.log(mp.pi)
lam0 = 2 / mp.pi * mp.log(4 / mp.pi)
J0 = 2 * (mp.log(mp.pi) - gam) / mp.pi
check("161/100<k0<9/5", mp.mpf(161) / 100 < k0 < mp.mpf(9) / 5, mp.nstr(k0, 10))
check("lambda0<1/(2pi)", lam0 < 1 / (2 * mp.pi), mp.nstr(lam0 * 2 * mp.pi, 8))
check("J0>1/pi", J0 > 1 / mp.pi, mp.nstr(J0 * mp.pi, 8))
check("e^{1/4}>=41/32>32/25; 4/pi<32/25 via pi>25/8", mp.e**0.25 >= mp.mpf(41) / 32 > mp.mpf(32) / 25 and Fr(4) / Fr(25, 8) == Fr(32, 25))
check("log(eps/pi)+int_eps^pi dt/(2 sin(t/2)) -> log(4/pi)",
      abs(mp.log(mp.mpf('1e-12') / mp.pi) - mp.log(mp.tan(mp.mpf('1e-12') / 4)) - mp.log(4 / mp.pi)) < 1e-20)
check("J0 bound needs log pi - gamma > 1/2 (11/10-3/5)", Fr(11, 10) - Fr(3, 5) == Fr(1, 2))

# 5. scalar profile f, f''' formula, sign of f'''/sin(w/2), H(w)-H0
def Ccal(tt):
    return -mp.digamma(tt) - mp.digamma(1 - tt)
def Phi(tt):
    tt = tt - mp.floor(tt)
    if tt == 0:
        return mp.mpf(1)
    return mp.sin(mp.pi * tt) / mp.pi * (Ccal(tt) - 2 * mp.log(mp.pi))
def f(w):
    return Phi(mp.mpf(1) / 2 + w / (2 * mp.pi))
check("f(0) = k0/pi", abs(f(0) - k0 / mp.pi) < 1e-30, mp.nstr(f(0), 12))
def f3_formula(w):
    return f(0) / 8 * mp.sin(w / 2) + 2 * mp.quad(lambda q: (q**3 * mp.sin(q * w) - mp.sin(w / 2) / 8) / mp.cos(mp.pi * q), [0, 0.5])
mp.mp.dps = 30
worst = -1
for w in [mp.mpf(k) / 10 for k in range(1, 31)]:
    d3 = mp.diff(f, w, 3)
    fo = f3_formula(w)
    worst = max(worst, abs(d3 - fo))
check("f''' integral formula vs numerical derivative (w=0.1..3.0)", worst < 1e-12, mp.nstr(worst, 3))
r = max(f3_formula(w) / mp.sin(w / 2) for w in [mp.mpf(k) / 50 * mp.pi for k in range(1, 50)])
check("max f'''/sin(w/2) < -311/71680", r < -mp.mpf(311) / 71680, mp.nstr(r, 6))
mx = max(abs(f3_formula(w)) for w in [mp.mpf(k) / 50 * mp.pi for k in range(-50, 51)])
check("max|f'''| < 13/20", mx < mp.mpf(13) / 20, mp.nstr(mx, 6))
# sine-ratio monotonicity R_t(w) <= sin(pi t)
bad = 0
for tq in [mp.mpf(k) / 40 for k in range(1, 20)]:
    for w in [mp.mpf(j) / 40 * mp.pi for j in range(1, 40)]:
        if mp.sin(tq * w) / mp.sin(w / 2) > mp.sin(mp.pi * tq) + 1e-25:
            bad += 1
check("sin(tw)/sin(w/2) <= sin(pi t) on grid", bad == 0)

# H via paired absolutely convergent formula
def H(w):
    integrand = lambda q: (f(w + q) + f(w - q) - 2 * f(w)) / (2 * mp.sin(q / 2))
    return lam0 * f(w) + mp.quad(integrand, [0, mp.pi / 2, mp.pi]) / mp.pi
mp.mp.dps = 20
H0 = H(mp.mpf(0))
kappa_H0 = None
worst = -10
for w in [mp.mpf(k) / 12 * mp.pi for k in range(1, 13)]:
    lhs = H(w) - H0
    rhs = -(mp.pi - 3) * w**2 / (4 * mp.pi**3)
    worst = max(worst, lhs - rhs)
check("H(w)-H0 <= -(pi-3)w^2/(4pi^3) at 12 points", worst <= 0, "max(lhs-rhs)=" + mp.nstr(worst, 5))
check("H0 = 0.310002264...", abs(H0 - mp.mpf('0.310002264407')) < 1e-8, mp.nstr(H0, 12))
print("ALL PASS" if ok else "SOME FAIL")
