"""Independent interval re-evaluation of the E13/E14-outer320, E15-far192 and
E12-corner256 scalar envelopes.  Auditor: Claude Opus 5.5 xhigh (m3).
Uses mpmath.iv outward interval arithmetic (rigorous enclosures of every
transcendental input).  Formulas are re-typed from the theory files, not
imported from repository code.  Run:
  PYTHONPATH=<audit2>/pylib python3 -P envelopes.py
"""
import sys
from fractions import Fraction as Fr
from mpmath import iv, mp
iv.prec = 200

PI = iv.pi
E = iv.e
def I(x):
    if isinstance(x, Fr):
        return iv.mpf(x.numerator) / iv.mpf(x.denominator)
    return iv.mpf(x)
def lt(x, q):  # rigorous x<q
    return x.b < I(q).a
def gt(x, q):
    return x.a > I(q).b
def fmt(x):
    return '[%s, %s]' % (mp.nstr(mp.mpf(x.a), 12), mp.nstr(mp.mpf(x.b), 12))

ok_all = True
def check(name, cond, x=None):
    global ok_all
    ok_all &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name + ('' if x is None else '  ' + fmt(x)))

def common(n):
    n = I(n); m = n + 1; L = iv.log(n); H = 1 + L
    b = 4 / PI**2; r = iv.log(I(Fr(5, 2))) + I(Fr(1, 18))
    Da = ((52 / PI**2) * H + 7) / n + 20 * H / (PI * n**2)
    KD = ((6 + 16 / (3 * PI)) * H + 2 / PI) / n
    eps = 3 * PI / (2 * m); ell = -iv.log(iv.sin(eps))
    W = (3 * iv.log(m) + iv.log(2) + 2 * iv.log(PI) + 2) / (PI * m)
    T = (4 * L**2 - 3 * L) / PI**2
    D = Da + 10 / n**2
    Mesh = (b * (2 * L + 2 * r) / n + (4 + b * (L + 1 / n)) / (4 * n**2 - 1)
            + b / (2 * n - 1)**2 + (5 + b * (iv.log(n + I(Fr(1, 2))) + 2)) / (4 * (n - I(Fr(1, 2)))**2))
    ebar = D + Mesh + 1 / n
    return dict(n=n, m=m, L=L, H=H, b=b, r=r, Da=Da, KD=KD, eps=eps, ell=ell,
                W=W, T=T, D=D, Mesh=Mesh, ebar=ebar)

# ---------------- E13 / E14-outer320 ----------------
u1 = I(Fr(47, 384)); a0 = I(Fr(337, 384)); w0 = I(Fr(721, 384))
p0 = I(Fr(12, 25)); P0 = I(Fr(24, 25)); eta = I(Fr(3, 2))
js = I(Fr(23, 250)); ts = I(Fr(221, 500))

def e13(n):
    c = common(n); n_, m, L, H, b, r = c['n'], c['m'], c['L'], c['H'], c['b'], c['r']
    ell, W, KD = c['ell'], c['W'], c['KD']
    C = 1 + 8 * a0 * m / (3 * PI)
    Gb_ = p0 * (1 + iv.log(1 + C / p0))
    gb = 1 + iv.log(1 + C / p0) - C / (p0 + C)
    MA = p0 / PI + 4 * a0 / PI**2
    VB = 23 + (3 * Gb_ + (2 * p0 + 6 * P0) * ell + 26 * a0 + 20) / PI
    CB = 6 + (4 + 4 * a0 / E) / PI
    Genv = 7 * L * MA / m + VB / (2 * m) + (4 / m) * (7 + (P0 / PI) * (5 + 2 * iv.log(2 * m))) + 2 * CB / m
    Denv = a0 * c['Da'] + 10 / n_**2
    R6 = (21 + 21 * a0 + 2 * L + ((1 + 48 * p0) * H + 24 * p0) / PI) / n_ + I(Fr(317 * 12 + 5, 12)) / n_**2
    Dm = 4 * w0 / PI + a0 * b * iv.log(PI); Zm = Dm + a0 * b / n_
    Menv = (a0 * b * (2 * L + 2 * r) / n_ + (Dm + a0 * b * (L + 1 / n_)) / (4 * n_**2 - 1)
            + a0 * b / (2 * n_ - 1)**2 + (Zm + a0 * b * (iv.log(n_ + I(Fr(1, 2))) + 2)) / (4 * (n_ - I(Fr(1, 2)))**2))
    Cb = Denv + Genv + R6 + Menv
    Cs = eta * (7 * L / (PI * m) + (3 * gb + 2 * ell) / (2 * PI * m) + (48 * H + 24) / (PI * n_)) \
        + 3 * ((iv.log(2) + 4 * iv.log(PI)) / (PI * m) + W)
    Cl = (12 * ell + 16 * (5 + 2 * iv.log(2 * m))) / (PI * m)
    Gb = u1 * (c['T'] + js) - ts * p0 - Cb - P0 * KD - c['ebar']
    K = c['T'] + js - Cl - 4 * KD
    A = eta * ts + Cs
    F = Gb - A**2 / (4 * K)
    c.update(C=C, Gamma_b=Gb_, gamma_b=gb, MA_b=MA, VB_b=VB, CB_b=CB, G_env=Genv, D_env=Denv,
             R6_env=R6, M_env=Menv, Cb=Cb, Cs=Cs, Cl=Cl, Gb=Gb, K=K, A=A, F=F)
    return c

print('== E14-outer320 written component bounds at n=320 (E13 formulas) ==')
c = e13(320)
for key, q, sense in [('L', Fr(57679, 10000), '>'), ('L', Fr(5769, 1000), '<'), ('H', Fr(677, 100), '<'),
                      ('T', Fr(293, 25), '>'), ('D', Fr(27, 200), '<'), ('Mesh', Fr(7, 400), '<'),
                      ('ebar', Fr(5, 32), '<'), ('ebar', Fr(249, 1600), '<'), ('KD', Fr(1, 6), '<'),
                      ('W', Fr(3, 125), '<'), ('ell', Fr(13, 3), '<'),
                      ('Gamma_b', Fr(18, 5), '<'), ('gamma_b', Fr(15, 2), '<'), ('MA_b', Fr(13, 25), '<'),
                      ('CB_b', Fr(8), '<'), ('D_env', Fr(3, 25), '<'), ('VB_b', Fr(50), '<'),
                      ('G_env', Fr(9, 25), '<'), ('R6_env', Fr(17, 50), '<'), ('M_env', Fr(2, 125), '<'),
                      ('Cb', Fr(209, 250), '<'), ('Cs', Fr(71, 100), '<'), ('Cl', Fr(7, 20), '<'),
                      ('Gb', Fr(3, 40), '>'), ('K', Fr(10), '>'), ('A', Fr(7, 5), '<'), ('F', Fr(13, 500), '>')]:
    x = c[key]
    check('n=320 %s %s %s' % (key, sense, q), lt(x, q) if sense == '<' else gt(x, q), x)
# log m, log 2m
check('n=320 log m < 289/50', lt(iv.log(c['m']), Fr(289, 50)), iv.log(c['m']))
check('n=320 log 2m < 13/2', lt(iv.log(2 * c['m']), Fr(13, 2)), iv.log(2 * c['m']))
check('n=320 1+C/p0<2m', lt(1 + c['C'] / p0 - 2 * c['m'], 0))
# Cs pieces
m = c['m']; L = c['L']; H = c['H']; n_ = c['n']
check('7L/(pi m)<41/1000', lt(7 * L / (PI * m), Fr(41, 1000)), 7 * L / (PI * m))
check('(3gb+2ell)/(2pi m)<2/125', lt((3 * c['gamma_b'] + 2 * c['ell']) / (2 * PI * m), Fr(2, 125)))
check('(48H+24)/(pi n)<353/1000', lt((48 * H + 24) / (PI * n_), Fr(353, 1000)), (48 * H + 24) / (PI * n_))
check('(log2+4logpi)/(pi m)<3/500', lt((iv.log(2) + 4 * iv.log(PI)) / (PI * m), Fr(3, 500)))
# exact rational chain of E14 (2)-(5)
g_num = Fr(47, 384) * (Fr(293, 25) + Fr(23, 250)) - Fr(221, 500) * Fr(12, 25) - Fr(209, 250) - Fr(4, 25) - Fr(5, 32)
print('E14 Gb rational numerator =', g_num, '; claimed 195191/2400000 ->', g_num == Fr(195191, 2400000), '; >3/40:', g_num > Fr(3, 40))
check('E14 Gb numerator equals 195191/2400000', g_num == Fr(195191, 2400000))
Klow = Fr(293, 25) + Fr(23, 250) - Fr(7, 20) - Fr(2, 3)
check('E14 K lower %s > 10' % Klow, Klow > 10)
Aup = Fr(3, 2) * Fr(221, 500) + Fr(71, 100)
check('E14 A upper %s < 7/5' % Aup, Aup < Fr(7, 5))
Flow = Fr(3, 40) - Fr(7, 5)**2 / 40
check('E14 F lower %s == 13/500' % Flow, Flow == Fr(13, 500))
Cbsum = Fr(3, 25) + Fr(9, 25) + Fr(17, 50) + Fr(2, 125)
check('E14 Cb sum %s == 209/250' % Cbsum, Cbsum == Fr(209, 250))
check('E14 Cs (3/2)(41/100)+3(3/500+3/125)=141/200', Fr(3, 2) * Fr(41, 100) + 3 * (Fr(3, 500) + Fr(3, 125)) == Fr(141, 200))
print('n=320 exact-interval F =', fmt(c['F']), ' Gb', fmt(c['Gb']), ' K', fmt(c['K']), ' A', fmt(c['A']))

# monotone sanity scan (measurement, not proof) of E13 components on n>=320
print('== E13 envelope direction scan (measurement) ==')
prev = None; mono = True
ns = [320, 321, 330, 384, 400, 512, 640, 1000, 1024, 2048, 4096, 10**4, 10**5, 10**6, 10**8, 10**12]
for nn in ns:
    cc = e13(nn)
    row = {k: mp.mpf(cc[k].mid) for k in ('Cb', 'Cs', 'Cl', 'KD', 'ebar', 'T', 'Gb', 'K', 'A', 'F')}
    if prev:
        for k in ('Cb', 'Cs', 'Cl', 'KD', 'ebar', 'A'):
            if not row[k] < prev[k]: mono = False; print('non-decrease', k, nn)
        for k in ('T', 'Gb', 'K', 'F'):
            if not row[k] > prev[k]: mono = False; print('non-increase', k, nn)
    prev = row
    print('n=%-14d F=%s Gb=%s K=%s A=%s' % (nn, mp.nstr(row['F'], 8), mp.nstr(row['Gb'], 8), mp.nstr(row['K'], 8), mp.nstr(row['A'], 8)))
check('E13 sampled directions (Cb,Cs,Cl,KD,ebar,A down; T,Gb,K,F up) on scan', mono)
# where does the E13 gate first close with these constants (measurement only)
lo_n = None
for nn in range(200, 321):
    cc = e13(nn)
    if cc['K'].a > 0 and cc['F'].a > 0:
        lo_n = nn; break
print('measurement: smallest n in [200,320] with rigorous K>0,F>0 for E13+ebar(j*,t*):', lo_n)

# ---------------- E15 far192 ----------------
print('== E15 CEhat(192,7/24) and gate ==')
def e15(n, u):
    c = common(n); n_, m, L, H, b, r = c['n'], c['m'], c['L'], c['H'], c['b'], c['r']
    u = I(u); A = 1 - u; Cc = 2 - u
    Fv = 2 * iv.sqrt(u * (1 - u)) if u.b <= 0.5 else I(1)
    Q = iv.sqrt(8 * u) if (8 * u).b <= 4 else I(2)
    ell, W, KD = c['ell'], c['W'], c['KD']
    Dhat = A * c['Da'] + 10 / n_**2
    Gam = Fv * (1 + iv.log(1 + (1 + 8 * A * m / (3 * PI)) / Fv))
    MA = Fv / PI + 4 * A / PI**2
    VB = 23 + (3 * Gam + (2 * Fv + 6 * Q) * ell + 26 * A + 20 + 2 * Fv * iv.log(2)) / PI
    CB = 6 + (4 + 4 * A / E) / PI
    G = 7 * L * MA / m + VB / (2 * m) + (4 / m) * (7 + (Q / PI) * (5 + 2 * iv.log(2 * m))) + 4 * Fv * iv.log(PI) / (PI * m) + 2 * CB / m
    C6 = (21 + 21 * A + 2 * L + ((1 + 48 * Fv) * H + 24 * Fv) / PI) / n_ + I(Fr(3809, 12)) / n_**2
    Db = 4 * Cc / PI + A * b * iv.log(PI); Zb = Db + A * b / n_
    M = (A * b * (2 * L + 2 * r) / n_ + (Db + A * b * (L + 1 / n_)) / (4 * n_**2 - 1) + A * b / (2 * n_ - 1)**2
         + (Zb + A * b * (iv.log(n_ + I(Fr(1, 2))) + 2)) / (4 * (n_ - I(Fr(1, 2)))**2))
    CE = Dhat + G + C6 + M + Fv * W
    Gn = u * (c['T'] + js) - ts * Fv - CE - KD * Q - c['ebar']
    c.update(Dhat=Dhat, Gammahat=Gam, MAhat=MA, VBhat=VB, CBhat=CB, Ghat=G, C6hat=C6, Mhat=M, FW=Fv * W,
             CEhat=CE, Gn=Gn, Fv=Fv, Q=Q)
    return c
c = e15(192, Fr(7, 24))
for key, q, sense in [('L', Fr(657, 125), '>'), ('L', Fr(421, 80), '<'), ('H', Fr(63, 10), '<'), ('T', Fr(19, 2), '>'),
                      ('D', Fr(43, 200), '<'), ('Dhat', Fr(4, 25), '<'), ('Mesh', Fr(7, 250), '<'), ('ebar', Fr(1, 4), '<'),
                      ('KD', Fr(13, 50), '<'), ('ell', Fr(4), '<'), ('Gammahat', Fr(13, 2), '<'), ('MAhat', Fr(3, 5), '<'),
                      ('VBhat', Fr(57), '<'), ('CBhat', Fr(8), '<'), ('Ghat', Fr(7, 10), '<'), ('C6hat', Fr(31, 40), '<'),
                      ('Mhat', Fr(1, 50), '<'), ('FW', Fr(1, 30), '<'), ('CEhat', Fr(17, 10), '<'),
                      ('Fv', Fr(11, 12), '<'), ('Q', Fr(31, 20), '<'), ('Gn', Fr(79, 2000), '>')]:
    x = c[key]
    check('E15 n=192,u0 %s %s %s' % (key, sense, q), lt(x, q) if sense == '<' else gt(x, q), x)
g_rat = Fr(7, 24) * (Fr(19, 2) + Fr(23, 250)) - Fr(221, 500) * Fr(11, 12) - Fr(17, 10) - Fr(13, 50) * Fr(31, 20) - Fr(1, 4)
check('E15 rational G_192(u0) chain = %s == 79/2000' % g_rat, g_rat == Fr(79, 2000))
check('E15 CEhat sum 4/25+7/10+31/40+1/50+1/30 = %s' % (Fr(4, 25) + Fr(7, 10) + Fr(31, 40) + Fr(1, 50) + Fr(1, 30)),
      Fr(4, 25) + Fr(7, 10) + Fr(31, 40) + Fr(1, 50) + Fr(1, 30) == Fr(1013, 600))
check('E15 cos(pi/4)<17/24 (24^2<2*17^2)', 24**2 < 2 * 17**2)
check('E15 sqrt119/12<11/12', 119 < 121)
check('E15 7/3<(31/20)^2', Fr(7, 3) < Fr(31, 20)**2)
# u-quotient monotonicity sanity: G_192(u)/u increasing on a u grid in [7/24,1]
ok = True; prev = None
us = [Fr(7, 24) + Fr(k, 200) * (1 - Fr(7, 24)) for k in range(201)] + [Fr(1, 2)]
us = sorted(set(us))
vals = []
for uu in us:
    g = e15(192, uu)['Gn']; q = mp.mpf((g / I(uu)).mid); vals.append((uu, q))
for (u_a, qa), (u_b, qb) in zip(vals, vals[1:]):
    if not qb > qa: ok = False; print('quotient non-increase', u_a, u_b)
check('E15 G_192(u)/u increasing on 202-point u grid (measurement)', ok)
print('  min G_192(u) on grid ~', mp.nstr(min(mp.mpf(e15(192, uu)['Gn'].a) for uu in us), 8))
# n-direction sanity of G_n(u0)
ok = True; prev = None
for nn in [192, 193, 200, 256, 320, 384, 512, 1024, 10**4, 10**6, 10**9]:
    g = mp.mpf(e15(nn, Fr(7, 24))['Gn'].mid)
    if prev is not None and not g > prev: ok = False
    prev = g
check('E15 G_n(u0) increasing on n scan (measurement; proof uses fixed-phase CEphi)', ok)
# where would the same anchor first close (measurement only)
first = None
for nn in range(150, 193):
    if e15(nn, Fr(7, 24))['Gn'].a > 0: first = nn; break
print('measurement: smallest n in [150,192] with rigorous G_n(7/24)>0:', first)

# ---------------- E12 corner256 ----------------
print('== E12-corner256 at n=256 ==')
def e12(n):
    c = common(n); n_, m, L, H, b = c['n'], c['m'], c['L'], c['H'], c['b']
    MA = 1 / PI + 4 / PI**2
    g = 1 + iv.log(2 + 8 * m / (3 * PI))
    VBg = 23 + (3 * g + 14 * iv.log(m) + 46 + 2 * iv.log(2)) / PI
    Gg = 7 * L * MA / m + VBg / (2 * m) + (4 / m) * (7 + (2 / PI) * (5 + 2 * iv.log(2 * m))) + 4 * iv.log(PI) / (PI * m) + 16 / m
    Gg2 = (7 * MA * L + I(Fr(111, 2)) + (63 + iv.log(2) + 4 * iv.log(PI) + 7 * iv.log(m) + 16 * iv.log(2 * m) + I(Fr(3, 2)) * g) / PI) / m
    six = (64 + 16 * L) / n_ + 318 / n_**2
    CEbar = c['D'] + Gg + six + c['Mesh'] + c['W']
    A4 = 4 / n_ + 40 * H / (PI * n_**2); C4 = A4 + 20 / n_**2
    kWy = ((I(19) / 2) * H + 15 * L + I(265) / 3) / n_ + (179 + 17 * L) / n_**2
    Mn = (4 * L**2 + I(Fr(79, 5)) * L) / PI**2 + I(Fr(9, 4)) + CEbar + 2 * c['KD']
    q0 = I(Fr(7, 48)); rU = I(Fr(2, 125)); h = PI / 4
    dA = q0 * (c['T'] - c['ebar'] + js) - I(Fr(1, 4)) - C4 - h * kWy
    dD = 2 * q0 * (c['T'] + js) - I(Fr(4, 15)) - CEbar - I(Fr(3, 2)) * c['KD'] - c['ebar']
    FA = dA - rU * Mn; FD = dD - 2 * rU * Mn
    delta = iv.mpf([min(dA.a, (dD / 2).a), min(dA.b, (dD / 2).b)])
    coef = (16 / PI**2) * (delta - Mn * PI**4 / 6144)
    c.update(Gg=Gg, Gg2=Gg2, six=six, CEbar=CEbar, A4=A4, C4=C4, kWy=kWy, M=Mn, dA=dA, dD=dD, FA=FA, FD=FD, coef=coef)
    return c
c = e12(256)
check('E12 Gg collected form equals defining form', abs(mp.mpf((c['Gg'] - c['Gg2']).mid)) < 1e-40)
for key, q, sense in [('L', Fr(277, 50), '>'), ('L', Fr(111, 20), '<'), ('H', Fr(131, 20), '<'), ('T', Fr(107, 10), '>'),
                      ('D', Fr(1, 6), '<'), ('Gg', Fr(5, 8), '<'), ('six', Fr(61, 100), '<'), ('Mesh', Fr(11, 500), '<'),
                      ('W', Fr(7, 250), '<'), ('CEbar', Fr(3, 2), '<'), ('ebar', Fr(1, 5), '<'), ('KD', Fr(1, 5), '<'),
                      ('C4', Fr(9, 500), '<'), ('kWy', Fr(93, 100), '<'), ('M', Fr(26), '<'),
                      ('dA', Fr(2293, 4200), '>'), ('FA', Fr(1, 8), '>'), ('dD', Fr(881, 1000), '>'), ('FD', Fr(49, 1000), '>'),
                      ('coef', Fr(1, 30), '>')]:
    x = c[key]
    check('E12 n=256 %s %s %s' % (key, sense, q), lt(x, q) if sense == '<' else gt(x, q), x)
check('E12 rU=2/125>pi^4/6144', lt(PI**4 / 6144, Fr(2, 125)))
check('E12 125*22^4<2*7^4*6144', 125 * 22**4 < 2 * 7**4 * 6144)
check('E12 delta_A rational chain', Fr(2317, 1500) - Fr(1, 4) - Fr(9, 500) - Fr(1023, 1400) == Fr(2293, 4200))
check('E12 q0*(107/10-1/5+23/250)=2317/1500', Fr(7, 48) * (Fr(107, 10) - Fr(1, 5) + Fr(23, 250)) == Fr(2317, 1500))
check('E12 (11/14)(93/100)=1023/1400', Fr(11, 14) * Fr(93, 100) == Fr(1023, 1400))
check('E12 FA chain', Fr(2293, 4200) - Fr(52, 125) == Fr(2729, 21000))
check('E12 2q0(107/10+23/250)=9443/3000', 2 * Fr(7, 48) * (Fr(107, 10) + Fr(23, 250)) == Fr(9443, 3000))
check('E12 delta_D chain', Fr(9443, 3000) - Fr(4, 15) - Fr(3, 2) - Fr(3, 10) - Fr(1, 5) == Fr(881, 1000))
check('E12 FD chain', Fr(881, 1000) - Fr(104, 125) == Fr(49, 1000))
check('E12 (8/5)(49/2000)=49/1250>1/30', Fr(8, 5) * Fr(49, 2000) == Fr(49, 1250) and Fr(49, 1250) > Fr(1, 30))
check('E12 8(q0-rU)=779/750', 8 * (Fr(7, 48) - Fr(2, 125)) == Fr(779, 750))
check('E12 3q0+(79/5)rU=6903/10000', 3 * Fr(7, 48) + Fr(79, 5) * Fr(2, 125) == Fr(6903, 10000))
check('E12 kappa bound 4*(319/360)/(197/20)=638/1773<9/25', 4 * Fr(319, 360) / Fr(197, 20) == Fr(638, 1773) and Fr(638, 1773) < Fr(9, 25))
check('E12 axis Ec<(9/25)*(3/5)/(9/10)=6/25', Fr(9, 25) * Fr(3, 5) / Fr(9, 10) == Fr(6, 25))
check('E12 diag kappa/sqrt2 < 9/35', lt(I(Fr(9, 25)) / iv.sqrt(2), Fr(9, 35)))
# hybrid checker equivalence: q=32*min(dA,dD/2), t=M pi^4/192 -> delta>M pi^4/6144
check('hybrid corner criterion with u=v=1/32 equals delta>M pi^4/6144', Fr(1, 32) / 6 / 32 == Fr(1, 6144))
ok = True; prev = None
for nn in [256, 257, 300, 320, 384, 512, 1024, 4096, 10**5, 10**8, 10**12]:
    cc = e12(nn); v = (mp.mpf(cc['FA'].mid), mp.mpf(cc['FD'].mid))
    if prev and not (v[0] > prev[0] and v[1] > prev[1]): ok = False; print('non-increase', nn)
    prev = v
check('E12 FA,FD increasing on n scan (measurement)', ok)
first = None
for nn in range(200, 257):
    cc = e12(nn)
    if cc['FA'].a > 0 and cc['FD'].a > 0: first = nn; break
print('measurement: smallest n in [200,256] with rigorous FA>0,FD>0:', first)

print('ALL CHECKS PASS' if ok_all else 'SOME CHECK FAILED')
sys.exit(0 if ok_all else 1)
