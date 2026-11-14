import numpy as np
from scipy.integrate import quad
PI=np.pi
def r(w):
    return 1/np.tan(w)-1/w if w<PI/2 else -1/w
def R(w):  # primitive of r: log sin w - log w on (0,pi/2], then -log w + const
    return np.log(np.sin(w))-np.log(w) if w<=PI/2 else -np.log(w)
rng=np.random.default_rng(3)
worst=0
for _ in range(30):
    n=int(rng.integers(32,400)); hs=PI/n; v=rng.uniform(0.01,1.4); t=rng.uniform(0,1)
    N=200000
    k=np.arange(N)
    samp=np.array([r(v+hs*(kk+t)) for kk in k[:5000]])
    ints=np.array([(R(v+(kk+1)*hs)-R(v+kk*hs))/hs for kk in k[:5000]])
    E=(samp-ints).sum()
    # remaining cells all beyond pi/2 if v+5000h>pi/2 : r=-1/w exact sum via asymptotics
    w0=v+5000*hs
    assert w0>PI/2
    # sum_{k>=0} [-1/(w0+h(k+t)) + (1/h)log((w0+h(k+1))/(w0+hk))]
    # = (1/h)[ -sum 1/(k+t+w0/h) + sum log((k+1+c)/(k+c)) ], c=w0/h -> (1/h)[psi(c+t) - log c] (matched limit)
    from scipy.special import digamma
    c=w0/hs
    E+= (digamma(c+t)-np.log(c))/hs*(-1)*(-1)  # check sign below
    val=(0.5-t)*r(v)
    worst=max(worst,abs(E-val)/(5*hs/24)); print(f"n={n} v={v:.3f} t={t:.3f} E={E:.6f} (1/2-t)r(v)={val:.6f} ratio={abs(E-val)/(5*hs/24):.3f}")

print("max ratio |E-(1/2-t)r(v)|/(5h/24) =",worst)
