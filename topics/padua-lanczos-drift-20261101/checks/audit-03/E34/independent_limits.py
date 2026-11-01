#!/usr/bin/env python3
"""Audit-03 exact E34 reconstruction; imports no campaign or prior-audit code.

Finite corroboration of the analytic proof, not a universal computer proof.
Weighted node coordinates avoid square roots; all matrix tests are exact.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
import sympy as s


def cols(vs):
    return s.Matrix.hstack(*vs)


def case(name, pts, weights, t, selection, source):
    n = len(pts)
    W = s.diag(*weights)
    I = s.eye(n)
    dot = lambda a, b: (a.T * W * b)[0]
    proj = lambda B: B * (B.T * W * B).inv() * B.T * W
    mons = [s.Matrix([x**(d-j)*y**j for x, y in pts])
            for d in range(t+2) for j in range(d+1)]
    nt = (t+1)*(t+2)//2
    S = cols(mons)
    assert S.rank() == S.cols < n
    P = proj(S)
    prefix = []
    for a in mons[:nt]:
        for q in prefix:
            a = a - q*dot(q, a)/dot(q, q)
        prefix.append(a)
    Pt = proj(cols(prefix))
    ops = [s.diag(*[p[j] for p in pts]) for j in (0, 1)]
    base = t*(t+1)//2
    parents = [prefix[base+j-a] for j, a in enumerate(selection)]
    raw = [ops[a]*p for a, p in zip(selection, parents)]
    V = cols(prefix+[r for j, r in enumerate(raw) if j != source])
    Pv = proj(V)
    w = (I-Pv)*raw[source]
    w2 = dot(w, w)
    par2 = dot(parents[source], parents[source])
    v2 = dot(raw[source], raw[source])/par2
    b2 = w2/par2
    kappas = [s.factor(dot(Pt*A*w, Pt*A*w)/w2) for A in ops]
    assert b2 > 0 and kappas[selection[source]] >= b2
    normals = [(I-P)*I[:, j] for j in range(n)]
    normals = [r for r in normals if r != s.zeros(n, 1)]
    r = normals[0]
    if len(normals) > 1 and 2*r-3*normals[1] != s.zeros(n, 1):
        r = 2*r-3*normals[1]
    assert S.T*W*r == s.zeros(S.cols, 1)
    r2 = dot(r, r)
    tested = []
    for eta, alpha in [(s.Rational(-2), 0), (s.Rational(-1, 10), 0),
                       (s.Rational(1, 7), 0), (s.Rational(1, 10**8), 0),
                       (s.Rational(1, 7), -1), (s.Rational(1, 7), s.Rational(-3, 2))]:
        f = eta*r+alpha*w
        # Non-normal cases include a component along all other raw columns.
        if alpha:
            f += sum((s.Rational(j+1, 3)*raw[j] for j in range(t+2)
                      if j != source), prefix[0])
        changed = list(raw)
        changed[source] += f
        C = cols(prefix+changed)
        assert C.rank() == C.cols
        Ph = proj(C)
        theta2 = eta**2*r2/((1+alpha)**2*w2+eta**2*r2)
        D = Ph-P
        assert (D**4-theta2*D**2) == s.zeros(n)
        assert s.trace(D**2) == 2*theta2
        deltas = []
        for A, kap2 in zip(ops, kappas):
            B = (I-Ph)*A*Pt
            G = W.inv()*B.T*W*B
            val = s.factor(s.trace(G))
            assert G*G == val*G  # weighted self-adjoint positive Gram: rank <= 1
            assert val == kap2*theta2
            if alpha == 0:
                u2 = eta**2*r2/(v2*par2)
                assert s.factor(val/u2-kap2*v2/(b2+u2*v2)) == 0
            deltas.append(str(val))
        projected = P*C
        assert projected.rank() == S.cols-(alpha == -1)
        tested.append({'eta': str(eta), 'alpha': str(alpha), 'delta_sq': deltas,
                       'source_projected_rank': projected.rank()})
    return {'name': name, 't': t, 'selection': ''.join('XY'[a] for a in selection),
            'source': source, 'v2': str(v2), 'b2': str(b2),
            'kappa2': [str(x) for x in kappas],
            'limit_sq': [str(s.factor(x*v2/b2)) for x in kappas], 'tests': tested}


def repair_checks():
    e = [s.eye(5)[:, j] for j in range(5)]
    exact_prefix = cols(e[:2])
    P = exact_prefix*exact_prefix.T
    q0 = e[0]
    for sign in (-1, 1):
        q = (e[0]+sign*3*e[1]+2*e[3])/s.sqrt(14)
        a = q-q0*(q0.T*q)[0]
        b = P*q
        assert a != s.zeros(5, 1) and b != s.zeros(5, 1)
        assert (e[1].T*b)[0] != 0
        assert (e[1].T*q)[0]**2 >= s.Rational(1, 4)
        assert (e[3].T*b)[0] == 0 and (e[3].T*a)[0] != 0
    assert (s.eye(5)-q0*q0.T)*q0 == s.zeros(5, 1)  # dependent parent rejected
    q = (e[0]+e[3])/s.sqrt(2)
    assert P*q != s.zeros(5, 1) and (e[1].T*q)[0] == 0  # gamma gate necessary
    for p in range(3):
        before = cols(e[:p]) if p else s.zeros(5, 0)
        through = cols(e[:p+1])
        assert (s.eye(5)-before*before.T)*e[p] == e[p]
        assert through*through.T*e[p] == e[p]
    # A nonzero repair can stay wholly within the stored span. Use rational
    # orthonormal columns and gamma=3/5>1/2; r_j are exact reference columns.
    q1 = s.Rational(3, 5)*e[1]+s.Rational(4, 5)*e[2]
    q2 = s.Rational(4, 5)*e[1]-s.Rational(3, 5)*e[2]
    Q = cols([q0, q1, q2])
    assert Q.T*Q == s.eye(3)
    discarded = -(s.eye(5)-P)*q1
    repaired = P*q1/s.sqrt((q1.T*P*q1)[0])
    assert discarded != s.zeros(5, 1) and repaired != q1
    assert Q*Q.T*discarded == discarded
    assert Q*Q.T*repaired == repaired
    assert Q*Q.T*(repaired-q1) == repaired-q1
    return {'exact_parent_identity': True, 'positive_and_negative_gamma': True,
            'gamma_zero_projection_nonzero': True, 'dependent_parent_zero': True,
            'outside_stored_span_assertion_counterexample': {
                'ambient': 'orthonormal exact reference r0,r1,r2,r3,r4',
                'p': 1, 'stored': ['r0', '(3r1+4r2)/5', '(4r1-3r2)/5'],
                'gamma': '3/5', 'discarded': '-4r2/5', 'repaired': 'r1',
                'nonzero_change': True, 'correction_and_repaired_parent_in_stored_span': True,
                'no_claim_of_realization_by_specific_IEEE_run': True}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    start = time.time()
    T3 = [(x, y) for x in range(4) for y in range(4-x)]
    T4 = [(x, y) for x in range(5) for y in range(5-x)]
    points4 = [(0, 0), (1, 0), (0, 1), (1, 1)]
    rows = [case('minimal_nonuniform_t0_'+str(m), points4,
                 [s.Rational(i, 10) for i in range(1, 5)], 0, [0, 1], m) for m in range(2)]
    rows += [case('T3_'+''.join('XY'[a] for a in sel)+'_'+str(m), T3,
                  [s.Rational(1, 10)]*10, 1, sel, m)
             for sel in ([0, 1, 1], [0, 0, 1]) for m in range(3)]
    rows.append(case('T4_XYXY_1', T4, [s.Rational(1, 15)]*15, 2, [0, 1, 0, 1], 1))
    byname = {r['name']: r for r in rows}
    assert byname['T3_XYY_0']['limit_sq'] == ['88/15', '0']
    assert byname['T3_XYY_1']['limit_sq'] == ['2', '3/2']
    assert s.Rational(byname['T4_XYXY_1']['kappa2'][1])/s.Rational(byname['T4_XYXY_1']['b2']) == s.Rational(7, 4)
    out = {'purpose': __doc__, 'command': 'PYTHONPATH=/workspace/padua-drift-runs/python-deps '
           'OPENBLAS_NUM_THREADS=1 python3 -B '+str(Path(__file__))+' --output '+args.output,
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'python': sys.version.split()[0], 'sympy': s.__version__, 'platform': platform.platform(),
           'cases': rows, 'repairs': repair_checks(), 'all_assertions_passed': True,
           'elapsed_seconds': round(time.time()-start, 3)}
    Path(args.output).write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'PASS': True, 'cases': len(rows), 'source_settings': sum(len(r['tests']) for r in rows),
                      'elapsed_seconds': out['elapsed_seconds']}))


if __name__ == '__main__':
    main()
