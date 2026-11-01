#!/usr/bin/env python3
"""Independent E34 re-audit: exact SymPy projector computations.

No developer/audit-01 imports. Uses weighted node-value coordinates (isometric
to sqrt(weight)-scaled Euclidean coordinates) and unnormalized orthogonal
prefixes, with unit-parent scaling accounted for explicitly.
"""
import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path
import sys
import sympy as s


def columns(vs):
    return s.Matrix.hstack(*vs)


def evaluate(points, degree):
    return [s.Matrix([x ** (d-j) * y ** j for x,y in points])
            for d in range(degree+1) for j in range(d+1)]


def check_case(name, points, weights, t, selection, m, alpha, normal_scale, full_orders=False):
    W = s.diag(*weights)
    M = len(points)
    I = s.eye(M)
    def dot(x,y):
        return (x.T*W*y)[0]
    def projector(B):
        return B*(B.T*W*B).inv()*B.T*W
    def orthogonal(vs):
        out=[]
        for v in vs:
            for q in out:
                v=v-q*dot(q,v)/dot(q,q)
            assert dot(v,v)>0
            out.append(v)
        return out
    def adj(B):
        return W.inv()*B.T*W
    mons=evaluate(points,t+1)
    S=columns(mons)
    assert S.rank()==S.cols and M>S.cols
    pref=orthogonal(evaluate(points,t))
    B=columns(pref)
    Pt=projector(B)
    P=projector(S)
    X=s.diag(*[x for x,y in points]); Y=s.diag(*[y for x,y in points])
    As={'X':X,'Y':Y}
    base=t*(t+1)//2
    parents=[pref[base+j-(a=='Y')] for j,a in enumerate(selection)]
    raw=[As[a]*q for a,q in zip(selection,parents)]
    V=columns(pref+[v for j,v in enumerate(raw) if j!=m])
    PV=projector(V)
    w=(I-PV)*raw[m]
    b2=dot(w,w)
    parent2=dot(parents[m],parents[m])
    unit_b2=b2/parent2
    normal=None
    for mon in reversed(evaluate(points,t+2)):
        r=(I-P)*mon
        if r!=s.zeros(M,1): normal=r;break
    assert normal is not None
    # Deliberately include all other degree-(t+1) columns, including columns
    # processed later, in f_parallel. This tests the problematic quantifier.
    vpart=B[:,0]+sum((s.Rational(j+2,3)*v for j,v in enumerate(raw) if j!=m),s.zeros(M,1))
    f=alpha*w+normal_scale*normal+vpart
    fp=(I-P)*f
    assert s.simplify(dot(f,w)/b2)==alpha
    g=(1+alpha)*w+fp
    predicted=projector(columns([*pref,*[v for j,v in enumerate(raw) if j!=m],g]))
    changed=list(raw);changed[m]=raw[m]+f
    orders=list(itertools.permutations(range(t+2))) if full_orders else [tuple(range(t+1,-1,-1))]
    tested=0
    for order in orders:
        for mode in ['none','two_pass','arbitrary']:
            stored=list(pref)
            for pos,j in enumerate(order):
                v=changed[j]
                passes=0 if mode=='none' else 2
                for run in range(passes):
                    for k,q in enumerate(stored):
                        c=dot(q,v)/dot(q,q) if mode=='two_pass' else s.Rational((-1)**(k+run)*(k+2),pos+run+3)
                        v=v-c*q
                assert v!=s.zeros(M,1)
                stored.append(s.Rational((-1)**pos*(pos+2),pos+1)*v)
            C=columns(stored)
            assert C.rank()==S.cols
            assert projector(C)==predicted
            tested+=1
    D=predicted-P
    lam=s.factor(s.trace(D*D)/2)
    assert (D**4-lam*D**2)==s.zeros(M)
    expected=s.factor(dot(fp,fp)/((1+alpha)**2*b2+dot(fp,fp)))
    assert lam==expected
    result={}
    for nm,A in As.items():
        defect=(I-predicted)*A*Pt
        G=adj(defect)*defect
        delta2=s.factor(s.trace(G))
        assert G.rank()<=1
        kappa2=s.factor(dot(Pt*A*w,Pt*A*w)/b2)
        assert delta2==kappa2*lam
        assert (kappa2==0)==(columns([*pref,*[v for j,v in enumerate(raw) if j!=m],*[A*q for q in pref]]).rank()==V.cols)
        result[nm]={'kappa2':str(kappa2),'delta2':str(delta2),'kappa2_over_unit_b2':str(kappa2/unit_b2)}
    assert s.Rational(result[selection[m]]['kappa2'])>=unit_b2
    return {'name':name,'rules':tested,'theta2':str(lam),'unit_b2':str(unit_b2),'alpha':str(alpha),
            'parent_norm2':str(parent2),'v_norm2_unit_parent':str(dot(raw[m],raw[m])/parent2),
            'normal_norm2':str(dot(normal,normal)),'operators':result}, (W,B,Pt,P,raw,V,PV,w,normal)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    T3=[(s.Integer(i),s.Integer(j)) for j in range(4) for i in range(4-j)]
    out=[]
    for m in range(3):
        for alpha in [s.Integer(0),s.Integer(-1),s.Rational(-3,2)]:
            rec,_=check_case(f'T3_BJ_m{m}_alpha{alpha}',T3,[s.Rational(1,10)]*10,1,'XYY',m,alpha,s.Rational(2,7),True)
            out.append(rec)
    # Non-product, nonuniform degree 0 and non-staircase degree 2 tests.
    P0=[(s.Integer(0),s.Integer(0)),(s.Integer(1),s.Integer(0)),(s.Integer(0),s.Integer(2)),(s.Integer(3),s.Integer(1))]
    for m in range(2):
        rec,_=check_case(f'nonuniform_t0_m{m}',P0,[s.Rational(i,10) for i in range(1,5)],0,'XY',m,s.Integer(-1),s.Rational(3,5),True)
        out.append(rec)
    T4=[(s.Integer(i),s.Integer(j)) for j in range(5) for i in range(5-j)]
    for m in range(4):
        rec,_=check_case(f'T4_t2_XYXY_m{m}',T4,[s.Rational(1,15)]*15,2,'XYXY',m,s.Rational(1,3),s.Rational(-1,5))
        out.append(rec)
    # Exact symbolic direct-projector counterexample to the erroneous limit.
    rec,(W,B,Pt,P,raw,V,PV,w,r)=check_case('limit_counterexample',T3,[s.Rational(1,10)]*10,1,'XYY',0,s.Integer(0),s.Integer(1))
    eta=s.symbols('eta',real=True)
    C=columns([*list(B.columnspace()),raw[0]+eta*r,raw[1],raw[2]])
    Ph=s.simplify(C*(C.T*W*C).inv()*C.T*W)
    X=s.diag(*[x for x,y in T3]);D=s.simplify((s.eye(10)-Ph)*X*Pt)
    delta2=s.factor(s.trace(W.inv()*D.T*W*D))
    v2=(raw[0].T*W*raw[0])[0];r2=(r.T*W*r)[0]
    unit_source_limit2=s.simplify(s.limit(delta2/eta**2,eta,0)*v2/r2)
    assert unit_source_limit2!=v2
    assert unit_source_limit2/v2==s.Rational(4,3)
    m1=next(x for x in out if x['name']=='T3_BJ_m1_alpha0')
    assert s.Rational(m1['unit_b2'])==s.Rational(28,115)
    assert s.Rational(m1['normal_norm2'])==s.Rational(72,175)
    assert s.Rational(m1['operators']['Y']['delta2'])/s.Rational(m1['operators']['X']['delta2'])==s.Rational(3,4)
    # U(3) checked independently by exact monomial matrix rank; proof is analytic.
    rank3=columns(evaluate(T3,3)).rank();assert rank3==10
    result={'purpose':'Independent exact finite corroboration; no campaign code imports; analytic audit proves universal claim',
            'command':'python3 -B '+str(Path(__file__))+' --output '+args.output,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'python':sys.version.split()[0],'sympy':s.__version__,'platform':platform.platform(),
            'all_assertions_passed':True,'T3_U3_rank':rank3,'cases':out,
            'counterexample':{'measure':'uniform T3','t':1,'selection':'XYY','source_product':'v20=X[x-1]',
                'source':'eta times normal part of y^3; then eta = u sqrt(v20_norm2/r_norm2)',
                'v20_norm2':str(v2),'b2':rec['unit_b2'],'kappaX2':rec['operators']['X']['kappa2'],
                'direct_deltaX2_as_function_of_eta':str(delta2),'limit_deltaX2_over_u2':str(unit_source_limit2),
                'false_claim_squared_value':str(v2),'actual_limit_squared_over_claimed':str(unit_source_limit2/v2)}}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_assertions_passed':True,'cases':len(out),'rules':sum(x['rules'] for x in out),
                      'counterexample':result['counterexample']},indent=2))


if __name__=='__main__':main()
