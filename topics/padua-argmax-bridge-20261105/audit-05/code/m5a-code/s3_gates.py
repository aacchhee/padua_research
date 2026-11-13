# M5A s3: gate clauses of Cor 4.6/4.7 and Table 1, recomputed with mpmath interval
# arithmetic (outward rounding, 60 digits) from the formulas printed in (uc:constants),
# (uc:uniform-allowance), Cor 4.6 and Cor 4.7; termwise-maximum gap with Fractions.
import mpmath as mp
from mpmath import iv
from fractions import Fraction as Fr
import sympy as sp

iv.dps = 60
ok = True
def check(name, cond, info=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + str(info) if info else ""))

PI = iv.pi
def consts(n):
    n = iv.mpf(n); m = n + 1
    L = iv.log(n); Lb = 1 + L
    T = (4 * L**2 - 3 * L) / PI**2
    b0 = 4 / PI**2; r0 = iv.log(iv.mpf(5) / 2) + iv.mpf(1) / 18
    D = ((52 / PI**2) * Lb + 7) / n + 10 / n**2 + 20 * Lb / (PI * n**2)
    M = (b0 * (2 * L + 2 * r0) / n + (4 + b0 * (L + 1 / n)) / (4 * n**2 - 1) + b0 / (2 * n - 1)**2
         + (5 + b0 * (iv.log(n + iv.mpf(1) / 2) + 2)) / (4 * (n - iv.mpf(1) / 2)**2))
    eb = D + M + 1 / n
    KD = ((6 + 16 / (3 * PI)) * Lb + 2 / PI) / n
    A4 = 4 / n + 40 * Lb / (PI * n**2); C4 = A4 + 20 / n**2
    db = (17 * L + 27) / n**2
    kWx = ((iv.mpf(19) / 2) * Lb + (iv.mpf(23) / 3) * L + iv.mpf(155) / 2) / n + 152 / n**2
    kWy = kWx + db
    Wn = (3 * iv.log(m) + iv.log(2) + 2 * iv.log(PI) + 2) / (PI * m)
    gn = 1 + iv.log(2 + 8 * m / (3 * PI)); MA = 1 / PI + 4 / PI**2
    Gg = (7 * MA * L + iv.mpf(111) / 2 + (63 + iv.log(2) + 4 * iv.log(PI) + 7 * iv.log(m) + 16 * iv.log(2 * m) + iv.mpf(3) / 2 * gn) / PI) / m
    CE = D + Gg + (64 + 16 * L) / n + 318 / n**2 + M + Wn
    Mn = (4 * L**2 + iv.mpf(79) / 5 * L) / PI**2 + iv.mpf(9) / 4 + CE + 2 * KD
    js = iv.mpf(23) / 250; ts = iv.mpf(221) / 500
    Us = T - eb + A4 + js
    lx = kWx + iv.mpf(5) / 48; ly = kWy
    dx = 11 * Us / 48 - iv.mpf(5) / 12; dy = 11 * Us / 48
    return dict(L=L, T=T, eb=eb, KD=KD, CE=CE, C4=C4, kWx=kWx, kWy=kWy, db=db, Mn=Mn,
                Us=Us, dx=dx, dy=dy, lx=lx, ly=ly, js=js, ts=ts)

def G(n, rho1):
    c = consts(n)
    Ts = c["T"] + c["js"]; h = iv.mpf(rho1) / 2
    return Ts * (1 - iv.cos(h)) - (c['ts'] + 2 * c['KD']) * iv.sin(h) - c['ts']**2 * iv.cos(h) / (2 * Ts) - c['CE'] - c['eb'], (c['ts'] + 2 * c['KD']) / Ts

table = {
 192: dict(L=(5.257495,5.257496), T=(9.604492,9.604493), eb=(0.241128,0.241129), KD=(0.254190,0.254191), CE=(1.821444,1.821445), C4=(0.023537,0.023538), kWx=(0.927319,0.927320), kWy=(0.930476,0.930477), db=(0.003156,0.003157), Mn=(24.198997,24.198998), Us=(9.478358,9.478359), dx=(1.755457,1.755458), dy=(2.172123,2.172124), lx=(1.031486,1.031487), ly=(0.930476,0.930477)),
 256: dict(L=(5.545177,5.545178), T=(10.776565,10.776566), eb=(0.187434,0.187435), KD=(0.199293,0.199294), CE=(1.405236,1.405237), C4=(0.017201,0.017202), kWx=(0.714007,0.714008), kWy=(0.715858,0.715859), db=(0.001850,0.001851), Mn=(25.393055,25.393056), Us=(10.698027,10.698028), dx=(2.034964,2.034965), dy=(2.451631,2.451632), lx=(0.818174,0.818175), ly=(0.715858,0.715859)),
 295: dict(L=(5.686975,5.686976), T=(11.378959,11.378960), eb=(0.165491,0.165492), KD=(0.176646,0.176647), CE=(1.236309,1.236310), C4=(0.014767,0.014768), kWx=(0.627598,0.627599), kWy=(0.629020,0.629021), db=(0.001421,0.001422), Mn=(26.051329,26.051330), Us=(11.320005,11.320006), dx=(2.177501,2.177502), dy=(2.594168,2.594169), lx=(0.731765,0.731766), ly=(0.629020,0.629021)),
 512: dict(L=(6.238324,6.238325), T=(13.876118,13.876119), eb=(0.101753,0.101754), KD=(0.110067,0.110068), CE=(0.750341,0.750342), C4=(0.008240,0.008241), kWx=(0.379664,0.379665), kWy=(0.380171,0.380172), db=(0.000507,0.000508), Mn=(28.979594,28.979595), Us=(13.874529,13.874530), dx=(2.762912,2.762913), dy=(3.179579,3.179580), lx=(0.483830,0.483831), ly=(0.380171,0.380172)),
}
nbad = 0
for n, row in table.items():
    c = consts(n)
    for k, (lo, hi) in row.items():
        val = c[k]
        inside = (val.a >= mp.mpf(str(lo))) and (val.b <= mp.mpf(str(hi)))
        if not inside:
            nbad += 1
            print(f"   table mismatch n={n} {k}: computed [{mp.nstr(val.a, 12)}, {mp.nstr(val.b, 12)}] vs [{lo},{hi}]")
check("Table 1: all 60 enclosures contain the recomputed interval", nbad == 0, f"{nbad} outside")

# Cor 4.6 bases
g512, r512 = G(512, 1)
check("(t*+2K_D)/T*(512) < 3/50", r512.b < mp.mpf(3) / 50, mp.nstr(r512.b, 8))
check("tan(1/2) > 1/2", iv.tan(iv.mpf(1) / 2).a > 0.5)
check("G(512,1) > 534264/10^6", g512.a > mp.mpf(534264) / 10**6, mp.nstr(g512.a, 12))
g192, r192 = G(192, PI / 2)  # rho1 = pi/2
check("(t*+2K_D)/T*(192) < 1/10", r192.b < mp.mpf(1) / 10, mp.nstr(r192.b, 8))
check("G(192,pi/2) > 98316/10^6 (exact 1/sqrt2)", g192.a > mp.mpf(98316) / 10**6, mp.nstr(g192.a, 12))
# with 707107/10^6 substituted in the adverse terms
c = consts(192); Ts = c['T'] + c['js']; s2 = iv.mpf(707107) / 10**6
g192s = Ts * (1 - s2) - (c['ts'] + 2 * c['KD']) * s2 - c['ts']**2 * s2 / (2 * Ts) - c['CE'] - c['eb']
check("G(192,pi/2) with 707107/10^6 substitution > 98316/10^6", g192s.a > mp.mpf(98316) / 10**6, mp.nstr(g192s.a, 12))
check("G(512,1) > 1/2 and G(192,pi/2) > 3/100", g512.a > 0.5 and g192.a > 0.03)

# Cor 4.7 bases
c = consts(512)
dx, dy, lx, ly, C4 = c['dx'], c['dy'], c['lx'], c['ly'], c['C4']
e = dx * dy / (dx + dy); f = (dy * lx + dx * ly) / (dx + dy); g = (lx - ly)**2 / (4 * (dx + dy))
pmax = C4 + g + f**2 / (4 * e)
pmax2 = C4 + lx**2 / (4 * dx) + ly**2 / (4 * dy)
vert = f / (2 * e)
p_half = C4 + g + f / 2 - e / 4
check("d_x(512) > 1", dx.a > 1, mp.nstr(dx.a, 8))
check("0 < d_beta(512) < 5/48", c['db'].a > 0 and c['db'].b < mp.mpf(5) / 48, mp.nstr(c['db'].b, 6))
check("0 < l_x - l_y = 5/48 - d_beta", (lx - ly).a > 0 and abs((lx - ly - (iv.mpf(5) / 48 - c['db'])).b) < 1e-50)
check("U*(512) >= 0", c['Us'].a > 0)
check("max p_512 < 40786/10^6 < 41/1000", pmax.b < mp.mpf(40786) / 10**6, mp.nstr(pmax.b, 14))
check("max identities agree", abs((pmax - pmax2).b) < 1e-40 and abs((pmax - pmax2).a) < 1e-40)
check("vertex f/(2e) < 3/20", vert.b < mp.mpf(3) / 20, mp.nstr(vert.b, 12))
check("p_512(1/2) < -143069/10^6 < -1/7", p_half.b < -mp.mpf(143069) / 10**6 and mp.mpf(143069) / 10**6 > mp.mpf(1) / 7, mp.nstr(p_half.b, 12))
print("   margin of 40786/10^6 bound:", mp.nstr(mp.mpf(40786) / 10**6 - pmax.b, 4))

# symbolic identities: square completion, max, vertex
X, Y, rho, LX, LY, DX, DY, C = sp.symbols('x y rho lx ly dx dy C4', positive=True)
E = DX * DY / (DX + DY); F = (DY * LX + DX * LY) / (DX + DY); Gs = (LX - LY)**2 / (4 * (DX + DY))
quad_line = (C + LX * X + LY * (rho - X) - DX * X**2 - DY * (rho - X)**2)
xs = sp.solve(sp.diff(quad_line, X), X)[0]
check("square completion on x+y=rho", sp.simplify(quad_line.subs(X, xs) - (C + Gs + F * rho - E * rho**2)) == 0)
check("max p = C4+lx^2/(4dx)+ly^2/(4dy)", sp.simplify(C + Gs + F**2 / (4 * E) - (C + LX**2 / (4 * DX) + LY**2 / (4 * DY))) == 0)
check("vertex f/(2e) = lx/(2dx)+ly/(2dy)", sp.simplify(F / (2 * E) - (LX / (2 * DX) + LY / (2 * DY))) == 0)
check("x* at rho=1/2", sp.simplify(xs.subs(rho, sp.Rational(1, 2)) - (DY / 2 + (LX - LY) / 2) / (DX + DY)) == 0)
# monotonicity of d_beta and (T+A4)'
nn = sp.symbols('n', positive=True)
Ls = sp.log(nn)
dbeta = (17 * Ls + 27) / nn**2
check("d_beta' < 0 for n>=1", sp.simplify(sp.diff(dbeta, nn) * nn**3 - (17 - 2 * (17 * Ls + 27))) == 0)
TA = (4 * Ls**2 - 3 * Ls) / sp.pi**2 + 4 / nn + 40 * (1 + Ls) / (sp.pi * nn**2)
der = sp.diff(TA, nn)
worst = min(float((der - Ls / nn**3 * (nn**2 / 2 - 4 * nn - 40)).subs(nn, v)) for v in [32, 40, 64, 100, 160, 512, 1e4, 1e8])
check("(T+A4)' - (L/n^3)(n^2/2-4n-40) > 0 at samples n>=32", worst > 0, f"{worst:.3e}")
# Fraction checks for the termwise maximum and correlated saving
for L in [Fr(3), Fr(7, 2), Fr(5), Fr(10), Fr(100)]:
    gap_low = Fr(275) + 219 * L
    # 25+17L-(73+49L)/pi > (275+219L)/157 uses 1/pi < 50/157
    lhs_with = 25 + 17 * L - (73 + 49 * L) * Fr(50, 157)
    assert lhs_with == gap_low / 157
check("64+16L+3Lbar-{42+2L+(49Lbar+24)/pi} >= (275+219L)/157 (with 1/pi<50/157)", True)
check("pi > 157/50", mp.pi > mp.mpf(157) / 50)
Aq = 398 / (11 * mp.pi**2); Bq = 48 / mp.pi
check("A=398/(11pi^2)>18/5, B=48/pi>15", Aq > 3.6 and Bq > 15, f"A={mp.nstr(Aq,6)} B={mp.nstr(Bq,6)}")
check("A+B-sqrt(A^2+B^2) > 3 and 2(A-3)(B-3) > 9", Aq + Bq - mp.sqrt(Aq**2 + Bq**2) > 3 and 2 * (Aq - 3) * (Bq - 3) > 9,
      mp.nstr(Aq + Bq - mp.sqrt(Aq**2 + Bq**2), 6))
check("796/(11pi^2) = (52+28*(3/4)*(32/33))/pi^2", Fr(52) + 28 * Fr(3, 4) * Fr(32, 33) == Fr(796, 11))
tm = 42 + 2 * 0 + (49 + 24) / mp.pi; tm1 = 2 + 49 / mp.pi
check("termwise max ~ (65.2+17.6L)/n", abs(tm - 65.24) < 0.01 and abs(tm1 - 17.60) < 0.01, f"{mp.nstr(tm,5)} + {mp.nstr(tm1,5)} L")
print("ALL PASS" if ok else "SOME FAIL")
