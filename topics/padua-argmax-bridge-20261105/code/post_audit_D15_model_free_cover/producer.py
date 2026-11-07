"""D15 FLOAT heuristic ONLY. Exact checker never imports this module."""
from fractions import Fraction as F
import math
N=2048
MAX_VERTICES=384
MAX_VISITED=2048

def propose_tree(phase_s_float,state,checkpoint):
 cache={};visited=0
 def canon(a,b):
  if a+b>1:a,b=1-a,1-b
  orbit=[]
  for sa in (-1,1):
   for sb in (-1,1):
    for p in range(-2,3):
     for q in range(-2,3):
      x,y=sa*a+p,sb*b+q
      if (p+q)%2==0 and min(x,y)>=0 and x+y<=1:orbit.append((x,y))
  return min(orbit)
 def value(a,b):
  key=canon(a,b)
  if key not in cache:
   if len(cache)>=MAX_VERTICES:raise RuntimeError('producer vertex cap')
   state['pending_vertex']=list(map(str,key));checkpoint()
   x=phase_s_float(N,math.pi*float(key[0]),math.pi*float(key[1]))
   if not math.isfinite(x) or x<0:raise RuntimeError('nonfinite producer')
   cache[key]=x;state['float_cache'][','.join(map(str,key))]=x.hex();state['pending_vertex']=None;checkpoint()
  return cache[key]
 def visit(node,al,ah,bl,bh,depth,path):
  nonlocal visited
  state['pending_path']=path;state['visited']=visited;checkpoint()
  if visited>=MAX_VISITED or depth>64:raise RuntimeError('producer tree cap')
  visited+=1
  if al+bl>1:node.clear();node['leaf']=True;checkpoint();return '.'
  U=max(value(a,b) for a in (al,ah) for b in (bl,bh))
  U+=M*(22/7)**2*(float(ah-al)**2+(2048/2049)**2*float(bh-bl)**2)/8
  near=float(al+bl)<=1/(2*(157/50));far=float(min(ah+bh,F(1)))>=1/(2*(22/7))
  allnear=2*(22/7)*float(min(ah+bh,F(1)))<=1
  if U<corner_guess or ((allnear or not far) and U-1/32<corner_guess) or ((not near or U-1/32<corner_guess) and (not far or U<corner_guess)):
   node.clear();node['leaf']=True;checkpoint();return '.'
  axis=0 if ah-al>=bh-bl else 1;t=(al+ah)/2 if axis==0 else (bl+bh)/2
  if axis==0:left,right=(al,t,bl,bh),(t,ah,bl,bh)
  else:left,right=(al,ah,bl,t),(al,ah,t,bh)
  node.clear();node.update(axis=axis,at=str(t),left={'pending':True},right={'pending':True});checkpoint()
  l=visit(node['left'],*left,depth+1,path+'0');r=visit(node['right'],*right,depth+1,path+'1')
  return ('a' if axis==0 else 'b')+l+r
 state['tree']={'pending':True};state['float_cache']={};checkpoint()
 grid=[(F(i,4),F(j,4)) for i in range(5) for j in range(5-i)]
 V=max(value(a,b) for a,b in grid)
 theta=(22/7)**2*(1+(2048/2049)**2)/128
 if not math.isfinite(V) or V<=0 or not 0<=theta<1:raise RuntimeError('heuristic norm guard')
 M=math.ceil(V/(1-theta));corner_guess=value(F(0),F(0))
 if M<=0 or not math.isfinite(corner_guess) or corner_guess<=0:raise RuntimeError('heuristic norm/corner')
 state['heuristic_norm']={'V_hex':V.hex(),'Mceil':M,'corner_hex':corner_guess.hex()};checkpoint()
 tokens=visit(state['tree'],F(0),F(1),F(0),F(1),0,'')
 state['pending_path']=None;state['visited']=visited;checkpoint()
 return {'format':'D15-midpoint-v1','n':2048,'preorder':tokens}

if __name__=='__main__':
 raise SystemExit('Use reviewed controller.py --run-once; producer has no standalone execution path')
