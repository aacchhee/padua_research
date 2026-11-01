#!/usr/bin/env python3
"""Fresh finite checks of orthogonality, cross blocks and determinant scaling."""
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json
import sys
import numpy as np


def axis(m,n):
    theta=np.arange(m+1)*np.pi/m
    weights=np.array([0.5]+[1.0]*(m-1)+[0.5])/m
    norms=np.array([1.0 if a in (0,m) else 0.5 for a in range(n+1)])
    phi=np.cos(np.outer(theta,np.arange(n+1)))/np.sqrt(norms)
    return phi,weights


def main():
    rows=[]
    for n,phase in [(1,0),(2,1),(3,0),(4,1),(6,1),(7,0),(8,1)]:
        exps=[(a,b) for a,b in product(range(n+1),repeat=2) if a+b<=n]
        even=[e for e in exps if sum(e)%2==0];odd=[e for e in exps if sum(e)%2]
        exps=even+odd;ne,no=len(even),len(odd)
        px,wx=axis(n,n);py,wy=axis(n+1,n)
        points=list(product(range(n+1),range(n+2)))
        full=np.array([[px[i,a]*py[j,b] for a,b in exps] for i,j in points])
        weights=np.array([wx[i]*wy[j] for i,j in points])
        choose=np.array([(i+j-phase)%4<2 for i,j in points])
        assert choose.sum()==comb(n+2,2)
        V=full[choose];W=weights[choose]
        G=V.T@(W[:,None]*V)
        # Compute the character moments directly from the mathematical sums.
        Zx=np.array([[sum(wx[j]*(1j**j)*px[j,a]*px[j,c] for j in range(n+1)) for c in range(n+1)] for a in range(n+1)])
        Zy=np.array([[sum(wy[j]*(1j**j)*py[j,b]*py[j,d] for j in range(n+2)) for d in range(n+1)] for b in range(n+1)])
        A=np.array([[np.real((1-1j)*(1j**(-phase))*Zx[a,c]*Zy[b,d]) for c,d in odd] for a,b in even])
        block=np.block([[np.eye(ne),A],[A.T,np.eye(no)]])/2
        full_res=float(np.max(np.abs(full.T@(weights[:,None]*full)-np.eye(len(exps)))))
        gram_res=float(np.max(np.abs(G-block)))
        assert full_res<1e-12 and gram_res<1e-12
        _,lg=np.linalg.slogdet(G);_,lv=np.linalg.slogdet(V);_,ls=np.linalg.slogdet(np.eye(no)-A.T@A)
        first=abs(lg-(2*lv+np.log(W).sum()));second=abs(lg-(-len(exps)*np.log(2)+ls))
        assert first<1e-10 and second<1e-10
        sigma=float(np.linalg.svd(A,compute_uv=False)[0])
        assert sigma<1
        rows.append({'n':n,'phase':phase,'full_grid_orthogonality_residual':full_res,
                     'gram_block_residual':gram_res,'evaluation_logdet_identity_error':first,
                     'schur_logdet_identity_error':second,'measured_sigma':sigma})
    out={'all_checks_passed':True,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'numpy':np.__version__,'status':'MEASURED supplementary checks only; written proof separately audited',
         'rows':rows,'method':'Fresh direct full-grid normalized basis, direct finite complex sums, and two independent determinant identities.'}
    Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'all_checks_passed':True,'cases':len(rows),'max_gram_residual':max(r['gram_block_residual'] for r in rows)}))


if __name__=='__main__':
    main()
