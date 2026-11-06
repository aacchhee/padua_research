# Independent check (Claude) of every T8 round06 M=N witness: nodes cos(2pi(k z_j/M + phi_j/den)), k<M.
# Rank over F_p via ring hom Z[zeta_L,1/2]->F_p, omega primitive L-th root, p=1 mod L, primes distinct from producer's.
import json, sys, math, time
from sympy import isprime, primitive_root, factorint
d=json.load(open(sys.argv[1]))
def rank_mod(M,p):
    M=[r[:] for r in M]; rk=0; nc=len(M[0])
    for c in range(nc):
        piv=next((r for r in range(rk,len(M)) if M[r][c]),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]; inv=pow(M[rk][c],p-2,p); prow=M[rk]
        for r in range(rk+1,len(M)):
            f=M[r][c]
            if f:
                f=f*inv%p; M[r]=[(x-f*y)%p for x,y in zip(M[r],prow)]
        rk+=1
    return rk
out=[]
for w in d['rows']:
    if w.get('outcome')!='exact_witness': continue
    n,N,Mo,z=w['n'],w['N'],w['M'],w['z']; den=w['phase_den']; ph=w['phase_nums']
    L=Mo*den//math.gcd(Mo,den)
    m=[tuple((k*z[j]*(L//Mo)+ph[j]*(L//den))%L for j in range(3)) for k in range(Mo)]
    key=lambda r: tuple(min(x,(L-x)%L) for x in r)
    nodes=sorted({key(r) for r in m})
    used={c['p'] for c in w['certificate']['checks']}
    mons=[(a,b,c) for a in range(n+1) for b in range(n+1) for c in range(n+1) if a+b+c<=n]
    t=1; p=None
    while True:
        q=L*t+1
        if q>1000 and isprime(q) and q not in used: p=q; break
        t+=1
    g=primitive_root(p); om=pow(g,(p-1)//L,p); assert all(pow(om,L//r,p)!=1 for r in factorint(L))
    i2=pow(2,p-2,p); cv=lambda x:(pow(om,x,p)+pow(om,(L-x)%L,p))*i2%p
    t0=time.time()
    V=[[pow(cv(r[0]),a,p)*pow(cv(r[1]),b,p)*pow(cv(r[2]),c,p)%p for a,b,c in mons] for r in nodes]
    rk=rank_mod(V,p)
    out.append(dict(n=n,N=N,M=Mo,z=z,L=L,nodes=len(nodes),p=p,rank=rk,ok=(len(nodes)==N and rk==N),sec=round(time.time()-t0,1)))
    print(out[-1],flush=True)
print("ALL_OK",all(o['ok'] for o in out),"degrees",[o['n'] for o in out])
