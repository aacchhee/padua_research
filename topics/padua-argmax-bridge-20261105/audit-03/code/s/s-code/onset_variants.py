# Planning scan [MEASURED; mpmath 30 digits on phase grids, NOT an enclosure] of simplified
# analytic-tail architectures, using only estimates already proved in the paper:
#   relative (uc:relative-comparison): S-Lc <= Ec - u*U + C4 + kx*x + ky*y  (near col. rho<=1/2, wide col. rho<=1)
#   central pair (uc:central-pair-bounds): Ec <= c x^{3/2} - Bbeta, c=3/8 (rho<=1/2) or 5/12 (rho<=1),
#       Bbeta >= 1679 y^2/8000 (rho<=1/2), Bbeta>=0 always
#   absolute gate Gabs = u(T+j) - t0 p - CbarE - KD P - ebar  (uc:global-error, origin-lower, model-loss)
#   tail floors min(Fnear,Fsmall,Fh) (r<=21/40), Fw for r<=pi/4 (ul:tail-floors)
import mpmath as mp
from abs_tail import consts, tail_floor, gabs, j, t0
mp.mp.dps = 30; pi = mp.pi
def rel_consts(c):
    n = c['n']; L = c['L']; H = 1 + L
    A4 = 4/n + 40*H/(pi*n**2); C4 = A4 + 20/n**2; db = (17*L + 27)/n**2
    JN = ((mp.mpf(3)/2)*H + mp.mpf(16)/5)/n + 78/n**2; JW = ((mp.mpf(3)/2)*H + 6)/n + 148/n**2
    kNx = ((mp.mpf(19)/2)*H + (mp.mpf(23)/3)*L + mp.mpf(677)/10)/n + 82/n**2
    kWx = ((mp.mpf(19)/2)*H + (mp.mpf(23)/3)*L + mp.mpf(155)/2)/n + 152/n**2
    return dict(A4=A4, C4=C4, JN=JN, JW=JW, kNx=kNx, kNy=kNx + db, kWx=kWx, kWy=kWx + db)
def Fw_floor(c, r):
    n = c['n']; ar = 1 - r**2/4; Ar = mp.mpf(97)/100*ar - r/2
    Iw = mp.mpf(5369)/15000*ar - mp.mpf(7379)/30000*r; Rw = mp.mpf(37621)/15000*ar - mp.mpf(3)/2*r
    Fw = mp.mpf(539)/1936*Iw - (140*Ar + 400*Rw)/(157*n) - 800*Ar/(3*n**2)
    pp = mp.mpf(22)/7; eta = ar*(1 - (4*pp + r)/n) - r/2
    Fn = 2*eta/(pp + r)*n/(n + 1)*(mp.mpf(1)/4 - 1/n); Fs = mp.mpf(35)/286*(1 - 6/n)**2*(ar - r/2)
    return min(Fn, Fs, Fw)
def floor_at(c, r):
    if r <= mp.mpf(21)/40: return max(tail_floor(c, r), Fw_floor(c, r)) if r <= pi/4 else tail_floor(c, r)
    if r <= pi/4: return Fw_floor(c, r)
    return -mp.inf
def rel_upper(c, rc, x, y, col):
    u = 1 - (mp.cos(x) + mp.cos(y))/2; rho = x + y
    if col == 'N':
        U = c['T'] - c['ebar'] + rc['A4'] + rho*rc['JN'] + j; kx, ky = rc['kNx'], rc['kNy']
    else:
        U = c['T'] - c['ebar'] + rc['A4'] + rho*rc['JW'] + j; kx, ky = rc['kWx'], rc['kWy']
    if rho <= mp.mpf(1)/2: Ec = mp.mpf(3)/8*x**mp.mpf(1.5) - mp.mpf(1679)/8000*y**2
    else: Ec = mp.mpf(5)/12*x**mp.mpf(1.5)
    return Ec - u*U + rc['C4'] + kx*x + ky*y
def scan(n, N=48):
    c = consts(n); rc = rel_consts(c)
    out = {}
    for col in ('N', 'W'):
        worst = (mp.inf, None)
        for i in range(1, N + 1):
            r = mp.mpf(i)/(2*N); fl = floor_at(c, r)
            for k in range(N + 1):
                x = r*k/N; y = r - x
                g = fl - rel_upper(c, rc, x, y, col)
                if g < worst[0]: worst = (g, float(r))
        out['halfnear_' + col] = worst
    # wide region [1/2,1]: exclusion by max(-upper, floor-upper) (noncorner) ; and primitive-only (-upper)
    worst_nc = (mp.inf, None); worst_prim_from = None
    for i in range(N + 1):
        r = mp.mpf(1)/2 + mp.mpf(i)/(2*N)
        fl = floor_at(c, r)
        mprim = mp.inf; mnc = mp.inf
        for k in range(N + 1):
            x = r*k/N; y = r - x
            up = rel_upper(c, rc, x, y, 'W')
            mprim = min(mprim, -up); mnc = min(mnc, max(-up, fl - up))
        if mnc < worst_nc[0]: worst_nc = (mnc, float(r))
        if mprim > 0 and worst_prim_from is None: worst_prim_from = float(r)
    out['wide_noncorner'] = worst_nc; out['wide_primitive_negative_from_rho'] = worst_prim_from
    # crude outer: rho in [1,pi], all centres, Gabs with uniform CbarE
    worst = (mp.inf, None)
    for i in range(N + 1):
        r = 1 + (pi - 1)*i/N
        for k in range(N + 1):
            x = r*k/N; y = r - x
            if x > pi or y > pi: continue
            g = gabs(c, x, y, c['ebar'])
            if g < worst[0]: worst = (g, float(r))
    out['outer_crude'] = worst
    return out
if __name__ == '__main__':
    for n in (300, 320, 352, 384, 416, 448, 480, 512, 640, 768, 1024):
        o = scan(n)
        print(f"n={n:5d} halfnear(nearcol)={float(o['halfnear_N'][0]):+.5f}@{o['halfnear_N'][1]:.3f} "
              f"halfnear(widecol)={float(o['halfnear_W'][0]):+.5f}@{o['halfnear_W'][1]:.3f} "
              f"wide[1/2,1]={float(o['wide_noncorner'][0]):+.4f}@{o['wide_noncorner'][1]:.3f} "
              f"primitive<0 from rho={o['wide_primitive_negative_from_rho']} "
              f"outer_crude={float(o['outer_crude'][0]):+.4f}@{o['outer_crude'][1]:.2f}")
