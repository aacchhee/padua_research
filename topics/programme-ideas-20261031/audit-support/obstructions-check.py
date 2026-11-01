#!/usr/bin/env python3
"""Independent audit diagnostics at candidate 614709d4a60fb0c2593b05764e8d5aceda1be381.

Auditor: Codex; user-requested gpt-6-astra xhigh, inherited runtime identifiers
not separately exposed. Does not modify developer evidence. Output to stdout.
"""
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import numpy as np
import scipy
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/programme-ideas-20261031'
ENV = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
files = [
    'checks/adversarial-M1.md', 'checks/adversarial-M2.md',
    'checks/adversarial-gen2-3.md', 'report.md', 'ideas/candidates.md',
    'checks/code/adv/M2/m2_favard_commutant.py',
    'checks/code/adv/M2/m2_common.py',
    'checks/code/adv/M1/m1_word_rule.py',
    'checks/code/adv/gen2-3/t3_delta_exponent.py',
    'checks/code/adv/gen2-3/pairs.py',
]
result = {
    'candidate': '614709d4a60fb0c2593b05764e8d5aceda1be381',
    'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                    'scipy': scipy.__version__, 'sympy': sp.__version__,
                    'platform': platform.platform()},
    'inputs': {f: hashlib.sha256((TOPIC / f).read_bytes()).hexdigest() for f in files},
    'runs': [],
}
for rel in [
    'checks/code/adv/M2/m2_favard_commutant.py',
    'checks/code/adv/M1/m1_word_rule.py',
    'checks/code/adv/gen2-3/t3_delta_exponent.py',
]:
    proc = subprocess.run([sys.executable, str(TOPIC / rel)], cwd=ROOT,
                          env=ENV, capture_output=True, text=True, timeout=120)
    result['runs'].append({'command': [sys.executable, str(TOPIC / rel)],
                           'returncode': proc.returncode,
                           'stdout': proc.stdout, 'stderr': proc.stderr})
    if proc.returncode:
        raise RuntimeError(proc.stderr)

# Independent exact arithmetic for the same 45-degree cluster mechanism.
# Hx=diag(0,e), Hy=R diag(0,e) R^T, box=(-e/10,1)^2.
# Mx has eigenvalues a=e/10, b=11e(1-e)/10; My=R Mx R^T.
# det((Mx My+My Mx)/2)=-(a+b)^2 (a^2-6ab+b^2)/16.
# This verifies only this formula and reference cluster, not every possible
# certificate, positive-pivot recurrence pair, or computed-section class.
exact = []
for exponent in [1, 2, 3, 4, 8]:
    eps = F(1, 10**exponent)
    a, b = eps / 10, 11 * eps * (1-eps) / 10
    determinant = -(a+b)**2 * (a*a - 6*a*b + b*b) / 16
    assert determinant < 0
    exact.append({'eps': str(eps), 'delta': str(eps*eps/2),
                  'line_distance': str(eps/10), 'determinant': str(determinant),
                  'product_positive_inertia': 1,
                  'Mx_positive_inertia': 2, 'My_positive_inertia': 2,
                  'count_formula': '3/2', 'reference_count': 2})
result['independent_exact_cluster'] = exact

# Exact n=2 Padua counterexample to an unqualified three-dimensional
# pattern-commutant claim. This is verification evidence, not a new PD-T.
xs = [1, 1, 0, 0, -1, -1]
ys = [1, -sp.Rational(1,2), sp.Rational(1,2), -1, 1, -sp.Rational(1,2)]
ws = list(map(sp.Rational, [F(1,12), F(1,6), F(1,3), F(1,6), F(1,12), F(1,6)]))
mons = [(0,0), (1,0), (0,1), (2,0), (1,1), (0,2)]
V = sp.Matrix([[sp.Rational(x)**i * sp.Rational(y)**j for i,j in mons]
               for x,y in zip(xs,ys)])
W = sp.diag(*ws)
poly = []
for j in range(6):
    p = V[:,j]
    for q in poly:
        p -= q * (q.T * W * p)[0]
    poly.append(sp.simplify(p / sp.sqrt((p.T * W * p)[0])))
P = sp.Matrix.hstack(*poly)
Hx_exact = sp.simplify(P.T * W * sp.diag(*xs) * P)
Hy_exact = sp.simplify(P.T * W * sp.diag(*ys) * P)
assert Hx_exact * Hy_exact == Hy_exact * Hx_exact
index = {m:i for i,m in enumerate(mons)}
pi_y = [index.get((i,j+1)) if i+j < 2 else None for i,j in mons]
sym_entries = [(i,j) for i in range(6) for j in range(i,6)
               if (pi_y[j] is None or i<=pi_y[j])
               and (pi_y[i] is None or j<=pi_y[i])]
cols = []
for i,j in sym_entries:
    E = sp.zeros(6)
    E[i,j] = E[j,i] = 1
    cols.append((Hx_exact * E - E * Hx_exact).reshape(36,1))
commutator_map = sp.Matrix.hstack(*cols)
rank = commutator_map.rank()
assert V.det() == -sp.Rational(27,2)
assert len(sym_entries) - rank == 6
result['exact_padua_pattern_commutant'] = {
    'n': 2, 'N': 6, 'x': list(map(str,xs)), 'y': list(map(str,ys)),
    'w': list(map(str,ws)), 'monomial_order': mons, 'det_V': str(V.det()),
    'Hx': str(Hx_exact), 'Hy': str(Hy_exact),
    'pattern_Hy_symmetric_variables': sym_entries,
    'commutator_map_rank': rank, 'commutant_dimension': len(sym_entries)-rank,
    'observation': 'Dimension 6, exceeding span{I,Hx,Hy} dimension 3.'}

# Strict positivity does not follow merely from simultaneous symmetry.
Hx = np.diag([0., 1., 2.]); Hy = np.diag([0., 1., -1.])
weights = np.eye(3)[0, :]**2
assert np.array_equal(weights, [1., 0., 0.])
result['nonnegative_not_strictly_positive'] = {
    'Hx_diagonal': Hx.diagonal().tolist(), 'Hy_diagonal': Hy.diagonal().tolist(),
    'first_component_squared_weights': weights.tolist(),
    'observation': 'Commuting real symmetric pairs can have dark zero-weight modes.'}
print(json.dumps(result, indent=2))
