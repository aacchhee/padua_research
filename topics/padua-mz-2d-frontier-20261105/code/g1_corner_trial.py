#!/usr/bin/env python3
"""Floating Rayleigh tests of normalized continuous corner kernels."""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from g1_spectral import PaduaOperator


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',nargs='+',type=int,default=[100,400,1000,2000]);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    report=dict(status='MEASURED',rigorous_enclosures=False,command=sys.argv,
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        operator_code_sha256=hashlib.sha256(Path(__file__).with_name('g1_spectral.py').read_bytes()).hexdigest(),results=[])
    for m in args.m:
        start=time.monotonic();op=PaduaOperator(m,m-1);a,b=op.idx.T
        v=np.sqrt((2*a+1)*(2*b+1))/2
        sign=(-1.)**(a if m%2==0 else b)
        for name,z in [('single',v),('symmetric',v*(1+sign)),('antisymmetric',v*(1-sign))]:
            norm2=float(z@z);z=z/np.sqrt(norm2);av=op@z
            row=dict(m=m,n=m-1,trial=name,second_corner=[-1,1] if m%2==0 else [1,-1],
                unnormalized_continuous_norm_squared=norm2,rayleigh=float(z@av),
                relative_eigenvector_residual=float(np.linalg.norm(av-(z@av)*z)),
                seconds_since_m_start=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            report['results'].append(row);args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(json.dumps(report,indent=2)+'\n');print(m,name,row['rayleigh'],flush=True)

if __name__=='__main__':main()
