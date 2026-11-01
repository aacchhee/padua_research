"""Exact quartic feasibility diagnostics only; no maxima-count certification."""
import json,time,argparse
from collections import Counter
import sympy as s
x,y=s.symbols('x y');r2=s.sqrt(2);r5=s.sqrt(5);K=s.QQ.algebraic_field(r2,r5)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=32);args=ap.parse_args();t0=time.time()
 nodes=[(s.cos(s.pi*j/4),s.cos(s.pi*k/5),j,k)for j in range(5)for k in range(6)if(j+k)%2==0]
 mons=[x**a*y**(d-a)for d in range(5)for a in range(d,-1,-1)]
 V=s.polys.matrices.DomainMatrix.from_Matrix(s.Matrix([[m.subs({x:u,y:v})for m in mons]for u,v,j,k in nodes])).convert_to(K)
 vinv=V.inv();assert (V*vinv).to_Matrix()==s.eye(15);inv=vinv.to_Matrix()
 L=[s.Poly(sum(mons[q]*inv[q,b]for q in range(15)),x,y,domain=K)for b in range(15)]
 perm=[next(q for q,z in enumerate(nodes)if(z[2],z[3])==(4-j,k))for u,v,j,k in nodes]
 def reflect(mask):return sum(((mask>>b)&1)<<perm[b]for b in range(15))
 def orbit(mask):return{mask,32767-mask,reflect(mask),32767-reflect(mask)}
 masks=[m for m in range(32768)if m==min(orbit(m))]
 print(json.dumps({'K':str(K),'construction_seconds':time.time()-t0,'orbit_count':len(masks),'x_reflection':perm}),flush=True)
 stats=Counter();started=time.time()
 for k,mask in enumerate(masks[:args.limit]):
  t=time.time();P=sum((1 if(mask>>b)&1 else-1)*L[b]for b in range(15));A,B=P.diff(x),P.diff(y)
  if not A or not B:stats['flat']+=1;continue
  G=s.gcd(A,B);a,b=A.exquo(G),B.exquo(G);stats['gdegree'+str(G.total_degree())]+=1
  rx=s.resultant(a.as_expr(),b.as_expr(),y);ry=s.resultant(a.as_expr(),b.as_expr(),x)
  stats[str((s.degree(rx,x),s.degree(ry,y)))]+=1
  print(json.dumps({'k':k,'mask':mask,'gdegree':G.total_degree(),'degrees':[s.degree(rx,x),s.degree(ry,y)],'seconds':time.time()-t},default=int),flush=True)
 print(json.dumps({'scope':min(args.limit,len(masks)),'seconds':time.time()-started,'stats':dict(stats)}),flush=True)
if __name__=='__main__':main()
