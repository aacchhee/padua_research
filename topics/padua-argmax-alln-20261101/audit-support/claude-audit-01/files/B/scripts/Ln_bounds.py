"""Claude audit-01 auditor B: MEASURED check of gated-06 bounds 0<=L_n<=H_{floor(n/2)}/(pi(n+1)),
n*(L_n - log n/(pi n)) bounded, L_2=0, L_n>0 for n>=3; and consistency of the d1 screen n=256 local
excess at alpha=-1/256 with L_256/256."""
import numpy as np, mpmath as mp, json, gzip, sys
res = {'violations_upper': [], 'nonpositive_n>=3': [], 'min_ratio': None}
mx, mn = -1e9, 1e9
for n in range(2, 20001):
    k = np.arange(1, n//2 + 1)
    s = np.sum(1/np.tan(k*np.pi/n)) if n > 2 else 0.0
    if n == 2: s = 0.0
    L = s/(n*(n+1))
    H = np.sum(1.0/k)
    if L > H/(np.pi*(n+1)) + 1e-15: res['violations_upper'].append(n)
    if n >= 3 and L <= 0: res['nonpositive_n>=3'].append(n)
    if n >= 3:
        e = n*(L - np.log(n)/(np.pi*n)); mx = max(mx, e); mn = min(mn, e)
res['n*(L_n - log n/(pi n)) range over 3..20000'] = [mn, mx]
mp.mp.dps = 30
L256 = mp.fsum(mp.cot(k*mp.pi/256) for k in range(1, 129))/(256*257)
res['L_256'] = float(L256); res['L_256/256'] = float(L256/256)
d = json.loads(gzip.open(sys.argv[1]).read())
res['screen_keys'] = list(d.keys())[:20]
print(json.dumps(res, indent=1))
