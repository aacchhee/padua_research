"""D11 FLOAT heuristic skeleton; NEVER a proof checker. No native adapter.
No import from checker: producer guesses may only select a complete rational tree.
"""
from fractions import Fraction
import math

N=512
M=34.0
MAX_VERTICES=384
MAX_VISITED=2048


def propose_tree_skeleton(phase_s_float,corner_guess):
    """Deterministic depth-first longest-side midpoint subdivision.
    Callback must use unchanged phase_probe.c phase_s(n,pi*a,pi*b).
    Values/acceptance guesses remain floating diagnostics only.
    """
    cache={}
    visited=0
    def value(a,b):
        # Floating producer cache need not be minimal; checker rebuilds its own.
        if a+b>1:a,b=1-a,1-b
        key=(a,b)
        if key not in cache:
            if len(cache)>=MAX_VERTICES:raise RuntimeError('producer vertex cap')
            x=phase_s_float(N,math.pi*float(a),math.pi*float(b))
            if not math.isfinite(x) or x<0:raise RuntimeError('nonfinite producer')
            cache[key]=x
        return cache[key]
    def visit(al,ah,bl,bh,depth):
        nonlocal visited
        visited+=1
        if visited>MAX_VISITED or depth>64:raise RuntimeError('producer tree cap')
        if al+bl>1:return {'leaf':True}
        U=max(value(a,b) for a in (al,ah) for b in (bl,bh))
        U+=M*(22/7)**2*(float(ah-al)**2+(512/513)**2*float(bh-bl)**2)/8
        near=float(al+bl)<=1/(2*(157/50))
        far=float(min(ah+bh,Fraction(1)))>=1/(2*(22/7))
        allnear=2*(22/7)*float(min(ah+bh,Fraction(1)))<=1
        if U<corner_guess or ((allnear or not far) and U-1/32<corner_guess) or ((not near or U-1/32<corner_guess) and (not far or U<corner_guess)):
            return {'leaf':True}
        axis=0 if ah-al>=bh-bl else 1
        t=(al+ah)/2 if axis==0 else (bl+bh)/2
        if axis==0:left,right=(al,t,bl,bh),(t,ah,bl,bh)
        else:left,right=(al,ah,bl,t),(al,ah,t,bh)
        return {'axis':axis,'at':str(t),'left':visit(*left,depth+1),'right':visit(*right,depth+1)}
    tree=visit(Fraction(0),Fraction(1),Fraction(0),Fraction(1),0)
    return {'format':'D11-tree-v1','n':512,'tree':tree}


def phase_s_float(*args):
    raise RuntimeError('BLOCKED: producer compiler/ABI/resource adapter not implemented')


if __name__=='__main__':
    raise SystemExit('PREPARATION ONLY: no producer execution is implemented')
