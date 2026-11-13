import math
def nodes(n,z):
    N=math.comb(n+3,3); M,L=2*N,4*N
    return L,sorted({tuple(min(v,L-v) for v in (((2*k+1)*a)%L for a in z)) for k in range(M)})
L,A=nodes(7,(1,17,212)); _,B=nodes(7,(1,17,28))
H=L//2
refl={ (u1,u2,H-u3) for (u1,u2,u3) in A}
print(len(A),len(B),refl==set(B))
# orbit check: the 8 labels under coordinate permutations/sign reflections normalized to first=1
orb=[(1,17,28),(1,17,212),(1,28,223),(1,44,113),(1,44,127),(1,113,196),(1,127,196),(1,212,223)]
def canon_set(z):
    L,S=nodes(7,z); return frozenset(S)
import itertools
base=set(B)
for z in orb:
    _,S=nodes(7,z)
    ok=False
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([0,1],repeat=3):
            T={tuple((H-p[perm[i]]) if signs[i] else p[perm[i]] for i in range(3)) for p in S}
            if T==base: ok=True
    print(z,ok)
print(min(orb))
