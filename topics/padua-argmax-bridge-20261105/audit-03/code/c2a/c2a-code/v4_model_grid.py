# C2A audit: completed model on a phase grid (float precision, scipy quad).
# Checks uc:model-loss, uc:central-decomposition, uc:regular-loss, uc:weighted-C,
# uc:central-pair*, b_full coefficient identity, envelope uc:endpoint-envelope, and
# several of the companion's added claims (aD<=7u/2, xp+yq<=4u, bounded subtracted integrand).
import math, sys
import numpy as np
from scipy import integrate, special
pi = math.pi; EG = 0.5772156649015329
def Cc(t): return -special.digamma(t)-special.digamma(1-t)
def Phi(t):
    t = t-math.floor(t)
    if t < 1e-14 or t > 1-1e-14: return 1.0
    return math.sin(pi*t)/pi*(Cc(t)-2*math.log(pi))
def f(w): return Phi(0.5+w/(2*pi))
lam0 = 2/pi*math.log(4/pi)
def H(w):
    w = abs(w)
    g = lambda t: (f(w+t)+f(w-t)-2*f(w))/(2*math.sin(t/2))
    pts = [pi-w] if 0 < pi-w < pi else None
    val, err = integrate.quad(g, 0, pi, points=pts, limit=200, epsabs=1e-12)
    return lam0*f(w)+val/pi
H0 = H(0.0)
C0 = 2*EG+4*math.log(2); bst = C0-3.5; B = C0**2/pi**2; d0 = C0*bst/pi**2; v0 = 7*bst/(2*pi**2)
g0 = 4*(math.log(pi)**2-math.log(2)**2)/pi**2; t0 = 2*math.log(2)/pi
kappa = 0.9197101183884925
G = EG+math.log(8/pi); Cstar = 4*G**2/pi**2+kappa; j = H0+d0-g0; bc = 8*G/pi**2
I4 = 0.8740191848

def J(v, s, e):
    s = abs(s)
    if v <= 0: return 2*s*math.log(math.sin(e))
    if s <= v:
        c = (v-s)/2; b = (v+s)/2
        xl = lambda z: 0.0 if z <= 0 else z*math.log(z/v)
        return 2*(xl(c)+xl(b))
    c = (s-v)/2; b = (s+v)/2; se = math.sin(e)
    if s*se >= v: return 2*s*math.log(se)
    th = math.asin(s*se/v); t1 = (th-e)/2
    out = 2*s*math.log(se)+2*b*math.log(math.cos(t1)/math.sin(t1+e))
    if c > 0 and t1 > 0: out -= 2*c*math.log(math.cos(t1+e)/math.sin(t1))
    return out

def phase(x, y):
    rho = x+y; ce = math.cos(rho/2); cd = math.cos((x-y)/2); a = ce*cd; u = 1-a; z = (1-ce)*(1-cd)
    p = math.sin(x); q = math.sin(y); return rho, ce, cd, a, u, z, p, q

def bfull(x, y):
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    U0 = ce*f(x-y)+cd*f(x+y)
    alog = 0.0 if a <= 0 else a*math.log(a)
    return 2*U0/pi+(8*a*math.log(2)+4*alog+2*(x*p+y*q))/pi**2

def Einf(x, y):
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    def wC(c, t):  # c * C(t) with continuous endpoint value pi
        if t < 1e-13 or t > 1-1e-13: return pi
        return c*Cc(t)
    return a/3+wC(cd, 0.5+(x-y)/(2*pi))*wC(ce, 0.5+(x+y)/(2*pi))/pi**2

def cancel_integrand(t, x, y):
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    T = 2*a/math.tan(t/2); e = min(t, pi-t)
    return J(p/2, (q+T)/2, e)+J(p/2, abs(q-T)/2, e)-4*a/math.tan(t/2)*math.log(math.sin(t))

def Cinf(x, y):
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    val, err = integrate.quad(cancel_integrand, 0, pi, args=(x, y), points=[pi/2], limit=400, epsabs=1e-11)
    return Einf(x, y)+ce*H(x-y)+cd*H(x+y)-(1/3+g0)*a+val/pi**2, val

def Ec(x, y):
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    def ig(t):
        w = a*math.tan(t/2)
        return J(p/2, w+q/2, t)+J(p/2, abs(w-q/2), t)-4*w*math.log(math.sin(t))
    val, err = integrate.quad(ig, 0, pi/2, limit=400, epsabs=1e-12)
    return val/pi**2

def Bbeta(x, y):
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    if q == 0: return 0.0
    b = 2*math.atan(q/(2*a))
    val, err = integrate.quad(lambda t: (q/2-a*math.tan(t/2))*(-math.log(math.sin(t))), 0, b, limit=200)
    return 4/pi**2*val, b

print('H0 =', H0, ' C* =', Cstar, ' j =', j)
viol = []
worst = {}
def track(name, slack, pt):
    if name not in worst or slack < worst[name][0]: worst[name] = (slack, pt)
    if slack < -1e-9: viol.append((name, slack, pt))

M = int(sys.argv[1]) if len(sys.argv) > 1 else 14
pts = []
for i in range(M+1):
    for k in range(M+1-i):
        pts.append((pi*i/M, pi*k/M))
# finer near origin
for i in range(9):
    for k in range(9-i):
        pts.append((0.125*i, 0.125*k))
for (x, y) in pts:
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    bf = bfull(x, y)
    track('bfull-bc<=3u/pi^2', 3*u/pi**2-(bf-bc), (x, y))
    track('bfull<79/(5pi^2)', 79/(5*pi**2)-bf, (x, y))
    track('xp+yq<=4u', 4*u-(x*p+y*q), (x, y))
    Dm = (Cc(0.5+(x+y)/(2*pi)) if rho < pi-1e-12 else None)
    if a > 1e-12:
        Dsum = Cc(0.5+(x+y)/(2*pi))+Cc(0.5+(x-y)/(2*pi))-2*C0
        track('aD<=7u/2', 3.5*u-a*Dsum, (x, y))
    Ci, val = Cinf(x, y)
    track('Cinf-C*<=-ju+t0p-(H0+v0)z', -j*u+t0*p-(H0+v0)*z-(Ci-Cstar), (x, y))
    track('Cinf<9/4', 2.25-Ci, (x, y))
    track('Einf<=a/3+B-d0u-v0z', a/3+B-d0*u-v0*z-Einf(x, y), (x, y))
    if rho <= pi/2+1e-12:
        ec = Ec(x, y)
        # central decomposition: val/pi^2 should equal Ec exactly on rho<=pi/2
        track('central-decomp |Ec - cancel|', 1e-8-abs(ec-val/pi**2), (x, y))
        track('regular-loss', -j*u-(H0+v0)*z-((Ci-ec)-Cstar), (x, y))
        Bb = Bbeta(x, y)
        bb = Bb[0] if isinstance(Bb, tuple) else Bb
        if a > 0:
            track('Ec<=4I4 p^1.5/(pi^2 sqrt a)-Bb', 4*I4*p**1.5/(pi**2*math.sqrt(a))-bb-ec, (x, y))
        if x == 0: track('Ec(0,y)=-Bb', 1e-8-abs(ec+bb), (x, y))
        if rho <= 0.5+1e-12:
            track('Ec<=3x^1.5/8-Bb', 3*x**1.5/8-bb-ec, (x, y))
            track('Bb>=1679y^2/8000', bb-1679*y**2/8000, (x, y))
        if rho <= 1+1e-12:
            track('Ec<=5x^1.5/12-Bb', 5*x**1.5/12-bb-ec, (x, y))
        if isinstance(Bb, tuple):
            track('0<=b<=rho', rho-Bb[1], (x, y)); track('b>=y', Bb[1]-y, (x, y))
print('points:', len(pts), ' violations:', len(viol))
for vv in viol[:30]: print(vv)
for k, (s, pt) in sorted(worst.items()): print('%-34s min slack %.3e at (%.4f, %.4f)' % (k, s, pt[0], pt[1]))
# weighted-C on theta grid
mn = min((C0-bst*(1-math.cos(th/2)))-(math.cos(th/2)*Cc(0.5+th/(2*pi)) if abs(th) < pi-1e-12 else pi) for th in np.linspace(-pi, pi, 2001))
print('weighted-C min slack', mn)
# coefficient identity: b_full = 2 D0 + (1/pi) int_0^pi {A(t)+A(2pi-t)-8a/(pi t)} dt, and |subtracted integrand| sup
for (x, y) in [(0.3, 0.2), (1.0, 0.4), (0.2, 2.5), (1.5, 1.5), (0.0, 0.0), (pi, 0.0)]:
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    def A(v):
        cot = 1/math.tan(v/2); C = (p-q-2*a*cot)/4; D = (p+q+2*a*cot)/4
        return 2*(abs(C)+abs(D))/pi
    sub = lambda t: A(t)+A(2*pi-t)-8*a/(pi*t)
    val, err = integrate.quad(sub, 0, pi, limit=400, points=[max(1e-9, pi-x-y), pi-abs(x-y)] if a > 0 else None)
    U0 = ce*f(x-y)+cd*f(x+y); D0 = U0/pi+4*a/pi**2*math.log(pi)
    alog = 0.0 if a <= 0 else a*math.log(a)
    ident = (8*a*math.log(2/pi)+4*alog+2*(x*p+y*q))/pi
    supv = max(abs(sub(t)) for t in np.linspace(1e-6, pi, 4000))
    print('coef (%.2f,%.2f): integral %.12f closed %.12f | bfull-2D0-integral/pi = %.2e | sup|subtracted integrand| = %.4f' % (x, y, val, ident, bfull(x, y)-2*D0-val/pi, supv))
