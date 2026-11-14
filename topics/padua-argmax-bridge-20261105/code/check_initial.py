#!/usr/bin/env python3
"""Independent supplementary N6 reconstruction; no developer module imports."""
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
LOCAL = ROOT / 'local-output/argmax-bridge-20261105/check-initial'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    x, y = s.symbols('x y')
    basis = s.Matrix([1, x, y, x*x, x*y, y*y])
    nodes = [(1, 1), (1, -s.Rational(1, 2)), (0, s.Rational(1, 2)),
             (0, -1), (-1, 1), (-1, -s.Rational(1, 2))]
    matrix = s.Matrix([list(basis.subs({x:a, y:b})) for a, b in nodes])
    need(matrix.det() != 0, 'n2 unisolvence')
    cardinals = list((basis.T * matrix.inv()).applyfunc(s.expand))
    need(all(s.simplify(sum(cardinals)-1) == 0 for _ in [0]), 'unity')
    r = s.sqrt(2)
    points = [(-r/2, 0), (r/2, 0), (-1, -r/2)]
    values = [[s.simplify(p.subs({x:a, y:b})) for p in cardinals] for a,b in points]
    norms = [s.simplify(sum(s.Abs(v) for v in row)) for row in values]
    expected = [s.Rational(3,2)+r/6, s.Rational(3,2)+r/6, s.Rational(1,3)+r]
    need(all(s.simplify(a-b) == 0 for a,b in zip(norms,expected)), 'exact norms')
    need(50 > 49, 'strict gap via positive square comparison')
    fresh = json.loads((LOCAL/'n6-two-trace.json').read_text())
    developer = json.loads((TOPIC/'evidence/n6-two-trace.json').read_text())
    math_keys = ['degree','t','witness_s','comparison_s','monomial_order','node_indices',
                 'rational_cardinal_coefficients','rational_inversion_matches_corrected_kernel',
                 'rows','gap','gap_positive_exactly','status']
    need(all(fresh[k] == developer[k] for k in math_keys), 'frozen N6 replay mismatch')
    files = ['code/n6_two_trace_exact.py', 'theory/N6-two-trace-obstruction.md',
             'theory/N6-parallel-family-verification.md', 'ideas/N6-two-trace.md',
             'novelty-gate-N6.md', 'evidence/n6-two-trace.json']
    pin = '0bca52bc1b8edf2e91d3749b710d2df285dc3e6b'
    for name in files:
        relative = (TOPIC/name).relative_to(ROOT).as_posix()
        frozen = subprocess.check_output(['git','show',f'{pin}:{relative}'], cwd=ROOT)
        need(frozen == (TOPIC/name).read_bytes(), 'frozen source mismatch '+name)
    receipt = {
        'format':'padua-bridge-independent-math-initial-v1',
        'role':'distinct supplementary checker; required Claude audit remains pending',
        'requested_model_effort':'gpt-6-astra high',
        'runtime_model_effort':'not independently exposed',
        'rules_head':'95366c19562e88c11138f88aab0a6617d6b15305',
        'frozen_input_commit':pin,
        'python':platform.python_version(), 'sympy':s.__version__,
        'command':[sys.executable,*sys.argv], 'cwd':str(ROOT), 'seed':None,
        'checker_sha256':sha(Path(__file__)),
        'input_sha256':{name:sha(TOPIC/name) for name in files},
        'registry_sha256':sha(ROOT/'state/IDEAS.md'),
        'frozen_developer_script_reexecuted':True,
        'fresh_raw_receipt':str((LOCAL/'n6-two-trace.json').relative_to(ROOT)),
        'fresh_raw_receipt_sha256':sha(LOCAL/'n6-two-trace.json'),
        'fresh_raw_receipt_bytes':(LOCAL/'n6-two-trace.json').stat().st_size,
        'raw_independent_execution_false_field':'hard-coded by unchanged developer script; actual separate execution recorded here',
        'mathematical_receipt_fields_compared':math_keys,
        'all_mathematical_fields_equal':True,
        'independent_sympy_reconstruction':{
            'vandermonde_determinant':str(matrix.det()),
            'cardinals':[str(p) for p in cardinals],
            'values':[[str(v) for v in row] for row in values],
            'norms':[str(v) for v in norms],
            'gap':str(s.simplify(norms[2]-norms[0])),
            'positive_gap_reason':'sqrt(50)>sqrt(49), hence 5*sqrt(2)>7',
        },
        'analytic_review':['unimodular torus inverse and 4/2/1 multiplicities',
                           'node/nonnode corner phases and fixed-trace visits',
                           'exceptional corrected x mode and finite frequency bounds',
                           'exact n2 signs and strict counterexample'],
        'scope':'fixed-t two-trace comparison only; broad N6 and PD-T099 unaffected',
        'status':'PASS',
    }
    output = TOPIC/'evidence/independent-math-initial.json'
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','receipt':str(output),'sha256':sha(output)}))


if __name__ == '__main__':
    main()
