"""Exact n=2 Bernstein certificate example (auditor-constructed illustration)."""
import sympy as sp
x,y,s,t=sp.symbols('x y s t')
n=2; m=3
X=[sp.cos(sp.pi*j/n) for j in range(n+1)]; Y=[sp.cos(sp.pi*k/m) for k in range(m+1)]
nodes=[(X[j],Y[k]) for j in range(n+1) for k in range(m+1) if (j+k)%2==0]
mons=[x**p*y**q for p in range(n+1) for q in range(n+1-p)]
V=sp.Matrix([[mm.subs({x:a,y:b}) for mm in mons] for (a,b) in nodes])
Vi=V.inv()
card=[sp.expand(sum(Vi[i,l]*mons[i] for i in range(len(mons)))) for l in range(len(nodes))]
print("nodes:",nodes)
print("cardinals:",card)
lam_c=sum(abs(c.subs({x:-1,y:-1})) for c in card); print("Lambda_c(2) =",lam_c, " value at (1,-1):",sum(abs(c.subs({x:1,y:-1})) for c in card))
def bern_coeffs(poly,x0,x1,y0,y1,deg=2):
    p=sp.Poly(sp.expand(poly.subs({x:x0+(x1-x0)*s,y:y0+(y1-y0)*t})),s,t)
    C={}
    for i in range(deg+1):
        for j in range(deg+1):
            # power coefficient a_{pq} -> Bernstein: sum_{p<=i,q<=j} a_pq C(i,p)C(j,q)/(C(deg,p)C(deg,q))
            C[(i,j)]=sum(p.coeff_monomial(s**pp*t**qq)*sp.binomial(i,pp)*sp.binomial(j,qq)/(sp.binomial(deg,pp)*sp.binomial(deg,qq)) for pp in range(i+1) for qq in range(j+1))
    return C
leaves=[(-1,0,-1,0),(0,1,-1,0),(-1,0,0,1),(0,1,0,1)]
for L in leaves:
    sums={ij: sum(abs(bern_coeffs(c,*L)[ij]) for c in card) for ij in [(i,j) for i in range(3) for j in range(3)]}
    print("leaf",L, {k:str(v) for k,v in sums.items()})
