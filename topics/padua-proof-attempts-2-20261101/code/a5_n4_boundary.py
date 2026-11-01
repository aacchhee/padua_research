"""Exact n4 edge-arrangement and corner certificate producer.

No old certifier imports. The independent checker must verify supplied partitions.
"""
import json,time,sys,argparse
from collections import Counter
from a5_n4_boxes import *

def norm(p):
 assert p
 return p.norm().sqf_part().clear_denoms()[1].primitive()[1]
def intervals(p):
 return[(F(str(a)),F(str(b)))for(a,b),m in p.intervals(eps=s.Rational(1,10**22))]
def encintervals(v):return[[str(a),str(b)]for a,b in v]
def fixedbox(T):return(rat(T[0])[0],rat(T[1])[1])
def onedge(p,axis,side,T):
 v=fixedbox(T);return evaluate(terms(p),(side*S,side*S),v)if axis==0 else evaluate(terms(p),v,(side*S,side*S))
def fieldsg(c):return sign(cfield(K.to_sympy(K.from_sympy(c))))
def samples(roots):
 if not roots:return[F(0)]
 return[roots[0][0]-1]+[(roots[i][1]+roots[i+1][0])/2 for i in range(len(roots)-1)]+[roots[-1][1]+1]

def boundaries(nodes=None,L=None):
 t0=time.time()
 if nodes is None:nodes,L=construct()
 edges=[];stats=Counter();unresolved=[];eid=0
 for axis,side in((0,-1),(0,1),(1,-1),(1,1)):
  z=(x,y)[axis];t=(y,x)[axis]
  R=[s.Poly(q.as_expr().subs(z,side),t,domain=K)for q in L]
  assert all(R),'identicallyzero boundarycardinal requires schemaextension'
  product=s.prod(R);E=product.sqf_part();simple=s.Poly(1,t,domain=K)
  for q in R:
   for f,m in q.sqf_list()[1]:
    if m==1:simple*=f
  assert simple.rem(E).is_zero,'singular-only edgecrease requires localproof'
  eroots=intervals(norm(E));ss=samples(eroots);masks=[]
  for u in ss:
   vals=[fieldsg(q.eval(s.Rational(u.numerator,u.denominator)))for q in R];assert all(vals)
   masks.append(sum(1<<i for i,zs in enumerate(vals)if zs>0))
  masks=sorted(set(masks));edge={'axis':axis,'side':side,'E_norm_intervals':encintervals(eroots),'samples':list(map(str,ss)),'sample_masks':masks,'patterns':[]}
  for mask in masks:
   sg=[1 if mask>>i&1 else -1 for i in range(15)];P=sum(sg[i]*L[i]for i in range(15));q=sum(sg[i]*R[i]for i in range(15));D=q.diff();DD=D.diff()
   row={'mask':mask,'kind':'roots'}
   if not D:row['kind']='flat';edge['patterns'].append(row);stats['flat']+=1;continue
   sf=D.sqf_part();Dr=sf.exquo(s.gcd(sf,E));rr=intervals(norm(Dr));row['Dr_norm_intervals']=encintervals(rr);row['points']=[]
   for i,I in enumerate(rr):
    point={'i':i};code=None
    if I[1]<=-1 or I[0]>=1:code='outside'
    elif sign(onedge(Dr.as_expr(),axis,side,I)):code='derivative'
    elif onedge(DD.as_expr(),axis,side,I)[0]>0:code='minimum'
    else:
     for j in range(15):
      if scale(onedge(R[j].as_expr(),axis,side,I),sg[j])[1]<0:code='sign';point['b']=j;break
    if code is None:
     mid=sum(I)/2;r=F(1,2**30);U=(mid-r,mid+r)
     consistent=all(scale(onedge(R[j].as_expr(),axis,side,U),sg[j])[0]>0 for j in range(15))
     if consistent and U[0]>-1 and U[1]<1 and onedge(DD.as_expr(),axis,side,U)[1]<0:
      dlo=onedge(D.as_expr(),axis,side,(U[0],U[0]));dhi=onedge(D.as_expr(),axis,side,(U[1],U[1]));N=-side*P.diff(z);NI=onedge(N.as_expr(),axis,side,U)
      if dlo[0]>0 and dhi[1]<0:
       if NI[1]<0:code='root';point['id']=eid;eid+=1
       elif NI[0]>0:code='normal'
       if code:point['interval']=list(map(str,U))
    if code is None:
     code='unresolved';unresolved.append({'axis':axis,'side':side,'mask':mask,'i':i,'I':list(map(str,I)),'q':str(q.as_expr()),'D':str(D.as_expr())})
    point['code']=code;row['points'].append(point);stats[code]+=1
   edge['patterns'].append(row)
  edges.append(edge)
  print(json.dumps({'edge':[axis,side],'patterns':len(masks),'Enormdegree':norm(E).degree(),'seconds':time.time()-t0,'edgecount':eid,'unresolved':len(unresolved),'stats':dict(stats)}),file=sys.stderr,flush=True)
 corners=[];cid=0
 for u,v in((-1,-1),(-1,1),(1,-1),(1,1)):
  sub={x:u,y:v};vals=[K.from_sympy(q.as_expr().subs(sub))for q in L];row={'point':[u,v]}
  if vals.count(K.one)==1 and vals.count(K.zero)==14:row['kind']='node'
  else:
   zeros=[i for i,c in enumerate(vals)if c==K.zero];sg=[1 if fieldsg(K.to_sympy(c))>0 else -1 for c in vals];ok=True
   for bits in range(1<<len(zeros)):
    signsv=sg[:]
    for j,b in enumerate(zeros):signsv[b]=1 if bits>>j&1 else -1
    P=sum(signsv[i]*L[i]for i in range(15));du=-u*P.diff(x).as_expr().subs(sub);dv=-v*P.diff(y).as_expr().subs(sub)
    if fieldsg(du)>=0 or fieldsg(dv)>=0:ok=False
   row.update(zeros=zeros)
   if ok:row.update(kind='max',id=cid);cid+=1
   else:row.update(kind='unresolved');unresolved.append(row)
  corners.append(row)
 return edges,corners,{'edge':eid,'corner':cid,'counts':dict(stats),'unresolved':len(unresolved),'complete':not unresolved,'seconds':time.time()-t0},unresolved

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();e,c,summary,u=boundaries();open(a.output,'w').write(json.dumps({'edges':e,'corners':c,'summary':summary,'unresolved':u},separators=(',',':'),sort_keys=True));print(json.dumps(summary),flush=True)
