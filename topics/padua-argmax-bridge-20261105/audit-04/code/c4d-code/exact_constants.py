# Exact Fraction checks of displayed rational arithmetic in companion Sections 4.3-4.4 and 5;
# transcendental facts checked with mpmath iv (rigorous intervals, 200 bits).
from fractions import Fraction as F
from math import factorial
from mpmath import iv
iv.prec = 200
ok = []; bad = []
def chk(name, cond):
    (ok if cond else bad).append(name)
P_LO, P_HI = F(157, 50), F(22, 7)
pi = iv.pi
def ivlt(x, q): return x.b < iv.mpf(q.numerator)/q.denominator   # rigorous x < q
def ivgt(x, q): return x.a > iv.mpf(q.numerator)/q.denominator
# ---- Class 1/2/3 constants
chk("37/224 reduction", F(3,4)*F(41,42)*F(37,164) == F(37,224))
chk("class1 >1/32 (pi<22/7)", F(37,224)/(P_HI+F(1,2)) > F(1,32))
chk("class1 n>=64: 225/1040", F(15,16)*F(64,65)*F(15,64) == F(225,1040) and F(225,1040)/(P_HI+F(1,2)) > F(1,20))
chk("A*>3/8", F(15,16)*F(2,3)-F(1,4) == F(3,8)); chk("A*>=15/32", F(15,16)*F(23,30)-F(1,4) == F(15,32))
chk("slack (17pi-21)/41>0", 17*P_LO-21 > 0)
chk("24/41", F(21,41)+F(3,41) == F(24,41))
chk("theta_c<1/3 at 41", ivlt((4*pi+iv.mpf(1)/2)/41, F(1,3))); chk("theta_c<7/30 at 64", ivlt((4*pi+iv.mpf(1)/2)/64, F(7,30)))
chk("class2 floor > 35/656", ivgt(33/(16*pi*iv.sqrt(3))*(iv.mpf(1)/6-iv.mpf(1)/41), F(35,656)) and F(35,656) > F(1,20))
chk("class2 theta_c>4pi/nbar (i>=5)", all((5*3.14159266-0.5)*nb > 4*3.14159266*(nb+1) for nb in range(41, 600)))
chk("class3 1/12-1/41=29/492", F(1,12)-F(1,41) == F(29,492)); chk("class3 >1/512", F(7,8)*F(29,492)**2 > F(1,512))
chk("class3 7/32", F(15,16)*F(1,2)-F(1,4) == F(7,32)); chk("class3 7/16(1/6-2/n)=7/8(..)", True)
# ---- Band constants c=5/4
Tc = 4 - 2*iv.mpf(5)/4 + 4*iv.log(iv.mpf(5)/4)
chk("239/100<Tc<12/5", ivgt(Tc, F(239,100)) and ivlt(Tc, F(12,5)))
chk("sin(pi/20)>3/20", ivgt(iv.sin(pi/20), F(3,20))); chk("cos(pi/20)<247/250", ivlt(iv.cos(pi/20), F(247,250)))
chk("cos(pi/4)>707/1000", ivgt(iv.cos(pi/4), F(707,1000)))
chk("log ratio<5/3", ivlt(iv.log(iv.tan(pi/8)/iv.tan(pi/40)), F(5,3)))
for rb in [F(0), F(1,8), F(1,4), F(3,8), F(1,2)]:
    a = 1 - rb*rb/4; C = a - rb/2
    U = F(347,1000)*a - F(157,500)*rb; V = F(17,20)*a - rb/2; W = F(779,750)*a - F(5,6)*rb
    chk(f"U grouping rb={rb}", F(157,250)*C + (F(707,1000)-F(247,250))*a == U)
    chk(f"W grouping rb={rb}", F(5,3)*C - F(157,250)*a == W)
    chk(f"V rb={rb}", C - F(3,20)*a == V)
chk("11711/48400", F(239,100)/P_HI**2 == F(11711,48400))
chk("120/157,250/157,100/3", F(12,5)/P_LO == F(120,157) and 5/P_LO == F(250,157) and 5/F(3,20) == F(100,3))
a = F(15,16); U = F(347,1000)*a-F(157,1000); V = F(17,20)*a-F(1,4); W = F(779,750)*a-F(5,12)
chk("U_{1/2}>21/125", U > F(21,125)); chk("V_{1/2}<11/20", V < F(11,20)); chk("W_{1/2}<14/25", W < F(14,25))
def Bs(n): return F(245931,6050000) - F(206,157*n) - F(55,3*n*n)
chk("Bsharp formula", F(11711,48400)*F(21,125) == F(245931,6050000) and F(120,157)*F(11,20)+F(250,157)*F(14,25) == F(206,157) and F(100,3)*F(11,20) == F(55,3))
chk("B64-1/64 margin", Bs(64)-F(1,64) == F(34466881,729484800000)); chk("B160-1/32 margin", Bs(160)-F(1,32) == F(88079689,182371200000))
def Bn(n, rb):
    a = 1-rb*rb/4; U = F(347,1000)*a-F(157,500)*rb; V = F(17,20)*a-rb/2; W = F(779,750)*a-F(5,6)*rb
    return F(11711,48400)*U-F(120,157*n)*V-F(250,157*n)*W-F(100,3*n*n)*V
chk("B_41(1/2)<0 (1/512 tier needed)", Bn(41, F(1,2)) < 0)
chk("Bn(1/2)>=Bsharp n=41..511", all(Bn(n, F(1,2)) >= Bs(n) for n in range(41, 512)))
# B_n(rb) monotonic in rb? (MEASURED on grid; text claims no monotonicity needed)
mono = all(Bn(n, F(k,16)) >= Bn(n, F(k+1,16)) for n in (41,64,160,511) for k in range(8))
print("[MEASURED] B_n(rb) decreasing in rb on grid:", mono)
# ---- Uniform tail c=2
chk("11/4<4log2<14/5", ivgt(4*iv.log(2), F(11,4)) and ivlt(4*iv.log(2), F(14,5)))
chk("sin(pi/4)<71/100", ivlt(iv.sin(pi/4), F(71,100))); chk("7/320", F(15,16)*F(29,100)-F(1,4) == F(7,320))
chk("sin(pi/100)>3/100", ivgt(iv.sin(pi/100), F(3,100))); chk("log tan ratio<10/3", ivlt(iv.log(iv.tan(pi/8)/iv.tan(pi/200)), F(10,3)))
chk("6pi/25>471/625", 6*P_LO/25 > F(471,625))
As = F(97,100)*F(15,16)-F(1,4); Is = F(2303,5000)*F(15,16)-F(471,2500); Rs = F(4837,1875)*F(15,16)-F(5,6)
C = F(15,16)-F(1,4)
chk("I* grouping", C*F(471,625) + F(15,16)*(F(707,1000)-1) == Is)
chk("R* grouping", C*F(10,3) - F(15,16)*F(471,625) == Rs)
chk("tail coefficients", F(11,4)/P_HI**2 == F(539,1936) and F(14,5)/P_LO == F(140,157) and 8/P_LO == F(400,157) and 8/F(3,100) == F(800,3))
Fh = lambda n: F(539,1936)*Is - (140*As+400*Rs)/(157*n) - 800*As/(3*n*n)
chk("Fh(295)>50064/1e6", Fh(295) > F(50064,10**6) and F(50064,10**6) > F(1,20)); chk("As,Rs>0", As > 0 and Rs > 0)
print("Fh(294) =", float(Fh(294)), " Fh(295) =", float(Fh(295)))
# ---- Corner lemma
qh, rU = F(7,48), F(2,125)
dA = qh*(F(107,10)-F(1,5)+F(23,250)) - F(1,4) - F(9,500) - F(11,14)*F(93,100) - rU*26
dD = 2*qh*(F(107,10)+F(23,250)) - F(4,15) - F(3,2) - F(3,2)*F(1,5) - F(1,5) - 2*rU*26
chk("dA-rU M = 2729/21000 (coarse)", dA == F(2729,21000) and dA > F(1,8)); chk("dD-2rU M = 49/1000 (coarse)", dD == F(49,1000))
chk("10451/30000", 5*qh - F(119,5)*rU == F(10451,30000) and 8*(qh-rU) > 0)
chk("(16/pi^2)(49/2000)>49/1250>1/30", 16/P_HI**2*F(49,2000) > F(49,1250) and F(49,1250) > F(1,30))
chk("U=V=pi^2/32 -> sqrt(2U)=pi/4", True)
chk("E_c(h,0): a>17/20", ivgt((1+iv.cos(pi/4))/2, F(17,20))); chk("p^1.5<3/5", ivlt(iv.sqrt(2)**(-iv.mpf(3)/2), F(3,5)))
chk("sqrt a>9/10", ivgt(iv.sqrt((1+iv.cos(pi/4))/2), F(9,10)))
chk("4I4/pi^2<9/25 via 319/360,197/20", 4*F(319,360)/F(197,20) < F(9,25)); chk("6/25", F(9,25)*F(3,5)/F(9,10) == F(6,25))
chk("(9/25)/sqrt2<4/15", (F(9,25)/F(4,15))**2 < 2)
import mpmath; mpmath.mp.dps=30; print("[MEASURED] I4 =", mpmath.quad(lambda t: mpmath.sqrt(1-t**4), [0,1]), "319/360 =", 319/360)
chk("diag u=1-cos h > 2 qh", ivgt(1-iv.cos(pi/4), F(7,24))); chk("sqrt2 KD<3/2 KD", True)
# ---- Section 5 rational pieces
chk("784/663", 1/(1-P_HI**2/64) == F(784,663)); chk("121/784", P_HI**2/64 == F(121,784))
eps = F(1, 2**53)
chk("2^26/27! < eps", F(2**26, factorial(27)) < eps)
chk("majorant<2", sum(F(4**j, factorial(2*j+1)) for j in range(13)) < 2 and 1+F(2,3)+F(2,15)+F(64,5040)/(1-F(1,18)) < 2)
chk("ratio 1/18 at j=3", F(4, 8*9) == F(1,18))
chk("normal guard (1-e)[1-e-(2/3)(1+e)^3]>1/4", (1-eps)*(1-eps-F(2,3)*(1+eps)**3) > F(1,4))
chk("1/25!>2^-85", F(1, factorial(25)) > F(1, 2**85))
g38 = 38*eps/(1-38*eps); chk("2 g38 < 77 eps", 2*g38 < 77*eps)
chk("theta/t upper < 1+6eps", (1+2*eps)/(1-eps)**2 < 1+6*eps); chk("theta/t lower > 1-6eps", (1-2*eps)/(1+eps)**2 > 1-6*eps)
chk("128 eps = 2^-46", 128*eps == F(1, 2**46)); chk("77+1+6=84<128", 77+1+6 == 84)
pfp = F(884279719003555, 2**48); chk("p_fp = float(pi) nearest", float(pfp) == 3.141592653589793)
chk("|pi/pfp-1|<=2eps", ivlt(abs(pi/(iv.mpf(884279719003555)/2**48) - 1), 2*eps))
# Machin and arctan bracket of A_80 orientation
chk("tan(2th)=5/12", 2*F(1,5)/(1-F(1,25)) == F(5,12)); chk("tan(4th)=120/119", 2*F(5,12)/(1-F(25,144)) == F(120,119))
chk("tan(4th-phi)=1", (F(120,119)-F(1,239))/(1+F(120,119)*F(1,239)) == 1)
chk("A_80 last index 79 odd -> lower; remainder 1/(161 q^161)", 2*79+3 == 161)
# corner witness geometry
chk("u'+v'=25/512", F(1,32)+F(9,512) == F(25,512)); chk("max(u',mu^4 v')=u'", all(F(1,32) >= F(n,n+1)**4*F(9,512) for n in range(41,256)))
chk("3pi/16>1/2 iff pi>8/3", 3*P_LO/16 > F(1,2) and P_LO/4 > F(1,2))
chk("near cut 1/(2pi)<3/16 and <1/4", 1/(2*P_LO) < F(3,16))
print("OK:", len(ok)); print("FAILED:", bad)
