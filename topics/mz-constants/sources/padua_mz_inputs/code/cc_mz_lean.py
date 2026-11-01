"""Memory-lean version of cc_mz_large.py: only the binding parity at n=N-1 (N even -> odd part),
lambda_min only. Usage: python3 cc_mz_lean.py N"""
import sys, time, numpy as np
from scipy.linalg import eigh, toeplitz, hankel
def Ik(k):
    k = np.asarray(k, dtype=float); out = np.zeros_like(k); ev = (k % 2 == 0); out[ev] = 2.0/(1.0-k[ev]**2); return out
N = int(sys.argv[1]); n = N-1; par = n % 2
idx = np.arange(par, n+1, 2); m = len(idx)
# |i-j| = 2|a-b| ; i+j = 2(a+b)+2par
d = Ik(2*np.arange(m)); s = Ik(2*np.arange(2*m-1) + 2*par)
sq = np.where(2*np.arange(2*m-1)+2*par <= N, s, Ik(2*N - (2*np.arange(2*m-1)+2*par)))
t0 = time.time()
T = toeplitz(d); T += hankel(s[:m], s[m-1:]); T *= 0.5
Q = toeplitz(d); Q += hankel(sq[:m], sq[m-1:]); Q *= 0.5
lo = eigh(Q, T, eigvals_only=True, subset_by_index=[0,0], overwrite_a=True, overwrite_b=True, check_finite=False)[0]
print(f"N={N} n=N-1 parity={par}: lmin={lo:.6f} 1/lmin={1/lo:.4f} lnN={np.log(N):.4f} [{time.time()-t0:.0f}s]", flush=True)
