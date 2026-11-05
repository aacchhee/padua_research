# Own MEASURED sanity check of L3-01 constants (2)-(5) and the attributed radius ceiling, incl. lambda_1=0.
import mpmath as mp, random, sys
mp.mp.dps=60
random.seed(int(sys.argv[2]) if len(sys.argv)>2 else 1)
s=int(sys.argv[1]) if len(sys.argv)>1 else 3
mons=[(t-j,j) for t in range(s+1) for j in range(t+1)]; N=len(mons)
M=max(N+4,int(1.5*N))
pts=[]
while len(pts)<M:
    x=mp.mpf(random.randint(1,999))/1000; y=mp.mpf(random.randint(1,999))/1000
    if x+y<1: pts.append((x,y))
w=[mp.mpf(random.randint(1,9)) for _ in pts]; W=sum(w); w=[wi/W for wi in w]
X=[p[0] for p in pts]; Y=[p[1] for p in pts]
idx={m:k for k,m in enumerate(mons)}
par=[None]; A=[None]
for k,(i,j) in enumerate(mons[1:],1):
    if i>=1: par.append(idx[(i-1,j)]); A.append(X)
    else: par.append(idx[(i,j-1)]); A.append(Y)
dot=lambda u,v: mp.fsum(a*b for a,b in zip(u,v)); nrm=lambda u: mp.sqrt(dot(u,u))
q=[[mp.sqrt(wi) for wi in w]]; c={}; beta=[None]; v=[None]
for k in range(1,N):
    yk=[a*b for a,b in zip(A[k],q[par[k]])]; v.append(nrm(yk)); r=yk[:]
    for l in range(k):
        c[(k,l)]=dot(q[l],yk); r=[ri-c[(k,l)]*ql for ri,ql in zip(r,q[l])]
    b_=nrm(r); beta.append(b_); q.append([ri/b_ for ri in r])
a=[None]+[max(abs(t) for t in A[k]) for k in range(1,N)]
def consts(lam):
    h=[mp.mpf(0)]; C=[None]
    for k in range(1,N):
        H=mp.sqrt(mp.fsum(hl**2 for hl in h[:k]))
        Ck=a[k]*(1+lam[k])*h[par[k]]+lam[k]*v[k]+v[k]*H; C.append(Ck); h.append(2*Ck/beta[k])
    b=max(C[k]/beta[k] for k in range(1,N))
    Delta=mp.mpf(0); K=mp.mpf(1)
    for i in range(M):
        S=mp.mpf(0)
        L=mp.eye(N)
        for k in range(1,N):
            alpha=A[k][i]
            for l in range(k):
                D=a[k]*(1+lam[k])*h[par[k]]+lam[k]*v[k]+v[k]*h[l]
                T=2*D/beta[k]+2*abs(c[(k,l)])*C[k]/beta[k]**2+(2*abs(alpha)*C[k]/beta[k]**2 if l==par[k] else 0)
                S+=T**2
                L[k,l]=(c[(k,l)]-(alpha if l==par[k] else 0))/beta[k]
        Delta=max(Delta,mp.sqrt(S)); Li=L**-1
        K=max(K,mp.norm(Li,2) if False else mp.sqrt(mp.fsum(Li[r_,cc]**2 for r_ in range(N) for cc in range(N))))
    d=K*Delta
    inv=lambda z: mp.inf if z==0 else 1/z
    rR=min(mp.mpf(1),inv(2*b),inv(2*d))
    return b,Delta,K,d,rR
cases={'lam=1':[None]+[mp.mpf(1)]*(N-1),
       'lam1=0,rest=1':[None,mp.mpf(0)]+[mp.mpf(1)]*(N-2),
       'lam1..3=0,rest=1':[None,0,0,0]+[mp.mpf(1)]*(N-4),
       'only_last=1':[None]+[mp.mpf(0)]*(N-2)+[mp.mpf(1)],
       'lam=0':[None]+[mp.mpf(0)]*(N-1)}
print('s',s,'N',N,'nodes',M)
for name,lam in cases.items():
    lam=[None]+[mp.mpf(x) for x in lam[1:]]
    b,Dl,K,d,rR=consts(lam)
    pos=[k for k in range(1,N) if lam[k]>0]
    if pos:
        j=pos[0]; ceil=mp.power(5,-mp.mpf(N-2-j)/2)/(4*mp.sqrt(2)*lam[j])
        orig=(mp.power(5,-mp.mpf(N-3)/2)/(4*mp.sqrt(2)*lam[1])) if lam[1]>0 else mp.inf
    else: j=None; ceil=mp.inf; orig=mp.inf
    print(f"{name:18s} b={mp.nstr(b,6)} d/b={mp.nstr(d/b,6) if b else 'na'} d>=sqrt2 b:{d>=mp.sqrt(2)*b} r_R={mp.nstr(rR,6)} orig_ceiling={mp.nstr(orig,6)} shifted(j={j})={mp.nstr(ceil,6)} r<=orig:{rR<=orig} r<=shifted:{rR<=ceil}")
