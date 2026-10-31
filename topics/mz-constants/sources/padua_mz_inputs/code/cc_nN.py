import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
"""lambda_min of CC Gram at n=N (full interpolation space) and at n=N-1, N-2, and theta*N, to compare growth."""
import numpy as np, sys
sys.argv=[sys.argv[0]]
from cc_mz_large import extremes
for N in (80, 320, 1280, 5120):
    out=[]
    for n in (N, N-1, N-2, N-4, N-16, int(0.95*N), int(0.9*N)):
        lo=min(extremes(N,n,p)[0] for p in (0,1)); out.append(f"n={n}:{lo:.4f}")
    print(N, " ".join(out), flush=True)
