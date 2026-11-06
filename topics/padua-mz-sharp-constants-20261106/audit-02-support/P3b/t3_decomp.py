import numpy as np, json, math, sys
from cc_common import *
q=8
def run(N, extra_vectors=True):
    L=math.log(N); J=N//2; K=math.ceil(L*L); M=int(N//L)
    assert 1<K<=M<N/4
    lam,ustar,w=lam_min(N)
    k=np.arange(N+1); c=np.ones(N+1); c[0]=c[-1]=2; a_sign=(-1.0)**k
    # left output half grid t in [0,N/2]
    t,wt=cell_grid(N/2,q)
    th=np.pi*t/N; mass=wt*np.sin(th)*np.pi/N
    # full interpolation matrix on left half via coef matrix
    C=coef_matrix(N)
    Phi=np.cos(np.outer(th,np.arange(N+1)))@C        # rows t, cols k
    H=(2*t*np.sin(np.pi*t)/np.pi)[:,None]*a_sign[None,:]/(c[None,:]*(t[:,None]**2-k[None,:]**2))
    r=Phi-H
    P=np.zeros_like(H)
    ints=np.arange(1,M+1)
    P[:,ints]=(2*np.sin(np.pi*t)/(np.pi*t))[:,None]*a_sign[None,ints]*(ints[None,:]<t[:,None])
    R=np.zeros_like(H); R[:,ints]=H[:,ints]-P[:,ints]
    sq=np.sqrt(mass)[:,None]
    Hs=H*sq; Ps=P*sq; Rs=R*sq; rs=r*sq; Phis=Phi*sq
    def lnorm(A,u): return float(np.sum((A@u)**2))
    def both(A,u): # squared norm over both output halves (reflection)
        return lnorm(A,u)+lnorm(A,u[::-1])
    Qf=lambda u: float(np.sum(w*u*u))
    groups={
      'good': (k>=K)&(k<=M) | (k>=N-M)&(k<=N-K),
      'micint': (k>=1)&(k<K) | (k>N-K)&(k<=N-1),
      'end': (k==0)|(k==N),
      'bulk': (k>M)&(k<N-M)}
    left={'good':(k>=K)&(k<=M),'micint':(k>=1)&(k<K),'end':k==0}
    right={g:left[g][::-1] for g in left}
    res=dict(N=N,L=L,K=K,M=M,lam=lam,L2lam=L*L*lam,CN=None)
    H_J=np.sum(1/np.arange(1,J+1)); A=2*H_J/math.pi+1; eps=2/L**2
    CN=math.sqrt(2*A*A+6)/(math.pi*math.sqrt(1-eps)); res['CN']=CN
    HK=np.sum(1/np.arange(1,K+1))
    res['DN']=160+2*math.sqrt(L*HK)+30*math.sqrt(L+5)
    # operator norms (sup over inputs) of pieces in Q-norm
    ws=1/np.sqrt(w)
    def opn(A,cols):
        B=A[:,cols]*ws[None,cols]; return float(np.linalg.svd(B,compute_uv=False)[0])
    on={}
    lg=np.where(left['good'])[0]; lmi=np.where(left['micint'])[0]; li=np.arange(1,M+1)
    on['R_selferr_1..M_lefthalf']=opn(Rs,li)            # claimed <=80
    on['P_prim_good_lefthalf']=opn(Ps,lg)               # claimed <= C_N/sqrt2-ish per half
    on['P_prim_micint_lefthalf']=opn(Ps,lmi)            # claimed <= 2sqrt(L H_K)/sqrt2...
    cr=np.where(k>=N-M)[0]
    on['cross_from_right_edge_lefthalf']=opn(Hs,cr)     # claimed <= sqrt(3(L+1))
    edge=np.where((k<=M)|(k>=N-M))[0]
    on['r_cot_edges_lefthalf']=opn(rs,edge)             # claimed <= 2sqrt(2(L+1))
    on['endpoint0_self_lefthalf']=opn(Hs,np.array([0]))
    # bulk full norm: both halves; bulk support symmetric so use stacked
    bk=np.where(groups['bulk'])[0]
    Bfull=np.vstack([Phis[:,bk], Phis[:,(N-bk)]])*ws[None,bk]
    on['bulk_full']=float(np.linalg.svd(Bfull,compute_uv=False)[0])  # claimed <= sqrt(pi L/2)
    # whole interpolation operator norm (both halves) = 1/sqrt(lam)
    on['claimed']=dict(R=80,cross=math.sqrt(3*(L+1)),r=2*math.sqrt(2*(L+1)),bulk=math.sqrt(math.pi*L/2),
                       end=math.sqrt(L+5),Pgood_both=CN,Pmic_both=2*math.sqrt(L*HK))
    res['opnorms']=on
    # identity checks
    res['check_r_sup']=float(np.max(np.abs(r[:,edge]))*N/2)  # should be <=2 (|e|<2 => |r_k|<=2/(N c_k))
    # vectors
    rng=np.random.default_rng(1)
    vecs={'minimizer':ustar}
    if extra_vectors:
        vecs['alt_inv_sqrtw']=(-1.0)**k/np.sqrt(w)
        vecs['alt_good_only']=(-1.0)**k/np.sqrt(w)*groups['good']
        vecs['center']=np.exp(-((k-N/2)/5.0)**2)*(-1.0)**k
        vecs['ends_opposite']=np.where(k==0,1.0,0)-np.where(k==N,1.0,0)
        vecs['ends_equal']=np.where(k==0,1.0,0)+np.where(k==N,1.0,0)
        vecs['random']=rng.standard_normal(N+1)/np.sqrt(w)
        vecs['minimizer_signflip_alt']=ustar*(-1.0)**k
    vr={}
    for name,u in vecs.items():
        Q=Qf(u); tot=both(Phis,u)
        d=dict(norm_over_sqrtQ=math.sqrt(tot/Q))
        for g in ['good','micint','end']:
            ug=u*(left[g]|right[g])
            d[g+'_Qfrac']=Qf(ug)/Q
            # self primitive / self error / cross / r on both halves
            uL=u*left[g]; uR=u*right[g]
            def piece(A_self,A_cross):
                s=lnorm(A_self,uL)+lnorm(A_self,uR[::-1])
                return math.sqrt(s/Q)
            if g!='end':
                d[g+'_prim']=piece(Ps,None)
                d[g+'_err']=piece(Rs,None)
            else:
                d[g+'_self']=piece(Hs,None)
            d[g+'_cross']=math.sqrt((lnorm(Hs,uR)+lnorm(Hs,uL[::-1]))/Q)
            d[g+'_r']=math.sqrt(both(rs,ug)/Q)
            d[g+'_total']=math.sqrt(both(Phis,ug)/Q)
        ub=u*groups['bulk']; d['bulk_Qfrac']=Qf(ub)/Q; d['bulk_total']=math.sqrt(both(Phis,ub)/Q)
        vr[name]=d
    res['vectors']=vr
    return res
out=[]
for N in [int(a) for a in sys.argv[1:]]:
    r=run(N); out.append(r)
    print(json.dumps(r,indent=0,default=float)[:4000],flush=True)
json.dump(out,open('t3_decomp_%s.json'%'_'.join(sys.argv[1:]),'w'),indent=1,default=float)
