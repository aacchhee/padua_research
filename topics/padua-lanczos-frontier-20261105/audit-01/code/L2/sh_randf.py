import sys, json, numpy as np
sys.path.insert(0,'.')
from sh_own import family, build, dual, closure_deriv, U
rng=np.random.default_rng(12345)
for n in (2,3,4,5):
    X,Y,W,S,T,one,m=family(n,'f64'); M=len(X)
    cols,par,idx,b,d,al,tau2,ip=build(n,X,Y,W,n+1)
    N=lambda s:(s+1)*(s+2)//2
    h=idx[(n,0)]; p=par[h][1]
    frep=rng.standard_normal(M)                 # arbitrary represented vector f
    sw=np.sqrt(W)
    Fval=np.sqrt(d[p])*frep/sw                  # monic value-space forcing F=sqrt(d_p) f
    worst=0
    for rule in ('cgs','fixed'):
        db=dual(b,d,par,al,ip,{h:Fval},rule,N(n))
        rep,Pt=closure_deriv(b,db,W,X,N(n-1),N(n))
        Rn=np.eye(M)-sw[:,None]*Pt/sw[None,:]   # rep-space normal projector
        Rf=Rn@frep
        for k,(t,j) in enumerate(cols[:N(n-1)]):
            qk=sw*b[k]/np.sqrt(d[k]); Dk=rep@qk
            want=-((-2.0)**j)*Rf if t==n-1 else 0*Rf
            worst=max(worst,np.max(np.abs(Dk-want))/np.linalg.norm(Rf))
        fro=np.sum(rep**2); 
        worst=max(worst,abs(fro-(4.0**n-1)/3*np.dot(Rf,Rf))/fro)
    print(json.dumps({'n':n,'arbitrary_f_column_formula_and_fro_max_rel_err':float(worst)}))
