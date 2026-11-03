"""Native all-active corner predicates versus frozen n4--7 certificates."""
import argparse,gzip,lzma,json,sys,hashlib,importlib,time
from pathlib import Path
FROZEN=Path(__file__).resolve().parents[2]/'padua-proof-attempts-2-20261101'/'code'
sys.path.insert(0,str(FROZEN))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--frozen-output-dir',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();rows=[];started=time.monotonic()
    for n in range(4,8):
        m=importlib.import_module('a5_n%d_boundary'%n);nodes,L=m.construct();N=len(L)
        path=Path(a.frozen_output_dir)/('a5_n%d_certificate.json.'%n+('xz'if n==7 else'gz'))
        raw=path.read_bytes();data=json.loads(gzip.decompress(raw)if raw[:2]==b'\x1f\x8b'else lzma.decompress(raw))
        def at(p,u,v):return sum((c*u**i*v**j for(i,j),c in p.rep.to_dict().items()),m.K.zero)
        def sign(c):return m.ksign(c)if n>=6 else m.sign(m.cfield(m.K.to_sympy(c)))
        records=[];cid=0;active=0
        for u,v in((-1,-1),(-1,1),(1,-1),(1,1)):
            vals=[at(p,u,v)for p in L];row={'point':[u,v]}
            if vals.count(m.K.one)==1 and vals.count(m.K.zero)==N-1:row['kind']='node'
            else:
                zeros=[i for i,c in enumerate(vals)if c==m.K.zero];sg=[1 if sign(c)>0 else-1 for c in vals]
                dx=[-u*at(p.diff(m.x),u,v)for p in L];dy=[-v*at(p.diff(m.y),u,v)for p in L]
                for bits in range(1<<len(zeros)):
                    signs=sg[:]
                    for j,b in enumerate(zeros):signs[b]=1 if bits>>j&1 else-1
                    for d in(dx,dy):assert sign(sum((s*c for s,c in zip(signs,d)),m.K.zero))<0
                    active+=1
                row.update(kind='max',id=cid,zeros=zeros);cid+=1
            records.append(row)
        assert records==data['corners'],(n,records,data['corners'])
        row=dict(n=n,certificate_sha256=hashlib.sha256(raw).hexdigest(),all_corners_identical=True,corner_maxima=cid,active_masks_checked=active)
        rows.append(row);print(json.dumps(row),flush=True)
    Path(a.output).write_text(json.dumps(dict(all_controls_passed=True,count_certified=False,scope='native corner predicates against frozen n4--7 corner certificates only',rows=rows,seconds=time.monotonic()-started),indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
