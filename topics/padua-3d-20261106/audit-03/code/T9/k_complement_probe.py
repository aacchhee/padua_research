# Auditor feasibility probe (exact integer enumeration; timing MEASURED).
# For degree n: every row-HNF lattice L<=Z^3 with det<=8N and min l1>=2n; compute |cos H| (H = annihilator of L).
# Reports the minimum folded count, to compare with N=binom(n+3,3).  Not a committed result; feasibility evidence only.
import sys, time, math
n=int(sys.argv[1]); N=math.comb(n+3,3); R=2*n-1; DMAX=int(sys.argv[2]) if len(sys.argv)>2 else 8*N
t0=time.process_time()
def short_exists(a,b,c,d,e,f):
    for i in range(-(R//a),R//a+1):
        x=i*a; rx=R-abs(x)
        for j in range((-rx-i*b+d-1)//d,(rx-i*b)//d+1):
            y=i*b+j*d; ry=rx-abs(y)
            if ry<0: continue
            base=i*c+j*e
            for k in range((-ry-base+f-1)//f,(ry-base)//f+1):
                z=base+k*f
                if abs(z)<=ry and (x or y or z): return True
    return False
def fold(a,b,c,d,e,f):
    m=a*d*f
    # adjugate of upper-triangular B (rows): B=[[a,b,c],[0,d,e],[0,0,f]]; B^{-1}=adj/m ; dual generators = columns of adj
    adj=[[d*f,-b*f,b*e-c*d],[0,a*f,-a*e],[0,0,a*d]]
    gens=[tuple(adj[r][col]%m for r in range(3)) for col in range(3)]
    seen={(0,0,0)}; frontier=[(0,0,0)]
    while frontier:
        nxt=[]
        for v in frontier:
            for g in gens:
                w=((v[0]+g[0])%m,(v[1]+g[1])%m,(v[2]+g[2])%m)
                if w not in seen: seen.add(w); nxt.append(w)
        frontier=nxt
    assert len(seen)==m
    return len({tuple(min(x,m-x) for x in v) for v in seen})
best=None; count=0; tested=0; atN=[]
for m in range(1,DMAX+1):
    for a in [x for x in range(1,m+1) if m%x==0]:
        for d in [x for x in range(1,m//a+1) if (m//a)%x==0]:
            f=m//(a*d)
            if f<2*n: continue
            for b in range(d):
                for e in range(f):
                    if short_exists(10**9,0,0,d,e,f): continue
                    for c in range(f):
                        tested+=1
                        if short_exists(a,b,c,d,e,f): continue
                        count+=1; F=fold(a,b,c,d,e,f)
                        if best is None or F<best[0]: best=(F,m,(a,b,c,d,e,f))
                        if F<=N: atN.append((F,m,(a,b,c,d,e,f)))
print({'n':n,'N':N,'det_max':DMAX,'tested':tested,'lattices_min>=2n':count,'min_fold':best,'num_fold<=N':len(atN),'examples_fold<=N':sorted(atN)[:3],'cpu_seconds':round(time.process_time()-t0,1)})
