#!/usr/bin/env python3
"""Minimum-only floating sign screen; exploratory m>1000 is post hoc."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy.sparse.linalg import eigsh
from g1_spectral import PaduaOperator


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',type=int,nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--vector-dir',type=Path,required=True);ap.add_argument('--ncv',type=int,default=40);args=ap.parse_args()
    report=dict(status='MEASURED',rigorous_enclosures=False,command=sys.argv,code_sha256=sha(__file__),
        operator_code_sha256=sha(Path(__file__).with_name('g1_spectral.py')),seed=20261105,tolerance=2e-11,ncv=args.ncv,
        exploratory_scope='m>1000 requested post hoc by orchestrator on 2026-11-05 after lower corner branch observed',results=[])
    args.output.parent.mkdir(parents=True,exist_ok=True);args.vector_dir.mkdir(parents=True,exist_ok=True)
    for m in args.m:
        tick=time.monotonic();op=PaduaOperator(m,m-1);rng=np.random.default_rng(20261105)
        values,vectors=eigsh(op,k=1,which='SA',v0=rng.standard_normal(op.shape[0]),ncv=args.ncv,tol=2e-11,maxiter=20000)
        v=vectors[:,0];v/=np.linalg.norm(v);av=op@v;ray=float(v@av)
        path=args.vector_dir/f'm{m}-n{m-1}-min.npy';np.save(path,v)
        row=dict(m=m,n=m-1,dimension=op.shape[0],minimum=ray,residual_2_float=float(np.linalg.norm(av-ray*v)),
            matvecs=op.calls,seconds=time.monotonic()-tick,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            vector=dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size))
        report['results'].append(row);args.output.write_text(json.dumps(report,indent=2)+'\n')
        print(m,ray,row['residual_2_float'],row['seconds'],flush=True)

if __name__=='__main__':main()
