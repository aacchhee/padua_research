import sys, numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mz_padua_cc_check import padua_leb_eta, leg_hat
from numpy.polynomial import legendre as L
import numpy.polynomial.chebyshev as C
def cc_w(N):
    # Waldvogel-style weights via DCT formula
    k = np.arange(N+1); th = k*np.pi/N
    w = np.zeros(N+1)
    for j in range(N+1):
        s = 0.0
        for m in range(0, N//2+1):
            b = 1.0 if (m==0 or 2*m==N) else 2.0
            s += b/(1-4*m*m)*np.cos(2*m*th[j])
        c = 1.0 if j in (0,N) else 2.0
        w[j] = c*s/N
    return np.cos(th), w
def legmat(x, n):
    # stable 3-term recurrence orthonormal Legendre
    P = np.zeros((len(x), n+1)); P[:,0]=1/np.sqrt(2)
    if n>=1: P[:,1]=np.sqrt(3/2)*x
    for k in range(1,n):
        a = np.sqrt((2*k+1)*(2*k+3))/(k+1); b = k/(k+1)*np.sqrt((2*k+3)/(2*k-1))
        P[:,k+1] = a*x*P[:,k] - b*P[:,k-1]
    return P
for N in (40, 80, 160, 320, 640, 1280, 2560):
    x, w = cc_w(N)
    out=[]
    for n in (N-3, N-2, N-1, N):
        B = legmat(x, n); G = B.T@(w[:,None]*B)
        ev = np.linalg.eigvalsh(G)
        out.append(f"n=N-{N-n}: eta={max(abs(1-ev[0]),abs(ev[-1]-1)):.4f} [lmin={ev[0]:.4f}, lmax={ev[-1]:.4f}]")
    print(N, " | ".join(out), flush=True)
for m in (40, 50):
    e,c,neg = padua_leb_eta(m, m-1); print("Padua Leb m=",m," n=m-1 eta=",round(e,4)," cond=",round(c,2), flush=True)
