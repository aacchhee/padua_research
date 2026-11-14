# M5A s2: row-average decomposition (C4B-02) and the four atomic row identities (C4C-M3).
# Finite identities are checked in float64 / mpmath at sampled phases (MEASURED);
# the trigonometric reductions are also checked symbolically with sympy.
import numpy as np
import mpmath as mp
import sympy as sp
from scipy import integrate, special

rng = np.random.default_rng(20261113)
ok = True
def check(name, cond, info=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + str(info) if info else ""))

def Pn(n, u):  # T_{n+1}(cos u) + T_n(cos u)
    return np.cos((n + 1) * u) + np.cos(n * u)

def Gn(n, u, v):  # divided-difference evaluation form (localization:68-69)
    return (Pn(n, u) - Pn(n, v)) / (np.cos(u) - np.cos(v)) - np.cos(n * u)

def coeffs(x, y, v):
    p, q = np.sin(x), np.sin(y)
    a = (np.cos(x) + np.cos(y)) / 2
    Cm = (p - q - 2 * a / np.tan(v / 2)) / 4
    Cp = (p + q + 2 * a / np.tan(v / 2)) / 4
    etam = 0.5 + (x - y + v) / (2 * np.pi)
    etap = 0.5 + (x + y - v) / (2 * np.pi)
    return a, Cm, Cp, etam, etap

def Nn(n, eta):
    k = np.arange(n)
    return np.sum(np.abs(1 / np.tan(np.pi * (k + eta) / n)))

def gfun(C, D, e, t):
    A = C / np.tan(t); B = D / np.tan(t + e)
    return np.abs(A + B) - np.abs(A) - np.abs(B)

# ---------- C4B-02: exact row identities at n = 192, 256, 512 ----------
for n in (192, 256, 512):
    m = n + 1
    worst_cot = worst_dec = worst_Cid = worst_off = 0.0
    for trial in range(40):
        x, y = rng.uniform(0, np.pi, 2)
        if x + y >= np.pi:
            x, y = np.pi - x, np.pi - y
        r = int(rng.integers(2, 2 * m - 2))
        dr = (1 - r) % 2
        k = np.arange(n)
        u = (dr * np.pi + x + 2 * k * np.pi) / n
        v = (r * np.pi + y) / m
        a, Cm, Cp, etam, etap = coeffs(x, y, v)
        G = Gn(n, u, v)
        lhs = (-1) ** dr * G / 2
        rhs = Cm / np.tan((u - v) / 2) + Cp / np.tan((u + v) / 2)
        worst_cot = max(worst_cot, np.max(np.abs(lhs - rhs) / (1 + np.abs(lhs))))
        # offsets
        o1 = (n * (u - v) / (2 * np.pi) - etam) % 1.0
        o2 = (n * (u + v) / (2 * np.pi) - etap) % 1.0
        worst_off = max(worst_off, np.max(np.minimum(o1, 1 - o1)), np.max(np.minimum(o2, 1 - o2)))
        # weight identities
        ce, cd = np.cos((x + y) / 2), np.cos((x - y) / 2)
        Cm2 = -ce * np.sin(np.pi * etam) / (2 * np.sin(v / 2))
        Cp2 = cd * np.sin(np.pi * etap) / (2 * np.sin(v / 2))
        worst_Cid = max(worst_Cid, abs(Cm - Cm2), abs(Cp - Cp2))
        # row decomposition R_r/n = |C-|N(eta-)/n + |C+|N(eta+)/n + (1/n) sum g
        Rr = np.sum(np.abs(G / 2))
        X = (u - v) / 2
        dec = abs(Cm) * Nn(n, etam) / n + abs(Cp) * Nn(n, etap) / n + np.sum(gfun(Cm, Cp, v, X)) / n
        worst_dec = max(worst_dec, abs(Rr / n - dec) / (1 + Rr / n))
    check(f"n={n}: (-1)^d G/2 = C- cot + C+ cot (40 rows)", worst_cot < 1e-8, f"{worst_cot:.2e}")
    check(f"n={n}: offsets == eta-, eta+ mod 1", worst_off < 1e-8, f"{worst_off:.2e}")
    check(f"n={n}: C-/C+ weight identities", worst_Cid < 1e-12, f"{worst_Cid:.2e}")
    check(f"n={n}: R_r/n = |C-|N/n+|C+|N/n+(1/n)sum g", worst_dec < 1e-10, f"{worst_dec:.2e}")

# pole estimate with digamma profile
for n in (192, 256, 512):
    L = np.log(n)
    worst = 0
    for eta in np.linspace(0.001, 0.999, 61):
        prof = (2 * L + (-special.digamma(eta) - special.digamma(1 - eta)) - 2 * np.log(np.pi)) / np.pi
        worst = max(worst, abs(Nn(n, eta) / n - prof) * n * n)
    check(f"n={n}: |N_n/n - (2L+C-2log pi)/pi| n^2 <= 5", worst <= 5, f"max n^2 err={worst:.3f}")

# worked row value quoted in the companion table: (x,y)=(0.4,0.3), n=512, r=253
def Ccal(t):
    return -special.digamma(t) - special.digamma(1 - t)
def Phi(t):
    t = t - np.floor(t)
    return 1.0 if t == 0 else np.sin(np.pi * t) / np.pi * (Ccal(t) - 2 * np.log(np.pi))
def Icanc(C, D, e):
    # complete cancellation integral; split at poles, sign changes and equality roots
    f = lambda t: gfun(C, D, e, t)
    grid = np.linspace(1e-12, np.pi - 1e-12, 200001)
    vals = np.abs(C / np.tan(grid)) - np.abs(D / np.tan(grid + e))
    s1 = np.sign(C / np.tan(grid)) * np.sign(D / np.tan(grid + e))
    pts = set([0.0, np.pi, (np.pi - e) % np.pi])
    for arr in (vals, s1):
        idx = np.nonzero(np.diff(np.sign(arr)))[0]
        for i in idx:
            pts.add(grid[i]); pts.add(grid[i + 1])
    pts = sorted(p for p in pts if 0 <= p <= np.pi)
    tot = 0.0
    for a0, b0 in zip(pts[:-1], pts[1:]):
        if b0 - a0 > 1e-14:
            tot += integrate.quad(f, a0, b0, limit=200, epsabs=1e-13)[0]
    return tot
x, y, n, r = 0.4, 0.3, 512, 253
m = n + 1; L = np.log(n)
dr = (1 - r) % 2
k = np.arange(n)
u = (dr * np.pi + x + 2 * k * np.pi) / n
v = (r * np.pi + y) / m
Rr_n = np.sum(np.abs(Gn(n, u, v) / 2)) / n
a, Cm, Cp, etam, etap = coeffs(x, y, v)
ce, cd = np.cos((x + y) / 2), np.cos((x - y) / 2)
A = 2 * (abs(Cm) + abs(Cp)) / np.pi
B = (ce * Phi(etam) + cd * Phi(etap)) / (2 * np.sin(v / 2)) + Icanc(Cm, Cp, v) / np.pi
V = A * L + B
check("worked row r=253: R_r/n = 5.265493", abs(Rr_n - 5.265493) < 5e-7, f"{Rr_n:.7f}")
check("worked row r=253: profile V = 5.265474", abs(V - 5.265474) < 5e-6, f"{V:.7f}")

# ---------- C4C-M3: four atomic row identities ----------
def sinc(t):
    return np.sinc(t / np.pi)
def tau(t):
    return 1.0 if t == 0 else t / np.tan(t)
for n in (192, 256, 512):
    m = n + 1; mu = n / m
    w1 = w2 = w3 = w4 = 0.0
    possets_ok = True
    for trial in range(60):
        x, y = rng.uniform(0, 1.5, 2)
        if x + y >= np.pi - 1e-3:
            continue
        for (rr, b) in ((1, y), (1, -y), (2, -y)):
            w = rr * np.pi + b
            ce, cd = np.cos((x + b) / 2), np.cos((x - b) / 2)
            a = ce * cd
            # reference f_j, many indices of parity 1-r
            J = np.arange(-(4001 + rr), 4002 + rr)
            J = J[(J - (1 - rr)) % 2 == 0]
            z = J * np.pi + x
            sm = (-1.0) ** ((rr - J - 1) // 2)
            sp_ = (-1.0) ** ((J + rr - 1) // 2)
            fj = (ce * sm * sinc((z - w) / 2) + cd * sp_ * sinc((z + w) / 2)) / w
            w1 = max(w1, np.max(np.abs(fj - 4 * a / (w * w - z * z))))
            # symmetric sum plus tail estimate ~ -4a * 2 * sum_{|z|>Z} 1/z^2
            tail = -4 * a * 2 / (2 * np.pi * np.pi) / (J.max())  # -4a*sum 1/z^2 over |j|>J (spacing 2)
            w2 = max(w2, abs(np.sum(fj) + tail - (-np.sin(b) / w)))
            pos = set(J[fj > 0].tolist())
            want = set(range(-rr + 1, rr, 2))
            if pos != want:
                possets_ok = False
            # actual signed row over the n actual indices
            Ja = np.arange(-n - 2, n + 2)
            Ja = Ja[((Ja - (1 - rr)) % 2 == 0)]
            uj = (Ja * np.pi + x) / n
            Ja = Ja[(uj >= -np.pi) & (uj < np.pi)]
            assert len(Ja) == n, (len(Ja), n)
            z = Ja * np.pi + x; uj = z / n; vv = w / m
            sm = (-1.0) ** ((rr - Ja - 1) // 2); sp_ = (-1.0) ** ((Ja + rr - 1) // 2)
            Fj_nm = (ce * sm * sinc((z - mu * w) / 2) * np.array([tau(t) for t in (uj - vv) / 2])
                     + cd * sp_ * sinc((z + mu * w) / 2) * np.array([tau(t) for t in (uj + vv) / 2])) / (2 * m * np.sin(w / (2 * m)))
            signed = np.sum(Fj_nm)
            target = a / m - np.sin(b) / w * tau(vv / 2)
            w3 = max(w3, abs(signed - target))
            # intermediate tangent form with chart coefficients
            p = np.sin(x); qb = np.sin(b)
            Cm = (p - qb - 2 * a / np.tan(vv / 2)) / 4
            Cp = (p + qb + 2 * a / np.tan(vv / 2)) / 4
            inter = -(Cm * np.tan((x - b + vv) / 2) + Cp * np.tan((x + b - vv) / 2)) / m
            w4 = max(w4, abs(signed - inter))
    check(f"n={n}: f_j = 4a/(w^2-z^2)", w1 < 1e-12, f"{w1:.1e}")
    check(f"n={n}: sum f_j = -sin b/w (with tail)", w2 < 1e-6, f"{w2:.1e}")
    check(f"n={n}: positive set = {{-r+1,...,r-1}} on interior samples", possets_ok)
    check(f"n={n}: (1/nm) sum F_j = a/m - (sin b/w) tau(v/2)", w3 < 1e-11, f"{w3:.1e}")
    check(f"n={n}: intermediate -(1/m){{C- tan + C+ tan}} form", w4 < 1e-11, f"{w4:.1e}")

# symbolic braces reduction: C- tan(a1)+C+ tan(b1) = -a + (sin b/2) cot(v/2)
X, Bv, Vv = sp.symbols('x b v', real=True)
aa = (sp.cos(X) + sp.cos(Bv)) / 2
Cm = (sp.sin(X) - sp.sin(Bv) - 2 * aa * sp.cot(Vv / 2)) / 4
Cp = (sp.sin(X) + sp.sin(Bv) + 2 * aa * sp.cot(Vv / 2)) / 4
expr = Cm * sp.tan((X - Bv + Vv) / 2) + Cp * sp.tan((X + Bv - Vv) / 2) - (-aa + sp.sin(Bv) / 2 * sp.cot(Vv / 2))
vals = [abs(complex(expr.subs({X: xv, Bv: bv, Vv: vv}).evalf(30))) for xv, bv, vv in
        [(0.3, 0.2, 0.01), (0.7, -0.4, 0.02), (1.1, 0.5, 0.3), (0.2, -0.9, 1.3)]]
check("braces reduce to -a+(sin b/2)cot(v/2) (sympy, 4 points, 30 digits)", max(vals) < 1e-25, f"{max(vals):.1e}")
tsum = sp.simplify(sp.tan((Bv - X) / 2) + sp.tan((Bv + X) / 2) - sp.sin(Bv) / aa)
check("tan((b-x)/2)+tan((b+x)/2) = sin b / a", tsum == 0 or abs(complex(tsum.subs({X: 0.37, Bv: 0.81}).evalf())) < 1e-25)
print("ALL PASS" if ok else "SOME FAIL")
