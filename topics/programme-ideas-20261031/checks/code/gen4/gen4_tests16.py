import numpy as np, time
t=time.time()
# L1 norm over T^2 of the rhombus Dirichlet kernel D_n = sum_{|j|+|k|<=n} e^{i(j th + k ph)}, and the 1D Dirichlet constant; also the Chebyshev-projection norm on the square via even part (cosine) kernel: P_n f = sum_{i+j<=n} c_ij T_i T_j -> kernel on [0,pi]^2: K(th,ph;th',ph') = sum_{i+j<=n} eps_i eps_j cos(i th)cos(i th') cos(j ph) cos(j ph'); its sup over (th,ph) of L1 norm = Lebesgue constant of the Chebyshev projection on the square.
def dirichlet_rhombus_L1(n, M=None):
    M = M or 8*n+9
    th=(np.arange(M)+0.5)*2*np.pi/M; 
    J=np.arange(-n,n+1)
    E=np.exp(1j*np.outer(th,J))  # M x (2n+1)
    # D(th,ph)=sum_j e^{ij th} sum_{|k|<=n-|j|} e^{ik ph} = sum_j e^{ij th} D_{n-|j|}(ph)
    # build matrix over ph: Dk(ph) for k=0..n
    ph=th
    Dk=np.array([np.sum(np.cos(np.outer(ph,np.arange(1,k+1))),axis=1)*2+1 if k>0 else np.ones(M) for k in range(n+1)])  # (n+1) x M
    D = E @ Dk[np.abs(J)]   # M x M (th x ph)
    return np.mean(np.abs(D))
def dirichlet_1d(n,M=None):
    M=M or 8*n+9; th=(np.arange(M)+0.5)*2*np.pi/M
    return np.mean(np.abs(1+2*np.sum(np.cos(np.outer(th,np.arange(1,n+1))),axis=1)))
for n in (10,20,40,80,160):
    L2=dirichlet_rhombus_L1(n); L1=dirichlet_1d(n)
    print('n',n,'||D_n rhombus||_1 = %.4f'%L2, ' (4/pi^2 log n)^2*? ratio L2/log^2 n = %.4f'%(L2/np.log(n)**2), ' 1D ||D_n||_1 = %.4f, /log n = %.4f (4/pi^2=%.4f)'%(L1,L1/np.log(n),4/np.pi**2), ' L2/L1^2 = %.4f'%(L2/L1**2), 'time %.0f'%(time.time()-t))
