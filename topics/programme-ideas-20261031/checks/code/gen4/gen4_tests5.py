import numpy as np, sys
sys.path.insert(0,'.')
from gen4_tests import padua, cheb_basis
# Weighted-Fekete stationarity test: gradient of log|det V| w.r.t. node B equals grad ell_B(B).
# ell_B(x) = w_B [K_n(x,B) - T_n(x) T_n(x_B)] (defect in T_n(x), RES convention). Compute grad by finite differences of the explicit formula.
def lagrange_grad(n):
    P,w = padua(n); V,idx = cheb_basis(P[:,0],P[:,1],n)
    Tn = lambda x: np.cos(n*np.arccos(np.clip(x,-1,1)))
    h=1e-6; G=np.zeros((len(P),2))
    for d in range(2):
        Pp=P.copy(); Pp[:,d]+=h; Pm=P.copy(); Pm[:,d]-=h
        for (S,sgn) in ((Pp,1),(Pm,-1)):
            Vs,_=cheb_basis(S[:,0],S[:,1],n)
            # ell_B(S_B) for each B: diag of w*(Vs V^T - Tn(x_S) Tn(x_B))
            val = w*(np.sum(Vs*V,axis=1) - Tn(S[:,0])*Tn(P[:,0]))
            G[:,d]+= sgn*val/(2*h)
    return P,w,G
for n in (4,6,8,12):
    P,w,G = lagrange_grad(n)
    interior = (np.abs(P[:,0])<0.999999)&(np.abs(P[:,1])<0.999999)
    Gi=G[interior]; Pi=P[interior]
    # test separable gradient field: G_x = f(x) only? check variance of G_x across nodes sharing same x
    xs=np.unique(np.round(Pi[:,0],10)); 
    varx = max(np.ptp(Gi[Pi[:,0].round(10)==x,0]) for x in xs if np.sum(Pi[:,0].round(10)==x)>1) if len(xs)>0 else None
    ys=np.unique(np.round(Pi[:,1],10))
    vary = max(np.ptp(Gi[Pi[:,1].round(10)==y,1]) for y in ys if np.sum(Pi[:,1].round(10)==y)>1)
    # candidate: G_x/n = -d/dx log w, w=(1-x^2)^a => G_x/n = 2 a x/(1-x^2) -> a estimate
    ax = Gi[:,0]*(1-Pi[:,0]**2)/(2*n*Pi[:,0]+1e-300)
    ay = Gi[:,1]*(1-Pi[:,1]**2)/(2*n*Pi[:,1]+1e-300)
    print('n',n,'#interior',interior.sum(),'max|grad| interior %.3e'%np.abs(Gi).max(),'ptp of G_x across same-x nodes %.2e'%varx,'ptp G_y same-y %.2e'%vary)
    print('   alpha_x estimates (nodes with |x|>0.2):', np.round(ax[np.abs(Pi[:,0])>0.2],4)[:8], ' alpha_y:', np.round(ay[np.abs(Pi[:,1])>0.2],4)[:8])
    # also print G_x/n vs x for a few
    print('   sample (x, G_x/n):', np.round(np.c_[Pi[:6,0],Gi[:6,0]/n],4).tolist())
