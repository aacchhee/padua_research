#!/usr/bin/env python3
"""Regenerate the degenerate m2 identity case, whose extrema both equal1."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--scratch',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();args.scratch.mkdir(parents=True,exist_ok=True)
    binary=args.scratch/'cert_pencil';source=HERE/'cert_pencil.c'
    subprocess.run(['cc','-O3','-std=c11',str(source),'-lgmp','-o',str(binary)],check=True)
    prefix=args.scratch/'m2';cp=subprocess.run([str(binary),'2',str(prefix)],capture_output=True,text=True,check=True)
    path=prefix.with_suffix('.exact');blocks=[]
    with path.open() as f:
        m,n0,n1,off=map(int,f.readline().split())
        if (m,n0,n1,off)!=(2,2,1,2):raise ValueError('unexpected m2 dimensions')
        for n in (n0,n1):
            d=int(f.readline());h=[int(f.readline()) for _ in range(n*n)];q=[int(f.readline()) for _ in range(n*n)]
            if d<=0 or h!=q:raise ValueError('m2 exact identity failed')
            blocks.append({'dimension':n,'positive_common_denominator':str(d),'scaled_H_equals_Q':True})
        if f.read():raise ValueError('trailing input')
    out={'status':'exact development identity check; independent regeneration of this case pending',
         'rules_input_sha':'83cf6f1ee244f2e72057332a7ec04ee74db1f0de','command':sys.argv,
         'm':2,'n':1,'dimension':3,'exact_extrema':['1','1'],'blocks':blocks,
         'native_input_sha256':sha(path),'native_stderr':cp.stderr.strip(),
         'source_sha256':{source.name:sha(source),Path(__file__).name:sha(Path(__file__))},
         'method':'Entrywise exact H=Q; H positive definite by the continuous Gram identity PD-T106',
         'regression':'Native pencil also matched frozen Fraction pencil in cert-exact-entry-regression.json'}
    args.output.write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':main()
