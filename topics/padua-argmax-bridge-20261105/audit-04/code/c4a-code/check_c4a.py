"""C4A independent checks of companion Sections 1-3 (introduction, preliminaries, corner).
Written fresh for audit-04; does not import audit-03 scripts.  Run:
  PYTHONPATH=<pylib> python3 -I check_c4a.py
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
t0 = time.time()
ok = True
def rep(name, cond, extra=""):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + extra if extra else ""))

pi = mp.pi
a = 2/pi
gam = mp.euler
d = gam + mp.log(8/pi)
c1 = a*d
b = 2*a*c1

# ---------- kappa (4) ----------
def kappa_integrand(t):
    if t == 0:
        return mp.mpf(0)
    s = mp.nsum(lambda j: 1/((2*j+1)*((2*j+1)**2 - t**2)), [0, mp.inf])
    return (8/pi)*t**2*mp.cot(pi*t/2)*s
kap = mp.quad(kappa_integrand, [0, 0.5, 1])
c = c1**2 + kap
print("kappa =", mp.nstr(kap, 20), " b =", mp.nstr(b, 16), " c =", mp.nstr(c, 16))
rep("kappa approx 0.919710118388", abs(kap - mp.mpf('0.919710118388')) < 1e-12)
rep("b approx 1.225522125742", abs(b - mp.mpf('1.225522125742')) < 1e-12)
rep("c approx 1.846160310424", abs(c - mp.mpf('1.846160310424')) < 1e-12)
rep("integrand -> 2 at t=1 (intro/corner)", abs(kappa_integrand(1 - mp.mpf('1e-12')) - 2) < 1e-9)
L = mp.mpf(3)
rep("ell>=3 tail bound sum_{l>=L} l^-3 <= L^-3+1/(2L^2) (L=3)",
    mp.nsum(lambda l: l**-3, [3, mp.inf]) <= L**-3 + 1/(2*L**2))
rep("lim t^2 cot(pi t/2)/(1-t^2) = pi/4",
    abs((lambda t: t**2*mp.cot(pi*t/2)/(1-t**2))(1-mp.mpf('1e-15')) - pi/4) < 1e-12)
# square identity (intro 294-296)
Nn = mp.mpf(7.5)
rep("a^2 log^2N + b logN + c = (a logN + c1)^2 + kappa = (4/pi^2)(logN+d)^2+kappa",
    abs(a**2*mp.log(Nn)**2 + b*mp.log(Nn) + c - (a*mp.log(Nn)+c1)**2 - kap) < 1e-25
    and abs((a*mp.log(Nn)+c1)**2 - 4/pi**2*(mp.log(Nn)+d)**2) < 1e-25)

# ---------- Padua nodes, Lemma 2.1, Lambda_c via kernel ----------
def nodes(n):
    m = n+1
    out = []
    for j in range(n+1):
        for k in range(m+1):
            if (j+k) % 2 == 0:
                eps = 0.5 if j in (0, n) else 1.0
                eta = 0.5 if k in (0, m) else 1.0
                out.append((j, k, math.cos(j*math.pi/n), math.cos(k*math.pi/m), 2*eps*eta/(n*m)))
    return out
def T(p, x):
    return math.cos(p*math.acos(max(-1.0, min(1.0, x))))
def card(n, z, B):
    # (6): L_B(z) = w_jk [K_n(z,B) - T_n(z1)T_n(B1)]
    j, k, x, y, w = B
    s = 0.0
    for p in range(n+1):
        for q in range(n+1-p):
            nu = (1 if p == 0 else 2)*(1 if q == 0 else 2)
            s += nu*T(p, z[0])*T(p, x)*T(q, z[1])*T(q, y)
    return w*(s - T(n, z[0])*T(n, x))
maxdelta = 0.0
for n in range(1, 8):
    P = nodes(n)
    rep("node count n=%d equals dim (n+1)(n+2)/2" % n, len(P) == (n+1)*(n+2)//2)
    for B in P:
        for A_ in P:
            v = card(n, (A_[2], A_[3]), B)
            maxdelta = max(maxdelta, abs(v - (1.0 if A_ is B else 0.0)))
rep("(6) cardinal values delta_AB for n=1..7", maxdelta < 1e-11, "max err %.2e" % maxdelta)

def lam(n, z):
    return sum(abs(card(n, z, B)) for B in nodes(n))

# n=1 example: weights, Gram, cardinals, lambda_1
P1 = nodes(1)
rep("n=1 nodes (1,1),(1,-1),(-1,0) weights 1/4,1/4,1/2",
    sorted([(round(x, 12), round(y, 12), w) for (_, _, x, y, w) in P1]) ==
    sorted([(1.0, 1.0, 0.25), (1.0, -1.0, 0.25), (-1.0, 0.0, 0.5)]))
G = np.array([[sum(w*f(x, y)*g(x, y) for (_, _, x, y, w) in P1) for g in (lambda x, y: 1, lambda x, y: x, lambda x, y: y)]
              for f in (lambda x, y: 1, lambda x, y: x, lambda x, y: y)])
rep("n=1 Gram diag(1,1,1/2)", np.allclose(G, np.diag([1, 1, 0.5])))
grid = np.linspace(-1, 1, 81)
vals = [(lam(1, (x, y)), x, y) for x in grid for y in grid]
mx = max(v[0] for v in vals)
arg = sorted({(round(v[1], 6), round(v[2], 6)) for v in vals if v[0] > mx - 1e-12})
rep("n=1 lambda max 2 at (-1,+-1) on 81^2 grid", abs(mx - 2) < 1e-12 and arg == [(-1.0, -1.0), (-1.0, 1.0)], str(arg))
# lambda_1 closed form
rep("lambda_1 = max(1,|y|+(1-x)/2) on grid",
    max(abs(v[0] - max(1, abs(v[2]) + (1-v[1])/2)) for v in vals) < 1e-12)

# ---------- (8), (12), (13) ----------
def eps_(j, n): return mp.mpf(1)/2 if j in (0, n) else mp.mpf(1)
def lam_c_8(n):
    m = n+1
    s = mp.mpf(0)
    for j in range(n+1):
        for k in range(n+1):
            if (j+k) % 2 == 1:
                th, ph = j*pi/n, k*pi/m
                f = (1+mp.cos(ph))/abs(mp.cos(th)-mp.cos(ph))
                s += mp.mpf(eps_(j, n))*mp.mpf(eps_(k, m))*f
    return 4*s/(n*m) + mp.mpf(1)/m
def w_(x): return mp.cot(pi*x/2)
def B_(x): return mp.cot(pi*x) - 1/(pi*x) + 1/(pi*(1-x))
def lam_c_12a(n):
    m = n+1
    s = mp.mpf(0)
    for r in range(1, m):
        al = (1 - mp.mpf(r)/m)/2
        Tnr = mp.fsum(mp.cot(pi*(l+al)/n) for l in range(r))
        s += w_(mp.mpf(r)/m)*Tnr
    return 1 - mp.mpf(2*n)/m + 4*s/(n*m)
def lam_c_12b(n):
    m = n+1
    Hm = mp.mpf(0); V = mp.mpf(0)
    for r in range(1, m):
        x = mp.mpf(r)/m; s_ = m-r; al = (1-x)/2
        D = mp.digamma(r+al) + mp.digamma(s_-al) - mp.digamma(m-al) - mp.digamma(al)
        Hm += w_(x)*D
        V += w_(x)*mp.fsum(B_((l+al)/n) for l in range(r))
    return -1 + mp.mpf(2)/m + 4*Hm/(pi*m) + 4*V/(n*m)
lc2 = lam_c_8(2)
rep("Lambda_c(2)=3 from (8)", abs(lc2 - 3) < 1e-25)
# exact rational (8) for n=2 (f values are rational at these angles)
summ = {(0, 1): Fr(1, 2)*Fr(3), (1, 0): Fr(1)*Fr(1, 2)*Fr(2), (1, 2): Fr(1), (2, 1): Fr(1, 2)}
rep("n=2 table entries 3/2,1,1,1/2 and total 3",
    [summ[k] for k in [(0, 1), (1, 0), (1, 2), (2, 1)]] == [Fr(3, 2), 1, 1, Fr(1, 2)]
    and Fr(4, 6)*sum(summ.values()) + Fr(1, 3) == 3)
dev = 0
for n in range(2, 13):
    l8 = lam_c_8(n); la = lam_c_12a(n); lb = lam_c_12b(n)
    lk = lam(n, (-1.0, -1.0)) if n <= 9 else None
    dev = max(dev, abs(l8-la), abs(l8-lb))
    if lk is not None:
        dev = max(dev, abs(l8 - lk)/1e5)  # float kernel: loose
        if abs(l8 - lk) > 1e-9:
            rep("kernel vs (8) n=%d" % n, False, "%s %s" % (l8, lk))
    # other nonnode corner
    oc = (1.0, -1.0) if n % 2 == 0 else (-1.0, 1.0)
    if n <= 9:
        if abs(lam(n, oc) - float(l8)) > 1e-9:
            rep("other corner equal n=%d" % n, False)
rep("(8) = (12a) = (12b) = kernel corner value, n=2..12 (kernel to 9)", dev < 1e-20, "max dev %s" % mp.nstr(dev, 3))
print("Lambda_c(1) via kernel =", lam(1, (-1.0, -1.0)))

# D_n closed form, D_n(pi,pi), |D_n-(-1)^j| = 2f on odd checkerboard
def Dn_sum(n, u, v):
    return mp.fsum(mp.cos(p*u)*mp.cos(q*v)*(1 if p == 0 else 2)*(1 if q == 0 else 2)
                   for p in range(n+1) for q in range(n+1-p))
def Dn_closed(n, u, v):
    up, um = (u+v)/2, (v-u)/2
    return (mp.sin((n+1)*up)*mp.sin((n+1)*um) + mp.sin(n*up)*mp.sin(n*um))/(mp.sin(up)*mp.sin(um))
err = 0
for n in range(2, 8):
    m = n+1
    err = max(err, abs(Dn_sum(n, mp.mpf('0.37'), mp.mpf('1.91')) - Dn_closed(n, mp.mpf('0.37'), mp.mpf('1.91'))))
    rep("D_n(pi,pi)=(-1)^n(2n+1), n=%d" % n, abs(Dn_sum(n, pi, pi) - (-1)**n*(2*n+1)) < 1e-20)
    for j in range(n+1):
        for k in range(m+1):
            if (j+k) % 2 == 1 and not (j == n and k == m):
                th, ph = j*pi/n, k*pi/m
                val = Dn_sum(n, th, ph)
                f = (1+mp.cos(ph))/abs(mp.cos(th)-mp.cos(ph))
                err = max(err, abs(abs(val - (-1)**j) - 2*f))
                err = max(err, abs(val - (-1)**j*(2+mp.cos(th)+mp.cos(ph))/(mp.cos(th)-mp.cos(ph))))
rep("diamond closed form and |D_n-(-1)^j|=2f, n=2..7", err < 1e-18, mp.nstr(err, 3))

# signed row sum n, positive indices, absolute row 2P_r - n, r=0 row n^2
err = 0; poserr = False
for n in range(2, 12):
    m = n+1
    for r in range(1, m):
        v = r*pi/m
        js = [j for j in range(-n+1, n+1) if (j - (1-r)) % 2 == 0]
        assert len(js) == n
        F = [(1+mp.cos(v))/(mp.cos(j*pi/n)-mp.cos(v)) for j in js]
        err = max(err, abs(mp.fsum(F) - n))
        pos = sorted(j for j, Fv in zip(js, F) if Fv > 0)
        if pos != list(range(-r+1, r, 2)):
            poserr = True
        al = (1-mp.mpf(r)/m)/2
        Pr = w_(mp.mpf(r)/m)*mp.fsum(mp.cot(pi*(l+al)/n) for l in range(r))
        err = max(err, abs(mp.fsum(abs(x) for x in F) - (2*Pr - n)))
    err = max(err, abs(mp.fsum(mp.csc((l+mp.mpf(1)/2)*pi/n)**2 for l in range(n)) - n**2))
rep("signed row sum n; absolute row 2P_r-n; csc^2 half-step sum n^2 (n<=11)", err < 1e-18, mp.nstr(err, 3))
rep("positive sample indices exactly -r+1..r-1 step 2", not poserr)
# sine product constant C_n = 2^{n-1}
z = mp.mpf('0.3141')
rep("sin(nz) = 2^{n-1} prod sin(z+l pi/n), n=2..8",
    max(abs(mp.sin(n*z) - 2**(n-1)*mp.fprod(mp.sin(z+l*pi/n) for l in range(n))) for n in range(2, 9)) < 1e-25)

# (13) square identity and L_n = (1/n) sum cot y_r ; L_n - A(n) = O(n^-2)
err = 0
for n in range(2, 30):
    s = mp.mpf(0)
    for j in range(n+1):
        for k in range(n+1):
            if (j+k) % 2 == 1:
                th, tk = j*pi/n, k*pi/n
                s += mp.mpf(eps_(j, n))*mp.mpf(eps_(k, n))*(1+mp.cos(tk))/abs(mp.cos(th)-mp.cos(tk))
    Ln = 2*mp.fsum((mp.mpf(1)/2 if r == n else 1)*mp.csc(r*pi/(2*n)) for r in range(1, n+1, 2))/n
    Ln2 = mp.fsum(mp.cot((2*r-1)*pi/(4*n)) for r in range(1, n+1))/n
    err = max(err, abs(4*s/n**2 - Ln**2), abs(Ln - Ln2))
rep("(13) equal-mesh sum = L_n^2 and L_n=(1/n)sum cot y_r, n=2..29", err < 1e-20, mp.nstr(err, 3))
rep("L_2 = sqrt 2", abs(2*mp.csc(pi/4)/2 - mp.sqrt(2)) < 1e-25)
for n in (50, 200, 800):
    Ln = mp.fsum(mp.cot((2*r-1)*pi/(4*n)) for r in range(1, n+1))/n
    print("  n=%d  n^2 (L_n - A(n)) = %s" % (n, mp.nstr(n**2*(Ln - a*(mp.log(n)+d)), 8)))

# (14) deformation bound: max ratio
worst = 0
for n in list(range(2, 41)) + [64, 101]:
    m = n+1
    for j in range(n+1):
        for k in range(n+1):
            if (j+k) % 2 == 1:
                th, ph, tk = j*math.pi/n, k*math.pi/m, k*math.pi/n
                f1 = (1+math.cos(ph))/abs(math.cos(th)-math.cos(ph))
                f0 = (1+math.cos(tk))/abs(math.cos(th)-math.cos(tk))
                l = abs(j-k)
                worst = max(worst, abs(f1-f0)/(math.pi**2*n/(2*l*l)))
rep("(14) |f(th,ph)-f(th,th)| <= pi^2 n/(2 l^2), n<=40,64,101", worst <= 1, "max ratio %.4f" % worst)

# kappa limit (15): Lambda_c - A(n)^2 -> kappa  ; and full expansion
def lam_c_fast(n):
    # (12a) in float64, adequate for consistency illustration
    m = n+1
    r = np.arange(1, m); x = r/m; al = (1-x)/2
    s = 0.0
    for rr, xx, aa in zip(r, x, al):
        l = np.arange(rr)
        s += (1/np.tan(np.pi*xx/2))*np.sum(1/np.tan(np.pi*(l+aa)/n))
    return 1 - 2*n/m + 4*s/(n*m)
fa, fb, fd, fk = float(a), float(b), float(d), float(kap)
print("  n, Lambda_c(n), four-term expansion, N*(Lambda_c - A(N)^2 - kappa)")
for n in (2, 3, 4, 10, 50, 200, 1000, 3000):
    lc = float(lam_c_8(n)) if n <= 10 else lam_c_fast(n)
    N = n + 0.5
    exp4 = 4/math.pi**2*math.log(N)**2 + fb*math.log(N) + float(c) - 1/N
    print("  %5d  %.10f  %.10f  %.6f" % (n, lc, exp4, N*(lc - fa**2*(math.log(N)+fd)**2 - fk)))

# ---------- Section 3.3 constants ----------
psi = mp.digamma
rep("psi(1/2) = -gamma-2log2", abs(psi(mp.mpf(1)/2) + gam + 2*mp.log(2)) < 1e-25)
rep("psi'(1/2) = pi^2/2", abs(mp.psi(1, mp.mpf(1)/2) - pi**2/2) < 1e-25)
rep("psi(R+1/2)=psi(1/2)+2H_{2R}-H_R (R=1..6)",
    max(abs(psi(R+mp.mpf(1)/2) - psi(mp.mpf(1)/2) - 2*mp.harmonic(2*R) + mp.harmonic(R)) for R in range(1, 7)) < 1e-25)
q0 = pi**2/4 - 1
Su = mp.nsum(lambda r: (r*mp.psi(1, r+mp.mpf(1)/2) - 1)/r, [1, mp.inf])
rep("S_u = 1+2log2-pi^2/4", abs(Su - (1+2*mp.log(2)-pi**2/4)) < 1e-15, mp.nstr(Su, 12))
rep("q0 + S_u = 2 log 2", abs(q0 + Su - 2*mp.log(2)) < 1e-15)
rep("finite recurrence sum_{r<=R} psi'(r+1/2) identity R=1..7",
    max(abs(mp.fsum(mp.psi(1, r+mp.mpf(1)/2) for r in range(1, R+1)) -
            ((R+mp.mpf(1)/2)*mp.psi(1, R+mp.mpf(1)/2) + psi(R+mp.mpf(1)/2) - psi(mp.mpf(1)/2) - mp.psi(1, mp.mpf(1)/2)/2))
        for R in range(1, 8)) < 1e-25)
# (16) uniform for z>=1: sup z^2 |psi - log z + 1/(2z)|, z^2|psi' - 1/z|
zs = [1 + k*0.25 for k in range(0, 400)]
print("  sup z^2|psi-log z+1/(2z)| on [1,100] = %s ; sup z^2|psi'-1/z| = %s" % (
    mp.nstr(max(z**2*abs(psi(z) - mp.log(z) + 1/(2*z)) for z in zs), 5),
    mp.nstr(max(z**2*abs(mp.psi(1, z) - 1/mp.mpf(z)) for z in zs), 5)))
# ψ'' bound |ψ''| <= z^-2 + 2 z^-3
rep("|psi''(z)| <= z^-2+2z^-3 on sample z in (0.05,50)",
    all(abs(mp.psi(2, z)) <= z**-2 + 2*z**-3 for z in [mp.mpf(k)/20 for k in range(1, 1000)]))
# e_r, u_r decay
print("  r^2 e_r (r=50,400):", mp.nstr(50**2*(psi(50.5)-mp.log(50)), 6), mp.nstr(400**2*(psi(400.5)-mp.log(400)), 6),
      "; r^2 u_r:", mp.nstr(50**2*(50*mp.psi(1, 50.5)-1), 6), mp.nstr(400**2*(400*mp.psi(1, 400.5)-1), 6))
# (19) centring error: max m^2 |D - centred|
worst = 0
for m in list(range(3, 120)) + [301]:
    n = m-1
    for r in range(1, m):
        s_ = m-r; x = mp.mpf(r)/m; al = (1-x)/2
        D = psi(r+al) + psi(s_-al) - psi(m-al) - psi(al)
        cen = psi(r+mp.mpf(1)/2) + psi(s_) - psi(al) - psi(m) - (r*mp.psi(1, r+mp.mpf(1)/2) + s_*mp.psi(1, s_) - s_*mp.psi(1, m))/(2*m)
        worst = max(worst, m**2*abs(D - cen))
print("  (19) max m^2 |D - centred| over m<=119,301:", mp.nstr(worst, 5))
# (20) remainder Q / (s^-2+(ms)^-1+m^-2)
worst = 0
F_ = lambda x: mp.log(x) + mp.log(1-x) - psi((1-x)/2)
for m in list(range(3, 90)) + [301]:
    for r in range(1, m):
        s_ = m-r; x = mp.mpf(r)/m; al = (1-x)/2
        D = psi(r+al) + psi(s_-al) - psi(m-al) - psi(al)
        er = psi(r+mp.mpf(1)/2) - mp.log(r); ur = r*mp.psi(1, r+mp.mpf(1)/2) - 1
        Q = D - (mp.log(m) + F_(x) + er - 1/(2*m*(1-x)) - (x+ur)/(2*m))
        worst = max(worst, abs(Q)/(mp.mpf(1)/s_**2 + mp.mpf(1)/(m*s_) + mp.mpf(1)/m**2))
print("  (20) max |Q|/(s^-2+(ms)^-1+m^-2):", mp.nstr(worst, 5))
# J(0)=d0, J'(0)=q0, R(0), R(1)
d0 = gam + 2*mp.log(2)
J = lambda x: mp.log(1-x) - psi((1-x)/2)
rep("J(0)=d0, J'(0)=q0", abs(J(0)-d0) < 1e-25 and abs(mp.diff(J, 0) - q0) < 1e-20)
Rf = lambda x: w_(x)*F_(x) - a*(mp.log(x)+d0)/x
rep("R(0+)=a q0, R(1-)=pi - a d0",
    abs(Rf(mp.mpf('1e-12')) - a*q0) < 1e-9 and abs(Rf(1-mp.mpf('1e-12')) - (pi - a*d0)) < 1e-9)
# integrals I1, I2, IB, (23)
I1 = mp.quad(lambda x: w_(x)/(1-x) - a/x, [0, 1])
I2 = mp.quad(lambda x: x*w_(x), [0, 1])
IB = mp.quad(lambda x: x*w_(x)*B_(x), [0, 1])
rep("(23) 2I_B - a I_1 = a^2-1+a^2 log(pi/2)", abs(2*IB - a*I1 - (a**2 - 1 + a**2*mp.log(pi/2))) < 1e-20,
    mp.nstr(2*IB - a*I1, 17))
bH = -2 - a**2*(gam + 2*mp.log(2)) - a*(I1 + I2)
bB = -a**2 + 2*IB + a*I2
rep("2 + beta_H + beta_B = -1 - a^2 d", abs(2 + bH + bB + 1 + a**2*d) < 1e-20, mp.nstr(2+bH+bB, 15))
rep("int_0^1 (w - a/x) = a log(2/pi)", abs(mp.quad(lambda x: w_(x) - a/x, [0, 1]) - a*mp.log(2/pi)) < 1e-20)
rep("int_0^{pi/2}(cot y - 1/y) = log(2/pi)", abs(mp.quad(lambda y: mp.cot(y) - 1/y, [0, pi/2]) - mp.log(2/pi)) < 1e-20)
# integrand identity of (23) at sample points
x = mp.mpf('0.37'); ww = w_(x)
lhs = 2*x*ww*B_(x) - a*(ww/(1-x) - a/x)
mid = x*(ww**2-1) - 2*a*ww + a**2/x
rhs = -a*mp.diff(lambda t: t*w_(t), x) - a*(ww - a/x) - 2*x
rep("(23) integrand identities at x=0.37", abs(lhs-mid) < 1e-25 and abs(mid-rhs) < 1e-20)
# C_K
fK = lambda t: mp.log(t)/t
CK = mp.nsum(lambda j: (fK(j)+fK(j+1))/2 - (mp.log(j+1)**2 - mp.log(j)**2)/2, [1, mp.inf])
mm = 2000
lhs = mp.fsum(mp.log(r)/r for r in range(1, mm))
print("  C_K = %s ; m^2/log m * residual at m=2000: %s" % (mp.nstr(CK, 10),
      mp.nstr((lhs - (mp.log(mm)**2/2 + CK - mp.log(mm)/(2*mm)))*mm**2/mp.log(mm), 5)))
# (22) weight sum
for mm in (50, 400):
    ws = mp.fsum(w_(mp.mpf(r)/mm) for r in range(1, mm))/mm
    print("  (22) m=%d m^2*(weight sum - a(log m+gamma+log(2/pi))) = %s" % (mm, mp.nstr(mm**2*(ws - a*(mp.log(mm)+gam+mp.log(2/pi))), 6)))
# F_B(0)=a^2/2, G_B(0)=a^2, C_B and kappa consistency (needs C_H): C_H from large m extrapolation
CB = 4*mp.quad(lambda t: w_(t)*mp.quad(B_, [0, t]) if t > 0 else 0, [0, 1])
rep("F_B(0)=a/pi=a^2/2, G_B(0)=2a/pi=a^2", abs(a/pi - a**2/2) < 1e-25 and abs(2*a/pi - a**2) < 1e-25)
def Hm(m):
    s = mp.mpf(0)
    for r in range(1, m):
        x = mp.mpf(r)/m; s_ = m-r; al = (1-x)/2
        s += w_(x)*(psi(r+al) + psi(s_-al) - psi(m-al) - psi(al))
    return 4*s/(pi*m)
CHs = []
for m in (400, 800):
    A2 = a**2*(mp.log(m)+d)**2
    CHs.append(Hm(m) - A2 - (-a**2*mp.log(m) + bH)/m)
print("  C_H estimates (m=400,800):", [mp.nstr(v, 10) for v in CHs], " C_B =", mp.nstr(CB, 12))
print("  -1 + C_H + C_B =", mp.nstr(-1 + CHs[-1] + CB, 10), " vs kappa", mp.nstr(kap, 10))
rep("-1 + C_H + C_B approx kappa (1e-6)", abs(-1 + CHs[-1] + CB - kap) < 1e-6)
# smooth part (18): 4V_n/(nm) vs C_B + beta_B/n
for n in (100, 400):
    m = n+1; V = mp.mpf(0)
    for r in range(1, m):
        x = mp.mpf(r)/m; al = (1-x)/2
        V += w_(x)*mp.fsum(B_((l+al)/n) for l in range(r))
    print("  (18) n=%d  n^2*(4V/(nm) - C_B - beta_B/n) = %s" % (n, mp.nstr(n**2*(4*V/(n*m) - CB - bB/n), 6)))
# half step
z_ = sp.symbols('z', positive=True)
Ps = sp.Symbol('a')**2*(sp.log(z_)+sp.Symbol('d'))**2
rep("P' and P'' formulas", sp.simplify(sp.diff(Ps, z_) - 2*sp.Symbol('a')**2*(sp.log(z_)+sp.Symbol('d'))/z_) == 0 and
    sp.simplify(sp.diff(Ps, z_, 2) - 2*sp.Symbol('a')**2*(1 - sp.log(z_) - sp.Symbol('d'))/z_**2) == 0)
# (9) B endpoint values
rep("B(0+)=1/pi, B(1-)=-1/pi", abs(B_(mp.mpf('1e-15')) - 1/pi) < 1e-12 and abs(B_(1-mp.mpf('1e-15')) + 1/pi) < 1e-12)
rep("w(x) <= pi(1-x) on [1/2,1)", all(w_(mp.mpf(k)/1000) <= pi*(1-mp.mpf(k)/1000) for k in range(500, 1000)))
# sinc identity cot z - 1/z = -z int t^2 sinc(tz)/sinc z
zz = mp.mpf('0.83')
rep("cot z - 1/z = -z int_0^1 t^2 sinc(tz) dt / sinc z",
    abs(mp.cot(zz) - 1/zz + zz*mp.quad(lambda t: t**2*mp.sinc(t*zz), [0, 1])/mp.sinc(zz)) < 1e-25)
print("ALL PASS" if ok else "SOME FAIL", " elapsed %.1fs" % (time.time() - t0))
