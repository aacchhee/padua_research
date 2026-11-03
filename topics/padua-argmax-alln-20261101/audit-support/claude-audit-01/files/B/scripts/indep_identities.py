"""Claude audit-01 auditor B: independent high-precision identity checks.
Own implementation: Padua Lagrange cardinals via a Chebyshev Vandermonde solve (no repo code).
Checks: lambda (Lagrange) == four-reflection formula; S == periodic odd-board primitive S_n(alpha,beta);
Delta>=Qv,Qh>=0; Qv/Qh periodic formula (B) of gated-01; codex-04 vertical lambda=S(s)-Delta;
codex-05 horizontal lambda=S^h(s)-Delta^h; numerator identity (1) of gated-02 cleared;
collision family identity (13) of gated-03.  MEASURED (mpmath, 50 digits)."""
import mpmath as mp, random, json, sys, itertools
mp.mp.dps = 50
pi = mp.pi
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 7)

def T(k, x):  # Chebyshev via cos(k acos x) is fine for |x|<=1; use recurrence for robustness
    a, b = mp.mpf(1), x
    if k == 0: return a
    for _ in range(k-1): a, b = b, 2*x*b - a
    return b

def Dfour(n, u, v):  # PD-T185 (5): finite rhombus Fourier sum
    s = mp.mpf(0)
    cu = [mp.cos(p*u) for p in range(n+1)]; cv = [mp.cos(q*v) for q in range(n+1)]
    for p in range(n+1):
        for q in range(n+1-p):
            s += (1 if p == 0 else 2)*(1 if q == 0 else 2)*cu[p]*cv[q]
    return s

def Ddd(n, u, v):  # divided difference of P=T_{n+1}+T_n (only off-diagonal)
    P = lambda z: T(n+1, z) + T(n, z)
    x, y = mp.cos(u), mp.cos(v)
    return (P(y) - P(x))/(y - x)

def G(n, u, v):
    return Dfour(n, u, v) - mp.cos(n*u)

def nodes(n):
    m = n+1
    out = []
    for j in range(n+1):
        for k in range(m+1):
            if (j+k) % 2 == 0:
                e = mp.mpf(1)/2 if j in (0, n) else mp.mpf(1)
                f = mp.mpf(1)/2 if k in (0, m) else mp.mpf(1)
                out.append((j, k, e, f))
    return out

def lagrange_lebesgue(n, x, y, cache={}):
    m = n+1
    if n not in cache:
        nd = nodes(n)
        basis = [(p, q) for p in range(n+1) for q in range(n+1-p)]
        assert len(nd) == len(basis) == (n+1)*(n+2)//2
        V = mp.matrix(len(nd), len(basis))
        for i, (j, k, _, _) in enumerate(nd):
            X, Y = mp.cos(j*pi/n), mp.cos(k*pi/m)
            for c, (p, q) in enumerate(basis):
                V[i, c] = T(p, X)*T(q, Y)
        cache[n] = (nd, basis, V)
    nd, basis, V = cache[n]
    bz = mp.matrix([T(p, x)*T(q, y) for (p, q) in basis])
    ell = mp.lu_solve(V.T, bz)
    return sum(abs(ell[i]) for i in range(len(nd))), ell

def fourcopy(n, th, ph):
    m = n+1
    lam = S = Qv = Qh = mp.mpf(0)
    for (j, k, e, f) in nodes(n):
        w = 2*e*f/(n*m)
        a, b = j*pi/n, k*pi/m
        g = {(s, t): G(n, th + s*a, ph + t*b) for s in (1, -1) for t in (1, -1)}
        lam += w*abs(sum(g.values()))/4
        A = sum(abs(z) for z in g.values())
        S += w*A/4
        Qv += w*sum(abs(g[(s, 1)]) + abs(g[(s, -1)]) - abs(g[(s, 1)] + g[(s, -1)]) for s in (1, -1))/4
        Qh += w*sum(abs(g[(1, t)]) + abs(g[(-1, t)]) - abs(g[(1, t)] + g[(-1, t)]) for t in (1, -1))/4
    return lam, S, Qv, Qh

def primitive(n, al, be):  # gated-02 S_n(alpha,beta), periodic odd board
    m = n+1; N = n*m
    s = mp.mpf(0)
    for j in range(2*n):
        for r in range(2*m):
            if (j+r) % 2 == 1:
                s += abs(G(n, j*pi/n + al/n, r*pi/m + be/m))/2
    return s/N

def Qv_formulaB(n, J, al, ph):  # gated-01 (B)
    m = n+1
    tot = mp.mpf(0)
    for k in range(m+1):
        f = mp.mpf(1)/2 if k in (0, m) else mp.mpf(1)
        b = k*pi/m
        for j in range(2*n):
            if (j+k) % 2 != J % 2: continue
            u = j*pi/n + al/n
            Hp = (-1)**j*G(n, u, ph + b)/2; Hm = (-1)**j*G(n, u, ph - b)/2
            tot += f*(abs(Hp) + abs(Hm) - abs(Hp + Hm))
    return tot/(n*m)

def odd_rep(n, th, ph):
    m = n+1
    best = None
    for J in range(n+1):
        for K in range(m+1):
            if (J+K) % 2 == 1:
                al = n*th - J*pi; be = m*ph - K*pi
                d = abs(al) + abs(be)
                if best is None or d < best[0]: best = (d, J, K, al, be)
    return best

res = {'lambda_vs_fourcopy': 0, 'S_vs_primitive': 0, 'QvB': 0, 'neg_Q': 0, 'cases': 0, 'maxdiamond': 0,
       'Dfour_vs_dd': 0, 'vertical': 0, 'horizontal': 0, 'numerator': 0, 'collision13': 0}
for n in [2, 3, 4, 5, 6, 7, 8, 9]:
    m = n+1
    for trial in range(4):
        th = mp.mpf(random.random())*pi; ph = mp.mpf(random.random())*pi
        if trial == 3:  # a point within tiny phase of an odd coset, near the (pi,pi) corner region
            th = pi - pi/n + mp.mpf('1e-3')/n; ph = pi - mp.mpf('2e-3')/m
        lamL, _ = lagrange_lebesgue(n, mp.cos(th), mp.cos(ph))
        lam, S, Qv, Qh = fourcopy(n, th, ph)
        d, J, K, al, be = odd_rep(n, th, ph)
        res['maxdiamond'] = max(res['maxdiamond'], float(d/pi))
        Sp = primitive(n, al, be)
        res['lambda_vs_fourcopy'] = max(res['lambda_vs_fourcopy'], float(abs(lamL - lam)))
        res['S_vs_primitive'] = max(res['S_vs_primitive'], float(abs(S - Sp)))
        res['QvB'] = max(res['QvB'], float(abs(Qv - Qv_formulaB(n, J, al, ph))))
        Delta = S - lam
        if not (Delta >= Qv - mp.mpf('1e-40') and Delta >= Qh - mp.mpf('1e-40') and Qv >= -1e-40 and Qh >= -1e-40):
            res['neg_Q'] += 1
        res['cases'] += 1
    # Fourier sum vs divided difference at random off-diagonal angles
    for _ in range(5):
        u, v = mp.mpf(random.random())*7, mp.mpf(random.random())*7
        res['Dfour_vs_dd'] = max(res['Dfour_vs_dd'], float(abs(Dfour(n, u, v) - Ddd(n, u, v))))
    # codex-04 vertical: edge x=eps, complementary beta=q pi/m, eps^n(-1)^q=-1, t=beta+s/m
    for eps in (1, -1):
        for q in range(1, m):
            if (eps**n)*(-1)**q != -1: continue
            s = mp.mpf(random.uniform(-3, 3))
            t = q*pi/m + s/m
            if not (0 <= t <= pi): continue
            lamL, _ = lagrange_lebesgue(n, mp.mpf(eps), mp.cos(t))
            # PD-T189 S_n(s)
            N = n*m; Ss = mp.mpf(0)
            for j in range(2*n):
                for r in range(2*m):
                    if (j+r) % 2: Ss += abs(((-1)**j*Dfour(n, j*pi/n, r*pi/m + s/m) - 1)/2)
            Ss /= N
            Dl = mp.mpf(0)
            for (j, k, e, f) in nodes(n):
                w = 2*e*f/(n*m)
                uj = j*pi/n if eps == 1 else pi - j*pi/n
                tau = (eps**n)*(-1)**j
                Hp = (tau*Dfour(n, uj, t + k*pi/m) - 1)/2; Hm = (tau*Dfour(n, uj, t - k*pi/m) - 1)/2
                Dl += w*(abs(Hp) + abs(Hm) - abs(Hp + Hm))
            res['vertical'] = max(res['vertical'], float(abs(lamL - (Ss - Dl))))
            # also PD-T189 S_n(s) equals gated-02 S_n(0,s)
            res['vertical'] = max(res['vertical'], float(abs(Ss - primitive(n, 0, s))))
            break
    # codex-05 horizontal: y=eps=(-1)^l, alpha0=q pi/n with q+m l odd, theta=alpha0+s/n
    for l in (0, 1):
        eps = (-1)**l
        for q in range(1, n):
            if (q + m*l) % 2 != 1: continue
            s = mp.mpf(random.uniform(-3, 3)); th = q*pi/n + s/n
            if not (0 <= th <= pi): continue
            lamL, _ = lagrange_lebesgue(n, mp.cos(th), mp.mpf(eps))
            N = n*m; Sh = mp.mpf(0)
            for j in range(2*n):
                for r in range(2*m):
                    if (j+r) % 2: Sh += abs(((-1)**r*Dfour(n, j*pi/n + s/n, r*pi/m) + mp.cos(s))/2)
            Sh /= N
            Dh = mp.mpf(0)
            for (j, k, e, f) in nodes(n):
                w = 2*e*f/(n*m)
                bp = mp.acos(eps*mp.cos(k*pi/m)); kap = (-1)**(k + m*l)
                Hp = (kap*Dfour(n, th + j*pi/n, bp) + mp.cos(s))/2; Hm = (kap*Dfour(n, th - j*pi/n, bp) + mp.cos(s))/2
                Dh += w*(abs(Hp) + abs(Hm) - abs(Hp + Hm))
            res['horizontal'] = max(res['horizontal'], float(abs(lamL - (Sh - Dh))))
            break
    # gated-02 (1) cleared numerator identity at random shifted odd lattice points
    for _ in range(6):
        j = random.randrange(2*n); r = random.randrange(2*m)
        if (j+r) % 2 == 0: r = (r+1) % (2*m)
        al, be = mp.mpf(random.uniform(-3, 3)), mp.mpf(random.uniform(-3, 3))
        u, v = j*pi/n + al/n, r*pi/m + be/m
        lhs = (-1)**j*G(n, u, v)*(mp.cos(u) - mp.cos(v))
        rhs = (mp.cos(al) + mp.cos(be))*(1 + mp.cos(v)) - mp.sin(al)*mp.sin(u) + mp.sin(be)*mp.sin(v)
        res['numerator'] = max(res['numerator'], float(abs(lhs - rhs)))
    # gated-03 (13): r=j+1, h=n-j<=n/3, D(u,v)=(-1)^n{V(X)U_m(T)+U_n(X)V(T)}
    def U(k, z):
        return sum(mp.cos(i*z) for i in range(1-k, k, 2))
    def Vn(z):
        return mp.cos((2*n+1)*z/2)/mp.cos(z/2)
    for h in range(0, n//3 + 1):
        for (al, be) in ((0, 0), (mp.mpf('0.03'), mp.mpf('-0.02')), (mp.mpf('-0.05'), mp.mpf('0.04'))):
            j = n - h; r = j + 1
            u, v = j*pi/n + al/n, r*pi/m + be/m
            x, y = (h*pi - al)/n, (h*pi - be)/m
            X, Tt = (x + y)/2, (x - y)/2
            rhs = (-1)**n*(Vn(X)*U(m, Tt) + U(n, X)*Vn(Tt))
            res['collision13'] = max(res['collision13'], float(abs(Dfour(n, u, v) - rhs)))
print(json.dumps(res, indent=1))
