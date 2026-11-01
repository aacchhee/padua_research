"""Small exact value certificate for n8 global argmax, after a count certificate.

The independent checker must replay every bound, rather than trust this output.
"""
import json,gzip,argparse,hashlib,sys
from functools import lru_cache
from a5_n8_boxes import *

def exact_abs(v):
 if v==K.zero:return v
 sg=ksign(v);assert sg in(-1,1),'undecided exact corner sign'
 return sg*v

def decI(I):return(rat(F(I[0]))[0],rat(F(I[1]))[1])
def pathbox(path):
 Q=[(-S,S),(-S,S)]
 for bit in path:
  a=0 if Q[0][1]-Q[0][0]>=Q[1][1]-Q[1][0]else 1;m=sum(Q[a])//2
  Q[a]=(Q[a][0],m)if bit=='0'else(m,Q[a][1])
 return Q

def produce(cert):
 nodes,L=construct();LT=list(map(terms,L));LX=[terms(q.diff(x))for q in L];LY=[terms(q.diff(y))for q in L]
 @lru_cache(None)
 def P(mask):return sum((1 if mask>>i&1 else -1)*L[i]for i in range(45))
 @lru_cache(None)
 def PT(mask):return terms(P(mask))
 def masklist(Q):
  sg=[sign(centered(LT[i],LX[i],LY[i],*Q))for i in range(45)];amb=[i for i,v in enumerate(sg)if not v];fixed=sum(1<<i for i,v in enumerate(sg)if v>0)
  return[fixed+sum(1<<i for j,i in enumerate(amb)if bits>>j&1)for bits in range(1<<len(amb))]
 flatmax=-10*S;flatn=0
 for leaf in cert['leaves']:
  indices=[i for i,v in enumerate(leaf.get('patterns',[]))if v['code']in('flat','factor')]
  if not indices:continue
  Q=pathbox(leaf['path']);masks=masklist(Q)
  for i in indices:
   v=evaluate(PT(masks[i]),*Q);flatmax=max(flatmax,v[1]);flatn+=1
 interior=[]
 for root in cert['interior_roots']:
  v=evaluate(PT(root['mask']),*[decI(I)for I in root['R']]);interior.append({'id':root['id'],'enclosure':[str(F(z,S))for z in v]})
 edges=[];edgeflat=0
 for edge in cert['edges']:
  a,side=edge['axis'],edge['side'];normal=(x,y)[a];t=(y,x)[a]
  for row in edge['patterns']:
   p=P(row['mask']);q=p.eval(normal,side)
   if row['kind']=='flat':assert q.degree()<=0 and q.eval(0)in(-1,1);edgeflat+=1;continue
   for point in row['points']:
    if point['code']!='root':continue
    T=decI(point['interval']);Q=[(side*S,side*S),T]if a==0 else[T,(side*S,side*S)];v=evaluate(terms(q),*Q);edges.append({'id':point['id'],'enclosure':[str(F(z,S))for z in v]})
 corners=[]
 for u,v in((-1,-1),(1,-1)):
  vals=[K.convert(q.eval(x,u).eval(y,v))for q in L];value=sum((exact_abs(c)for c in vals),K.zero);corners.append(value)
 assert corners[0]==corners[1];C=corners[0];CI=cfield(C);upper=max([S,flatmax]+[int(F(r['enclosure'][1])*S)for r in interior+edges]);assert upper<CI[0];cut=F(upper+CI[0],2*S)
 return{'format':'a5-n8-global-v1','cut':str(cut),'corner_value':encfield(C),'bounded_codes':['flat','factor'],'node_value':'1','exception_leaf_occurrences':flatn,'exception_upper':str(F(flatmax,S)),'edge_flat_patterns':edgeflat,'interior_values':interior,'edge_values':edges,'complete':True}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('certificate');ap.add_argument('--output',required=True);args=ap.parse_args();raw=open(args.certificate,'rb').read();cert=json.loads(gzip.decompress(raw));assert cert['summary']['complete'];out=produce(cert);out['certificate_sha256']=hashlib.sha256(raw).hexdigest();out['source_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();open(args.output,'w').write(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({'complete':out['complete'],'flat_occurrences':out['exception_leaf_occurrences'],'flat_upper':out['exception_upper'],'interior_values':len(out['interior_values']),'edge_values':len(out['edge_values']),'corner_value':out['corner_value']}))
