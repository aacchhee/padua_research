#!/usr/bin/env python3
"""Independent finite regression, stored-witness assembly and rejection controls.
Does not establish universal spectral bounds or replace the Claude audit.
"""
import hashlib, importlib.util, json, platform, sys
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[3]
TOP=ROOT/'topics/padua-mz-2d-20261101'
spec=importlib.util.spec_from_file_location('producer',ROOT/'tracks/mz-constants/code/mz2d_exact.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def integral(k):return F(0) if k&1 else F(2,1-k*k)
def own_moment(m,r,s):
    # Repeated reflections are nodal cosine identities; simultaneous complement
    # on the even checkerboard moves to the total-degree interpolation triangle.
    while r>m:r=abs(2*m-r)
    while s>m+1:s=abs(2*(m+1)-s)
    if r+s>m:r,s=m-r,m+1-s
    return integral(r)*integral(s)

def nodal_check(m):
    order=2*m*(m+1);z=sp.Symbol('z')
    K=sp.QQ.alg_field_from_poly(sp.Poly(sp.cyclotomic_poly(order,z),z),'zeta')
    root=K([1,0]);powers=[root**j for j in range(order)];half=K.convert(sp.Rational(1,2))
    def cosine(j):return half*(powers[j%order]+powers[-j%order])
    def val(j,k,a,b):return cosine(a*j*(m+1))*cosine(b*k*m)
    nodes=[(j,k) for j in range(m+1) for k in range(m+2) if not (j+k)%2]
    modes=[(a,d-a) for d in range(m+1) for a in range(d,-1,-1)];N=len(nodes)
    V=DomainMatrix([[val(j,k,a,b) for a,b in modes] for j,k in nodes],(N,N),K)
    inv=V.inv().to_list()
    moments=[K.convert(sp.Rational(integral(a)*integral(b))) for a,b in modes]
    weights=[sum((moments[t]*inv[t][q] for t in range(N)),K.zero) for q in range(N)]
    count=0
    # Includes modes beyond endpoint Gram range to exercise complementary aliases.
    for d in range(2*m+3):
        for a in range(d+1):
            b=d-a;actual=sum((weights[q]*val(j,k,a,b) for q,(j,k) in enumerate(nodes)),K.zero)
            expected=own_moment(m,a,b)
            assert actual==K.convert(sp.Rational(expected)),(m,a,b)
            assert expected==p.moment(m,a,b)
            count+=1
    basis,H,Q,_=p.pencil(m)
    entries=0
    values={(a,b):[val(j,k,a,b) for j,k in nodes] for a,b in basis}
    for i,(a,b) in enumerate(basis):
        for t,(c,d) in enumerate(basis):
            actual=sum((weights[q]*values[a,b][q]*values[c,d][q] for q in range(N)),K.zero)
            assert actual==K.convert(sp.Rational(Q[i][t]))
            # Direct polynomial integration independently checks the continuous form.
            x=sp.Symbol('x')
            hx=sp.integrate(sp.chebyshevt(a,x)*sp.chebyshevt(c,x),(x,-1,1))
            hy=sp.integrate(sp.chebyshevt(b,x)*sp.chebyshevt(d,x),(x,-1,1))
            assert sp.Rational(H[i][t])==hx*hy
            entries+=1
    return {'m':m,'nodes':N,'cyclotomic_order':order,'field_degree':int(sp.totient(order)),'exact_nodal_moment_checks':count,'direct_nodal_Gram_and_polynomial_integral_pairs':entries}

def region_checks():
    counts={key:0 for key in ['L','C','X0','X1','Y0','Y1']}
    total=0
    for m in range(2,13):
        for a in range(2*m-1):
            for b in range(2*m-1-a):
                if a<=m and b<=m+1:
                    key='L' if a+b<=m else 'C'
                    value=integral(a)*integral(b) if key=='L' else integral(m-a)*integral(m+1-b)
                elif a>m:
                    key='X0' if a-b>=m else 'X1'
                    value=integral(2*m-a)*integral(b) if key=='X0' else integral(a-m)*integral(m+1-b)
                else:
                    key='Y0' if b-a>=m+2 else 'Y1'
                    value=integral(a)*integral(2*m+2-b) if key=='Y0' else integral(m-a)*integral(b-m-1)
                assert value==p.moment(m,a,b)==own_moment(m,a,b),(m,a,b,key)
                counts[key]+=1;total+=1
    assert all(counts.values())
    return {'m_range':[2,12],'all_a_plus_b_at_most_2m_minus_2':True,'moment_checks':total,'region_counts':counts}

def stored_witness(data):
    row=next(x for x in data['results'] if x['m']==30);w=row['witness'];v=w['coefficients'];m=30
    assert len(v)==225 and len({(a,b) for a,b,c in v})==225
    assert all(a>=0 and b>=0 and a+b<=29 and isinstance(c,int) and c for a,b,c in v)
    qa=F(0);hb=F(0)
    for a,b,c in v:
        for d,e,f in v:
            products=[(a+d,b+e),(a+d,abs(b-e)),(abs(a-d),b+e),(abs(a-d),abs(b-e))]
            qa+=c*f*sum((own_moment(m,r,s) for r,s in products),F(0))/4
            hb+=c*f*sum((integral(r)*integral(s) for r,s in products),F(0))/4
    assert qa==F(w['Q_p_squared']) and hb==F(w['integral_p_squared'])
    assert qa/hb==F(w['rayleigh_quotient']) and hb-4*qa==F(w['strict_b_minus_4a'])>0 and hb>0
    # Corrupt only the advertised coefficient list: the same checker must reject
    # the now-inconsistent stored exact forms, rather than trusting their strings.
    bad=json.loads(json.dumps(data));next(x for x in bad['results'] if x['m']==30)['witness']['coefficients'][0][2]+=1
    return {'nonzero_coefficients':len(v),'Q_p_squared':str(qa),'integral_p_squared':str(hb),'strict_b_minus_4a':str(hb-4*qa),'rayleigh_quotient':str(qa/hb)},bad

def rejection_controls(data,bad):
    basis,H,Q,blocks=p.pencil(2);good=[p.fmpz_mat([[int(i==j) for j in range(len(b))] for i in range(len(b))]) for b in blocks]
    controls=[]
    def reject(name,fn):
        try:fn()
        except (AssertionError,ZeroDivisionError):controls.append({'name':name,'rejected':True});return
        raise AssertionError('control unexpectedly accepted: '+name)
    reject('zero congruence',lambda:p.inertia(H,Q,blocks,F(0),[p.fmpz_mat(len(b),len(b)) for b in blocks]))
    singular=[p.fmpz_mat([[int(i==j and i!=0) for j in range(len(b))] for i in range(len(b))]) for b in blocks]
    reject('singular congruence',lambda:p.inertia(H,Q,blocks,F(0),singular))
    reject('singular exact endpoint t=1 at m2',lambda:p.inertia(H,Q,blocks,F(1),good))
    reject('zero enclosure width',lambda:p.run(2,F(0)))
    reject('negative enclosure width',lambda:p.run(2,F(-1,1000000)))
    reject('corrupted stored coefficient',lambda:stored_witness(bad))
    return controls

def normalize(x):
    if isinstance(x,dict):return {k:normalize(v) for k,v in x.items() if k!='seconds'}
    if isinstance(x,list):return [normalize(v) for v in x]
    return x

def main():
    source=TOP/'evidence/exact-spectra.json';rerun=TOP/'evidence/independent-exact-spectra.json'
    data=json.loads(source.read_text());other=json.loads(rerun.read_text())
    assert normalize(data['results'])==normalize(other['results'])
    witness,bad=stored_witness(data)
    out={'command':sys.argv,'python':sys.version,'platform':platform.platform(),'sympy':sp.__version__,'python_flint':p.flint.__version__,'script_sha256':digest(Path(__file__)),'producer_sha256':digest(ROOT/'tracks/mz-constants/code/mz2d_exact.py'),'source_receipt_sha256':digest(source),'independent_receipt_sha256':digest(rerun),'definitions_sha256':digest(TOP/'definitions.md'),'results_match_after_removing_only_seconds':True,'five_inexact_region_regression':region_checks(),'nodal_regressions':[nodal_check(m) for m in range(1,6)],'stored_m30_witness':witness,'rejection_controls':rejection_controls(data,bad),'scope':'Technical execution and finite exact regressions supplement mathematical audit; required Claude audit remains pending.'}
    target=TOP/'evidence/independent-additional-checks.json';target.write_text(json.dumps(out,indent=2)+'\n');print('PASS',target)
if __name__=='__main__':main()
