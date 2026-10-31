"""Claude audit-01 independent reconstruction of C0 catalogue counts and C3 ranks.
Written from the theory-file definitions; imports nothing from the developer code."""
import itertools, math, random, json, sys
from math import gcd, comb
from functools import reduce

def fiber_count(L,a,k,c):
    h=[0]*k; h[0]=1
    for Lj,aj in zip(L,a):
        g=[0]*k
        for r in range(k):
            m=Lj//k+(1 if r<Lj%k else 0)
            if m:
                for s in range(k): g[(s+aj*r)%k]+=h[s]*m
        h=g
    return h[c]

def orbit(d,n,k,a,c,L):
    seen=set(); stack=[(tuple(a),c%k,tuple(L))]
    while stack:
        a_,c_,L_=stack.pop()
        key=(a_,c_,L_)
        if key in seen: continue
        seen.add(key)
        for u in range(1,k):
            if gcd(u,k)==1: stack.append((tuple(u*x%k for x in a_),u*c_%k,L_))
        for j in range(d):
            a2=list(a_); a2[j]=(-a_[j])%k
            stack.append((tuple(a2),(c_-a_[j]*(L_[j]-1))%k,L_))
        for i in range(d):
            for j in range(i+1,d):
                if L_[i]==L_[j]:
                    a2=list(a_); a2[i],a2[j]=a2[j],a2[i]; stack.append((tuple(a2),c_,L_))
    return seen

raw=0; canon=0; surv={2:[],3:[]}; done=set()
for d in (2,3):
    for n in range(1,7):
        for L in itertools.combinations_with_replacement([n+1,n+2,n+3],d):
            for k in range(2,7):
                for a in itertools.product(range(1,k),repeat=d):
                    if reduce(gcd,a,k)!=1: continue
                    for c in range(k):
                        raw+=1
                        key=(d,n,k,a,c,L)
                        if key in done: continue
                        orb=orbit(d,n,k,a,c,L)
                        for (a_,c_,L_) in orb: done.add((d,n,k,a_,c_,L_))
                        canon+=1
                        cnt=fiber_count(L,a,k,c)
                        # sanity: orbit members have equal count
                        assert all(fiber_count(L_,a_,k,c_)==cnt for a_,c_,L_ in orb)
                        if cnt==comb(n+d,d): surv[d].append((n,k,a,c,L))
print("raw",raw,"canonical",canon,"survivors d2",len(surv[2]),"d3",len(surv[3]))
for d in (2,3): print(d,[sum(1 for s in surv[d] if s[0]==n) for n in range(1,7)])

# ---- C3: independent ranks at different primes / more trials
def pts(n,k,a,c,L):
    return sorted(i for i in itertools.product(*(range(x) for x in L)) if sum(p*q for p,q in zip(a,i))%k==c)
def canon_pts(P,L):
    best=None
    for mask in range(8):
        T=tuple(sorted(tuple(L[j]-1-x if mask>>j&1 else x for j,x in enumerate(p)) for p in P))
        if best is None or T<best: best=T
    return best
def mons(n): return [(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]
def rank_mod(M,p):
    M=[r[:] for r in M]; r=0; cols=len(M[0])
    for col in range(cols):
        piv=None
        for i in range(r,len(M)):
            if M[i][col]%p: piv=i;break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; inv=pow(M[r][col],p-2,p)
        for i in range(len(M)):
            if i!=r and M[i][col]%p:
                f=M[i][col]*inv%p; M[i]=[(x-f*y)%p for x,y in zip(M[i],M[r])]
        r+=1
    return r
reps={}
for (n,k,a,c,L) in surv[3]:
    P=pts(n,k,a,c,L); reps.setdefault((n,L,canon_pts(P,L)),[]).append((k,a,c))
print("C3 representatives",len(reps))
rng=random.Random(20261031)
PR=[10007,10009,32003]; res={}
for (n,L,P),srcs in reps.items():
    N=comb(n+3,3); best=0
    for p in PR:
        for t in range(3):
            ax=[rng.sample(range(p),x) for x in L]
            M=[[pow(ax[0][i],e0,p)*pow(ax[1][j],e1,p)*pow(ax[2][l],e2,p)%p for (e0,e1,e2) in mons(n)] for (i,j,l) in P]
            best=max(best,rank_mod(M,p))
            if best==N: break
        if best==N: break
    res[(n,L,P)]=(best,N)
for n in range(1,7):
    g=[v for kk,v in res.items() if kk[0]==n]
    print("n",n,"reps",len(g),"full",sum(b==N for b,N in g),"deficient",sum(b<N for b,N in g))
json.dump([{"n":k[0],"L":k[1],"points":k[2],"rank":v[0],"N":v[1]} for k,v in res.items()],open("topics/lattice-unisolvence-20261031/claude-audit/outputs/indep_ranks.json","w"))
