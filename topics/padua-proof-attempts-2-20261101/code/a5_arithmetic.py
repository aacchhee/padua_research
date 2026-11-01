"""Developer exact algebra and outward rational interval arithmetic for A5."""
from dataclasses import dataclass
from fractions import Fraction as F
import sympy as sp
from math import isqrt
x,y=sp.symbols('x y'); rt=sp.sqrt(2); K=sp.QQ.algebraic_field(rt)
@dataclass(frozen=True)
class I:
 lo:F; hi:F
 def __post_init__(self):
  object.__setattr__(self,'lo',F(self.lo));object.__setattr__(self,'hi',F(self.hi));assert self.lo<=self.hi
 def __add__(self,z):
  z=iv(z);return I(self.lo+z.lo,self.hi+z.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,z):return self+-iv(z)
 def __rsub__(self,z):return iv(z)+-self
 def __mul__(self,z):
  z=iv(z);v=[a*b for a in(self.lo,self.hi)for b in(z.lo,z.hi)];return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,z):
  z=iv(z);assert not z.lo<=0<=z.hi;return self*I(1/z.hi,1/z.lo)
 def __pow__(self,k):
  assert k>=0
  if k==0:return iv(1)
  if not k%2 and self.lo<=0<=self.hi:return I(0,max(abs(self.lo),abs(self.hi))**k)
  vals=[self.lo**k,self.hi**k];return I(min(vals),max(vals))
 def absmax(self):return max(abs(self.lo),abs(self.hi))
 def contains0(self):return self.lo<=0<=self.hi
 def strings(self):return[str(self.lo),str(self.hi)]
def iv(z):return z if isinstance(z,I)else I(F(z),F(z))
# Verified rational radical enclosure, narrower than every ordinary root box.
rlo=F(isqrt(2*10**126),10**63)
assert rlo*rlo<2<(rlo+F(1,10**63))**2
RI=I(rlo,rlo+F(1,10**63))
def coeffpair(c):
 c=sp.expand(c);a=c.coeff(rt,0);b=c.coeff(rt,1);assert sp.expand(c-a-b*rt)==0
 return F(int(a.p),int(a.q)),F(int(b.p),int(b.q))
def encfield(c):return list(map(str,coeffpair(c)))
def decfield(ab):return sp.Rational(ab[0])+sp.Rational(ab[1])*rt
def encpoly(p):
 p=sp.Poly(p,x,y,domain=K);return[[i,j,*encfield(c)]for(i,j),c in p.terms()]
def polyterms(p):
 return[(i,j,iv(a)+iv(b)*RI)for(i,j),c in sp.Poly(p,x,y,domain=K).terms()for a,b in[coeffpair(c)]]
def evalpoly(p,X,Y):
 if not isinstance(p,list):p=polyterms(p)
 return sum((c*X**i*Y**j for i,j,c in p),iv(0))
def cardinals():
 mons=[x**a*y**(d-a)for d in range(4)for a in range(d,-1,-1)]
 nodes=[(sp.cos(sp.pi*j/3),sp.cos(sp.pi*k/4))for j in range(4)for k in range(5)if(j+k)%2==0]
 V=sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix([[m.subs({x:u,y:v})for m in mons]for u,v in nodes])).convert_to(K)
 inv=V.inv().to_Matrix()
 assert V.to_Matrix()*inv==sp.eye(10)
 return nodes,[sp.Poly(sum(mons[q]*inv[q,b]for q in range(10)),x,y,domain=K)for b in range(10)]
def rational_norm(expr,t):
 p=sp.Poly(expr,t,domain=K)
 norm=sp.Poly(sp.expand(p.as_expr()*p.as_expr().xreplace({rt:-rt})),t,domain=sp.QQ)
 assert norm
 return norm.sqf_part().clear_denoms()[1].primitive()[1]
def root_intervals(p,eps=sp.Rational(1,10**20)):
 return[I(F(int(a.p),int(a.q)),F(int(b.p),int(b.q)))for(a,b),m in p.intervals(eps=eps)]
def cmatrix(H,c):
 # Exact field inverse evaluated at rational midpoint; use rational nearest with denominator1e12.
 hc=H.subs({x:sp.Rational(c[0].numerator,c[0].denominator),y:sp.Rational(c[1].numerator,c[1].denominator)})
 if hc.det()==0:return None
 inv=hc.inv();C=[]
 for row in inv.tolist():
  values=[]
  for q in row:
   normal=K.to_sympy(K.convert(q))
   a,b=coeffpair(normal);bound=iv(a)+iv(b)*RI
   values.append(((bound.lo+bound.hi)/2).limit_denominator(10**12))
  C.append(values)
 return C
def contraction(Hterms,C,X,Y):
 H=[[evalpoly(Hterms[i][j],X,Y)for j in range(2)]for i in range(2)]
 E=[[iv(int(i==j))-sum((C[i][k]*H[k][j]for k in range(2)),iv(0))for j in range(2)]for i in range(2)]
 return max(sum(E[i][j].absmax()for j in range(2))for i in range(2)),E
