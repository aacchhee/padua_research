#!/usr/bin/env python3
"""L2 auditor's own exact check of the G2 certificates (no repository code imported).
Own T24/rotQ24 builder, own BJ monic Gram-Schmidt, and a first-principles
derivative of the actual closure operator (I-P_hat_12) X P_hat_11 for two
different smooth exact-base rules via exact rational dual numbers."""
import sys, time, json, hashlib
from flint import fmpq as Q, fmpq_mat as Mat

def points(name):
    pts=[]
    for i in range(25):
        for j in range(25 if name=='rotated' else 25-i):
            x,y=Q(i,12)-1,Q(j,12)-1
            pts.append((x,y) if name=='triangle' else ((3*x-4*y)/5,(4*x+3*y)/5))
    return pts

def N(s): return (s+1)*(s+2)//2

def build(pts,deg):
    M=len(pts); X=[p[0] for p in pts]; Y=[p[1] for p in pts]
    cols=[[Q(1)]*M]; meta=[(0,0)]; par=[None]; idx={(0,0):0}
    for t in range(1,deg+1):
        for j in range(t+1):
            if j==0: a,p=0,idx[(t-1,0)]
            else: a,p=1,idx[(t-1,j-1)]
            idx[(t,j)]=len(cols); meta.append((t,j)); par.append((a,p))
            cols.append(None)
    # columns as 1xM Mat
    Xv=Mat([X]); Yv=Mat([Y])
    def mulc(v,a):
        c=X if a==0 else Y
        return Mat([[v[0,i]*c[i] for i in range(M)]])
    b=[Mat([[Q(1)]*M])]; d=[Q(M)]; alpha=[None]; tau2=[None]
    for k in range(1,len(meta)):
        a,p=par[k]; u=mulc(b[p],a)
        al=[(bl*u.transpose())[0,0]/dl for bl,dl in zip(b,d)]
        r=u
        for c,bl in zip(al,b):
            if c: r=r-c*bl
        b.append(r); d.append((r*r.transpose())[0,0]); alpha.append(al); tau2.append((u*u.transpose())[0,0])
    return X,Y,b,d,par,alpha,tau2,meta,mulc

def dual_run(b,d,par,alpha,mulc,h,F,rule,M):
    """Return derivative columns db_k (1xM) of the perturbed monic columns at eps=0.
    rule 'cgs': b_hat_k = u - sum_l <b_hat_l,u>/<b_hat_l,b_hat_l> b_hat_l, u=A b_hat_p + eps F_k.
    rule 'fixed': b_hat_k=(1+eps*rho_k)[u - sum_l (alpha_kl+eps*r_kl) b_hat_l] (coefficients not recomputed)."""
    Z=Mat(1,M); db=[Z]
    for k in range(1,len(b)):
        a,p=par[k]
        u=mulc(b[p],a); du=mulc(db[p],a)
        if k==h: du=du+F
        if rule=='cgs':
            v=du
            for l in range(k):
                c=alpha[k][l]
                # derivative of c_hat*b_hat_l: dc*b_l + c*db_l
                num=(b[l]*u.transpose())[0,0]
                dnum=(db[l]*u.transpose())[0,0]+(b[l]*du.transpose())[0,0]
                dden=2*(b[l]*db[l].transpose())[0,0]
                dc=dnum/d[l]-num*dden/(d[l]*d[l])
                if dc: v=v-dc*b[l]
                if c: v=v-c*db[l]
        else:
            rho=Q((3*k)%7-3,5)
            v=du
            for l in range(k):
                c=alpha[k][l]; r=Q((7*k+3*l)%11-5,7)
                if c: v=v-c*db[l]
                v=v-r*b[l]
            v=v+rho*b[k]   # derivative of (1+eps rho) * (exact residual b_k)
        db.append(v)
    return db

def closure_derivative_frob(b,d,db,X,M,ns,nt):
    """W such that d/deps[(I-P_hat_t) X P_hat_s] = W Bs^T; returns W, ||.||_F^2.
    Uses P=B(B^TB)^(-1)B^T product rule with full dG (no orthogonality of perturbed columns assumed)."""
    Bt=Mat([[b[k][0,i] for k in range(nt)] for i in range(M)])   # M x nt
    dBt=Mat([[db[k][0,i] for k in range(nt)] for i in range(M)])
    Bs=Mat([[b[k][0,i] for k in range(ns)] for i in range(M)])
    dBs=Mat([[db[k][0,i] for k in range(ns)] for i in range(M)])
    Xd=Mat(M,M)
    for i in range(M): Xd[i,i]=X[i]
    Gti=Mat(nt,nt); Gsi=Mat(ns,ns)
    for k in range(nt): Gti[k,k]=1/d[k]
    for k in range(ns): Gsi[k,k]=1/d[k]
    XBs=Xd*Bs
    # exact closure R_t X Bs = 0 check
    assert XBs-Bt*(Gti*(Bt.transpose()*XBs))==Mat(M,ns)
    dGt=dBt.transpose()*Bt+Bt.transpose()*dBt
    dGs=dBs.transpose()*Bs+Bs.transpose()*dBs
    # dP_t X P_s = [dBt Gti Bt^T + Bt Gti dBt^T - Bt Gti dGt Gti Bt^T] XBs Gsi Bs^T
    K1=Bt.transpose()*XBs; K2=dBt.transpose()*XBs
    T1=dBt*(Gti*K1)+Bt*(Gti*K2)-Bt*(Gti*(dGt*(Gti*K1)))
    term1=-(T1*Gsi)                       # coefficient matrix of Bs^T
    # (I-P_t) X dP_s = (I-P_t) X [dBs Gsi Bs^T + Bs Gsi dBs^T - Bs Gsi dGs Gsi Bs^T]
    # second/third pieces: (I-P_t) X Bs = 0 (checked), so only first piece survives; but compute generally:
    XdBs=Xd*dBs
    RXdBs=XdBs-Bt*(Gti*(Bt.transpose()*XdBs))
    term2=RXdBs*Gsi
    W=term1+term2
    # also verify the dropped pieces vanish exactly (R_t X Bs = 0 already asserted)
    Gs=Mat(ns,ns)
    for k in range(ns): Gs[k,k]=d[k]
    fro=sum((W[i,j]**2*d[j] for i in range(M) for j in range(ns)),Q(0))   # tr(W Gs W^T)
    return W,fro

def main():
    name=sys.argv[1]; nodes=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else []
    t0=time.time(); pts=points(name); M=len(pts)
    X,Y,b,d,par,alpha,tau2,meta,mulc=build(pts,12)
    assert len(b)==91 and all(z>0 for z in d)
    B=Mat([[b[k][0,i] for i in range(M)] for k in range(91)])
    G=B*B.transpose()
    assert all(G[i,j]==(d[i] if i==j else 0) for i in range(91) for j in range(91))
    X2=max(x*x for x in X)
    h=6; assert meta[h]==(3,0) and par[h]==(0,3)
    ns,nt=78,91
    print(json.dumps({'event':'basis','set':name,'M':M,'X2':str(X2),'tau2_h6':str(tau2[h]),'secs':round(time.time()-t0,2)}),flush=True)
    # own omega formula for all nodes (L2-01 eq.(7)-(8)), own implementation
    g=[Mat(1,M) for _ in range(91)]; g[h]=Mat([[Q(1)]*M])
    for k in range(h+1,91):
        a,p=par[k]; v=mulc(g[p],a)
        for l in range(h,k):
            if alpha[k][l]: v=v-alpha[k][l]*g[l]
        g[k]=v
    C=Mat(91,ns)
    for j in range(ns):
        xb=mulc(b[j],0)
        for l in range(91):
            C[l,j]=(b[l]*xb.transpose())[0,0]/d[l]
    Rdiag=[1-sum((b[k][0,i]**2/d[k] for k in range(91)),Q(0)) for i in range(M)]
    ell=[]
    for i in range(M):
        e=Q(0)
        for j in range(ns):
            om=X[i]*g[j][0,i]-sum((C[l,j]*g[l][0,i] for l in range(h,91) if C[l,j]),Q(0))
            e+=om*om/d[j]
        ell.append(tau2[h]*Rdiag[i]*e)
    imax=max(range(M),key=lambda i:ell[i])
    Wl=ell[imax]/X2; Rl=sum(ell,Q(0))/(90*M*X2)
    fl=lambda q:int(q.numerator)//int(q.denominator)
    out={'event':'formula','set':name,'argmax_node':imax,'point':[str(c) for c in pts[imax]],
         'W_lower_floor':fl(Wl),'R_partial_floor':fl(Rl),'W_lower_sha':hashlib.sha256(str(Wl).encode()).hexdigest(),
         'R_partial_sha':hashlib.sha256(str(Rl).encode()).hexdigest(),'secs':round(time.time()-t0,2)}
    print(json.dumps(out),flush=True)
    # first-principles actual-rule derivative at selected nodes
    if nodes==[-1]:
        tot=Q(0); allmatch=True; maxrank=0
        for i in range(M):
            F=Mat(1,M); F[0,i]=1
            db=dual_run(b,d,par,alpha,mulc,h,F,'cgs',M)
            W,fro=closure_derivative_frob(b,d,db,X,M,ns,nt)
            allmatch&=(tau2[h]*fro==ell[i]); tot+=tau2[h]*fro
        Rd=tot/(90*M*X2)
        print(json.dumps({'event':'dual_allnodes','set':name,'all_nodes_match_ell':allmatch,'R_partial_floor_dual':fl(Rd),'R_partial_sha_dual':hashlib.sha256(str(Rd).encode()).hexdigest(),'secs':round(time.time()-t0,2)}),flush=True)
        nodes=[]
    for i in nodes:
        F=Mat(1,M); F[0,i]=1
        res={}
        for rule in ('cgs','fixed'):
            db=dual_run(b,d,par,alpha,mulc,h,F,rule,M)
            W,fro=closure_derivative_frob(b,d,db,X,M,ns,nt)
            rank=W.rref()[1]
            res[rule]=(fro,rank,W)
        assert res['cgs'][2]==res['fixed'][2], 'rule dependence!'
        fro,rank,_=res['cgs']
        print(json.dumps({'event':'dual','set':name,'node':i,'rank_W':rank,'rules_identical_derivative':True,
              'tau2_fro_equals_ell':tau2[h]*fro==ell[i],'gain_floor':fl(tau2[h]*fro/X2),'secs':round(time.time()-t0,2)}),flush=True)
main()
