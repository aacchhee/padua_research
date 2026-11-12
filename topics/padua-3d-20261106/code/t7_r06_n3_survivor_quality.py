#!/usr/bin/env python3
"""Attempt common-mesh quality for every full-rank n3 pilot witness."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from t7_r06_search import hpoints,basis_torus,mesh_eval,quality,meta,require
from t7_r06_census_reduced import torus_nodes


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();inp=args.output_dir/'census-reduced-pilot-n3-from20.jsonl';outpath=args.output_dir/'t7-r06-n3-pilot-quality.jsonl'
    _,E=mesh_eval(3);counts=Counter();cache={};gcache={};best=None;worst=None;maxcond=0.;maxresidual=0.
    with inp.open() as source,outpath.open('w') as raw:
        for line in source:
            rec=json.loads(line)
            if rec['decision']!='exact full-rank specialization':continue
            counts['witnesses_attempted']+=1;h=tuple(rec['hnf'])
            if h not in gcache:gcache[h]=hpoints(h)
            p,m,g=gcache[h];q,D,fold=torus_nodes(p,m,rec['orders'],rec['phase_stratum']);key=(D,tuple(map(tuple,fold)))
            if key not in cache:
                cache[key]=quality(basis_torus(fold,D,(0,0,0),3),E)
            qual=cache[key];row={'hnf':h,'phase_stratum':rec['phase_stratum'],'quality':qual}
            if qual is None:counts['floating_rank_inconclusive']+=1
            else:
                counts['quality_measured']+=1;maxcond=max(maxcond,qual['condition2']);maxresidual=max(maxresidual,qual['inverse_residual_inf'])
                if best is None or qual['lambda21']<best['quality']['lambda21']:best=row
                if worst is None or qual['lambda21']>worst['quality']['lambda21']:worst=row
            raw.write(json.dumps(row)+'\n')
    out=meta(args);out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();out['input_raw_sha256']=hashlib.sha256(inp.read_bytes()).hexdigest()
    out['counts']=dict(counts);out['distinct_rational_node_sets']=len(cache);out['best']=best;out['worst']=worst;out['maximum_condition2']=maxcond;out['maximum_inverse_residual_inf']=maxresidual
    out['raw']={'path':str(outpath),'bytes':outpath.stat().st_size,'sha256':hashlib.sha256(outpath.read_bytes()).hexdigest()};out['seconds']=time.monotonic()-start
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large');print(json.dumps({'counts':dict(counts),'seconds':out['seconds']}))


if __name__=='__main__':main()
