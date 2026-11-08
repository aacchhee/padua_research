# Independent auditor check (Claude Opus 5.5): corner Lebesgue value of Padua
# interpolation from the DEFINITION (solve interpolation in Pi_n^2 at the
# nodes), versus the auditor's own derived exact row formula.
# Nodes: (cos(j pi/n), cos(k pi/(n+1))), 0<=j<=n, 0<=k<=n+1, j+k even.
import sys
import mpmath as mp

mp.mp.dps = 40

def nodes(n):
    return [(mp.cos(j*mp.pi/n), mp.cos(k*mp.pi/(n+1)))
            for j in range(n+1) for k in range(n+2) if (j+k) % 2 == 0]

def cheb(m, x):
    return mp.cos(m*mp.acos(x)) if abs(x) <= 1 else mp.chebyt(m, x)

def brute(n):
    P = nodes(n)
    basis = [(a, b) for a in range(n+1) for b in range(n+1-a)]
    assert len(P) == len(basis) == (n+1)*(n+2)//2
    # Chebyshev values via cos to stay exact on [-1,1]
    def phi(pt):
        x, y = pt
        tx = [mp.chebyt(m, x) for m in range(n+1)]
        ty = [mp.chebyt(m, y) for m in range(n+1)]
        return [tx[a]*ty[b] for (a, b) in basis]
    V = mp.matrix([phi(pt) for pt in P])          # rows: nodes
    rhs = mp.matrix(phi((mp.mpf(-1), mp.mpf(-1))))
    ell = mp.lu_solve(V.T, rhs)                    # sum_xi ell_xi phi_m(xi) = phi_m(c)
    return mp.fsum(abs(e) for e in ell)

def rowformula(n):
    """Auditor's derived formula:
    Lambda_c = 1/(n+1) + (2/(n(n+1))) [ (1/2) rho0 + sum_{k=1}^n (2 cot q_k S_k - n) ],
    p_j = pi j/(2n), q_k = pi k/(2n+2), mu_j = 1/2 at j in {0,n}, else 1,
    S_k = sum_{j<=k-1, j = k-1 mod 2} mu_j [cot(q+p_j)+cot(q-p_j)],
    rho0 = sum_{j odd} mu_j 2/sin^2 p_j."""
    pi = mp.pi
    mu = lambda j: mp.mpf(1)/2 if j in (0, n) else mp.mpf(1)
    rho0 = mp.fsum(mu(j)*2/mp.sin(pi*j/(2*n))**2 for j in range(1, n+1, 2))
    tot = rho0/2
    for k in range(1, n+1):
        q = pi*k/(2*n+2)
        S = mp.fsum(mu(j)*(mp.cot(q+pi*j/(2*n)) + mp.cot(q-pi*j/(2*n)))
                    for j in range(k-1, -1, -2))
        tot += 2*mp.cot(q)*S - n
    return mp.mpf(1)/(n+1) + 2*tot/(n*(n+1))

def direct_cardinal(n):
    """Auditor's derived closed cardinal value |L| = w * 2cos^2(v/2)/|cos^2(u/2)-cos^2(v/2)|
    on reflected indices j'+k' odd; exceptional node (n,n+1) gives 1/(n+1)."""
    pi = mp.pi
    s = mp.mpf(0)
    for jp in range(n+1):
        for kp in range(n+2):
            if (jp+kp) % 2 == 0:
                continue
            nb = (jp in (0, n)) + (kp in (0, n+1))
            w = mp.mpf(2)/(n*(n+1)) / 2**nb
            if (jp, kp) == (n, n+1):
                s += mp.mpf(1)/(n+1); continue
            A = mp.cos(pi*jp/(2*n))**2; B = mp.cos(pi*kp/(2*n+2))**2
            s += w*2*B/abs(A-B)
    return s

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    for n in range(2, nmax+1):
        b = brute(n); r = rowformula(n); d = direct_cardinal(n)
        print(n, mp.nstr(b, 30), mp.nstr(b-r, 3), mp.nstr(b-d, 3))
