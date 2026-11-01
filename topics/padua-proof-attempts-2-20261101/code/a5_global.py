"""Additional exact degree3 value/flat-pattern certificate for A4(d)."""
from a5_arithmetic import *

def roundup(z,den=10**6):return F(-((-z*den).numerator//(-z*den).denominator),den)
def rounddown(z,den=10**6):return F((z*den).numerator//(z*den).denominator,den)
def encbound(Z):return[str(rounddown(Z.lo)),str(roundup(Z.hi))]
def global_certificate(cert):
 _,L=cardinals();flat=[];ivals=[];evals=[]
 for rec in cert['patterns']:
  mask=rec['mask'];P=sum((1 if(mask>>b)&1 else-1)*L[b]for b in range(10))
  if rec['kind']=='flat':
   axis=0 if not P.diff(y)else 1;panels=[]
   for k in range(32):
    T=I(F(k,16)-1,F(k+1,16)-1)
    Z=evalpoly(P,T,iv(0))if axis==0 else evalpoly(P,iv(0),T)
    upper=roundup(Z.hi);assert upper<3
    panels.append({'interval':T.strings(),'upper':str(upper)})
   flat.append({'mask':mask,'axis':axis,'panels':panels})
  else:
   # This fact is also proved by nonzero residualresultants and constantg.
   assert sp.Poly(sum((sp.Rational(a)+sp.Rational(b)*rt)*x**i*y**j for i,j,a,b in rec['g']),x,y,domain=K).total_degree()==0
   for rr in rec.get('pairs',[]):
    if rr['code']=='root':
     X,Y=[I(*map(F,z))for z in rr['box']]
     Z=evalpoly(P,X,Y);bound=encbound(Z);assert F(bound[1])<F(15,4)
     ivals.append({'id':rr['id'],'enclosure':bound})
 for edge in cert['edges']:
  axis,side=edge['axis'],edge['side'];normal=(x,y)[axis]
  for rec in edge['patterns']:
   for rr in rec.get('points',[]):
    if rr['code']=='root':
     mask=rr['fullmask'];P=sum((1 if(mask>>b)&1 else-1)*L[b]for b in range(10))
     T=I(*map(F,rr['interval']));q=P.as_expr().subs(normal,side)
     Z=evalpoly(q,iv(side),T)if axis==0 else evalpoly(q,T,iv(side))
     bound=encbound(Z);assert F(bound[1])<F(15,4)
     evals.append({'id':rr['id'],'enclosure':bound})
 C=sp.Rational(17,6)+sp.Rational(2,3)*rt
 assert evalpoly(C,iv(0),iv(0)).lo>F(15,4)
 return{'flat_bound':'3','cut':'15/4','flat':flat,'interior_values':sorted(ivals,key=lambda z:z['id']),'edge_values':sorted(evals,key=lambda z:z['id']),'corner_value':encfield(C),'part1_representatives':[{'edge_id':2,'sigma':1},{'edge_id':3,'sigma':-1}]}
