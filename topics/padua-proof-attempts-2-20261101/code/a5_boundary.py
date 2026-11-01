"""Exact physical-boundary certificate producer for degree3 A5."""
import json,sys,time
from collections import Counter
from a5_arithmetic import *

def onedge(p,axis,side,T):
 return evalpoly(p,iv(side),T)if axis==0 else evalpoly(p,T,iv(side))
def field_in(c,T):
 Z=evalpoly(c,iv(0),iv(0));return T.lo<=Z.lo<=Z.hi<=T.hi

def boundaries():
 nodes,L=cardinals();edges=[];stats=Counter();unresolved=[];eid=0
 for axis,side in((0,-1),(0,1),(1,-1),(1,1)):
  normal=(x,y)[axis];t=(y,x)[axis]
  restricted=[sp.Poly(l.as_expr().subs(normal,side),t,domain=K)for l in L]
  zeros=[i for i,p in enumerate(restricted)if not p]
  edge={'axis':axis,'side':side,'zeros':zeros,'patterns':[]}
  points=[z[1-axis]for z in nodes if z[axis]==side]+[sp.Integer(0)]
  for mask in range(1024):
   if any((mask>>i)&1 for i in zeros):continue
   signs=[1 if(mask>>i)&1 else-1 for i in range(10)]
   q=sum(signs[i]*restricted[i]for i in range(10));D=q.diff();DD=D.diff()
   rec={'mask':mask,'kind':'roots'}
   if not D:rec['kind']='flat';edge['patterns'].append(rec);stats['flat']+=1;continue
   norm=rational_norm(D.as_expr(),t);roots=root_intervals(norm);rec['roots']=[z.strings()for z in roots];rec['points']=[]
   for i,T in enumerate(roots):
    rr={'i':i};code=None
    if T.hi<=-1 or T.lo>=1:code='outside'
    elif not onedge(D.as_expr(),axis,side,T).contains0():code='derivative'
    elif onedge(DD.as_expr(),axis,side,T).lo>=0:code='hessian'
    else:
     for b in range(10):
      if b not in zeros and(signs[b]*onedge(restricted[b].as_expr(),axis,side,T)).hi<0:code='sign';rr['b']=b;break
    if code is None:
     for point in points:
      if not field_in(point,T)or sp.expand(D.as_expr().subs(t,point))!=0:continue
      if any(restricted[b] and sp.expand(restricted[b].as_expr().subs(t,point))==0 and sp.expand(restricted[b].diff().as_expr().subs(t,point))!=0 for b in range(10))and not onedge(DD.as_expr(),axis,side,T).contains0():
       code='regular';rr['point']=encfield(point);break
    if code is None:
     # Larger root interval supports strict sign inequalities even at singletonprojections.
     mid=(T.lo+T.hi)/2;r=F(1,10**10);U=I(mid-r,mid+r)
     consistent=all((signs[b]*onedge(restricted[b].as_expr(),axis,side,U)).lo>0 for b in range(10)if b not in zeros)
     if consistent and U.lo>-1 and U.hi<1 and onedge(DD.as_expr(),axis,side,U).hi<0:
      fullsign=signs[:];ok=True
      for b in zeros:
       quotient=L[b].exquo(sp.Poly(normal-side,x,y,domain=K))
       Z=onedge(quotient.as_expr(),axis,side,U)
       if Z.lo>0:fullsign[b]=-side
       elif Z.hi<0:fullsign[b]=side
       else:ok=False;break
      if ok:
       fullmask=sum((int(sg>0)<<b)for b,sg in enumerate(fullsign))
       P=sum(fullsign[b]*L[b]for b in range(10));N=-side*P.diff(normal)
       NI=onedge(N.as_expr(),axis,side,U)
       dlo=onedge(D.as_expr(),axis,side,iv(U.lo));dhi=onedge(D.as_expr(),axis,side,iv(U.hi))
       if dlo.lo>0 and dhi.hi<0:
        if NI.hi<0:code='root';rr['id']=eid;eid+=1
        elif NI.lo>0:code='normal'
        if code is not None:rr['interval']=U.strings();rr['fullmask']=fullmask
    if code is None:
     code='unresolved';unresolved.append({'axis':axis,'side':side,'mask':mask,'i':i,'T':T.strings(),'q':str(q.as_expr()),'D':str(D.as_expr())})
    rr['code']=code;rec['points'].append(rr);stats[code]+=1
   edge['patterns'].append(rec)
  edges.append(edge)
  print(json.dumps({'edge':[axis,side],'counts':dict(stats),'unresolved':len(unresolved)}),file=sys.stderr,flush=True)
 corners=[];cid=0
 for u,v in((-1,-1),(-1,1),(1,-1),(1,1)):
  sub={x:u,y:v};vals=[sp.expand(l.as_expr().subs(sub))for l in L]
  rr={'point':[u,v]}
  if vals.count(1)==1 and vals.count(0)==9:rr['kind']='node'
  else:
   zeros=[b for b,z in enumerate(vals)if z==0];sg=[1 if z>0 else-1 for z in vals]
   ok=True;worst=[]
   for bits in range(1<<len(zeros)):
    signs=sg[:]
    for j,b in enumerate(zeros):signs[b]=1 if(bits>>j)&1 else-1
    P=sum(signs[b]*L[b]for b in range(10))
    du=sp.expand(-u*P.diff(x).as_expr().subs(sub));dv=sp.expand(-v*P.diff(y).as_expr().subs(sub))
    if not(du<0 and dv<0):ok=False
    worst.append([str(du),str(dv)])
   if ok:rr.update(kind='max',zeros=zeros,id=cid);cid+=1
   else:rr.update(kind='unresolved',zeros=zeros,derivatives=worst);unresolved.append(rr)
  corners.append(rr)
 return edges,corners,{'edge':eid,'corner':cid,'counts':dict(stats),'unresolved':len(unresolved)},unresolved
if __name__=='__main__':
 e,c,s,u=boundaries();print(json.dumps({'edges':e,'corners':c,'summary':s,'unresolved':u},separators=(',',':')))
