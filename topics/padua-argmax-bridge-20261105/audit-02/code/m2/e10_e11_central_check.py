"""Independent numerical cross-check (sampled; NOT a proof) of E10/E11 central model bounds.
Claude audit2 m2. I(C,D,e) computed by direct quadrature for validation of the C06 closed
forms; Ec then from closed-form J. Domain: closed rho<=pi/2 (E11-halfpi), axes included."""
import mpmath as mp
mp.mp.dps = 20
pi = mp.pi

def I_direct(C, D, e):
    C, D, e = mp.mpf(C), mp.mpf(D), mp.mpf(e)
    f = lambda x: abs(C*mp.cot(x)+D*mp.cot(x+e)) - abs(C*mp.cot(x)) - abs(D*mp.cot(x+e))
    pts = [mp.mpf(0), pi-e, pi]
    # roots of C cot x + D cot(x+e) = 0  <=> C sin(x+e)cos x + D cos(x+e) sin x = 0
    # <=> (C+D) sin(2x+e) + (C-D) sin(e) = 0  -> sin(2x+e) = (D-C) sin e/(C+D)
    if C + D != 0:
        r = (D-C)*mp.sin(e)/(C+D)
        if abs(r) <= 1:
            th = mp.asin(r)
            for cand in [(th-e)/2, (pi-th-e)/2, (th-e)/2+pi, (pi-th-e)/2+pi, (th-e)/2-pi]:
                if 0 < cand < pi: pts.append(cand)
    pts = sorted(set(pts))
    return mp.quad(f, pts)

def J(u, s, e):
    u, s, e = mp.mpf(u), mp.mpf(s), mp.mpf(e)
    if s <= u:
        c, b = (u-s)/2, (u+s)/2
        if u == 0: return mp.mpf(0)
        t = lambda w: 0 if w == 0 else w*mp.log(w/u)
        return 2*(t(c)+t(b))
    c, b = (s-u)/2, (s+u)/2
    if s*mp.sin(e) >= u:
        return 2*s*mp.log(mp.sin(e))
    th = mp.asin(s*mp.sin(e)/u); x1 = (th-e)/2
    return 2*s*mp.log(mp.sin(e)) + 2*(b*mp.log(mp.cos(x1)/mp.sin(x1+e)) - c*mp.log(mp.cos(x1+e)/mp.sin(x1)))

def Zf(v, s, e):
    v, s, e = mp.mpf(v), mp.mpf(s), mp.mpf(e)
    if v == 0: return mp.mpf(0)
    g = lambda t: mp.sqrt(max(v*v - s*s*mp.sin(t)**2, 0))/mp.sin(t)
    pts = [e]
    if s > v:
        tr = mp.asin(v/s)
        if e < tr < pi/2: pts.append(tr)
    pts.append(pi/2)
    return 2*mp.quad(g, pts)

out = []
def rep(*a):
    s = " ".join(str(z) for z in a); print(s); out.append(s)

# 1. validate closed-form J against direct I at sample parameters (incl. root and no-root cases)
mx = 0
for (u, s, e) in [(0.3, 0.1, 0.7), (0.3, 0.5, 0.4), (0.3, 0.5, 1.2), (0.2, 1.3, 0.1), (0.45, 0.46, 0.05), (0.1, 0.9, 1.5)]:
    d = abs(J(u, s, e) - I_direct((u-s)/2, (u+s)/2, e)); mx = max(mx, d)
rep("max |J_closed - I_direct| on 6 parameter triples:", mp.nstr(mx, 5))
# 2. E<=Z, equality for s>=v
worst = -mp.inf; eqd = 0
for (v, s, e) in [(0.3, 0.1, 0.7), (0.3, 0.2, 0.05), (0.4, 0.39, 0.3), (0.3, 0.5, 0.4), (0.2, 1.3, 0.1), (0.1, 0.9, 1.5), (0.5, 0.7, 0.2)]:
    E = J(v, s, e) - 2*s*mp.log(mp.sin(e)); Z = Zf(v, s, e)
    worst = max(worst, E - Z)
    if s >= v: eqd = max(eqd, abs(E-Z))
rep("max (E-Z) over 7 samples (<=0 expected):", mp.nstr(worst, 6), "; max|E-Z| for s>=v (0 expected):", mp.nstr(eqd, 5))

I4 = mp.quad(lambda t: mp.sqrt(1-t**4), [0, 1])
kap = 4*I4/pi**2
rep("I4 =", mp.nstr(I4, 15), "< 319/360 =", mp.nstr(mp.mpf(319)/360, 15), "; kappa =", mp.nstr(kap, 15))

def phase(x, y):
    x, y = mp.mpf(x), mp.mpf(y)
    a = (mp.cos(x)+mp.cos(y))/2; p = mp.sin(x); q = mp.sin(y)
    return a, p, q

def Ec(x, y):
    a, p, q = phase(x, y); v = p/2; dl = q/2
    b = 2*mp.atan(dl/a)
    def integrand(e):
        s0 = a*mp.tan(e/2)
        return J(v, s0+dl, e) + J(v, abs(s0-dl), e) - 4*s0*mp.log(mp.sin(e))
    pts = [mp.mpf(0)]
    if 0 < b < pi/2: pts.append(b)
    pts.append(pi/2)
    return mp.quad(integrand, pts)/pi**2

def Bbeta(x, y):
    a, p, q = phase(x, y)
    if q == 0: return mp.mpf(0)
    b = 2*mp.atan(q/(2*a))
    return 4/pi**2*mp.quad(lambda e: (q/2-a*mp.tan(e/2))*(-mp.log(mp.sin(e))), [0, b])

def Lsin(b):
    return mp.quad(lambda e: -mp.log(mp.sin(e)), [0, b]) if b > 0 else mp.mpf(0)

# 3. grid on closed rho<=pi/2 incl. axes and the rho=pi/2 edge
N = 10
worst11 = (-mp.inf, None); worst10 = (-mp.inf, None); cnt = 0
for i in range(N+1):
    for j in range(N+1-i):
        x = (pi/2)*i/N; y = (pi/2)*j/N
        a, p, q = phase(x, y)
        ec = Ec(x, y); bb = Bbeta(x, y)
        rhs11 = kap*p**mp.mpf(1.5)/mp.sqrt(a) - bb
        s11 = ec - rhs11
        if s11 > worst11[0]: worst11 = (s11, (x, y))
        if x + y <= 1 + mp.mpf('1e-30'):
            b = 2*mp.atan(q/(2*a))
            rhs10 = kap*p**mp.mpf(1.5)/mp.sqrt(a) + q/pi**2*Lsin(b)
            s10 = ec - rhs10
            if s10 > worst10[0]: worst10 = (s10, (x, y))
        cnt += 1
rep("grid points (closed rho<=pi/2, N=10):", cnt)
rep("max [Ec - (kappa p^1.5/sqrt a - Bbeta)] (E11 (2), <=0 expected):", mp.nstr(worst11[0], 6), "at", [mp.nstr(z, 5) for z in worst11[1]])
rep("max [Ec - E10 (2) rhs] on rho<=1 subset (<=0 expected):", mp.nstr(worst10[0], 6), "at", [mp.nstr(z, 5) for z in worst10[1]])
# 4. x=0 identity Ec(0,y)=-Bbeta and y=0 axis limit
d0 = max(abs(Ec(0, y) + Bbeta(0, y)) for y in [mp.mpf('0.3'), mp.mpf(1), pi/2])
rep("max |Ec(0,y)+Bbeta(0,y)| at y=0.3,1,pi/2 (0 expected):", mp.nstr(d0, 5), "; Ec(0,pi/2) =", mp.nstr(Ec(0, pi/2), 10))
for x in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
    a, p, q = phase(x, 0)
    rep("axis ratio Ec(x,0)/[kappa p^1.5/sqrt a] at x=", mp.nstr(x, 3), ":", mp.nstr(Ec(x, 0)/(kap*p**mp.mpf(1.5)/mp.sqrt(a)), 10))
# 5. elementary forms E11 (3): Ec <= (3/8) x^1.5 - Bbeta (rho<=1/2), (5/12) x^1.5 - Bbeta (rho<=1); 5/4: 9/20
w = {}
for (R, cst) in [(mp.mpf(1)/2, mp.mpf(3)/8), (mp.mpf(1), mp.mpf(5)/12), (mp.mpf(5)/4, mp.mpf(9)/20)]:
    ww = -mp.inf
    for i in range(9):
        for j in range(9-i):
            x = R*i/8; y = R*j/8
            ww = max(ww, Ec(x, y) - (cst*x**mp.mpf(1.5) - Bbeta(x, y)))
    rep("rho<=", mp.nstr(R, 3), ": max [Ec - (", mp.nstr(cst, 4), "x^1.5 - Bbeta)] =", mp.nstr(ww, 6), "(<=0 expected)")
# 6. kernel K(k) <= 1/sqrt(2k) and F bound
def K(k):
    return mp.quad(lambda t: 1/(mp.sin(t)**2+k*k), [mp.acos(1-k), pi/2])
rep("K(k)*sqrt(2k) at k=0.01,0.3,0.9:", [mp.nstr(K(mp.mpf(k))*mp.sqrt(2*mp.mpf(k)), 6) for k in ['0.01', '0.3', '0.9']])
def Fdir(v, a):
    return mp.quad(lambda e: Zf(v, a*mp.tan(e/2), e), [0, pi/2])
for (v, a) in [(mp.mpf('0.25'), mp.mpf('0.9')), (mp.mpf('0.5'), mp.mpf('0.5'))]:
    rep("F(v,a) direct / bound 4sqrt2 I4 v^1.5/sqrt a at", (mp.nstr(v, 3), mp.nstr(a, 3)), ":", mp.nstr(Fdir(v, a)/(4*mp.sqrt(2)*I4*v**mp.mpf(1.5)/mp.sqrt(a)), 8))
