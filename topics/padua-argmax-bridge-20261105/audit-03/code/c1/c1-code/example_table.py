import sys, os
sys.path.insert(0, os.environ.get("PYLIB", ""))
import mpmath as mp
mp.mp.dps = 25
kappa = mp.mpf('0.9197101183884925351'); a = 2/mp.pi; d = mp.euler + mp.log(8/mp.pi)
Lc = {2: mp.mpf(3), 3: mp.mpf('3.7761423749154'), 10: mp.mpf('6.8771001625'), 50: mp.mpf('12.8669170532'), 200: mp.mpf('19.725381378')}
# n=2 hand terms of (8)
f = lambda u, v: (1 + mp.cos(v)) / abs(mp.cos(u) - mp.cos(v))
th = [0, mp.pi/2, mp.pi]; ph = [0, mp.pi/3, 2*mp.pi/3, mp.pi]
terms = [(j, k, e, mp.nstr(e * f(th[j], ph[k]), 6)) for (j, k, e) in [(0,1,0.5),(1,0,0.5),(1,2,1),(2,1,0.5)]]
print("n=2 weighted terms of (8):", terms)
for n, L in Lc.items():
    N = n + mp.mpf(1)/2
    approx = a**2*(mp.log(N)+d)**2 + kappa - 1/N
    print(n, mp.nstr(L, 10), mp.nstr(approx, 10), mp.nstr(L-approx, 4))
