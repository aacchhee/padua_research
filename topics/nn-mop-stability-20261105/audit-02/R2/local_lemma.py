"""Independent exact test of the localized NN lemma (conditioning-normality-certificate.md MINOR 11).
Positive discrete measures; one weight of w2 is tuned so that a chosen mixed index nu*=(n,1) of
degree k is singular, while all indices of degree <= k-1 stay normal.  Then with R=k-1:
 - NN identities hold at |nu|<=R-1 (verified by direct polynomial identity, coefficients unique),
 - compatibility (A),(B1),(B2) at |eta|<=R-2,
 - C4 layer recursion from marginal data reproduces true coefficients through layer R-1,
 - the computed d at eta=nu*-e1-e2 vanishes (equivalence d!=0 <=> opposite corner normal),
   and the certificate implication holds at other degree-k targets.
"""
from fractions import Fraction as F
import itertools, sys

def mom(x,w,p): return sum(wi*xi**p for xi,wi in zip(x,w))
def L(x,w,poly,shift=0):  # poly: coeff list low->high
    return sum(c*mom(x,w,j+shift) for j,c in enumerate(poly))

def det(A):
    A=[r[:] for r in A]; n=len(A); d=F(1)
    for i in range(n):
        p=next((r for r in range(i,n) if A[r][i]!=0),None)
        if p is None: return F(0)
        if p!=i: A[i],A[p]=A[p],A[i]; d=-d
        d*=A[i][i]
        for r in range(i+1,n):
            f=A[r][i]/A[i][i]
            if f: A[r]=[a-f*b for a,b in zip(A[r],A[i])]
    return d
def solve(A,b):
    n=len(A); M=[A[i][:]+[b[i]] for i in range(n)]
    for i in range(n):
        p=next(r for r in range(i,n) if M[r][i]!=0); M[i],M[p]=M[p],M[i]
        M[i]=[v/M[i][i] for v in M[i]]
        for r in range(n):
            if r!=i and M[r][i]!=0:
                f=M[r][i]; M[r]=[a-f*c for a,c in zip(M[r],M[i])]
    return [M[i][n] for i in range(n)]

def Mmat(x,W,nu):
    n,m=nu;k=n+m
    rows=[[mom(x,W[0],i+j) for j in range(k)] for i in range(n)]
    rows+=[[mom(x,W[1],i+j) for j in range(k)] for i in range(m)]
    return rows
def normal(x,W,nu): return det(Mmat(x,W,nu))!=0
def P(x,W,nu):
    n,m=nu;k=n+m
    if k==0: return [F(1)]
    rhs=[-mom(x,W[0],i+k) for i in range(n)]+[-mom(x,W[1],i+k) for i in range(m)]
    return solve(Mmat(x,W,nu),rhs)+[F(1)]
def padd(*ps):
    n=max(len(p) for p in ps); out=[F(0)]*n
    for p in ps:
        for i,c in enumerate(p): out[i]+=c
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def sc(c,p): return [c*v for v in p]
def xm(p): return [F(0)]+p
def t(p): return p[-2] if len(p)>=2 else F(0)

def true_nn(x,W,nu,Pd):
    """NN coefficients at nu by direct identity matching (needs Pd on the involved indices)."""
    n,m=nu; out={}
    for j,(e) in enumerate([(1,0),(0,1)]):
        succ=(n+e[0],m+e[1])
        b=t(Pd[nu])-t(Pd[succ])
        res=padd(xm(Pd[nu]),sc(-1,Pd[succ]),sc(-b,Pd[nu]))
        preds=[(n-1,m) if n>0 else None,(n,m-1) if m>0 else None]
        basis=[Pd[p] for p in preds if p]
        # solve res = sum a_i basis_i by coefficients (unique if independent)
        if not basis:
            assert all(c==0 for c in res); a=[]
        else:
            dim=len(basis[0])
            A=[[bp[r] if r<len(bp) else F(0) for bp in basis] for r in range(dim)]
            rr=[res[r] if r<len(res) else F(0) for r in range(dim)]
            # least-squares-free exact: pick independent rows
            import itertools as it
            sol=None
            for rows in it.combinations(range(dim),len(basis)):
                S=[A[r] for r in rows]
                if det(S)!=0: sol=solve(S,[rr[r] for r in rows]);break
            assert sol is not None
            chk=padd(*[sc(s,bp) for s,bp in zip(sol,basis)],sc(-1,res))
            assert all(c==0 for c in chk), ('NN identity residual', nu, j)
            a=sol
        it_=iter(a)
        a1=next(it_) if preds[0] else F(0); a2=next(it_) if preds[1] else F(0)
        out[j]=(b,a1,a2)
    assert out[0][1:]==out[1][1:], 'a coefficients depend on j'
    # h-ratio check
    for s,(pred) in enumerate([(n-1,m),(n,m-1)]):
        if nu[s]>0:
            h=L(x,W[s],Pd[nu],nu[s]); hp=L(x,W[s],Pd[pred],nu[s]-1)
            assert hp!=0 and out[0][1+s]==h/hp, ('h ratio',nu,s)
    return dict(b1=out[0][0],b2=out[1][0],a1=out[0][1],a2=out[0][2])

def marg(x,w,K):
    ps=[[F(1)]]
    al=[];be=[]
    # monic OPs via axis moment systems
    for k in range(1,K+2):
        W=[w,w]; ps.append(P(x,[w,w],(k,0)))
    for k in range(K+1):
        be.append(t(ps[k])-t(ps[k+1]))
        al.append(F(0) if k==0 else L(x,w,ps[k],k)/L(x,w,ps[k-1],k-1))
    return al,be

def c4(x,W,T):
    """Layer recursion (PD-T289 Sec.2) from marginal data through layer T."""
    a1m,b1m=marg(x,W[0],T); a2m,b2m=marg(x,W[1],T)
    c={}
    for s in range(T+1):
        for n in range(s+1):
            c[(n,s-n)]={}
    for k in range(T+1):
        c[(k,0)].update(a1=a1m[k],a2=F(0),b1=b1m[k]); c[(0,k)].update(a1=F(0),a2=a2m[k],b2=b2m[k])
    d=lambda nu:c[nu]['b2']-c[nu]['b1']
    S=lambda nu:c[nu]['a1']+c[nu]['a2']
    for s in range(T):
        # a's on layer s+1
        for n in range(1,s+1):
            eta=(n,s+1-n)
            c[eta]['a1']=c[(n,s-n)]['a1']*d((n,s-n))/d((n-1,s-n))
            c[eta]['a2']=c[(n-1,s+1-n)]['a2']*d((n-1,s+1-n))/d((n-1,s-n))
        for n in range(s+1):
            nu=(n,s-n); e1=(n+1,s-n); e2=(n,s-n+1)
            q=c[nu]['b1']-(S(e1)-S(e2))/d(nu)
            c[e2]['b1']=q; c[e1]['b2']=q+d(nu)
    return c

def run(x,W,label,R,singular_target):
    N=len(x)
    deg=lambda k:[(n,k-n) for n in range(k+1)]
    norm={nu:normal(x,W,nu) for k in range(N+1) for nu in deg(k)}
    assert all(norm[nu] for k in range(R+1) for nu in deg(k)), 'hypothesis fails'
    assert not norm[singular_target]
    Pd={nu:P(x,W,nu) for nu in norm if norm[nu]}
    tr={nu:true_nn(x,W,nu,Pd) for k in range(R) for nu in deg(k)}   # |nu|<=R-1
    # compatibility at |eta|<=R-2
    dd=lambda nu:tr[nu]['b2']-tr[nu]['b1']; SS=lambda nu:tr[nu]['a1']+tr[nu]['a2']
    ncomp=0
    for k in range(R-1):
        for nu in deg(k):
            n,m=nu; e1=(n+1,m); e2=(n,m+1)
            assert Pd[e1]==padd(Pd[e2],sc(dd(nu),Pd[nu])) or padd(Pd[e1],sc(-1,Pd[e2]),sc(-dd(nu),Pd[nu]))==[0]
            if m>0: assert tr[e1]['a2']*dd((n,m-1))==dd(nu)*tr[nu]['a2']
            if n>0: assert tr[e2]['a1']*dd((n-1,m))==dd(nu)*tr[nu]['a1']
            assert tr[e1]['b2']-tr[e2]['b1']==dd(nu)
            assert dd(nu)*tr[e2]['b1']==dd(nu)*tr[nu]['b1']-(SS(e1)-SS(e2))
            ncomp+=1
    comp=c4(x,W,R-1)
    for nu in tr:
        for f in ('a1','a2','b1','b2'):
            assert comp[nu][f]==tr[nu][f],(nu,f)
    # certificate step at target degree k=R+1
    k=R+1; res=[]
    for nu in deg(k):
        n,m=nu
        if n>0 and m>0:
            eta=(n-1,m-1); dv=comp[eta]['b2']-comp[eta]['b1']
            res.append((nu,dv!=0,norm[nu]))
            assert (dv!=0)==norm[nu], ('equivalence fails',nu)
    higher=[nu for nu in norm if not norm[nu]]
    print(f'{label}: N={N} R={R} NN sites={len(tr)} squares={ncomp} C4==true through layer {R-1};'
          f' degree-{k} (d!=0, normal): {res}; all non-normal indices deg<=N: {sorted(higher,key=sum)}')

def tune(x,w1,w2,idx,target):
    # det M_target is affine in w2[idx] when target[1]==1: solve for root
    def dv(tv):
        W2=list(w2);W2[idx]=tv;return det(Mmat(x,[w1,W2],target))
    d0=dv(F(0));d1=dv(F(1)); return -d0/(d1-d0)

if __name__=='__main__':
    # Case 1: N=5, singular (2,1) at degree 3 (R=2)
    x=[F(i) for i in range(5)]; w1=[F(1),F(2),F(1),F(3),F(1)]; w2=[F(2),F(1),F(1),F(1),None]
    for idx_try in range(5):
        pass
    cases=[]
    for N,target,idx in [(5,(2,1),4),(6,(3,1),5),(7,(4,1),6),(6,(2,1),0),(7,(3,1),3)]:
        x=[F(i) for i in range(N)]
        w1=[F(1+(i*i)%3) for i in range(N)]
        w2=[F(1+(2*i+1)%4, 1+i%2) for i in range(N)]
        tv=tune(x,w1,w2,idx,target)
        if tv<=0: print('nonpositive tuned weight',N,target,idx,tv); continue
        w2[idx]=tv
        try:
            run(x,[w1,w2],f'tuned w2[{idx}]={tv}',sum(target)-1,target)
        except AssertionError as e:
            print('ASSERT',N,target,idx,e)
