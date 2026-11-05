#!/usr/bin/env python3
"""Claude audit third path (MEASURED, float64 + exact norm by Python Fractions).
Written from definitions.md only; imports no topic code and no FLINT.
1. builds Padua weights from the PD-T106 kernel formula in float64 and checks
   the defining moment equations sum w T_a(x)T_b(y) = h_a h_b, a+b<=m;
2. evaluates Q_m(p^2) for the dyadic witness in float64;
3. computes the exact continuous norm N with fractions.Fraction and compares it
   with the producer's exact-norm.txt."""
import sys, gzip, json, math, time
from fractions import Fraction
import numpy as np
wpath, normpath = sys.argv[1], sys.argv[2]
t0 = time.time()
raw = json.loads(gzip.decompress(open(wpath, 'rb').read()))
m, n, bits = raw['m'], raw['n'], raw['bits']
Cint = raw['coefficients']
S = 1 << bits
# exact norm
N = Fraction(0)
for a in range(n+1):
    row = 0; den = 1
    acc = Fraction(0)
    for b in range(n+1-a):
        c = Cint[a*(n+1)+b]
        if c: acc += Fraction(c*c, 2*b+1)
    N += acc / (2*a+1)
N = N*4/(S*S)
prod = Fraction(open(normpath).read().strip())
t1 = time.time()
# weights
th = np.pi*np.arange(m+1)/m; ph = np.pi*np.arange(m+2)/(m+1)
r = np.arange(m+1)
h = np.where(r % 2 == 0, 2/(1-r.astype(float)**2), 0.0)
c = np.where(r == 0, 1.0, 2.0)
D = np.outer(c*h, c*h) * (r[:, None]+r[None, :] <= m)
D[m, 0] /= 2
Tx = np.cos(np.outer(th, r)); Ty = np.cos(np.outer(ph, r))
K = Tx @ D @ Ty.T
e = lambda L: np.where((np.arange(L) == 0) | (np.arange(L) == L-1), 0.5, 1.0)
W = (2/(m*(m+1))) * np.outer(e(m+1), e(m+2)) * K
W[(np.arange(m+1)[:, None]+np.arange(m+2)[None, :]) % 2 == 1] = 0
M = Tx.T @ W @ Ty
target = np.outer(h, h) * (r[:, None]+r[None, :] <= m)
mask = r[:, None]+r[None, :] <= m
moment_err = np.abs(M-target)[mask].max()
# polynomial
C = np.array(Cint, dtype=float).reshape(n+1, n+1)/S
Lx = np.polynomial.legendre.legvander(np.cos(th), n)
Ly = np.polynomial.legendre.legvander(np.cos(ph), n)
P = Lx @ C @ Ly.T
q = float(np.sum(W*P*P))
out = dict(m=m, n=n, witness=wpath, exact_norm_equal_producer=(N == prod),
           norm_float=float(N), sum_w=float(W.sum()), max_moment_error=float(moment_err),
           q_float=q, rayleigh_float=q/float(N), sum_abs_wp2=float(np.sum(np.abs(W)*P*P)),
           seconds_norm=t1-t0, seconds_total=time.time()-t0, numpy=np.__version__)
print(json.dumps(out))
