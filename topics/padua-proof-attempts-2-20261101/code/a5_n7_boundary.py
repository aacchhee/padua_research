"""Exact n7 edge-arrangement and corner certificate producer.

No old certifier imports. The independent checker must verify supplied partitions.
"""
import json,time,sys,argparse
from collections import Counter
from a5_n7_boxes import *

def norm(p):
 assert p
 return norm_monic(p.monic())
@lru_cache(None)
def norm_monic(p):
 # Norm tower in the low-height tensor coordinates, rather than the native
 # theta quotient. Reduction modulo p3 before the second resultant is exact.
 variable=p.gens[0];aa,bb=s.Dummy('a'),s.Dummy('b');coeff={}
 for (degree,),c in p.rep.to_dict().items():
  parts=kparts(c)
  for i in range(3):
   for j in range(4):
    v=parts[4*i+j]
    if v:coeff[(j,)]=coeff.get((j,),0)+s.Rational(v.numerator,v.denominator)*aa**i*variable**degree
 ring=s.QQ.poly_ring(variable,aa)
 lifted=s.Poly.from_dict(coeff,(bb,),domain=ring)
 quartic=s.Poly(bb**4-4*bb**2+2,bb,domain=ring)
 intermediate=quartic.resultant(lifted)
 ring=s.QQ.poly_ring(variable)
 cubic=s.Poly(aa**3-aa**2-2*aa+1,aa,domain=ring)
 reduced=s.Poly(intermediate,aa,domain=ring).rem(cubic)
 result=s.Poly(cubic.resultant(reduced),variable,domain=s.QQ)
 assert result
 return result.sqf_part().clear_denoms()[1].primitive()[1]
def primitive_positive(p):
 return p.clear_denoms()[1].primitive()[1]
def root_counter(p):
 # A positively rescaled Sturm chain controls denominator growth. Evaluate
 # signs by integer homogenization, once per endpoint, without rational gcds.
 chain=[primitive_positive(p)]
 if p.degree()>0:
  chain.append(primitive_positive(p.diff()))
  while True:
   remainder=-chain[-2].rem(chain[-1])
   if not remainder:break
   chain.append(primitive_positive(remainder))
 rows=[tuple(map(int,q.all_coeffs()))for q in chain]
 def variation(point):
  signs=[]
  for row in rows:
   if point is None:v=row[0]
   elif point=='-inf':v=row[0]*(-1 if(len(row)-1)%2 else 1)
   else:
    a,b=point.numerator,point.denominator;v=row[0];d=b
    for c in row[1:]:v=v*a+c*d;d*=b
   if v:signs.append(1 if v>0 else-1)
  return sum(u!=v for u,v in zip(signs,signs[1:]))
 total=variation('-inf')-variation(None)
 return total,variation
def intervals(p):return list(intervals_monic(p.monic()))
def dyadic_value(v):
 mantissa,exponent=v.man_exp()
 return F(int(mantissa))*F(2)**int(exponent)
@lru_cache(None)
def intervals_monic(p):
 # Arb supplies outward candidates; exact Sturm checks prove all-real-root
 # coverage before serialization. The independent checker verifies the
 # supplied partition again, without performing isolation.
 from flint import fmpz_poly,ctx
 integral=p.clear_denoms()[1].primitive()[1]
 zz=fmpz_poly([int(c)for c in reversed(integral.all_coeffs())])
 total,variations=root_counter(p);oldprec=ctx.prec
 try:
  for precision in(128,256,512):
   ctx.prec=precision;balls=zz.complex_roots();real=[];uncertain=False
   for ball,multiplicity in balls:
    if ball.imag==0:
     mid=dyadic_value(ball.real.mid());radius=dyadic_value(ball.real.rad());real.append((mid-radius,mid+radius))
    elif not(ball.imag>0 or ball.imag<0):uncertain=True
   if uncertain or len(real)!=total:continue
   for bits in(80,112,160,224):
    grid=1<<bits;roots=[]
    for lo,hi in real:
     a=F((lo*grid).numerator//(lo*grid).denominator,grid)
     h=hi*grid;b=F(-((-h.numerator)//h.denominator),grid)
     if p.eval(s.Rational(str(a)))==0:b=a
     elif p.eval(s.Rational(str(b)))==0:a=b
     roots.append((a,b))
    roots.sort()
    if not all(roots[i][1]<roots[i+1][0]for i in range(len(roots)-1)):continue
    valid=True
    for a,b in roots:
     aa=s.Rational(str(a));bb=s.Rational(str(b))
     if a==b:valid=valid and p.eval(aa)==0
     else:valid=valid and p.eval(aa)!=0 and p.eval(bb)!=0 and variations(a)-variations(b)==1
    if valid:return tuple(roots)
 finally:ctx.prec=oldprec
 # Failure is never success. Retain exact Sturm isolation as a slow fallback.
 return tuple((F(str(a)),F(str(b)))for(a,b),m in p.intervals(eps=s.Rational(1,10**22)))
def squarefree_union(restricted):
 # Exact gcd splitting constructs pairwise-coprime squarefree components of
 # the union. All gcd inputs have degree at most7, avoiding the expanded
 # degree252 product's derivative gcd and costly K-irreducible factorizations.
 components=[];simple=s.Poly(1,restricted[0].gens[0],domain=K)
 for q in restricted:
  sf=q.sqf_list()[1]
  p=s.prod(f for f,m in sf).monic();new=[]
  for f in components:
   g=s.gcd(f,p).monic()
   if g.degree()>0:
    new.append(g);v=f.exquo(g)
    if v.degree()>0:new.append(v.monic())
    p=p.exquo(g).monic()
   else:new.append(f)
  if p.degree()>0:new.append(p.monic())
  components=new
  for f,m in sf:
   if m==1:simple*=f
 E=s.prod(components).monic()
 assert simple.rem(E).is_zero,'singular-only edgecrease requires localproof'
 return E,components
def arrangement_intervals(components):
 # Norm multiplicativity: normalize exact small gcd components, then use
 # distinct QQ irreducibles. The independent checker verifies complete norm
 # coverage; producer search/isolation itself carries no proof authority.
 factors={}
 for f in components:
  nf=norm(f)
  for h,k in nf.factor_list()[1]:
   h=h.monic();factors[tuple(h.all_coeffs())]=h
 polynomials=list(factors.values());digits=22
 while True:
  roots=[]
  for p in polynomials:
   roots.extend((F(str(a)),F(str(b)))for(a,b),m in p.intervals(eps=s.Rational(1,10**digits)))
  roots.sort()
  if all(roots[i][1]<roots[i+1][0]for i in range(len(roots)-1)):return roots,sum(p.degree()for p in polynomials)
  digits*=2
def encintervals(v):return[[str(a),str(b)]for a,b in v]
def fixedbox(T):return(rat(T[0])[0],rat(T[1])[1])
def onedge(p,axis,side,T):
 v=fixedbox(T);return evaluate(terms(p),(side*S,side*S),v)if axis==0 else evaluate(terms(p),v,(side*S,side*S))
def fieldsg(c):return ksign(K.convert(c))
def evalK(p,z):
 kz=K.convert(z);return sum((c*kz**i for(i,),c in p.rep.to_dict().items()),K.zero)
def samples(roots):
 if not roots:return[F(0)]
 return[roots[0][0]-1]+[(roots[i][1]+roots[i+1][0])/2 for i in range(len(roots)-1)]+[roots[-1][1]+1]

def boundaries(nodes=None,L=None):
 t0=time.time()
 if nodes is None:nodes,L=construct()
 edges=[];stats=Counter();unresolved=[];eid=0
 for axis,side in((0,-1),(0,1),(1,-1),(1,1)):
  z=(x,y)[axis];t=(y,x)[axis]
  R=[q.eval(z,side)for q in L]
  assert all(R),'identicallyzero boundarycardinal requires schemaextension'
  print(json.dumps({'edge_stage':'restrictions','edge':[axis,side],'seconds':time.time()-t0}),file=sys.stderr,flush=True)
  E,components=squarefree_union(R)
  print(json.dumps({'edge_stage':'squarefree','edge':[axis,side],'degree':E.degree(),'seconds':time.time()-t0}),file=sys.stderr,flush=True)
  eroots,enormdegree=arrangement_intervals(components);ss=samples(eroots);masks=[]
  print(json.dumps({'edge_stage':'arrangement','edge':[axis,side],'normdegree':enormdegree,'seconds':time.time()-t0}),file=sys.stderr,flush=True)
  for u in ss:
   vals=[fieldsg(evalK(q,s.Rational(u.numerator,u.denominator)))for q in R];assert all(vals)
   masks.append(sum(1<<i for i,zs in enumerate(vals)if zs>0))
  masks=sorted(set(masks));edge={'axis':axis,'side':side,'E_norm_intervals':encintervals(eroots),'samples':list(map(str,ss)),'sample_masks':masks,'patterns':[]}
  for mask in masks:
   sg=[1 if mask>>i&1 else -1 for i in range(36)];P=sum(sg[i]*L[i]for i in range(36));q=sum(sg[i]*R[i]for i in range(36));D=q.diff();DD=D.diff()
   row={'mask':mask,'kind':'roots'}
   if not D:row['kind']='flat';edge['patterns'].append(row);stats['flat']+=1;continue
   sf=D.sqf_part();Dr=sf.exquo(s.gcd(sf,E));rr=intervals(norm(Dr));row['Dr_norm_intervals']=encintervals(rr);row['points']=[]
   for i,I in enumerate(rr):
    point={'i':i};code=None
    if I[1]<=-1 or I[0]>=1:code='outside'
    elif sign(onedge(Dr,axis,side,I)):code='derivative'
    elif onedge(DD,axis,side,I)[0]>0:code='minimum'
    else:
     for j in range(36):
      if scale(onedge(R[j],axis,side,I),sg[j])[1]<0:code='sign';point['b']=j;break
    if code is None:
     mid=sum(I)/2;r=F(1,2**30);U=(mid-r,mid+r)
     consistent=all(scale(onedge(R[j],axis,side,U),sg[j])[0]>0 for j in range(36))
     if consistent and U[0]>-1 and U[1]<1 and onedge(DD,axis,side,U)[1]<0:
      dlo=onedge(D,axis,side,(U[0],U[0]));dhi=onedge(D,axis,side,(U[1],U[1]));N=-side*P.diff(z);NI=onedge(N,axis,side,U)
      if dlo[0]>0 and dhi[1]<0:
       if NI[1]<0:code='root';point['id']=eid;eid+=1
       elif NI[0]>0:code='normal'
       if code:point['interval']=list(map(str,U))
    if code is None:
     code='unresolved';unresolved.append({'axis':axis,'side':side,'mask':mask,'i':i,'I':list(map(str,I)),'q':str(q.as_expr()),'D':str(D.as_expr())})
    point['code']=code;row['points'].append(point);stats[code]+=1
   edge['patterns'].append(row)
  edges.append(edge)
  print(json.dumps({'edge':[axis,side],'patterns':len(masks),'Enormdegree':enormdegree,'seconds':time.time()-t0,'edgecount':eid,'unresolved':len(unresolved),'stats':dict(stats)}),file=sys.stderr,flush=True)
 corners=[];cid=0
 for u,v in((-1,-1),(-1,1),(1,-1),(1,1)):
  sub={x:u,y:v};vals=[native_eval(q,u,v)for q in L];vals=[K.convert(z)for z in vals];row={'point':[u,v]}
  if vals.count(K.one)==1 and vals.count(K.zero)==35:row['kind']='node'
  else:
   zeros=[i for i,c in enumerate(vals)if c==K.zero];sg=[1 if fieldsg(c)>0 else -1 for c in vals];ok=True
   for bits in range(1<<len(zeros)):
    signsv=sg[:]
    for j,b in enumerate(zeros):signsv[b]=1 if bits>>j&1 else -1
    P=sum(signsv[i]*L[i]for i in range(36));du=-u*native_eval(P.diff(x),u,v);dv=-v*native_eval(P.diff(y),u,v)
    if fieldsg(du)>=0 or fieldsg(dv)>=0:ok=False
   row.update(zeros=zeros)
   if ok:row.update(kind='max',id=cid);cid+=1
   else:row.update(kind='unresolved');unresolved.append(row)
  corners.append(row)
 return edges,corners,{'edge':eid,'corner':cid,'counts':dict(stats),'unresolved':len(unresolved),'complete':not unresolved,'seconds':time.time()-t0},unresolved

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();e,c,summary,u=boundaries();open(a.output,'w').write(json.dumps({'edges':e,'corners':c,'summary':summary,'unresolved':u},separators=(',',':'),sort_keys=True));print(json.dumps(summary),flush=True)
