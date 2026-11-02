"""Extra high-precision checks: (i) codex-05 S^h(s) equals gated-02 S_n(s,0) (consistency with gated-16, outside
B's main scope); (ii) removed collision family B={r=j+1, j>=2n/3} at zero phase: F_h(0,0)>=4n/(3 pi^2) (r02 D1) and
F_0(0,0)=n; (iii) gated-03 (5) lower bounds t>=cL/m, b>=cd/m on the regular set at phases |alpha|+|beta|<=pi/48."""
import sys, random, mpmath as mp
sys.path.insert(0, sys.argv[1])
from indep_identities_lib import primitive, G, Dfour
mp.mp.dps = 40; pi = mp.pi; random.seed(13)
w = 0; minratio = mp.inf; ct = mp.inf; cb = mp.inf
for n in range(2, 10):
    m = n+1; N = n*m
    s = mp.mpf(random.uniform(-3, 3))
    Sh = mp.fsum(abs(((-1)**r*Dfour(n, j*pi/n + s/n, r*pi/m) + mp.cos(s))/2)
                 for j in range(2*n) for r in range(2*m) if (j+r) % 2)/N
    w = max(w, abs(Sh - primitive(n, s, 0)))
for n in list(range(2, 30)) + [64, 101, 200]:
    m = n+1
    for j in range(n+1):
        if j < 2*n/3: continue
        r = j+1; h = n-j
        F = (-1)**j*(Dfour(n, j*pi/n, r*pi/m) - mp.cos(n*j*pi/n))/2 if n <= 30 else None
        if F is None:
            x, y = h*pi/n, h*pi/m
            F = (1 - mp.cos(y))/(mp.cos(y) - mp.cos(x)) if h else mp.mpf(n)
        if h == 0: assert abs(F - n) < 1e-25, (n, F)
        minratio = min(minratio, F/(4*n/(3*pi**2)))
for n in (5, 8, 13, 40):
    m = n+1
    for j in range(n+1):
        for r in range(m+1):
            if (j+r) % 2 == 0 or (r == j+1 and j >= 2*n/3): continue
            L = abs(j-r); d = min(j+r, 2*n+1-j-r)
            for (al, be) in ((pi/48, 0), (-pi/48, 0), (0, pi/48), (0, -pi/48), (pi/96, pi/96), (pi/96, -pi/96), (-pi/96, pi/96), (-pi/96, -pi/96)):
                u, v = j*pi/n + al/n, r*pi/m + be/m
                ct = min(ct, abs(mp.sin((u-v)/2))/(L/mp.mpf(m))); cb = min(cb, mp.sin((u+v)/2)/(d/mp.mpf(m)))
print('max|S^h(s)-S_n(s,0)| =', mp.nstr(w, 3))
print('min F_h(0,0)/(4n/(3pi^2)) over B family =', mp.nstr(minratio, 8))
print('min t/(L/m) =', mp.nstr(ct, 6), ' min b/(d/m) =', mp.nstr(cb, 6))
