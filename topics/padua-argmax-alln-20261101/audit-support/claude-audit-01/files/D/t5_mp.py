"""mpmath (40 digits) spot-check of theory14 ratio R=(lambda-a*Lc)/(rho^2 log(n+1)) at n=20,21 via the
first-principles rhombus sum R_n(u,v)=sum_{|p|+|q|<=n} e^{i(pu+qv)} (no U-quotient), and cross-check of float values."""
import sys, os, json
import mpmath as mp
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from padlib import lebesgue, corner_value
mp.mp.dps = 40
def Rn(n, u, v):
    # direct finite cosine sum: sum_{a+b<=n} c_a c_b cos(a u) cos(b v), c_0=1, c_a=2
    cu = [mp.cos(a*u) for a in range(n+1)]; cv = [mp.cos(b*v) for b in range(n+1)]
    s = mp.mpf(0)
    for a in range(n+1):
        ca = 1 if a == 0 else 2
        inner = mp.fsum((1 if b == 0 else 2)*cv[b] for b in range(n+1-a))
        s += ca*cu[a]*inner
    return s
def lam(n, th, ph):
    m = n+1; tot = mp.mpf(0)
    for j in range(n+1):
        for k in range(m+1):
            if (j+k) % 2: continue
            eps = mp.mpf(1)/2 if j in (0, n) else 1; eta = mp.mpf(1)/2 if k in (0, m) else 1
            w = 2*eps*eta/(n*m)
            a = j*mp.pi/n; b = k*mp.pi/m
            s = 0
            for sa in (1, -1):
                for sb in (1, -1):
                    u = th+sa*a; v = ph+sb*b
                    s += Rn(n, u, v) - mp.cos(n*u)
            tot += abs(w*s/4)
    return tot
out = []
for n in (20, 21):
    m = n+1
    Lc = lam(n, mp.pi, mp.pi)
    for (rho, t) in ((mp.mpf('1e-3'), mp.mpf('0.5')), (mp.mpf(1)/64, mp.mpf(1)), (mp.mpf(1)/64, mp.mpf(0))):
        al = rho*t; be = rho*(1-t)
        L = lam(n, mp.pi-al/n, mp.pi-be/m)
        a = (mp.cos(al)+mp.cos(be))/2
        R = (L-a*Lc)/(rho**2*mp.log(n+1))
        Lf = lebesgue(n, [float(mp.pi-al/n)], [float(mp.pi-be/m)])[0]
        out.append({"n": n, "rho": mp.nstr(rho, 6), "t": mp.nstr(t, 3), "Lc_mp": mp.nstr(Lc, 25), "Lc_float": corner_value(n),
                    "lam_mp": mp.nstr(L, 25), "lam_float": Lf, "R_mp": mp.nstr(R, 12), "strict": bool(L < Lc)})
        print(out[-1], flush=True)
json.dump(out, open(os.path.join(os.path.dirname(__file__), "t5_mp.json"), "w"), indent=1)
