"""Deterministic endpoint and malformed-input controls for exact native loop."""
if not __debug__:
    raise RuntimeError('T1 native edge controls refuse optimized Python')
import argparse,hashlib,importlib,json,random,subprocess,sys,time
from pathlib import Path
from types import SimpleNamespace
from t1_native import evaluator
from t1_memo import evaluator as memo_evaluator
from _t1_native import accumulate
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
    start=time.monotonic();count=0;payload=hashlib.sha256();rows=[]
    rng=random.Random(392107)
    for n in range(4,9):
        m=importlib.import_module('a5_n%d_boxes'%n);new,cache=evaluator(m,expected_unit=m.S);memo,_=memo_evaluator(m);u=m.S
        boxes=[((-u,u),(-u,u)),((0,0),(0,0)),((-u,-u),(u,u)),((-1,1),(-1,1)),((u-1,u),(0,1)),((-u*3,u*4),(-u*2,0))]
        # Negative and large arbitrary-precision coefficients exercise every
        # floor/ceiling remainder sign; repeated terms preserve sum order.
        vectors=[[ ],[(0,0,(0,0))],[(n,n,(-u,u))],[(1,0,(-1,1))]]
        for _ in range(100):
            terms=[]
            for __ in range(rng.randrange(1,65)):
                c0=rng.randrange(-u*u,u*u);c1=c0+rng.randrange(0,u)
                terms.append((rng.randrange(n+1),rng.randrange(n+1),(c0,c1)))
            vectors.append(terms)
        for Q in boxes:
            for terms in vectors:
                old=m.evaluate(terms,*Q);actual=new(terms,*Q)
                assert old==actual==memo(terms,*Q),(n,Q,terms,old,actual)
                payload.update(repr(actual).encode());count+=1
        # A live n8 module at default160 bits, not only historic precision.
        if n==8:
            strict,_=evaluator(m);assert strict(vectors[-1],*boxes[-1])==m.evaluate(vectors[-1],*boxes[-1])
        changed=SimpleNamespace(S=u,power=m.power,mul=m.mul);guarded,_=evaluator(changed,expected_unit=u);changed.S=u+1
        try:guarded([],boxes[0][0],boxes[0][1])
        except ValueError:pass
        else:raise AssertionError('scale mutation accepted')
        rows.append({'n':n,'precision':m.PREC,'comparisons':len(boxes)*len(vectors),'cache':cache.cache_info()._asdict()})
    bad=[([],[],0),([],[],-1),([],[],True),([(0,0,(True,1))],[[ (0,1) ]],1<<160),([(-1,0,(0,1))],[[ (0,1) ]],1<<160),([(10**100,0,(0,1))],[[ (0,1) ]],1<<160),([(0,0,(0,1))],[[ (0,) ]],1<<160),([(0,2,(0,1))],[[ (0,1) ]],1<<160)]
    for arguments in bad:
        try:accumulate(*arguments)
        except (ValueError,OverflowError):pass
        else:raise AssertionError(('malformed native input accepted',arguments))
    refusals=[]
    for name in ('t1_native.py','t1_native_build.py','t1_native_produce.py','t1_native_controls.py','t1_native_edge_controls.py'):
        for flag in ('-O','-OO'):
            r=subprocess.run([sys.executable,flag,str(Path(__file__).with_name(name))],capture_output=True,text=True)
            assert r.returncode and 'refuse' in r.stderr,(name,flag,r)
            refusals.append([name,flag])
    result={'all_controls_passed':True,'count_certified':False,'rows':rows,'exact_endpoint_equalities':count,'endpoint_payload_sha256':payload.hexdigest(),'malformed_inputs_rejected':len(bad),'optimized_refusals':refusals,'seconds':time.monotonic()-start}
    Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
