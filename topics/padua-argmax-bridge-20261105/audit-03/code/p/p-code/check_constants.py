"""Referee checks of Section 4 scalar constants (MEASURED, mpmath 40 digits).
Checks the displayed rational bounds at the base degrees 320 (near, annulus,
outer), 256 (corner), 192 (far), the scalar profile lemma, the origin identity
(uc:origin-identity) and selected-pair floor algebra. Not a proof.
"""
import math, time
import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 40
t0 = time.process_time()
pi, g_, ln = mp.pi, mp.euler, mp.log
R = lambda p, q: mp.mpf(p) / q
out = []
def chk(name, val, op, bound):
    ok = (val < bound) if op == '<' else (val > bound)
    out.append((name, mp.nstr(val, 10), op, mp.nstr(bound, 10), 'OK' if ok else 'FAIL'))

kappa = mp.mpf('0.91971011838849253509951822579')
C0 = 2 * g_ + 4 * ln(2)
k0 = C0 - 2 * ln(pi)
H0 = kappa / 2 + (2 * k0 / pi**2) * ln(2 / pi)
bstar = C0 - R(7, 2)
Bc = C0**2 / pi**2
d0 = C0 * bstar / pi**2
v0 = 7 * bstar / (2 * pi**2)
g0 = 4 * (ln(pi)**2 - ln(2)**2) / pi**2
j = H0 + d0 - g0
t0c = 2 * ln(2) / pi
chk('H0>7/25', H0, '>', R(7, 25)); chk('H0<1633/5125', H0, '<', R(1633, 5125))
chk('d0>39/250', d0, '>', R(39, 250)); chk('g0<43/125', g0, '<', R(43, 125))
chk('j>23/250', j, '>', R(23, 250)); chk('t0<221/500', t0c, '<', R(221, 500))
dd = g_ + ln(8 / pi)
Cstar_corner = 4 * dd**2 / pi**2 + kappa
Cstar_model = Bc - g0 + 2 * H0
out.append(('C* corner vs model (identity is the definition of H0 via kappa)', mp.nstr(Cstar_corner - Cstar_model, 5)))

# ---- scalar profile f and finite part H, independent of kappa ----
def Ccal(t): return -mp.digamma(t) - mp.digamma(1 - t)
def Phi(t):
    t = t - mp.floor(t)
    if t == 0: return mp.mpf(1)
    return mp.sin(pi * t) / pi * (Ccal(t) - 2 * ln(pi))
def f(w): return Phi(R(1, 2) + w / (2 * pi))
lam0 = 2 / pi * ln(4 / pi)
def Hfin(w):
    fw = f(w)
    I = mp.quad(lambda t: (f(w + t) + f(w - t) - 2 * fw) / (2 * mp.sin(t / 2)), [0, pi / 2, pi - mp.mpf('1e-30'), pi] if False else [0, pi / 4, pi / 2, pi])
    return lam0 * fw + I / pi
H0direct = Hfin(mp.mpf(0))
out.append(('H0 direct finite part', mp.nstr(H0direct, 15), 'H0 from kappa', mp.nstr(H0, 15), 'diff', mp.nstr(H0direct - H0, 3)))
# f bounds on a grid
ws = [-pi + 2 * pi * i / 400 for i in range(401)]
fv = [f(w) for w in ws]
chk('min f>1/2', min(fv), '>', R(1, 2)); chk('max f<=1(+eps)', max(fv), '<', 1 + mp.mpf('1e-30'))
lip = max(abs(fv[i + 1] - fv[i]) / (2 * pi / 400) for i in range(400))
chk('Lip f<2', lip, '<', 2)
g2 = max(abs(mp.diff(f, w, 2)) for w in ws[1:-1:4])
chk('|f\'\'|<1 (interior)', g2, '<', 1)
g3 = max(abs(mp.diff(f, w, 3)) for w in ws[2:-2:8])
chk('|f\'\'\'|<13/20', g3, '<', R(13, 20))
Hgrid = [Hfin(w) for w in [pi * i / 16 for i in range(1, 17)]]
chk('max_w H(w) - H0 <= 0 (grid w=k pi/16)', max(Hgrid) - H0direct, '<', mp.mpf('1e-25'))
J0 = 2 * (ln(pi) - g_) / pi
chk('J0>1/pi', J0, '>', 1 / pi)
chk('f(0)<3/5', f(0), '<', R(3, 5))

# ---- uc:constants and phase allowances ----
def base(n):
    n = mp.mpf(n); m = n + 1; L = ln(n); H = 1 + L
    T = (4 * L**2 - 3 * L) / pi**2; b0 = 4 / pi**2; r0 = ln(R(5, 2)) + R(1, 18)
    D = ((52 / pi**2) * H + 7) / n + 10 / n**2 + 20 * H / (pi * n**2)
    Mm = b0 * (2 * L + 2 * r0) / n + (4 + b0 * (L + 1 / n)) / (4 * n**2 - 1) + b0 / (2 * n - 1)**2 + (5 + b0 * (ln(n + R(1, 2)) + 2)) / (4 * (n - R(1, 2))**2)
    ebar = D + Mm + 1 / n
    KD = ((6 + 16 / (3 * pi)) * H + 2 / pi) / n
    A4 = 4 / n + 40 * H / (pi * n**2); C4 = A4 + 20 / n**2; dbeta = (17 * L + 27) / n**2
    JN = (R(3, 2) * H + R(16, 5)) / n + 78 / n**2; JW = (R(3, 2) * H + 6) / n + 148 / n**2
    kNx = (R(19, 2) * H + R(23, 3) * L + R(677, 10)) / n + 82 / n**2; kNy = kNx + dbeta
    kWx = (R(19, 2) * H + R(23, 3) * L + R(155, 2)) / n + 152 / n**2; kWy = kWx + dbeta
    Wn = (3 * ln(m) + ln(2) + 2 * ln(pi) + 2) / (pi * m)
    gn = 1 + ln(2 + 8 * m / (3 * pi)); MA = 1 / pi + 4 / pi**2
    Gg = (7 * MA * L + R(111, 2) + (63 + ln(2) + 4 * ln(pi) + 7 * ln(m) + 16 * ln(2 * m) + R(3, 2) * gn) / pi) / m
    CEbar = D + Gg + (64 + 16 * L) / n + 318 / n**2 + Mm + Wn
    Mn = (4 * L**2 + R(79, 5) * L) / pi**2 + R(9, 4) + CEbar + 2 * KD
    return dict(n=n, m=m, L=L, H=H, T=T, b0=b0, r0=r0, D=D, M=Mm, ebar=ebar, KD=KD, A4=A4, C4=C4, dbeta=dbeta,
                JN=JN, JW=JW, kNx=kNx, kNy=kNy, kWx=kWx, kWy=kWy, Wn=Wn, CEbar=CEbar, Mn=Mn)

b = base(320)
chk('L320>57679/10000', b['L'], '>', R(57679, 10000)); chk('L320<5769/1000', b['L'], '<', R(5769, 1000))
chk('T>293/25', b['T'], '>', R(293, 25)); chk('D<27/200', b['D'], '<', R(27, 200)); chk('M<7/400', b['M'], '<', R(7, 400))
chk('ebar<249/1600', b['ebar'], '<', R(249, 1600)); chk('C4<677/50000', b['C4'], '<', R(677, 50000))
chk('kNx<11031/20000', b['kNx'], '<', R(11031, 20000)); chk('kNy<11056/20000', b['kNy'], '<', R(11056, 20000))
chk('kNx<705963/1280000', b['kNx'], '<', R(705963, 1280000)); chk('kNy<56602113/102400000', b['kNy'], '<', R(56602113, 102400000))
UN0 = b['T'] - b['ebar'] + b['A4'] + j
chk('U_N(rho=0)>23337/2000', UN0, '>', R(23337, 2000)); chk('J_N>21/500', b['JN'], '>', R(21, 500))
chk('kWx<583/1000', b['kWx'], '<', R(583, 1000)); chk('kWy<117/200', b['kWy'], '<', R(117, 200))
chk('T-ebar+j>2331/200', b['T'] - b['ebar'] + j, '>', R(2331, 200))
# monotonicity in real n of the near costs and U_N (sampled)
ns = [320 * 1.05**i for i in range(0, 200)]
mono = True
prev = None
for nn in ns:
    bb = base(nn)
    vec = (bb['kNx'], bb['kNy'], bb['C4'], bb['kWx'], bb['kWy'], -(bb['T'] - bb['ebar'] + bb['A4'] + j), -(bb['T'] - bb['ebar'] + bb['A4'] + R(1, 2) * bb['JN'] + j))
    if prev and any(v > p + mp.mpf('1e-30') for v, p in zip(vec, prev)): mono = False
    prev = vec
out.append(('near costs decrease / U_N increase on sampled n>=320', mono))

# near quadratic
ell1, ell2, d1, d2 = R(12531, 20000), R(11056, 20000), R(1911, 800), R(24539, 8000)
UNlow = R(23337, 2000) + R(21, 500) * R(1, 8)
chk('d1 from (47/192)U_N-15/32 at rho>=1/8', R(47, 192) * UNlow - R(15, 32), '>', d1)
chk('d2 from (47/192)U_N+1679/8000', R(47, 192) * UNlow + R(1679, 8000), '>', d2)
chk('ell1 = kNx+3/40', b['kNx'] + R(3, 40), '<', ell1)
e = d1 * d2 / (d1 + d2); fq = (d2 * ell1 + d1 * ell2) / (d1 + d2); gq = (ell1 - ell2)**2 / (4 * (d1 + d2))
chk('e>13429/10000', e, '>', R(13429, 10000)); chk('f<29714/50000', fq, '<', R(29714, 50000)); chk('g<1/4000', gq, '<', R(1, 4000))
out.append(('integer ineq 34161^2 < 32*8233*4431', 34161**2, 32 * 8233 * 4431, 34161**2 < 32 * 8233 * 4431))
# rho<=1/8 claim
d_ = 2; e2 = Fr(1); f2 = (Fr(12531, 20000) + Fr(11056, 20000)) / 2; g2q = (Fr(12531, 20000) - Fr(11056, 20000))**2 / 16
val = Fr(677, 50000) + g2q + f2 * Fr(1, 8) - e2 * Fr(1, 64)
out.append(('rho<=1/8: S-Lc bound at rho=1/8', float(val), '<77/1000', val < Fr(77, 1000)))
Lh = lambda r: Fr(5123, 50000) - Fr(4447, 50000) * r - Fr(1281, 50000) * r * r
out.append(('L_h(1/8)>9/100', float(Lh(Fr(1, 8))), Lh(Fr(1, 8)) > Fr(9, 100)))
# A_h, B_h exact
Ah = Fr(1241317, 9680000) - Fr(679, 251200) - Fr(77392, 3768000) - Fr(97, 38400)
Bh = Fr(253869, 2420000) - Fr(35, 25120) - Fr(2000, 150720) - Fr(1, 768)
out.append(('A_h', float(Ah), Fr(5123, 50000) < Ah < Fr(1281, 12500), 'B_h', float(Bh), 0 < Bh < Fr(4447, 50000)))
# F_h coefficients recomputed from the lemma's F_h definition at n=320
n = 320
cA = Fr(539, 1936) * Fr(2303, 5000) - (140 * Fr(97, 100) + 400 * Fr(4837, 1875)) / (157 * n) - 800 * Fr(97, 100) / (3 * n * n)
cB = Fr(539, 1936) * Fr(471, 1250) - (140 * Fr(1, 2) + 400 * Fr(5, 3)) / (157 * n) - 800 * Fr(1, 2) / (3 * n * n)
out.append(('F_h coeffs from lemma == displayed A_h,B_h', cA == Ah, cB == Bh))
cAw = Fr(539, 1936) * Fr(5369, 15000) - (140 * Fr(97, 100) + 400 * Fr(37621, 15000)) / (157 * n) - 800 * Fr(97, 100) / (3 * n * n)
cBw = Fr(539, 1936) * Fr(7379, 30000) - (140 * Fr(1, 2) + 400 * Fr(3, 2)) / (157 * n) - 800 * Fr(1, 2) / (3 * n * n)
Aw = Fr(2893891, 29040000) - Fr(679, 251200) - Fr(75242, 3768000) - Fr(97, 38400)
Bw = Fr(3977281, 58080000) - Fr(35, 25120) - Fr(15, 1256) - Fr(1, 768)
out.append(('F_w coeffs from lemma == displayed A_w,B_w', cAw == Aw, cBw == Bw, float(Aw), float(Bw), Fr(37, 500) < Aw < Fr(3, 40), 0 < Bw < Fr(27, 500)))
aw = lambda r: 1 - r * r / 4
out.append(('F_w(3/5) >= 697/20000', float(Fr(37, 500) * aw(Fr(3, 5)) - Fr(27, 500) * Fr(3, 5)), Fr(37, 500) * aw(Fr(3, 5)) - Fr(27, 500) * Fr(3, 5) >= Fr(697, 20000)))
Fh2140 = Ah * aw(Fr(21, 40)) - Bh * Fr(21, 40)
out.append(('F_h(21/40) > 17/500 (A_h,B_h exact)', float(Fh2140), Fh2140 > Fr(17, 500)))
# wide quadratic
e3 = Fr(9, 4) * Fr(8, 3) / (Fr(9, 4) + Fr(8, 3)); f3 = (Fr(8, 3) * Fr(11, 16) + Fr(9, 4) * Fr(47, 80)) / (Fr(9, 4) + Fr(8, 3)); g3q = (Fr(11, 16) - Fr(47, 80))**2 / (4 * (Fr(9, 4) + Fr(8, 3)))
out.append(('wide e,f,g', e3 == Fr(72, 59), f3 == Fr(3029, 4720), g3q == Fr(3, 5900)))
P = lambda r: Fr(141, 10000) + Fr(257, 400) * r - Fr(61, 50) * r * r
out.append(('P(1/2),P(3/5)', P(Fr(1, 2)) == Fr(607, 20000), P(Fr(3, 5)) == Fr(-99, 2500)))
chk('kWx+5/48<11/16', b['kWx'] + R(5, 48), '<', R(11, 16)); chk('kWy<47/80', b['kWy'], '<', R(47, 80))
chk('(11/48)(T-ebar+j)-5/12>9/4', R(11, 48) * (b['T'] - b['ebar'] + j) - R(5, 12), '>', R(9, 4))
chk('(11/48)(T-ebar+j)>8/3', R(11, 48) * (b['T'] - b['ebar'] + j), '>', R(8, 3))
chk('C4+g<141/10000', b['C4'] + R(3, 5900), '<', R(141, 10000))
# F_near, F_small at n=320, r=3/5
def Fnear(n, r, ppi=R(22, 7)):
    a = 1 - r * r / 4; eta = a * (1 - (4 * ppi + r) / n) - r / 2
    return 2 * eta / (ppi + r) * n / (n + 1) * (R(1, 4) - R(1, n))
def Fsmall(n, r):
    a = 1 - r * r / 4; return R(35, 286) * (1 - R(6, n))**2 * (a - r / 2)
chk('F_near(320,3/5)>549/10000', Fnear(320, R(3, 5)), '>', R(549, 10000)); chk('F_small(320,3/5)>549/10000', Fsmall(320, R(3, 5)), '>', R(549, 10000))
mn = min((Fnear(320, r) - R(11, 100) * (1 - r * r / 4 - r / 2)) for r in [R(i, 200) for i in range(101)])
chk('min_{r<=1/2}(F_near-(11/100)(a-r/2)) at 320', mn, '>', 0)
mn = min((Fsmall(320, r) - R(11, 100) * (1 - r * r / 4 - r / 2)) for r in [R(i, 200) for i in range(101)])
chk('min_{r<=1/2}(F_small-(11/100)(a-r/2)) at 320', mn, '>', 0)

# finite floor exact margins
E = lambda n: Fr(245931, 6050000) - Fr(206, 157 * n) - Fr(55, 3 * n * n)
out.append(('E64-1/64', E(64) - Fr(1, 64) == Fr(34466881, 729484800000), 'E160-1/32', E(160) - Fr(1, 32) == Fr(88079689, 182371200000)))
# band raw values at r=1/2, c=5/4, [pi/20,pi/4]
r = R(1, 2); a = 1 - r * r / 4; C = a - r / 2; a0, b0b = pi / 20, pi / 4
I = C * (b0b - a0) + a * (mp.cos(b0b) - mp.cos(a0)); A0 = C - a * mp.sin(a0)
Rr = C * ln(mp.tan(b0b / 2) / mp.tan(a0 / 2)) - a * (b0b - a0)
chk('I>21/125', I, '>', R(21, 125)); chk('A0<11/20', A0, '<', R(11, 20)); chk('R<14/25', Rr, '<', R(14, 25))
chk('log ratio<5/3', ln(mp.tan(b0b / 2) / mp.tan(a0 / 2)), '<', R(5, 3))
Tc = 4 - 2 * R(5, 4) + 4 * ln(R(5, 4)); chk('T_c>239/100', Tc, '>', R(239, 100)); chk('T_c<12/5', Tc, '<', R(12, 5))
chk('full arc 7/8(29/492)^2>1/512', R(7, 8) * R(29, 492)**2, '>', R(1, 512))
chk('class1 37/(224(pi+1/2))>1/32', R(37, 224) / (pi + R(1, 2)), '>', R(1, 32))
chk('class1 225/(1040(pi+1/2))>1/20', R(225, 1040) / (pi + R(1, 2)), '>', R(1, 20))
chk('class2 33/(16 pi sqrt3)(1/6-1/41)', R(33, 16) / (pi * mp.sqrt(3)) * (R(1, 6) - R(1, 41)), '>', R(35, 656))
chk('35/656>1/20', R(35, 656), '>', R(1, 20))

# ---- outer gate at n=320 ----
n = mp.mpf(320); m = n + 1; L = b['L']; H = b['H']
u1 = R(47, 384); a0o = R(337, 384); w0 = R(721, 384); p0 = R(12, 25); P0 = R(24, 25); eta = R(3, 2)
chk('u1 <= 1-cos(1/2)', u1, '<', 1 - mp.cos(R(1, 2)))
eps_ = 3 * pi / (2 * m); ell = -ln(mp.sin(eps_)); Da = b['D'] - 10 / n**2; Cc = 1 + 8 * a0o * m / (3 * pi)
Gb = p0 * (1 + ln(1 + Cc / p0)); gb = 1 + ln(1 + Cc / p0) - Cc / (p0 + Cc)
Mb = p0 / pi + 4 * a0o / pi**2; CBb = 6 + (4 + 4 * a0o / mp.e) / pi
Vb = 23 + (3 * Gb + (2 * p0 + 6 * P0) * ell + 26 * a0o + 20) / pi
Gbb = 7 * L * Mb / m + Vb / (2 * m) + 2 * CBb / m + (4 / m) * (7 + (P0 / pi) * (5 + 2 * ln(2 * m)))
Rb = (21 + 21 * a0o + 2 * L + ((1 + 48 * p0) * H + 24 * p0) / pi) / n + (317 + R(5, 12)) / n**2
b0 = 4 / pi**2; r0 = ln(R(5, 2)) + R(1, 18)
Db = 4 * w0 / pi + a0o * b0 * ln(pi); Zb = Db + a0o * b0 / n
Mcb = a0o * b0 * (2 * L + 2 * r0) / n + (Db + a0o * b0 * (L + 1 / n)) / (4 * n**2 - 1) + a0o * b0 / (2 * n - 1)**2 + (Zb + a0o * b0 * (ln(n + R(1, 2)) + 2)) / (4 * (n - R(1, 2))**2)
Cb = a0o * Da + 10 / n**2 + Gbb + Rb + Mcb
Cs = eta * (7 * L / (pi * m) + (3 * gb + 2 * ell) / (2 * pi * m) + (48 * H + 24) / (pi * n)) + 3 * ((ln(2) + 4 * ln(pi)) / (pi * m) + b['Wn'])
Cl = (12 * ell + 16 * (5 + 2 * ln(2 * m))) / (pi * m)
js, ts = R(23, 250), R(221, 500)
G = u1 * (b['T'] + js) - ts * p0 - Cb - P0 * b['KD'] - b['ebar']
K = b['T'] + js - Cl - 4 * b['KD']; Aout = eta * ts + Cs
for nm_, v_, op, bd in [('K_D<1/6', b['KD'], '<', R(1, 6)), ('W_n<3/125', b['Wn'], '<', R(3, 125)), ('ell<13/3', ell, '<', R(13, 3)),
                        ('Gamma_b<18/5', Gb, '<', R(18, 5)), ('gamma_b<15/2', gb, '<', R(15, 2)), ('M_b<13/25', Mb, '<', R(13, 25)),
                        ('C_Bb<8', CBb, '<', 8), ('a0Da+10/n^2<3/25', a0o * Da + 10 / n**2, '<', R(3, 25)), ('G_b<9/25', Gbb, '<', R(9, 25)),
                        ('R_b<17/50', Rb, '<', R(17, 50)), ('Mcal_b<2/125', Mcb, '<', R(2, 125)), ('C_b<209/250', Cb, '<', R(209, 250)),
                        ('C_s<141/200', Cs, '<', R(141, 200)), ('C_l<7/20', Cl, '<', R(7, 20)), ('G>195191/2400000', G, '>', R(195191, 2400000)),
                        ('K>10', K, '>', 10), ('A<7/5', Aout, '<', R(7, 5)), ('gap G-A^2/(4K)>13/500 (from bounds)', R(3, 40) - R(49, 1000), '>', R(13, 500) - mp.mpf('1e-40')),
                        ('actual G-A^2/4K', G - Aout**2 / (4 * K), '>', R(13, 500)),
                        ('sqrt(33887)/192<P0', mp.sqrt(33887) / 192, '<', P0), ('slope 674/sqrt33887<4', 674 / mp.sqrt(33887), '<', 4),
                        ('sin(1/2)<p0', mp.sin(R(1, 2)), '<', p0), ('cos(1/2)<a0', mp.cos(R(1, 2)), '<', a0o),
                        ('sin eps>23/(5m)', mp.sin(eps_), '>', R(23, 5) / m)]:
    chk('outer320 ' + nm_, v_, op, bd)
chk('j_* < j', R(23, 250), '<', j); chk('t_0<t_*', t0c, '<', ts)
# outer gate monotone in n (sampled)
def outer_gap(nv):
    bb = base(nv); n = mp.mpf(nv); m = n + 1; L = bb['L']; H = bb['H']
    eps_ = 3 * pi / (2 * m); ell = -ln(mp.sin(eps_)); Da = bb['D'] - 10 / n**2; Cc = 1 + 8 * a0o * m / (3 * pi)
    Gb = p0 * (1 + ln(1 + Cc / p0)); gb = 1 + ln(1 + Cc / p0) - Cc / (p0 + Cc)
    Vb = 23 + (3 * Gb + (2 * p0 + 6 * P0) * ell + 26 * a0o + 20) / pi
    Gbb = 7 * L * Mb / m + Vb / (2 * m) + 2 * CBb / m + (4 / m) * (7 + (P0 / pi) * (5 + 2 * ln(2 * m)))
    Rb = (21 + 21 * a0o + 2 * L + ((1 + 48 * p0) * H + 24 * p0) / pi) / n + (317 + R(5, 12)) / n**2
    Zb = Db + a0o * b0 / n
    Mcb = a0o * b0 * (2 * L + 2 * r0) / n + (Db + a0o * b0 * (L + 1 / n)) / (4 * n**2 - 1) + a0o * b0 / (2 * n - 1)**2 + (Zb + a0o * b0 * (ln(n + R(1, 2)) + 2)) / (4 * (n - R(1, 2))**2)
    Cb = a0o * Da + 10 / n**2 + Gbb + Rb + Mcb
    Cs = eta * (7 * L / (pi * m) + (3 * gb + 2 * ell) / (2 * pi * m) + (48 * H + 24) / (pi * n)) + 3 * ((ln(2) + 4 * ln(pi)) / (pi * m) + bb['Wn'])
    Cl = (12 * ell + 16 * (5 + 2 * ln(2 * m))) / (pi * m)
    G = u1 * (bb['T'] + js) - ts * p0 - Cb - P0 * bb['KD'] - bb['ebar']; K = bb['T'] + js - Cl - 4 * bb['KD']; A = eta * ts + Cs
    return G - A**2 / (4 * K), G, K
gaps = [outer_gap(320 * 1.1**i)[0] for i in range(0, 80)]
out.append(('outer gap min over sampled n>=320 (needs >13/500=0.026)', mp.nstr(min(gaps), 8)))
out.append(('outer gap at n=319,300,256 (onset check, not claimed)', [mp.nstr(outer_gap(k)[0], 6) for k in (319, 300, 256, 200)]))

# ---- corner 256 ----
c = base(256)
q0 = R(7, 48); h = pi / 4; rU = R(2, 125)
dA = q0 * (c['T'] - c['ebar'] + j) - R(1, 4) - c['C4'] - h * c['kWy']
dD = 2 * q0 * (c['T'] + j) - R(4, 15) - c['CEbar'] - R(3, 2) * c['KD'] - c['ebar']
for nm_, v_, op, bd in [('L256>277/50', c['L'], '>', R(277, 50)), ('T>107/10', c['T'], '>', R(107, 10)), ('ebar<1/5', c['ebar'], '<', R(1, 5)),
                        ('KD<1/5', c['KD'], '<', R(1, 5)), ('CEbar<3/2', c['CEbar'], '<', R(3, 2)), ('C4<9/500', c['C4'], '<', R(9, 500)),
                        ('kWy<93/100', c['kWy'], '<', R(93, 100)), ('M(256)<26', c['Mn'], '<', 26), ('rU>pi^4/6144', rU, '>', pi**4 / 6144),
                        ('dA-rU M>2729/21000', dA - rU * c['Mn'], '>', R(2729, 21000)), ('dD-2rU M>49/1000', dD - 2 * rU * c['Mn'], '>', R(49, 1000)),
                        ('(1-cos h)/2>q0', (1 - mp.cos(h)) / 2, '>', q0), ('E_c diag (4I4/pi^2)/sqrt2<4/15', 4 * mp.quad(lambda t: mp.sqrt(1 - t**4), [0, 1]) / pi**2 / mp.sqrt(2), '<', R(4, 15)),
                        ('I4<319/360', mp.quad(lambda t: mp.sqrt(1 - t**4), [0, 1]), '<', R(319, 360)), ('(16/pi^2)(49/2000)>1/30', 16 / pi**2 * R(49, 2000), '>', R(1, 30))]:
    chk('corner256 ' + nm_, v_, op, bd)
def corner_gate(nv):
    c = base(nv)
    dA = q0 * (c['T'] - c['ebar'] + j) - R(1, 4) - c['C4'] - h * c['kWy']
    dD = 2 * q0 * (c['T'] + j) - R(4, 15) - c['CEbar'] - R(3, 2) * c['KD'] - c['ebar']
    return min(dA, dD / 2) - c['Mn'] * pi**4 / 6144
cg = [corner_gate(256 * 1.1**i) for i in range(80)]
out.append(('corner gate min sampled n>=256 (needs >49/2000)', mp.nstr(min(cg), 6)))

# ---- far 192 ----
f1 = base(192); n = mp.mpf(192); m = n + 1; L = f1['L']; H = f1['H']
u0 = R(7, 24); Au = 1 - u0; Cu = 2 - u0; Fu = 2 * mp.sqrt(u0 * (1 - u0)); Qu = mp.sqrt(8 * u0)
eps_ = 3 * pi / (2 * m); ell = -ln(mp.sin(eps_))
Dhat = Au * (f1['D'] - 10 / n**2) + 10 / n**2
Gam = Fu * (1 + ln(1 + (1 + 8 * Au * m / (3 * pi)) / Fu))
MA = Fu / pi + 4 * Au / pi**2; CB = 6 + (4 + 4 * Au / mp.e) / pi
VB = 23 + (3 * Gam + (2 * Fu + 6 * Qu) * ell + 26 * Au + 20 + 2 * Fu * ln(2)) / pi
Ghat = (L * 2 * MA + VB) / (2 * m) + 6 * L * MA / m + (4 / m) * (7 + (Qu / pi) * (5 + 2 * ln(2 * m))) + 4 * Fu * ln(pi) / (pi * m) + 2 * CB / m
C6 = (21 + 21 * Au + 2 * L + ((1 + 48 * Fu) * H + 24 * Fu) / pi) / n + (317 + R(5, 12)) / n**2
Dbar = 4 * Cu / pi + Au * b0 * ln(pi); Zbar = Dbar + Au * b0 / n
Mhat = Au * b0 * (2 * L + 2 * r0) / n + (Dbar + Au * b0 * (L + 1 / n)) / (4 * n**2 - 1) + Au * b0 / (2 * n - 1)**2 + (Zbar + Au * b0 * (ln(n + R(1, 2)) + 2)) / (4 * (n - R(1, 2))**2)
CE = Dhat + Ghat + C6 + Mhat + Fu * f1['Wn']
for nm_, v_, op, bd in [('L192>21/4', L, '>', R(21, 4)), ('L<421/80', L, '<', R(421, 80)), ('H<63/10', H, '<', R(63, 10)), ('T>19/2', f1['T'], '>', R(19, 2)),
                        ('ebar<1/4', f1['ebar'], '<', R(1, 4)), ('KD<13/50', f1['KD'], '<', R(13, 50)), ('Dhat<4/25', Dhat, '<', R(4, 25)),
                        ('Ghat<7/10', Ghat, '<', R(7, 10)), ('C6hat<31/40', C6, '<', R(31, 40)), ('Mhat<1/50', Mhat, '<', R(1, 50)),
                        ('F W_n<1/30', Fu * f1['Wn'], '<', R(1, 30)), ('CEhat<17/10', CE, '<', R(17, 10)), ('F<11/12', Fu, '<', R(11, 12)), ('Q<31/20', Qu, '<', R(31, 20)),
                        ('cos(pi/4)<17/24', mp.cos(pi / 4), '<', R(17, 24))]:
    chk('far192 ' + nm_, v_, op, bd)
anchor = Fr(7, 24) * (Fr(19, 2) + Fr(23, 250)) - Fr(221, 500) * Fr(11, 12) - Fr(17, 10) - Fr(13, 50) * Fr(31, 20) - Fr(1, 4)
out.append(('far192 anchor == 79/2000', anchor == Fr(79, 2000)))
actual_anchor = u0 * (f1['T'] + j) - t0c * Fu - CE - f1['KD'] * Qu - f1['ebar']
out.append(('far192 actual anchor (with true j,t0)', mp.nstr(actual_anchor, 8)))
out.append(('cpu_s', time.process_time() - t0))
for row in out:
    print(*row)
