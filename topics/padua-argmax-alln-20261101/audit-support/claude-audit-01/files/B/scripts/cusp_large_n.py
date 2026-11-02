"""MEASURED float64 (own kernel): slope of S_n(alpha,0) at larger n vs exact L_n; screen value at n=256."""
import numpy as np, json, math
def U(k, z):
    s = np.sin(z)
    with np.errstate(divide='ignore', invalid='ignore'):
        val = np.sin(k*z)/s
    return np.where(np.abs(s) < 1e-13, k*np.cos(k*z)/np.cos(z), val)
def S(n, al, be):
    m = n+1
    j, r = np.nonzero((np.arange(2*n)[:, None] + np.arange(2*m)[None, :]) % 2)
    u = j*np.pi/n + al/n; v = r*np.pi/m + be/m
    P, T = (u+v)/2, (v-u)/2
    D = U(m, P)*U(m, T) + U(n, P)*U(n, T)
    return math.fsum(np.abs(D - np.cos(n*u)).tolist())/(2*n*m)
out = []
for n in (31, 32, 101, 256, 512):
    k = np.arange(1, n//2+1); L = float(np.sum(1/np.tan(k*np.pi/n)))/(n*(n+1))
    Lc = S(n, 0, 0)
    a = 1e-7
    out.append({'n': n, 'L_n': L, 'slope_est': (S(n, a, 0) - Lc)/a, 'slope_est_neg': (S(n, -a, 0) - Lc)/a,
                'Lc': Lc})
out.append({'n=256 S(-1/256,0)-Lc': S(256, -1/256, 0) - S(256, 0, 0), 'screen_reported': 1.76177240e-05})
print(json.dumps(out, indent=1))
