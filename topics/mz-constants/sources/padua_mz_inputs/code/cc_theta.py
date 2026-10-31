import numpy as np
exec(open(__import__("os").path.join(__import__("os").path.dirname(__file__),"cc_asym.py")).read().split("for N in (40")[0])
for N in (80, 320, 1280, 2560):
    x, w = cc_w(N); out=[]
    for th in (0.6, 0.75, 0.9, 0.95):
        n = int(th*N); B = legmat(x, n); ev = np.linalg.eigvalsh(B.T@(w[:,None]*B))
        out.append(f"n={th}N: lmin={ev[0]:.4f} lmax={ev[-1]:.4f}")
    print(N, " | ".join(out), flush=True)
# which polynomial attains lmin at n=N-1? check concentration at endpoints
N=320; x,w=cc_w(N); B=legmat(x,N-1); G=B.T@(w[:,None]*B); ev,V=np.linalg.eigh(G)
c=V[:,0]; print("lmin eigvec: weight on top 5 degrees", np.round(np.abs(c[-5:])**2,3), "sum top10", round(float((c[-10:]**2).sum()),3))
