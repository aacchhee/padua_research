"""Claude audit-01 auditor B: independent high-precision identity checks.
Own implementation: Padua Lagrange cardinals via a Chebyshev Vandermonde solve (no repo code).
Checks: lambda (Lagrange) == four-reflection formula; S == periodic odd-board primitive S_n(alpha,beta);
Delta>=Qv,Qh>=0; Qv/Qh periodic formula (B) of gated-01; codex-04 vertical lambda=S(s)-Delta;
codex-05 horizontal lambda=S^h(s)-Delta^h; numerator identity (1) of gated-02 cleared;
collision family identity (13) of gated-03.  MEASURED (mpmath, 50 digits)."""
import mpmath as mp, random, json, sys, itertools
mp.mp.dps = 60
pi = mp.pi
random.seed(7)

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

