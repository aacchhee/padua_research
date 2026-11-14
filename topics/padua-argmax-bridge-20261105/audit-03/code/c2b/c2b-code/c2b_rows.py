"""C2B audit: end-to-end numerical test of the ADDED finite-row identities in
comparison-unified.tex (companion):
  * L2572  sum_j |f_j| = ell_r (partial fractions) and f_j sinc formula
  * L3330-3341 exact endpoint error e_r = R_r/(nm) - ell_r, closest row e_0
  * L2836-2844 J_cen(0)=2/m and E_ret(0) formula
  * L2330 sum_{r notin A6} 1/|sin v_r| <= 2 m H_n
Uses only the ORIGINAL regular-sample identity
  (-1)^delta G_n(u,v_r)/2 = C(v_r) cot((u-v_r)/2) + D(v_r) cot((u+v_r)/2)
with C,D from uc:row-profile.  Floating point (double); tolerances printed.
"""
import numpy as np
rng = np.random.default_rng(20261108)

def setup(n, x, y):
    m = n + 1
    rho = x + y
    ce, cd = np.cos(rho/2), np.cos((x-y)/2)
    return dict(n=n, m=m, x=x, y=y, a=ce*cd, ce=ce, cd=cd, p=np.sin(x), q=np.sin(y))

def row_sum(S, r):
    n, m, x, y, a, p, q = (S[k] for k in "n m x y a p q".split())
    v = (r*np.pi + y)/m
    dl = (1 - r) % 2
    u = (dl*np.pi + x + 2*np.pi*np.arange(n))/n
    C = (p - q - 2*a/np.tan(v/2))/4
    D = (p + q + 2*a/np.tan(v/2))/4
    val = C/np.tan((u-v)/2) + D/np.tan((u+v)/2)
    return np.abs(val).sum(), val

def ell(S, r, b):
    a, x = S["a"], S["x"]
    w = r*np.pi + b
    js = np.arange(-r+1, r, 2)
    return np.sin(b)/w + 8*a*np.sum(1/(w**2 - (js*np.pi + x)**2))

def sinc(t):
    return np.sinc(t/np.pi)

def tau(t):
    return 1.0 if abs(t) < 1e-300 else t/np.tan(t)

def f_ref(S, r, b, j):
    x = S["x"]
    ce, cd = np.cos((x+b)/2), np.cos((x-b)/2)
    w = r*np.pi + b; z = j*np.pi + x
    sm = (-1)**((r-j-1)//2); sp = (-1)**((j+r-1)//2)
    return (ce*sm*sinc((z-w)/2) + cd*sp*sinc((z+w)/2))/w

def e_formula(S, r, b, P):
    n, m, x, a, p = S["n"], S["m"], S["x"], S["a"], S["p"]
    mu = n/m; w = r*np.pi + b; v = w/m
    tot = -a/m + np.sin(b)/w*(tau(v/2) - 1)
    for j in P:
        z = j*np.pi + x; u = z/n
        Dh = mu**2*w**2 - z**2; Dp = w**2 - z**2
        K = sinc((abs(u)+v)/2)*sinc((abs(u)-v)/2)
        Hh = (1 + np.cos(v))/(2*K)
        g = -p*np.sin(u) + np.sin(b)*np.sin(v)
        tot += 8*a*(mu/Dh - 1/Dp) + 8*mu*a*(Hh-1)/Dh + 2*mu*g/(Dh*K)
    return tot

worst = {}
def upd(k, v):
    worst[k] = max(worst.get(k, 0.0), v)

# --- 1. partial fraction sum |f_j| = ell_r and far bound
for trial in range(300):
    x = rng.uniform(0, 1); y = rng.uniform(0, 1 - x)
    S = setup(64, x, y)
    for r, b in ((1, y), (1, -y), (2, -y)):
        par = (1 - r) % 2
        J = np.arange(-200000 + par, 200001, 2)
        J = J[(J - par) % 2 == 0]
        fj = np.array([f_ref(S, r, b, j) for j in J]) if False else None
        x_ = S["x"]; ce, cd = np.cos((x_+b)/2), np.cos((x_-b)/2)
        w = r*np.pi + b; z = J*np.pi + x_
        sm = np.where(((r-J-1)//2) % 2 == 0, 1.0, -1.0); sp = np.where(((J+r-1)//2) % 2 == 0, 1.0, -1.0)
        fj = (ce*sm*sinc((z-w)/2) + cd*sp*sinc((z+w)/2))/w
        tail = 8*S["a"]/(np.pi**2*400000)  # crude tail ~ sum 4a/z^2 beyond
        upd("PF |sum|f_j|-ell_r|", abs(np.abs(fj).sum() - ell(S, r, b)))
        # structure: f_j = 4a/(w^2-z^2) + sin-part?  test far indices
        far = np.abs(z) >= 4*np.pi
        rel = np.abs(fj[far] - 4*S["a"]/(w**2 - z[far]**2)).max()
        upd("far f_j - 4a/(w^2-z^2) (max abs)", rel)
        pos = J[fj > 0]
        exp = [0] if r == 1 else [-1, 1]
        upd("positive reference set mismatch", 0.0 if list(pos) == exp else 1.0)

# boundary value at (r,b,x)=(1,-pi,0): linked limit
S = setup(64, 0.0, np.pi - 1e-7)
vals = [f_ref(S, 1, -(np.pi - 1e-7), j) for j in range(-6, 7, 2)]
print("f_j at (1,-pi+1e-7,0), j=-6..6 even:", np.round(vals, 6))

# --- 2. exact endpoint error e_r and closest row, on rho<=1
for n in (32, 33, 47, 160, 321):
    for trial in range(60):
        x = rng.uniform(1e-4, 1); y = rng.uniform(1e-4, 1 - x)
        S = setup(n, x, y); m = S["m"]
        for row, (r, b, P) in {1: (1, y, [0]), 2*m-1: (1, -y, [0]), 2*m-2: (2, -y, [-1, 1])}.items():
            R, val = row_sum(S, row)
            e_act = R/(n*m) - ell(S, r, b)
            e_for = e_formula(S, r, b, P)
            upd("e_r identity |actual-formula|", abs(e_act - e_for))
            upd("e_r identity rel", abs(e_act - e_for)/max(abs(e_act), 1e-12))
            # sign pattern: number of samples with sign opposite to bulk
            s = np.sign(val); bulk = np.sign(np.median(s))
            upd("count opposite-sign samples - |P| (chart)", abs(int((s != bulk).sum()) - len(P)))
        R0, val0 = row_sum(S, 0)
        e0_act = R0/(n*m) - sinc(y)
        e0_for = -S["a"]/m + sinc(y)*(tau(y/(2*m)) - 1)
        upd("closest row e_0 |actual-formula|", abs(e0_act - e0_for))
        s = np.sign(val0); upd("closest row opposite-sign samples", int((s != np.sign(np.median(s))).sum()))

# --- 3. origin: J_cen(0)=2/m and E_ret(0)
for n in (32, 33, 160, 161):
    S = setup(n, 1e-9, 1e-9); m = S["m"]
    Jc = (row_sum(S, m-1)[0] + row_sum(S, m)[0])/(n*m)
    upd("J_cen(0) - 2/m (scaled by m)", abs(Jc - 2/m)*m)
    Jend = sum(row_sum(S, r)[0] for r in (0, 1, 2*m-1, 2*m-2))/(n*m)
    C2 = sinc(S["y"]) + ell(S, 1, S["y"]) + ell(S, 1, -S["y"]) + ell(S, 2, -S["y"])
    mu = n/m
    sm = 0.0; sg = 0.0
    for (w, z) in ((np.pi, 0.0), (np.pi, 0.0), (2*np.pi, np.pi), (2*np.pi, -np.pi)):
        v = w/m; u = z/n
        Dh = mu**2*w**2 - z**2; Dp = w**2 - z**2
        K = sinc((abs(u)+v)/2)*sinc((abs(u)-v)/2); Hh = (1+np.cos(v))/(2*K)
        sm += mu/Dh - 1/Dp; sg += (Hh-1)/Dh
    Eret_for = -2/m + 8*sm + 8*mu*sg
    upd("E_ret(0) |actual-formula| *m", abs(Jend + Jc - C2 - Eret_for)*m)
    print(f"n={n}: E_ret(0)*m = {(Jend+Jc-C2)*m:.6f}  lower bound 22/45-71m/n^2 = {22/45-71*m/n**2:.6f}")

# --- 4. sum 1/|sin v_r| over r notin A6
for n in (32, 33, 100, 320, 1001):
    m = n + 1; Hn = sum(1/k for k in range(1, n+1))
    for y in np.linspace(0, np.pi, 41):
        A6 = {0, 1, 2*m-2, 2*m-1, m-1, m}
        s = sum(1/abs(np.sin((r*np.pi + y)/m)) for r in range(2*m) if r not in A6)
        upd("sum 1/|sin v_r| / (2 m H_n)", s/(2*m*Hn))

for k, v in worst.items():
    print(f"{k:45s} worst = {v:.3e}")
