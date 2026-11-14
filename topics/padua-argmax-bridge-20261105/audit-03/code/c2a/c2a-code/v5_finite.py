# C2A audit: finite-row items in lines 1465-2050
import math, numpy as np
from scipy import special
pi = math.pi; EG = 0.5772156649015329
def Cc(t): return -special.digamma(t)-special.digamma(1-t)
# (1) pole-error: |B_n(t)/n - (2L+C(t)-2log pi)/pi| <= 5/n^2 ; also weighted by sin(pi t)
worst = 0; wpt = None
for n in list(range(2, 80))+[100, 128, 160, 199, 256, 320, 500, 1000]:
    ts = np.linspace(1e-4, 1-1e-4, 801)
    k = np.arange(n)
    for t in ts:
        Bn = np.sum(np.abs(1/np.tan(pi*(k+t)/n)))
        err = abs(Bn/n-(2*math.log(n)+Cc(t)-2*math.log(pi))/pi)*n**2
        if err > worst: worst = err; wpt = (n, t)
print('pole-error: max n^2*|err| =', round(worst, 4), 'at', wpt, '(claimed <5; component sum pi^2/3+pi/4+1/(2pi)=%.4f)' % (pi**2/3+pi/4+1/(2*pi)))
# (2) paired tail braces <= 1/(3k^3)
mx = 0
for kk in range(1, 200):
    for t in np.linspace(0, 1, 101):
        br = 2*math.log(1+1/kk)-1/(kk+t)-1/(kk+1-t)
        mx = max(mx, abs(br)*3*kk**3)
print('paired tail |brace|*3k^3 max =', round(mx, 4))
# (3) c''(w) formula and -c''(pi/2)=16/pi^3
for w in [0.3, 1.0, pi/2]:
    cpp = 2/math.tan(w)/math.sin(w)**2-2/w**3
    ser = -4*w*sum((3*pi**2*j**2+w**2)/(pi**2*j**2-w**2)**3 for j in range(1, 200000))
    print("c''(%.3f) direct %.10f series %.10f" % (w, cpp, ser))
print('16/pi^3 =', 16/pi**3)
# (4) half-line defect for reference (-w,w): |sum_{v+h(k+t)<pi/2} cot(v+h(k+t)) + log sin v/h - (log d - psi(d+t))/h| <= 4/pi
mx = 0; mpt = None
for n in [32, 64, 160, 400]:
    h = pi/n
    for v in np.linspace(0.3*h, pi/2-0.3*h, 157):
        d = v/h
        for t in np.linspace(0.001, 0.999, 41):
            kmax = int(math.floor((pi/2-v)/h-t))
            ks = np.arange(0, kmax+1)
            ks = ks[v+h*(ks+t) < pi/2]
            S = np.sum(1/np.tan(v+h*(ks+t)))
            val = abs(S+math.log(math.sin(v))/h-(math.log(d)-special.digamma(d+t))/h)
            if val > mx: mx = val; mpt = (n, v, t)
print('half-line defect max =', round(mx, 5), 'at', mpt, ' 4/pi =', round(4/pi, 5))
# (5) psi estimate 0 <= log w - 1/(2w) - psi(w) <= 1/(8w^2)
ws = np.geomspace(0.05, 1e4, 2000)
r = np.log(ws)-1/(2*ws)-special.digamma(ws)
print('psi estimate: min', r.min(), ' max ratio to 1/(8w^2)', np.max(r*8*ws**2))
# (6) row identity (-1)^delta G_n(u,v)/2 = C cot((u-v)/2)+D cot((u+v)/2), and offsets = eta_-/+ mod 1
def Gn(n, u, v):
    nu = lambda p: 1 if p == 0 else 2
    s = 0.0
    for p in range(n+1):
        for q in range(n+1-p):
            s += nu(p)*nu(q)*math.cos(p*u)*math.cos(q*v)
    return s-math.cos(n*u)
n = 7; m = n+1
maxdev = 0; maxoff = 0
for (x, y) in [(0.3, 0.7), (1.1, 0.2), (0.05, 2.9)]:
    ce = math.cos((x+y)/2); cd = math.cos((x-y)/2); a = ce*cd; p = math.sin(x); q = math.sin(y)
    for r_ in range(2*m):
        dl = (1-r_) % 2
        vr = (r_*pi+y)/m
        cot2 = 1/math.tan(vr/2)
        C = (p-q-2*a*cot2)/4; D = (p+q+2*a*cot2)/4
        em = 0.5+(x-y+vr)/(2*pi); ep = 0.5+(x+y-vr)/(2*pi)
        for k in range(n):
            u = (dl*pi+x+2*k*pi)/n
            lhs = (-1)**dl*Gn(n, u, vr)/2
            rhs = C/math.tan((u-vr)/2)+D/math.tan((u+vr)/2)
            maxdev = max(maxdev, abs(lhs-rhs))
        # fractional offsets: (u-v)/2 = pi(k+t-)/n , (u+v)/2 = pi(k'+t+)/n  (mod pi)
        u0 = (dl*pi+x)/n
        tm = ((u0-vr)/2*n/pi) % 1; tp = ((u0+vr)/2*n/pi) % 1
        # compare with eta_- mod 1 and with 1-eta_+ mod 1 (cot((u+v)/2) has offset pole at -v)
        maxoff = max(maxoff, min(abs(tm-(em % 1)), 1-abs(tm-(em % 1))))
        maxoff_p = min(abs(tp-((1-ep) % 1)), 1-abs(tp-((1-ep) % 1)))
        maxoff = max(maxoff, maxoff_p)
print('row identity max deviation (n=7):', maxdev, ';  max |offset - eta| mod 1:', maxoff)
# (7) telescope singular sample identity
n = 37; m = n+1; a = 0.83; U0 = 1.234; t = 0.31
L = math.log(n); B0 = 4*a/pi**2; D0 = U0/pi+B0*math.log(pi); Zn = D0-B0*math.log(m/n)
mx = 0
for k in range(2, m-1):
    zz = pi*(k+t)/m
    lhs = (U0+(4*a/pi)*(L+math.log(zz)))/zz/m
    rhs = Zn/(k+t)+B0*math.log(k+t)/(k+t)
    mx = max(mx, abs(lhs-rhs))
print('singular-sample identity max dev:', mx)
# (8) Sigma_{r not in A6} |cot(v_r/2)| <= 4 m H_n / pi ; and including A6 rows
for n in [32, 100]:
    m = n+1; Hn = sum(1/j for j in range(1, n+1))
    for y in [1e-6, 0.5, pi-1e-6]:
        rs = [r for r in range(2*m) if r not in (0, 1, 2*m-2, 2*m-1, m-1, m)]
        s_ord = sum(abs(1/math.tan((r*pi+y)/(2*m))) for r in rs)
        s_all = sum(abs(1/math.tan((r*pi+y)/(2*m))) for r in range(2*m))
        print('n=%d y=%.2g: sum over r not in A6 = %.2f, all rows = %.3g, bound 4mH_n/pi = %.2f' % (n, y, s_ord, s_all, 4*m*Hn/pi))
