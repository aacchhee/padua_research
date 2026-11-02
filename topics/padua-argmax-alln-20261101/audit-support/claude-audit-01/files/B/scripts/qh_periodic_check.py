"""High-precision check: horizontal projected defect Qh equals (nm)^-1 sum_j e_j sum_{r in [0,2m), j+r=K mod 2} d^H,
with d^H the triangle defect of G(theta+-a_j, r pi/m+beta/m)/2 (normalization used implicitly by gated-05)."""
import sys, random, mpmath as mp
sys.path.insert(0, sys.argv[1])
from indep_identities_lib import fourcopy, odd_rep, G
mp.mp.dps = 50; pi = mp.pi; random.seed(3)
worst = 0
for n in range(2, 9):
    m = n+1
    for _ in range(3):
        th = mp.mpf(random.random())*pi; ph = mp.mpf(random.random())*pi
        lam, S, Qv, Qh = fourcopy(n, th, ph)
        d, J, K, al, be = odd_rep(n, th, ph)
        tot = mp.mpf(0)
        for j in range(n+1):
            e = mp.mpf(1)/2 if j in (0, n) else mp.mpf(1)
            for r in range(2*m):
                if (j + r) % 2 != K % 2: continue
                v = r*pi/m + be/m
                Hp = G(n, th + j*pi/n, v)/2; Hm = G(n, th - j*pi/n, v)/2
                tot += e*(abs(Hp) + abs(Hm) - abs(Hp + Hm))
        worst = max(worst, abs(tot/(n*m) - Qh))
print('max |Qh_periodic - Qh_fourcopy| =', mp.nstr(worst, 5))
