import numpy as np, carrier, g1x
from scipy.special import roots_legendre
from math import log
def l2(f, N):
    xg, wg = roots_legendre(N); return float(np.sum(wg*f(np.arccos(xg))**2))
carrier.l2 = l2
AJm, AJp = 3.75098821137025988438, 2.17372444063582269455
ms = [200, 201, 400, 401, 800, 801, 1600, 1601, 3200, 3201]
rows = {}
for m in ms:
    W = carrier.g1.weights_dct(m)
    out = []
    for (a,b,sg) in [(0.25,0.2,-1),(0.25,0.24,-1),(0.125,0.2,1),(0.125,0.24,1)]:
        Q, n2, nX, nY = carrier.carrier_quot(m,a,b,sg,W)
        out.append((a,b,sg,Q,n2))
        print(m, 'a=%.3f b=%.2f sign=%+d  Q/log m=%.5f (lim %.5f)  norm2=%.5f  R/log m=%.5f (packet lim %.5f)' % (
            a,b,sg,Q/log(m), sg*(16 if sg<0 else 8)*a*b/9, n2, Q/n2/log(m), sg*(16 if sg<0 else 8)*a*b/9/(AJm if sg<0 else AJp)), flush=True)
    rows[m]=out
import json; json.dump({str(k):v for k,v in rows.items()}, open('quot.json','w'))
