"""High-precision checks at boundary/corner/node points (both parities n=2..9): Lagrange lambda equals the
four-reflection formula; S equals the odd-board primitive at the diamond phase; Delta>=Qv,Qh>=0;
lambda=1 at nodes; nonnode corners have lambda=S(0,0)=Lambda_c and Delta=0; node corners lambda=1."""
import sys, random, mpmath as mp
sys.path.insert(0, sys.argv[1])
from indep_identities_lib import fourcopy, odd_rep, primitive, lagrange_lebesgue
mp.mp.dps = 50; pi = mp.pi; random.seed(5)
w1 = w2 = 0; bad = 0; info = []
for n in range(2, 10):
    m = n+1
    Lc = primitive(n, 0, 0)
    pts = [(0, mp.mpf(random.random())*pi), (pi, mp.mpf(random.random())*pi),
           (mp.mpf(random.random())*pi, 0), (mp.mpf(random.random())*pi, pi),
           (0, 0), (pi, 0), (0, pi), (pi, pi), (2*pi/n, 4*pi/m) if n >= 2 else (0, 0)]
    for (th, ph) in pts:
        lamL, _ = lagrange_lebesgue(n, mp.cos(th), mp.cos(ph))
        lam, S, Qv, Qh = fourcopy(n, th, ph)
        d, J, K, al, be = odd_rep(n, th, ph)
        Sp = primitive(n, al, be)
        w1 = max(w1, abs(lamL - lam)); w2 = max(w2, abs(S - Sp))
        if not (S - lam >= Qv - 1e-40 and S - lam >= Qh - 1e-40 and min(Qv, Qh) >= -1e-40): bad += 1
    # corners: which are nonnode (J+K odd)? (theta,phi)=(J pi/n... )
    for (Jc, Kc) in ((0, 0), (n, 0), (0, m), (n, m)):
        lamL, _ = lagrange_lebesgue(n, mp.cos(Jc*pi/n), mp.cos(Kc*pi/m))
        info.append((n, (Jc, Kc), 'nonnode' if (Jc+Kc) % 2 else 'node', mp.nstr(lamL - (Lc if (Jc+Kc) % 2 else 1), 3)))
print('max|lambda_Lagrange - fourcopy| =', mp.nstr(w1, 3), ' max|S - primitive| =', mp.nstr(w2, 3), ' Q-violations =', bad)
for row in info: print(row)
