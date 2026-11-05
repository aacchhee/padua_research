#!/usr/bin/env python3
"""Independent exact finite checks for scalar plateau, aliases, and torus lift."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys,time,platform

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def convolution(x,y):
    z={}
    for a,v in x.items():
        for b,w in y.items():z[a+b]=z.get(a+b,F(0))+v*w
    return z

def main():
    tick=time.monotonic(); pairs=0; frequencies=0; lift_pairs=0; alias_tests=0
    for m in range(1,25):
        # Angles represented in units of pi, hence period two.
        gamma=[(F(j,m),F(k,m+1)) for j in range(2*m) for k in range(2*(m+1)) if (j+k)%2==0]
        lifts=set()
        for t,s in gamma:
            u,v=(t+s)/2,(t-s)/2
            lifts.add((u%2,v%2));lifts.add(((u+1)%2,(v+1)%2))
        assert len(lifts)==4*m*(m+1)
        if m<=8:
            lifts=list(lifts); a=F(1,2*(m+1))
            for i,z in enumerate(lifts):
                for w in lifts[:i]:
                    du=abs(z[0]-w[0]);du=min(du,2-du)
                    dv=abs(z[1]-w[1]);dv=min(dv,2-dv)
                    assert max(du,dv)>=a
                    lift_pairs+=1
        for n in range(m):
            L=(m-n+3)//4;M=n+2*L-2
            f={r:F(L-abs(r),L) for r in range(-L+1,L)}
            coeff={k:v/L**2 for k,v in convolution({k:F(1) for k in range(-M,M+1)},convolution(f,f)).items()}
            assert all(coeff.get(k,0)==1 for k in range(-n,n+1))
            assert all(abs(k)<=m-1 for k,v in coeff.items() if v)
            for a in range(-m,m+1):
                for b in range(-m,m+1):
                    value=coeff.get(a+b,0)*coeff.get(a-b,0)
                    if abs(a)+abs(b)<=n:assert value==1
                    if abs(a)+abs(b)>=m:assert value==0
                    frequencies+=1
            if m<=10:
                source=[(a,b) for a in range(-n,n+1) for b in range(-n,n+1) if abs(a)+abs(b)<=n]
                target=[(a,b) for a in range(-m+1,m) for b in range(-m+1,m) if coeff.get(a+b,0)*coeff.get(a-b,0)]
                for a,b in source:
                    for c,d in target:
                        dx,dy=a-c,b-d
                        alias=(dx%(2*m)==0 and dy%(2*(m+1))==0) or (dx%(2*m)==m and dy%(2*(m+1))==m+1)
                        assert not alias or (a,b)==(c,d)
                        alias_tests+=1
            pairs+=1
    root=Path(__file__).resolve().parents[3]
    theory=Path(__file__).resolve().parent.parent/'theory/f3-smooth-diamond-reference.md'
    out={'status':'Exact rational finite regression, not an all-m computer proof','pass':True,
         'rules_input_sha':'83cf6f1ee244f2e72057332a7ec04ee74db1f0de','command':sys.argv,'python':sys.version,'platform':platform.platform(),
         'inputs':{str(p.relative_to(root)):sha(p) for p in [Path(__file__).resolve(),theory]},
         'scalar_and_diamond_scope':'m=1..24, every n=0..m-1','degree_pairs':pairs,'frequency_tests':frequencies,
         'lift_scope':'counts m=1..24; all pairwise torus separations m=1..8','lift_pair_tests':lift_pairs,
         'alias_scope':'m=1..10, every n=0..m-1, every input/output supported frequency','alias_pair_tests':alias_tests,
         'seconds':time.monotonic()-tick}
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
