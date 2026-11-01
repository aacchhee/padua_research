"""Exact endpoint identity controls and bounded real-leaf cache benchmark."""
import argparse
from dataclasses import FrozenInstanceError
from fractions import Fraction
import hashlib
from pathlib import Path
import time
import a5_checker_n8_staged_cached as cache

HERE=Path(__file__).resolve()
BEFORE=hashlib.sha256(HERE.read_bytes()).hexdigest()
ENTRY_BEFORE=cache.ENTRY_SHA_AT_IMPORT
check=cache.check

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--interior',required=True)
    parser.add_argument('--interior-sha256',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args();start=time.monotonic()
    cache.ORIGINAL_GUARD()
    raw=Path(args.interior).read_bytes()
    check.require(cache.staged.sha(raw)==args.interior_sha256,'wrong benchmark input')
    data=cache.staged.load_json(raw);v=check.Verifier(data['field_embedding'])
    boxes=[(check.Interval.bounds(-1,1),check.Interval.bounds(-1,1)),
           (check.Interval.point(0),check.Interval.point(0)),
           (check.Interval.point(Fraction(1,3)),check.Interval.point(Fraction(-2,7))),
           (check.Interval.bounds(Fraction(-1,256),Fraction(3,512)),
            check.Interval.bounds(Fraction(-1,64),Fraction(1,128)))]
    boxes.extend(check.path_rectangle(data['leaves'][i]['path'])[1]
                 for i in (0,1,10,100,1000,2000))
    polynomials=list(v.lterms)+list(v.ldx)+list(v.ldy)
    polynomials.extend(t for group in v.lhessian for t in group)
    for mask in (0,1,3,17,255,1024,8191,21845,1<<44,(1<<45)-1):
        polynomials.extend(v.terms_for(mask,a,b)for a,b in((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)))
    polynomials.extend(((),((0,0,check.Interval(-7,11)),),
                        ((8,0,check.Interval.bounds(-2,3)),(0,8,check.Interval.bounds(-3,-1)),
                         (4,4,check.Interval.bounds(Fraction(-1,3),Fraction(2,7))),
                         (4,4,check.Interval.bounds(Fraction(-5,7),Fraction(1,11))))))
    identities=0
    def equal(terms,box):
        nonlocal identities
        old=cache.ORIGINAL_EVALUATE(terms,box);new=cache.cached_evaluate(terms,box)
        check.require((old.lo,old.hi)==(new.lo,new.hi),'cached endpoint BIT mismatch')
        identities+=1
    for box in boxes:
        for terms in polynomials:equal(terms,box)
    axis_ids=[]
    for root in data['interior_roots']:
        bounds,box=check.parse_rectangle(root['R'])
        for a,b in((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)):
            equal(v.terms_for(root['mask'],a,b),box)
        low,high=bounds[0]
        if low<=0<=high:
            axis_ids.append(root['id'])
            hull=((min(low,-high),max(high,-low)),bounds[1])
            hb=tuple(check.Interval.bounds(a,b)for a,b in hull)
            for terms in polynomials:equal(terms,hb)
    table=cache.monomials(0,0,0,0,160)
    check.require(table is cache.monomials(0,0,0,0,160),'identical coordinate key did not reuse immutable table')
    try:
        table[0][0].lo=1
    except FrozenInstanceError:
        immutable=True
    else:
        raise RuntimeError('cached interval was mutable')
    for i in range(600):
        cache.monomials(i,i+1,-i-1,-i,160)
    check.require(cache.monomials.cache_info().currsize<=512,'cache bound failed')
    rejected_precision=False
    try:cache.monomials(0,0,0,0,159)
    except check.Rejected:rejected_precision=True
    check.require(rejected_precision,'changed precision was accepted')
    selected=[leaf for leaf in data['leaves']if'all_gradient'in leaf][:100]
    check.require(len(selected)==100,'benchmark needs100 actual universal leaves')
    # Warm coefficient/cardinal caches BEFORE timing either backend.
    for leaf in selected:v.leaf(leaf)
    old_start=time.monotonic()
    for leaf in selected:v.leaf(leaf)
    old_seconds=time.monotonic()-old_start
    cache.monomials.cache_clear();check.evaluate=cache.cached_evaluate
    new_start=time.monotonic()
    try:
        for leaf in selected:v.leaf(leaf)
    finally:
        check.evaluate=cache.ORIGINAL_EVALUATE
    new_seconds=time.monotonic()-new_start
    stats=cache.monomials.cache_info()._asdict()
    cache.install();cache.guard_entry()
    after=hashlib.sha256(HERE.read_bytes()).hexdigest()
    check.require(BEFORE==after and ENTRY_BEFORE==cache.staged.sha(cache.HERE.read_bytes()),'cache/control source changed')
    result={'format':'a5-n8-bit-identical-cache-controls-v1','all_controls_passed':True,
            'count_certified':False,'scope':'bitwise evaluator equivalence and100 supplied-leaf benchmark only; no full count',
            'exact_endpoint_identities':identities,'polynomial_vectors':len(polynomials),'common_boxes':len(boxes),
            'actual_root_boxes':len(data['interior_roots']),'actual_axis_hulls':axis_ids,
            'empty_cross_zero_points_and_repeated_terms_checked':True,'immutable_cache':immutable,
            'cache_maxsize':512,'wrong_precision_rejected':rejected_precision,
            'benchmark_leaves':len(selected),'old_seconds':old_seconds,'cached_seconds':new_seconds,
            'speedup':old_seconds/new_seconds,'cache_info':stats,
            'input_sha256':cache.staged.sha(raw),'entry_sha256':ENTRY_BEFORE,
            'entry_sha256_after':cache.staged.sha(cache.HERE.read_bytes()),
            'controls_sha256':BEFORE,'controls_sha256_after':after,'sources_unchanged':True,
            'base_staged_sha256':cache.BASE_SHA,'main_sha256':cache.staged.MAIN_SHA,
            'old_controls_sha256':cache.staged.CONTROLS_SHA,'seconds':time.monotonic()-start}
    cache.ORIGINAL_ATOMIC(args.output,result)
    print(__import__('json').dumps(result,sort_keys=True),flush=True)

if __name__=='__main__':main()
