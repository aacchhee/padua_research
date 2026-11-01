"""Exact physical node-gap and radial-cube certificate producer.

All comparisons are exact or outward fixed-dyadic integer arithmetic. No old
certifier imports and no floating root/gradient calculations.
"""
import argparse,json,time,sys
from functools import cmp_to_key
from a5_n7_field import (s,x,y,K,S,PREC,F,cfield,cparts,encfield,terms,evaluate,centered,construct,encbox,kparts,kfield,ksign)

def norm(q):return K.to_sympy(K.convert(q))
def exactsign(q):
 q=norm(q)
 if q==0:return 0
 z=cfield(q)
 if z[0]>0:return 1
 if z[1]<0:return -1
 raise ArithmeticError('128-bit enclosure cannot decide exact field sign')
def compare(a,b):return exactsign(a-b)
def node_gradients(nodes,L):
 # Evaluate native exact ANP coefficient vectors, avoiding repeated symbolic parsing.
 deriv=[(q.diff(x).rep.to_dict(),q.diff(y).rep.to_dict())for q in L]
 out=[]
 for u,v,j,k in nodes:
  ku,kv=K.convert(u),K.convert(v);up=[ku**i for i in range(7)];vp=[kv**i for i in range(7)]
  g=[tuple(sum((c*up[a]*vp[b]for(a,b),c in row.items()),K.zero)for row in pair)for pair in deriv]
  assert all(sum((z[a]for z in g),K.zero)==K.zero for a in range(2))
  out.append(g)
 return out

def gap_for_node(index,node,g):
 coords=node[:2];segments=[];lower=None;zero_witness=None
 for axis in(0,1):
  other=1-axis
  for fixed in(-1,1):
   if(coords[axis]==-K.one and fixed<0)or(coords[axis]==K.one and fixed>0):continue
   lo=s.Integer(0)if coords[other]==-K.one else s.Integer(-1)
   hi=s.Integer(0)if coords[other]==K.one else s.Integer(1)
   klo,khi=K.convert(lo),K.convert(hi);breaks=[klo,khi]
   for i,grad in enumerate(g):
    if i==index or grad[other]==K.zero:continue
    t=-fixed*grad[axis]/grad[other]
    if ksign(t-klo)>=0 and ksign(t-khi)<=0:breaks.append(t)
   breaks=sorted(set(breaks),key=cmp_to_key(lambda a,b:ksign(a-b)))
   for t in breaks:
    a=[fixed*grad[axis]+t*grad[other]for grad in g]
    value=a[index]+sum((ksign(a[i])*a[i]for i in range(len(g))if i!=index),K.zero)
    assert ksign(value)>=0
    v=kfield(value)[0];lower=v if lower is None else min(lower,v)
    if value==K.zero and zero_witness is None:zero_witness={'axis':axis,'fixed':fixed,'t':encfield(t)}
   segments.append({'axis':axis,'fixed':fixed,'bounds':[str(lo),str(hi)],'breaks':[encfield(t)for t in breaks]})
 assert segments and lower is not None
 return{'index':index,'node':[encfield(q)for q in coords],'segments':segments,'gap_lower':str(F(lower,S)),'zero_witness':zero_witness}

def cubes(nodes,L,gaps):
 LT=list(map(terms,L));LX=[terms(q.diff(x))for q in L];LY=[terms(q.diff(y))for q in L]
 H=[[terms(q.diff((x,2))),terms(q.diff(x).diff(y)),terms(q.diff((y,2)))]for q in L]
 for rec,node in zip(gaps,nodes):
  if rec['zero_witness'] is not None or F(rec['gap_lower'])<=0:rec['status']='zero_gap';continue
  q=rec['index'];Z=[cfield(v)for v in node[:2]];cc=[(v[0]+v[1])//2 for v in Z];m=F(rec['gap_lower']);done=False
  for exponent in range(4,25):
   r=S>>exponent;B=[(c-r,c+r)for c in cc]
   good=True
   for axis,z in enumerate(node[:2]):
    if z!=-K.one and B[axis][0]<=-S:good=False
    if z!=K.one and B[axis][1]>=S:good=False
   if not good:continue
   Llo=centered(LT[q],LX[q],LY[q],*B)[0]
   if Llo<=0:continue
   Hbounds=[]
   for rows in H:
    vals=[evaluate(p,*B)for p in rows]
    Hbounds.append(max(abs(z)for z in vals[0])+2*max(abs(z)for z in vals[1])+max(abs(z)for z in vals[2]))
   Hsum=sum(Hbounds);R=max(max(B[a][1]-Z[a][0],Z[a][1]-B[a][0])for a in range(2))
   if F(R*Hsum,S*S)>=m/2:continue
   rec.update(status='accepted',B=encbox(B),R=str(F(R,S)),H=str(F(Hsum,S)),H_i=[str(F(v,S))for v in Hbounds],Lq_lower=str(F(Llo,S)));done=True;break
  if not done:rec['status']='no_cube'
 return gaps

def build_node_certificates(nodes,L,with_cubes=True):
 gs=node_gradients(nodes,L);gaps=[]
 for i,(node,g)in enumerate(zip(nodes,gs)):
  rec=gap_for_node(i,node,g);gaps.append(rec)
  print(json.dumps({'node':i,'label':node[2:],'gap_lower':rec['gap_lower'],'zero':rec['zero_witness']is not None}),file=sys.stderr,flush=True)
 return cubes(nodes,L,gaps)if with_cubes else gaps

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--gaps-only',action='store_true');args=ap.parse_args();t0=time.time()
 nodes,L=construct();records=build_node_certificates(nodes,L,not args.gaps_only)
 result={'format':'a5-n7-nodes-v1','n':7,'precision':PREC,'nodes':records,'summary':{'nodes':len(nodes),'positive_gaps':sum(r['zero_witness']is None and F(r['gap_lower'])>0 for r in records),'accepted_cubes':sum(r.get('status')=='accepted'for r in records),'seconds':time.time()-t0,'backend':str(s.external.gmpy.GROUND_TYPES),'scope':'exact node cone predicates only; no maxima count'}}
 open(args.output,'w').write(json.dumps(result,separators=(',',':'),sort_keys=True));print(json.dumps(result['summary']),flush=True)
