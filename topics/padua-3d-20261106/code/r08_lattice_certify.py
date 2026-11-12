#!/usr/bin/env python3
"""Small exact witnesses and predecessor cross-links for the round08 census."""
import argparse, collections, fractions, hashlib, itertools, json, math
import pathlib, sys
from r08_lattice import ROOT, INPUT, identity, exps, characters, exact_rank, folded, shortest

def cyclic_hnf(z,q):
    # All examples have first generator coordinate1, but solve using last unit.
    inv=pow(z[2],-1,q)
    return (1,0,-z[0]*inv%q,1,-z[1]*inv%q,q)
def moment(v,alpha):
    q=math.prod((v[0],v[3],v[5]))
    return fractions.Fraction(characters(v,alpha).get((0,0,0),0),2**sum(x!=0 for x in alpha))
def basis(points,n):
    import numpy as np
    T=[np.polynomial.chebyshev.chebvander(points[:,j],n) for j in range(3)]
    return np.array([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in exps(n)]).T
def quality(v,n,mesh=41):
    import numpy as np
    q,F=folded(v);P=np.cos(2*np.pi*np.array(sorted(F))/q);V=basis(P,n)
    C=np.linalg.inv(V);ax=np.cos(np.pi*np.arange(mesh)/(mesh-1));best=0.
    for x in ax:
        Ptest=np.array([(x,y,z) for y in ax for z in ax]);best=max(best,float(np.abs(basis(Ptest,n)@C).sum(axis=1).max()))
    return {'mesh':mesh,'Lambda_mesh':best,'condition':float(np.linalg.cond(V)),'cardinal_residual':float(np.abs(V@C-np.eye(len(V))).max())}
def main():
    p=argparse.ArgumentParser();p.add_argument('--receipt',required=True);a=p.parse_args()
    certpath=ROOT/'evidence/t7-r06-certificate.json';cert=json.loads(certpath.read_text())
    t7=[(a,r,s,b,t,c) for a,b,c,r,s,t in cert['prime_survivors_HNF']]
    t7stats=collections.Counter((shortest(v),exact_rank(v,2),len(folded(v)[1])) for v in t7)
    admissible=[v for v in t7 if shortest(v)>=4]
    assert len(admissible)==24 and all(exact_rank(v,2)==10 and len(folded(v)[1])==10 for v in admissible)
    rows=[]
    for z in [(1,3,7),(1,4,6),(1,5,8),(1,7,8)]:
        v=cyclic_hnf(z,19);q,F=folded(v)
        nonzero=[(al,str(moment(v,al))) for al in exps(4) if sum(al)>0 and moment(v,al)]
        deg=min(sum(al) for al,m in nonzero)-1
        rows.append({'z':z,'hnf':v,'shortest_l1':shortest(v),'fold':len(F),'exact_rank':exact_rank(v,2),
                     'exact_Haar_degree':deg,'first_nonzero_moments':[[list(al),m] for al,m in nonzero if sum(al)==deg+1],
                     'weights_numerators':sorted(F.values()),'weights_denominator':q,
                     'folded_node_numerators':sorted(F),'quality_MEASURED':quality(v,2)})
    witnesses=[]
    for n,v in [(1,(1,1,1,2,0,2)),(3,(1,3,3,6,0,10)),(4,(4,0,4,4,4,8)),(5,(5,0,5,5,5,10))]:
        q,F=folded(v)
        assert all(not moment(v,al) for al in exps(2*n-1) if any(al))
        witnesses.append({'n':n,'hnf':v,'det':q,'fold':len(F),'rank':exact_rank(v,n),'shortest_l1':shortest(v),
                          'positive_Haar_weights':True,'moments_through':2*n-1})
    out={'schema':'padua-r08-lattice-witness-v1','input_sha':INPUT,
         'sources':[identity(__file__),identity(pathlib.Path(__file__).with_name('r08_lattice.py'))],
         'inputs':[identity(certpath)],'command':sys.argv,'order19_T7_count':len(t7),
         'order19_shortest_rank_fold_hist':[[s,r,m,c] for (s,r,m),c in sorted(t7stats.items())],
         'admissible_T7_order19_hnfs':admissible,'cyclic_T2_witnesses':rows,'other_exact_witnesses':witnesses}
    pathlib.Path(a.receipt).write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps({'order19_hist':out['order19_shortest_rank_fold_hist'],'other_witnesses':witnesses}),flush=True)
if __name__=='__main__':main()
