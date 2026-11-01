"""New exact n=3 A5 certificate producer. No imports from the old certifier.

Exact resultants/norm real-root isolation enumerate all signed-polynomial
stationary systems. The separate a5_checker verifies supplied certificates.
"""
import argparse,json,gzip,time,platform,sys
from collections import Counter
from pathlib import Path
import sympy as sp
from a5_arithmetic import *

def encC(C):return[[str(q)for q in row]for row in C]
def root_record(P,Lterms,signs,Q,H,Hterms,exact=None):
 # Finite rational box includes the entire projected pair, including singletonroots.
 X,Y=Q;c=[(Z.lo+Z.hi)/2 for Z in Q]
 r=F(1,10**8)
 box=[I(z-r,z+r)for z in c]
 if any(Z.lo<=-1 or Z.hi>=1 for Z in box):return None
 C=cmatrix(H,c)
 if C is None:return None
 norm,E=contraction(Hterms,C,*box)
 if norm>=1:return None
 ht=evalpoly(Hterms[0][0],*box);dt=evalpoly(sp.expand(H.det()),*box)
 if ht.hi>=0 or dt.lo<=0:return None
 if any((signs[b]*evalpoly(Lterms[b],*box)).lo<=0 for b in range(10)):return None
 if exact is None:
  fc=[evalpoly(P.diff(v),iv(c[0]),iv(c[1]))for v in(x,y)]
  K=[iv(c[i])-sum((C[i][k]*fc[k]for k in range(2)),iv(0))+sum((E[i][j]*I(-r,r)for j in range(2)),iv(0))for i in range(2)]
  if not all(box[i].lo<K[i].lo<=K[i].hi<box[i].hi for i in range(2)):return None
 rec={'code':'root','box':[Z.strings()for Z in box],'C':encC(C)}
 if exact is not None:rec['point']=[encfield(v)for v in exact]
 return rec

def produce(limit=1024):
 nodes,L=cardinals();Lterms=list(map(polyterms,L));exactpoints=nodes+[(sp.Rational(1,2),sp.Integer(0))]
 cert={'format':'a5-n3-v1','n':3,'patterns':[],'edges':[],'corners':[]}
 counts=Counter();unresolved=[];started=time.time();rootid=0
 for mask in range(limit):
  signs=[1 if(mask>>i)&1 else-1 for i in range(10)]
  P=sum(signs[i]*L[i]for i in range(10));A,B=P.diff(x),P.diff(y)
  if not A or not B:
   rec={'mask':mask,'kind':'flat'};counts['flat']+=1;cert['patterns'].append(rec);continue
  G=sp.gcd(A,B);a,b=A.exquo(G),B.exquo(G)
  rec={'mask':mask,'kind':'residual','g':encpoly(G)}
  if a.total_degree()==0 or b.total_degree()==0:
   rec['kind']='unit';counts['unit']+=1;cert['patterns'].append(rec);continue
  Rx=sp.resultant(a.as_expr(),b.as_expr(),y);Ry=sp.resultant(a.as_expr(),b.as_expr(),x)
  assert Rx!=0 and Ry!=0
  nx,ny=rational_norm(Rx,x),rational_norm(Ry,y)
  xr,yr=root_intervals(nx),root_intervals(ny)
  rec['xroots']=[z.strings()for z in xr];rec['yroots']=[z.strings()for z in yr];rec['pairs']=[]
  H=sp.hessian(P.as_expr(),(x,y));Hterms=[[polyterms(H[i,j])for j in range(2)]for i in range(2)]
  Dterms=polyterms(sp.expand(H.det()));Aterms=polyterms(A);Bterms=polyterms(B)
  for i,X in enumerate(xr):
   for j,Y in enumerate(yr):
    Q=[X,Y];rr={'ij':[i,j]};code=None
    if any(Z.hi<=-1 or Z.lo>=1 for Z in Q):code='outside'
    elif not evalpoly(Aterms,X,Y).contains0()or not evalpoly(Bterms,X,Y).contains0():code='gradient'
    elif evalpoly(Hterms[0][0],X,Y).lo>=0 or evalpoly(Hterms[1][1],X,Y).lo>=0 or evalpoly(Dterms,X,Y).hi<=0:code='hessian'
    else:
     for k in range(10):
      if(signs[k]*evalpoly(Lterms[k],X,Y)).hi<0:code='sign';rr['b']=k;break
    if code is None:
     for point in exactpoints:
      pe=[evalpoly(v,iv(0),iv(0))for v in point]
      if not all(Q[k].lo<=pe[k].lo<=pe[k].hi<=Q[k].hi for k in range(2)):continue
      sub={x:point[0],y:point[1]}
      if any(sp.expand(z.as_expr().subs(sub))!=0 for z in(A,B)):continue
      regular=any(sp.expand(lb.as_expr().subs(sub))==0 and any(sp.expand(lb.diff(v).as_expr().subs(sub))!=0 for v in(x,y))for lb in L)
      c=[(Z.lo+Z.hi)/2 for Z in Q];C=cmatrix(H,c)
      if regular and C is not None and contraction(Hterms,C,X,Y)[0]<1:
       code='regular';rr['point']=[encfield(v)for v in point];rr['C']=encC(C);break
    if code is None:
     rrec=root_record(P,Lterms,signs,Q,H,Hterms)
     if rrec is not None:rr.update(rrec);rr['id']=rootid;rootid+=1;code='root'
    if code is None:
     code='unresolved';unresolved.append({'mask':mask,'ij':[i,j],'x':X.strings(),'y':Y.strings(),'P':str(P.as_expr()),'A':str(A.as_expr()),'B':str(B.as_expr())})
    rr['code']=code;rec['pairs'].append(rr);counts[code]+=1
  cert['patterns'].append(rec);counts['residual']+=1
  if mask%32==0:print(json.dumps({'mask':mask,'seconds':round(time.time()-started,2),'counts':dict(counts),'unresolved':len(unresolved)}),file=sys.stderr,flush=True)
 cert['summary']={'interior':rootid,'counts':dict(counts),'unresolved':len(unresolved),'patterns':limit,'complete':False}
 return cert,unresolved

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=1024);ap.add_argument('--output',required=True);ap.add_argument('--unresolved',required=True);args=ap.parse_args()
 cert,unresolved=produce(args.limit)
 if args.limit==1024:
  from a5_boundary import boundaries
  from a5_global import global_certificate
  e,c,bs,bu=boundaries();cert['edges']=e;cert['corners']=c;unresolved.extend(bu)
  cert['summary'].update(edge=bs['edge'],corner=bs['corner'],total=cert['summary']['interior']+bs['edge']+bs['corner'],boundary_counts=bs['counts'],unresolved=len(unresolved),complete=not unresolved)
  cert['global']=global_certificate(cert)
 path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
 data=json.dumps(cert,separators=(',',':'),sort_keys=True).encode()
 if path.suffix=='.gz':
  with path.open('wb')as f:
   with gzip.GzipFile(filename='',fileobj=f,mode='wb',mtime=0)as z:z.write(data)
 else:path.write_bytes(data)
 Path(args.unresolved).write_text(json.dumps(unresolved,indent=2)+'\n')
 print(json.dumps({'output':str(path),'bytes':path.stat().st_size,'summary':cert['summary']}),flush=True)
if __name__=='__main__':main()
