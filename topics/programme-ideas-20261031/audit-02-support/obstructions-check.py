#!/usr/bin/env python3
"""Independent targeted re-audit at cadb35066160e466cb1704b9791ad6f374446422.

Auditor: Codex /root/audit_obstructions; inherited user-requested Astra xhigh.
Only reads developer evidence; all outputs go to stdout for audit recording.
"""
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import numpy as np
import scipy
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/programme-ideas-20261031'
OLD = Path('/workspace/programme-audit-614709d/topics/programme-ideas-20261031')
SHA = 'cadb35066160e466cb1704b9791ad6f374446422'
ENV = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
relevant = [
    'response-01.md', 'OPEN_TARGETS.md', 'report.md', 'ideas/candidates.md',
    'checks/adversarial-M1.md', 'checks/adversarial-M2.md',
    'checks/adversarial-gen2-3.md', 'checks/adversarial-gen3-1.md',
    'theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md',
    'theory/programme-ideas-claude-03-compressed-commutator-identity.md',
    'theory/programme-ideas-claude-N01-symmetrised-product-inertia-count.md',
    'theory/programme-ideas-claude-N04-pattern-commutant-not-three-dimensional.md',
    'theory/programme-ideas-claude-N05-fourier-basis-commutation-fails.md',
]
out = {'candidate': SHA, 'historical_candidate':
       '614709d4a60fb0c2593b05764e8d5aceda1be381',
       'model_assignment': 'gpt-6-astra xhigh (inherited; resolved runtime metadata unexposed)',
       'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                       'scipy': scipy.__version__, 'sympy': sp.__version__,
                       'platform': platform.platform()},
       'review_input_sha256': {p: hashlib.sha256((TOPIC/p).read_bytes()).hexdigest()
                               for p in relevant},
       'rules_and_registry_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
          for p in ['AGENTS.md','agents/WORKFLOW.md','agents/codex/CODEX.md','state/IDEAS.md']},
       'runs': []}

unchanged, different = [], []
for p in sorted((OLD/'checks/code').rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts:
        rel = p.relative_to(OLD)
        current = TOPIC / rel
        match = current.is_file() and p.read_bytes() == current.read_bytes()
        row = {'path': str(rel), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
        (unchanged if match else different).append(row)
out['historical_code_and_output_identity'] = {
    'reference_snapshot': str(OLD), 'unchanged_count': len(unchanged),
    'unchanged': unchanged, 'different': different}
assert not different

for rel in ['checks/code/response-01/inertia_two_node_family.py',
            'checks/code/response-02/padua_pattern_commutant.py',
            'checks/code/adv/gen3-1/commutator_sections.py',
            'checks/code/adv/M2/m2_favard_commutant.py']:
    cp = subprocess.run([sys.executable, '-I', str(TOPIC/rel)],
                        cwd=ROOT, env=ENV, capture_output=True, text=True, timeout=180)
    assert cp.returncode == 0, cp.stderr
    record = {'command': [sys.executable, '-I', str(TOPIC/rel)],
              'sha256': hashlib.sha256((TOPIC/rel).read_bytes()).hexdigest(),
              'returncode': cp.returncode, 'stdout': cp.stdout, 'stderr': cp.stderr}
    if 'response-01/inertia_' in rel:
        data = json.loads(cp.stdout)
        assert data['det_S_equals_formula']
        assert len(data['instances']) == 5
        assert all(r['n_box_formula'] == '3/2' and r['n_plus_S'] == 1
                   and r['n_plus_Mx'] == r['n_plus_My'] == 2 for r in data['instances'])
        record['comparison_with_committed_output'] = json.loads(
            (TOPIC/rel.replace('.py','.out')).read_text()) == data
        assert record['comparison_with_committed_output']
    elif 'padua_pattern_commutant' in rel:
        data = json.loads(cp.stdout)
        assert data['det_V'] == '-27/2'
        assert data['commutator_zero'] and data['all_pivots_positive']
        assert data['pattern_violations'] == []
        assert data['n_symmetric_variables_in_pattern_y'] == 17
        assert data['rank_of_commutator_map'] == 11 and data['commutant_dimension'] == 6
        record['comparison_with_committed_output'] = json.loads(
            (TOPIC/rel.replace('.py','.out')).read_text()) == data
        assert record['comparison_with_committed_output']
    elif 'commutator_sections' in rel:
        rows=[]
        for line in cp.stdout.splitlines():
            v=line.split()
            if len(v)==6 and v[0].isdigit() and v[1].isdigit():
                rows.append([int(v[0]),int(v[1]),*map(float,v[2:])])
        assert len(rows)==66
        assert min(r[2] for r in rows) >= 0.08
        assert max(r[2] for r in rows) <= 0.5000001
        record['parsed_summary']={'row_count':len(rows),
            'min_commutator_norm': min(r[2] for r in rows),
            'max_commutator_norm': max(r[2] for r in rows),
            'max_identity_entry_error':max(r[4] for r in rows)}
    out['runs'].append(record)

# An independent dense QR/SVD route verifies the invariant identity and unitary
# Fourier transformation on one freshly executed instance without reusing outputs.
M=64
t=2*np.pi*np.arange(M)/M
x=np.cos(7*t)*np.cos(t)
y=np.cos(7*t)*np.sin(t)
F=np.fft.fft(np.eye(M))/np.sqrt(M)
own=[]
for n in range(1,5):
    mons=[(d-j,j) for d in range(n+1) for j in range(d+1)]
    V=np.column_stack([x**a*y**b for a,b in mons])
    Q,_=np.linalg.qr(V)
    XQ=x[:,None]*Q; YQ=y[:,None]*Q
    Hx=Q.T@XQ; Hy=Q.T@YQ
    C=Hx@Hy-Hy@Hx
    Rx=XQ-Q@Hx; Ry=YQ-Q@Hy
    pred=-(Rx.T@Ry-Ry.T@Rx)
    Qf=F@Q; Xf=F@np.diag(x)@F.conj().T; Yf=F@np.diag(y)@F.conj().T
    A=Qf.conj().T@Xf@Qf; B=Qf.conj().T@Yf@Qf
    err=float(np.max(np.abs(C-pred)))
    ferr=float(np.max(np.abs(C-(A@B-B@A))))
    assert err < 1e-12 and ferr < 1e-12
    own.append({'n':n,'norm':float(np.linalg.norm(C,2)),
                'boundary_identity_max_error':err,'Fourier_transform_max_error':ferr})
out['independent_QR_reconstruction']=own
print(json.dumps(out,indent=2))
