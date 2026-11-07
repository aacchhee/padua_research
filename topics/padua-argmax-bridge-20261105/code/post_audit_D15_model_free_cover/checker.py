"""D15 exact predicates. Independent of FLOAT producer arithmetic."""
from fractions import Fraction as F

N=2048
PI_LO=F(157,50)
PI_HI=F(22,7)
KAPPA=F(2048,2049)
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


def grid():
    return [(F(i,4),F(j,4)) for i in range(5) for j in range(5-i)]


def norm_from_grid(uppers):
    if len(uppers)!=15 or any(not isinstance(x,F) or x<0 for x in uppers):
        raise ValueError('fifteen exact nonnegative grid uppers required')
    V=max(uppers)
    theta=PI_HI**2*(1+KAPPA**2)/128
    if V<=0 or not 0<=theta<1:raise ValueError('norm absorption guard')
    bound=V/(1-theta)
    M=F(-(-bound.numerator//bound.denominator))
    return M,{'V':str(V),'theta':str(theta),'Mceil':str(M)}


def corner_witness(L,uppers,M):
    if not isinstance(L,F) or L<=0 or len(uppers)!=3 or any(not isinstance(x,F) or x<0 for x in uppers):
        raise ValueError('fresh exact corner endpoints required')
    if not isinstance(M,F) or M<=0:raise ValueError('global norm')
    a,b=F(1,4),F(3,16)
    if min(PI_LO*a,PI_LO*b)<F(1,2):raise ValueError('corner geometry')
    u,v=a*a/2,b*b/2
    losses=[L-U for U in uppers]
    q=min(losses[0]/u,losses[1]/v,losses[2]/(u+v))
    threshold=M*PI_HI**4*max(u,KAPPA**4*v)/6
    if q<=threshold:raise ValueError('fresh primary corner loss criterion')
    return {'losses':list(map(str,losses)),'q':str(q),'threshold':str(threshold),'gap':str(q-threshold),'barrier_coefficient_lower':str((q-threshold)/PI_HI**2)}


def leaf_predicate(box,U,L,M):
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
    raise ValueError('unaccepted leaf; strict exact margin failed')


def verify_tree_skeleton(document,L,certified_upper,M,arithmetic_identity="synthetic-control-only",cache=None):
    """Inject fresh C11 Arb oracle only after separately reviewed source integration.
    Never trusts producer values, booleans, keys, point results or bound fields.
    Controller separately validates scientific data dependencies, native closure and resources.
    """
    if set(document)!={'format','n','tree'} or document['format']!='D15-tree-v1' or type(document['n']) is not int or document['n']!=N:
        raise ValueError('format/degree')
    cache={} if cache is None else cache
    if not isinstance(cache,dict) or len(cache)>MAX_VERTICES:raise ValueError("invalid cache")
    for key,value in cache.items():
        if not isinstance(key,tuple) or len(key)!=4 or key[:2]!=(arithmetic_identity,N) or not all(isinstance(x,F) for x in key[2:]) or canonical(*key[2:])!=key[2:] or not isinstance(value,F) or value<0:
            raise ValueError("invalid fresh internal cache entry")
    seen=set()
    visited=0
    counts={}
    margins={}
    def upper(a,b):
        key=(N,*canonical(a,b))
        cache_key=(arithmetic_identity,*key)
        if cache_key not in cache:
            if len(cache)>=MAX_VERTICES:
                raise ValueError('vertex cap')
            # Adapter must key additionally by frozen source/arithmetic identity.
            value=certified_upper(key)
            if not isinstance(value,F) or value<0:
                raise ValueError('oracle did not return nonnegative exact upper')
            cache[cache_key]=value
        return cache[cache_key]
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
                mode=leaf_predicate(box,values,L,M)
                bound=max(values)+M*PI_HI**2*((ah-al)**2+KAPPA**2*(bh-bl)**2)/8
                required=[]
                if mode=='FAR':required=[('FAR',L-bound)]
                elif mode=='NEAR':required=[('NEAR',L-bound+F(1,32))]
                else:
                    if al+bl<=1/(2*PI_LO):required.append(('SPLIT_NEAR',L-bound+F(1,32)))
                    if min(ah+bh,F(1))>=1/(2*PI_HI):required.append(('SPLIT_FAR',L-bound))
                for label,gap in required:
                    if gap<=0:raise ValueError('strict margin bookkeeping')
                    margins[label]=min(margins.get(label,gap),gap)
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
    if not isinstance(M,F) or M<=0:raise ValueError("uncertified global norm")
    if not isinstance(L,F) or L<=0:
        raise ValueError('uncertified corner lower')
    walk(document['tree'],(F(0),F(1),F(0),F(1)),0)
    return {'scope':'exact complete tree and strict leaf predicates','visited':visited,'vertices':len(cache),'leaf_counts':counts,'minimum_strict_margins':{k:str(v) for k,v in margins.items()}}


def decode_certificate(document):
    if not isinstance(document,dict) or set(document)!={'format','n','preorder'} or document['format']!='D15-midpoint-v1' or type(document['n']) is not int or document['n']!=N:
        raise ValueError('certificate schema/degree')
    tokens=document['preorder']
    if not isinstance(tokens,str) or not 1<=len(tokens)<=MAX_VISITED:
        raise ValueError('preorder size/type')
    index=0
    def take(box,depth):
        nonlocal index
        if index>=len(tokens) or depth>64:raise ValueError('missing sibling/depth')
        token=tokens[index];index+=1
        if token=='.':return {'leaf':True}
        al,ah,bl,bh=box
        if token=='a':
            t=(al+ah)/2;axis=0;left,right=(al,t,bl,bh),(t,ah,bl,bh)
        elif token=='b':
            t=(bl+bh)/2;axis=1;left,right=(al,ah,bl,t),(al,ah,t,bh)
        else:raise ValueError('unknown preorder token')
        return {'axis':axis,'at':str(t),'left':take(left,depth+1),'right':take(right,depth+1)}
    tree=take((F(0),F(1),F(0),F(1)),0)
    if index!=len(tokens):raise ValueError('extra/duplicated tree suffix')
    return {'format':'D15-tree-v1','n':N,'tree':tree}


def verify_certificate(document,L,certified_upper,M,arithmetic_identity="synthetic-control-only",cache=None):
    return verify_tree_skeleton(decode_certificate(document),L,certified_upper,M,arithmetic_identity,cache)


if __name__=='__main__':
    raise SystemExit('Use reviewed controller.py --run-once; checker has no standalone native path')
