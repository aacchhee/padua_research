"""Cheap exact controls and >=20 single-corruption rejection controls."""
import copy
from fractions import Fraction as F
import numpy as np
import check as c
def arithmetic_controls():
    tests=[]
    def enclose(name,interval,value):
        lo,hi=interval; c.need(lo<=value<=hi,name); tests.append(name)
    for num,den,value in [(0,1,F(0)),(1,6,F(1,2)),(1,2,F(1)),(5,6,F(1,2)),
                          (1,1,F(0)),(7,6,F(-1,2)),(-1,2,F(-1)),(123456,1,F(0))]:
        lo,hi=c.sinpi(np.array([num],dtype=np.int64),den)
        enclose('sinpi '+str((num,den)),(F(float(lo[0])),F(float(hi[0]))),value)
    for k in [1,2,7]:
        for j in [-3,0,2]:
            lo,hi=c.ratio(k,np.array([j*37],dtype=np.int64),37)
            enclose('removable '+str((k,j)),(F(float(lo[0])),F(float(hi[0]))),F(k*(-1)**(j*(k-1))))
    enclose('S2 corner',c.S(2,0,0),F(3))
    enclose('lambda2 corner',c.actual_lambda(2,0,0),F(3))
    for j,k in [(0,0),(0,2),(1,1),(1,3),(2,0),(2,2)]:
        enclose('lambda2 node '+str((j,k)),c.actual_lambda(2,1-F(j,2),1-F(k,3)),F(1))
    enclose('pairwise positive sum',c.total((np.ones(103),np.ones(103))),F(103))
    for p,q in [((F(1),F(0)),(F(0),F(1))),((F(3,4),F(1,4)),(F(1,4),F(3,4))),((F(1,2),F(1,2)),(F(1,2),F(1,2)))]:
        c.need(c.fold(*p)==q and c.fold(*q)==q,'closed seam fold'); tests.append('seam fold '+str(p))
    r=(F(0),F(1),F(0),F(1)); w=[F(0)]*4
    enclose('quadratic interior maximum',(F(0),c.maximum(r,w,F(1),F(1))),c.PHI**2/4)
    # The maximum over the triangle is attained at (1/2,1/2), a closed edge point.
    c.need(c.maximum(r,w,F(1),F(1))==c.PHI**2/4,'closed seam maximum')
    try: c.geometry(511,F(1,2**60),F(0))
    except ValueError: tests.append('overflow rejection')
    else: raise ValueError('overflow rejection missing')
    return tests
def corruption_controls(base,cache):
    mutations=[]
    def edit(name,path,value): mutations.append((name,path,value))
    edit('certificate format',['format'],'wrong')
    edit('noninteger degree',['n'],199.)
    edit('wrong tree n',['tree','n'],198)
    edit('incomplete tree',['tree','preorder'],base['tree']['preorder'][:-1])
    edit('trailing tree',['tree','preorder'],base['tree']['preorder']+'.')
    edit('flipped split',['tree','preorder'],'b'+base['tree']['preorder'][1:])
    edit('unknown token',['tree','preorder'],'x')
    edit('uncovered analytic root',['tree','preorder'],'f')
    edit('pi bracket',['pi_bracket'],['3','4'])
    edit('norm method',['norm','method'],'UNKNOWN')
    edit('analytic with TREE',['norm','method'],'TREE')
    edit('floor tier',['floor','tier'],'max(1/2,B)')
    edit('floor guard',['floor','domain'],'everywhere')
    edit('far degree',['analytic_far','minimum_degree'],191)
    edit('far gap',['analytic_far','primitive_gap'],'1/2')
    edit('far guard',['analytic_far','closed_normalized_guard'],'a+b>=0')
    edit('far dependencies',['analytic_far','dependencies'],[])
    edit('corner kind',['corner','kind'],'UNKNOWN')
    edit('corner theorem',['corner','theorem'],'unproved')
    edit('missing S key',['S_upper_rows'],base['S_upper_rows'][1:])
    edit('duplicate S key',['S_upper_rows'],base['S_upper_rows']+[base['S_upper_rows'][0]])
    lowered=copy.deepcopy(base['S_upper_rows']); lowered[0][2]='0x1p+0'
    edit('lowered S endpoint',['S_upper_rows'],lowered)
    badkey=copy.deepcopy(base['S_upper_rows']); badkey[0][0]='-1/4'
    edit('wrong S key',['S_upper_rows'],badkey)
    edit('raised L endpoint',['origin_lower_hex'],'0x1p+10')
    edit('nonfinite endpoint',['origin_lower_hex'],'inf')
    badlam=copy.deepcopy(base['lambda_upper_rows']); badlam[0][0]='0'
    edit('wrong actual point',['lambda_upper_rows'],badlam)
    badlam=copy.deepcopy(base['lambda_upper_rows']); badlam[0][2]='0x1p+0'
    edit('lowered actual endpoint',['lambda_upper_rows'],badlam)
    results=[]
    for name,path,value in mutations:
        d=copy.deepcopy(base); node=d
        for p in path[:-1]: node=node[p]
        node[path[-1]]=value
        try: c.check(d,cache)
        except (ValueError,KeyError,TypeError) as e: results.append({'name':name,'rejected':True,'reason':str(e)})
        else: raise ValueError('corruption accepted: '+name)
    return results
