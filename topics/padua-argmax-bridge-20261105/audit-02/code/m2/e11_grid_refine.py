"""Refinement: per-sample J validation at higher precision, and E11 (2) slack excluding origin
on closed rho<=pi/2 (incl. axes, rho=pi/2 edge). Sampled numerics; not a proof."""
import mpmath as mp
src = open('m2-code/e10_e11_central_check.py').read().split('out = []')[0]
exec(src)
mp.mp.dps = 30
for (u, s, e) in [(0.3, 0.1, 0.7), (0.3, 0.5, 0.4), (0.3, 0.5, 1.2), (0.2, 1.3, 0.1), (0.45, 0.46, 0.05), (0.1, 0.9, 1.5)]:
    print("J vs I_direct", (u, s, e), mp.nstr(J(u, s, e), 12), mp.nstr(I_direct((u-s)/2, (u+s)/2, e), 12))
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
N = 12; worst = (-mp.inf, None); minslack_rel = mp.inf
for i in range(N+1):
    for j in range(N+1-i):
        if i == 0 and j == 0: continue
        x = (pi/2)*i/N; y = (pi/2)*j/N
        a, p, q = phase(x, y); bb = Bb(x, y)
        rhs = kap*p**mp.mpf(1.5)/mp.sqrt(a) - bb; ec = Ec(x, y)
        if ec - rhs > worst[0]: worst = (ec-rhs, (x, y), ec, rhs)
print("E11(2) max slack Ec-rhs excluding origin, closed rho<=pi/2 N=12:", mp.nstr(worst[0], 6), "at", [mp.nstr(z, 6) for z in worst[1]], "Ec=", mp.nstr(worst[2], 8), "rhs=", mp.nstr(worst[3], 8))
# tiny-phase and edge points
for (x, y) in [(mp.mpf('1e-6'), 0), (mp.mpf('1e-6'), mp.mpf('1e-6')), (0, mp.mpf('1e-6')), (pi/2, 0), (pi/4, pi/4), (0, pi/2), (mp.mpf('1e-3'), pi/2-mp.mpf('1e-3'))]:
    a, p, q = phase(x, y); bb = Bb(x, y); rhs = kap*p**mp.mpf(1.5)/mp.sqrt(a) - bb; ec = Ec(x, y)
    print("point", (mp.nstr(x, 4), mp.nstr(y, 4)), "Ec-rhs=", mp.nstr(ec-rhs, 6), "Ec=", mp.nstr(ec, 8))
