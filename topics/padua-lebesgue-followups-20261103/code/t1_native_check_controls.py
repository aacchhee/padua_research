"""Native checker endpoint controls and100 real universal-leaf timings."""
if not __debug__:
    raise RuntimeError('T1 native checker controls refuse optimized Python')
import argparse,hashlib,json,time
from fractions import Fraction
from pathlib import Path
import t1_native_check_backend as native
cached=native.cached;check=native.check

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--interior',required=True);ap.add_argument('--output',required=True);options=ap.parse_args()
    start=time.monotonic();cached.ORIGINAL_GUARD();raw=Path(options.interior).read_bytes();data=cached.staged.load_json(raw);v=check.Verifier(data['field_embedding'])
    boxes=[(check.Interval.bounds(-1,1),check.Interval.bounds(-1,1)),(check.Interval.point(0),check.Interval.point(0)),(check.Interval.point(Fraction(1,3)),check.Interval.point(Fraction(-2,7))),(check.Interval.bounds(Fraction(-1,256),Fraction(3,512)),check.Interval.bounds(Fraction(-1,64),Fraction(1,128)))]
    boxes.extend(check.path_rectangle(data['leaves'][i]['path'])[1] for i in(0,1,10,100,1000,2000))
    polynomials=list(v.lterms)+list(v.ldx)+list(v.ldy)
    polynomials.extend(t for group in v.lhessian for t in group)
    for mask in(0,1,3,17,255,1024,8191,21845,1<<44,(1<<45)-1):
        polynomials.extend(v.terms_for(mask,a,b)for a,b in((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)))
    repeated=(4,4,check.Interval.bounds(Fraction(-5,7),Fraction(1,11)))
    polynomials.extend(((),((0,0,check.Interval(-7,11)),),(repeated,repeated,repeated)))
    count=0;payload=hashlib.sha256()
    def compare(terms,box):
        nonlocal count
        expected=cached.ORIGINAL_EVALUATE(terms,box);old=cached.cached_evaluate(terms,box);actual=native.evaluate(terms,box)
        check.require(expected==old==actual,'native checker endpoint mismatch');payload.update(repr((actual.lo,actual.hi)).encode());count+=1
    for box in boxes:
        for terms in polynomials:compare(terms,box)
    for root in data['interior_roots']:
        _,box=check.parse_rectangle(root['R'])
        for a,b in((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)):compare(v.terms_for(root['mask'],a,b),box)
    selected=[leaf for leaf in data['leaves']if'all_gradient'in leaf][:100];check.require(len(selected)==100,'needs100 actual leaves')
    original=check.evaluate
    try:
        check.evaluate=cached.cached_evaluate
        for leaf in selected:v.leaf(leaf)
        begin=time.monotonic()
        for leaf in selected:v.leaf(leaf)
        cached_seconds=time.monotonic()-begin
        check.evaluate=native.evaluate
        for leaf in selected:v.leaf(leaf)
        begin=time.monotonic()
        for leaf in selected:v.leaf(leaf)
        native_seconds=time.monotonic()-begin
    finally:check.evaluate=original
    wrong_precision=False
    try:native.table_view(0,0,0,0,159)
    except check.Rejected:wrong_precision=True
    check.require(wrong_precision,'wrong precision accepted')
    for i in range(600):native.table_view(i,i+1,-i-1,-i,160)
    check.require(native.table_view.cache_info().currsize<=512,'unbounded native view cache')
    cached.ORIGINAL_GUARD()
    result={'all_controls_passed':True,'count_certified':False,'exact_endpoint_equalities':count,'payload_sha256':payload.hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),'polynomial_vectors':len(polynomials),'boxes':len(boxes),'actual_root_boxes':len(data['interior_roots']),'benchmark_leaves':100,'cached_seconds':cached_seconds,'native_seconds':native_seconds,'cached_over_native':cached_seconds/native_seconds,'wrong_precision_refused':wrong_precision,'cache':native.table_view.cache_info()._asdict(),'backend_sha256':hashlib.sha256(Path(native.__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
    Path(options.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
