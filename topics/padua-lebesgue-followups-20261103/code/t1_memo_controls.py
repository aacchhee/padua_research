"""Compare cached/frozen exact endpoints on frozen n4--7 certificate data."""
if not __debug__:
    raise RuntimeError('T1 refuses optimized Python: t1_memo_controls.py')
import argparse,gzip,lzma,json,sys,hashlib,importlib,time
from pathlib import Path
from fractions import Fraction
from t1_memo import evaluator
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))

def load(path):
    raw=path.read_bytes();data=gzip.decompress(raw)if raw[:2]==b'\x1f\x8b'else lzma.decompress(raw)
    return raw,json.loads(data)

def box_for(path,unit):
    Q=[(-unit,unit),(-unit,unit)]
    for bit in path:
        axis=0 if Q[0][1]-Q[0][0]>=Q[1][1]-Q[1][0]else 1
        lo,hi=Q[axis];mid=(lo+hi)//2;Q[axis]=(lo,mid)if bit=='0'else(mid,hi)
    return tuple(Q)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--frozen-output-dir',required=True);parser.add_argument('--output',required=True);a=parser.parse_args()
    start=time.monotonic();rows=[]
    for n in range(4,8):
        t=time.monotonic();m=importlib.import_module('a5_n%d_boxes'%n);nodes,L=m.construct()
        file=Path(a.frozen_output_dir)/('a5_n%d_certificate.json.'%n+('xz'if n==7 else'gz'))
        raw,data=load(file);new,cache=evaluator(m);unit=m.S
        leaves=data['leaves'];indices=sorted(set([0,len(leaves)-1]+[i*len(leaves)//40 for i in range(40)]))
        boxes=[box_for(leaves[i]['path'],unit)for i in indices]
        boxes += [tuple(tuple(int(Fraction(v)*unit)for v in z)for z in r['R'])for r in data['interior_roots']]
        boxes += [((-unit,unit),(-unit,unit)),((0,0),(0,0)),((int(unit//3),int(unit//3)),(-unit//7,unit//7))]
        polynomials=[m.terms(q)for p in L for q in(p,p.diff(m.x),p.diff(m.y),p.diff((m.x,2)),p.diff(m.x).diff(m.y),p.diff((m.y,2)))]
        count=0;old_seconds=new_seconds=0;payload=hashlib.sha256()
        for Q in boxes:
            for terms in polynomials:
                before=time.monotonic();old=m.evaluate(terms,*Q);old_seconds+=time.monotonic()-before
                before=time.monotonic();cached=new(terms,*Q);new_seconds+=time.monotonic()-before
                assert old==cached,(n,Q,old,cached)
                payload.update(repr(old).encode());count+=1
        # Actual signed root-polynomial coefficient vectors also cover sums.
        for root in data['interior_roots']:
            mask=root['mask'];p=sum(((1 if mask>>i&1 else-1)*q for i,q in enumerate(L)),m.s.Poly(0,m.x,m.y,domain=m.K))
            Q=tuple(tuple(int(Fraction(v)*unit)for v in z)for z in root['R'])
            for q in(p,p.diff(m.x),p.diff(m.y),p.diff((m.x,2)),p.diff(m.x).diff(m.y),p.diff((m.y,2))):
                terms=m.terms(q);old=m.evaluate(terms,*Q);cached=new(terms,*Q);assert old==cached;count+=1;payload.update(repr(old).encode())
        row=dict(n=n,certificate_sha256=hashlib.sha256(raw).hexdigest(),exact_endpoint_equalities=count,cardinal_derivative_vectors=len(polynomials),boxes=len(boxes),old_seconds=old_seconds,cached_seconds=new_seconds,speedup=old_seconds/new_seconds,endpoint_payload_sha256=payload.hexdigest(),seconds=time.monotonic()-t,cache=cache.cache_info()._asdict())
        rows.append(row);print(json.dumps(row),flush=True)
    result=dict(all_controls_passed=True,count_certified=False,rows=rows,seconds=time.monotonic()-start,memo_source_sha256=hashlib.sha256(Path(__file__).with_name('t1_memo.py').read_bytes()).hexdigest())
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
