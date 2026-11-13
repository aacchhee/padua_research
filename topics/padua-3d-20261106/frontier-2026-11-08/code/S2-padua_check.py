import numpy as np, itertools
# 2D Padua torus lift: rank-1 lattice t -> (n t, (n+1) t), t = 2 pi j / (2n(n+1)), j=0..2n(n+1)-1 (generating curve on torus)
for n in [6,10,16]:
    M = 2*n*(n+1)
    t = 2*np.pi*np.arange(M)/M
    X = np.stack([n*t, (n+1)*t],1)  # torus points (equal weights 1/M)
    w = np.full(M, 1.0/M)
    A = [k for k in itertools.product(range(-n,n+1),repeat=2) if abs(k[0])+abs(k[1])<=n-1]
    A = np.array(A)
    E = np.exp(1j*X@A.T)*np.sqrt(w)[:,None]
    G = E.conj().T@E
    err = np.abs(G-np.eye(len(A))).max()
    Pxx = w*len(A)
    print(n, "M",M,"|A|",len(A),"Gram err %.2e"%err, "max Pxx %.4f"%Pxx.max(), "sum(1-Pxx)", round((1-Pxx).sum(),6), "M-|A|", M-len(A))
    # check exactness on O_{2n-1}
    K = [k for k in itertools.product(range(-2*n,2*n+1),repeat=2) if 0<abs(k[0])+abs(k[1])<=2*n-1]
    mx = max(abs(np.exp(1j*X@np.array(k)).mean()) for k in K)
    print("   max |moment| on 0<|k|_1<=2n-1: %.2e"%mx)
