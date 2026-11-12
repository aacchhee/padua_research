# Check lead: cyclic orbit M=N=20, n=3, z=(1,2,7), phases (30,75,69)/120 turn: nodes cos(2pi(k z_j/20 + phi_j)), k=0..19
from sympy import isprime, primitive_root
z=(1,2,7); ph=(30,75,69)
m=[tuple((6*k*z[j]+ph[j])%120 for j in range(3)) for k in range(20)]
key=lambda r: tuple(min(x,(120-x)%120) for x in r)
print("distinct nodes", len({key(r) for r in m}))
mons=[(i,j,l) for i in range(4) for j in range(4) for l in range(4) if i+j+l<=3]
def rank_mod(M,p):
    M=[r[:] for r in M]; rk=0; cols=len(M[0])
    for c in range(cols):
        piv=next((r for r in range(rk,len(M)) if M[r][c]%p),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]; inv=pow(M[rk][c],p-2,p)
        for r in range(len(M)):
            if r!=rk and M[r][c]%p:
                f=M[r][c]*inv%p; M[r]=[(x-f*y)%p for x,y in zip(M[r],M[rk])]
        rk+=1
    return rk
for p in [241,601,1201]:
    assert isprime(p) and (p-1)%120==0
    g=primitive_root(p); om=pow(g,(p-1)//120,p); i2=pow(2,p-2,p)
    c=lambda x:(pow(om,x,p)+pow(om,(-x)%120,p))*i2%p
    V=[[c(r[0])**a*c(r[1])**b*c(r[2])**d%p for a,b,d in mons] for r in m]
    print(p, "rank", rank_mod(V,p))
