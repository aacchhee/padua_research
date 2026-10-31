"""Padua discriminant over R (float check of the closed form proved via discrete orthogonality):
   det V_mon(Pad_n in Dickson coordinates X=2x, Y=2y)^2 = 2^{(n^2+3n+6)/2} * (n(n+1))^{(n+1)(n+2)/2}
   equivalently det V_cheb(Pad_n)^2 = 2^{4+n-n^2-N} (n(n+1))^N,  N = (n+1)(n+2)/2.
Proof: V^T W V = D  =>  det(V)^2 = det D / det W, with det D = 2^{1-n-n^2}, det W = 2^{N-2n-3} (n(n+1))^{-N}
(2 corner points with e_j e_k = 1/4, 2n-1 edge points with 1/2), and V_cheb -> V_mon(2x,2y) is unitriangular
up to the factor 2^{[a>=1]+[b>=1]} per column.  Consequence: the reduction of Pad_n modulo a prime above p is
unisolvent iff p does not divide 2n(n+1).
Run: python3 -I discriminant_real.py"""
import numpy as np
from math import log
for n in range(1, 13):
    pts = [(2*np.cos(j*np.pi/n), 2*np.cos(k*np.pi/(n+1))) for j in range(n+1) for k in range(n+2) if (j+k) % 2 == 0]
    idx = [(a, d-a) for d in range(n+1) for a in range(d, -1, -1)]
    V = np.array([[x**a * y**b for a, b in idx] for x, y in pts])
    s, ld = np.linalg.slogdet(V)
    N = len(pts)
    pred = 0.5*(((n*n+3*n+6)/2)*log(2) + N*log(n*(n+1)))
    print(f"n={n:2d} N={N:3d} log|det| numeric {ld:12.6f}  closed form {pred:12.6f}  rel.diff {abs(ld-pred)/pred:.1e}")
