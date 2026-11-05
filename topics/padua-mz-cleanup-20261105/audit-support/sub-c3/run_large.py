import numpy as np, carrier
from scipy.special import roots_legendre
from math import log
def l2(f, N):
    xg, wg = roots_legendre(N)
    return float(np.sum(wg*f(np.arccos(xg))**2))
carrier.l2 = l2
AJm, AJp = 3.75098821137025988438, 2.17372444063582269455
print('norm limits: A*Jm(1/4)=%.12f  A*Jp(1/8)=%.12f' % (AJm, AJp))
for m in [1000, 1001, 8000, 8001, 64000, 64001, 256000]:
    _, _, D, X, Y, _ = carrier.factors(m, 0.25, 0.2, -1)
    nm = l2(X, m+10)*l2(Y, m+10)
    _, _, D, X, Y, _ = carrier.factors(m, 0.125, 0.2, +1)
    npl = l2(X, m+10)*l2(Y, m+10)
    print(m, 'neg %.9f (diff %.2e)   pos %.9f (diff %.2e)' % (nm, nm-AJm, npl, npl-AJp))
