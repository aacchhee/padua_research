"""D11 exact predicate/tree skeleton. No native adapter or runnable certificate gate.
Independent of producer arithmetic. Public CLI always refuses mathematical use.
"""
from fractions import Fraction as F

N=512
M=F(34)
PI_LO=F(157,50)
PI_HI=F(22,7)
KAPPA=F(512,513)
MAX_VERTICES=384
MAX_VISITED=2048


def rational(s):
    if not isinstance(s,str) or len(s)>256:
        raise ValueError('bounded canonical rational string required')
    q=F(s)
    if str(q)!=s:
        raise ValueError('noncanonical rational')
    return q


def canonical(a,b):
    """Only S inputs are folded. Physical phase geometry is never folded."""
    if not (0<=a<=1 and 0<=b<=1):
        raise ValueError('raw vertex outside unit square')
    if a+b>1:
        a,b=1-a,1-b
    orbit=[]
    for sa in (-1,1):
        for sb in (-1,1):
            for p in range(-2,3):
                for q in range(-2,3):
                    x,y=sa*a+p,sb*b+q
                    if (p+q)%2==0 and x>=0 and y>=0 and x+y<=1:
                        orbit.append((x,y))
    if not orbit:
        raise ValueError('empty orbit')
    return min(orbit)


def corner_witness(receipt):
    """Recompute exact D09 losses; identity/interval replay is external prerequisite.
    This pure helper alone does NOT establish an accepted corner premise.
    """
    if receipt['global_norm']['selected']!='34':
        raise ValueError('wrong norm')
    L=rational(receipt['corner']['point']['lower'])
    p=receipt['rectangles']['primary']
    if p['geometry']['a_turn']!='1/4' or p['geometry']['b_turn']!='3/16':
        raise ValueError('wrong corner rectangle')
    a,b=F(1,4),F(3,16)
    if min(PI_LO*a,PI_LO*b)<F(1,2):
        raise ValueError('corner geometry')
    u,v=a*a/2,b*b/2
    upper=[rational(p['vertices'][key]['point']['upper']) for key in ('x','y','xy')]
    losses=[L-U for U in upper]
    q=min(losses[0]/u,losses[1]/v,losses[2]/(u+v))
    threshold=M*PI_HI**4*max(u,KAPPA**4*v)/6
    if L<=0 or q<=threshold:
        raise ValueError('corner loss criterion')
    return L,{'losses':list(map(str,losses)),'q':str(q),'threshold':str(threshold),'gap':str(q-threshold)}


def leaf_predicate(box,U,L):
    """D10(6), exact closed clipping/proxy nonemptiness, no polygon optimizer."""
    al,ah,bl,bh=box
    low=al+bl
    if low>1:
        return 'OUTSIDE'
    high=min(ah+bh,F(1))
    bound=max(U)+M*PI_HI**2*((ah-al)**2+KAPPA**2*(bh-bl)**2)/8
    if bound<L:
        return 'FAR'
    # Optional all-actually-near guard. Near floor is noncorner only;
    # the separately validated actual-corner premise supplies its other case.
    if 2*PI_HI*high<=1 and bound-F(1,32)<L:
        return 'NEAR'
    near_nonempty=low<=1/(2*PI_LO)
    far_nonempty=high>=1/(2*PI_HI)
    if (not near_nonempty or bound-F(1,32)<L) and (not far_nonempty or bound<L):
        return 'SPLIT'
    raise ValueError('unaccepted leaf')


def verify_tree_skeleton(document,L,certified_upper):
    """Inject fresh C11 Arb oracle only after separately reviewed source integration.
    Never trusts producer values, booleans, keys, point results or bound fields.
    Return is a predicate diagnostic, NOT the full scientific acceptance gate.
    """
    if set(document)!={'format','n','tree'} or document['format']!='D11-tree-v1' or type(document['n']) is not int or document['n']!=N:
        raise ValueError('format/degree')
    cache={}
    seen=set()
    visited=0
    counts={}
    def upper(a,b):
        key=(N,*canonical(a,b))
        if key not in cache:
            if len(cache)>=MAX_VERTICES:
                raise ValueError('vertex cap')
            # Adapter must key additionally by frozen source/arithmetic identity.
            value=certified_upper(key)
            if not isinstance(value,F) or value<0:
                raise ValueError('oracle did not return nonnegative exact upper')
            cache[key]=value
        return cache[key]
    def walk(node,box,depth):
        nonlocal visited
        visited+=1
        if visited>MAX_VISITED or depth>64 or not isinstance(node,dict) or id(node) in seen:
            raise ValueError('tree cap/type/alias')
        seen.add(id(node))
        al,ah,bl,bh=box
        if set(node)=={'leaf'} and node['leaf'] is True:
            if al+bl>1:
                mode='OUTSIDE'
            else:
                values=[upper(a,b) for a in (al,ah) for b in (bl,bh)]
                mode=leaf_predicate(box,values,L)
            counts[mode]=counts.get(mode,0)+1
            return
        if set(node)!={'axis','at','left','right'} or type(node['axis']) is not int or node['axis'] not in (0,1):
            raise ValueError('incomplete/pending/duplicate tree')
        t=rational(node['at'])
        if node['axis']==0:
            if not al<t<ah:raise ValueError('no split progress')
            left,right=(al,t,bl,bh),(t,ah,bl,bh)
        else:
            if not bl<t<bh:raise ValueError('no split progress')
            left,right=(al,ah,bl,t),(al,ah,t,bh)
        walk(node['left'],left,depth+1)
        walk(node['right'],right,depth+1)
    if not isinstance(L,F) or L<=0:
        raise ValueError('uncertified corner lower')
    walk(document['tree'],(F(0),F(1),F(0),F(1)),0)
    return {'diagnostic':'exact tree/leaf predicates only','visited':visited,'vertices':len(cache),'leaf_counts':counts}


def fresh_c11_upper(*args,**kwargs):
    raise RuntimeError('BLOCKED: fresh build/API/closure/resource adapter not implemented')


if __name__=='__main__':
    raise SystemExit('PREPARATION ONLY: no certificate acceptance or native execution is implemented')
