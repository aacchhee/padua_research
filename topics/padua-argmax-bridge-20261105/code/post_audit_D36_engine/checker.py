"""D36 generic single-degree final-witness checker; no oracle, discovery or work on import."""
from fractions import Fraction as F
PI_LO=F(157,50)
PI_HI=F(22,7)
MAX_S=256
MAX_NODES=2047
MAX_DEPTH=18
def degree(n):
 if type(n) is not int or not 41<=n<=4095:raise ValueError('integer degree41..4095 required')
 return n

def actual_keys(n):
 degree(n)
 if n>=1024:raise ValueError('actual-point branch is only below1024')
 return ((F(1,4*n),F(0)),(F(0),F(3,16*(n+1))),(F(1,4*n),F(3,16*(n+1))))

def floor_identity(n):
 degree(n)
 if n<64:tier='D29-radius41: max(1/512,min(1/32,B_n(r_B)))'
 elif n<160:tier='accepted C02: max(1/64,min(1/20,B_n(r_B)))'
 elif n<512:tier='accepted C02: max(1/32,min(1/20,B_n(r_B)))'
 else:tier='accepted D29-floor512: 1/20'
 return {'tier':tier,'domain':'actual noncorner signed rho<=r_B<=1/2 only'}

def corner_identity(n):
 degree(n)
 if n<1024:return {'kind':'ACTUAL_THREE','theorem':'accepted D08/D32 pi/4 by3pi/16; exact pi^4 losses'}
 return {'kind':'ANALYTIC_D27','theorem':'accepted D27-wide-corner for every n>=1024','closed_patch':'[0,pi/4]^2 at both parity-correct actual corners','radial_squared_loss':'1/8','dependencies':['D27-global-norm','D20 full-phase error','D16 actual-origin allowance','completed-model','computer-assisted PD-T271','D02 uniform limit']}


def canonical(a,b):
 if not all(isinstance(x,F) for x in (a,b)) or not (0<=a<=1 and 0<=b<=1):raise ValueError('unit-square Fraction vertex')
 if a+b>1:a,b=1-a,1-b
 return min((a,b),(b,a)) if a+b==1 else (a,b)

def grid():
 return sorted({canonical(F(i,4),F(j,4)) for i in range(5) for j in range(5-i)})

def vertices(box):
 al,ah,bl,bh=box
 return {canonical(a,b) for a in (al,ah) for b in (bl,bh)}

def theta(n,box):
 degree(n)
 al,ah,bl,bh=box
 return PI_HI**2*((ah-al)**2+F(n,n+1)**2*(bh-bl)**2)/8

def radius_floor(n,box):
 degree(n);_,ah,_,bh=box;r=min(F(1,2),PI_HI*(ah+bh))
 if n>=512:delta=F(1,20)
 else:
  a=1-r*r/4;U=F(347,1000)*a-F(157,500)*r;V=F(17,20)*a-r/2;W=F(779,750)*a-F(5,6)*r
  B=F(11711,48400)*U-F(120,157*n)*V-F(250,157*n)*W-F(100,3*n*n)*V
  uniform=F(1,512) if n<64 else (F(1,64) if n<160 else F(1,32))
  cap=F(1,32) if n<64 else F(1,20)
  delta=max(uniform,min(cap,B))
 if not 0<=r<=F(1,2) or delta<=0:raise ValueError('actual-near floor domain')
 return r,delta


def ceiling(x):
 if not isinstance(x,F) or x<=0:raise ValueError('positive exact norm input')
 return F(-(-x.numerator//x.denominator))

def coarse_norm(uppers):
 if set(uppers)!=set(grid()) or len(uppers)!=13 or any(not isinstance(x,F) or x<0 for x in uppers.values()):raise ValueError('complete13 coarse upper keys')
 return ceiling(F(784,663)*max(uppers.values()))

def corner(n,L,uppers,M,require=True):
 degree(n)
 if n>=1024:
  if uppers!=[]:raise ValueError("analytic branch must not contain actual-point data")
  return corner_identity(n)
 if not isinstance(L,F) or L<=0 or len(uppers)!=3 or any(not isinstance(x,F) or x<0 for x in uppers) or not isinstance(M,F) or M<=0:raise ValueError('fresh exact corner premises')
 u,v=F(1,32),F(9,512);losses=[L-x for x in uppers]
 q=min(losses[0]/u,losses[1]/v,losses[2]/(u+v))
 t=M*PI_HI**4*max(u,F(n,n+1)**4*v)/6;gap=q-t
 if require and gap<=0:raise ValueError('strict actual-corner pi-fourth criterion failed')
 return {'u_prime':str(u),'v_prime':str(v),'losses':list(map(str,losses)),'q':str(q),'threshold':str(t),'gap':str(gap),'radial_squared_coefficient_lower':str(gap/(2*PI_HI**2))}

def leaf(n,box,V,L,M):
 degree(n)
 al,ah,bl,bh=box
 if al+bl>1:return 'OUTSIDE',None,[],None,None
 if not isinstance(V,F) or V<0 or not isinstance(L,F) or L<=0 or not isinstance(M,F) or M<=0:raise ValueError('exact Peano premises')
 U=V+theta(n,box)*M;r,delta=radius_floor(n,box);low=al+bl;high=min(ah+bh,F(1))
 if U<L:return 'FAR',U,[('FAR',L-U)],r,delta
 if 2*PI_HI*high<=1 and U-delta<L:return 'NEAR',U,[('NEAR',L-U+delta)],r,delta
 near=low<=1/(2*PI_LO);far=high>=1/(2*PI_HI)
 if (near and U-delta>=L) or (far and U>=L):return None,U,[],r,delta
 req=[]
 if near:req.append(('SPLIT_NEAR',L-U+delta))
 if far:req.append(('SPLIT_FAR',L-U))
 return 'SPLIT',U,req,r,delta

def decode(n,doc):
 degree(n)
 if not isinstance(doc,dict) or set(doc)!={'format','n','preorder'} or doc['format']!='D36-midpoint-v1' or type(doc['n']) is not int or doc['n']!=n:raise ValueError('complete tree degree/schema')
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

def tree_norm(n,leaves,uppers):
 degree(n)
 keys=tree_keys(leaves)
 if not set(keys)<=set(uppers) or any(not isinstance(uppers[k],F) or uppers[k]<0 for k in keys):raise ValueError('complete final-corner uppers')
 if any(not 0<=theta(n,box)<1 for _,box in leaves if box[0]+box[2]<=1):return None,None
 R=max(max(uppers[k] for k in vertices(box))/(1-theta(n,box)) for _,box in leaves if box[0]+box[2]<=1)
 return ceiling(R),R

def select_norm(n,leaves,uppers,Mcoarse):
 degree(n)
 Mt,R=tree_norm(n,leaves,uppers)
 # Predeclared rule; TREE wins ties. This is never tried after a failed final check.
 if Mt is not None and Mt<=Mcoarse:return 'TREE',Mt,R
 return 'GRID',Mcoarse,R

def verify(n,doc,uppers,L,actual,method,claimed_M):
 degree(n)
 leaves=decode(n,doc);needed=set(tree_keys(leaves))
 if method=='GRID':needed.update(grid())
 elif method!='TREE':raise ValueError('norm witness method')
 if set(uppers)!=needed or len(uppers)>MAX_S or any(not isinstance(x,F) or x<0 for x in uppers.values()):raise ValueError('complete and only retained S premises')
 if (F(0),F(0)) not in needed:raise ValueError('origin premise absent')
 if not isinstance(L,F) or not 0<L<=uppers[(F(0),F(0))]:raise ValueError('fresh origin lower/upper consistency')
 if method=='GRID':M=coarse_norm({k:uppers[k] for k in grid()});R=None
 else:
  M,R=tree_norm(n,leaves,uppers)
  if M is None:raise ValueError('chosen tree norm has invalid absorption theta')
 if not isinstance(claimed_M,F) or M!=claimed_M:raise ValueError('claimed norm differs from retained proof')
 witness=corner(n,L,actual,M);counts={};margins={};floors=[]
 for ident,box in leaves:
  V=max(uppers[k] for k in vertices(box)) if box[0]+box[2]<=1 else None
  tag,U,required,r,delta=leaf(n,box,V,L,M)
  if tag is None:raise ValueError('final strict phase leaf failed')
  counts[tag]=counts.get(tag,0)+1
  if r is not None:floors.append((r,delta))
  for label,gap in required:
   if gap<=0:raise ValueError('strict margin bookkeeping')
   margins[label]=min(margins.get(label,gap),gap)
 return {'n':n,'nodes':len(doc['preorder']),'leaves':len(leaves),'S_premises':len(uppers),'norm_method':method,'M':str(M),'R_tree':None if R is None else str(R),'L':str(L),'leaf_counts':counts,'minimum_strict_margins':{k:str(v) for k,v in margins.items()},'minimum_used_floor':str(min(x[1] for x in floors)),'corner':witness,'floor':floor_identity(n)}

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

ESSENTIAL_KEYS={'format','status','n','tree','pi_bracket','S_upper_columns','S_upper_rows','origin_lower_hex','lambda_upper_columns','lambda_upper_rows','norm','floor','corner','verification','freeze','whole_raw_evidence','execution_role','CPU_stages','CPU_through_receipt_start','scope'}

def parse_essential(doc,expected_source_identity):
 """Strict D36-v1 only. Old numbers are diagnostics, never a fresh oracle."""
 if not isinstance(doc,dict) or set(doc)!=ESSENTIAL_KEYS or doc['format']!='D36-kept-proof-v1':raise ValueError('strict essential schema/version')
 n=degree(doc['n'])
 if doc['status']!='PROVISIONAL_REQUIRES_FINAL_ACCOUNTING_AND_RETURN0' or doc['pi_bracket']!=['157/50','22/7']:raise ValueError('essential status/pi bracket')
 ident=doc['freeze']
 if not isinstance(ident,dict) or set(ident)!={'path','bytes','sha256'} or type(ident['bytes']) is not int or ident['bytes']<=0 or not isinstance(ident['path'],str) or not isinstance(expected_source_identity,dict) or ident['sha256']!=expected_source_identity.get('sha256') or ident['bytes']!=expected_source_identity.get('bytes'):raise ValueError('unrecognized source/arithmetic identity')
 if doc['floor']!=floor_identity(n) or doc['corner']!=corner_identity(n):raise ValueError('floor/corner theorem domain identity')
 if doc['S_upper_columns']!=['a_pi','b_pi','outward_upper_hex'] or doc['lambda_upper_columns']!=['physical_xi_pi','physical_zeta_pi','outward_upper_hex']:raise ValueError('point argument/API columns')
 rows=doc['S_upper_rows']
 if not isinstance(rows,list) or not 1<=len(rows)<=MAX_S:raise ValueError('retained S row count')
 uppers={}
 for row in rows:
  if not isinstance(row,list) or len(row)!=3:raise ValueError('retained S row shape')
  a,b=map(rational,row[:2]);key=(a,b)
  if canonical(a,b)!=key or key in uppers:raise ValueError('duplicate/noncanonical S key')
  value=exact_hex(row[2])
  if value<0:raise ValueError('negative old upper diagnostic')
  uppers[key]=value
 norm=doc['norm']
 if not isinstance(norm,dict) or set(norm)!={'method','M'} or norm['method'] not in ('TREE','GRID'):raise ValueError('norm proof selector')
 oldM=rational(norm['M'])
 if oldM<=0 or oldM.denominator!=1:raise ValueError('positive integer norm field')
 leaves=decode(n,doc['tree']);needed=set(tree_keys(leaves))
 if norm['method']=='GRID':needed.update(grid())
 if set(uppers)!=needed or (F(0),F(0)) not in needed:raise ValueError('complete and only norm/tree point premises')
 actual_rows=doc['lambda_upper_rows'];keys=actual_keys(n) if n<1024 else ()
 if not isinstance(actual_rows,list) or len(actual_rows)!=len(keys):raise ValueError('actual/analytic branch row closure')
 actual=[]
 for row,key in zip(actual_rows,keys):
  if not isinstance(row,list) or len(row)!=3 or tuple(map(rational,row[:2]))!=key:raise ValueError('registered physical actual key/order')
  value=exact_hex(row[2])
  if value<0:raise ValueError('negative actual upper diagnostic')
  actual.append(value)
 v=doc['verification'];required_verification={'n','nodes','leaves','S_premises','norm_method','M','R_tree','L','leaf_counts','minimum_strict_margins','minimum_used_floor','corner','floor'}
 if not isinstance(v,dict) or set(v)!=required_verification or type(v['n']) is not int or v['n']!=n:raise ValueError('verification record schema; booleans are not proof')
 for field,value in (('nodes',len(doc['tree']['preorder'])),('leaves',len(leaves)),('S_premises',len(needed))):
  if type(v[field]) is not int or v[field]!=value:raise ValueError('verification geometry count shape')
 if v['norm_method']!=norm['method'] or v['M']!=norm['M'] or v['floor']!=floor_identity(n):raise ValueError('verification method/degree-floor metadata')
 rational(v['L']);rational(v['minimum_used_floor'])
 if v['R_tree'] is not None:rational(v['R_tree'])
 if not isinstance(v['leaf_counts'],dict) or any(type(count) is not int or count<0 for count in v['leaf_counts'].values()) or not isinstance(v['minimum_strict_margins'],dict) or not isinstance(v['corner'],dict):raise ValueError('verification record types')
 for label,value in v['minimum_strict_margins'].items():
  if not isinstance(label,str) or rational(value)<=0:raise ValueError('strict margin metadata type')
 if n<1024:
  c=v['corner'];fields={'u_prime','v_prime','losses','q','threshold','gap','radial_squared_coefficient_lower'}
  if set(c)!=fields or not isinstance(c['losses'],list) or len(c['losses'])!=3:raise ValueError('actual-corner metadata shape')
  for value in c['losses']+[c[k] for k in fields-{'losses'}]:rational(value)
 elif v['corner']!=corner_identity(n):raise ValueError('analytic corner metadata identity')
 if not isinstance(doc['CPU_stages'],list) or not isinstance(doc['scope'],str) or not isinstance(doc['execution_role'],str):raise ValueError('receipt metadata types')
 raw=doc['whole_raw_evidence']
 if not isinstance(raw,dict) or set(raw)!={'path','bytes','sha256'} or type(raw['bytes']) is not int or raw['bytes']<=0 or not isinstance(raw['path'],str) or not isinstance(raw['sha256'],str) or len(raw['sha256'])!=64 or any(c not in '0123456789abcdef' for c in raw['sha256']):raise ValueError('whole raw identity shape')
 oldL=exact_hex(doc['origin_lower_hex'])
 if not 0<oldL<=uppers[(F(0),F(0))]:raise ValueError('old origin enclosure shape')
 return {'n':n,'tree':doc['tree'],'method':norm['method'],'keys':sorted(needed),'old_uppers':uppers,'old_actual':actual,'old_L':oldL,'old_M':oldM}

def verify_essential(doc,expected_source_identity):
 p=parse_essential(doc,expected_source_identity)
 return verify(p['n'],p['tree'],p['old_uppers'],p['old_L'],p['old_actual'],p['method'],p['old_M'])
