"""Independent exact geometry/norm/corner application, no author checker import."""
import json, math
from fractions import Fraction as Q
N=2048; K=Q(N,N+1); P=Q(22,7); PLO=Q(157,50)
ACTUAL=((Q(1,8192),Q(0)),(Q(0),Q(1,10928)),(Q(1,8192),Q(1,10928)))
def strict_json(path):
 def pairs(items):
  d={}
  for k,v in items:
   if k in d:raise ValueError('duplicate key')
   d[k]=v
  return d
 def bad(s):raise ValueError(s)
 return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=bad)
def canonical(a,b):
 assert 0<=a<=1 and 0<=b<=1
 if a+b>1:a,b=1-a,1-b
 # Inside T no other representative exists except the complementary
 # hypotenuse pair, induced by (-a,-b)+(1,1).
 return min((a,b),(b,a)) if a+b==1 else (a,b)
def geometry(cert):
 assert set(cert)=={'format','n','preorder'} and cert['format']=='D15-midpoint-v1'
 assert type(cert['n']) is int and cert['n']==N
 seq=cert['preorder'];assert isinstance(seq,str) and 0<len(seq)<=2048
 at=0;leaves=[];depthmax=0
 def walk(box,depth):
  nonlocal at,depthmax
  assert at<len(seq) and depth<=64
  depthmax=max(depthmax,depth);token=seq[at];at+=1
  if token=='.':leaves.append(box);return
  assert token in 'ab'
  left=list(box);right=list(box);offset=0 if token=='a' else 2
  midpoint=(box[offset]+box[offset+1])/2
  assert box[offset]<midpoint<box[offset+1]
  left[offset+1]=midpoint;right[offset]=midpoint
  walk(tuple(left),depth+1);walk(tuple(right),depth+1)
 walk((Q(0),Q(1),Q(0),Q(1)),0);assert at==len(seq)
 grid=[(Q(i,4),Q(j,4)) for i in range(5) for j in range(5-i)]
 squares=[(Q(i,4),Q(i+1,4),Q(j,4),Q(j+1,4)) for i in range(4) for j in range(4-i)]
 raw={(a,b) for al,ah,bl,bh in squares for a in (al,ah) for b in (bl,bh)}
 folded={(1-a,1-b) if a+b>1 else (a,b) for a,b in raw}
 assert len(squares)==10 and len(raw)==19 and folded==set(grid)
 points={canonical(a,b) for a,b in grid}
 assert len(points)==13
 for al,ah,bl,bh in leaves:
  if al+bl<=1:points.update(canonical(a,b) for a in (al,ah) for b in (bl,bh))
 assert len(points)==51 and len(leaves)==39 and len(seq)==77
 # Cross-check shortcut against finite even-lattice orbit, without author code.
 for a,b in raw|{(a,b) for al,ah,bl,bh in leaves for a in (al,ah) for b in (bl,bh)}:
  orbit={(s*a+i,t*b+j) for s in (-1,1) for t in (-1,1) for i in range(-2,3) for j in range(-2,3) if (i+j)%2==0 and s*a+i>=0 and t*b+j>=0 and s*a+i+t*b+j<=1}
  assert canonical(a,b)==min(orbit)
 return leaves,sorted(points),grid,depthmax

def endpoints(hexes):
 assert len(hexes)==3
 vals=[float.fromhex(s) for s in hexes]
 assert all(math.isfinite(x) for x in vals) and 0<=vals[0]<=vals[1] and vals[2]>=0
 assert [x.hex() for x in vals]==hexes
 return Q.from_float(vals[0]),Q.from_float(vals[1])
def application(cert,rows):
 leaves,points,grid,depth=geometry(cert)
 intervals={}
 for row in rows:
  api,a,b,lo,hi,rad,counts,duration=row
  assert api in ('S','lambda') and 0<=duration<=20
  pair=(Q(a),Q(b));assert [str(x) for x in pair]==[a,b]
  key=(api,*pair);assert key not in intervals
  assert len(counts)==(6 if api=='S' else 13) and all(type(c) is int and c>=0 for c in counts)
  intervals[key]=endpoints([lo,hi,rad])
 assert set(intervals)=={('S',*p) for p in points}|{('lambda',*p) for p in ACTUAL}
 L=intervals['S',Q(0),Q(0)][0];assert L>0
 gridrows=[{'raw':list(map(str,p)),'canonical':list(map(str,canonical(*p))),'upper':str(intervals['S',*canonical(*p)][1])} for p in grid]
 V=max(Q(x['upper']) for x in gridrows);theta=P*P*(1+K*K)/128
 assert V>0 and 0<theta<1
 exact=V/(1-theta);M=Q((exact.numerator+exact.denominator-1)//exact.denominator)
 assert M==42 and M-1<exact<=M
 losses=[L-intervals['lambda',*p][1] for p in ACTUAL]
 u=Q(1,32);v=Q(9,512)
 q=min(losses[0]/u,losses[1]/v,losses[2]/(u+v))
 threshold=M*P**4*max(u,K**4*v)/6;gap=q-threshold
 assert gap>0 and PLO/4>=Q(1,2) and PLO*Q(3,16)>=Q(1,2)
 counts={};margins={};details=[]
 for box in leaves:
  al,ah,bl,bh=box
  if al+bl>1:mode='OUTSIDE';bound=None;delta=None
  else:
   values=[intervals['S',*canonical(a,b)][1] for a in (al,ah) for b in (bl,bh)]
   bound=max(values)+M*P**2*((ah-al)**2+K**2*(bh-bl)**2)/8
   if bound<L:mode='FAR';delta=L-bound
   elif 2*P*min(ah+bh,1)<=1 and bound-Q(1,32)<L:mode='NEAR';delta=L-bound+Q(1,32)
   else:raise AssertionError('leaf not accepted by whole FAR/NEAR; no proxy rescue')
   assert delta>0;margins[mode]=min(margins.get(mode,delta),delta)
  counts[mode]=counts.get(mode,0)+1
  details.append([list(map(str,box)),mode,None if bound is None else str(bound),None if delta is None else str(delta)])
 assert counts=={'NEAR':5,'FAR':32,'OUTSIDE':2}
 return {'norm':{'grid':gridrows,'V':str(V),'theta':str(theta),'Mceil':str(M)},'L':str(L),
 'corner':{'losses':list(map(str,losses)),'q':str(q),'threshold':str(threshold),'gap':str(gap),'barrier_coefficient_lower':str(gap/P**2)},
 'cover':{'visited':len(cert['preorder']),'vertices':len(points),'leaf_counts':counts,'minimum_strict_margins':{k:str(v) for k,v in margins.items()}},'max_depth':depth},details
