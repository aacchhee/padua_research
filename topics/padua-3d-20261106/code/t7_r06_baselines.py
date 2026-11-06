#!/usr/bin/env python3
"""Inherited unscaled-QR baseline, preserving family optimization outputs."""
import argparse
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.linalg import qr
from t7_r06_search import old,mesh_eval,quality,basis_x,meta

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--receipt',type=Path,required=True);args=ap.parse_args()
    t=time.monotonic();out=meta(args);out['baseline_correction']='Primary QR pivots use inherited UNscaled product-Chebyshev columns; previous receipt QR was orthonormal-column extraction, a distinct secondary comparator.'
    rows=[]
    for n in range(3,7):
        _,E=mesh_eval(n);cand=np.array(list(it.product(old.lobatto(2*n+1),repeat=3)))
        piv=qr(old.basis(cand,n).T,pivoting=True,mode='economic')[2]
        X=cand[piv[:math.comb(n+3,3)]]
        rows.append({'n':n,'inherited_unscaled_qr':quality(basis_x(X,n),E),'nodes_sha256':hashlib.sha256(X.tobytes()).hexdigest()})
    out['baselines']=rows;out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();out['seconds']=time.monotonic()-t
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(rows))

if __name__=='__main__':main()
