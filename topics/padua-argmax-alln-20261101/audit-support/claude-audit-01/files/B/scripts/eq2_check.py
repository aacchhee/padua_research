"""Check gated-02/03 eq (2): periodic odd-board S_n(alpha,beta) equals the endpoint-weighted physical odd-mesh
four-reflection sum; also S even in each phase separately; also the zero-row exact formula
F_{j,m}(alpha,0) = -(sin alpha/2) tan(u/2), u=j pi/n+alpha/n."""
import sys, random, mpmath as mp
sys.path.insert(0, sys.argv[1])
from indep_identities_lib import primitive, G
mp.mp.dps = 50; pi = mp.pi; random.seed(9)
w = w2 = w3 = 0
for n in range(2, 10):
    m = n+1; N = n*m
    for _ in range(3):
        al, be = mp.mpf(random.uniform(-2, 2)), mp.mpf(random.uniform(-1, 1))
        tot = mp.mpf(0)
        for j in range(n+1):
            for r in range(m+1):
                if (j+r) % 2 == 0: continue
                e = mp.mpf(1)/2 if j in (0, n) else mp.mpf(1); f = mp.mpf(1)/2 if r in (0, m) else mp.mpf(1)
                for s in (1, -1):
                    for t in (1, -1):
                        tot += e*f*abs((-1)**j*G(n, j*pi/n + s*al/n, r*pi/m + t*be/m)/2)
        P = primitive(n, al, be)
        w = max(w, abs(tot/N - P))
        w2 = max(w2, abs(P - primitive(n, -al, be)), abs(P - primitive(n, al, -be)))
    for j in range(n):
        if (j + n) % 2: continue
        al = mp.mpf(random.uniform(-0.5, 0.5)); u = j*pi/n + al/n
        Fz = (-1)**j*G(n, u, pi)/2
        w3 = max(w3, abs(Fz + mp.sin(al)/2*mp.tan(u/2)))
print('eq(2) max err', mp.nstr(w, 3), '; evenness max err', mp.nstr(w2, 3), '; zero-row exact formula max err', mp.nstr(w3, 3))
