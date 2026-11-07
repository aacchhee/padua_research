import sys, math, itertools as it
import bf_cosets as b
def run_fast(M, degs):
    N=2*M
    targets={n:math.comb(n+3,3) for n in degs}
    maxsize=8*max(targets.values())
    Hs=b.subgroups(M,maxsize)
    p=b.find_prime(N); z=b.prim_root_of_unity(N,p); cy=b.Cyclo(N)
    hits={n:{"target_cases":0,"unisolvent":0,"deficient_exact":0} for n in degs}
    ex=[]; inv=0; cos=0; mism=[]
    classif={}
    for H in Hs:
        if not all(b.negj(h,j,M) in H for h in H for j in range(3)): continue
        inv+=1
        P=[tuple(2*c for c in h) for h in H]; Pset=set(P)
        S=[[aj for aj in range(N) if tuple((2*aj)%N if k==j else 0 for k in range(3)) in Pset] for j in range(3)]
        seen=set(); ncos=0
        for a in it.product(*S):
            A=frozenset(tuple((ai+pi)%N for ai,pi in zip(a,pp)) for pp in P)
            key=min(A)
            if key in seen: continue
            seen.add(key)
            assert all(b.negj(u,j,N) in A for u in A for j in range(3))
            ncos+=1; cos+=1
            X=sorted({tuple(min(c,N-c) for c in u) for u in A})
            for n,t in targets.items():
                if len(X)!=t: continue
                hits[n]["target_cases"]+=1
                modes=b.basis(n)
                if b.modp_rank(N,p,z,X,modes)==t:
                    hits[n]["unisolvent"]+=1; ex.append((n,b.proj_orders(H,M),a,X))
                elif b.exact_rank(cy,X,modes)==t:
                    hits[n]["unisolvent"]+=1; ex.append((n,"FS",b.proj_orders(H,M),a,X))
                else:
                    hits[n]["deficient_exact"]+=1
        classif.setdefault(b.proj_orders(H,M),[]).append(ncos)
    divs=[d for d in range(1,M+1) if M%d==0]
    for m in it.product(divs,repeat=3):
        pred=sorted(c for c,sz in b.predicted(m) if sz<=maxsize)
        if sorted(classif.get(m,[]))!=pred: mism.append(m)
    print({"M":M,"subgroups":len(Hs),"inv":inv,"cosets":cos,"mismatch":mism})
    print(hits); print(ex[:4])
if __name__=="__main__":
    run_fast(int(sys.argv[1]),tuple(int(x) for x in sys.argv[2].split(",")))
