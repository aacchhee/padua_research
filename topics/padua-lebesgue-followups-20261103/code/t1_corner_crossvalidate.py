"""Native ANP corner-evaluation equality against frozen Poly.eval, n4--7."""
import argparse, hashlib, importlib, json, sys, time
from pathlib import Path
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.monotonic();rows=[]
    for n in range(4,8):
        t=time.monotonic();m=importlib.import_module('a5_n%d_boundary'%n);nodes,L=m.construct()
        pairs=0; payload=[]
        for u,v in((-1,-1),(-1,1),(1,-1),(1,1)):
            for p in L:
                for q in(p,p.diff(m.x),p.diff(m.y)):
                    native=sum((c*u**i*v**j for(i,j),c in q.rep.to_dict().items()),m.K.zero)
                    symbolic=m.K.convert(q.eval(m.x,u).eval(m.y,v))
                    assert native==symbolic,(n,u,v,q)
                    payload.append(tuple(str(c)for c in native.to_list()));pairs+=1
        row=dict(n=n,cardinals=len(L),exact_value_derivative_equalities=pairs,seconds=time.monotonic()-t,payload_sha256=hashlib.sha256(repr(payload).encode()).hexdigest(),source_sha256=hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest())
        rows.append(row);print(json.dumps(row),flush=True)
    result=dict(accepted=True,scope='native coefficient-sum evaluation equals frozen symbolic Poly.eval at all cardinal corner values and first derivatives for n4--7; no count certification',rows=rows,seconds=time.monotonic()-start)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
