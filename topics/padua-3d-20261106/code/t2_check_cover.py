#!/usr/bin/env python3
"""Small exact checker for every declared n3 normalized generator nullvector.
No floating arithmetic and no reliance on scratch catalogues or producer dictionary.
"""
import hashlib,itertools,json,math
from pathlib import Path
TOP=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check():
    p=TOP/'evidence/t2-n3-null-cover.json';data=json.loads(p.read_text())
    assert (data['n'],data['N'],data['M'],data['count'])==(3,20,39,171)
    expected=set(itertools.combinations(range(1,20),2));seen=set()
    ranks={}
    for b,c,rank,terms in data['witnesses']:
        assert (b,c) in expected and (b,c) not in seen;seen.add((b,c))
        assert terms and all(isinstance(v,int) and v!=0 for _,v in terms)
        powers=[tuple(a) for a,_ in terms]
        assert len(set(powers))==len(powers)
        assert all(len(a)==3 and all(isinstance(t,int) and t>=0 for t in a) and sum(a)<=3 for a in powers)
        values=[0]*39
        # Full Laurent Fourier coefficients rather than producer's folded cos rows.
        for a,v in terms:
            for signs in itertools.product([-1,1],repeat=3):
                frequency=sum(s*x*z for s,x,z in zip(signs,a,(1,b,c)))%39
                values[frequency]+=v
        assert values==[0]*39,(b,c,values)
        ranks[rank]=ranks.get(rank,0)+1
    assert seen==expected
    result={'schema':'t2-null-cover-check-v1','command':'python topics/padua-3d-20261106/code/t2_check_cover.py','checker_sha256':digest(Path(__file__)),'input_sha256':digest(p),'coverage':len(seen),'nonzero_Pi3_nullvectors':len(seen),'all_exact_Laurent_remainders_zero':True,'observed_ranks_untrusted_by_this_checker':ranks,'status':'PASS; developer execution, independent rerun needed for computer-proof acceptance'}
    (TOP/'evidence/t2-cover-check.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps(result))
if __name__=='__main__':check()
