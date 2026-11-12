# Independent (Claude orchestrator) check: 455 stored binary64 points are distinct dyadics in [-1,1]^3
# and Pi_12-unisolvent: integer-scaled monomial matrix has nonzero determinant mod primes (hence over Q).
import json, sys, base64, struct, hashlib
from fractions import Fraction
d=json.load(open(sys.argv[1])); raw=base64.b85decode(d['coordinates_base85'])
assert len(raw)==455*3*8; print("coord sha256", hashlib.sha256(raw).hexdigest())
vals=struct.unpack('<%dd'%(455*3),raw); pts=[tuple(Fraction(v) for v in vals[3*i:3*i+3]) for i in range(455)]
assert len(set(pts))==455 and all(-1<=c<=1 for p in pts for c in p)
den=max(c.denominator for p in pts for c in p); e=den.bit_length()-1; assert den==1<<e
mons=[(a,b,c) for a in range(13) for b in range(13) for c in range(13) if a+b+c<=12]; assert len(mons)==455
def detmod(p):
    inv2e=pow(2,-e,p) if False else None
    M=[[ (int(x*den)%p)**a*(int(y*den)%p)**b*(int(z*den)%p)**c %p for a,b,c in mons] for x,y,z in pts]
    # row scaling by den^(a+b+c) per column is a nonzero factor mod p (p odd); determinant nonzero iff original nonzero
    n=len(M); r=0
    for col in range(n):
        piv=next((i for i in range(r,n) if M[i][col]),None)
        if piv is None: return 0
        M[r],M[piv]=M[piv],M[r]; iv=pow(M[r][col],p-2,p); pr=M[r]
        for i in range(r+1,n):
            f=M[i][col]
            if f: f=f*iv%p; M[i]=[(u-f*v)%p for u,v in zip(M[i],pr)]
        r+=1
    return 1
print("max denominator 2^%d"%e)
for p in [2147483647, 998244353]:
    print(p, "full rank" if detmod(p) else "SINGULAR mod p")
