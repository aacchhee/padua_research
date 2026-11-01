"""Exact B3 four-atom moment identities and all-parameter polynomial signs.

No numerical eigenvalue/sign decision. The written theorem supplies the
spectral-gap, inertia and reference interpretation of these exact checks.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import time
import sympy as sp

HERE = Path(__file__).resolve()
SOURCE_AT_IMPORT = hashlib.sha256(HERE.read_bytes()).hexdigest()
t = sp.Symbol('t', real=True)
x, y = sp.symbols('x y', real=True)
T = sp.Rational(1, 10**6)
NODES = [(0, 0), (sp.Rational(1, 2), sp.Rational(1, 2)),
         (-sp.Rational(1, 2), sp.Rational(1, 2)), (0, -sp.Rational(1, 2))]
WEIGHTS = [(1-t)/3, (1-t)/3, (1-t)/3, t]

def rat(a):
    return str(sp.factor(a))

def expect_zero(matrix):
    return all(sp.cancel(c) == 0 for c in matrix)

def expectation(poly):
    return sp.factor(sum(w*poly.subs({x: a, y: b}) for (a,b),w in zip(NODES,WEIGHTS)))

def polynomial_bound(poly):
    """Exact constant +/- absolute coefficient tail on [0,T]."""
    p = sp.Poly(poly, t, domain=sp.QQ)
    a = p.nth(0)
    tail = sum(abs(p.nth(j))*T**j for j in range(1, p.degree()+1))
    return {'coefficients_ascending': [rat(p.nth(j)) for j in range(p.degree()+1)],
            'constant': rat(a), 'absolute_tail': rat(tail),
            'lower': rat(a-tail), 'upper': rat(a+tail)}, a-tail, a+tail

def rational_sign_certificate(expr, desired, remove_t_power=0):
    reduced = sp.cancel(expr / t**remove_t_power)
    numerator, denominator = sp.fraction(reduced)
    den0 = denominator.subs(t,0)
    assert den0 != 0
    if den0 < 0:
        numerator, denominator = -numerator, -denominator
    nc,nl,nu = polynomial_bound(numerator)
    dc,dl,du = polynomial_bound(denominator)
    assert dl > 0
    assert (nu < 0) if desired == -1 else (nl > 0)
    return {'expression': rat(expr), 'removed_positive_t_power': remove_t_power,
            'numerator': nc, 'denominator': dc, 'sign': desired,
            'certified_for_every_t': f'0 < t <= {T}'}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--expect-source-sha256',required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    assert a.expect_source_sha256 == SOURCE_AT_IMPORT
    started=time.monotonic()
    m=(2-5*t)/6
    v=(1-t)*(25*t+2)/36
    r2=(1-t)/6
    q=(1+5*t)/6
    d=m*(1-25*t)/(25*t+2)
    basis=[sp.Integer(1),y-m,x]
    G=sp.Matrix(3,3,lambda i,j:expectation(basis[i]*basis[j]))
    Gx=sp.Matrix(3,3,lambda i,j:expectation(x*basis[i]*basis[j]))
    Gy=sp.Matrix(3,3,lambda i,j:expectation(y*basis[i]*basis[j]))
    Tx=sp.Matrix([[0,0,r2],[0,0,(1+5*t)/(25*t+2)],[1,q,0]])
    Ty=sp.Matrix([[m,v,0],[1,d,0],[0,0,sp.Rational(1,2)]])
    assert expect_zero(G-sp.diag(1,v,r2))
    assert expect_zero(G*Tx-Gx) and expect_zero(G*Ty-Gy)
    assert expect_zero(G*Tx-Tx.T*G) and expect_zero(G*Ty-Ty.T*G)
    assert sp.factor(sum(WEIGHTS)) == 1
    # Fixed first three nodes determine Pi_1, independent of t.
    V=sp.Matrix([[1,b,a0]for a0,b in NODES[:3]])
    determining=sp.factor(V.det());assert determining != 0
    K=(Tx*Ty-Ty*Tx).applyfunc(sp.factor)
    assert all(K[i,j]==0 for i in range(3)for j in range(3)if i==0 or j==0 or i==j)
    delta2=sp.factor(-sp.trace(K*K)/2)
    expected_delta2=27*t*t/(2*(25*t+2)**3)
    assert sp.cancel(delta2-expected_delta2)==0
    h2=t/10
    Mx=h2*sp.eye(3)-Tx*Tx
    My=h2*sp.eye(3)-Ty*Ty
    S=((Mx*My+My*Mx)/2).applyfunc(sp.factor)
    detS=sp.factor(S.det());traceS=sp.factor(sp.trace(S))
    det_cert=rational_sign_certificate(detS,-1,2)
    trace_cert=rational_sign_certificate(traceS,1)
    leading=sp.factor(sp.limit(detS/t**2,t,0))
    assert leading == -sp.Rational(217,204800)
    # Ancillary rational inequalities used by the handwritten spectral proof.
    A2=sp.factor(r2+(1+5*t)**2/(6*(25*t+2)))
    assert sp.cancel(A2-(1+11*t)/(2*(25*t+2)))==0
    ytrace=sp.factor(m+d);ydet=sp.factor(m*d-v)
    assert sp.cancel(ytrace-(2-5*t)/(2*(25*t+2)))==0
    assert sp.cancel(ydet+6*t/(25*t+2))==0
    auxiliary={
      'r2_minus_p2':rational_sign_certificate(r2-sp.Rational(1,100),1),
      'v_minus_p2':rational_sign_certificate(v-sp.Rational(1,100),1),
      'Hx_nonzero_eigenvalue_squared_above_one_fifth':rational_sign_certificate(A2-sp.Rational(1,5),1),
      'Hy_block_trace_above_two_fifths':rational_sign_certificate(ytrace-sp.Rational(2,5),1),
      'delta_squared_below_4t_squared':rational_sign_certificate(4-delta2/t**2,1),
    }
    # 8t <= h/2 and 10t <= h/4; exact squared inequalities.
    assert 256*T <= sp.Rational(1,10)
    assert 1600*T <= sp.Rational(1,10)
    source_after=hashlib.sha256(HERE.read_bytes()).hexdigest()
    assert source_after == SOURCE_AT_IMPORT
    proof={'degree':1,'dimension':3,'support_size':4,'parameter_upper':rat(T),
           'nodes':[[rat(a0),rat(b)]for a0,b in NODES],
           'weights':list(map(rat,WEIGHTS)), 'basis':list(map(rat,basis)),
           'gram_diagonal':list(map(rat,[1,v,r2])),
           'Tx':[[rat(c)for c in row]for row in Tx.tolist()],
           'Ty':[[rat(c)for c in row]for row in Ty.tolist()],
           'positive_measure_moment_section_identities':True,
           'determining_minor':rat(determining),'weighted_selfadjoint_identities':True,
           'commutator':[[rat(c)for c in row]for row in K.tolist()],
           'delta_squared':rat(delta2),
           'box_halfwidth_squared':rat(h2),
           'det_S_leading_coefficient':rat(leading),
           'det_S_negative':det_cert,'trace_S_positive':trace_cert,
           'Hx_nonzero_eigenvalue_squared':rat(A2),
           'Hy_block_trace':rat(ytrace),'Hy_block_determinant':rat(ydet),
           'auxiliary_sign_certificates':auxiliary,
           'squared_gap_and_reference_inequalities':True}
    canonical=json.dumps(proof,sort_keys=True,separators=(',',':')).encode()
    result={'format':'b3-four-atom-exact-v1','scope':'exact moment identities and rational polynomial signs on the entire stated interval; theorem interpretation is written separately',
            'proof':proof,'proof_payload_sha256':hashlib.sha256(canonical).hexdigest(),
            'metadata':{'python':platform.python_version(),'sympy':sp.__version__,
                        'arithmetic':'exact rational symbolic polynomial identities and coefficient bounds; no float signs',
                        'source_sha256_before':SOURCE_AT_IMPORT,'source_sha256_after':source_after,
                        'source_unchanged':True,'seconds':time.monotonic()-started}}
    out=Path(a.output);assert not out.exists(),'refuse existing output'
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'output':str(out),'bytes':out.stat().st_size,
                      'proof_payload_sha256':result['proof_payload_sha256'],
                      'exact_checks_passed':True,'seconds':result['metadata']['seconds']}))

if __name__=='__main__':
    main()
