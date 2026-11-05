#!/usr/bin/env python3
"""Hybrid native port: C/GMP pencil, native FLINT congruences, integer checks.

Numerical SciPy proposes transforms and rational endpoints only. Acceptance
uses no floating tolerances. Bulk matrices/transforms remain in --scratch.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time
from fractions import Fraction

import flint
from flint import fmpz_mat
import numpy as np
import scipy
import scipy.linalg

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
INPUT='83cf6f1ee244f2e72057332a7ec04ee74db1f0de'
FROZEN={10:('356191/1000000','204357/125000'),20:('272233/1000000','1723313/1000000'),
        30:('47341/200000','1757929/1000000'),40:('214817/1000000','222261/125000')}
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def require(test,message):
    if not test:raise ValueError(message)

def check(B,expected_dimension):
    require(B.nrows()==B.ncols()==expected_dimension,'wrong dimensions')
    require(B==B.transpose(),'nonsymmetric congruence')
    neg=0;minimum=None
    for i in range(expected_dimension):
        d=B[i,i]
        margin=abs(d)-sum(abs(B[i,j]) for j in range(expected_dimension) if j!=i)
        require(margin>0,'strict diagonal dominance rejected')
        neg+=int(d<0);minimum=margin if minimum is None else min(minimum,margin)
    return {'negative':neg,'zero':0,'positive':expected_dimension-neg,
            'minimum_strict_dominance_margin':str(minimum)}

def controls():
    cases=[('zero',fmpz_mat([[0]])),('boundary',fmpz_mat([[1,1],[1,1]])),
           ('nonsymmetric',fmpz_mat([[3,1],[0,3]])),('indefinite_nondominant',fmpz_mat([[1,2],[2,-1]]))]
    out=[]
    for name,B in cases:
        try:check(B,B.nrows())
        except ValueError as e:out.append({'case':name,'rejected':str(e)})
        else:raise RuntimeError('malformed control accepted: '+name)
    out.append({'case':'mixed_sign_dominant','accepted':check(fmpz_mat([[-3,1],[1,3]]),2)})
    return out

def run(m,args,binary):
    started=time.monotonic();prefix=args.scratch/f'm{m}'
    proc=subprocess.run([str(binary),str(m),str(prefix)],check=True,capture_output=True,text=True)
    native_seconds=time.monotonic()-started
    exact=prefix.with_suffix('.exact');floats=prefix.with_suffix('.float')
    times={'native_pencil_seconds':native_seconds};blocks=[];dim=0
    with exact.open() as f,floats.open('rb') as ff:
        mm,n0,n1,off=map(int,f.readline().split());require(mm==m,'native m mismatch')
        for bi,n in enumerate((n0,n1)):
            D=int(f.readline());require(D>0,'nonpositive native scale')
            H=fmpz_mat(n,n,[int(f.readline()) for _ in range(n*n)])
            Q=fmpz_mat(n,n,[int(f.readline()) for _ in range(n*n)])
            Hf=np.fromfile(ff,dtype=np.float64,count=n*n).reshape(n,n)
            Qf=np.fromfile(ff,dtype=np.float64,count=n*n).reshape(n,n)
            require(H==H.transpose() and Q==Q.transpose(),'native asymmetry')
            st=time.monotonic();vals,v=scipy.linalg.eigh(Qf,Hf,check_finite=True)
            times[f'block{bi}_proposal_seconds']=time.monotonic()-st
            R=fmpz_mat([[int(round(float(x)*args.scale)) for x in row] for row in v])
            # This distribution changes evaluation order only:
            # R^T (td*Q-tn*H) R = td*(R^T Q R)-tn*(R^T H R).
            st=time.monotonic();RT=R.transpose();BH=RT*H*R;BQ=RT*Q*R
            times[f'block{bi}_congruence_seconds']=time.monotonic()-st
            require(BH==BH.transpose() and BQ==BQ.transpose(),'congruence asymmetry')
            transform=prefix.with_name(prefix.name+f'-R{bi}.txt')
            transform.write_text('\n'.join(' '.join(str(R[i,j]) for j in range(n)) for i in range(n))+'\n')
            blocks.append((n,D,BH,BQ,vals[0],vals[-1],digest(transform),str(transform)))
            dim+=n
        require(f.read()=='','extra exact input');require(ff.read()==b'','extra float input')
    vmin=min(x[4] for x in blocks);vmax=max(x[5] for x in blocks)
    width=Fraction(args.width);brackets=[]
    for value in (vmin,vmax):
        lo=math.floor(float(value)/float(width))*width;brackets.append((lo,lo+width))
    if m in FROZEN and width==Fraction(1,10**6):
        require(tuple(str(x[0]) for x in brackets)==FROZEN[m],'PD-T107 bracket mismatch')
    checks=[]
    for name,(lo,hi),expected in zip(('minimum','maximum'),brackets,((0,1),(dim-1,dim))):
        endpoints=[]
        for t,wanted in zip((lo,hi),expected):
            st=time.monotonic();entries=[]
            for n,D,BH,BQ,_,__,sha,path in blocks:
                B=t.denominator*BQ-t.numerator*BH
                rec=check(B,n);rec.update(dimension=n,positive_common_denominator=str(D*t.denominator),integer_transform_sha256=sha)
                entries.append(rec)
            total=sum(x['negative'] for x in entries);require(total==wanted,'wrong exact endpoint inertia')
            endpoints.append({'endpoint':str(t),'negative':total,'zero':0,'positive':dim-total,'blocks':entries,'seconds':time.monotonic()-st})
        checks.append({'extremum':name,'open_interval':[str(lo),str(hi)],'lower':endpoints[0],'upper':endpoints[1]})
    result={'m':m,'n':m-1,'dimension':dim,'measured_extrema':[float(vmin),float(vmax)],
            'checked_offblock_upper_entries':off,'integer_transform_rounding_scale':str(args.scale),'checks':checks,
            'times':times,'wall_seconds':time.monotonic()-started,'peak_self_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'native_stderr':proc.stderr.strip(),'native_exit_code':proc.returncode,
            'bulk':[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in [exact,floats]+[Path(x[7]) for x in blocks]]}
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',nargs='+',type=int,required=True)
    ap.add_argument('--scratch',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True)
    ap.add_argument('--scale',type=int,default=10**12);ap.add_argument('--width',default='1/1000000')
    args=ap.parse_args();args.scratch.mkdir(parents=True,exist_ok=True);args.output_dir.mkdir(parents=True,exist_ok=True)
    require(args.scale>0 and Fraction(args.width)>0,'nonpositive proposal scale or width')
    binary=args.scratch/'cert_pencil';source=HERE/'cert_pencil.c'
    compile_command=['cc','-O3','-std=c11','-Wall','-Wextra',str(source),'-lgmp','-o',str(binary)]
    cp=subprocess.run(compile_command,check=True,capture_output=True,text=True)
    metadata={'status':'exact development execution; separate independent checker and rerun required',
        'rules_input_sha':INPUT,'command':sys.argv,'python':sys.version,'platform':platform.platform(),
        'numpy':np.__version__,'scipy':scipy.__version__,'python_flint':flint.__version__,'flint':flint.__FLINT_VERSION__,
        'environment':{k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        'source_sha256':{p.name:digest(p) for p in (source,Path(__file__))},'binary_sha256':digest(binary),
        'frozen_producer_sha256':digest(ROOT/'tracks/mz-constants/code/mz2d_exact.py'),
        'definitions_sha256':digest(ROOT/'topics/padua-mz-2d-20261101/definitions.md'),
        'compiler':subprocess.check_output(['cc','--version'],text=True).splitlines()[0],
        'compile_command':compile_command,'compile_warnings':cp.stderr,'controls':controls()}
    for m in args.m:
        print('start exact native',m,flush=True);out=dict(metadata);out['result']=run(m,args,binary)
        path=args.output_dir/f'cert-m{m}.json';path.write_text(json.dumps(out,indent=1)+'\n')
        print('done exact native',m,'seconds',out['result']['wall_seconds'],'receipt',path,flush=True)

if __name__=='__main__':main()
