"""D34 exact n41 final-witness checker; no oracle, discovery or work on import."""
from fractions import Fraction as F
N=41
KAPPA=F(41,42)
PI_LO=F(157,50)
PI_HI=F(22,7)
MAX_S=256
MAX_NODES=2047
MAX_DEPTH=18
ACTUAL=((F(1,164),F(0)),(F(0),F(1,224)),(F(1,164),F(1,224)))

def canonical(a,b):
 if not all(isinstance(x,F) for x in (a,b)) or not (0<=a<=1 and 0<=b<=1):raise ValueError('unit-square Fraction vertex')
 if a+b>1:a,b=1-a,1-b
 return min((a,b),(b,a)) if a+b==1 else (a,b)

def grid():
 return sorted({canonical(F(i,4),F(j,4)) for i in range(5) for j in range(5-i)})

def vertices(box):
 al,ah,bl,bh=box
 return {canonical(a,b) for a in (al,ah) for b in (bl,bh)}

def theta(box):
 al,ah,bl,bh=box
 return PI_HI**2*((ah-al)**2+KAPPA**2*(bh-bl)**2)/8

def radius_floor(box):
 _,ah,_,bh=box;r=min(F(1,2),PI_HI*(ah+bh));a=1-r*r/4
 U=F(347,1000)*a-F(157,500)*r;V=F(17,20)*a-r/2;W=F(779,750)*a-F(5,6)*r
 B=F(11711,48400)*U-F(120,157*N)*V-F(250,157*N)*W-F(100,3*N*N)*V
 delta=max(F(1,512),min(F(1,32),B))
 if not 0<=r<=F(1,2) or delta<=0:raise ValueError('actual-near floor domain')
 return r,delta

def ceiling(x):
 if not isinstance(x,F) or x<=0:raise ValueError('positive exact norm input')
 return F(-(-x.numerator//x.denominator))

def coarse_norm(uppers):
 if set(uppers)!=set(grid()) or len(uppers)!=13 or any(not isinstance(x,F) or x<0 for x in uppers.values()):raise ValueError('complete13 coarse upper keys')
 return ceiling(F(784,663)*max(uppers.values()))

def corner(L,uppers,M,require=True):
 if not isinstance(L,F) or L<=0 or len(uppers)!=3 or any(not isinstance(x,F) or x<0 for x in uppers) or not isinstance(M,F) or M<=0:raise ValueError('fresh exact corner premises')
 u,v=F(1,32),F(9,512);losses=[L-x for x in uppers]
 q=min(losses[0]/u,losses[1]/v,losses[2]/(u+v))
 t=M*PI_HI**4*max(u,KAPPA**4*v)/6;gap=q-t
 if require and gap<=0:raise ValueError('strict actual-corner pi-fourth criterion failed')
 return {'u_prime':str(u),'v_prime':str(v),'losses':list(map(str,losses)),'q':str(q),'threshold':str(t),'gap':str(gap),'radial_squared_coefficient_lower':str(gap/(2*PI_HI**2))}

def leaf(box,V,L,M):
 al,ah,bl,bh=box
 if al+bl>1:return 'OUTSIDE',None,[],None,None
 if not isinstance(V,F) or V<0 or not isinstance(L,F) or L<=0 or not isinstance(M,F) or M<=0:raise ValueError('exact Peano premises')
 U=V+theta(box)*M;r,delta=radius_floor(box);low=al+bl;high=min(ah+bh,F(1))
 if U<L:return 'FAR',U,[('FAR',L-U)],r,delta
 if 2*PI_HI*high<=1 and U-delta<L:return 'NEAR',U,[('NEAR',L-U+delta)],r,delta
 near=low<=1/(2*PI_LO);far=high>=1/(2*PI_HI)
 if (near and U-delta>=L) or (far and U>=L):return None,U,[],r,delta
 req=[]
 if near:req.append(('SPLIT_NEAR',L-U+delta))
 if far:req.append(('SPLIT_FAR',L-U))
 return 'SPLIT',U,req,r,delta

def decode(doc):
 if not isinstance(doc,dict) or set(doc)!={'format','n','preorder'} or doc['format']!='D34-midpoint-v1' or type(doc['n']) is not int or doc['n']!=N:raise ValueError('n41 complete tree schema')
 tokens=doc['preorder']
 if not isinstance(tokens,str) or not 1<=len(tokens)<=MAX_NODES:raise ValueError('node cap/type')
 pos=0;leaves=[]
 def visit(box,depth):
  nonlocal pos
  if pos>=len(tokens) or depth>MAX_DEPTH:raise ValueError('missing child/depth cap')
  ident=pos;token=tokens[pos];pos+=1
  if token=='.':leaves.append((ident,box));return
  al,ah,bl,bh=box
  if token=='a':
   t=(al+ah)/2;left,right=(al,t,bl,bh),(t,ah,bl,bh)
  elif token=='b':
   t=(bl+bh)/2;left,right=(al,ah,bl,t),(al,ah,t,bh)
  else:raise ValueError('tree token')
  visit(left,depth+1);visit(right,depth+1)
 visit((F(0),F(1),F(0),F(1)),0)
 if pos!=len(tokens):raise ValueError('trailing subtree')
 return leaves

def tree_keys(leaves):
 return sorted(set().union(*(vertices(box) for _,box in leaves if box[0]+box[2]<=1)))

def tree_norm(leaves,uppers):
 keys=tree_keys(leaves)
 if not set(keys)<=set(uppers) or any(not isinstance(uppers[k],F) or uppers[k]<0 for k in keys):raise ValueError('complete final-corner uppers')
 if any(not 0<=theta(box)<1 for _,box in leaves if box[0]+box[2]<=1):return None,None
 R=max(max(uppers[k] for k in vertices(box))/(1-theta(box)) for _,box in leaves if box[0]+box[2]<=1)
 return ceiling(R),R

def select_norm(leaves,uppers,Mcoarse):
 Mt,R=tree_norm(leaves,uppers)
 # Predeclared rule; TREE wins ties. This is never tried after a failed final check.
 if Mt is not None and Mt<=Mcoarse:return 'TREE',Mt,R
 return 'GRID',Mcoarse,R

def verify(doc,uppers,L,actual,method,claimed_M):
 if type(N) is not int or N!=41:raise ValueError('sole degree41')
 leaves=decode(doc);needed=set(tree_keys(leaves))
 if method=='GRID':needed.update(grid())
 elif method!='TREE':raise ValueError('norm witness method')
 if set(uppers)!=needed or len(uppers)>MAX_S or any(not isinstance(x,F) or x<0 for x in uppers.values()):raise ValueError('complete and only retained S premises')
 if (F(0),F(0)) not in needed:raise ValueError('origin premise absent')
 if not isinstance(L,F) or not 0<L<=uppers[(F(0),F(0))]:raise ValueError('fresh origin lower/upper consistency')
 if method=='GRID':M=coarse_norm({k:uppers[k] for k in grid()});R=None
 else:
  M,R=tree_norm(leaves,uppers)
  if M is None:raise ValueError('chosen tree norm has invalid absorption theta')
 if not isinstance(claimed_M,F) or M!=claimed_M:raise ValueError('claimed norm differs from retained proof')
 witness=corner(L,actual,M);counts={};margins={};floors=[]
 for ident,box in leaves:
  V=max(uppers[k] for k in vertices(box)) if box[0]+box[2]<=1 else None
  tag,U,required,r,delta=leaf(box,V,L,M)
  if tag is None:raise ValueError('final strict phase leaf failed')
  counts[tag]=counts.get(tag,0)+1
  if r is not None:floors.append((r,delta))
  for label,gap in required:
   if gap<=0:raise ValueError('strict margin bookkeeping')
   margins[label]=min(margins.get(label,gap),gap)
 return {'n':N,'nodes':len(doc['preorder']),'leaves':len(leaves),'S_premises':len(uppers),'norm_method':method,'M':str(M),'R_tree':None if R is None else str(R),'L':str(L),'leaf_counts':counts,'minimum_strict_margins':{k:str(v) for k,v in margins.items()},'minimum_used_floor':str(min(x[1] for x in floors)),'corner':witness,'floor':'accepted D29 radius41; actual noncorner rho<=r_B only'}

def exact_hex(s):
 import math
 if not isinstance(s,str) or len(s)>64:raise ValueError('bounded binary64 hex')
 x=float.fromhex(s)
 if not math.isfinite(x) or x.hex()!=s:raise ValueError('canonical finite outward endpoint')
 return F.from_float(x)

def rational(s):
 if not isinstance(s,str) or len(s)>256:raise ValueError('bounded rational string')
 q=F(s)
 if str(q)!=s:raise ValueError('canonical rational string')
 return q

def verify_essential(doc):
 """Reconstruct proof from kept premises only. Final-account/EXIT0 remain separate.
 The endpoint enclosure/authentication premise still needs the execution and
 independent fresh replay; a hexadecimal value alone is never its proof.
 """
 if not isinstance(doc,dict) or doc.get('format')!='D34-kept-proof-v1' or type(doc.get('n')) is not int or doc['n']!=41 or doc.get('pi_bracket')!=['157/50','22/7']:raise ValueError('essential schema/degree/bracket')
 rows=doc.get('S_upper_rows')
 if not isinstance(rows,list) or not 1<=len(rows)<=MAX_S:raise ValueError('retained S row count')
 uppers={}
 for row in rows:
  if not isinstance(row,list) or len(row)!=3:raise ValueError('retained S row shape')
  a,b=map(rational,row[:2]);key=(a,b)
  if canonical(a,b)!=key or key in uppers:raise ValueError('duplicate/noncanonical S key')
  uppers[key]=exact_hex(row[2])
 actual_rows=doc.get('lambda_upper_rows')
 if not isinstance(actual_rows,list) or len(actual_rows)!=3:raise ValueError('all3 actual upper rows')
 actual=[]
 for row,key in zip(actual_rows,ACTUAL):
  if not isinstance(row,list) or len(row)!=3 or tuple(map(rational,row[:2]))!=key:raise ValueError('registered physical actual key/order')
  actual.append(exact_hex(row[2]))
 norm=doc.get('norm')
 if not isinstance(norm,dict) or set(norm)!={'method','M'}:raise ValueError('norm proof selector')
 return verify(doc['tree'],uppers,exact_hex(doc['origin_lower_hex']),actual,norm['method'],rational(norm['M']))
