#!/usr/bin/env python3
"""[E] Direct-quadrature checks of the N1 cancellation integral used by F01-em2-entropy,
F04, F08-coefficients and F09 section 2.

I(C,D,v)=int_0^pi [|C cot x+D cot(x+v)|-|C cot x|-|D cot(x+v)|] dx  (N1-02 definition)
J(u,s,e)=I((u-s)/2,(u+s)/2,e)                                        (N1-14 definition)
Quadrature: mpmath tanh-sinh on pieces split at every pole, zero and sign change.
Usage: PYTHONPATH=<pylib> python3 entropy_J_check.py
"""
import random
from mpmath import mp, mpf, cot, sin, cos, tan, log, sqrt, asin, pi, quad, fabs, nstr

mp.dps = 30

def I(C, D, v):
    C, D, v = mpf(C), mpf(D), mpf(v)
    pts = {mpf(0), pi}
    def addmod(x):
        x = x % pi
        if 0 < x < pi:
            pts.add(x)
    addmod(pi/2); addmod(pi/2 - v); addmod(-v)
    if C + D != 0:
        k = (D - C)*sin(v)/(C + D)
        if fabs(k) <= 1:
            t = asin(k)
            for w in (t, pi - t):
                for j in range(-2, 3):
                    addmod((w + 2*pi*j - v)/2)
    pts = sorted(pts)
    g = lambda x: fabs(C*cot(x) + D*cot(x + v)) - fabs(C*cot(x)) - fabs(D*cot(x + v))
    return sum(quad(g, [pts[i], pts[i + 1]]) for i in range(len(pts) - 1))

def J(u, s, e):
    u, s = mpf(u), mpf(s)
    return I((u - s)/2, (u + s)/2, e)

def eta(x):
    return mpf(0) if x == 0 else x*log(x)

random.seed(20261108)
print("1. same-sign branch s<u: J = 2[c log(c/u)+b log(b/u)], independent of e")
mx = 0
for _ in range(12):
    u = mpf(random.uniform(0.02, 0.6)); s = u*mpf(random.uniform(0.0, 0.98)); e = mpf(random.uniform(0.05, 1.5))
    c, b = (u - s)/2, (u + s)/2
    mx = max(mx, fabs(J(u, s, e) - 2*(eta(c) + eta(b) - (c + b)*log(u))))
print("   max abs deviation over 12 random (u,s,e):", nstr(mx, 5))

print("2. s>u: R=J-2(s-u)log sin e; no-root (s sin e>=u): R=2u log sin e; root regime J_s formula")
mx3 = mxs = 0
for _ in range(8):
    u = mpf(random.uniform(0.05, 0.4)); e = mpf(random.uniform(0.3, 1.4))
    s = u/sin(e)*mpf(random.uniform(1.01, 2.0))   # no-root regime
    mx3 = max(mx3, fabs(J(u, s, e) - 2*(s - u)*log(sin(e)) - 2*u*log(sin(e))))
    s = u*mpf(random.uniform(1.02, 0.98/float(sin(e))))  # root regime u<s<u/sin e
    if s*sin(e) < u:
        dlt = mpf('1e-8')
        Js_num = (J(u, s + dlt, e) - J(u, s - dlt, e))/(2*dlt)
        Dd = sqrt(u**2 - s**2*sin(e)**2)
        Js = 2*log(sin(e)) + log((s*cos(e) - Dd)/(s*cos(e) + Dd))
        mxs = max(mxs, fabs(Js_num - Js))
print("   no-root R identity max dev:", nstr(mx3, 5), "; root-regime J_s formula max dev:", nstr(mxs, 5))

print("3. F08 (1): J(u,u+v,e*) - [|v|log|v|-(1+log 2u)|v|+2v_+ log tan e*], ratio to |v| -> 0")
for (u, es) in ((mpf('0.1'), mpf('0.7')), (mpf('0.05'), mpf('1.2'))):
    row = []
    for v in (mpf('1e-2'), mpf('1e-3'), mpf('1e-4'), mpf('-1e-2'), mpf('-1e-3'), mpf('-1e-4')):
        pred = fabs(v)*log(fabs(v)) - (1 + log(2*u))*fabs(v) + 2*max(v, 0)*log(tan(es))
        row.append(nstr((J(u, u + v, es) - pred)/fabs(v), 3))
    print(f"   u={u}, e*={es}: (J-pred)/|v| for v=+1e-2,+1e-3,+1e-4,-1e-2,-1e-3,-1e-4:", row)

print("4. F01 entropy obstruction: balanced alpha=beta=c, u=q/2, s_R(e)=|q/2-a tan(e/2)|, e0=2c")
for c in (mpf(1)/64, mpf(1)/8, mpf(1)/4):
    q = sin(c); a = cos(c); u = q/2; e0 = 2*c
    sR = lambda e: fabs(q/2 - a*tan(e/2))
    print(f"   c={nstr(c,4)}: s_R(e0)-u = {nstr(sR(e0) - u, 3)}")
    out = []
    for dl in (mpf('1e-2'), mpf('1e-3'), mpf('1e-4'), mpf('1e-5'), mpf('1e-6')):
        e = e0 - dl; h = dl/100
        dJ = (J(u, sR(e + h), e + h) - J(u, sR(e - h), e - h))/(2*h)
        pred = log((u + sR(e))/(u - sR(e)))*a/2/cos(e/2)**2
        out.append((nstr(dJ, 6), nstr(pred, 6)))
    print("      dJ/de along actual curve (numeric, predicted log((u+s)/(u-s)) s'):", out)
