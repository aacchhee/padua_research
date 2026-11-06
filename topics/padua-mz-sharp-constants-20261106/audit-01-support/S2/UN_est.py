import sys; sys.path.insert(0,'.'); import numpy as np
from residual import lam
for N in [10**4,10**6,10**8,4096**2*16]:
    T=Y=max(1,int(np.floor(N**(1/12)+1e-12))); Q=max(1,int(np.floor(np.sqrt(N))))
    best=None
    for alpha in [0.0,0.005,0.01,0.02,0.05,0.1,0.2,0.3,0.5]:
        l=lam(T,Y,alpha,min(Q,1500))  # float estimate of lam_max(B_Q) (Q capped for speed)
        A=1+Y**3/6+alpha*T**3/3
        u=max(0,l)+A/Q
        EM=T**2/N**2+8*T**3/(3*N)+2*T**2/np.sqrt(N); EK=8/N+2/np.sqrt(N)+2/N**2; EH=4*Y**3/(3*N)+Y**2/np.sqrt(N)
        U=1+alpha+u+alpha*EM+EK+EH
        if best is None or U<best[0]: best=(U,alpha,l,A/Q,EK+EH+alpha*EM)
    print(f"N={N:.3g} T=Y={T} Q={Q} U_N~{min(best[0],5/3):.4f} (alpha={best[1]}, lam(B_Q)={best[2]:.3e}, A/Q={best[3]:.2e}, E={best[4]:.2e}); L_N=1 (no admissible J with lambda_J-r_J>1)",flush=True)
