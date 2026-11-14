"""Recompute the telescope allowances (uc:constants, uc:uniform-allowance,
uc:analytic-norm) at the Section 4 hand-off degrees, compare with the
rational bounds quoted in localization-unified.tex (ul:near-base etc.).
j is taken at its proved lower bound 23/250 (uc:scalar-constants)."""
import sys; sys.path.insert(0, sys.argv[1])
from mpmath import mp, mpf, log, pi, e as E
from fractions import Fraction as F
mp.dps = 40
def consts(n):
    n = mpf(n); m = n + 1; L = log(n); H = 1 + L
    T = (4*L**2 - 3*L)/pi**2; b0 = 4/pi**2; r0 = log(mpf(5)/2) + mpf(1)/18
    D = ((52/pi**2)*H + 7)/n + 10/n**2 + 20*H/(pi*n**2)
    M = b0*(2*L + 2*r0)/n + (4 + b0*(L + 1/n))/(4*n**2 - 1) + b0/(2*n - 1)**2 + (5 + b0*(log(n + mpf(1)/2) + 2))/(4*(n - mpf(1)/2)**2)
    eb = D + M + 1/n
    KD = ((6 + 16/(3*pi))*H + 2/pi)/n
    A4 = 4/n + 40*H/(pi*n**2); C4 = A4 + 20/n**2; db = (17*L + 27)/n**2
    JN = (mpf(3)/2*H + mpf(16)/5)/n + 78/n**2; JW = (mpf(3)/2*H + 6)/n + 148/n**2
    kNx = ((mpf(19)/2)*H + (mpf(23)/3)*L + mpf(677)/10)/n + 82/n**2; kNy = kNx + db
    kWx = ((mpf(19)/2)*H + (mpf(23)/3)*L + mpf(155)/2)/n + 152/n**2; kWy = kWx + db
    gn = 1 + log(2 + 8*m/(3*pi)); MA = 1/pi + 4/pi**2
    Gg = (7*MA*L + mpf(111)/2 + (63 + log(2) + 4*log(pi) + 7*log(m) + 16*log(2*m) + mpf(3)/2*gn)/pi)/m
    Wn = (3*log(m) + log(2) + 2*log(pi) + 2)/(pi*m)
    CE = D + Gg + (64 + 16*L)/n + 318/n**2 + M + Wn
    Mn = (4*L**2 + mpf(79)/5*L)/pi**2 + mpf(9)/4 + CE + 2*KD
    return dict(L=L, H=H, T=T, D=D, M=M, eb=eb, KD=KD, A4=A4, C4=C4, JN=JN, JW=JW, kNx=kNx, kNy=kNy, kWx=kWx, kWy=kWy, CE=CE, Mn=Mn)
j = mpf(23)/250
c = consts(320)
claims320 = [("T>293/25", c['T'] > mpf(293)/25), ("D<27/200", c['D'] < mpf(27)/200), ("M<7/400", c['M'] < mpf(7)/400),
  ("ebar<249/1600", c['eb'] < mpf(249)/1600), ("C4<677/50000", c['C4'] < mpf(677)/50000),
  ("kNx<11031/20000", c['kNx'] < mpf(11031)/20000), ("kNy<11056/20000", c['kNy'] < mpf(11056)/20000),
  ("kNx<705963/1280000", c['kNx'] < mpf(705963)/1280000), ("kNy<56602113/102400000", c['kNy'] < mpf(56602113)/102400000),
  ("U_N - rho J_N > 23337/2000 & J_N>21/500", (c['T'] - c['eb'] + c['A4'] + j > mpf(23337)/2000) and c['JN'] > mpf(21)/500),
  ("kWx<583/1000", c['kWx'] < mpf(583)/1000), ("kWy<117/200", c['kWy'] < mpf(117)/200), ("T-ebar+j>2331/200", c['T'] - c['eb'] + j > mpf(2331)/200)]
print("n=320:", {k: float(v) for k, v in c.items()})
for s, ok in claims320: print("  ", "OK " if ok else "FAIL", s)
print("   margins: U_N base", float(c['T'] - c['eb'] + c['A4'] + j - mpf(23337)/2000), " T-e+j", float(c['T'] - c['eb'] + j - mpf(2331)/200))
c = consts(192)
print("n=192: T>19/2", c['T'] > 9.5, " ebar<1/4", c['eb'] < 0.25, " K_D<13/50", c['KD'] < mpf(13)/50, {k: float(c[k]) for k in ('T','eb','KD')})
c = consts(256)
print("n=256:", "T>107/10", c['T'] > mpf(107)/10, "ebar<1/5", c['eb'] < 0.2, "K_D<1/5", c['KD'] < 0.2, "CE<3/2", c['CE'] < 1.5,
      "C4<9/500", c['C4'] < mpf(9)/500, "kWy<93/100", c['kWy'] < mpf(93)/100, "M(256)<26", c['Mn'] < 26,
      {k: float(c[k]) for k in ('T','eb','KD','CE','C4','kWy','Mn')})
for n in (32, 75, 147, 148, 160):
    c = consts(n); print(f"n={n}: ebar={float(c['eb']):.5f} D={float(c['D']):.5f} M={float(c['M']):.5f} CE={float(c['CE']):.4f} M(n)={float(c['Mn']):.3f}")
