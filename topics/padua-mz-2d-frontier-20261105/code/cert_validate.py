#!/usr/bin/env python3
"""Developer regression against frozen Fraction pencil; not independent audit."""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import time

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--scratch',type=Path,required=True)
    ap.add_argument('--m',nargs='+',type=int,default=[2,3,10,11,20,30,40]);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();source=ROOT/'tracks/mz-constants/code/mz2d_exact.py'
    spec=importlib.util.spec_from_file_location('frozen',source);frozen=importlib.util.module_from_spec(spec);spec.loader.exec_module(frozen)
    out={'kind':'developer full-entry exact regression; not independent checker',
         'frozen_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'results':[]}
    for m in args.m:
        start=time.monotonic();prefix=args.scratch/f'm{m}';path=prefix.with_suffix('.exact')
        if not path.exists():subprocess.run([str(args.scratch/'cert_pencil'),str(m),str(prefix)],check=True)
        basis,H,Q,blocks=frozen.pencil(m);count=0
        with path.open() as f:
            mm,n0,n1,off=map(int,f.readline().split())
            if mm!=m or [n0,n1]!=list(map(len,blocks)):raise ValueError('header mismatch')
            for indices in blocks:
                D=int(f.readline())
                if D<=0:raise ValueError('nonpositive denominator')
                for matrix in (H,Q):
                    for i in indices:
                        for j in indices:
                            value=Fraction(int(f.readline()),D)
                            if value!=matrix[i][j]:raise ValueError(f'exact entry mismatch m={m} ({i},{j})')
                            count+=1
            if f.read():raise ValueError('trailing data')
        out['results'].append({'m':m,'checked_exact_entries':count,'checked_offblock_upper_entries':off,
                               'seconds':time.monotonic()-start,'equal':True})
        args.output.write_text(json.dumps(out,indent=1)+'\n');print('exact entries match',m,count,flush=True)
if __name__=='__main__':main()
