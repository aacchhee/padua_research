"""Refinement 2: direct I quadrature with all kink breakpoints (pi/2, pi/2-e); E11(2) slack for x>0."""
import mpmath as mp
src = open('m2-code/e10_e11_central_check.py').read().split('out = []')[0]
exec(src)
mp.mp.dps = 30
def I_direct2(C, D, e):
    C, D, e = mp.mpf(C), mp.mpf(D), mp.mpf(e)
    f = lambda x: abs(C*mp.cot(x)+D*mp.cot(x+e)) - abs(C*mp.cot(x)) - abs(D*mp.cot(x+e))
    pts = [mp.mpf(0), pi-e, pi, pi/2, pi/2-e if pi/2-e > 0 else pi/2]
    r = (D-C)*mp.sin(e)/(C+D)
    if abs(r) <= 1:
        th = mp.asin(r)
        for k in range(-2, 3):
            for cand in [(th-e)/2+k*pi/1, (pi-th-e)/2+k*pi]:
                if 0 < cand < pi: pts.append(cand)
    pts = sorted(set(pts))
    return mp.quad(f, pts, maxdegree=10)
mx = 0
for (u, s, e) in [(0.3, 0.1, 0.7), (0.3, 0.5, 0.4), (0.3, 0.5, 1.2), (0.2, 1.3, 0.1), (0.45, 0.46, 0.05), (0.1, 0.9, 1.5)]:
    d = abs(J(u, s, e) - I_direct2((u-s)/2, (u+s)/2, e)); mx = max(mx, d)
print("max |J_closed - I_direct (all kinks as breakpoints)|:", mp.nstr(mx, 5))
mp.mp.dps = 20
I4 = mp.quad(lambda t: mp.sqrt(1-t**4), [0, 1]); kap = 4*I4/pi**2
def phase(x, y):
    x, y = mp.mpf(x), mp.mpf(y); return (mp.cos(x)+mp.cos(y))/2, mp.sin(x), mp.sin(y)
def Ec(x, y):
    a, p, q = phase(x, y); v = p/2; dl = q/2; b = 2*mp.atan(dl/a)
    def ig(e):
        s0 = a*mp.tan(e/2); return J(v, s0+dl, e)+J(v, abs(s0-dl), e)-4*s0*mp.log(mp.sin(e))
    pts = [mp.mpf(0)] + ([b] if 0 < b < pi/2 else []) + [pi/2]
    return mp.quad(ig, pts)/pi**2
def Bb(x, y):
    a, p, q = phase(x, y)
    if q == 0: return mp.mpf(0)
    b = 2*mp.atan(q/(2*a)); return 4/pi**2*mp.quad(lambda e: (q/2-a*mp.tan(e/2))*(-mp.log(mp.sin(e))), [0, b])
N = 12; worst = (-mp.inf, None)
for i in range(1, N+1):
    for j in range(N+1-i):
        x = (pi/2)*i/N; y = (pi/2)*j/N
        a, p, q = phase(x, y); rhs = kap*p**mp.mpf(1.5)/mp.sqrt(a) - Bb(x, y); ec = Ec(x, y)
        r = (ec-rhs)/(kap*p**mp.mpf(1.5)/mp.sqrt(a))
        if r > worst[0]: worst = (r, (x, y))
print("E11(2): max over x>0 grid pts (N=12, closed rho<=pi/2) of (Ec-rhs)/(kappa p^1.5/sqrt a):", mp.nstr(worst[0], 6), "at", [mp.nstr(z, 6) for z in worst[1]], "(<0 expected)")
