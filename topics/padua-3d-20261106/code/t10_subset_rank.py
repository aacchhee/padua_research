#!/usr/bin/env python3
"""Exact finite-field full-rank certificates for frozen QR subsets.

A nonzero determinant after a primitive-q-root specialization proves the
cyclotomic determinant is nonzero. A deficient specialization is inconclusive.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import scipy.linalg as la
from sympy import factorint,isprime,primitive_root
import t10_lattices as t

def determinant_mod(A,p):
    A=A.copy();N=len(A);det=1
    for j in range(N):
        ids=np.flatnonzero(A[j:,j])
        if not len(ids):return j,0
        i=j+int(ids[0])
        if i!=j:A[[j,i]]=A[[i,j]];det=-det
        pivot=int(A[j,j]);det=det*pivot%p
        if j+1<N:
            factors=A[j+1:,j]*pow(pivot,-1,p)%p
            A[j+1:,j+1:]=(A[j+1:,j+1:]-factors[:,None]*A[j,j+1:])%p
            A[j+1:,j]=0
    return N,det

def main(a):
    data=json.loads(a.census.read_text());expected={}
    if a.extraction:
        expected={r['n']:r['selected_node_sha256'] for r in json.loads(a.extraction.read_text()) if r['name']=='extract-QR'}
    rows=[]
    for n in range(2,17):
        N=math.comb(n+3,3)
        best=min((r for r in data['rows'] if r['n']==n and r['rank']==N),key=lambda r:(r['fold'],r['det'],r['family']))
        q,K,w,P=t.folded(np.array(best['B']))
        ids=la.qr(t.basis(P,n).T,pivoting=True,mode='economic',check_finite=False)[2][:N]
        selected=[K[int(i)] for i in ids]
        payload=json.dumps({'denominator':q,'selected_folded_keys':selected},separators=(',',':')).encode()
        nodehash=hashlib.sha256(payload).hexdigest()
        if n in expected:assert nodehash==expected[n]
        k=1
        while not isprime(q*k+1):k+=1
        p=q*k+1;zeta=pow(int(primitive_root(p)),k,p)
        assert pow(zeta,q,p)==1 and all(pow(zeta,q//d,p)!=1 for d in factorint(q))
        xs=np.array([[(pow(zeta,h,p)+pow(zeta,-h,p))*pow(2,-1,p)%p for h in row] for row in selected],dtype=np.int64)
        tables=[]
        for axis in range(3):
            T=[np.ones(N,dtype=np.int64),xs[:,axis]]
            for j in range(2,n+1):T.append((2*xs[:,axis]*T[-1]-T[-2])%p)
            tables.append(T)
        V=np.array([tables[0][aa]*tables[1][bb]%p*tables[2][cc]%p for aa,bb,cc in t.exponents(n)]).T
        rank,det=determinant_mod(V,p)
        assert rank==N and det!=0
        rows.append([n,q,p,zeta,N,rank,det,nodehash]);print(rows[-1],flush=True)
    out={'status':'MEASURED exact full-rank certificates; independent replay needed for computer-proof status',
      'columns':['n','root_order_q','prime_p','primitive_q_root','N','rank_mod_p','det_mod_p','selected_node_sha256'],
      'rows':rows,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'helper_sha256':hashlib.sha256(Path(t.__file__).read_bytes()).hexdigest(),
      'input_sha256':hashlib.sha256(a.census.read_bytes()).hexdigest(),
      'reduction':'Map Z[zeta_q,1/2] into F_p using the certified primitive q-root. Nonzero determinant image implies nonzero characteristic-zero determinant. Deficient images would be inconclusive.'}
    a.out.write_text(json.dumps(out,separators=(',',':'))+'\n')
    assert a.out.stat().st_size<16384

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--census',type=Path,required=True)
    p.add_argument('--extraction',type=Path);p.add_argument('--out',type=Path,required=True)
    main(p.parse_args())
