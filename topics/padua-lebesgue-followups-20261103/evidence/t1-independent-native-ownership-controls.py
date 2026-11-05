"""Independent PyLong primitive: rational rounding, type faults, ref ownership."""
import argparse
from fractions import Fraction
import gc
import hashlib
import itertools
import json
from math import ceil,floor
from pathlib import Path
import sys
import _t1_native

def reference(terms,table,unit):
    lower=upper=0
    for i,j,c in terms:
        products=[Fraction(a*b,unit)for a in c for b in table[i][j]]
        lower+=floor(min(products));upper+=ceil(max(products))
    return lower,upper

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
    f=_t1_native.accumulate
    endpoints=(-7,-1,0,1,7)
    intervals=list(itertools.combinations_with_replacement(endpoints,2))
    comparisons=0
    for unit in (1,2,3,32,1<<160):
        for c,m in itertools.product(intervals,repeat=2):
            table=((m,),)
            for terms in (((0,0,c),),((0,0,c),(0,0,c)),()):
                assert f(terms,table,unit)==reference(terms,table,unit)
                comparisons+=1
    large=10**500+1234567
    terms=((0,0,(-large,large+3)),(1,0,(large//3,large//2)),(0,0,(-1,1)))
    table=(((large//7,large//6),),((-large,large),))
    unit=(1<<160)+17
    assert f(terms,table,unit)==reference(terms,table,unit);comparisons+=1
    # Each term must be rounded BEFORE summation, including negative products.
    for c in ((1,1),(-1,-1),(-1,1)):
        terms2=((0,0,c),(0,0,c));table2=(((1,1),),)
        assert f(terms2,table2,2)==reference(terms2,table2,2);comparisons+=1
    class IntSubclass(int):pass
    class ListSubclass(list):pass
    bad=[((),(),False),((),(),1.0),((),(),-1),((),(),0),
         (ListSubclass(),(),1),(((0,0,(IntSubclass(1),2)),),(((1,2),),),1),
         (((True,0,(1,2)),),(((1,2),),),1),(((0,False,(1,2)),),(((1,2),),),1),
         (((0,0,(1,2)),),(((False,2),),),1),(((0,0,(1,2)),),((ListSubclass((1,2)),),),1),
         (((-1,0,(1,2)),),(((1,2),),),1),(((0,-1,(1,2)),),(((1,2),),),1),
         (((10**100,0,(1,2)),),(((1,2),),),1),(((0,10**100,(1,2)),),(((1,2),),),1),
         (((0,0,(1,2)),),(),1),(((0,0,(1,2)),),((),),1),
         (((0,0,(1,2)),),(((),),),1),(((0,0,(1,2,3)),),(((1,2),),),1),
         (((0,0),),(((1,2),),),1)]
    for arguments in bad:
        try:f(*arguments)
        except (TypeError,ValueError,OverflowError):pass
        else:raise AssertionError(('invalid primitive input accepted',arguments))
    # Every input reference is borrowed; products and intermediate sums must be
    # released on success and each nonallocation fault path. Strong references
    # below stabilize the exact objects compared before/after 20000 calls.
    objects=[terms,table,unit,*terms,*table]
    objects.extend(q for term in terms for q in(term[2],*term[2]))
    objects.extend(q for row in table for pair in row for q in(pair,*pair))
    for _ in range(20):f(terms,table,unit)
    gc.collect();before=[sys.getrefcount(o)for o in objects]
    for _ in range(10000):
        f(terms,table,unit)
        try:f((*terms,(0,0,(1,))),table,unit)
        except ValueError:pass
        else:raise AssertionError('late malformed interval accepted')
    gc.collect();after=[sys.getrefcount(o)for o in objects]
    assert before==after,(before,after)
    result={'all_controls_passed':True,'count_certified':False,
            'scope':'native exact primitive controls only; no count certificate',
            'rational_rounding_comparisons':comparisons,'malformed_refusals':len(bad),
            'large_endpoint_decimal_digits':len(str(large)),
            'reference_counts_unchanged':True,'successful_ownership_iterations':10000,
            'late_failure_ownership_iterations':10000,'objects_observed':len(objects),
            'python':sys.version,'binary_path':_t1_native.__file__,
            'binary_sha256':hashlib.sha256(Path(_t1_native.__file__).read_bytes()).hexdigest(),
            'control_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
