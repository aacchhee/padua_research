"""Run the literally unchanged frozen corner tail; no interior/edge count."""
import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import time

MAIN_SHA='a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True)
    ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
    frozen=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
    sys.path.insert(0,str(frozen));import a5_checker_n8 as check
    source=Path(check.__file__);raw=source.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==MAIN_SHA
    input_raw=Path(a.input).read_bytes()
    data=json.loads(check.decode_payload(input_raw),object_pairs_hook=check.unique_object)
    verifier=check.Verifier(data['field_embedding'])
    # Proposal only: use exact native substitutions to label nodes and provide
    # zero lists. All maximum predicates are then checked by the frozen tail.
    corners=[];cid=0
    for u,v in((-1,-1),(-1,1),(1,-1),(1,1)):
        values=[p.rep.eval(check.native(u),0).eval(check.native(v),0)for p in verifier.cardinals]
        if values.count(check.FIELD.one)==1 and values.count(check.FIELD.zero)==44:
            row={'point':[u,v],'kind':'node'}
        else:
            row={'point':[u,v],'kind':'max','id':cid,
                 'zeros':[i for i,x in enumerate(values)if x==check.FIELD.zero]};cid+=1
        corners.append(row)
    module=ast.parse(raw)
    cls=next(n for n in module.body if isinstance(n,ast.ClassDef)and n.name=='Verifier')
    fn=next(n for n in cls.body if isinstance(n,ast.FunctionDef)and n.name=='boundaries')
    index=next(i for i,n in enumerate(fn.body)if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='expected_corners'for t in n.targets))
    body=fn.body[index:]
    tail_sha=hashlib.sha256(ast.dump(ast.Module(body=body,type_ignores=[]),include_attributes=False).encode()).hexdigest()
    wrapper=ast.parse('def corner_tail(self,corners,edge_roots,corner_roots,edge_dispositions,total_edge_patterns):\n pass\n').body[0]
    wrapper.body=body;namespace=dict(vars(check))
    exec(compile(ast.fix_missing_locations(ast.Module(body=[wrapper],type_ignores=[])),'<unchanged-frozen-corner-tail>','exec'),namespace)
    result=namespace['corner_tail'](verifier,corners,[],[],Counter(),0)
    assert hashlib.sha256(source.read_bytes()).hexdigest()==MAIN_SHA
    result.update(count_certified=False,scope='corner predicates only; empty edge accumulators are placeholders, not edge evidence',
                  checker_sha256=MAIN_SHA,corner_tail_ast_sha256=tail_sha,
                  driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256=hashlib.sha256(input_raw).hexdigest(),corners=corners,
                  seconds=time.monotonic()-start)
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
