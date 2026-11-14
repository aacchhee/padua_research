"""D28 generic exact static-tree absorption and physical cover predicates.
No endpoint values, native imports, or numerical discovery on import.
"""
from fractions import Fraction as F
N=6912
PI_LO=F(157,50)
PI_HI=F(22,7)
KAPPA=F(N,N+1)
TREE_SHA='5ff335b5e8c3a813b934f38b0938cf80bf29f546749651cd749e5ffc41c753d1'

def canonical(a,b):
 if not all(isinstance(x,F) for x in (a,b)) or not (0<=a<=1 and 0<=b<=1):raise ValueError('unit square rational vertices')
 if a+b>1:a,b=1-a,1-b
 return min((a,b),(b,a)) if a+b==1 else (a,b)

def decode(document):
 if not isinstance(document,dict) or set(document)!={'format','n','preorder'} or document['format']!='D19-midpoint-v1' or type(document['n']) is not int or document['n']!=2048:raise ValueError('frozen source tree schema')
 tokens=document['preorder']
 if not isinstance(tokens,str) or len(tokens)!=61:raise ValueError('fixed tree size')
 pos=0;leaves=[]
 def walk(box,depth):
  nonlocal pos
  if pos>=len(tokens) or depth>64:raise ValueError('missing sibling/depth')
  ident=pos;t=tokens[pos];pos+=1
  if t=='.':leaves.append((ident,box));return
  al,ah,bl,bh=box
  if t=='a':
   mid=(al+ah)/2;left,right=(al,mid,bl,bh),(mid,ah,bl,bh)
  elif t=='b':
   mid=(bl+bh)/2;left,right=(al,ah,bl,mid),(al,ah,mid,bh)
  else:raise ValueError('tree token')
  walk(left,depth+1);walk(right,depth+1)
 walk((F(0),F(1),F(0),F(1)),0)
 if pos!=len(tokens):raise ValueError('extra tree suffix')
 return leaves

def vertices(box):
 al,ah,bl,bh=box
 return {canonical(a,b) for a in (al,ah) for b in (bl,bh)}

def keys(leaves):
 return sorted(set().union(*(vertices(box) for _,box in leaves if box[0]+box[2]<=1)))

def theta(box):
 al,ah,bl,bh=box
 t=PI_HI**2*((ah-al)**2+KAPPA**2*(bh-bl)**2)/8
 if not 0<=t<1:raise ValueError('absorption theta')
 return t

def adaptive_norm(leaves,uppers):
 required=keys(leaves)
 if set(uppers)!=set(required) or any(not isinstance(v,F) or v<0 for v in uppers.values()):raise ValueError('exact complete fresh S key set required')
 ratios=[(max(uppers[k] for k in vertices(box))/(1-theta(box)),ident) for ident,box in leaves if box[0]+box[2]<=1]
 R=max(value for value,_ in ratios)
 if R<=0:raise ValueError('positive norm')
 M=F(-(-R.numerator//R.denominator))
 return M,{'R':str(R),'Mceil':str(M),'active_norm_leaf_ids':[i for value,i in ratios if value==R]}

def leaf(box,U,L,M):
 al,ah,bl,bh=box;low=al+bl
 if low>1:return 'OUTSIDE',None,[]
 high=min(ah+bh,F(1));bound=max(U)+theta(box)*M
 if bound<L:return 'FAR',bound,[('FAR',L-bound)]
 if 2*PI_HI*high<=1 and bound-F(1,16)<L:return 'NEAR',bound,[('NEAR',L-bound+F(1,16))]
 near=low<=1/(2*PI_LO);far=high>=1/(2*PI_HI)
 if (near and bound-F(1,16)>=L) or (far and bound>=L):raise ValueError('unaccepted strict leaf')
 req=[]
 if near:req.append(('SPLIT_NEAR',L-bound+F(1,16)))
 if far:req.append(('SPLIT_FAR',L-bound))
 return 'SPLIT',bound,req

def verify(leaves,lower,uppers):
 if type(N) is not int or N!=6912 or N<4096:raise ValueError('registered degree and analytic corner floor')
 if not isinstance(lower,F) or lower<=0:raise ValueError('fresh positive origin lower')
 M,norm=adaptive_norm(leaves,uppers);counts={};margins={};bounds=[]
 for ident,box in leaves:
  tag,bound,required=leaf(box,[uppers[k] for k in vertices(box)] if box[0]+box[2]<=1 else [],lower,M)
  counts[tag]=counts.get(tag,0)+1
  for label,gap in required:
   if gap<=0:raise ValueError('strict margin bookkeeping')
   margins[label]=min(margins.get(label,gap),gap)
  bounds.append([ident,tag,None if bound is None else str(bound)])
 return {'n':N,'nodes':2*len(leaves)-1,'vertices':len(uppers),'leaf_counts':counts,'minimum_strict_margins':{k:str(v) for k,v in margins.items()},'norm':norm,'L':str(lower),'leaf_bounds':bounds,'corner':'D17 analytic n>=4096 coefficient1/8; no lambda call'}
