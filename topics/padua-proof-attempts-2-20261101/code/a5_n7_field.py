"""Exact degree-seven tensor field, principal embedding, and cardinal kernel.

Tensor order a^i*b^j, i outer0..2,j inner0..3. a³-a²-2a+1=0,
b⁴-4b²+2=0; a,b are each the largest real root. No floats.
"""
import sympy as s
from fractions import Fraction as F
from math import lcm
import json,time,argparse,sys
from functools import lru_cache
x,y,t=s.symbols('x y t');NDEG=7;N=36;PREC=128;S=1<<PREC

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

a=2*s.cos(s.pi/7);b=2*s.cos(s.pi/8);K=s.QQ.algebraic_field(a,b)
ka,kb=K.convert(a),K.convert(b)
assert ka+kb==K.unit
F12=s.Poly(t**12-4*t**11-14*t**10+64*t**9+39*t**8-292*t**7+42*t**6+436*t**5-166*t**4-172*t**3+40*t**2+24*t+1,t)
assert K.mod.to_list()==F12.all_coeffs() and F12.is_irreducible
assert ka**3-ka**2-2*ka+K.one==K.zero and kb**4-4*kb**2+2*K.one==K.zero
BASIS=[ka**i*kb**j for i in range(3)for j in range(4)]
def native_vector(z):
 z=K.convert(z);v=[s.Rational(str(q))for q in reversed(z.to_list())];return v+[s.Rational(0)]*(12-len(v))
M=s.Matrix.hstack(*(s.Matrix(native_vector(z))for z in BASIS));MI=M.inv();assert M*MI==s.eye(12)
TRANS=tuple(tuple(F(str(q))for q in row)for row in MI.tolist())
def kparts(z):
 v=[F(str(q))for q in reversed(K.convert(z).to_list())];v +=[F(0)]*(12-len(v))
 return tuple(sum((TRANS[i][j]*v[j]for j in range(12)if TRANS[i][j] and v[j]),F(0))for i in range(12))
def decode(parts):return sum((K.convert(s.Rational(str(q)))*z for q,z in zip(parts,BASIS)),K.zero)
for j,z in enumerate(BASIS):assert kparts(z)==tuple(F(int(i==j))for i in range(12))
assert all(decode(kparts(K.unit**i))==K.unit**i for i in range(12))
PA=s.Poly(t**3-t**2-2*t+1,t);PB=s.Poly(t**4-4*t**2+2,t)
UA=s.Poly(s.chebyshevu(6,t/2),t);UB=s.Poly(s.chebyshevu(7,t/2),t)
assert UA.rem(PA).is_zero and UB.rem(PB).is_zero
assert UA.count_roots(s.Rational(9,5),s.Rational(181,100))==1 and UA.count_roots(s.Rational(181,100),s.oo)==0
assert UB.count_roots(s.Rational(184,100),s.Rational(185,100))==1 and UB.count_roots(s.Rational(185,100),s.oo)==0

def bracket(poly,lo,hi):
 lo=rat(lo)[0];hi=rat(hi)[1];coeff=list(map(int,poly.all_coeffs()));degree=poly.degree()
 def at(q):return sum(c*q**(degree-i)*S**i for i,c in enumerate(coeff))
 assert at(lo)<0<at(hi)
 while hi-lo>1:
  mid=(lo+hi)//2
  if at(mid)<0:lo=mid
  else:hi=mid
 assert at(lo)<0<at(hi)
 return(lo,hi)
AI=bracket(PA,F(9,5),F(181,100));BI=bracket(PB,F(184,100),F(185,100))
BINTERVALS=[mul(power(AI,i),power(BI,j))for i in range(3)for j in range(4)]
def cparts(parts):return asum(mul(rat(q),z)for q,z in zip(parts,BINTERVALS)if q)
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
 X=cheb_values(ka/2,7);Y=cheb_values(kb/2,8)
 assert X[0]==K.one and X[-1]==-K.one and Y[0]==K.one and Y[-1]==-K.one
 nodes=[(X[j],Y[k],j,k)for j in range(8)for k in range(9)if(j+k)%2==0]
 CT=[s.Poly(s.chebyshevt(i,x),x).as_dict()for i in range(8)]
 L=[]
 for u,v,j,k in nodes:
  ux=cheb_values(u,7);vy=cheb_values(v,7);weight=K(s.QQ(2,56))
  if j in(0,7):weight/=2
  if k in(0,8):weight/=2
  coeff={}
  for p in range(8):
   for q in range(8-p):
    cc=weight*(1 if p==0 else 2)*(1 if q==0 else 2)*ux[p]*vy[q]
    if(p,q)==(7,0):cc-=weight*ux[7]
    for(ix,),cx in CT[p].items():
     for(iy,),cy in CT[q].items():coeff[ix,iy]=coeff.get((ix,iy),K.zero)+cc*int(cx)*int(cy)
  coeff={ij:c for ij,c in coeff.items()if c!=K.zero};L.append(s.Poly.from_dict(coeff,(x,y),domain=K))
 if check:
  dsum={}
  for q in L:
   for ij,c in q.rep.to_dict().items():dsum[ij]=dsum.get(ij,K.zero)+c
  assert all(v==(K.one if ij==(0,0)else K.zero)for ij,v in dsum.items())
  for ni,(u,v,j,k)in enumerate(nodes):
   up=[u**i for i in range(8)];vp=[v**i for i in range(8)]
   for li,q in enumerate(L):assert sum((c*up[i]*vp[j]for(i,j),c in q.rep.to_dict().items()),K.zero)==(K.one if ni==li else K.zero)
 return nodes,L

def native_eval(p,u,v):
 ku,kv=K.convert(u),K.convert(v)
 up=[ku**i for i in range(8)];vp=[kv**i for i in range(8)]
 return sum((c*up[i]*vp[j]for(i,j),c in p.rep.to_dict().items()),K.zero)

@lru_cache(None)
def terms(p):
 if not isinstance(p,s.Poly):p=s.Poly(p,x,y,domain=K)
 if p.gens==(x,y):return[(i,j,kfield(c))for(i,j),c in p.rep.to_dict().items()if c!=K.zero]
 axis=0 if p.gens==(x,)else 1 if p.gens==(y,)else None
 assert axis is not None,p.gens
 return[(i if axis==0 else 0,i if axis==1 else 0,kfield(c))for(i,),c in p.rep.to_dict().items()if c!=K.zero]
def evaluate(p,X,Y):
 xp=[power(X,i)for i in range(8)];yp=[power(Y,i)for i in range(8)]
 return asum(mul(c,mul(xp[i],yp[j]))for i,j,c in p)
def centered(p,px,py,X,Y):
 cx=sum(X)//2;cy=sum(Y)//2
 z=add(evaluate(p,(cx,cx),(cy,cy)),add(mul(evaluate(px,X,Y),(X[0]-cx,X[1]-cx)),mul(evaluate(py,X,Y),(Y[0]-cy,Y[1]-cy))))
 w=evaluate(p,X,Y);return(max(z[0],w[0]),min(z[1],w[1]))
def embedding_record():return{'basis':'a^i*b^j, i=0,1,2 then j=0,1,2,3','a_minpoly':[1,-1,-2,1],'b_minpoly':[1,0,-4,0,2],'a_interval':[str(F(z,S))for z in AI],'b_interval':[str(F(z,S))for z in BI],'a_outer_interval':['9/5','181/100'],'b_outer_interval':['46/25','37/20'],'a_U6_count_inside':1,'a_U6_count_above':0,'b_U7_count_inside':1,'b_U7_count_above':0,'native_minpoly':[str(q)for q in K.mod.to_list()],'native_to_tensor':[[str(q)for q in row]for row in TRANS]}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--no-cardinals',action='store_true');args=ap.parse_args();start=time.time();out={'format':'a5-n7-field-v1','n':7,'precision':PREC,'embedding':embedding_record(),'backend':str(s.external.gmpy.GROUND_TYPES),'python':sys.version,'sympy':s.__version__}
 if not args.no_cardinals:
  nodes,L=construct();out.update(nodes=len(nodes),cardinals=len(L),exact_interpolation=True,partition_of_unity=True,coefficient_count=sum(len(q.terms())for q in L))
 out['seconds_after_import']=time.time()-start;open(args.output,'w').write(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps(out),flush=True)
