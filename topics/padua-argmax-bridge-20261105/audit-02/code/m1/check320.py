#!/usr/bin/env python3
"""Independent exact-Fraction recomputation of the E14 global320 scalar chain.

Auditor: Claude (Opus 5.5, xhigh), interim audit 10, 2026-11-07.
Rigour: every claimed rational inequality is re-checked in exact Fraction
arithmetic from independently derived rational enclosures of log2, log(5/4),
pi.  pi enclosure 157/50 < pi < 22/7 is the standard inherited one.
Prints PASS/FAIL lines plus exact slacks.  Exit code 1 on any FAIL.
"""
from fractions import Fraction as F
import sys

FAILS = []
def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" :: " + detail) if detail else ""))
    if not cond:
        FAILS.append(name)

def slack(a, b):
    """return b-a as fraction and float"""
    d = b - a
    return f"slack={d} (~{float(d):.3e})"

# ---------- rational enclosures (own derivation) ----------
def atanh_bounds(x, kmax):
    """2*atanh(x) = 2*sum x^(2k+1)/(2k+1); lower=partial sum k<=kmax,
    upper = lower + 2*x^(2kmax+3)/((2kmax+3)(1-x^2))  (tail with denominators
    replaced by the first omitted odd denominator)."""
    s = F(0)
    for k in range(kmax + 1):
        s += x ** (2 * k + 1) / (2 * k + 1)
    lo = 2 * s
    tail = 2 * x ** (2 * kmax + 3) / ((2 * kmax + 3) * (1 - x * x))
    return lo, lo + tail

l2lo, l2hi = atanh_bounds(F(1, 3), 3)        # terms up to x^7
l54lo, l54hi = atanh_bounds(F(1, 9), 1)      # terms up to x^3
# certificate stated in E14-halfnear320 sec.3
chk("log2 lower cert = 842/1215+2/15309", l2lo == F(842, 1215) + F(2, 15309), str(l2lo))
chk("log2 tail cert <= 1/78732 (their tail uses odd denom 9)",
    l2hi - l2lo <= F(1, 78732), f"own tail {l2hi-l2lo} vs 1/78732")
# their tail: denominators replaced by 9 -> 2*3^-9/(9*(1-1/9)) = 1/78732 exactly
chk("log2 their tail value", 2 * F(1, 3**9) / (9 * (1 - F(1, 9))) == F(1, 78732))
chk("log(5/4) lower cert = 488/2187", l54lo == F(488, 2187))
chk("log(5/4) their tail value", 2 * F(1, 9**5) / (5 * (1 - F(1, 81))) == F(1, 145800))
L2LO, L2HI = F(842, 1215) + F(2, 15309), F(842, 1215) + F(2, 15309) + F(1, 78732)
L54LO, L54HI = F(488, 2187), F(488, 2187) + F(1, 145800)
chk("6931/10000<log2", F(6931, 10000) < L2LO, slack(F(6931, 10000), L2LO))
chk("log2<69315/100000", L2HI < F(69315, 100000), slack(L2HI, F(69315, 100000)))
chk("2231/10000<log5/4", F(2231, 10000) < L54LO, slack(F(2231, 10000), L54LO))
chk("log5/4<22315/100000", L54HI < F(22315, 100000), slack(L54HI, F(22315, 100000)))

n = F(320)
LLO = 8 * L2LO + L54LO
LHI = 8 * L2HI + L54HI
chk("57679/10000<L320", F(57679, 10000) < LLO, slack(F(57679, 10000), LLO))
chk("L320<5769/1000", LHI < F(5769, 1000), slack(LHI, F(5769, 1000)))
# use the stated (weaker) rational bounds from here, as the proof does
Llo, Lhi = F(57679, 10000), F(5769, 1000)
Hlo, Hhi = 1 + Llo, 1 + Lhi
chk("H<6769/1000", Hhi <= F(6769, 1000))
PILO, PIHI = F(157, 50), F(22, 7)
PI2LO, PI2HI = F(197, 20), PIHI ** 2
chk("pi^2>197/20 from 157/50", PILO ** 2 > F(197, 20), str(PILO ** 2))
b_hi = 4 / PI2LO  # 4/pi^2 upper
chk("b=4/pi^2<41/100", b_hi < F(41, 100), str(b_hi))
# hr = log(5/2)+1/18 < 1
hr_hi = L2HI + L54HI + F(1, 18)
chk("hr=log(5/2)+1/18<1", hr_hi < 1, str(float(hr_hi)))

# ---------- halfnear320 section 3 component bounds ----------
T_lo = (4 * Llo ** 2 - 3 * Llo) / PI2HI
chk("T>293/25 (E14-halfnear (7))", T_lo > F(293, 25), slack(F(293, 25), T_lo))
chk("T numerator 567277810036/48400000000", T_lo == F(567277810036, 48400000000), str(T_lo))
D_hi = ((52 / PI2LO) * Hhi + 7) / n + 10 / n ** 2 + 20 * Hhi / (PILO * n ** 2)
chk("D<27/200", D_hi < F(27, 200), slack(D_hi, F(27, 200)))
chk("D cert form equals ours", D_hi == ((F(1040, 197) * F(6769, 1000) + 7) / 320 + (10 + F(6769, 157)) / 320 ** 2))
# Mesh: b(2L+2hr)/n+[4+b(L+1/n)]/(4n^2-1)+b/(2n-1)^2+[5+b(log(n+1/2)+2)]/[4(n-1/2)^2]
logn_half_hi = Lhi + F(1, 2) / n  # log(n+1/2)<=log n + 1/(2n)
mesh_lead = b_hi * (2 * Lhi + 2 * 1) / n   # hr<1
mesh_tail = (4 + b_hi * (Lhi + 1 / n)) / (4 * n ** 2 - 1) + b_hi / (2 * n - 1) ** 2 \
    + (5 + b_hi * (logn_half_hi + 2)) / (4 * (n - F(1, 2)) ** 2)
chk("Mesh three tails <14/n^2", mesh_tail < 14 / n ** 2, f"tails*n^2={float(mesh_tail*n**2):.4f}")
Mesh_hi = mesh_lead + mesh_tail
chk("Mesh<7/400 (with their 41/100 lead)", F(41, 100) * (2 * Lhi + 2) / n + 14 / n ** 2 < F(7, 400),
    slack(F(41, 100) * (2 * Lhi + 2) / n + 14 / n ** 2, F(7, 400)))
ebar_hi = F(27, 200) + F(7, 400) + 1 / n
chk("ebar<249/1600", ebar_hi <= F(249, 1600), str(ebar_hi))
chk("ebar<5/32 (outer)", F(249, 1600) < F(5, 32))
A4_lo = 4 / n
A4_hi = 4 / n + 40 * Hhi / (PILO * n ** 2)
C4_hi = A4_hi + 20 / n ** 2
chk("C4<677/50000", C4_hi < F(677, 50000), slack(C4_hi, F(677, 50000)))
# their C4 cert with pi>3:
C4_hi3 = 4 / n + 40 * Hhi / (3 * n ** 2) + 20 / n ** 2
print("INFO (own exploratory variant, NOT a claim of the record; record uses pi>157/50): C4 with pi>3 bound", float(C4_hi3), "vs 677/50000", float(F(677,50000)))
chk("C4 excess over 1/80 = 16678/16076800 <13/12500 (record cert, pi>157/50)", C4_hi - F(1,80) == F(16678,16076800) and F(16678,16076800) < F(13,12500))
db_hi = (17 * Lhi + 27) / n ** 2
kNx_hi = (F(19, 2) * Hhi + F(23, 3) * Lhi + F(677, 10)) / n + 82 / n ** 2
kNy_hi = kNx_hi + db_hi
chk("kNx<11031/20000", kNx_hi < F(11031, 20000), slack(kNx_hi, F(11031, 20000)))
chk("kNx cert =705963/1280000", kNx_hi == F(705963, 1280000), str(kNx_hi))
chk("kNy<11056/20000", kNy_hi < F(11056, 20000), slack(kNy_hi, F(11056, 20000)))
chk("kNy cert =56602113/102400000", kNy_hi == F(56602113, 102400000), str(kNy_hi))
JN_lo = (F(3, 2) * F(27, 4) + F(16, 5)) / n + 78 / n ** 2
chk("H>27/4", Hlo > F(27, 4))
chk("JN>2171/51200", JN_lo >= F(2171, 51200), str(JN_lo))
chk("JN>21/500", JN_lo > F(21, 500))
j_lo = F(23, 250)  # inherited E06 (PD-T271 dependent)
U0 = F(293, 25) - F(249, 1600) + F(1, 80) + j_lo
chk("U0>23337/2000 (halfnear (8))", U0 > F(23337, 2000), slack(F(23337, 2000), U0))

# ---------- halfnear section 1: beta0 ----------
beta0 = F(23, 24) * 1 * (F(69, 100) + F(3, 2)) / 10
chk("beta0=5037/24000=1679/8000", beta0 == F(5037, 24000) == F(1679, 8000))
# u >= 47/192 (x^2+y^2) for x,y<=1/2: 1-cos x >= x^2/2-x^4/24 >= x^2(1/2-1/96)
chk("47/192 cosine constant", (F(1, 2) - F(1, 4) / 24) / 2 == F(47, 192))
# Ec <= (3/8)x^(3/2): kappa/sqrt(a) with kappa<9/25 (E12: 638/1773<9/25), a>=cos^2(1/4)>=(31/32)^2
kap_hi = 4 * F(319, 360) / PI2LO
chk("kappa<638/1773<9/25", kap_hi == F(638, 1773) and kap_hi < F(9, 25), str(kap_hi))
chk("halfnear 3/8 >= kappa/cos(1/4) using cos(1/4)>=31/32", kap_hi * F(32, 31) < F(3, 8),
    slack(kap_hi * F(32, 31), F(3, 8)))
chk("annular 5/12 >= kappa/cos(1/2) using cos(1/2)>=7/8", kap_hi * F(8, 7) < F(5, 12),
    slack(kap_hi * F(8, 7), F(5, 12)))

# ---------- halfnear section 4 floors ----------
p = F(22, 7)
def Ah_(nn): return F(539, 1936) * F(2303, 5000) - F(140, 157) * F(97, 100) / nn - F(400, 157) * F(4837, 1875) / nn - F(800, 3) * F(97, 100) / nn ** 2
def Bh_(nn): return F(539, 1936) * F(471, 1250) - F(140, 157) * F(1, 2) / nn - F(400, 157) * F(5, 3) / nn - F(800, 3) * F(1, 2) / nn ** 2
def Aw_(nn): return F(539, 1936) * F(5369, 15000) - F(140, 157) * F(97, 100) / nn - F(400, 157) * F(37621, 15000) / nn - F(800, 3) * F(97, 100) / nn ** 2
def Bw_(nn): return F(539, 1936) * F(7379, 30000) - F(140, 157) * F(1, 2) / nn - F(400, 157) * F(3, 2) / nn - F(800, 3) * F(1, 2) / nn ** 2
Ah, Bh, Aw, Bw = Ah_(n), Bh_(n), Aw_(n), Bw_(n)
chk("Ah exact = stated four-piece form", Ah == F(1241317, 9680000) - F(679, 251200) - F(77392, 3768000) - F(97, 38400), str(Ah))
chk("Bh exact = stated", Bh == F(253869, 2420000) - F(35, 25120) - F(2000, 150720) - F(1, 768), str(Bh))
chk("Aw exact = stated", Aw == F(2893891, 29040000) - F(679, 251200) - F(75242, 3768000) - F(97, 38400), str(Aw))
chk("Bw exact = stated", Bw == F(3977281, 58080000) - F(35, 25120) - F(15, 1256) - F(1, 768), str(Bw))
chk("5123/50000<Ah<1281/12500", F(5123, 50000) < Ah < F(1281, 12500), f"Ah={float(Ah):.7f}")
chk("0<Bh<4447/50000", 0 < Bh < F(4447, 50000), f"Bh={float(Bh):.7f}")
chk("37/500<Aw<3/40", F(37, 500) < Aw < F(3, 40), f"Aw={float(Aw):.7f}")
chk("0<Bw<27/500", 0 < Bw < F(27, 500), f"Bw={float(Bw):.7f}")
chk("74451<1e6Aw<74455", 74451 < Aw * 10 ** 6 < 74455, f"{float(Aw*10**6):.3f}")
chk("53839<1e6Bw<53843", 53839 < Bw * 10 ** 6 < 53843, f"{float(Bw*10**6):.3f}")
def ar(r): return 1 - r * r / 4
def eta(r, nn): return ar(r) * (1 - (4 * p + r) / nn) - r / 2
def Fn(r, nn): return 2 * eta(r, nn) / (p + r) * (nn / (nn + 1)) * (F(1, 4) - 1 / nn)
def Fs(r, nn): return F(35, 286) * (1 - 6 / nn) ** 2 * (ar(r) - r / 2)
def Fh(r, nn): return Ah_(nn) * ar(r) - Bh_(nn) * r
def Fw(r, nn): return Aw_(nn) * ar(r) - Bw_(nn) * r
chk("158/321 factor", 2 * (n / (n + 1)) * (F(1, 4) - 1 / n) == F(158, 321))
# halfnear (9): Fh > Lh
def Lh(r): return F(5123, 50000) - F(4447, 50000) * r - F(1281, 50000) * r * r
# Lh - (Ah a_r - Bh r) <0 : coefficientwise
chk("Fh>Lh coefficientwise (r>=0)", Ah > F(5123, 50000) and Ah / 4 < F(1281, 50000) and Bh < F(4447, 50000))
# halfnear Fn,Fs >= (11/100)(a-r/2) on r<=1/2; check exact at grid + monotone argument
def minover(f, a, b, N=2000):
    return min(f(a + (b - a) * F(k, N)) for k in range(N + 1))
m_n = minover(lambda r: Fn(r, n) - F(11, 100) * (ar(r) - r / 2), F(0), F(1, 2), 400)
m_s = minover(lambda r: Fs(r, n) - F(11, 100) * (ar(r) - r / 2), F(0), F(1, 2), 400)
chk("[grid] Fn-(11/100)(a-r/2)>0 on [0,1/2]", m_n > 0, f"min~{float(m_n):.3e}")
chk("[grid] Fs-(11/100)(a-r/2)>0 on [0,1/2]", m_s > 0, f"min~{float(m_s):.3e}")
# exact algebraic: Fs coefficient
chk("Fs coef (35/286)(157/160)^2>11/100", F(35, 286) * F(157, 160) ** 2 > F(11, 100), str(float(F(35, 286) * F(157, 160) ** 2)))
# (11/100)(a-r/2) - Lh = 377/50000+1697r/50000-94r^2/50000
dd = lambda r: F(11, 100) * (ar(r) - r / 2) - Lh(r)
chk("(11/100)(a-r/2)-Lh identity", all(dd(F(k, 7)) == F(377, 50000) + F(1697, 50000) * F(k, 7) - F(94, 50000) * F(k, 7) ** 2 for k in range(5)))
chk("377+1697r-94r^2>0 on [0,1/2]", F(377) - 94 * F(1, 4) > 0)
# exact eta claim halfnear: eta>(959/1000)a_r - r/2 on r<=1/2: 1-(4p+1/2)/320 > 959/1000
chk("1-(4p+1/2)/320>959/1000", 1 - (4 * p + F(1, 2)) / n > F(959, 1000), str(1 - (4 * p + F(1, 2)) / n))
chk("p+1/2<=51/14", p + F(1, 2) <= F(51, 14))
chk("(158/321)/(51/14)>27/200 (442400>442017)", F(158, 321) / F(51, 14) > F(27, 200) and 158 * 14 * 200 == 442400 and 27 * 321 * 51 == 442017)

# ---------- halfnear section 5 quadratic ----------
def line_max(d1, d2, l1, l2):
    e = d1 * d2 / (d1 + d2)
    f = (d2 * l1 + d1 * l2) / (d1 + d2)
    g = (l1 - l2) ** 2 / (4 * (d1 + d2))
    return e, f, g
crv = F(47, 192) * (F(23337, 2000) + F(21, 500) * F(1, 8))
chk("(47/192)U>1143/400 on r>=1/8", crv > F(1143, 400), slack(F(1143, 400), crv))
d1, d2 = F(1143, 400) - F(15, 32), F(1143, 400) + F(1679, 8000)
chk("d1=1911/800,d2=24539/8000", d1 == F(1911, 800) and d2 == F(24539, 8000))
l1, l2 = F(11031, 20000) + F(3, 40), F(11056, 20000)
chk("l1=12531/20000", l1 == F(12531, 20000))
# tangent sqrt(x)<=(5/4)x+1/5: (3/8)x^(3/2)<=(15/32)x^2+(3/40)x
chk("tangent coeffs 15/32,3/40", F(3, 8) * F(5, 4) == F(15, 32) and F(3, 8) * F(1, 5) == F(3, 40))
e, f, g = line_max(d1, d2, l1, l2)
chk("e>13429/10000", e > F(13429, 10000), slack(F(13429, 10000), e))
chk("f<29714/50000", f < F(29714, 50000), slack(f, F(29714, 50000)))
chk("g<1/4000", g < F(1, 4000), slack(g, F(1, 4000)))
chk("halfnear exact e,g", e == F(468940290, 349192000) and g == F(3481, 13967680))
chk("C4+g<1379/100000", F(677, 50000) + g < F(1379, 100000), slack(F(677, 50000) + g, F(1379, 100000)))
# difference poly min
A2, A1, A0c = F(8233, 6250), F(-34161, 50000), F(8867, 100000)
mn = A0c - A1 ** 2 / (4 * A2)
chk("min_r[Lh-upper]>1/20000", mn > F(1, 20000), f"min={mn} (~{float(mn):.6e}); slack {float(mn-F(1,20000)):.3e}")
chk("integer comparison 34161^2<32*8233*4431", 34161 ** 2 == 1166973921 and 32 * 8233 * 4431 == 1167373536 and 34161 ** 2 < 32 * 8233 * 4431)
# r<=1/8 branch
dmin = min(F(23337, 2000) * F(47, 192) - F(15, 32), F(23337, 2000) * F(47, 192) + F(1679, 8000))
chk("both curvatures >2 for r<=1/8", dmin > 2, str(float(dmin)))
chk("l1,l2<=627/1000", l1 < F(627, 1000) and l2 < F(627, 1000))
v18 = F(677, 50000) + F(627, 1000) * F(1, 8) - F(1, 64)
chk("upper at r=1/8 <77/1000", v18 < F(77, 1000), str(float(v18)))
chk("Lh(1/8)>9/100", Lh(F(1, 8)) > F(9, 100), str(float(Lh(F(1, 8)))))
chk("r<=1/8 gap >13/1000", F(9, 100) - F(77, 1000) >= F(13, 1000))

# ---------- annular320 ----------
kWx_hi = (F(19, 2) * Hhi + F(23, 3) * Lhi + F(155, 2)) / n + 152 / n ** 2
kWy_hi = kWx_hi + db_hi
chk("kWx cert =373019/640000", kWx_hi == F(373019, 640000), str(kWx_hi))
chk("kWx<583/1000", kWx_hi < F(583, 1000), slack(kWx_hi, F(583, 1000)))
chk("kWy cert =59808113/102400000", kWy_hi == F(59808113, 102400000), str(kWy_hi))
chk("kWy<117/200", kWy_hi < F(117, 200), slack(kWy_hi, F(117, 200)))
chk("leading numerator 372069/2000", F(19, 2) * Hhi + F(23, 3) * Lhi + F(155, 2) == F(372069, 2000))
chk("constants 6+10+11+50+1/2=155/2", 6 + 10 + 11 + 50 + F(1, 2) == F(155, 2))
chk("148+4=152", 148 + 4 == 152)
TEJ = F(293, 25) - F(249, 1600) + F(23, 250)
chk("T-ebar+j>2331/200", TEJ > F(2331, 200), slack(F(2331, 200), TEJ))
chk("(11/48)(2331/200)>8/3 slack 41/9600", F(11, 48) * F(2331, 200) - F(8, 3) == F(41, 9600))
chk("11/48 cosine const on x<=1", (F(1, 2) - F(1, 24)) / 2 == F(11, 48))
d1, d2 = F(8, 3) - F(5, 12), F(8, 3)
chk("d1=9/4", d1 == F(9, 4))
l1c = F(583, 1000) + F(5, 48)
chk("l1=kWx+5/48<11/16", l1c < F(11, 16), slack(l1c, F(11, 16)))
chk("kWy<47/80", F(117, 200) < F(47, 80))
l1, l2 = F(11, 16), F(47, 80)
e, f, g = line_max(d1, d2, l1, l2)
chk("e=72/59>61/50", e == F(72, 59) and e > F(61, 50), slack(F(61, 50), e))
chk("f=3029/4720<257/400", f == F(3029, 4720) and f < F(257, 400), slack(f, F(257, 400)))
chk("g=3/5900", g == F(3, 5900))
chk("C4+g<141/10000", F(677, 50000) + g < F(141, 10000), slack(F(677, 50000) + g, F(141, 10000)))
def P(r): return F(141, 10000) + F(257, 400) * r - F(61, 50) * r * r
chk("P(1/2)=607/20000", P(F(1, 2)) == F(607, 20000))
chk("P(3/5)=-99/2500", P(F(3, 5)) == F(-99, 2500))
chk("P(1)", True, f"P(1)={P(F(1))} ~{float(P(F(1))):.4f}")
chk("P decreasing for r>=1/2 (vertex<1/2)", F(257, 400) / (2 * F(61, 50)) < F(1, 2), str(float(F(257, 400) / (2 * F(61, 50)))))
# floors on annulus
chk("1-(4p+3/5)/320=10739/11200>19/20", 1 - (4 * p + F(3, 5)) / n == F(10739, 11200) and F(10739, 11200) > F(19, 20))
chk("p+3/5<4", p + F(3, 5) < 4)
chk("158/(4*321)>3/25", F(158, 4 * 321) > F(3, 25))
chk("(3/25)(19/20)-(9/100) = 3/125", F(3, 25) * F(19, 20) - F(9, 100) == F(3, 125))
chk("3a/125-3r/200>0 at r=3/5", F(3, 125) * ar(F(3, 5)) - F(3, 200) * F(3, 5) > 0)
chk("(9/100)(a-r/2) at 3/5 = 549/10000", F(9, 100) * (ar(F(3, 5)) - F(3, 10)) == F(549, 10000))
chk("Fs coef at 320 (35/286)(157/160)^2>11/100>9/100", F(35, 286) * F(157, 160) ** 2 > F(11, 100))
# exact endpoint values of the actual floors (decreasing in r)
for nm, fn, rr in (("Fn", Fn, F(3, 5)), ("Fs", Fs, F(3, 5)), ("Fh", Fh, F(21, 40)), ("Fw", Fw, F(3, 5))):
    v = fn(rr, n)
    chk(f"exact {nm}({rr}) at 320 >17/500", v > F(17, 500), f"value~{float(v):.6f}, slack~{float(v-F(17,500)):.3e}")
chk("Fh(rB) lower bound (9)", F(5123, 50000) * ar(F(21, 40)) - F(4447, 50000) * F(21, 40) > F(17, 500),
    f"~{float(F(5123, 50000) * ar(F(21, 40)) - F(4447, 50000) * F(21, 40)):.6f}")
FwL = lambda r: F(37, 500) - F(27, 500) * r - F(3, 160) * r * r
chk("Fw lower (10) at 3/5 = 697/20000", FwL(F(3, 5)) == F(697, 20000))
chk("37/500*a_r - 27r/500 >= FwL (37/2000<=3/160)", F(37, 2000) <= F(3, 160))
chk("annular gap 17/500-607/20000=73/20000>3/1000", F(17, 500) - F(607, 20000) == F(73, 20000) and F(73, 20000) > F(3, 1000))
# positivity of A0,Rh,Rw on [0,3/5] (needed for loss monotonicity in n)
for nm, fun in (("A0", lambda r: F(97, 100) * ar(r) - r / 2), ("Rh", lambda r: F(4837, 1875) * ar(r) - F(5, 3) * r),
                ("Rw", lambda r: F(37621, 15000) * ar(r) - F(3, 2) * r), ("Ih", lambda r: F(2303, 5000) * ar(r) - F(471, 1250) * r),
                ("Iw", lambda r: F(5369, 15000) * ar(r) - F(7379, 30000) * r)):
    chk(f"{nm}>0 on [0,3/5] (decreasing, value at 3/5)", fun(F(3, 5)) > 0, f"{float(fun(F(3,5))):.4f}")
chk("eta(3/5,320)>0", eta(F(3, 5), n) > 0)

# ---------- assembly node lower (redundant) ----------
chk("4L^2/pi^2-ebar>1 at 320 (pi^2<10)", 4 * Llo ** 2 / 10 - F(249, 1600) > 1, f"~{float(4*Llo**2/10):.3f}")

# ---------- outer320 final system ----------
u1, jS, tS, p0, P0, eta_ = F(47, 384), F(23, 250), F(221, 500), F(12, 25), F(24, 25), F(3, 2)
Cb, KDh, eb5, Cs, Cl = F(209, 250), F(1, 6), F(5, 32), F(71, 100), F(7, 20)
Gb = u1 * (F(293, 25) + jS) - tS * p0 - Cb - P0 * KDh - eb5
chk("Gb = 195191/2400000", Gb == F(195191, 2400000), str(Gb))
chk("Gb>3/40", Gb > F(3, 40), slack(F(3, 40), Gb))
Kk = F(293, 25) + jS - Cl - 4 * KDh
chk("K>10", Kk > 10, str(float(Kk)))
Aa = eta_ * tS + Cs
chk("A<7/5", Aa < F(7, 5), str(float(Aa)))
Ff = F(3, 40) - F(7, 5) ** 2 / 40
chk("F>=13/500 from 3/40-(7/5)^2/40", Ff == F(13, 500))
Fexact = Gb - Aa ** 2 / (4 * Kk)
chk("F with own sharper K,A >13/500", Fexact > F(13, 500), f"~{float(Fexact):.5f}")
chk("Cb sum 3/25+9/25+17/50+2/125=209/250", F(3, 25) + F(9, 25) + F(17, 50) + F(2, 125) == F(209, 250))
chk("Cs (3/2)(41/100)+3(3/500+3/125)=141/200<71/100", F(3, 2) * F(41, 100) + 3 * (F(3, 500) + F(3, 125)) == F(141, 200) < F(71, 100))
chk("t*>=t0: 221/500 > 2log2/pi (log2<69315/100000, pi>157/50)", 2 * F(69315, 100000) / PILO < F(221, 500), str(float(2 * F(69315, 100000) / PILO)))
chk("u1<1-cos(1/2): 1-cos(1/2)>1/8-1/384 = 47/384 exactly (alt. series lower)", F(1, 8) - F(1, 384) == F(47, 384))

# ---------- E12 corner256 headline arithmetic ----------
q0, rU = F(7, 48), F(2, 125)
chk("cos(pi/4)<17/24 (576<578)", 24 ** 2 < 2 * 17 ** 2)
chk("q0=(1-17/24)/2 = 7/48", (1 - F(17, 24)) / 2 == F(7, 48))
dA = q0 * (F(107, 10) - F(1, 5) + F(23, 250)) - F(1, 4) - F(9, 500) - F(11, 14) * F(93, 100)
chk("delta_A>2293/4200", dA == F(2293, 4200), str(dA))
FA = dA - rU * 26
chk("FA = 2729/21000 >1/8", FA == F(2729, 21000) and FA > F(1, 8))
dD = 2 * q0 * (F(107, 10) + F(23, 250)) - F(4, 15) - F(3, 2) - F(3, 2) * F(1, 5) - F(1, 5)
chk("delta_D=881/1000", dD == F(881, 1000), str(dD))
FD = dD - 2 * rU * 26
chk("FD=49/1000", FD == F(49, 1000))
chk("min(FA,FD/2)=49/2000", min(FA, FD / 2) == F(49, 2000))
chk("(8/5)(49/2000)=49/1250>1/30", F(8, 5) * F(49, 2000) == F(49, 1250) > F(1, 30))
chk("16/pi^2>8/5", 16 / F(10) == F(8, 5))
chk("rU>pi^4/6144: 125*22^4<2*7^4*6144", 125 * 22 ** 4 < 2 * 7 ** 4 * 6144)
chk("8(q0-rU)=779/750>1", 8 * (q0 - rU) == F(779, 750))
chk("3q0+(79/5)rU=6903/10000<7/10", 3 * q0 + F(79, 5) * rU == F(6903, 10000))
# 256 log bounds
l2lo2 = F(842, 1215); l2hi2 = F(842, 1215) + F(1, 6804)
chk("log2 256-cert: tail after x^5 term <=1/6804", 2 * F(1, 3 ** 7) / (7 * (1 - F(1, 9))) <= F(1, 6804), str(2 * F(1, 3 ** 7) / (7 * (1 - F(1, 9)))))
chk("8*log2 in (277/50,111/20)", 8 * l2lo2 > F(277, 50) and 8 * l2hi2 < F(111, 20))
T256 = (4 * F(277, 50) ** 2 - 3 * F(277, 50)) / PI2HI
chk("T256>107/10", T256 > F(107, 10), str(T256))

print("\nFAILS:", FAILS)
sys.exit(1 if FAILS else 0)
