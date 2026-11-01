"""Exact n8 edge-arrangement and corner certificate producer.

No old certifier imports. The independent checker must verify supplied partitions.
"""
import json,time,sys,argparse
from collections import Counter
from a5_n8_boxes import *

def norm(p):
 assert p
 return p.norm().sqf_part().clear_denoms()[1].primitive()[1]
def intervals(p):
 return[(F(str(a)),F(str(b)))for(a,b),m in p.intervals(eps=s.Rational(1,10**22))]
def squarefree_union(restricted):
 # Exact gcd splitting constructs pairwise-coprime squarefree components of
 # the union. All gcd inputs have degree at most8, avoiding the expanded
 # degree360 product's derivative gcd and costly K-irreducible factorizations.
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

def boundaries(nodes=None,L=None,edge_limit=4):
 t0=time.time()
 if nodes is None:nodes,L=construct()
 edges=[];stats=Counter();unresolved=[];eid=0
 for axis,side in((0,-1),(0,1),(1,-1),(1,1))[:edge_limit]:
  z=(x,y)[axis];t=(y,x)[axis]
  R=[q.eval(z,side)for q in L]
  assert all(R),'identicallyzero boundarycardinal requires schemaextension'
  E,components=squarefree_union(R)
  eroots,enormdegree=arrangement_intervals(components);ss=samples(eroots);masks=[]
  for u in ss:
   vals=[fieldsg(evalK(q,s.Rational(u.numerator,u.denominator)))for q in R];assert all(vals)
   masks.append(sum(1<<i for i,zs in enumerate(vals)if zs>0))
  masks=sorted(set(masks));edge={'axis':axis,'side':side,'E_norm_intervals':encintervals(eroots),'samples':list(map(str,ss)),'sample_masks':masks,'patterns':[]}
  for mask in masks:
   sg=[1 if mask>>i&1 else -1 for i in range(45)];P=sum(sg[i]*L[i]for i in range(45));q=sum(sg[i]*R[i]for i in range(45));D=q.diff();DD=D.diff()
   row={'mask':mask,'kind':'roots'}
   if not D:row['kind']='flat';edge['patterns'].append(row);stats['flat']+=1;continue
   sf=D.sqf_part();Dr=sf.exquo(s.gcd(sf,E));rr=intervals(norm(Dr));row['Dr_norm_intervals']=encintervals(rr);row['points']=[]
   for i,I in enumerate(rr):
    point={'i':i};code=None
    if I[1]<=-1 or I[0]>=1:code='outside'
    elif sign(onedge(Dr,axis,side,I)):code='derivative'
    elif onedge(DD,axis,side,I)[0]>0:code='minimum'
    else:
     for j in range(45):
      if scale(onedge(R[j],axis,side,I),sg[j])[1]<0:code='sign';point['b']=j;break
    if code is None:
     mid=sum(I)/2;r=F(1,2**30);U=(mid-r,mid+r)
     consistent=all(scale(onedge(R[j],axis,side,U),sg[j])[0]>0 for j in range(45))
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
  sub={x:u,y:v};vals=[q.eval(x,u).eval(y,v)for q in L];vals=[K.convert(z)for z in vals];row={'point':[u,v]}
  if vals.count(K.one)==1 and vals.count(K.zero)==44:row['kind']='node'
  else:
   zeros=[i for i,c in enumerate(vals)if c==K.zero];sg=[1 if fieldsg(c)>0 else -1 for c in vals];ok=True
   for bits in range(1<<len(zeros)):
    signsv=sg[:]
    for j,b in enumerate(zeros):signsv[b]=1 if bits>>j&1 else -1
    P=sum(signsv[i]*L[i]for i in range(45));du=-u*P.diff(x).eval(x,u).eval(y,v);dv=-v*P.diff(y).eval(x,u).eval(y,v)
    if fieldsg(du)>=0 or fieldsg(dv)>=0:ok=False
   row.update(zeros=zeros)
   if ok:row.update(kind='max',id=cid);cid+=1
   else:row.update(kind='unresolved');unresolved.append(row)
  corners.append(row)
 return edges,corners,{'edge':eid,'corner':cid,'counts':dict(stats),'unresolved':len(unresolved),'complete':edge_limit==4 and not unresolved,'seconds':time.time()-t0},unresolved

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--edge-limit',type=int,choices=range(1,5),default=4);a=ap.parse_args();e,c,summary,u=boundaries(edge_limit=a.edge_limit);open(a.output,'w').write(json.dumps({'edges':e,'corners':c,'summary':summary,'unresolved':u},separators=(',',':'),sort_keys=True));print(json.dumps(summary),flush=True)
