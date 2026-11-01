"""Exact n=3 signed-gradient shape diagnostics; no count certification."""
import json,time,itertools,sys
from collections import Counter
import sympy as s
x,y=s.symbols('x y'); rt=s.sqrt(2); K=s.QQ.algebraic_field(rt)
mons=[x**a*y**(d-a) for d in range(4) for a in range(d,-1,-1)]
nodes=[(s.cos(s.pi*j/3),s.cos(s.pi*k/4)) for j in range(4) for k in range(5) if(j+k)%2==0]
V=s.polys.matrices.DomainMatrix.from_Matrix(s.Matrix([[m.subs({x:u,y:v}) for m in mons] for u,v in nodes])).convert_to(K)
inv=V.inv().to_Matrix()
L=[s.Poly(sum(mons[q]*inv[q,b] for q in range(10)),x,y,domain=K) for b in range(10)]
print('cardinals', [str(s.factor(p.as_expr())) for p in L],flush=True)
stats=Counter();t=time.time()
for bits in range(1024):
 p=sum((1 if(bits>>i)&1 else -1)*L[i] for i in range(10))
 A,B=p.diff(x),p.diff(y)
 if not A or not B: stats['one_zero']+=1;continue
 g=s.gcd(A,B);a=A.exquo(g);b=B.exquo(g)
 stats[('gdegree',g.total_degree())]+=1
 if a.total_degree()==0 or b.total_degree()==0: stats['unit_residual']+=1;continue
 rx=s.resultant(a.as_expr(),b.as_expr(),y)
 ry=s.resultant(a.as_expr(),b.as_expr(),x)
 stats[('resultant_degrees',s.degree(rx,x),s.degree(ry,y))]+=1
 if bits%128==0: print('progress',bits,time.time()-t,flush=True)
print('seconds',time.time()-t)
print(dict((str(k),v)for k,v in stats.items()))
