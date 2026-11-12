import sys, itertools as it, math
from collections import Counter
import bf_cosets as b
e=lambda q:q//2+1; o=lambda q:(q+1)//2
def lev(m,eps): return m//2+1 if eps==0 else (m//2 if m%2==0 else (m+1)//2)
CODES={"0":(),"p12":(0,1),"p13":(0,2),"p23":(1,2),"t":(0,1,2),"pl":(0,1,2)}
def classes(name):
    if name=="0": return [[()]]
    if name[0]=="p" and name!="pl": return [[(0,0),(1,1)],[(0,1),(1,0)]]
    if name=="t": return [[p for p in it.product((0,1),repeat=3) if sum(p)%2==s] for s in (0,1)]
    return [[p,tuple(1-x for x in p)] for p in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]]
def dim(name): return {"0":0,"t":1,"pl":2}.get(name,1)
M=int(sys.argv[1]); cap=160; N=2*M
form=Counter()
divs=[d for d in range(1,M+1) if M%d==0]
for m in it.product(divs,repeat=3):
    for name,act in CODES.items():
        if any(m[j]%2 for j in act): continue
        if math.prod(m)//2**dim(name)>cap: continue
        inact=[j for j in range(3) if j not in act]
        for C in classes(name):
            for eps in it.product((0,1),repeat=len(inact)):
                c=sum(math.prod((o if p[k] else e)(m[j]//2) for k,j in enumerate(act)) for p in C)
                c*=math.prod(lev(m[j],ee) for j,ee in zip(inact,eps))
                form[(m,c)]+=1
brute=Counter()
for H in b.subgroups(M,cap):
    if not all(b.negj(h,j,M) in H for h in H for j in range(3)): continue
    P=[tuple(2*c for c in h) for h in H]; Pset=set(P)
    S=[[aj for aj in range(N) if tuple((2*aj)%N if k==j else 0 for k in range(3)) in Pset] for j in range(3)]
    seen=set()
    for a in it.product(*S):
        A=frozenset(tuple((ai+pi)%N for ai,pi in zip(a,pp)) for pp in P)
        if min(A) in seen: continue
        seen.add(min(A))
        X={tuple(min(c,N-c) for c in u) for u in A}
        brute[(b.proj_orders(H,M),len(X))]+=1
print("M",M,"formula cosets",sum(form.values()),"brute cosets",sum(brute.values()),"identical (orders,|X|) multisets:",form==brute)
