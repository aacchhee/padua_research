"""Independent supplementary audit; pinned source 614709d4a60fb0c2593b05764e8d5aceda1be381.

Run from repository root: OPENBLAS_NUM_THREADS=1 python topics/programme-ideas-20261031/audit-support/rejections-check.py
Only this checker prints output. It does not modify source files.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import numpy as np
import scipy
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/programme-ideas-20261031'

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

def exact_ritz_counterexample():
    g = [sp.Rational(i, 2) for i in range(-2, 3)]
    nodes = [(x, y) for x in g for y in g]
    monomials = [(a, d-a) for d in range(3) for a in range(d+1)]
    V = sp.Matrix([[x**a*y**b for a,b in monomials] for x,y in nodes])
    P = V * (V.T * V).inv() * V.T
    B = nodes.index((0, 0))
    p = P[:, B]
    rx = P * sp.diag(*[x for x,y in nodes]) * p
    ry = P * sp.diag(*[y for x,y in nodes]) * p
    assert rx == sp.zeros(25, 1) and ry == sp.zeros(25, 1)
    assert P[B,B] < 1
    return dict(grid='5x5 equispaced [-1,1]^2', total_degree=2, node=[0,0],
                leverage=str(P[B,B]), residual_x_squared=str((rx.T*rx)[0]),
                residual_y_squared=str((ry.T*ry)[0]), exact_arithmetic='SymPy Rational')

result = dict(source_sha='614709d4a60fb0c2593b05764e8d5aceda1be381',
              requested_model='gpt-6-astra xhigh; inherited runtime metadata unexposed',
              environment=dict(python=platform.python_version(),numpy=np.__version__,
                               scipy=scipy.__version__,sympy=sp.__version__),
              exact_ritz_counterexample=exact_ritz_counterexample())

# Independent execution of the developer's recurrence library, restricted to K3's
# primary scope and a polynomial control. No 80-bit/reference approximation claim.
orf = module('orf2d_audit', TOPIC/'checks/code/decisive/gen1-3/orf2d.py')
x,y = orf.cheb_grid(64)
w = np.ones(len(x))
recurrence = []
for cls,orders in [('P', ['far']), ('Ppt', ['far','near'])]:
    lines = orf.make_lines(cls, 24, 3e-4, orders[0])
    for order in orders:
        lines = orf.make_lines(cls, 24, 3e-4, order)
        for proj,con,fixed,label in [(3,0,True,'L3'),(2,1,False,'L3c'),(3,1,False,'L4c'),(0,0,False,'LF')]:
            if cls=='P' and label=='L4c':
                continue
            run=orf.Lanczos(lines,24,proj=proj,con=con,fixed_dims=fixed).run(x,y,w)
            recurrence.append(dict(cls=cls,order=order,method=label,delta=float(orf.orth_defect(run.Q,w))))
result['primary_K3_rerun']=recurrence

# Reconstruct the commutator defect independently using QR of monomial evaluations.
t=2*np.pi*np.arange(64)/64
cx=np.cos(7*t)*np.cos(t)
cy=np.cos(7*t)*np.sin(t)
inds=[(a,d-a) for d in range(6) for a in range(d+1)]
VV=np.column_stack([cx**a*cy**b for a,b in inds])
QQ=np.linalg.qr(VV)[0]
degs=np.array([a+b for a,b in inds])
checks=[]
for degree in [1,2,3,4]:
    q=QQ[:,degs<=degree]
    qb=QQ[:,degs==degree+1]
    Hx=q.T@(cx[:,None]*q); Hy=q.T@(cy[:,None]*q)
    bx=qb.T@(cx[:,None]*q); by=qb.T@(cy[:,None]*q)
    comm=Hx@Hy-Hy@Hx
    predicted=-(bx.T@by-by.T@bx)
    checks.append(dict(degree=degree,commutator_norm=float(np.linalg.norm(comm,2)),
                       predicted_error=float(np.max(np.abs(comm-predicted)))))
result['independent_curve_commutator']=checks
print(json.dumps(result,indent=2))
