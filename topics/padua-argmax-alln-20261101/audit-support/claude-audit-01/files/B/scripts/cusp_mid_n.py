"""MEASURED mpmath (30 digits): slope of S_n(alpha,0) at n=31,32,64 vs exact L_n, using U-product with
U_k given by the finite Fourier sum (no removable-quotient tolerance)."""
import mpmath as mp, json
mp.mp.dps = 30
def Ufs(k, z):
    c = mp.cos(2*z); s1 = mp.cos(z)
    # sum_{i} cos((k-1-2i) z) via direct sum
    return mp.fsum(mp.cos((k-1-2*i)*z) for i in range(k))
def S(n, al):
    m = n+1; tot = []
    for j in range(2*n):
        for r in range(2*m):
            if (j+r) % 2:
                u = j*mp.pi/n + al/n; v = r*mp.pi/m
                P, T = (u+v)/2, (v-u)/2
                D = Ufs(m, P)*Ufs(m, T) + Ufs(n, P)*Ufs(n, T)
                tot.append(abs(D - mp.cos(n*u)))
    return mp.fsum(tot)/(2*n*m)
out = []
for n in (31, 32, 64):
    L = mp.fsum(mp.cot(k*mp.pi/n) for k in range(1, n//2+1))/(n*(n+1))
    Lc = S(n, 0); a = mp.mpf('1e-12')
    out.append({'n': n, 'L_n': mp.nstr(L, 18), 'slope+': mp.nstr((S(n, a)-Lc)/a, 18), 'slope-': mp.nstr((S(n, -a)-Lc)/a, 18), 'Lc': mp.nstr(Lc, 18)})
    print(out[-1], flush=True)
