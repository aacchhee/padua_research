#!/usr/bin/env python3
"""L2 auditor's own check of the SH_n closure statements (no repository code).
Value-space weighted formulation; first-principles dual-number derivative of
actual smooth exact-base rules, full projector product rule, rep-space norms.
backend 'mp' = numpy object arrays of mpmath mpf (dps 40), 'f64' = float64."""
import sys, json, time, itertools
import numpy as np
import mpmath as mp

def family(n, be):
    m=n+2
    if be=='mp':
        mp.mp.dps=40; pi=mp.pi; cos=mp.cos; sin=mp.sin; one=mp.mpf(1); cast=lambda a: np.array(a,dtype=object)
    else:
        pi=np.pi; cos=np.cos; sin=np.sin; one=1.0; cast=lambda a: np.array(a,dtype=float)
    th=[k*pi/(m+1) for k in range(1,m+1)]
    s=[cos(t) for t in th]; v=[2*sin(t)**2/(m+1) for t in th]
    X=[];Y=[];W=[];S=[];T=[]
    for k in range(m):
        for l in range(m):
            X.append(s[k]); Y.append(2*s[k]+s[l]); W.append(v[k]*v[l]); S.append(s[k]); T.append(s[l])
    return cast(X),cast(Y),cast(W),cast(S),cast(T),one,m

def U(r,z,one):
    a,b=0*z,0*z+one  # U_-1, U_0
    if r<0: return a
    for _ in range(r): a,b=b,2*z*b-a
    return b

def build(n,X,Y,W,deg):
    ip=lambda u,v: np.sum(W*u*v)
    cols=[];par=[];idx={}
    for t in range(deg+1):
        for j in range(t+1):
            idx[(t,j)]=len(cols); cols.append((t,j))
            if t==0: par.append(None)
            elif j==0: par.append((X,idx[(t-1,0)]))
            else: par.append((Y,idx[(t-1,j-1)]))
    b=[X*0+1]; d=[ip(b[0],b[0])]; al=[None]; tau2=[None]
    for k in range(1,len(cols)):
        A,p=par[k]; u=A*b[p]; a=[ip(bl,u)/dl for bl,dl in zip(b,d)]
        r=u.copy()
        for c,bl in zip(a,b): r=r-c*bl
        b.append(r); d.append(ip(r,r)); al.append(a); tau2.append(ip(u,u))
    return cols,par,idx,b,d,al,tau2,ip

def dual(b,d,par,al,ip,src,rule,K):
    """src: dict k->F_val (derivative forcing of the monic source eps*F at column k)."""
    db=[b[0]*0]
    for k in range(1,K):
        A,p=par[k]; u=A*b[p]; du=A*db[p]
        if k in src: du=du+src[k]
        v=du
        for l in range(k):
            if rule=='cgs':
                num=ip(b[l],u); dnum=ip(db[l],u)+ip(b[l],du); dden=2*ip(b[l],db[l])
                v=v-(dnum/d[l]-num*dden/d[l]**2)*b[l]-al[k][l]*db[l]
            else:
                v=v-al[k][l]*db[l]-((7*k+3*l)%11-5)/7.0*b[l] if not isinstance(b[0][0],mp.mpf) else v-al[k][l]*db[l]-mp.mpf((7*k+3*l)%11-5)/7*b[l]
        rho=((3*k)%7-3)/5.0 if not isinstance(b[0][0],mp.mpf) else mp.mpf((3*k)%7-3)/5
        if rule!='cgs': v=v+rho*b[k]
        db.append(v)
    return db

def proj_and_deriv(B,dB,W):
    # value-space weighted projector P=B G^-1 B^T Wt, G=B^T Wt B; product-rule derivative
    Wt=np.diag(W); G=B.T@Wt@B; dG=dB.T@Wt@B+B.T@Wt@dB
    Gi=np.diag([1/G[i,i] for i in range(G.shape[0])])  # baseline G diagonal (checked)
    P=B@Gi@B.T@Wt
    dP=dB@Gi@B.T@Wt+B@Gi@dB.T@Wt-B@Gi@dG@Gi@B.T@Wt
    return P,dP,G

def closure_deriv(b,db,W,X,ns,nt):
    Bs=np.array(b[:ns]).T; Bt=np.array(b[:nt]).T; dBs=np.array(db[:ns]).T; dBt=np.array(db[:nt]).T
    Ps,dPs,_=proj_and_deriv(Bs,dBs,W); Pt,dPt,_=proj_and_deriv(Bt,dBt,W)
    Xd=np.diag(X); I=np.diag(X*0+1)
    dOp=-dPt@Xd@Ps+(I-Pt)@Xd@dPs
    sw=np.array([mp.sqrt(w) if isinstance(w,mp.mpf) else np.sqrt(w) for w in W],dtype=object if isinstance(W[0],mp.mpf) else float)
    rep=(sw[:,None]*dOp)/sw[None,:]
    return rep,Pt

def fro2(A): return np.sum(A*A)

def run(n,be,full):
    t0=time.time()
    X,Y,W,S,T,one,m=family(n,be); M=len(X)
    cols,par,idx,b,d,al,tau2,ip=build(n,X,Y,W,n+1)
    N=lambda s:(s+1)*(s+2)//2
    Nn=N(n); H=Nn-1
    # checks of the family facts
    G=np.array([[ip(bi,bj) for bj in b] for bi in b])
    offd=max(abs(G[i,j]) for i in range(len(b)) for j in range(len(b)) if i!=j)
    h=idx[(n,0)]; p=par[h][1]
    sig2=tau2[h]/d[p]
    Xn2=max(x*x for x in X)
    e_val=U(n+1,S,one)                      # value-space of q_(n+1,0)/sqrt(w)
    # tensor-basis identification: q_rj = sqrt(w)U_r(s)U_j(t)  <=> b_k/sqrt(d_k) = U_r(S)U_j(T) in value space
    tens=max(max(abs(b[k][i]/ (d[k]**0.5 if be=='f64' else mp.sqrt(d[k])) - U(t-j,S,one)[i]*U(j,T,one)[i]) for i in range(M)) for k,(t,j) in enumerate(cols))
    info={'n':n,'backend':be,'M':M,'N_n':Nn,'H':H,'gram_offdiag_max':float(offd),'tensor_basis_maxdev':float(tens),
          'sigma2_h':float(sig2),'Xnorm2':float(Xn2),'Xnorm2_minus_cos2':float(Xn2-(mp.cos(mp.pi/(n+3))**2 if be=='mp' else np.cos(np.pi/(n+3))**2)),
          'e_norm2':float(np.sum(W*e_val*e_val)),'e_proj_on_Sn':float(max(abs(ip(e_val,b[k])) for k in range(Nn)))}
    # W: f_rep = q_(n+1,0)/sqrt2 -> F_rep=sqrt(d_p) f_rep -> F_val = sqrt(d_p/2) e_val ; use F_val=e_val and scale squared by d_p/2
    out={}
    for rule in ('cgs','fixed'):
        db=dual(b,d,par,al,ip,{h:e_val},rule,Nn)
        rep,Pt=closure_deriv(b,db,W,X,N(n-1),Nn)
        out[rule]=rep*1
    diff=float(np.max(np.abs(out['cgs']-out['fixed'])))
    rep=out['cgs']
    g_F=fro2(rep)*d[p]/2
    if be=='mp':
        sv=mp.svd_r(mp.matrix(rep.tolist()),compute_uv=False); spec2=max(sv)**2*d[p]/2
    else:
        spec2=np.linalg.svd(rep.astype(float),compute_uv=False)[0]**2*d[p]/2
    target=(mp.mpf(4)**n-1)/6 if be=='mp' else (4.0**n-1)/6
    # column structure: D(:,(n-1-j,j)) = rep q_k (q_k rep basis) should be -(-2)^j f_rep, f_rep = sqrt(w) e/sqrt2
    sw=np.array([mp.sqrt(w) for w in W],dtype=object) if be=='mp' else np.sqrt(W)
    colerr=0; lowcol=0
    for k,(t,j) in enumerate(cols[:N(n-1)]):
        qk=sw*b[k]/(mp.sqrt(d[k]) if be=='mp' else np.sqrt(d[k]))
        Dk=rep@qk*(mp.sqrt(d[p]/2) if be=='mp' else np.sqrt(d[p]/2))   # source scaled to unit budget
        if t==n-1:
            jj=j; want=-((-2)**jj)*sw*e_val/(mp.sqrt(2) if be=='mp' else np.sqrt(2))
            colerr=max(colerr,float(np.max(np.abs(Dk-want))))
        else:
            lowcol=max(lowcol,float(np.max(np.abs(Dk))))
    # budget check of the W source: ||f_rep||^2/sigma^2 = (1/2)/sig2
    info.update({'rules_max_derivative_diff':diff,'W_gain_fro':float(g_F),'W_gain_spec':float(spec2),'W_target_(4^n-1)/6':float(target),
                 'W_rel_err':float(abs(spec2-target)/target),'budget':float(mp.mpf(1)/2/sig2 if be=='mp' else 0.5/sig2),
                 'col_formula_maxerr':colerr,'lower_cols_max':lowcol,
                 'C_n_lower':float(mp.sqrt(target)/mp.cos(mp.pi/(n+3))) if be=='mp' else float(np.sqrt(target)/np.cos(np.pi/(n+3))),'2^(n-4)':2.0**(n-4)})
    if full:
        # full E_n by brute force over every (h,i) source direction and every stage, cgs rule
        tot=0.0; block=0.0
        for hh in range(1,Nn):
            pp=par[hh][1]
            for i in range(M):
                F=X*0; F[i]=one
                db=dual(b,d,par,al,ip,{hh:F},'cgs',Nn)
                for s in range(n):
                    rep,_=closure_deriv(b,db,W,X,N(s),N(s+1))
                    c=float(fro2(rep))*float(tau2[hh])/float(W[i])/(H*M*float(Xn2))
                    tot+=c
                    if hh==h and s==n-1: block+=c
        lowerR=(4.0**n-1)*(M-Nn)/(6*H*M*float(Xn2))
        info.update({'E_n_full':tot,'E_selected_block':block,'E_block_formula':lowerR,'E_block_rel_err':abs(block-lowerR)/lowerR,
                     'E_lower_closed':(4.0**n-1)/(6*n*(n+2)*np.cos(np.pi/(n+3))**2),'2^(n-8)':2.0**(n-8)})
    info['secs']=round(time.time()-t0,2)
    print(json.dumps(info),flush=True)

if __name__=='__main__':
    be=sys.argv[1]; full=sys.argv[2]=='full'
    for n in [int(x) for x in sys.argv[3].split(',')]: run(n,be,full)
