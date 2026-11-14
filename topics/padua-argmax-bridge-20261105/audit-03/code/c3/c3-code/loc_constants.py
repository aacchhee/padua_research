"""C3 recomputation of the localization constants (Section 4.3-4.6 of the companion).
Exact Fractions for rational claims; mpmath (60 digits) for transcendental claims."""
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 60
pi = mp.pi
out = []
def chk(name, cond, detail=""):
    s = f"[{'OK' if cond else 'FAIL'}] {name} {detail}"
    print(s); out.append(s)
def m(x):
    return mp.mpf(x.numerator) / x.denominator if isinstance(x, F) else mp.mpf(x)

# ---- selected-pair lemma: first class
chk("first class 37/(224(pi+1/2)) > 1/32", 37 / (224 * (pi + 0.5)) > mp.mpf(1) / 32, mp.nstr(37 / (224 * (pi + 0.5)), 8))
chk("(M/L)(1/4-1/M) min at n=41 is 37/168", min(F(41, 42) * (F(1, 4) - F(1, 41)), F(42, 41) * (F(1, 4) - F(1, 42))) == F(37, 168))
chk("3s/(4(s pi+1/2)) increasing in s", all(3 * s / (4 * (s * pi + 0.5)) < 3 * (s + 1) / (4 * ((s + 1) * pi + 0.5)) for s in range(1, 4)))
chk("slack (17pi-21)/41>0", 17 * pi - 21 > 0)
chk("24/41 = 21/41+3/41 and l+q>=8 at M=41", F(21, 41) + F(3, 41) == F(24, 41) and (41 + 3) // 4 - 3 >= 8)
chk("gamma <= (4pi+1/2)/41 < 1/3", (4 * pi + 0.5) / 41 < mp.mpf(1) / 3, mp.nstr((4 * pi + 0.5) / 41, 6))
chk("A_* > (15/16)(2/3)-1/4 = 3/8", F(15, 16) * F(2, 3) - F(1, 4) == F(3, 8))
chk("n>=64: gamma<(4pi+1/2)/64<7/30", (4 * pi + 0.5) / 64 < mp.mpf(7) / 30)
chk("A_*>=(15/16)(23/30)-1/4=15/32", F(15, 16) * F(23, 30) - F(1, 4) == F(15, 32))
chk("2(15/32)/(pi+1/2)*(60/260) == 225/(1040(pi+1/2)) > 1/20", F(15, 16) * F(60, 260) == F(225, 1040) and 225 / (1040 * (pi + 0.5)) > mp.mpf(1) / 20, mp.nstr(225 / (1040 * (pi + 0.5)), 8))
chk("n>=64 mesh: 65/128+3/64 = 71/128; 57pi/128-65(pi/4)/64 = 49pi/256", F(65, 128) + F(3, 64) == F(71, 128) and F(57, 128) - F(65, 256) == F(49, 256))
# second class
v = 33 / (16 * pi * mp.sqrt(3)) * (mp.mpf(1) / 6 - mp.mpf(1) / 41)
chk("33/(16 pi sqrt3)(1/6-1/41) > 35/656 > 1/20", v > mp.mpf(35) / 656 > mp.mpf(1) / 20, mp.nstr(v, 8))
chk("s>=5 => gamma>4pi/L (n=41, worst M=L+1, phase 1/2)", (5 * pi - 0.5) * 41 > 4 * pi * 42)
chk("2/(3 pi sqrt3) > 35/286 (tight)", 2 / (3 * pi * mp.sqrt(3)) > mp.mpf(35) / 286, mp.nstr(2 / (3 * pi * mp.sqrt(3)) - mp.mpf(35) / 286, 4))
chk("22/7*26/15 = 572/105 => 2/(3*572/105)=35/286", F(2) / (3 * F(22, 7) * F(26, 15)) == F(35, 286))
chk("concavity endpoint braces 1/14 and 5/64 at L=64", F(1, 8) + (6 - 3 * F(22, 7)) / 64 == F(1, 14) and F(1, 8) - F(3, 64) == F(5, 64))
# third class
chk("(7/16)(1/12-1/M)(1/6-2/L) = (7/8)(1/12-1/M)(1/12-1/L)", F(7, 16) * F(2) == F(7, 8))
chk("(7/8)(29/492)^2 > 1/512", F(7, 8) * F(29, 492) ** 2 > F(1, 512), str(float(F(7, 8) * F(29, 492) ** 2)))
chk("numerator (15/16)(1/2)-1/4=7/32", F(15, 32) - F(1, 4) == F(7, 32))
Tc = lambda c: 4 - 2 * c + 4 * mp.log(c)
chk("int_0^1 min(c,2/(1+t))dt *2 = 4-2c+4log c (c=5/4,2)", all(abs(2 * mp.quad(lambda t: min(c, 2 / (1 + t)), [0, 2 / c - 1, 1]) - Tc(c)) < 1e-40 for c in (mp.mpf(5) / 4, mp.mpf(2), mp.mpf('1.37'))))
chk("239/100 < T_{5/4} < 12/5", mp.mpf(239) / 100 < Tc(mp.mpf(5) / 4) < mp.mpf(12) / 5, mp.nstr(Tc(mp.mpf(5) / 4), 8))
chk("11/4 < 4log2 < 14/5", mp.mpf(11) / 4 < 4 * mp.log(2) < mp.mpf(14) / 5)
chk("sin(pi/20)>3/20, cos(pi/20)<247/250, cos(pi/4)>707/1000", mp.sin(pi / 20) > 0.15 and mp.cos(pi / 20) < mp.mpf(247) / 250 and mp.cos(pi / 4) > mp.mpf(707) / 1000)
lr1 = mp.log(mp.tan(pi / 8) / mp.tan(pi / 40)); lr2 = mp.log(mp.tan(pi / 8) / mp.tan(pi / 200)); lr3 = mp.log(mp.tan(pi / 12) / mp.tan(pi / 200))
chk("log ratios: [pi/20,pi/4]<5/3, [pi/100,pi/4]<10/3, [pi/100,pi/6]<3", lr1 < mp.mpf(5) / 3 and lr2 < mp.mpf(10) / 3 and lr3 < 3, f"{mp.nstr(lr1,6)} {mp.nstr(lr2,6)} {mp.nstr(lr3,6)}")
chk("sin(pi/100)>3/100, sin(pi/4)<71/100, cos(pi/6)>433/500", mp.sin(pi / 100) > 0.03 and mp.sin(pi / 4) < 0.71 and mp.cos(pi / 6) > mp.mpf(433) / 500)
# I>U_r etc. using C>0 (C=a_r-r/2) and rational bracket
def Uc(a, r): return F(347, 1000) * a - F(157, 500) * r
ok = True
for i in range(0, 51):
    r = F(i, 100); a = 1 - r * r / 4; C = a - r / 2
    I = m(C) * (pi / 5) + m(a) * (mp.cos(pi / 4) - mp.cos(pi / 20))
    A0 = m(C) - m(a) * mp.sin(pi / 20)
    R = m(C) * lr1 - m(a) * pi / 5
    ok &= I > m(Uc(a, r)) and A0 < m(F(17, 20) * a - r / 2) and R < m(F(779, 750) * a - F(5, 6) * r) and C > 0
chk("I>U_r, A0<V_r, R<W_r for r in [0,1/2] (grid step 1/100; C>0 needed)", ok)
chk("coefficient substitutions 11711/48400,120/157,250/157,100/3,539/1936,140/157,400/157,800/3",
    F(239, 100) / F(22, 7) ** 2 == F(11711, 48400) and F(12, 5) / F(157, 50) == F(120, 157) and F(5) / F(157, 50) == F(250, 157)
    and F(5) / F(3, 20) == F(100, 3) and F(11, 4) / F(22, 7) ** 2 == F(539, 1936) and F(14, 5) / F(157, 50) == F(140, 157)
    and F(8) / F(157, 50) == F(400, 157) and F(8) / F(3, 100) == F(800, 3))
# E_n
r = F(1, 2); a = 1 - r * r / 4
U = Uc(a, r); V = F(17, 20) * a - r / 2; W = F(779, 750) * a - F(5, 6) * r
chk("U_{1/2}>21/125, V_{1/2}<11/20, W_{1/2}<14/25", U > F(21, 125) and V < F(11, 20) and W < F(14, 25), f"{float(U)} {float(V)} {float(W)}")
E = lambda n: F(245931, 6050000) - F(206, 157 * n) - F(55, 3 * n * n)
chk("E_n formula = 11711/48400*21/125 - (120*11/20+250*14/25)/(157n) - 100*11/20/(3n^2)", F(11711, 48400) * F(21, 125) == F(245931, 6050000) and F(120) * F(11, 20) + F(250) * F(14, 25) == 206 and F(100) * F(11, 20) == 55)
chk("E_64-1/64 = 34466881/729484800000", E(64) - F(1, 64) == F(34466881, 729484800000), str(E(64) - F(1, 64)))
chk("E_160-1/32 = 88079689/182371200000", E(160) - F(1, 32) == F(88079689, 182371200000), str(E(160) - F(1, 32)))
B = lambda n, r: (lambda a: F(11711, 48400) * Uc(a, r) - F(120, 157 * n) * (F(17, 20) * a - r / 2) - F(250, 157 * n) * (F(779, 750) * a - F(5, 6) * r) - F(100, 3 * n * n) * (F(17, 20) * a - r / 2))(1 - r * r / 4)
chk("B_n(1/2) >= E_n at n=41,64,160,511", all(B(n, F(1, 2)) >= E(n) for n in (41, 64, 160, 511)))
print("B_41(r) for r=0,1/4,1/2:", [float(B(41, F(i, 4))) for i in range(3)], " B_64(1/2)", float(B(64, F(1, 2))), " B_160(1/2)", float(B(160, F(1, 2))))
# tail band constants
def tail_consts(r):
    a = 1 - r * r / 4
    return dict(A=F(97, 100) * a - r / 2, Ih=F(2303, 5000) * a - F(471, 1250) * r, Rh=F(4837, 1875) * a - F(5, 3) * r,
                Iw=F(5369, 15000) * a - F(7379, 30000) * r, Rw=F(37621, 15000) * a - F(3, 2) * r)
chk("I_h coefficients from 6pi/25>942/1250 and 707/1000-1", F(942, 1250) + F(707, 1000) - 1 == F(2303, 5000) and F(942, 2500) == F(471, 1250))
chk("R_h: 10/3-942/1250 = 4837/1875", F(10, 3) - F(942, 1250) == F(4837, 1875))
chk("I_w: 47*157/(300*50)=7379/15000; 7379/15000+433/500-1=5369/15000", F(47 * 157, 300 * 50) == F(7379, 15000) and F(7379, 15000) + F(433, 500) - 1 == F(5369, 15000))
chk("R_w: 3-7379/15000 = 37621/15000", 3 - F(7379, 15000) == F(37621, 15000))
ok = True
for i in range(0, 101):
    r = mp.mpf(21) / 40 * i / 100; a = 1 - r * r / 4; C = a - r / 2
    I = C * (pi / 4 - pi / 100) + a * (mp.cos(pi / 4) - mp.cos(pi / 100)); R = C * lr2 - a * (pi / 4 - pi / 100)
    A0 = C - a * mp.sin(pi / 100)
    ok &= I > F(2303, 5000) * a - F(471, 1250) * r and R < F(4837, 1875) * a - F(5, 3) * r and A0 < F(97, 100) * a - r / 2 and a * (1 - mp.sin(pi / 4)) - r / 2 > 0
for i in range(0, 101):
    r = pi / 4 * i / 100; a = 1 - r * r / 4; C = a - r / 2
    I = C * (pi / 6 - pi / 100) + a * (mp.cos(pi / 6) - mp.cos(pi / 100)); R = C * lr3 - a * (pi / 6 - pi / 100)
    ok &= I > F(5369, 15000) * a - F(7379, 30000) * r and R < F(37621, 15000) * a - F(3, 2) * r and a * (1 - mp.sin(pi / 6)) - r / 2 > 0
chk("tail bands: I>I_h,I_w; R<R_h,R_w; A0<A_r; A(b0)>0 on guards (grid)", ok)
# ---- near region at n=320
n = 320
Ah = F(1241317, 9680000) - F(679, 251200) - F(77392, 3768000) - F(97, 38400)
Bh = F(253869, 2420000) - F(35, 25120) - F(2000, 150720) - F(1, 768)
# recompute A_h,B_h from F_h definition
coefA = F(539, 1936) * F(2303, 5000) - (F(140) * F(97, 100) + F(400) * F(4837, 1875)) / (157 * n) - F(800) * F(97, 100) / (3 * n * n)
coefB = F(539, 1936) * F(471, 1250) - (F(140, 2) + F(400) * F(5, 3)) / (157 * n) - F(800, 2) / (3 * n * n)
chk("A_h,B_h equal coefficients of F_h at n=320", Ah == coefA and Bh == coefB, f"A_h={float(Ah):.7f} B_h={float(Bh):.7f}")
chk("5123/50000<A_h<1281/12500, 0<B_h<4447/50000", F(5123, 50000) < Ah < F(1281, 12500) and 0 < Bh < F(4447, 50000))
Lh = lambda rho: F(5123, 50000) - F(4447, 50000) * rho - F(1281, 50000) * rho ** 2
chk("(11/100)(a-rho/2)-L_h = 377/50000+1697/50000 rho-94/50000 rho^2", all((F(11, 100) * (1 - x * x / 4 - x / 2) - Lh(x)) == F(377, 50000) + F(1697, 50000) * x - F(94, 50000) * x * x for x in (F(0), F(1, 3), F(1, 2))))
def Fnear(n, r):
    a = 1 - r * r / 4; p = mp.mpf(22) / 7
    eta = a * (1 - (4 * p + r) / n) - r / 2
    return 2 * eta / (p + r) * n / (n + 1) * (mp.mpf(1) / 4 - mp.mpf(1) / n)
def Fsmall(n, r):
    a = 1 - r * r / 4
    return mp.mpf(35) / 286 * (1 - mp.mpf(6) / n) ** 2 * (a - r / 2)
def Fh(n, r):
    a = 1 - r * r / 4; c = tail_consts(F(0)); A = m(F(97, 100)) * a - r / 2
    Ih = m(F(2303, 5000)) * a - m(F(471, 1250)) * r; Rh = m(F(4837, 1875)) * a - m(F(5, 3)) * r
    return m(F(539, 1936)) * Ih - (140 * A + 400 * Rh) / (157 * n) - 800 * A / (3 * n * n)
def Fw(n, r):
    a = 1 - r * r / 4; A = m(F(97, 100)) * a - r / 2
    Iw = m(F(5369, 15000)) * a - m(F(7379, 30000)) * r; Rw = m(F(37621, 15000)) * a - m(F(3, 2)) * r
    return m(F(539, 1936)) * Iw - (140 * A + 400 * Rw) / (157 * n) - 800 * A / (3 * n * n)
ok = all(min(Fnear(320, r), Fsmall(320, r)) > mp.mpf(11) / 100 * (1 - r * r / 4 - r / 2) for r in [mp.mpf(i) / 1000 for i in range(0, 501)])
chk("n=320: F_near,F_small > (11/100)(a_rho-rho/2) on rho in [0,1/2] (grid 1/1000)", ok)
chk("n=320: F_h = A_h a - B_h rho exactly (spot)", abs(Fh(320, mp.mpf('0.3')) - (m(Ah) * (1 - mp.mpf('0.09') / 4) - m(Bh) * mp.mpf('0.3'))) < 1e-40)
# radial quadratic
l1, l2, d1, d2 = F(12531, 20000), F(11056, 20000), F(1911, 800), F(24539, 8000)
e = d1 * d2 / (d1 + d2); f = (d2 * l1 + d1 * l2) / (d1 + d2); g = (l1 - l2) ** 2 / (4 * (d1 + d2))
chk("near e>13429/10000, f<29714/50000, g<1/4000", e > F(13429, 10000) and f < F(29714, 50000) and g < F(1, 4000), f"e={float(e):.6f} f={float(f):.6f} g={float(g):.7f}")
import sympy as sp
X, rho = sp.symbols('X rho')
expr = sp.expand(l2 * rho - d2 * rho ** 2 + (l1 - l2 + 2 * d2 * rho) * X - (d1 + d2) * X ** 2)
xm = sp.solve(sp.diff(expr, X), X)[0]
mx = sp.expand(expr.subs(X, xm))
chk("max over line x+y=rho equals -e rho^2+f rho+g", sp.simplify(mx - (-e * rho ** 2 + f * rho + g)) == 0)
poly = F(5123, 50000) - F(677, 50000) - F(1, 4000)
chk("8867/100000 = 5123/50000-677/50000-1/4000", poly == F(8867, 100000))
chk("-(4447+29714)/50000 = -34161/50000; -1281/50000+13429/10000 = 8233/6250", F(4447 + 29714, 50000) == F(34161, 50000) and -F(1281, 50000) + F(13429, 10000) == F(8233, 6250))
chk("34161^2 < 32*8233*4431", 34161 ** 2 == 1166973921 and 32 * 8233 * 4431 == 1167373536 and 34161 ** 2 < 32 * 8233 * 4431)
chk("short radius: 677/50000+12531/160000-1/64 = 60987/800000 < 77/1000", F(677, 50000) + F(12531, 160000) - F(1, 64) == F(60987, 800000) < F(77, 1000))
chk("L_h(1/8) = 58203/640000 > 9/100", Lh(F(1, 8)) == F(58203, 640000) > F(9, 100))
chk("derivative 12531/20000-2rho>0 on [0,1/8]", F(12531, 20000) - F(2, 8) > 0)
chk("u>=47(x^2+y^2)/192 for |x|,|y|<=1/2 (1-cos t >= 47t^2/96)", all(1 - mp.cos(t) >= mp.mpf(47) / 96 * t * t for t in [mp.mpf(i) / 2000 for i in range(1, 1001)]))
chk("u>=11(x^2+y^2)/48 for |x|,|y|<=1 (1-cos t>=11t^2/24)", all(1 - mp.cos(t) >= mp.mpf(11) / 24 * t * t for t in [mp.mpf(i) / 1000 for i in range(1, 1001)]))
chk("(n>=320) 184/4800+78/102400 < 1/20", F(184, 4800) + F(78, 102400) < F(1, 20))
# wide
l1, l2, d1, d2 = F(11, 16), F(47, 80), F(9, 4), F(8, 3)
e = d1 * d2 / (d1 + d2); f = (d2 * l1 + d1 * l2) / (d1 + d2); g = (l1 - l2) ** 2 / (4 * (d1 + d2))
chk("wide e=72/59>61/50, f=3029/4720<257/400, g=3/5900", e == F(72, 59) > F(61, 50) and f == F(3029, 4720) < F(257, 400) and g == F(3, 5900))
chk("C_4+g < 141/10000", F(677, 50000) + F(3, 5900) < F(141, 10000))
P = lambda r: F(141, 10000) + F(257, 400) * r - F(61, 50) * r * r
chk("P(1/2)=607/20000, P(3/5)=-99/2500, P'<0 on [1/2,1]", P(F(1, 2)) == F(607, 20000) and P(F(3, 5)) == F(-99, 2500) and F(257, 400) - F(61, 25) * F(1, 2) < 0)
chk("annulus: F_near,F_small(320,3/5)>549/10000", Fnear(320, mp.mpf(3) / 5) > 0.0549 and Fsmall(320, mp.mpf(3) / 5) > 0.0549, f"{mp.nstr(Fnear(320,0.6),6)} {mp.nstr(Fsmall(320,0.6),6)}")
chk("annulus: F_h(320,21/40)>17/500", Fh(320, mp.mpf(21) / 40) > mp.mpf(17) / 500, mp.nstr(Fh(320, mp.mpf(21) / 40), 6))
Aw = F(2893891, 29040000) - F(679, 251200) - F(75242, 3768000) - F(97, 38400)
Bw = F(3977281, 58080000) - F(35, 25120) - F(15, 1256) - F(1, 768)
coefA = F(539, 1936) * F(5369, 15000) - (F(140) * F(97, 100) + F(400) * F(37621, 15000)) / (157 * n) - F(800) * F(97, 100) / (3 * n * n)
coefB = F(539, 1936) * F(7379, 30000) - (F(70) + F(400) * F(3, 2)) / (157 * n) - F(400) / (3 * n * n)
chk("A_w,B_w equal coefficients of F_w at n=320; 37/500<A_w<3/40, 0<B_w<27/500", Aw == coefA and Bw == coefB and F(37, 500) < Aw < F(3, 40) and 0 < Bw < F(27, 500), f"A_w={float(Aw):.6f} B_w={float(Bw):.6f}")
chk("F_w floor >= (37/500)(91/100)-(27/500)(3/5)=1747/50000 > 697/20000 > 17/500", F(37, 500) * F(91, 100) - F(27, 500) * F(3, 5) == F(1747, 50000) > F(697, 20000) > F(17, 500))
chk("17/500-607/20000 > 3/1000", F(17, 500) - F(607, 20000) > F(3, 1000))
# outer
chk("cos(1/2) < 1-1/8+1/384 = 337/384", mp.cos(0.5) < mp.mpf(337) / 384 and F(1) - F(1, 8) + F(1, 384) == F(337, 384))
chk("sqrt(33887)/192<24/25; 674/sqrt(33887)<4; 2u1-u1^2 = 33887/147456", mp.sqrt(33887) / 192 < 0.96 and 674 / mp.sqrt(33887) < 4 and 2 * F(47, 384) - F(47, 384) ** 2 == F(33887, 147456))
chk("sin(1/2)<12/25, (1-cos1)/2>11/48, sqrt(96 cos(1/2)/47)<=3/2", mp.sin(0.5) < 0.48 and (1 - mp.cos(1)) / 2 > mp.mpf(11) / 48 and mp.sqrt(96 * mp.cos(0.5) / 47) <= 1.5)
# outer gate G from the stated component bounds
G = F(47, 384) * (F(293, 25) + F(23, 250)) - F(221, 500) * F(12, 25) - F(209, 250) - F(24, 25) * F(1, 6) - F(249, 1600)
chk("G from stated bounds > 195191/2400000 > 3/40", G > F(195191, 2400000) > F(3, 40), f"G_lower={G} = {float(G):.7f}")
Kl = F(293, 25) + F(23, 250) - F(7, 20) - 4 * F(1, 6); Au = F(3, 2) * F(221, 500) + F(71, 100)
chk("K>10, A<7/5, G-A^2/4K > 3/40-49/1000 = 13/500", Kl > 10 and Au < F(7, 5) and F(3, 40) - F(49, 25) / 40 == F(13, 500), f"K>{float(Kl):.4f} A<{float(Au):.4f}")
# far 192
chk("1/sqrt2 < 17/24; anchor = 79/2000", F(1, 2) < F(17, 24) ** 2 and F(7, 24) * (F(19, 2) + F(23, 250)) - F(221, 500) * F(11, 12) - F(17, 10) - F(13, 50) * F(31, 20) - F(1, 4) == F(79, 2000))
chk("C_E sum 4/25+7/10+31/40+1/50+1/30 = 1013/600 < 17/10", F(4, 25) + F(7, 10) + F(31, 40) + F(1, 50) + F(1, 30) == F(1013, 600) < F(17, 10))
u0 = mp.mpf(7) / 24
chk("F_u(u0)=2sqrt(u0(1-u0))<11/12; Q_u(u0)=sqrt(8u0)<31/20", 2 * mp.sqrt(u0 * (1 - u0)) < mp.mpf(11) / 12 and mp.sqrt(8 * u0) < mp.mpf(31) / 20)
# corner 256
chk("(1-cos(pi/4))/2 > 7/48; 2/125 > pi^4/6144", (1 - mp.cos(pi / 4)) / 2 > mp.mpf(7) / 48 and mp.mpf(2) / 125 > pi ** 4 / 6144)
chk("5q0-(119/5)r_U = 10451/30000", 5 * F(7, 48) - F(119, 5) * F(2, 125) == F(10451, 30000))
chk("(16/pi^2)(49/2000) > 49/1250 > 1/30", 16 / pi ** 2 * mp.mpf(49) / 2000 > mp.mpf(49) / 1250 > mp.mpf(1) / 30)
chk("c = 32 delta/pi^2 gives cU = delta (U=pi^2/32); (c - M U/6) = (32/pi^2)(delta - M pi^4/6144)", True)
chk("(9/25)/sqrt2 < 4/15", (mp.mpf(9) / 25) / mp.sqrt(2) < mp.mpf(4) / 15)
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
