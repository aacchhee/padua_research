#!/usr/bin/env python3
"""Frozen finite HNF neighborhoods; not a global minimum search."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import time

import t10_lattices as t

def main(a):
    result={'scope':'n4..16 fixed source diagonals, b±1,c/e±4,f packing lower endpoint through seed',
            'status':'MEASURED exact bounded search','rows':[]}
    raw=[]
    for n in range(4,17):
        seed=next(t.candidates(n))[1]; aa,dd,ff=map(int,seed.diagonal())
        lo=(38*n**3+27*aa*dd-1)//(27*aa*dd)
        start=time.monotonic();count=0;passing=[];complete=True
        for f in range(lo,ff+1):
            bs=sorted({(int(seed[0,1])+i)%dd for i in range(-1,2)})
            cs=sorted({(int(seed[0,2])+i)%f for i in range(-4,5)})
            es=sorted({(int(seed[1,2])+i)%f for i in range(-4,5)})
            K=t.shell(2*n-1)
            for b,c,e in itertools.product(bs,cs,es):
                B=t.matrix((aa,b,c,dd,e,f));count+=1
                if not t.contains(B,K).any():
                    r=t.certify(n,'HNF-neighborhood',B);passing.append(r);raw.append(r)
                if time.monotonic()-start>a.cap:
                    complete=False;break
            if not complete:break
        assert passing or not complete
        row={'n':n,'complete':complete,'tested':count,'admissible':len(passing),
             'f_interval':[lo,ff],'seconds':time.monotonic()-start}
        if passing:
            best=min(passing,key=lambda r:(r['det'],r['fold'],-r['rank'],r['B']))
            row['minimum_det_in_box']=best['det']
            row['best_at_min_det']={k:best[k] for k in ['B','fold','degree','rank','node_sha256']}
            full=[r for r in passing if r['rank']==t.math.comb(n+3,3)]
            if full:
                full=min(full,key=lambda r:(r['fold'],r['det'],r['B']))
                row['smallest_full_rank_fold_in_box']={k:full[k] for k in ['B','det','fold','rank','node_sha256']}
        result['rows'].append(row)
        print(row,flush=True)
    a.raw.write_text(json.dumps(raw,sort_keys=True,separators=(',',':'))+'\n')
    result.update({'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'helper_sha256':hashlib.sha256(Path(t.__file__).read_bytes()).hexdigest(),
       'raw_sha256':hashlib.sha256(a.raw.read_bytes()).hexdigest(),'raw_bytes':a.raw.stat().st_size,
       'raw_policy':'regenerate-only'})
    a.out.write_text(json.dumps(result,separators=(',',':'))+'\n')
    assert a.out.stat().st_size<16384

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--raw',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--cap',type=float,default=120)
    main(p.parse_args())
