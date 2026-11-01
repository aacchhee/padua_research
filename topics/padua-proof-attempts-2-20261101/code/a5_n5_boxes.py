"""Exact outward fixed-dyadic diagnostic of complete spatial A5 enumeration.

No claimed count; unresolved leaves remain explicit.  Never imports old certifier.
"""
import argparse, json, time, sys, gzip
from collections import Counter
from fractions import Fraction as F
from math import isqrt,lcm
from functools import lru_cache
import sympy as s
x,y=s.symbols('x y');r3=s.sqrt(3);r5=s.sqrt(5);r15=s.sqrt(15)
K=s.QQ.algebraic_field(r3,r5);PREC=96;S=1<<PREC

def rat(q):
 q=F(q);return(q.numerator*S//q.denominator,-((-q.numerator*S)//q.denominator))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[1],-a[0])
def scale(a,n):return(a[0]*n,a[1]*n)if n>=0 else(a[1]*n,a[0]*n)
def mul(a,b):
 z=[u*v for u in a for v in b];return(min(z)//S,-((-max(z))//S))
def power(a,n):
 if not n:return(S,S)
 if n%2:return(a[0]**n//S**(n-1),-((-a[1]**n)//S**(n-1)))
 z=[a[0]**n,a[1]**n];return(0 if a[0]<=0<=a[1]else min(z)//S**(n-1),-((-max(z))//S**(n-1)))
def asum(xs):
 lo=hi=0
 for z in xs:lo+=z[0];hi+=z[1]
 return(lo,hi)
def fieldparts(c):
 c=s.expand(c);parts=[c.coeff(z)for z in(r3,r5,r15)];a=s.expand(c-sum(parts[i]*z for i,z in enumerate((r3,r5,r15))))
 assert a.is_Rational and all(q.is_Rational for q in parts),(c,a,parts)
 return tuple(F(str(q))for q in(a,*parts))
def cparts(parts):
 out=rat(parts[0])
 for q,n in zip(parts[1:],(3,5,15)):
  rt=isqrt(n*S*S);assert rt*rt<n*S*S<(rt+1)*(rt+1)
  out=add(out,mul(rat(q),(rt,rt+1)))
 return out
def cfield(c):return cparts(fieldparts(c))
def encfield(c):return[str(q)for q in fieldparts(c)]

def construct():
 nodes=[(s.cos(s.pi*j/5),s.cos(s.pi*k/6),j,k)for j in range(6)for k in range(7)if(j+k)%2==0]
 mons=[x**a*y**(d-a)for d in range(6)for a in range(d,-1,-1)]
 V=s.polys.matrices.DomainMatrix.from_Matrix(s.Matrix([[m.subs({x:u,y:v})for m in mons]for u,v,j,k in nodes])).convert_to(K)
 VI=V.inv();assert (V*VI).to_Matrix()==s.eye(21);inv=VI.to_Matrix()
 L=[s.Poly(sum(mons[q]*inv[q,b]for q in range(21)),x,y,domain=K)for b in range(21)]
 # Equality, not approximate evaluation, checks partition of unity.
 assert sum(L).as_expr()==1
 return nodes,L

def terms(p):return[(i,j,cfield(c))for(i,j),c in s.Poly(p,x,y,domain=K).terms()if c]
def evaluate(p,X,Y):
 xp=[power(X,i)for i in range(6)];yp=[power(Y,i)for i in range(6)]
 return asum(mul(c,mul(xp[i],yp[j]))for i,j,c in p)
def centered(p,px,py,X,Y):
 cx=(X[0]+X[1])//2;cy=(Y[0]+Y[1])//2
 a=add(evaluate(p,(cx,cx),(cy,cy)),add(mul(evaluate(px,X,Y),(X[0]-cx,X[1]-cx)),mul(evaluate(py,X,Y),(Y[0]-cy,Y[1]-cy))))
 b=evaluate(p,X,Y);return(max(a[0],b[0]),min(a[1],b[1]))
def sign(v):return 1 if v[0]>0 else -1 if v[1]<0 else 0

def encbox(Q):return[[str(F(v,S))for v in Z]for Z in Q]
def hull(Q,R):return[(min(Q[i][0],R[i][0]),max(Q[i][1],R[i][1]))for i in range(2)]
def precondition(Hxx,Hxy,Hyy,Q):
 c=[(Z[0]+Z[1])//2 for Z in Q];X=(c[0],c[0]);Y=(c[1],c[1])
 vals=[evaluate(p,X,Y)for p in(Hxx,Hxy,Hyy)];xx,xy,yy=[F(v[0]+v[1],2*S)for v in vals];d=xx*yy-xy*xy
 if not d:return None
 return[[yy/d,-xy/d],[-xy/d,xx/d]]
def inject(Hxx,Hxy,Hyy,C,Q):
 xx,xy,yy=[evaluate(p,*Q)for p in(Hxx,Hxy,Hyy)];H=[[xx,xy],[xy,yy]]
 E=[[add((S if i==j else 0,)*2,neg(asum(mul(rat(C[i][k]),H[k][j])for k in range(2))))for j in range(2)]for i in range(2)]
 norm=max(sum(max(abs(v)for v in E[i][j])for j in range(2))for i in range(2))
 return norm<S,E
def encC(C):return[[str(q)for q in row]for row in C]
def krawczyk(A,B,Hxx,Hxy,Hyy,C,R):
 ok,E=inject(Hxx,Hxy,Hyy,C,R)
 if not ok:return False
 c=[(Z[0]+Z[1])//2 for Z in R];fc=[evaluate(p,(c[0],c[0]),(c[1],c[1]))for p in(A,B)]
 KR=[add(add((c[i],c[i]),neg(asum(mul(rat(C[i][k]),fc[k])for k in range(2)))),asum(mul(E[i][j],(R[j][0]-c[j],R[j][1]-c[j]))for j in range(2)))for i in range(2)]
 return all(R[i][0]<KR[i][0]<=KR[i][1]<R[i][1]for i in range(2))

def solve(args):
 t0=time.time();nodes,L=construct();LT=list(map(terms,L));LX=[terms(q.diff(x))for q in L];LY=[terms(q.diff(y))for q in L]
 mons=[(i,d-i)for d in range(6)for i in range(d,-1,-1)]
 fieldcoeffs=[[fieldparts(q.coeff_monomial(x**i*y**j))for i,j in mons]for q in L]
 den=lcm(*(v.denominator for rows in fieldcoeffs for row in rows for v in row))
 LC=[[[int(v*den)for v in row]for row in rows]for rows in fieldcoeffs]
 def dterms(pc,dx,dy):
  out=[]
  for j,(a,b)in enumerate(mons):
   if a<dx or b<dy or not any(pc[j]):continue
   fac=1
   for z in range(dx):fac*=a-z
   for z in range(dy):fac*=b-z
   out.append((a-dx,b-dy,cparts(tuple(F(v*fac,den)for v in pc[j]))))
  return out
 def psym(pc):
  return s.Poly(sum(sum(s.Rational(v,den)*r for v,r in zip(pc[j],(1,r3,r5,r15)))*x**a*y**b for j,(a,b)in enumerate(mons)),x,y,domain=K)
 @lru_cache(None)
 def pdata(mask):
  selected=[i for i in range(21)if mask>>i&1]
  pc=tuple(tuple(2*sum(LC[i][j][k]for i in selected)-(den if j==0 and k==0 else 0)for k in range(4))for j in range(21))
  return pc,dterms(pc,1,0),dterms(pc,0,1),dterms(pc,2,0),dterms(pc,1,1),dterms(pc,0,2)
 roots=[];special_cache={};factor_cache={}
 special=[]
 for u in sorted(set(z[0]for z in nodes),key=str):
  for v in sorted(set(z[1]for z in nodes)|{s.Integer(0)},key=str):
   sub={x:u,y:v};vals=[K.from_sympy(q.as_expr().subs(sub))for q in L];gx=[K.from_sympy(q.diff(x).as_expr().subs(sub))for q in L];gy=[K.from_sympy(q.diff(y).as_expr().subs(sub))for q in L]
   regular=any(vals[i]==K.zero and(gx[i]!=K.zero or gy[i]!=K.zero)for i in range(21));node=vals.count(K.one)==1 and vals.count(K.zero)==20
   if regular or node:
    gfields=[[fieldparts(K.to_sympy(v))for v in g]for g in(gx,gy)]
    gd=lcm(*(v.denominator for g in gfields for z in g for v in z))
    ints=[[[int(v*gd)for v in z]for z in g]for g in gfields]
    special.append(((u,v),(cfield(u),cfield(v)),*ints))
 def atspecial(mask,j):
  key=(mask,j)
  if key not in special_cache:
   _,_,gx,gy=special[j];special_cache[key]=all(sum((1 if mask>>i&1 else -1)*g[i][k]for i in range(21))==0 for g in(gx,gy)for k in range(4))
  return special_cache[key]
 def exceptional(mask,Q,data):
  P,A,B,Hxx,Hxy,Hyy=data
  for j,(point,R,gx,gy)in enumerate(special):
   if any(R[i][1]<Q[i][0]-S//100 or R[i][0]>Q[i][1]+S//100 for i in range(2)):continue
   if not atspecial(mask,j):continue
   U=hull(Q,R);C=precondition(Hxx,Hxy,Hyy,U)
   if C and inject(Hxx,Hxy,Hyy,C,U)[0]:return {'code':'regular_point','point':[encfield(v)for v in point],'C':encC(C),'U':encbox(U)}
  return None
 def smoothroot(mask,Q,data):
  P,A,B,Hxx,Hxy,Hyy=data
  for rr in roots:
   if rr['mask']!=mask:continue
   R=rr['_R'];U=hull(Q,R);C=rr['_C']
   if inject(Hxx,Hxy,Hyy,C,U)[0]:return {'code':'root','id':rr['id'],'U':encbox(U)}
  c=[(Z[0]+Z[1])//2 for Z in Q]
  for it in range(5):
   point=[(v,v)for v in c];C=precondition(Hxx,Hxy,Hyy,point)
   if not C:return None
   fc=[evaluate(p,*point)for p in(A,B)];step=[neg(asum(mul(rat(C[i][k]),fc[k])for k in range(2)))for i in range(2)]
   c=[c[i]+(step[i][0]+step[i][1])//2 for i in range(2)]
  r=S>>30;R=[(v-r,v+r)for v in c]
  if any(Z[0]<=-S or Z[1]>=S for Z in R):return None
  C=precondition(Hxx,Hxy,Hyy,R)
  if not C or not krawczyk(A,B,Hxx,Hxy,Hyy,C,R):return None
  xx,xy,yy=[evaluate(p,*R)for p in(Hxx,Hxy,Hyy)]
  if xx[1]>=0 or add(mul(xx,yy),neg(power(xy,2)))[0]<=0:return None
  if any(scale(evaluate(LT[i],*R),1 if mask>>i&1 else -1)[0]<=0 for i in range(21)):return None
  U=hull(Q,R)
  if not inject(Hxx,Hxy,Hyy,C,U)[0]:return None
  if any(all(R[i][0]<=v['_R'][i][1]and v['_R'][i][0]<=R[i][1]for i in range(2))for v in roots):return None
  rr={'id':len(roots),'mask':mask,'R':encbox(R),'C':encC(C),'_R':R,'_C':C};roots.append(rr)
  return {'code':'root','id':rr['id'],'U':encbox(U)}
 def factor(mask,Q,data):
  if mask not in factor_cache:
   P=psym(data[0]);A=P.diff(x);B=P.diff(y);G=s.gcd(A,B)
   if G.total_degree()==0:factor_cache[mask]=None
   else:
    g=G.sqf_part();factor_cache[mask]=(terms(A.exquo(G)),terms(B.exquo(G)),terms(g.diff(x)),terms(g.diff(y)),str(G.as_expr()))
  v=factor_cache[mask]
  if v and(sign(evaluate(v[0],*Q))or sign(evaluate(v[1],*Q)))and(sign(evaluate(v[2],*Q))or sign(evaluate(v[3],*Q))):return {'code':'factor'}
  return None
 from a5_n5_nodes import build_node_certificates,cubes
 if args.node_file:
  node_cones=json.load(open(args.node_file))['nodes']
  if any('status'not in r for r in node_cones):node_cones=cubes(nodes,L,node_cones)
 else:node_cones=build_node_certificates(nodes,L)
 accepted_cones=[(r['index'],tuple(tuple(int(F(z)*S)for z in a)for a in r['B']))for r in node_cones if r['status']=='accepted']
 print(json.dumps({'node_cones':len(accepted_cones),'node_gap_positive':sum(F(r['gap_lower'])>0 for r in node_cones),'seconds':time.time()-t0}),flush=True)
 stats=Counter();leafstats=Counter();pending=[((-S,S),(-S,S),0,'')];unresolved=[];leaves=[];deepest=0;maxamb=0
 print(json.dumps({'construction_seconds':time.time()-t0,'precision':PREC}),flush=True)
 while pending and stats['visited']<args.boxes and time.time()-t0<args.seconds:
  X,Y,d,path=pending.pop();stats['visited']+=1;deepest=max(deepest,d)
  containing=next((index for index,B in accepted_cones if all(B[a][0]<(X,Y)[a][0] and (X,Y)[a][1]<B[a][1]for a in range(2))),None)
  if containing is not None:
   stats['discard']+=1;stats['node_cone']+=1;leafstats['node_cone']+=1
   if args.certificate:leaves.append({'path':path,'node_cone':containing})
   continue
  lv=[centered(p,LX[i],LY[i],X,Y)for i,p in enumerate(LT)];sg=[sign(v)for v in lv];amb=[i for i,z in enumerate(sg)if not z];maxamb=max(maxamb,len(amb))
  fixed=sum(1<<i for i,z in enumerate(sg)if z>0)
  codes=[];ok=False
  if len(amb)<=args.ambiguity or d>=args.full_depth:
   ok=True
   for bits in range(1<<len(amb)):
    mask=fixed+sum(1<<i for j,i in enumerate(amb)if bits>>j&1)
    data=pdata(mask);P,A,B,Hxx,Hxy,Hyy=data
    if not A or not B:code='flat'
    elif sign(evaluate(A,X,Y))or sign(evaluate(B,X,Y)):code='gradient'
    else:
     xx=evaluate(Hxx,X,Y);yy=evaluate(Hyy,X,Y);xy=evaluate(Hxy,X,Y)
     det=add(mul(xx,yy),neg(mul(xy,xy)))
     if xx[0]>0 or yy[0]>0 or det[1]<0:code='hessian'
     else:
      rec=None
      if d>=args.root_depth:rec=smoothroot(mask,(X,Y),data) or exceptional(mask,(X,Y),data) or factor(mask,(X,Y),data)
      if rec is None:ok=False;stats['failedmask']+=1;break
      code=rec
    if isinstance(code,str):code={'code':code}
    codes.append(code);stats[code['code']]+=1;stats['mask_checks']+=1
  if ok:
   stats['discard']+=1
   leafstats.update(row['code']for row in codes)
   if args.certificate:leaves.append({'path':path,'patterns':codes})
   continue
  if d>=args.depth:
   unresolved.append({'path':path,'X':[str(F(v,S))for v in X],'Y':[str(F(v,S))for v in Y],'ambiguity':len(amb),'mask':mask if len(amb)<=args.ambiguity else None});stats['depth_limit']+=1;continue
  axis=0 if X[1]-X[0]>=Y[1]-Y[0]else 1
  Z=(X,Y)[axis];m=(Z[0]+Z[1])//2
  if m in Z:raise AssertionError('precision exhausted')
  q1=[X,Y];q2=[X,Y];q1[axis]=(Z[0],m);q2[axis]=(m,Z[1]);pending.extend([(*q2,d+1,path+'1'),(*q1,d+1,path+'0')])
  if stats['visited']%1000==0:print(json.dumps({'seconds':time.time()-t0,'stats':dict(stats),'pending':len(pending),'depth':deepest,'unresolved':len(unresolved),'Pcache':pdata.cache_info().currsize}),flush=True)
 summary={'seconds':time.time()-t0,'stats':dict(stats),'pending':len(pending),'depth':deepest,'unresolved':len(unresolved),'Pcache':pdata.cache_info().currsize,'interior':len(roots),'leaf_counts':dict(leafstats),'leaf_pattern_records':sum(v for k,v in leafstats.items()if k!='node_cone'),'node_leaves':leafstats['node_cone'],'maximum_ambiguity':maxamb,'interior_complete':not pending and not unresolved,'complete':False}
 for rr in roots:rr.pop('_R');rr.pop('_C')
 out={'pattern_order':'compatible-mask','interior_roots':roots,'format':'a5-n5-spatial-v1','n':5,'precision':PREC,'node_cones':node_cones,'summary':summary,'unresolved':unresolved,'pending_paths':[v[-1]for v in pending],'leaves':leaves}
 out['metadata']={'python':sys.version,'sympy':s.__version__,'source_sha256':__import__('hashlib').sha256(open(__file__,'rb').read()).hexdigest(),'seed':None,'mathematical_run_deterministic':True}
 if args.boundary and summary['interior_complete']:
  from a5_n5_boundary import boundaries
  e,c,bs,bu=boundaries(nodes,L);out['edges']=e;out['corners']=c;out['boundary_summary']=bs;out['unresolved'].extend(bu);out['summary'].update(edge=bs['edge'],corner=bs['corner'],total=len(roots)+bs['edge']+bs['corner'],complete=not bu)
 data=json.dumps(out,separators=(',',':'),sort_keys=True).encode();f=gzip.open(args.output,'wb')if args.output.endswith('.gz')else open(args.output,'wb')
 with f:f.write(data)
 print(json.dumps(summary),flush=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--boxes',type=int,default=10000);ap.add_argument('--seconds',type=int,default=300);ap.add_argument('--depth',type=int,default=24);ap.add_argument('--ambiguity',type=int,default=5);ap.add_argument('--output',required=True);ap.add_argument('--certificate',action='store_true');ap.add_argument('--boundary',action='store_true');ap.add_argument('--full-depth',type=int,default=28);ap.add_argument('--root-depth',type=int,default=12);ap.add_argument('--node-file');solve(ap.parse_args())
