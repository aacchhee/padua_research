#!/usr/bin/env python3
"""MEASURED quality of every full n2 census survivor representative."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from t7_r06_search import hpoints,basis_torus,mesh_eval,quality,meta,require


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();top=Path(__file__).resolve().parents[1];start=time.monotonic();inp=top/'evidence/t7-r06-census-n2-complete.json'
    census=json.loads(inp.read_text());require(census['full_census'],'requires completed census')
    rows=[];_,E=mesh_eval(2)
    for rec in census['survivor_classes']:
        require(all(k>=0 for k in rec['phase_stratum']),'no positive-dimensional survivor allowed in this summary')
        p,m,_=hpoints(rec['hnf']);a=np.array([k/(2*mj) for k,mj in zip(rec['phase_stratum'],rec['orders'])])
        D=math_lcm(m,*[2*mj for mj in rec['orders']]);q=(p*(D//m)+np.rint(a*D).astype(int))%D
        fold=np.unique(np.minimum(q,(-q)%D),axis=0);V=basis_torus(fold,D,(0,0,0),2)
        rows.append({'order':rec['order'],'hnf':rec['hnf'],'phase_stratum':rec['phase_stratum'],'quality':quality(V,E)})
    primepath=args.output_dir/'census-complete-primes-n2.jsonl'
    for line in primepath.read_text().splitlines():
        rec=json.loads(line)
        if rec['rank_exact']!=10:continue
        p,m,_=hpoints(rec['hnf']);fold=np.unique(np.minimum(p,(-p)%m),axis=0)
        rows.append({'order':m,'hnf':rec['hnf'],'quality':quality(basis_torus(fold,m,(0,0,0),2),E)})
    out=meta(args);out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();out['input_receipt_sha256']=hashlib.sha256(inp.read_bytes()).hexdigest()
    out['survivors_measured']=len(rows);out['orders']=dict(Counter(r['order'] for r in rows));out['order16']=[r for r in rows if r['order']==16]
    out['best_lambda21']=min(r['quality']['lambda21'] for r in rows);out['worst_lambda21']=max(r['quality']['lambda21'] for r in rows)
    raw=args.output_dir/'t7-r06-census-quality.json';raw.write_text(json.dumps(rows,indent=2)+'\n')
    out['raw']={'path':str(raw),'bytes':raw.stat().st_size,'sha256':hashlib.sha256(raw.read_bytes()).hexdigest()};out['seconds']=time.monotonic()-start
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large');print(json.dumps(out))


def math_lcm(*values):
    import math
    return math.lcm(*values)


if __name__=='__main__':main()
