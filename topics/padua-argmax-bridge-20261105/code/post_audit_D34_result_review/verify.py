"""Independent exact finite-witness reconstruction. No author checker import."""
from fractions import Fraction as Q
import math
P,QLO,K=Q(22,7),Q(157,50),Q(41,42)
ACT=((Q(1,164),Q(0)),(Q(0),Q(1,224)),(Q(1,164),Q(1,224)))

def need(x,message):
 if not x:raise ValueError(message)

def hexq(s):
 need(isinstance(s,str) and len(s)<65,'hex syntax')
 x=float.fromhex(s);need(math.isfinite(x) and x.hex()==s,'finite canonical hex')
 return Q.from_float(x)

def key(a,b):
 need(0<=a<=1 and 0<=b<=1,'unit-square key')
 if a+b>1:a,b=1-a,1-b
 if a+b==1 and b<a:a,b=b,a
 return a,b

def corners(b):
 x,X,y,Y=b
 return {key(a,c) for a in (x,X) for c in (y,Y)}

def boxes(tree):
 need(set(tree)=={'format','n','preorder'} and tree['format']=='D34-midpoint-v1' and type(tree['n']) is int and tree['n']==41,'tree schema')
 s=tree['preorder'];need(isinstance(s,str) and 0<len(s)<=2047,'tree length')
 pending=[((Q(0),Q(1),Q(0),Q(1)),0)];leaves=[]
 for token in s:
  need(bool(pending),'trailing tokens');b,d=pending.pop();need(d<=18,'depth')
  if token=='.':leaves.append(b);continue
  x,X,y,Y=b
  if token=='a':
   z=(x+X)/2;left=(x,z,y,Y);right=(z,X,y,Y)
  elif token=='b':
   z=(y+Y)/2;left=(x,X,y,z);right=(x,X,z,Y)
  else:raise ValueError('bad token')
  pending.extend([(right,d+1),(left,d+1)])
 need(not pending,'missing subtree');return leaves

def curvature(b):
 x,X,y,Y=b
 return P*P*((X-x)**2+K*K*(Y-y)**2)/8

def floor_at(b):
 r=min(Q(1,2),P*(b[1]+b[3]));a=1-r*r/4
 # Independent expansion of B_41(r), retaining each original scalar charge.
 u=(347*a-314*r)/1000;v=(17*a-10*r)/20;w=(1558*a-1250*r)/1500
 B=11711*u/48400-120*v/(157*41)-250*w/(157*41)-100*v/(3*41**2)
 return r,max(Q(1,512),min(Q(1,32),B))

def phase(b,V,L,M):
 x,X,y,Y=b
 if x+y>1:return 'OUTSIDE',None
 upper=V+curvature(b)*M;r,delta=floor_at(b)
 if upper<L:return 'FAR',L-upper
 if 2*P*min(X+Y,1)<=1 and upper-delta<L:return 'NEAR',L-upper+delta
 requirements=[]
 if x+y<=1/(2*QLO):requirements.append(L-upper+delta)
 if min(X+Y,1)>=1/(2*P):requirements.append(L-upper)
 need(requirements and min(requirements)>0,'strict closed split predicate')
 return 'SPLIT',min(requirements)

def check(doc,uppers=None,L=None,actual=None):
 need(doc['format']=='D34-kept-proof-v1' and type(doc['n']) is int and doc['n']==41 and doc['pi_bracket']==['157/50','22/7'],'degree/pi')
 leaves=boxes(doc['tree']);inside=[b for b in leaves if b[0]+b[2]<=1]
 required=set().union(*(corners(b) for b in inside))
 saved={}
 for a,b,h in doc['S_upper_rows']:
  z=Q(a),Q(b);need(key(*z)==z and z not in saved,'unique canonical key');saved[z]=hexq(h)
 need(len(saved)==64 and set(saved)==required,'complete exact64 final keys')
 if uppers is None:uppers=saved
 need(set(uppers)==required and all(isinstance(v,Q) and v>=0 for v in uppers.values()),'fresh uppers')
 if L is None:L=hexq(doc['origin_lower_hex'])
 need(isinstance(L,Q) and 0<L<=uppers[(Q(0),Q(0))],'fresh origin')
 stored_actual=[]
 for row,z in zip(doc['lambda_upper_rows'],ACT):
  need(tuple(map(Q,row[:2]))==z,'physical corner key');stored_actual.append(hexq(row[2]))
 need(len(doc['lambda_upper_rows'])==3,'three actual rows')
 if actual is None:actual=stored_actual
 need(len(actual)==3 and all(isinstance(v,Q) and v>=0 for v in actual),'fresh actual uppers')
 need(all(curvature(b)<1 for b in inside),'own-tree absorption')
 R=max(max(uppers[z] for z in corners(b))/(1-curvature(b)) for b in inside)
 M=Q((R.numerator+R.denominator-1)//R.denominator)
 need(doc['norm']=={'method':'TREE','M':str(M)},'selected independent tree norm')
 u,v=Q(1,32),Q(9,512)
 q=min((L-actual[0])/u,(L-actual[1])/v,(L-actual[2])/(u+v))
 threshold=M*P**4/192;need(q>threshold,'actual corner strict loss')
 counts={};margins={}
 for b in leaves:
  V=max(uppers[z] for z in corners(b)) if b in inside else None
  label,gap=phase(b,V,L,M);counts[label]=counts.get(label,0)+1
  if gap is not None:margins[label]=min(margins.get(label,gap),gap)
 return {'n':41,'nodes':len(doc['tree']['preorder']),'leaves':len(leaves),'S_points':len(uppers),'M':str(M),'R':str(R),'L':str(L),'counts':counts,'margins':{k:str(v) for k,v in margins.items()},'minimum_floor':str(min(floor_at(b)[1] for b in inside)),'corner_q':str(q),'corner_threshold':str(threshold),'corner_gap':str(q-threshold),'radial_coefficient':str((q-threshold)/(2*P*P))}

def controls(doc):
 import copy
 def rejects(f):
  try:f()
  except (ValueError,KeyError,TypeError):return
  raise AssertionError('negative synthetic control accepted')
 for s in ('a.','..','?'):
  t=dict(doc['tree'],preorder=s);rejects(lambda:boxes(t))
 rejects(lambda:boxes(dict(doc['tree'],n=True)))
 bad=copy.deepcopy(doc);bad['S_upper_rows'].pop();rejects(lambda:check(bad))
 bad=copy.deepcopy(doc);bad['norm']['M']='12';rejects(lambda:check(bad))
 rejects(lambda:check(doc,actual=[hexq(doc['origin_lower_hex'])]*3))
 tangent=(Q(1,2),Q(1),Q(1,2),Q(1))
 rejects(lambda:phase(tangent,Q(100),Q(1),Q(1)))
 need(key(Q(1,4),Q(1,2))==(Q(1,4),Q(1,2)),'no interior swap')
 return {'negative_controls':8,'canonicalization':True,'native_calls':0}
