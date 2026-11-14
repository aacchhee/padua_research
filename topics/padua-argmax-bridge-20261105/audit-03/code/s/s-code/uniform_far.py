# [MEASURED planning] Is the phase-dependent allowance (uc:phase-allowance) needed?
# Test the absolute gate with the UNIFORM CbarE but exact u,p,P on the far half rho in [pi/2,pi] (far192 domain),
# and on rho in [1,pi] (outer domain); also the max of the wide relative upper on rho<=1/2 (for uniform floors),
# and the wide polynomial sign on [1/2,1] with the paper-style relaxations (u>=11(x^2+y^2)/48, sqrt x<=x+1/4).
import mpmath as mp
from abs_tail import consts, gabs, j, t0
from onset_variants import rel_consts, rel_upper
mp.mp.dps = 30; pi = mp.pi
def min_gate(c, rlo, rhi, N=60):
    w = (mp.inf, None)
    for i in range(N + 1):
        r = rlo + (rhi - rlo)*i/N
        for k in range(N + 1):
            x = r*k/N; y = r - x
            if x > pi or y > pi: continue
            g = gabs(c, x, y, c['ebar'])
            if g < w[0]: w = (g, (float(x), float(y)))
    return w
def wide_upper_max(c, rc, rmax, N=60):
    w = -mp.inf
    for i in range(1, N + 1):
        r = rmax*i/N
        for k in range(N + 1):
            x = r*k/N; y = r - x
            w = max(w, rel_upper(c, rc, x, y, 'W'))
    return w
def wide_poly(c, rc, rho):
    U = c['T'] - c['ebar'] + rc['A4'] + j   # drop rho*JW>=0
    l1 = rc['kWx'] + mp.mpf(5)/48; l2 = rc['kWy']
    d1 = mp.mpf(11)/48*U - mp.mpf(5)/12; d2 = mp.mpf(11)/48*U
    e = d1*d2/(d1 + d2); f = (d2*l1 + d1*l2)/(d1 + d2); g = (l1 - l2)**2/(4*(d1 + d2))
    return rc['C4'] - e*rho**2 + f*rho + g
for n in (192, 200, 224, 256, 320, 384, 448, 512, 640, 768, 1024):
    c = consts(n); rc = rel_consts(c)
    gf = min_gate(c, pi/2, pi); go = min_gate(c, mp.mpf(1), pi)
    wm = wide_upper_max(c, rc, mp.mpf(1)/2)
    print(f"n={n:5d} CbarE={float(c['CE']):.3f} far[pi/2,pi] uniform gate={float(gf[0]):+.4f} at {gf[1][0]:.2f},{gf[1][1]:.2f}  "
          f"outer[1,pi]={float(go[0]):+.4f}  max wide-upper(rho<=1/2)={float(wm):.4f}  "
          f"widepoly(1/2)={float(wide_poly(c, rc, mp.mpf(1)/2)):+.4f}")
