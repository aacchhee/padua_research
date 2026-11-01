"""Exact degree-twelve tensor field for degree-eight Padua nodes and independently checkable principal embedding.

Basis a^i*b^j, 0<=i<4, 0<=j<3; a^4-4a^2+2=0, b^3-3b-1=0.
The real embedding maps a and b to their verified largest real roots.
No floating evaluation is used. Cardinal coefficients use corrected Chebyshev
kernel; direct exact interpolation and partition checks are performed.
"""
import sympy as s
from fractions import Fraction as F
from math import isqrt,lcm
import json,time,argparse,sys
from functools import lru_cache
x,y,t=s.symbols('x y t');NDEG=8;N=45;DIM=12;PREC=160;S=1<<PREC

def rat(q):
 q=F(q);return(q.numerator*S//q.denominator,-((-q.numerator*S)//q.denominator))
def add(u,v):return(u[0]+v[0],u[1]+v[1])
def neg(u):return(-u[1],-u[0])
def scale(u,k):return(u[0]*k,u[1]*k)if k>=0 else(u[1]*k,u[0]*k)
def mul(u,v):
 z=[a*b for a in u for b in v];return(min(z)//S,-((-max(z))//S))
def power(u,k):
 if not k:return(S,S)
 z=[u[0]**k,u[1]**k];d=S**(k-1)
 return(0 if not k%2 and u[0]<=0<=u[1]else min(z)//d,-((-max(z))//d))
def asum(v):
 lo=hi=0
 for z in v:lo+=z[0];hi+=z[1]
 return(lo,hi)
def sign(u):return 1 if u[0]>0 else -1 if u[1]<0 else 0

a=s.sqrt(2+s.sqrt(2));b=2*s.cos(s.pi/9);K=s.QQ.algebraic_field(a,b)
ka,kb=K.convert(a),K.convert(b)
assert ka+kb==K.unit
assert len(K.mod.to_list())-1==DIM
assert ka**4-4*ka**2+K(2)==K.zero and kb**3-3*kb-K.one==K.zero
BASIS=[ka**i*kb**j for i in range(4)for j in range(3)]
def native_vector(z):
 z=K.convert(z);v=[s.Rational(str(q))for q in reversed(z.to_list())];return v+[s.Rational(0)]*(DIM-len(v))
M=s.Matrix.hstack(*(s.Matrix(native_vector(z))for z in BASIS));MI=M.inv();assert M*MI==s.eye(DIM) and MI*M==s.eye(DIM)
TRANS=tuple(tuple(F(str(q))for q in row)for row in MI.tolist())
def kparts(z):
 v=[F(str(q))for q in reversed(K.convert(z).to_list())];v +=[F(0)]*(DIM-len(v))
 return tuple(sum((TRANS[i][j]*v[j]for j in range(DIM)),F(0))for i in range(DIM))
def decode(parts):return sum((K.convert(s.Rational(str(q)))*z for q,z in zip(parts,BASIS)),K.zero)
for j,z in enumerate(BASIS):assert kparts(z)==tuple(F(int(i==j))for i in range(DIM))
assert all(decode(kparts(K.unit**i))==K.unit**i for i in range(DIM))
PA=s.Poly(t**4-4*t*t+2,t);PB=s.Poly(t**3-3*t-1,t)
UA=s.Poly(s.chebyshevu(7,t/2),t);UB=s.Poly(s.chebyshevu(8,t/2),t)
assert UA.rem(PA).is_zero and UB.rem(PB).is_zero
assert UA.count_roots(s.Rational(184,100),s.Rational(185,100))==1 and UA.count_roots(s.Rational(185,100),s.oo)==0
assert UB.count_roots(s.Rational(187,100),s.Rational(188,100))==1 and UB.count_roots(s.Rational(188,100),s.oo)==0
def isolate_dyadic(poly,lower,upper):
 lo=lower.numerator*S//lower.denominator;hi=-((-upper.numerator*S)//upper.denominator)
 def peval(q):
  degree=poly.degree();return sum(int(c)*q**(degree-i)*S**i for i,c in enumerate(poly.all_coeffs()))
 assert peval(lo)<0<peval(hi)
 while hi-lo>1:
  mid=(lo+hi)//2
  if peval(mid)<0:lo=mid
  else:hi=mid
 assert peval(lo)<0<peval(hi)
 return(lo,hi)
AI=isolate_dyadic(PA,F(184,100),F(185,100));BI=isolate_dyadic(PB,F(187,100),F(188,100))
BINTERVALS=[mul(power(AI,i),power(BI,j))for i in range(4)for j in range(3)]
def cparts(parts):return asum(mul(rat(q),z)for q,z in zip(parts,BINTERVALS))
def kfield(z):return cparts(kparts(z))
def ksign(z):
 z=K.convert(z)
 if z==K.zero:return 0
 sg=sign(kfield(z))
 if not sg:raise ArithmeticError('principal embedding precision cannot resolve nonzero field sign')
 return sg
def encfield(z):return[str(q)for q in kparts(z)]
def cfield(expr):return kfield(K.convert(expr))
def encbox(Q):return[[str(F(z,S))for z in I]for I in Q]
def cheb_values(z,n):
 out=[K.one,z]
 for i in range(2,n+1):out.append(2*z*out[-1]-out[-2])
 return out[:n+1]
def construct(check=True):
 X=cheb_values(ka/2,8);Y=cheb_values(kb/2,9)
 assert X[0]==K.one and X[-1]==-K.one and Y[0]==K.one and Y[-1]==-K.one
 nodes=[(X[j],Y[k],j,k)for j in range(9)for k in range(10)if(j+k)%2==0]
 assert len(nodes)==N
 CT=[s.Poly(s.chebyshevt(i,x),x).as_dict()for i in range(9)]
 L=[]
 for u,v,j,k in nodes:
  ux=cheb_values(u,8);vy=cheb_values(v,8);weight=K(s.QQ(2,72))
  if j in(0,8):weight/=2
  if k in(0,9):weight/=2
  coeff={}
  for p in range(9):
   for q in range(9-p):
    cc=weight*(1 if p==0 else 2)*(1 if q==0 else 2)*ux[p]*vy[q]
    if(p,q)==(8,0):cc-=weight*ux[8]
    for(ix,),cx in CT[p].items():
     for(iy,),cy in CT[q].items():coeff[ix,iy]=coeff.get((ix,iy),K.zero)+cc*int(cx)*int(cy)
  coeff={ij:c for ij,c in coeff.items()if c!=K.zero};L.append(s.Poly.from_dict(coeff,(x,y),domain=K))
 if check:
  dsum={}
  for q in L:
   for ij,c in q.rep.to_dict().items():dsum[ij]=dsum.get(ij,K.zero)+c
  assert all(v==(K.one if ij==(0,0)else K.zero)for ij,v in dsum.items())
  for ni,(u,v,j,k)in enumerate(nodes):
   up=[u**i for i in range(9)];vp=[v**i for i in range(9)]
   for li,q in enumerate(L):assert sum((c*up[i]*vp[j]for(i,j),c in q.rep.to_dict().items()),K.zero)==(K.one if ni==li else K.zero)
 return nodes,L

@lru_cache(None)
def terms(p):
 if not isinstance(p,s.Poly):p=s.Poly(p,x,y,domain=K)
 if p.gens==(x,y):return[(i,j,kfield(c))for(i,j),c in p.rep.to_dict().items()if c!=K.zero]
 axis=0 if p.gens==(x,)else 1 if p.gens==(y,)else None
 assert axis is not None,p.gens
 return[(i if axis==0 else 0,i if axis==1 else 0,kfield(c))for(i,),c in p.rep.to_dict().items()if c!=K.zero]
def evaluate(p,X,Y):
 xp=[power(X,i)for i in range(9)];yp=[power(Y,i)for i in range(9)]
 return asum(mul(c,mul(xp[i],yp[j]))for i,j,c in p)
def centered(p,px,py,X,Y):
 cx=sum(X)//2;cy=sum(Y)//2
 z=add(evaluate(p,(cx,cx),(cy,cy)),add(mul(evaluate(px,X,Y),(X[0]-cx,X[1]-cx)),mul(evaluate(py,X,Y),(Y[0]-cy,Y[1]-cy))))
 w=evaluate(p,X,Y);return(max(z[0],w[0]),min(z[1],w[1]))
def embedding_record():return{'basis':'a^i*b^j, i=0,1,2,3 then j=0,1,2','a_minpoly':[1,0,-4,0,2],'b_minpoly':[1,0,-3,-1],'a_interval':[str(F(z,S))for z in AI],'b_interval':[str(F(z,S))for z in BI],'a_outer_interval':['46/25','37/20'],'b_outer_interval':['187/100','47/25'],'a_U7_count_inside':1,'a_U7_count_above':0,'b_U8_count_inside':1,'b_U8_count_above':0,'native_minpoly':[str(q)for q in K.mod.to_list()],'native_to_tensor':[[str(q)for q in row]for row in TRANS]}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--no-cardinals',action='store_true');args=ap.parse_args();start=time.time();out={'format':'a5-n8-field-v1','n':8,'precision':PREC,'embedding':embedding_record(),'backend':str(s.external.gmpy.GROUND_TYPES),'python':sys.version,'sympy':s.__version__}
 if not args.no_cardinals:
  nodes,L=construct();out.update(nodes=len(nodes),cardinals=len(L),exact_interpolation=True,partition_of_unity=True,coefficient_count=sum(len(q.terms())for q in L))
 out['seconds_after_import']=time.time()-start;open(args.output,'w').write(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps(out),flush=True)
