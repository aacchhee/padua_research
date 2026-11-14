"""C2B audit: numerical (MEASURED, not proof) checks of analytic inequalities
asserted or explained in companion comparison-unified.tex L2001-4037.
Grid-based sup/variation estimates; reported as worst ratio claim/bound.
"""
import numpy as np
from scipy.special import digamma
from scipy.integrate import quad
rng = np.random.default_rng(7)
PI = np.pi

def Ccal(t):
    return -digamma(t) - digamma(1 - t)
def Phi(t):
    t = np.mod(t, 1.0)
    out = np.ones_like(t, dtype=float)
    msk = (t > 1e-12) & (t < 1 - 1e-12)
    tt = t[msk]
    out[msk] = np.sin(PI*tt)/PI*(Ccal(tt) - 2*np.log(PI))
    return out
def f(w):
    return Phi(0.5 + np.asarray(w, dtype=float)/(2*PI))
f0 = float(f(np.array([0.0]))[0])

def var(y):
    return np.abs(np.diff(y)).sum()

worst = {}
def upd(k, v):
    worst[k] = max(worst.get(k, -np.inf), v)

# ---------- cancellation J closed form, validated by quadrature
def J_closed(v, s, e):
    if v == 0:
        return 2*s*np.log(np.sin(e))
    if s <= v:
        c, b = (v-s)/2, (v+s)/2
        cl = c*np.log(c/v) if c > 0 else 0.0
        return 2*(cl + b*np.log(b/v))
    c, b = (s-v)/2, (s+v)/2
    if s*np.sin(e) >= v:
        return 2*s*np.log(np.sin(e))
    t1 = (np.arcsin(s*np.sin(e)/v) - e)/2
    return 2*s*np.log(np.sin(e)) + 2*(b*np.log(np.cos(t1)/np.sin(t1+e)) - c*np.log(np.cos(t1+e)/np.sin(t1)))

def J_quad(v, s, e):
    C, D = (v-s)/2, (v+s)/2
    g = lambda t: abs(C/np.tan(t) + D/np.tan(t+e)) - abs(C/np.tan(t)) - abs(D/np.tan(t+e))
    pts = sorted({PI/2-e, PI/2, PI-e})
    val, _ = quad(g, 1e-12, PI-1e-12, points=pts, limit=400)
    return val

for _ in range(40):
    v = rng.uniform(0, 1); s = rng.uniform(0, 1.5); e = rng.uniform(0.05, PI/2)
    upd("J closed vs quad", abs(J_closed(v, s, e) - J_quad(v, s, e)))

def R_(v, s, e):
    return J_closed(v, s, e) - 2*max(s - v, 0)*np.log(np.sin(e))

# ---------- (L2364) L-coefficient sup M_A and variation V_A over both folded sides
def Acoef(v, x, y):
    a = np.cos((x+y)/2)*np.cos((x-y)/2); p, q = np.sin(x), np.sin(y)
    C = (p - q - 2*a/np.tan(v/2))/4; D = (p + q + 2*a/np.tan(v/2))/4
    return 2*(np.abs(C) + np.abs(D))/PI, a, p, q
z = np.linspace(1e-4, PI - 1e-4, 40001)
for _ in range(400):
    x = rng.uniform(0, PI); y = rng.uniform(0, PI - x)
    AL, a, p, q = Acoef(z, x, y); AR, *_ = Acoef(2*PI - z, x, y)
    gL = AL - 4*a/(PI*z); gR = AR - 4*a/(PI*z)
    MA = max(p, q)/PI + 4*a/PI**2
    upd("sup|L-coef|/M_A^phi", max(np.abs(gL).max(), np.abs(gR).max())/MA)
    upd("(Var gL+Var gR)/V_A^phi", (var(gL) + var(gR))/(2*MA))

# ---------- (L2473-2483) central cancellation sup<4 per side, variation < 20 combined
e = np.linspace(1e-4, PI/2, 3001)
for _ in range(150):
    x = rng.uniform(0, PI); y = rng.uniform(0, PI - x)
    a = np.cos((x+y)/2)*np.cos((x-y)/2); p, q = np.sin(x), np.sin(y); dp = max(q - p, 0)
    tot_var = 0.0
    for side in ("L", "R"):
        s0 = a*np.tan(e/2)
        ss = s0 + q/2 if side == "L" else np.abs(s0 - q/2)
        ks = 2*np.maximum(ss - p/2, 0)
        Rv = np.array([R_(p/2, si, ei) for si, ei in zip(ss, e)])
        val = (ks - dp)*np.log(np.sin(e)) + dp*np.log(np.sin(e)/e) + Rv
        upd("central cancellation sup per side (claim <4)", np.abs(val).max())
        tot_var += var(val)
    upd("central cancellation var both sides (claim <20)", tot_var)

# ---------- (L3833-3856) relative cancellation: b_s, envelopes on rho<=1
for _ in range(200):
    rho = rng.uniform(1e-3, 1); x = rng.uniform(0, rho); y = rho - x
    a = np.cos(rho/2)*np.cos((x-y)/2); p, q = np.sin(x), np.sin(y); dp = max(q-p, 0)
    s0 = a*np.tan(e/2)
    bL = np.maximum(q-p, -2*s0) - dp; bR = np.maximum.reduce([np.full_like(e, -p-q), q-p-4*s0, -2*s0]) - dp
    upd("b_s combined sup /(3 rho)", (np.abs(bL).max() + np.abs(bR).max())/(3*rho))
    upd("b_s nonincreasing violation", max(np.diff(bL).max(), np.diff(bR).max()))
    for side, bs in (("L", bL), ("R", bR)):
        ss = s0 + q/2 if side == "L" else np.abs(s0 - q/2)
        Rv = np.array([R_(p/2, si, ei) for si, ei in zip(ss, e)])
        Cs = Rv + bs*np.log(np.sin(e)) + dp*np.log(np.sin(e)/e)
        env = rho*(7 + 4*(-np.log(np.sin(e))))
        upd("central hole envelope |C_s|/rho[7+4(-log sin e)]", (np.abs(Cs)/env).max())
    zz = np.linspace(1e-5, PI/2, 2001)
    Ci = np.maximum(np.abs(q*np.log(np.sin(zz)) - dp*np.log(PI-zz)), np.abs(-q*np.log(np.sin(zz)) - dp*np.log(PI-zz)))
    upd("initial hole envelope ratio", (Ci/(rho*(np.log(PI/(2*zz)) + np.log(PI)))).max())

# ---------- F_0 checks (L2884-3047, L3926-3971)
def F0parts(zv, L):
    b = 2/np.tan(zv/2) - 4/zv; d = 1/(2*np.sin(zv/2)) - 1/zv
    fz = f(zv)
    P0 = 2*(fz - f0)/zv + 2*fz*d
    Q0 = 2/np.tan(zv/2)*np.log(np.sin(zv)) - 4*np.log(zv)/zv
    return (L/PI)*b + P0 + Q0/PI
for n in (32, 64, 160, 320, 1000, 5000):
    m = n + 1; h = PI/m; L = np.log(n)
    zz = np.linspace(1e-7, 5*h/2, 4001)
    env = 7*zz/6 + zz/PI*np.maximum(np.log(PI/(2*n*zz)), 0)
    upd("initial-hole F0/envelope (claim <=1)", (F0parts(zz, L)/env).max())
    zc = np.linspace(21*PI/22, PI - 1e-9, 2001)
    upd("central-hole max F0 (claim < -1/25)", F0parts(zc, L).max())
    for lo, hi, Vb, Mb, lab in ((h/2, PI - h/2, L/2 + 12.5*np.log(2*m) + 37/3, None, "[h/2,pi-h/2]"),
                                (2*h, PI - h, L/2 + 12.5*np.log(m) + 37/3, 4*L/3 + 2*np.log(m)/3 + 20/3, "[2h,pi-h]")):
        zg = np.concatenate([np.geomspace(lo, 0.5, 20000), np.linspace(0.5, hi, 40000)[1:]])
        F = F0parts(zg, L); dF = np.gradient(F, zg)
        upd(f"Var F0' / V {lab}", var(dF)/Vb)
        if Mb is not None:
            upd(f"sup|F0'| / M {lab}", np.abs(dF).max()/Mb)
    # nB_out < 1 used for n>=160 ; D, M bars are origin row/mesh allowances
# ---------- pole-regular table (L3662-3787): V_s bounds on grid
zi = np.linspace(1e-6, PI/2, 3001); zc = np.linspace(PI/2, PI, 3001)
for rad, tab in ((0.5, dict(sV=33/8, V0=5/8, dV=9/4, ddV=57/40, varC=17/2, Pvi=537/200, Psi=123/40, Pvc=731/96, Psc=337/96)),
                 (1.0, dict(sV=17/4, V0=5/4, dV=5/2, ddV=31/20, varC=9, Pvi=289/100, Psi=67/20, Pvc=395/48, Psc=193/48))):
    for _ in range(300):
        rho = rng.uniform(1e-3, rad); x = rng.uniform(0, rho); y = rho - x
        ce, cd = np.cos(rho/2), np.cos((x-y)/2); a = ce*cd; dlt = x - y; ee = rho
        for sgn in (+1, -1):
            Vs = lambda zv: ce*f(zv + sgn*dlt) + cd*f(zv - sgn*ee) - 2*a*f(zv)
            V0 = float(Vs(np.array([0.0]))[0])
            vi = Vs(zi); dvi = np.gradient(vi, zi); ddvi = np.gradient(dvi, zi)
            upd(f"rho<={rad} sup|V_s| init / table", np.abs(vi).max()/(tab['sV']*rho))
            upd(f"rho<={rad} |V_0| / table", abs(V0)/(tab['V0']*rho))
            upd(f"rho<={rad} sup|V_s'| / table", np.abs(dvi).max()/(tab['dV']*rho))
            upd(f"rho<={rad} sup|V_s''| / table", np.abs(ddvi[5:-5]).max()/(tab['ddV']*rho))
            vc = Vs(zc)
            upd(f"rho<={rad} Var_I V_s / table", var(vc)/(tab['varC']*rho))
            d_i = 1/(2*np.sin(zi/2)) - 1/zi
            Pi_ = (vi - V0)/zi + vi*d_i
            Pc_ = vc/(2*np.sin(zc/2)) - V0/zc
            upd(f"rho<={rad} P_s init var / table", var(Pi_)/(tab['Pvi']*rho))
            upd(f"rho<={rad} P_s init sup / table", np.abs(Pi_).max()/(tab['Psi']*rho))
            upd(f"rho<={rad} P_s cent var / table", var(Pc_)/(tab['Pvc']*rho))
            upd(f"rho<={rad} P_s cent sup / table", np.abs(Pc_).max()/(tab['Psc']*rho))

# ---------- perturbed-cancellation variation (L2250-2329)
tt = np.linspace(0, PI, 200001)[1:-1]
for _ in range(300):
    ee = rng.uniform(0.05, PI/2); eps = rng.uniform(0.01, 0.5); w = rng.uniform(-2, 2)
    c, d = rng.uniform(-eps, eps, 2)
    def g(C, D):
        X = C/np.tan(tt); Y = D/np.tan(tt + ee)
        return np.abs(X + Y) - np.abs(X) - np.abs(Y)
    G = g(-w + c, w + d) - g(-w, w)
    Gp = np.concatenate([[0.0], G, [0.0]])  # poles assigned zero; periodic closure
    upd("Var f / (24 eps/sin e)", var(Gp)/(24*eps/np.sin(ee)))
    C, D = rng.uniform(-2, 2, 2)
    Gg = np.concatenate([[0.0], g(C, D), [0.0]])
    upd("Var g / (8 max/sin e)", var(Gg)/(8*max(abs(C), abs(D))/np.sin(ee)))

# matched-cell defect: see c2b_defect.py (exact primitive + digamma tail)
for k_, v_ in worst.items():
    print(f"{k_:55s} worst = {v_:.4f}")
