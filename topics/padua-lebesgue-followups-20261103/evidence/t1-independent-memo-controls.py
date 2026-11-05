"""Independent producer cache edge-case controls, with frozen arithmetic."""
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    args=parser.parse_args()
    topic=Path(__file__).resolve().parents[1]
    frozen=topic.parent/'padua-proof-attempts-2-20261101'/'code'
    sys.path[:0]=[str(topic/'code'),str(frozen)]
    from t1_memo import evaluator
    sources=[topic/'code'/'t1_memo.py',Path(__file__)]
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    rows=[]
    for n in range(4,9):
        m=importlib.import_module('a5_n%d_boxes'%n);unit=m.S
        source=Path(m.__file__);sources.append(source)
        new,cache=evaluator(m)
        boxes=[((-unit,unit),(-unit,unit)),((0,0),(0,0)),
               ((-3*unit,-2*unit),(unit//7,unit//3)),
               ((-unit//7,unit//3),(-unit//11,unit//5)),
               ((-1,0),(0,1)),((1,1),(-1,-1))]
        coefficients=[(-unit,unit),(0,0),(-7,11),(-3*unit,-unit),
                      (unit//13,unit//11),(unit,unit)]
        terms=[(),*((((i,j,c),))for i in range(n+1)for j in range(n+1-i)for c in coefficients)]
        half=n//2
        terms.extend([((n,0,(-7,11)),(0,n,(-13,-1)),(half,half,(-unit,unit)),
                       (half,half,(unit//7,unit//3))),
                      ((0,0,(-7,11)),(0,0,(-11,7)))])
        count=0
        for X,Y in boxes:
            for p in terms:
                assert m.evaluate(p,X,Y)==new(p,X,Y),(n,X,Y,p)
                count+=1
        table=cache(0,0,0,0)
        assert table is cache(0,0,0,0)
        try:table[0][0][0]=1
        except TypeError:pass
        else:raise AssertionError('mutable table')
        for i in range(600):cache(i,i+1,-i-1,-i)
        assert cache.cache_info().currsize<=512
        for value in (True,0.0):
            try:cache(value,0,0,0)
            except AssertionError:pass
            else:raise AssertionError('noninteger endpoint accepted')
        standin=SimpleNamespace(S=unit,power=m.power,mul=m.mul)
        changed,_=evaluator(standin);changed((),(0,0),(0,0));standin.S=unit*2
        try:changed((),(0,0),(0,0))
        except AssertionError:pass
        else:raise AssertionError('changed scale accepted')
        rows.append({'n':n,'exact_endpoint_equalities':count,
                     'cache_immutable':True,'cache_bounded':True,
                     'noninteger_endpoints_rejected':True,'changed_scale_rejected':True})
    result={'all_controls_passed':True,'count_certified':False,
            'scope':'exact cache endpoint identities and fault controls only',
            'rows':rows,'source_sha256':{str(p):sha(p)for p in sources}}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
