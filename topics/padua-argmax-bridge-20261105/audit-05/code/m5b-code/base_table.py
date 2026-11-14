#!/usr/bin/env python3
"""M5B independent recomputation of the P4-05 base-value table, the gates and
the corner-256 arithmetic.

Independent of code/onset512_analytic/check.py: uses mpmath interval arithmetic
(mpmath.iv, outward rounded, 80 decimal digits) with mpmath's own pi and log,
and, for the coarse rational chains, exact Fractions. Formulas transcribed from
paper comparison-unified.tex (uc:constants, uc:uniform-allowance,
uc:analytic-norm, Cor uc:absolute-gate, Cor uc:relative-gate) and
localization-unified.tex (corner lemma).
"""
from fractions import Fraction as Fr
import sys
import mpmath
from mpmath import iv

iv.dps = 80
PI = iv.pi
LOG = iv.log
JSTAR = iv.mpf(23) / 250
TSTAR = iv.mpf(221) / 500


def consts(n):
    n = iv.mpf(n)
    m = n + 1
    L = LOG(n)
    Lb = 1 + L
    T = (4 * L**2 - 3 * L) / PI**2
    b0 = 4 / PI**2
    r0 = LOG(iv.mpf(5) / 2) + iv.mpf(1) / 18
    D = ((52 / PI**2) * Lb + 7) / n + 10 / n**2 + 20 * Lb / (PI * n**2)
    Mesh = (b0 * (2 * L + 2 * r0) / n + (4 + b0 * (L + 1 / n)) / (4 * n**2 - 1)
            + b0 / (2 * n - 1)**2 + (5 + b0 * (LOG(n + iv.mpf(1) / 2) + 2)) / (4 * (n - iv.mpf(1) / 2)**2))
    ebar = D + Mesh + 1 / n
    KD = ((6 + 16 / (3 * PI)) * Lb + 2 / PI) / n
    A4 = 4 / n + 40 * Lb / (PI * n**2)
    C4 = A4 + 20 / n**2
    dbeta = (17 * L + 27) / n**2
    JW = ((iv.mpf(3) / 2) * Lb + 6) / n + 148 / n**2
    kx = ((iv.mpf(19) / 2) * Lb + (iv.mpf(23) / 3) * L + iv.mpf(155) / 2) / n + 152 / n**2
    ky = kx + dbeta
    gn = 1 + LOG(2 + 8 * m / (3 * PI))
    MA = 1 / PI + 4 / PI**2
    Gg = (7 * MA * L + iv.mpf(111) / 2 + (63 + LOG(2) + 4 * LOG(PI) + 7 * LOG(m) + 16 * LOG(2 * m)
                                           + (iv.mpf(3) / 2) * gn) / PI) / m
    Wn = (3 * LOG(m) + LOG(2) + 2 * LOG(PI) + 2) / (PI * m)
    CE = D + Gg + (64 + 16 * L) / n + 318 / n**2 + Mesh + Wn
    Mn = (4 * L**2 + (iv.mpf(79) / 5) * L) / PI**2 + iv.mpf(9) / 4 + CE + 2 * KD
    Ustar = T - ebar + A4 + JSTAR
    lx = kx + iv.mpf(5) / 48
    ly = ky
    dx = 11 * Ustar / 48 - iv.mpf(5) / 12
    dy = 11 * Ustar / 48
    return dict(L=L, T=T, ebar=ebar, KD=KD, CE=CE, C4=C4, kx=kx, ky=ky, dbeta=dbeta,
                M=Mn, Ustar=Ustar, dx=dx, dy=dy, lx=lx, ly=ly, A4=A4, JW=JW)


ORDER = ['L', 'T', 'ebar', 'KD', 'CE', 'C4', 'kx', 'ky', 'dbeta', 'M', 'Ustar', 'dx', 'dy', 'lx', 'ly']

# Printed table, paper/companion comparison-unified.tex (ad908acb)
TABLE = {
 192: {'L': ('5.257495', '5.257496'), 'T': ('9.604492', '9.604493'), 'ebar': ('0.241128', '0.241129'),
       'KD': ('0.254190', '0.254191'), 'CE': ('1.821444', '1.821445'), 'C4': ('0.023537', '0.023538'),
       'kx': ('0.927319', '0.927320'), 'ky': ('0.930476', '0.930477'), 'dbeta': ('0.003156', '0.003157'),
       'M': ('24.198997', '24.198998'), 'Ustar': ('9.478358', '9.478359'), 'dx': ('1.755457', '1.755458'),
       'dy': ('2.172123', '2.172124'), 'lx': ('1.031486', '1.031487'), 'ly': ('0.930476', '0.930477')},
 256: {'L': ('5.545177', '5.545178'), 'T': ('10.776565', '10.776566'), 'ebar': ('0.187434', '0.187435'),
       'KD': ('0.199293', '0.199294'), 'CE': ('1.405236', '1.405237'), 'C4': ('0.017201', '0.017202'),
       'kx': ('0.714007', '0.714008'), 'ky': ('0.715858', '0.715859'), 'dbeta': ('0.001850', '0.001851'),
       'M': ('25.393055', '25.393056'), 'Ustar': ('10.698027', '10.698028'), 'dx': ('2.034964', '2.034965'),
       'dy': ('2.451631', '2.451632'), 'lx': ('0.818174', '0.818175'), 'ly': ('0.715858', '0.715859')},
 295: {'L': ('5.686975', '5.686976'), 'T': ('11.378959', '11.378960'), 'ebar': ('0.165491', '0.165492'),
       'KD': ('0.176646', '0.176647'), 'CE': ('1.236309', '1.236310'), 'C4': ('0.014767', '0.014768'),
       'kx': ('0.627598', '0.627599'), 'ky': ('0.629020', '0.629021'), 'dbeta': ('0.001421', '0.001422'),
       'M': ('26.051329', '26.051330'), 'Ustar': ('11.320005', '11.320006'), 'dx': ('2.177501', '2.177502'),
       'dy': ('2.594168', '2.594169'), 'lx': ('0.731765', '0.731766'), 'ly': ('0.629020', '0.629021')},
 512: {'L': ('6.238324', '6.238325'), 'T': ('13.876118', '13.876119'), 'ebar': ('0.101753', '0.101754'),
       'KD': ('0.110067', '0.110068'), 'CE': ('0.750341', '0.750342'), 'C4': ('0.008240', '0.008241'),
       'kx': ('0.379664', '0.379665'), 'ky': ('0.380171', '0.380172'), 'dbeta': ('0.000507', '0.000508'),
       'M': ('28.979594', '28.979595'), 'Ustar': ('13.874529', '13.874530'), 'dx': ('2.762912', '2.762913'),
       'dy': ('3.179579', '3.179580'), 'lx': ('0.483830', '0.483831'), 'ly': ('0.380171', '0.380172')},
}


def contains(ivx, lo, hi):
    a, b = iv.mpf(lo), iv.mpf(hi)
    # true value interval ivx must lie strictly inside [lo, hi] (decimals are exact rationals)
    return (ivx.a > a.b) and (ivx.b < b.a)


def outward6(ivx):
    # what a correct floor/ceil 6-decimal outward enclosure of the true value would print
    lo = mpmath.floor(mpmath.mpf(ivx.a) * 10**6)
    hi = mpmath.ceil(mpmath.mpf(ivx.b) * 10**6)
    return int(lo), int(hi)


def main():
    bad = 0
    for n in (192, 256, 295, 512):
        c = consts(n)
        for k in ORDER:
            lo, hi = TABLE[n][k]
            ok = contains(c[k], lo, hi)
            olo, ohi = outward6(c[k])
            tight = (olo == int(round(float(lo) * 10**6)) and ohi == int(round(float(hi) * 10**6)))
            mid = mpmath.mpf(c[k].a)
            if not ok or not tight:
                bad += 1
            print(f"n={n:4d} {k:6s} true~{mpmath.nstr(mid, 12):>16s} printed=[{lo},{hi}] contains={ok} tightest6={tight}")
    print('TABLE MISMATCHES:', bad)

    # gates
    def gate(n, rho1):
        c = consts(n)
        Ts = c['T'] + JSTAR
        h = iv.mpf(rho1) / 2
        G = Ts * (1 - iv.cos(h)) - (TSTAR + 2 * c['KD']) * iv.sin(h) - TSTAR**2 * iv.cos(h) / (2 * Ts) - c['CE'] - c['ebar']
        ratio = (TSTAR + 2 * c['KD']) / Ts
        return G, ratio
    G512, r512 = gate(512, 1)
    G192, r192 = gate(192, PI / 2)
    print('G(512,1) =', G512, ' >1/2:', G512.a > 0.5, ' >0.534264:', G512.a > iv.mpf('0.534264').b, ' ratio', r512, '<3/50:', r512.b < iv.mpf(3) / 50,
          ' tan(1/2)>ratio:', iv.tan(iv.mpf(1) / 2).a > r512.b)
    print('G(192,pi/2) =', G192, ' >3/100:', G192.a > iv.mpf(3) / 100, ' >0.098316:', G192.a > iv.mpf('0.098316').b, ' ratio', r192, '<1/10:', r192.b < iv.mpf(1) / 10)
    c = consts(512)
    dx, dy, lx, ly, C4 = c['dx'], c['dy'], c['lx'], c['ly'], c['C4']
    e = dx * dy / (dx + dy)
    f = (dy * lx + dx * ly) / (dx + dy)
    g = (lx - ly)**2 / (4 * (dx + dy))
    peak = C4 + lx**2 / (4 * dx) + ly**2 / (4 * dy)
    half = C4 + g + f / 2 - e / 4
    vertex = lx / (2 * dx) + ly / (2 * dy)
    print('max p_512 =', peak, '<41/1000:', peak.b < iv.mpf(41) / 1000, '<40786e-6:', peak.b < iv.mpf(40786) / 10**6,
          'margin to 40786e-6:', mpmath.nstr(mpmath.mpf(40786) / 10**6 - mpmath.mpf(peak.b), 3))
    print('p_512(1/2) =', half, '<-1/7:', half.b < -iv.mpf(1) / 7, '<-143069e-6:', half.b < -iv.mpf(143069) / 10**6)
    print('vertex f/(2e) =', vertex, '<3/20:', vertex.b < iv.mpf(3) / 20, ' alt identity f/(2e)=', f / (2 * e))
    print('d_x(512)>1:', dx.a > 1, ' d_beta(512) in (0,5/48):', c['dbeta'].a > 0 and c['dbeta'].b < iv.mpf(5) / 48)
    # direct p(rho) at rho=1/2 from definition
    pdef = C4 + g + f * iv.mpf(1) / 2 - e * iv.mpf(1) / 4
    print('p(1/2) via def', pdef)
    xs = (dy / 2 + (lx - ly) / 2) / (dx + dy)
    ys = (dx / 2 - (lx - ly) / 2) / (dx + dy)
    print('x*, y* at rho=1/2:', xs, ys)

    # corner 256 coarse rational chains (exact Fractions)
    qh = Fr(7, 48); rU = Fr(2, 125)
    T_lo, eb_hi, KD_hi, CE_hi, C4_hi, ky_hi, M_hi = Fr(107, 10), Fr(1, 5), Fr(1, 5), Fr(3, 2), Fr(9, 500), Fr(93, 100), Fr(26)
    j_lo = Fr(23, 250)
    h_hi = Fr(22, 7) / 4
    dA = qh * (T_lo - eb_hi + j_lo) - Fr(1, 4) - C4_hi - h_hi * ky_hi - rU * M_hi
    dD = 2 * qh * (T_lo + j_lo) - Fr(4, 15) - CE_hi - Fr(3, 2) * KD_hi - eb_hi - 2 * rU * M_hi
    print('coarse delta_A - r_U M >', dA, '==2729/21000:', dA == Fr(2729, 21000), ' >1/8:', dA > Fr(1, 8), '>49/2000', dA > Fr(49, 2000))
    print('coarse delta_D - 2 r_U M >', dD, '==49/1000:', dD == Fr(49, 1000))
    # true values at 256
    c = consts(256)
    h = PI / 4
    jtrue = JSTAR  # conservative lower bound used
    qhi = iv.mpf(7) / 48
    dA_t = qhi * (c['T'] - c['ebar'] + jtrue) - iv.mpf(1) / 4 - c['C4'] - h * c['ky'] - iv.mpf(2) / 125 * c['M']
    dD_t = 2 * qhi * (c['T'] + jtrue) - iv.mpf(4) / 15 - c['CE'] - iv.mpf(3) / 2 * c['KD'] - c['ebar'] - 2 * iv.mpf(2) / 125 * c['M']
    print('true delta_A - r_U M(256) (j=23/250):', dA_t, ' true delta_D - 2r_U M(256):', dD_t)
    print('r_U > pi^4/6144:', (iv.mpf(2) / 125).a > (PI**4 / 6144).b, ' pi^4/6144 =', PI**4 / 6144)
    print('(16/pi^2)(49/2000) > 49/1250 > 1/30:', (16 / PI**2 * iv.mpf(49) / 2000).a > iv.mpf(49) / 1250, Fr(49, 1250) > Fr(1, 30))
    print('u axis (1-cos h)/2 > 7/48:', ((1 - iv.cos(h)) / 2).a > iv.mpf(7) / 48, ((1 - iv.cos(h)) / 2))
    print('u diag 1-cos h > 7/24:', (1 - iv.cos(h)).a > iv.mpf(7) / 24, (1 - iv.cos(h)))
    print('(9/25)/sqrt2 < 4/15:', (iv.mpf(9) / 25 / iv.sqrt(2)).b < iv.mpf(4) / 15)
    I4 = iv.mpf(mpmath.quad(lambda t: mpmath.sqrt(1 - t**4), [0, 1]))
    print('I4 approx', I4, ' 4I4/pi^2 approx', 4 * I4 / PI**2, '(<9/25?)', (4 * I4 / PI**2).b < iv.mpf(9) / 25, '; 319/360 bound gives', 4 * iv.mpf(319) / 360 / PI**2)
    a_ax = (1 + iv.cos(h)) / 2
    print('axis a=(1+cos h)/2 =', a_ax, '>17/20', a_ax.a > iv.mpf(17) / 20, ' p^{3/2}=', iv.sin(h)**iv.mpf(1.5), '<3/5', (iv.sin(h)**iv.mpf(1.5)).b < iv.mpf(3) / 5,
          ' sqrt a >9/10', iv.sqrt(a_ax).a > iv.mpf(9) / 10, ' Ec(h,0)<=', 4 * iv.mpf(319) / 360 / PI**2 * iv.sin(h)**iv.mpf(1.5) / iv.sqrt(a_ax), '< 6/25', (iv.mpf(9) / 25 * iv.mpf(3) / 5 / (iv.mpf(9) / 10)), Fr(9, 25) * Fr(3, 5) / Fr(9, 10))
    # 𝔗 - ebar + j positivity at 256
    print('T-ebar+j at 256 >0:', (c['T'] - c['ebar'] + JSTAR).a > 0)
    # displayed n=256 substitutions (companion)
    Tsub = (4 * Fr(277, 50)**2 - 3 * Fr(277, 50)) / Fr(22, 7)**2
    KDsub = ((6 + Fr(16) / (3 * Fr(157, 50))) * Fr(131, 20) + 2 / Fr(157, 50)) / 256
    Msub = (4 * Fr(111, 20)**2 + Fr(79, 5) * Fr(111, 20)) / Fr(157, 50)**2 + Fr(9, 4) + Fr(3, 2) + Fr(2, 5)
    print('T sub', Tsub, Tsub == Fr(6501467, 605000), Tsub > Fr(107, 10))
    print('KD sub', KDsub, KDsub == Fr(240503, 1205760), KDsub < Fr(1, 5))
    print('M sub', Msub, Msub == Fr(12590867, 492980), Msub < 26)
    L256 = LOG(256)
    print('L(256)', L256, '277/50<L<111/20', L256.a > iv.mpf(277) / 50, L256.b < iv.mpf(111) / 20, ' Lbar<131/20', (1 + L256).b < iv.mpf(131) / 20)
    # elementary bound check
    print('log pi', LOG(PI), '>11/10', LOG(PI).a > iv.mpf(11) / 10, ' log(157/50)>11/10', LOG(iv.mpf(157) / 50).a > iv.mpf(11) / 10)
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
