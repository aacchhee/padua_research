# ENCLOSED (python-flint arb balls, rigorous elementary functions) check of the proposed
# "architecture B" gates, using ONLY quantities defined/proved in the paper. This is a planning
# enclosure at the base degrees; the all-n monotone transfers are NOT proved here (listed as obligations).
import flint
from flint import arb
flint.ctx.prec = 200
pi = arb.pi()
def A(x): return arb(x)
def F(p, q): return arb(p)/arb(q)
j, t0 = F(23, 250), F(221, 500)          # paper: j>23/250, t0<221/500
def consts(n):
    n = A(n); m = n + 1; L = n.log(); H = 1 + L
    T = (4*L**2 - 3*L)/pi**2; b0 = 4/pi**2; r0 = F(5, 2).log() + F(1, 18)
    D = ((52/pi**2)*H + 7)/n + 10/n**2 + 20*H/(pi*n**2)
    Mm = b0*(2*L + 2*r0)/n + (4 + b0*(L + 1/n))/(4*n**2 - 1) + b0/(2*n - 1)**2 \
         + (5 + b0*((n + F(1, 2)).log() + 2))/(4*(n - F(1, 2))**2)
    ebar = D + Mm + 1/n
    KD = ((6 + 16/(3*pi))*H + 2/pi)/n
    gn = 1 + (2 + 8*m/(3*pi)).log(); MA = 1/pi + 4/pi**2
    Gg = (7*MA*L + F(111, 2) + (63 + A(2).log() + 4*pi.log() + 7*m.log() + 16*(2*m).log() + F(3, 2)*gn)/pi)/m
    Wn = (3*m.log() + A(2).log() + 2*pi.log() + 2)/(pi*m)
    CE = D + Gg + (64 + 16*L)/n + 318/n**2 + Mm + Wn
    A4 = 4/n + 40*H/(pi*n**2); C4 = A4 + 20/n**2; db = (17*L + 27)/n**2
    kWx = (F(19, 2)*H + F(23, 3)*L + F(155, 2))/n + 152/n**2; kWy = kWx + db
    Mnorm = (4*L**2 + F(79, 5)*L)/pi**2 + F(9, 4) + CE + 2*KD
    return dict(n=n, L=L, T=T, ebar=ebar, KD=KD, CE=CE, C4=C4, A4=A4, kWx=kWx, kWy=kWy, M=Mnorm)
def show(name, x, thr=None):
    s = f'{name:58s} = [{float(x.lower()):+.6f}, {float(x.upper()):+.6f}]'
    if thr is not None: s += f'   > {thr}: {bool(x.lower() > arb(thr) if not isinstance(thr, arb) else x.lower() > thr.upper())}'
    print(s)
# (B1)+(B2): one wide polynomial P(rho) on rho<=1 (u>=11(x^2+y^2)/48, Ec<=5x^{3/2}/12, sqrt x<=x+1/4, Bbeta>=0)
def wide_poly(c):
    U = c['T'] - c['ebar'] + c['A4'] + j            # drop rho*J_W >= 0
    l1 = c['kWx'] + F(5, 48); l2 = c['kWy']
    d1 = F(11, 48)*U - F(5, 12); d2 = F(11, 48)*U
    e = d1*d2/(d1 + d2); f = (d2*l1 + d1*l2)/(d1 + d2); g = (l1 - l2)**2/(4*(d1 + d2))
    return e, f, g
print('--- architecture B at N0=512 ---')
c = consts(512); e, f, g = wide_poly(c)
show('B1 near: 1/20 - (C4+g+f^2/(4e))  [noncorner rho<=1/2]', F(1, 20) - (c['C4'] + g + f**2/(4*e)), 0)
show('B2 wide: -P(1/2) [all centres, 1/2<=rho<=1]', -(c['C4'] + g + f/2 - e/4), 0)
show('B2 vertex f/(2e) (<1/2 => P decreasing on [1/2,1])', f/(2*e))
u1 = F(47, 384)  # 1-cos(1/2) > 47/384 (paper)
show('B3 outer crude: u1(T+j)-t0-CbarE-2KD-ebar [rho>=1]', u1*(c['T'] + j) - t0 - c['CE'] - 2*c['KD'] - c['ebar'], 0)
def closed_gate(c, rho1):
    TJ = c['T'] + j; s, co = (rho1/2).sin(), (rho1/2).cos()
    Aa = TJ*co + (t0 + 2*c['KD'])*s; Bb = t0*co
    return TJ - (Aa**2 + Bb**2).sqrt() - c['CE'] - c['ebar']
show('B3'' outer closed form G(512, rho1=1)', closed_gate(c, A(1)), 0)
# (B5) floors at 512, r=1/2: F_near, F_small, F_h from (ul:tail-floors)
def tail_floors(c, r):
    n = c['n']; r = arb(r); ar = 1 - r**2/4; pp = F(22, 7)
    eta = ar*(1 - (4*pp + r)/n) - r/2
    Fn = 2*eta/(pp + r)*n/(n + 1)*(F(1, 4) - 1/n)
    Fs = F(35, 286)*(1 - 6/n)**2*(ar - r/2)
    Ar = F(97, 100)*ar - r/2
    Ih = F(2303, 5000)*ar - F(471, 1250)*r; Rh = F(4837, 1875)*ar - F(5, 3)*r
    Fh = F(539, 1936)*Ih - (140*Ar + 400*Rh)/(157*n) - 800*Ar/(3*n**2)
    return Fn, Fs, Fh
Fn, Fs, Fh = tail_floors(c, F(1, 2))
show('B5 F_near(512,1/2)', Fn, F(1, 20)); show('B5 F_small(512,1/2)', Fs, F(1, 20)); show('B5 F_h(512,1/2)', Fh, F(1, 20))
# corner256 with absolute-only errors at 512 (would allow dropping relative column if the engine switched at 512)
h = pi/4
def gabs(c, x, y):
    u = 1 - (x.cos() + y.cos())/2; p = x.sin(); P = x.sin() + y.sin()
    return u*(c['T'] + j) - t0*p - c['CE'] - c['KD']*P - c['ebar']
dA = gabs(c, h, A(0)); dA2 = gabs(c, A(0), h); dD = gabs(c, h, h)
for nm, val in (('dA(h,0)', dA), ('dA(0,h)', dA2), ('dD/2', dD/2)):
    show(f'corner absolute at 512: {nm} - M pi^4/6144', val - c['M']*pi**4/6144, 0)
print('--- far192 by the closed-form uniform gate ---')
for n in (192, 256, 320):
    cc = consts(n)
    show(f'G({n}, rho1=pi/2) (certificates need > 3/100)', closed_gate(cc, pi/2), F(3, 100))
print('--- scalar values for the report ---')
for n in (192, 256, 320, 384, 512):
    cc = consts(n); print(f"n={n}: CbarE~{float(cc['CE'].mid()):.4f} ebar~{float(cc['ebar'].mid()):.4f} "
                          f"KD~{float(cc['KD'].mid()):.4f} T~{float(cc['T'].mid()):.4f} M~{float(cc['M'].mid()):.3f}")
