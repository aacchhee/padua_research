#!/usr/bin/env python3
"""Exact independent full rebuild, raw-array obstruction and flow derivative."""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform
from independent_check_moments import direct, inputs, module

HERE=Path(__file__).resolve().parent


def main():
    joint=module('independent_joint',HERE/'backward_joint.py')
    native=joint.native
    flow=module('independent_flow',HERE/'integrable_transport.py')
    paths=[Path(__file__),HERE/'independent_check_moments.py',HERE/'backward_joint.py',
           HERE/'native_mixed.py',HERE/'integrable_transport.py',native.BASE]
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    out=dict(python=platform.python_version(),mpmath=joint.mp.__version__,
             numpy=native.np.__version__,scipy=native.scipy.__version__,
             source_sha256=hashes,witnesses=[],integrable=[],native_current=[])
    for family in ('krawtchouk','hahn'):
        for N in (4,6):
            x,w=inputs(N,family)
            truth,J=direct(x,w)
            shift=Q(-2)
            wt=[[(xi-shift)*wi for xi,wi in zip(x,row)] for row in w]
            target,_=direct(x,wt,False)
            transported,_=flow.christoffel(truth,shift)
            assert transported==target
            direction=[Q(0)]*N+[xi*wi for row in w for xi,wi in zip(x,row)]
            rhs=flow.toda_rhs(truth)
            for nu in truth:
                for f in truth[nu]:
                    assert sum(a*b for a,b in zip(J[nu][f],direction))==rhs[nu][f]
            out['integrable'].append(dict(N=N,family=family,fields=4*len(truth),
                 christoffel_exact_equal=True,toda_exact_derivative_equal=True))
        for N in (4,8,12,16):
            x,w=inputs(N,family)
            truth,_=direct(x,w,False)
            for method in ('lu','qr','svd','nodeqr'):
                co,_=native.compute(N,family,method)
                correction=max(max(abs(Q(co[nu][f])-r[f]) for nu,r in truth.items())/
                    max(abs(r[f]) for r in truth.values()) for f in ('a1','a2','b1','b2'))
                out['native_current'].append(dict(N=N,family=family,method=method,E=float(correction)))
            if N!=4:
                continue
            for method in ('lu','nodeqr'):
                co,_=native.compute(N,family,method)
                measured=joint.witness(co,N,family,180,True)
                rep=measured['witness_input']
                xp=list(map(Q,rep['nodes']))
                wp=[list(map(Q,r)) for r in rep['normalized_weights']]
                assert all(a>0 for row in wp for a in row)
                assert all(sum(row)==1 for row in wp)
                assert all(a<b for a,b in zip(xp,xp[1:]))
                rebuilt,_=direct(xp,wp,False)
                correction=max(max(abs(Q(co[nu][f])-r[f]) for nu,r in rebuilt.items())/
                    max(abs(r[f]) for r in truth.values()) for f in ('a1','a2','b1','b2'))
                wn=[[a/sum(r) for a in r] for r in w]
                distance=max(max(abs(a-b) for a,b in zip(xp,x)),
                    max(abs(a-b)/b for row,t in zip(wp,wn) for a,b in zip(row,t)))
                assert abs(float(correction)-measured['full_coefficient_correction']) <= 1e-12*float(correction)
                assert abs(float(distance)-measured['data_mixed_sup']) <= 1e-12*float(distance)
                out['witnesses'].append(dict(N=N,family=family,method=method,
                    exact_full_rebuild=True,coefficient_correction=float(correction),
                    mixed_input_distance=float(distance),input_sha256=measured['witness_input_sha256']))
    co,_=native.compute(4,'krawtchouk','lu')
    b20,b10,b101,a110,a201=[Q(v) for v in (co[0,0]['b2'],co[0,0]['b1'],co[0,1]['b1'],co[1,0]['a1'],co[0,1]['a2'])]
    residual=(b20-b10)*(b101-b10)+a110-a201
    assert residual==Q(25700541873527631,649037107316853453566312041152512)
    out['independent_raw_compatibility_residual']=str(residual)
    assert hashes=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':
    main()
