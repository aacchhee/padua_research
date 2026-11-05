import sys, numpy as np, importlib.util
from math import log, pi, floor
spec = importlib.util.spec_from_file_location('g1', '/home/user/padua_research/topics/padua-mz-cleanup-20261105/code/g1_spectral.py')
g1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(g1)

def fejer(r, t):
    # F_r(cos t) = 1 + 2 sum_{l=1}^r (1-l/(r+1)) cos(l t)  (exact cosine sum, vectorized via closed form w/ guard)
    t = np.asarray(t, float); L = r+1
    s = np.sin(t/2); out = np.empty_like(t)
    small = np.abs(s) < 1e-12
    out[~small] = (np.sin(L*t[~small]/2)/s[~small])**2/L
    out[small] = L
    return out
def factors(m, a, b, sign):
    r, s = floor(a*m), floor(b*m)
    D = m if m%2==0 else m+1           # carrier mesh denominator (even)
    if sign<0: carr = lambda t: np.cos(D*t/2)
    else:      carr = lambda t: np.sin(D*t/2)*np.sin(r*t)
    X = lambda t: carr(t)*fejer(r,t)   # carrier-coordinate factor
    Y = lambda t: fejer(s,t)           # other coordinate
    deg = D//2 + (2*r if sign>0 else r) + s
    return r, s, D, X, Y, deg
def l2(f, N):
    xg, wg = np.polynomial.legendre.leggauss(N)
    return float(np.sum(wg*f(np.arccos(xg))**2))
def carrier_quot(m, a, b, sign, W=None):
    r, s, D, X, Y, deg = factors(m, a, b, sign)
    assert deg <= m-1, (m, deg)
    if W is None: W = g1.weights_dct(m)
    tx = np.pi*np.arange(m+1)/m; ty = np.pi*np.arange(m+2)/(m+1)
    if m%2==0: px, py = X(tx), Y(ty)   # even: carrier in x
    else:      px, py = Y(tx), X(ty)   # odd: carrier in y
    Q = float(px**2 @ W @ py**2)
    N = m+10
    nX, nY = l2(X, N), l2(Y, N)
    return Q, nX*nY, nX, nY
if __name__ == '__main__':
    # reproduce independent-check norms (b=1/5)
    for m in [32,64,128,33,65,129]:
        print(m, 'neg a=1/4 norm2 %.15f' % carrier_quot(m,0.25,0.2,-1)[1], ' pos a=1/8 norm2 %.15f' % carrier_quot(m,0.125,0.2,+1)[1])
