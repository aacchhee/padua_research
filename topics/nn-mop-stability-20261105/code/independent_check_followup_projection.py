#!/usr/bin/env python3
"""Separate fits plus exact defining-moment witness/objective/gradient checks."""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform
import mpmath as mp
import backward_projection as dev
from independent_check_moments import direct, inputs, FIELDS

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
FILES=[Path(__file__),HERE/'independent_check_moments.py',HERE/'backward_projection.py',
       HERE/'native_mixed.py',HERE/'backward_joint.py',HERE/'conditioning.py',dev.native.BASE]


def hashes():
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in FILES}


def near(a,b):
    assert abs(a-b)<=1e-12*max(abs(a),abs(b),1e-100),(a,b)


def case(family,method):
    N=4
    raw,_=dev.native.compute(N,family,method)
    fit=dev.fit(raw,N,family,dps=160)
    witness=fit['rational_input']
    x=list(map(Q,witness['nodes']))
    w=[list(map(Q,row)) for row in witness['normalized_weights']]
    assert all(x[i]<x[i+1] for i in range(N-1))
    assert all(a>0 for row in w for a in row) and all(sum(row)==1 for row in w)
    c,J=direct(x,w)
    x0,w0=inputs(N,family)
    w0=[[a/sum(row) for a in row] for row in w0]
    truth,_=direct(x0,w0,False)
    scale={f:max(abs(row[f]) for row in truth.values()) for f in FIELDS}
    residual=[]
    chart=[]
    for nu in c:
        for f in FIELDS:
            residual.append((Q(raw[nu][f])-c[nu][f])/scale[f])
            g=J[nu][f]
            row=[a/scale[f] for a in g[:N]]
            for s in range(2):
                avg=sum(w[s][i]*g[(s+1)*N+i] for i in range(N))
                row.extend(w[s][i]*(g[(s+1)*N+i]-avg)/scale[f] for i in range(N-1))
            chart.append(row)
    cost=sum(a*a for a in residual)
    gradient=[sum(row[k]*a for row,a in zip(chart,residual)) for k in range(3*N-2)]
    frob2=sum(a*a for row in chart for a in row)
    stationary2=sum(a*a for a in gradient)/(cost*frob2)
    # Exact rational threshold: rounded witness remains numerically stationary.
    assert stationary2<Q(1,10**100)
    data=max(max(abs(a-b) for a,b in zip(x,x0)),
             max(abs(a-b)/b for row,old in zip(w,w0) for a,b in zip(row,old)))
    correction=max(map(abs,residual))
    near(float(data),fit['input_mixed_sup'])
    near(float(correction),fit['full_coefficient_correction'])
    with mp.workdps(180):
        spd=mp.sqrt(mp.mpf(cost.numerator)/cost.denominator)
        stationarity=mp.sqrt(mp.mpf(stationary2.numerator)/stationary2.denominator)
        near(float(spd),fit['coefficient_SPD_norm'])
        near(float(stationarity),fit['returned_witness_scaled_stationarity'])
        assert fit['returned_witness_stationarity_dps']==180
    for f in FIELDS:
        exact=max(abs(Q(raw[nu][f])-c[nu][f]) for nu in c)/scale[f]
        near(float(exact),fit['fields'][f])
    original=json.loads(Path('/tmp/backward-projection-'+family+'-r2-160.json').read_text())
    row=next(r for r in original['cases'] if r['N']==N and r['method']==method)
    assert row['rational_input']==witness
    assert row['rational_input_sha256']==fit['rational_input_sha256']
    return dict(N=N,family=family,method=method,exact_normality_systems=14,
                full_array_entries=4*len(c),positive_ordered_normalized=True,
                rational_witness_equal_to_developer=True,independent_replayed_fit=True,
                input_units_u=float(data*2**53),correction_units_u=float(correction*2**53),
                SPD_norm=float(spd),exact_stationarity_squared_below_1e_100=True,
                stationarity_float=float(stationarity),
                returned_stationarity_checked=True,
                exact_squared_SPD_hex_sha256=hashlib.sha256(
                    (hex(cost.numerator)+'/'+hex(cost.denominator)).encode()).hexdigest(),
                rational_input_sha256=fit['rational_input_sha256'])


def main():
    pinned=hashes()
    with mp.workdps(160):
        A=mp.matrix([[0,0],[1,0],[0,1],[1,1]])
        b=mp.matrix([7,1,2,3])
        z=dev.least_squares(A,b)
        assert mp.norm(z-mp.matrix([1,2]))<mp.mpf('1e-140')
        assert mp.norm(A.T*(A*z-b))<mp.mpf('1e-140')
    out=dict(python=platform.python_version(),platform=platform.platform(),
             mpmath=mp.__version__,numpy=dev.native.np.__version__,scipy=dev.native.scipy.__version__,
             source_sha256=pinned,structural_zero_QR_sanity=True,
             scope='finite exact feasible witnesses and measured numerical fits; no nearest-point certification',
             cases=[case(f,m) for f in ('krawtchouk','hahn') for m in ('lu','nodeqr')])
    assert hashes()==pinned
    print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':main()
