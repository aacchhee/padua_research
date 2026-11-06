#!/usr/bin/env python3
"""M2 reconstruction vs pinned exact-generator H, independently of solver errors."""
import argparse,hashlib,json
from pathlib import Path
import mpmath as mp
from c4_normalization import ROOT,load,monic_hessenberg,affine_monic
from c4_compare import bitmatrix,distance


def main():
    p=argparse.ArgumentParser();p.add_argument('--external',type=Path,required=True);p.add_argument('--receipt',type=Path,required=True);a=p.parse_args()
    bp=ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
    gp=ROOT/'topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py'
    b,g=load('fid_base',bp),load('fid_truth',gp)
    cases=[]
    with mp.workdps(220):
        for r in json.loads(a.external.read_text()):
            if r['input_kind']!='archive_integer' or r['N']!=6:continue
            x,w=b.inputs(6,r['family']);_,c=g.ground_truth(x,w)
            H=monic_hessenberg(c,6)
            H=[[mp.mpf(v.numerator)/v.denominator for v in row] for row in H]
            H=affine_monic(H,mp.mpf(5)/2,mp.mpf(5)/2)
            referr=distance(H,bitmatrix(r['exact_bits'],6))
            cases.append(dict(family=r['family'],topic_N=6,paper_N=5,reference_relative=referr,
                solver_relative={k:distance(H,bitmatrix(v['H_bits'],6)) for k,v in r['algorithms'].items() if v['status']=='ok'},
                passed=referr<=1e-12))
    if not cases:raise ValueError('missing selected fidelity configuration')
    out=dict(M2='PASS' if all(r['passed'] for r in cases) else 'FAIL',
        fidelity_rule='relative spectral error against pinned exact-generator output <=1e-12; solver errors reported separately',
        cases=cases,files={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (a.external,Path(__file__),bp,gp)})
    a.receipt.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    if out['M2']!='PASS':raise ValueError('normalization fidelity mismatch')


if __name__=='__main__':main()
