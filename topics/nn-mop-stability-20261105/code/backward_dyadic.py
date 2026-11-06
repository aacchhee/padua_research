#!/usr/bin/env python3
"""Exact necessary-compatibility obstruction for a frozen native raw array.

Default checks the compact stored dyadic certificate without importing
numerical libraries. --reproduce additionally regenerates the N4 Krawtchouk
LU array and checks that all five dyadic fields equal the frozen witness.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

# b2_00, b1_00, b1_01, a1_10, a2_01, exactly as stored binary64.
WITNESS = ['0', '-3602879701896397/18014398509481984',
           '-4803839602528527/36028797018963968',
           '5764607523034235/18014398509481984',
           '6004799503160661/18014398509481984']
RESIDUAL = Q(25700541873527631,649037107316853453566312041152512)


def check(values):
    b20,b10,b101,a110,a201=map(Q,values)
    r=(b20-b10)*(b101-b10)+a110-a201
    if r!=RESIDUAL or r==0: raise ArithmeticError('dyadic obstruction certificate failed')
    return r


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--reproduce',action='store_true')
    args=ap.parse_args()
    r=check(WITNESS)
    out=dict(status='exact dyadic necessary-identity certificate',
             fields=['b2_00','b1_00','b1_01','a1_10','a2_01'],
             values=WITNESS,residual=str(r),nonzero=True,
             identity='(b2_00-b1_00)*(b1_01-b1_00)+a1_10-a2_01 = 0',
             code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    if args.reproduce:
        path=Path(__file__).with_name('native_mixed.py')
        spec=importlib.util.spec_from_file_location('native_dyadic_reproducer',path)
        mod=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        c,_=mod.compute(4,'krawtchouk','lu')
        v=[c[0,0]['b2'],c[0,0]['b1'],c[0,1]['b1'],c[1,0]['a1'],c[0,1]['a2']]
        q=list(map(Q.from_float,v))
        if q!=list(map(Q,WITNESS)):raise ArithmeticError('native five-field reproduction differs')
        check(q)
        out.update(reproduced=True,native_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__': main()
