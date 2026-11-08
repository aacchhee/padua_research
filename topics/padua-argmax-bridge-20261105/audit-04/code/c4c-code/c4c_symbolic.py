#!/usr/bin/env python3
"""C4C symbolic identity checks (sympy) for added/changed derivations in
companion comparison-unified.tex lines 1990-4020 at 24a98db."""
import sympy as sp

ok_all = True


def chk(name, expr):
    global ok_all
    e = sp.simplify(expr)
    ok = (e == 0)
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f"  residual={e}"))
    ok_all &= ok


# 1. completing the square (ul:radial-quadratic, ul:wide-polynomial)
x, rho, lx, ly, dx, dy, C4 = sp.symbols("x rho l_x l_y d_x d_y C4", real=True)
S0 = dx + dy
e = dx * dy / S0
f = (dy * lx + dx * ly) / S0
g = (lx - ly) ** 2 / (4 * S0)
xstar = (dy * rho + (lx - ly) / 2) / S0
lhs = lx * x + ly * (rho - x) - dx * x ** 2 - dy * (rho - x) ** 2
chk("square completion on x+y=rho", lhs - (g + f * rho - e * rho ** 2 - S0 * (x - xstar) ** 2))
chk("max identity C4+g+f^2/(4e) = C4+lx^2/(4dx)+ly^2/(4dy)",
    (g + f ** 2 / (4 * e)) - (lx ** 2 / (4 * dx) + ly ** 2 / (4 * dy)))
chk("vertex identity f/(2e)=lx/(2dx)+ly/(2dy)", f / (2 * e) - (lx / (2 * dx) + ly / (2 * dy)))
ystar_text = (dx / 2 - (lx - ly) / 2) / S0
xstar_text = (dy / 2 + (lx - ly) / 2) / S0
chk("x*,y* at rho=1/2 as displayed", (xstar.subs(rho, sp.Rational(1, 2)) - xstar_text)
    + (sp.Rational(1, 2) - xstar.subs(rho, sp.Rational(1, 2)) - ystar_text))

# 2. absolute gate trigonometric reduction
h, dl, Th, t, K = sp.symbols("h delta Theta t K", real=True)
X, Y = h + dl, h - dl
u = 1 - (sp.cos(X) + sp.cos(Y)) / 2
A = Th * sp.cos(h) + (t + 2 * K) * sp.sin(h)
B = t * sp.cos(h)
chk("u*Theta - t sin x - K(sin x+sin y) = Theta - A cos d - B sin d",
    sp.expand_trig(u * Th - t * sp.sin(X) - K * (sp.sin(X) + sp.sin(Y)) - (Th - A * sp.cos(dl) - B * sp.sin(dl))))
chk("a = cos h cos delta", sp.expand_trig((sp.cos(X) + sp.cos(Y)) / 2 - sp.cos(h) * sp.cos(dl)))

# 3. R_mesh exact rewrite (L2711-2718)
B0, D0, L, en, ep, em, H2, Th_, Tg = sp.symbols("B0 D0 L eps_n eta_p eta_m H2 T_h T_g", real=True)
Zn = D0 - B0 * en
Hn = -(L + ep) - (L + em) + Th_
Qn = -sp.Rational(1, 2) * ((L + ep) ** 2 + (L + em) ** 2) + Tg
Rmesh = -B0 * en * H2 - Zn * Hn - B0 * Qn - B0 * L ** 2 - 2 * D0 * L
jc = ep + em
Rnew = -B0 * en * (2 * L + H2) + (D0 + B0 * L - B0 * en) * jc + B0 / 2 * (ep ** 2 + em ** 2) + (-Zn * Th_ - B0 * Tg)
chk("R_mesh rewrite with Tail=-Z_n T_h - B0 T_g", Rmesh - Rnew)

# 4. delta_a R_mesh (L3516-3520)
a, D00, H2t, H20, Hnt, Hn0, Qnt, Qn0 = sp.symbols("a D00 H2t H20 Hnt Hn0 Qnt Qn0", real=True)
B00 = sp.Symbol("B00")
B0p = a * B00
def Rm(B0_, D0_, H2_, Hn_, Qn_):
    return -B0_ * en * H2_ - (D0_ - B0_ * en) * Hn_ - B0_ * Qn_ - B0_ * L ** 2 - 2 * D0_ * L
lhs = Rm(B0p, D0, H2t, Hnt, Qnt) - a * Rm(B00, D00, H20, Hn0, Qn0)
Zn0 = D00 - B00 * en
rhs = (-B0p * en * (H2t - H20) - a * Zn0 * (Hnt - Hn0) - B0p * (Qnt - Qn0)
       - (D0 - a * D00) * (Hnt + 2 * L))
chk("delta_a R_mesh identity", lhs - rhs)

# 5. displacement identity and S_disp(0)
mu, w, z, m = sp.symbols("mu w z m", positive=True)
Dh = mu ** 2 * w ** 2 - z ** 2
Dp = w ** 2 - z ** 2
chk("mu/D_h-1/D' = (1/2m){...} with mu=1-1/m",
    (mu / Dh - 1 / Dp - (1 / (2 * m)) * (1 / ((mu * w - z) * (w - z)) + 1 / ((mu * w + z) * (w + z)))).subs(mu, 1 - 1 / m))
pi = sp.pi
Sd = 0
for (ww, zz) in ((pi, 0), (pi, 0), (2 * pi, pi), (2 * pi, -pi)):
    for sg in (1, -1):
        Sd += 1 / ((mu * ww + sg * zz) * (ww + sg * zz))
chk("S_disp(0) closed form", Sd - (4 / mu + 2 / (2 * mu - 1) + 2 / (3 * (2 * mu + 1))) / pi ** 2)
chk("S_disp(0)(mu=1)=56/(9pi^2)", Sd.subs(mu, 1) - sp.Rational(56, 9) / pi ** 2)
chk("4*56/90-2=22/45", sp.Rational(4 * 56, 90) - 2 - sp.Rational(22, 45))

# 6. convolution identity (L2010-2022) for symbolic q's, j=1..6
qm, qp, s = sp.symbols("q_m q_p s", positive=True)
for j in range(1, 7):
    lhs = (sum(1 / (k + qm) for k in range(j)) + sum(1 / (k + qp) for k in range(j))) / (j + s)
    rhs = sum(1 / ((k + qm) * (j - 1 - k + qp)) for k in range(j))
    chk(f"convolution identity j={j} with q_m+q_p=1+s", (lhs - rhs).subs(qp, 1 + s - qm))

# 7. cutoff-recurrence algebra (L2002-2007): ell_j - D0/nu - B0 log nu/nu = Xi_j
psi_m, psi_p, nu = sp.symbols("psi_m psi_p nu", positive=True)
aa = sp.Symbol("a", positive=True)
B0a = 4 * aa / pi ** 2
ellj = (D0 + 2 * aa / pi ** 2 * (psi_m + psi_p)) / nu
Xi = 2 * aa / (pi ** 2 * nu) * (psi_m + psi_p - 2 * sp.log(nu))
chk("ell_j - D0/nu - B0 log(nu)/nu = Xi_j", ellj - D0 / nu - B0a * sp.log(nu) / nu - Xi)

# 8. reflection products (L2079-2083)
A_, A2, B_, B2 = sp.symbols("psi_td psi_1mtd psi_te psi_1mte")
Cd, Ce = -(A_ + A2), -(B_ + B2)
chk("A'B + B'A = {CdCe - (A'-A)(B'-B)}/2", (A2 * B_ + B2 * A_) - (Cd * Ce - (A2 - A_) * (B2 - B_)) / 2)
xx, yy = sp.symbols("x y", real=True)
td = sp.Rational(1, 2) + (xx - yy) / (2 * pi)
te = sp.Rational(1, 2) + (xx + yy) / (2 * pi)
a_xy = (sp.cos(xx) + sp.cos(yy)) / 2
expr = a_xy * sp.cot(pi * td) * sp.cot(pi * te) - (sp.cos(yy) - sp.cos(xx)) / 2
import random
random.seed(1)
mx = 0
for _ in range(20):
    vx, vy = random.uniform(0.05, 1.4), random.uniform(0.05, 1.4)
    mx = max(mx, abs(float(expr.subs({xx: vx, yy: vy}))))
print(("PASS " if mx < 1e-12 else "FAIL ") + f"a cot(pi td)cot(pi te)=(cos y-cos x)/2 (numeric, max {mx:.1e})")
ok_all &= mx < 1e-12

# 9. B_t(s) primitive and its extremes (L3215-3222)
ss, tt = sp.symbols("s t", real=True)
mu_t = tt - sp.Rational(1, 2)
Bl = ss ** 2 / 2 - mu_t * ss          # s<t
Br = ss ** 2 / 2 - mu_t * ss - (ss - tt)  # s>t
chk("B_t(1)=0", Br.subs(ss, 1))
chk("B_t(t)=t(1-t)/2", Bl.subs(ss, tt) - tt * (1 - tt) / 2)
chk("min on [0,t] at s=mu_t equals -(t-1/2)^2/2", Bl.subs(ss, mu_t) + (tt - sp.Rational(1, 2)) ** 2 / 2)
chk("min on [t,1] at s=t+1/2 equals -(t-1/2)^2/2", Br.subs(ss, tt + sp.Rational(1, 2)) + (tt - sp.Rational(1, 2)) ** 2 / 2)
Kt_mean = sp.integrate(ss, (ss, 0, 1)) - (1 - tt)
chk("mean of K_t is t-1/2", Kt_mean - mu_t)

# 10. central branch numerator (L2238)
b1, b2, e_ = sp.symbols("b1 b2 e", positive=True)
num = b1 * sp.cos(t) * sp.sin(t + e_) - b2 * sp.cos(t + e_) * sp.sin(t)
chk("branch numerator", sp.expand_trig(num - ((b1 - b2) * sp.sin(2 * t + e_) + (b1 + b2) * sp.sin(e_)) / 2))
chk("d/dt sin(t+e)/sin t = -sin e/sin^2 t", sp.simplify(sp.diff(sp.sin(t + e_) / sp.sin(t), t) + sp.sin(e_) / sp.sin(t) ** 2))

# 11. parameter integral closed form (L2411-2414)
S, v = sp.symbols("S v", positive=True)
val = (S + v) * sp.log(S + v) - (S - v) * sp.log(S - v) - 2 * v * sp.log(v)
chk("param integral second form", sp.expand_log(val - (2 * v * sp.log((S + v) / v) + (S - v) * sp.log(1 + 2 * v / (S - v))), force=True))
chk("d/dS param integral = log((v+S)/(S-v))", sp.simplify(sp.diff(val, S) - sp.log((v + S) / (S - v))))

# 12. d'(z) formula (L2906) and Q0 representation, (r0*)''
zz = sp.Symbol("z", positive=True)
dz = 1 / (2 * sp.sin(zz / 2)) - 1 / zz
X2 = zz / 2
chk("d'(z) formula", sp.simplify(sp.diff(dz, zz) - (sp.sin(X2) ** 2 - X2 ** 2 * sp.cos(X2)) / (4 * X2 ** 2 * sp.sin(X2) ** 2)))
cfun = lambda q: sp.cot(q) - 1 / q
chk("d = (c(z/4)-c(z/2))/2", sp.simplify(sp.expand_trig(dz - (cfun(zz / 4) - cfun(zz / 2)) / 2)).rewrite(sp.sin).simplify())
F = sp.Function("f")
r0s = 2 * (F(zz) - F(0)) / zz
chk("(r0*)''", sp.simplify(sp.diff(r0s, zz, 2) - (2 * sp.diff(F(zz), zz, 2) / zz - 4 * sp.diff(F(zz), zz) / zz ** 2 + 4 * (F(zz) - F(0)) / zz ** 3)))
# A_s' = z^-2 int_0^z t V''(t) dt  <=>  d/dz[z^2 A_s'] = z V''
V = sp.Function("V")
As = (V(zz) - V(0)) / zz
chk("d/dz(z^2 A_s') = z V''", sp.simplify(sp.diff(zz ** 2 * sp.diff(As, zz), zz) - zz * sp.diff(V(zz), zz, 2)))

# 13. nB_out derivative (L3012-3013)
nn = sp.Symbol("n", positive=True)
mm = nn + 1
Kf = sp.log(nn) + 25 * sp.log(2 * mm) + sp.Rational(193, 3)
nB = pi * nn * Kf / (8 * mm ** 2) + 1 / (8 * nn)
chk("d/dn(nB_out)", sp.simplify(sp.diff(nB, nn) - (pi * ((1 - nn) * Kf + mm + 25 * nn) / (8 * mm ** 3) - 1 / (8 * nn ** 2))))

# 14. (T+A4)' lower bound claim: derivative expression
Lf = sp.log(nn)
Tf = (4 * Lf ** 2 - 3 * Lf) / pi ** 2
A4f = 4 / nn + 40 * (1 + Lf) / (pi * nn ** 2)
der = sp.diff(Tf + A4f, nn)
import math
worst = min(float(der.subs(nn, k) - (math.log(k) / k ** 3) * (k * k / 2 - 4 * k - 40)) for k in [32, 33, 40, 64, 100, 512, 10 ** 4, 10 ** 6])
print(("PASS " if worst > 0 else "FAIL ") + f"(T+A4)' > (L/n^3)(n^2/2-4n-40) on sampled n (min gap {worst:.3e}); analytic argument checked by hand")

# 15. G_g regrouping: termwise max of G_phi with C_B<8 equals G_g
Lg, logm, log2m, gn, M_A, lg2, lpi = sp.symbols("L logm log2m g_n M_A log2 logpi", positive=True)
Gmax = ((2 * Lg * M_A + 23 + (3 * gn + 14 * logm + 26 + 20 + 2 * lg2) / pi) / 2
        + 6 * Lg * M_A + 4 * (7 + 2 / pi * (5 + 2 * log2m)) + 4 * lpi / pi + 2 * 8)
Gg = 7 * M_A * Lg + sp.Rational(111, 2) + (63 + lg2 + 4 * lpi + 7 * logm + 16 * log2m + sp.Rational(3, 2) * gn) / pi
chk("termwise max of m*G_phi (C_B<8, P<=2, ...) equals m*G_g", sp.expand(Gmax - Gg))

# 16. 2(A-3)(B-3)>9 <=> A+B-sqrt(A^2+B^2)>3 and the A constant
A1 = sp.Rational(52) + sp.Rational(28) * sp.Rational(3, 4) * sp.Rational(32, 33)
chk("A = (52+28*(3/4)*(32/33))/(2 pi^2) = 398/(11 pi^2)", A1 / (2 * pi ** 2) - sp.Rational(398, 11) / pi ** 2)

# 17. relative assembly coefficients
chk("6+10+11+50+1/2=155/2", 6 + 10 + 11 + 50 + sp.Rational(1, 2) - sp.Rational(155, 2))
chk("product-rule constant (80/323)(10/19+8/17)=25760/104329",
    sp.Rational(80, 323) * (sp.Rational(10, 19) + sp.Rational(8, 17)) - sp.Rational(25760, 104329))
print("displacement-sum increment", float(sp.Rational(25760, 104329) * (6 + sp.Rational(2, 27))), "< 3/2")
chk("8(5+20)(800/1083)=160000/1083", 8 * 25 * sp.Rational(800, 1083) - sp.Rational(160000, 1083))
print("sine column", float(14 * sp.Rational(50, 49) * sp.Rational(800, 1083)), "< 11")
print("pole-regular sum", sp.Rational(289, 100) + sp.Rational(395, 48) + 4 * sp.Rational(67, 20) + 2 * sp.Rational(193, 48),
      "=", sp.Rational(39073, 1200))
chk("pole-regular total", sp.Rational(289, 100) + sp.Rational(395, 48) + 4 * sp.Rational(67, 20) + 2 * sp.Rational(193, 48) - sp.Rational(39073, 1200))
chk("Var P_s central 27/4+17/16+5/12=395/48", sp.Rational(27, 4) + sp.Rational(17, 16) + sp.Rational(5, 12) - sp.Rational(395, 48))
chk("sup P_s central 51/16+5/6=193/48", sp.Rational(51, 16) + sp.Rational(5, 6) - sp.Rational(193, 48))
chk("half-line coefficients 32/27+32/51+85/612", sp.Rational(32, 27) + sp.Rational(32, 51) + sp.Rational(85, 612) - sp.Rational(1991, 1020))
print("half-line coeff total", float(sp.Rational(32, 27) + sp.Rational(32, 51) + sp.Rational(85, 612)))
chk("V_F assembly 74/3+119/3=193/3", sp.Rational(74, 3) + sp.Rational(119, 3) - sp.Rational(193, 3))
chk("7/(12pi)((3h/2)^2+(5h/2)^2), h=pi/m -> 119pi/(24m^2)",
    sp.Rational(7, 12) / pi * ((sp.Rational(3, 2) * pi / m) ** 2 + (sp.Rational(5, 2) * pi / m) ** 2) - 119 * pi / (24 * m ** 2))
print("\nALL PASS" if ok_all else "\nSOME FAIL")
