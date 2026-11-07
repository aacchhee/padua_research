"""Exact Fraction re-check of E06-H-consequences and E07-global-assembly rational chains
(Claude audit2 m2). Each check prints PASS/FAIL. Rational inputs are those stated in the
files; analytic premises (D10/E01/E02/E04/D24/D37 formulas) are NOT re-derived here."""
from fractions import Fraction as F
import sympy as sp
res = []
def chk(name, cond, *info):
    res.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, *info)

# ---- E06-H-consequences (3) ----
H0lo = F(9, 20) - F(2)*F(9, 5)*F(23, 50)/F(197, 20)
chk("E06 H0 lower = 5553/19700 > 7/25", H0lo == F(5553, 19700) and H0lo > F(7, 25), H0lo)
H0hi = F(23, 50) - F(2)*F(161, 100)*F(18, 41)/10
chk("E06 H0 upper = 1633/5125 < 8/25", H0hi == F(1633, 5125) and H0hi < F(8, 25), H0hi)
chk("log(25/16) > 2(s-1)/(s+1)=18/41", F(2)*(F(25, 16)-1)/(F(25, 16)+1) == F(18, 41))
g0hi = F(80, 197)*(F(23, 20)**2 - F(69, 100)**2)
chk("E06 g0 upper < 43/125", g0hi == F(677120, 1970000) and g0hi < F(43, 125), g0hi)
chk("E06 j > 23/250", F(7, 25)+F(39, 250)-F(43, 125) == F(23, 250))
t0hi = 2*F(6932, 10000)/F(157, 50)
chk("E06 t0 < 221/500", t0hi == F(6932, 15700) and t0hi < F(221, 500), t0hi)
dl = F(9, 4) - F(1847, 1000); eps = F(1, 400)
chk("E06 delta>403/1000", dl == F(403, 1000))
a1 = dl - 2*eps; b1 = F(23, 250)+eps
lhs = a1*a1 + a1*b1
chk("E06 (6)/(7): LHS>196015/1e6 > (221/500)^2=195364/1e6", a1 == F(199, 500) and b1 == F(189, 2000) and lhs > F(196015, 10**6) and F(221, 500)**2 == F(195364, 10**6), lhs, lhs - F(221, 500)**2)
chk("E06 cR(R=1)*j = 253/12000 ; /2 = 253/24000", F(11, 48)*F(23, 250) == F(253, 12000))
chk("E06 (11) 2/3-253/12000 = 7747/12000; 19/24-7747/12000=1753/12000", F(2, 3)-F(253, 12000) == F(7747, 12000) and F(19, 24)-F(7747, 12000) == F(1753, 12000))
eps2 = F(11, 50)
chk("E06 (13): 2eps=11/25, j+eps>39/125", 2*eps2 == F(11, 25) and F(23, 250)+eps2 == F(39, 125))
u1 = F(47, 384)
chk("E06 u1(1-u1)*384^2 = 15839 and 15839<128^2", u1*(1-u1)*384*384 == 15839 and 15839 < 128**2)
chk("E06 (15) 17/20-11/25+(39/125)u1-(221/500)(2/3) = 7369/48000 > 3/20", F(17, 20)-F(11, 25)+F(39, 125)*u1-F(221, 500)*F(2, 3) == F(7369, 48000) and F(7369, 48000) > F(3, 20) and F(6211, 7260) > F(17, 20))
# with HM (eps=0) correlated global increment bound: -j/2+sqrt(j^2/4+t0^2) decreasing in j
jl = F(23, 250); tt = F(221, 500)
# check (-jl/2 + sqrt(jl^2/4+tt^2)) < 101/250  <=> sqrt(...) < 101/250 + jl/2
rhs = F(101, 250) + jl/2
chk("E06/E07 HM global increment -j/2+sqrt(j^2/4+t0^2) < 101/250", jl*jl/4 + tt*tt < rhs*rhs)
chk("9/4 - 923/500 = 101/250", F(9, 4)-F(923, 500) == F(101, 250))

# ---- E07-global-assembly ----
Llo, Lhi = 9*F(693, 1000), 9*F(7, 10)
chk("E07g L bounds 6237/1000<L<63/10", Llo == F(6237, 1000) and Lhi == F(63, 10))
Tlo = (4*Llo**2 - 3*Llo)*F(49, 484)
chk("E07g T>69/5", Tlo > F(69, 5), float(Tlo))
chk("E07g V>27/2, UN>=V+j>1699/125", F(69, 5)-F(3, 10) == F(27, 2) and F(27, 2)+F(23, 250) == F(1699, 125))
n = 512; Hh = F(73, 10); Lh_ = F(63, 10); pil = 3
C4 = F(4, n) + 40*Hh/(pil*n*n) + F(20, n*n)
chk("E07g C4 bound = 203/24576 < 83/10000", C4 == F(203, 24576) and C4 < F(83, 10000))
kNx = (F(19, 2)*Hh + F(29, 2)*Lh_ + F(1163, 15))/n + F(82, n*n); db = (17*Lh_+27)/F(n*n)
chk("E07g kNy < 7/15", kNx+db < F(7, 15) and (F(19, 2)*Hh + F(29, 2)*Lh_ + F(1163, 15))/n == F(7147, 15360) and F(82, n*n)+db == F(2161, 2621440), float(kNx+db))
kWx = (F(19, 2)*Hh + 15*Lh_ + F(265, 3))/n + F(152, n*n)
chk("E07g kWy < 99/200", kWx+db < F(99, 200) and (F(19, 2)*Hh + 15*Lh_ + F(265, 3))/n == F(15131, 30720), float(kWx+db))
Gg = (F(1323, 40)+F(111, 2)+F(2389, 31))/513
six = (67+19*Lh_)/n + F(318, n*n)
mesh = F(41, 100)*(2*Lh_+2)/n + F(14, n*n)
W = (3*F(3151, 500)+F(7, 10)+F(12, 5)+2)/(F(157, 50)*513)
chk("E07g CE pieces Gg<13/40 six<367/1000 Mesh<3/250 W<3/200", Gg < F(13, 40) and six < F(367, 1000) and mesh < F(3, 250) and W < F(3, 200), float(Gg), float(six), float(mesh), float(W))
chk("E07g CE sum 809/1000", F(9, 100)+F(13, 40)+F(367, 1000)+F(3, 250)+F(3, 200) == F(809, 1000))
Ah = F(1241317, 9680000)-F(679, 401920)-F(4837, 376800)-F(97, 98304)
Bh = F(253869, 2420000)-F(35, 40192)-F(125, 15072)-F(25, 49152)
Aw = F(2893891, 29040000)-F(679, 401920)-F(37621, 3014400)-F(97, 98304)
Bw = F(3977281, 58080000)-F(35, 40192)-F(75, 10048)-F(25, 49152)
chk("E07g Ah,Bh,Aw,Bw bounds", F(14, 125) < Ah < F(57, 500) and Bh < F(12, 125) and F(21, 250) < Aw < F(11, 125) and Bw < F(3, 50), float(Ah), float(Bh), float(Aw), float(Bw))
r = sp.symbols('r')
chk("E07g Fn step diff = 1349/100000 a_r - 17r/2000", F(27, 200)*F(487, 500)-F(59, 500) == F(1349, 100000) and (F(27, 200)-F(59, 500))/2 == F(17, 2000))
chk("E07g Fs coefficient compare", 35*253**2*500 == 1120157500 and 59*286*256**2 == 1105854464 and F(35, 286)*F(253, 256)**2 > F(59, 500))
expr = sp.expand(sp.Rational(59, 500)*(1-r**2/4-r/2) - (sp.Rational(14, 125)-sp.Rational(12, 125)*r-sp.Rational(57, 2000)*r**2))
chk("E07g common-bound minus Lh = 3/500+37r/1000-r^2/1000", sp.simplify(expr-(sp.Rational(3, 500)+sp.Rational(37, 1000)*r-r**2/1000)) == 0)
Lh = lambda x: F(14, 125)-F(12, 125)*x-F(57, 2000)*x*x
Lw = lambda x: F(21, 250)-F(3, 50)*x-F(11, 500)*x*x
chk("E07g Lh(21/40)>1/25, Lw(3/5)=501/12500>1/25, (9/100)(a-r/2) at 3/5 = 549/10000", Lh(F(21, 40)) > F(1, 25) and Lw(F(3, 5)) == F(501, 12500) and F(9, 100)*(1-F(9, 100)-F(3, 10)) == F(549, 10000))
# radial line formula symbolic
d1, d2, l1, l2, x = sp.symbols('d1 d2 l1 l2 x', positive=True)
q = -d1*x**2 - d2*(r-x)**2 + l1*x + l2*(r-x)
xs = sp.solve(sp.diff(q, x), x)[0]
val = sp.simplify(q.subs(x, xs))
form = -d1*d2/(d1+d2)*r**2 + (d2*l1+d1*l2)/(d1+d2)*r + (l1-l2)**2/(4*(d1+d2))
chk("radial max formula e,f,g", sp.simplify(val-form) == 0)
def efg(D1, D2, L1, L2):
    return D1*D2/(D1+D2), (D2*L1+D1*L2)/(D1+D2), (L1-L2)**2/(4*(D1+D2))
cH = F(47, 192)*F(1699, 125)
chk("E07g half-near d1>52/25 d2>123/40", cH-F(4, 9)-F(77, 96) > F(52, 25) and cH-F(1, 6)-F(1, 12) > F(123, 40), float(cH-F(4, 9)-F(77, 96)), float(cH-F(1, 4)))
chk("E07g half-near linears", F(7, 15)+F(77, 96)/4 == F(427, 640) and F(7, 15)+F(1, 12)/4 == F(39, 80))
e, f, g = efg(F(52, 25), F(123, 40), F(427, 640), F(39, 80))
chk("E07g half-near e=6396/5155>31/25 f<3/5 g=26450/16891904<1/625", e == F(6396, 5155) and e > F(31, 25) and f < F(3, 5) and g == F(26450, 16891904) and g < F(1, 625), float(f), float(g))
chk("E07g half-near C4+g<1/100", F(83, 10000)+F(1, 625) < F(1, 100))
q7 = sp.expand(sp.Rational(14, 125)-sp.Rational(12, 125)*r-sp.Rational(57, 2000)*r**2 - (sp.Rational(1, 100)+sp.Rational(3, 5)*r-sp.Rational(31, 25)*r**2))
chk("E07g (7) polynomial", sp.simplify(q7-(sp.Rational(51, 500)-sp.Rational(87, 125)*r+sp.Rational(2423, 2000)*r**2)) == 0)
chk("E07g (7) min > 1/500 (disc)", 4*F(2423, 2000)*F(1, 10) > F(87, 125)**2 and 4*F(2423, 2000)*F(1, 10)*78125000 == 37859375 and F(87, 125)**2*78125000 == 37845000)
# BOX
cB = F(47, 192)*F(1699, 125)
d1b, d2b = cB-F(7, 15)-F(17, 20), cB-F(7, 40)-F(7, 80)
chk("E07g BOX curvatures >2, >3", d1b > 2 and d2b > 3, float(d1b), float(d2b))
chk("E07g BOX linears", F(99, 200)+F(17, 20)/4 == F(283, 400) and F(99, 200)+F(7, 80)/4 == F(827, 1600))
e, f, g = efg(F(2), F(3), F(283, 400), F(827, 1600))
chk("E07g BOX e=6/5 f=101/160<16/25 g<19/10000; C4+g<11/1000", e == F(6, 5) and f == F(101, 160) and f < F(16, 25) and g < F(19, 10000) and F(83, 10000)+F(19, 10000) < F(11, 1000))
qb = lambda x: F(11, 1000)+F(16, 25)*x-F(6, 5)*x*x
chk("E07g BOX values at 1/2,3/5", qb(F(1, 2)) == F(31, 1000) and qb(F(3, 5)) == F(-37, 1000))
# LARGE (D24, r<=3/4)
cL = F(61, 256)*F(1699, 125)
chk("E07g cosine 61/256 = 1/4-(3/4)^2/48", F(1, 4)-F(9, 16)/48 == F(61, 256))
d1l = cL - F(1, 2) - F(109, 120)*F(5, 6); d2l = cL - F(3, 16) - F(3, 32)*F(5, 4)
chk("E07g LARGE curvatures >19/10, >29/10", d1l > F(19, 10) and d2l > F(29, 10), float(d1l), float(d2l))
l1L, l2L = F(99, 200)+F(109, 120)*F(3, 10), F(99, 200)+F(3, 32)*F(1, 5)
chk("E07g LARGE linears 307/400, 411/800", l1L == F(307, 400) and l2L == F(411, 800))
bx = -F(19, 10)/4 + l1L/2 + F(1, 100); ymax = l2L**2/(4*F(29, 10))
chk("E07g LARGE x>=1/2 boundary+C4 <= -13/160, ymax<1/40", bx <= F(-13, 160) and ymax < F(1, 40), bx, float(ymax))
by = -F(29, 10)/4 + l2L/2 + F(1, 100); xmax = l1L**2/(4*F(19, 10))
chk("E07g LARGE y>=1/2 boundary+C4 <= -733/1600, xmax<2/25", by <= F(-733, 1600) and xmax < F(2, 25), by, float(xmax))
# FAR
cF = F(11, 48)*F(1699, 125)
d1f, d2f = cF-F(8, 15)-F(5, 6), cF-F(1, 5)-F(1, 10)*F(5, 4)
chk("E07g FAR curvatures >87/50, >139/50", d1f > F(87, 50) and d2f > F(139, 50), float(d1f), float(d2f))
e, f, g = efg(F(87, 50), F(139, 50), F(159, 200), F(103, 200))
chk("E07g FAR e=12093/11300 f<69/100 g<11/2500, C4+g<13/1000", e == F(12093, 11300) and f < F(69, 100) and g < F(11, 2500) and F(83, 10000)+F(11, 2500) < F(13, 1000), float(f), float(g))
qf = lambda x: F(13, 1000)+F(69, 100)*x-F(107, 100)*x*x
chk("E07g FAR (9) at 3/4 = -571/8000", qf(F(3, 4)) == F(-571, 8000))
GO = u1*F(69, 5)-F(101, 250)-F(81, 100)-F(3, 25)-F(3, 10)
chk("E07g (10) GO_H = 881/16000 > 1/20", GO == F(881, 16000) and GO > F(1, 20))
print("SUMMARY", sum(1 for _, ok in res if ok), "/", len(res), "PASS")
