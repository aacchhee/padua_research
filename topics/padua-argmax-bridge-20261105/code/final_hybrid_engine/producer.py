"""Deterministic generic exact-oracle midpoint producer; no FLOAT or work on import."""
from fractions import Fraction as F
import checker as C

def produce(n,upper,L,M,state,checkpoint):
 C.degree(n)
 visited=0;tokens=[];trace=state['trace']=[]
 def visit(box,depth,path):
  nonlocal visited
  if visited>=C.MAX_NODES or depth>C.MAX_DEPTH:raise RuntimeError('producer node/depth cap')
  ident=visited;visited+=1;slot=len(tokens);tokens.append('?')
  row={'id':ident,'path':path,'depth':depth,'box':list(map(str,box)),'decision':'PENDING'};trace.append(row)
  state['active_path']=path;state['visited_nodes']=visited;checkpoint()
  al,ah,bl,bh=box
  if al+bl>1:tokens[slot]='.';row['decision']='OUTSIDE';checkpoint();return
  if C.analytic_far(n,box):
   tokens[slot]='f';row['decision']='ANALYTIC_FAR';row['analytic']=C.require_analytic_far(n,box);checkpoint();return
  keys=sorted(C.vertices(box));V=max(upper(*key) for key in keys)
  tag,U,required,r,delta=C.leaf(n,box,V,L,M)
  row.update({'V':str(V),'U':str(U),'r_B':str(r),'delta_B':str(delta)})
  if tag is not None:tokens[slot]='.';row['decision']=tag;checkpoint();return
  if depth>=C.MAX_DEPTH:raise RuntimeError('unaccepted leaf at maximum depth')
  # Larger squared weighted width, exact; ties split a. Lower child first.
  axis='a' if (ah-al)**2>=F(n,n+1)**2*(bh-bl)**2 else 'b'
  if axis=='a':
   t=(al+ah)/2;left,right=(al,t,bl,bh),(t,ah,bl,bh)
  else:
   t=(bl+bh)/2;left,right=(al,ah,bl,t),(al,ah,t,bh)
  tokens[slot]=axis;row['decision']='BISECT_'+axis;checkpoint()
  visit(left,depth+1,path+'0');visit(right,depth+1,path+'1')
 visit((F(0),F(1),F(0),F(1)),0,'')
 state['active_path']=None;state['visited_nodes']=visited;checkpoint()
 return {'format':'FINAL-HYBRID-midpoint-v1','n':n,'preorder':''.join(tokens)}
