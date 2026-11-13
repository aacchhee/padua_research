#!/usr/bin/env python3
"""Supplementary checker; run producer code only in a disposable checkout.

Original receipts are copied before execution. Producer scratch paths are
redirected by changing module globals only; result-bearing functions are intact.
The historical D0 replay internally executes read-only `git show`.
"""
import argparse
import collections
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

TOPIC = Path('topics/padua-3d-20261106')
PIN = 'a1cce96d6c936d36d2f0e302585a94e5fd735f48'
STAGES = ['replay', 't2_screen', 't2_generators', 't2_quality',
          't2_check_cover', 't3_checks', 't4_stacks', 't5_exact', 't5_support']
OUTPUTS = ['replay.json', 't2-cyclic-screen.json', 't2-generators.json',
           't2-quality.json', 't2-cover-check.json', 't3-checks.json',
           't4-mesh-M.json', 't4-mesh-A.json', 't4-mesh-L.json',
           't4-baselines.json', 't5-exact.json', 't5-support.json']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stage(args):
    code = args.source_root / TOPIC / 'code'
    sys.path.insert(0, str(code))
    spec = importlib.util.spec_from_file_location(args.stage, code/(args.stage+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    scratch = args.work_dir/'scratch'
    scratch.mkdir(parents=True, exist_ok=True)
    if hasattr(module, 'TMP'):
        module.TMP = scratch
    if args.stage == 't2_generators':
        original_path = module.Path
        module.Path = lambda p: scratch if str(p) == '/tmp/padua-3d-20261106' else original_path(p)
    if args.stage in ('t3_checks', 't5_exact', 't5_support'):
        sys.argv = [str(code/(args.stage+'.py')), '--output',
                    str(args.source_root/TOPIC/'evidence'/(args.stage.replace('_', '-')+'.json'))]
        module.main()
    elif args.stage == 't4_stacks':
        sys.argv = [str(code/'t4_stacks.py'), '--max-degree', '12']
        module.main(argparse.Namespace(max_degree=12))
    elif args.stage == 't2_check_cover':
        module.check()
    else:
        module.main()


def check_h39(path):
    """Independent Fraction convolution, not the producer's folded dictionary."""
    data = json.loads(path.read_text())
    assert (data['n'], data['N'], data['M'], data['count']) == (3, 20, 39, 171)
    expected = set(itertools.combinations(range(1, 20), 2))
    seen = set()
    for b, c, unused_rank, terms in data['witnesses']:
        assert (b, c) in expected and (b, c) not in seen
        seen.add((b, c))
        assert terms
        powers = [tuple(a) for a, v in terms]
        assert len(powers) == len(set(powers))
        residue = collections.defaultdict(Fraction)
        for a, coefficient in terms:
            assert type(coefficient) is int and coefficient != 0
            assert len(a) == 3 and all(type(k) is int and k >= 0 for k in a) and sum(a) <= 3
            polynomial = {0: Fraction(coefficient)}
            for power, frequency in zip(a, (1, b, c)):
                axis = collections.defaultdict(Fraction)
                axis[(power*frequency) % 39] += Fraction(1, 2)
                axis[(-power*frequency) % 39] += Fraction(1, 2)
                product = collections.defaultdict(Fraction)
                for i, u in polynomial.items():
                    for j, v in axis.items():
                        product[(i+j) % 39] += u*v
                polynomial = product
            for i, u in polynomial.items():
                residue[i] += u
        assert all(v == 0 for v in residue.values()), (b, c)
    assert seen == expected
    return {'coverage': len(seen), 'arithmetic': 'Fraction Laurent convolution modulo t^39-1',
            'all_zero': True, 'recorded_ranks_used': False, 'H39_discharged': True}


def independent_math():
    import sympy as s
    import mpmath as mp
    # Full exact moment matrix, using tensor Chebyshev modes at radical nodes.
    x = s.symbols('x')
    axis = [-s.sqrt(3)/2, s.S.Zero, s.sqrt(3)/2]
    nodes = list(itertools.product(axis, repeat=3))
    powers = [a for a in itertools.product(range(6), repeat=3) if sum(a) <= 5]
    table = [[s.chebyshevt(k, t).expand() for k in range(6)] for t in axis]
    indices = list(itertools.product(range(3), repeat=3))
    matrix = s.Matrix([[s.prod(table[j][k] for j, k in zip(pt, a)) for pt in indices] for a in powers])
    moments = s.Matrix([int(a == (0, 0, 0)) for a in powers])
    chi = s.Matrix([s.prod(s.chebyshevt(2, t) for t in pt) for pt in nodes])
    assert matrix.rank() == 26
    assert matrix*s.ones(27, 1)/27 == moments
    assert matrix*chi == s.zeros(56, 1)
    support = []
    for t in sorted({-1/v for v in chi}):
        weights = (s.ones(27, 1)+t*chi)/27
        assert matrix*weights == moments
        support.append({'t': str(t), 'support': sum(v != 0 for v in weights),
                        'nonnegative': all(v >= 0 for v in weights)})
    assert min(r['support'] for r in support if r['nonnegative']) == 21
    assert min(r['support'] for r in support) == 15
    # Direct orthonormal boundary maps; no producer section routine imported.
    ranks = []
    for d in (2, 3):
        for q in range(7):
            basis = [a for a in itertools.product(range(q+1), repeat=d) if sum(a) == q]
            next_basis = [a for a in itertools.product(range(q+2), repeat=d) if sum(a) == q+1]
            pos = {a: k for k, a in enumerate(next_basis)}
            boundary = []
            for j in (0, 1):
                B = s.zeros(len(next_basis), len(basis))
                for col, a in enumerate(basis):
                    b = list(a); b[j] += 1
                    B[pos[tuple(b)], col] = s.sqrt(2)/2 if a[j] == 0 else s.Rational(1, 2)
                boundary.append(B)
            C = boundary[0].T*boundary[1]-boundary[1].T*boundary[0]
            r = C.rank()
            expected = 2*((q+1)//2) if d == 2 else 2*((q+1)**2//4)
            assert r == expected
            ranks.append([d, q, r])
    # Independent exact block-determinant controls on rational planar lower sets.
    determinants = []
    for n in range(4):
        modes = [(a, b, k) for k in range(n+1) for a in range(n-k+1) for b in range(n-k-a+1)]
        slices = [[(a, b) for a in range(n-k+1) for b in range(n-k-a+1)] for k in range(n+1)]
        for heights in [list(range(n+1)), list(reversed(range(n+1)))]:
            pts = [(a, b, heights[k]) for k, pts2 in enumerate(slices) for a, b in pts2]
            V = s.Matrix([[s.prod(s.Integer(t)**e for t, e in zip(pt, mode)) for mode in modes] for pt in pts])
            planar = s.S.One
            for pts2 in slices:
                planar *= s.Matrix([[s.Integer(a)**u*s.Integer(b)**v for u, v in pts2] for a, b in pts2]).det()
            predicted = planar*s.prod((heights[j]-heights[i])**len(slices[j]) for j in range(n+1) for i in range(j))
            assert V.det() == predicted != 0
            determinants.append([n, heights, str(predicted)])
    for m in range(1, 51):
        inverse_norm_sum = sum(1 if (a, b) in ((0, 0), (m, 0)) else 2**((a > 0)+(b > 0))
                               for a in range(m+1) for b in range(m-a+1))
        assert inverse_norm_sum == 2*m*(m+1)
    with mp.workdps(60):
        integral = mp.log(2)/24 + mp.quad(lambda v: (1-v)**3*mp.log(mp.sin(mp.pi*v)), [0, mp.mpf('.5'), 1])/3
        analytic = -mp.log(2)/24-mp.zeta(3)/(4*mp.pi**2)
        assert abs(integral-analytic) < mp.mpf('1e-55')
        diagnostic = {'weighted_integral': mp.nstr(integral, 40),
                      'absolute_difference': mp.nstr(abs(integral-analytic), 8),
                      'lower_rate': mp.nstr(3*mp.zeta(3)/(2*mp.pi**2), 40),
                      'status': 'MEASURED quadrature corroboration; hand proof is separate'}
    return {'H39_method_separate': True, 'T5_Chebyshev_matrix_rank': 26,
            'T5_support_roots': support, 'boundary_ranks_d_q_rank': ranks,
            'rational_stack_determinants': determinants,
            'Padua_inverse_Gram_sum_m1_to_50': True, 'T4_integral': diagnostic}


IGNORED = {'elapsed_seconds', 'elapsed_total_seconds', 'seconds', 'command', 'catalogue_path',
           'preregistration_sha256'}


def clean(value):
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items() if k not in IGNORED}
    if isinstance(value, list):
        return [clean(v) for v in value]
    return value


def main(args):
    import numpy, scipy, sympy, mpmath
    evidence = args.source_root/TOPIC/'evidence'
    originals = args.original or args.work_dir/'original'
    originals.mkdir(parents=True, exist_ok=True)
    args.work_dir.mkdir(parents=True, exist_ok=True)
    for name in OUTPUTS:
        if not (originals/name).exists():
            shutil.copyfile(evidence/name, originals/name)
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    executed = []
    for name in STAGES:
        command = [sys.executable, str(Path(__file__).resolve()), '--source-root', str(args.source_root),
                   '--work-dir', str(args.work_dir), '--stage', name]
        started = time.monotonic()
        result = subprocess.run(command, cwd=args.source_root, env=env, capture_output=True, text=True)
        log = args.work_dir/(name+'.log')
        log.write_text(result.stdout+result.stderr)
        executed.append({'stage': name, 'exit_code': result.returncode,
                         'elapsed_seconds': round(time.monotonic()-started, 3), 'log_sha256': sha(log)})
        assert result.returncode == 0, (name, result.stderr)
    comparisons = {}
    for name in OUTPUTS:
        old = json.loads((originals/name).read_text())
        new = json.loads((evidence/name).read_text())
        equal = clean(old) == clean(new)
        comparisons[name] = {'original_sha256': sha(originals/name), 'replay_sha256': sha(evidence/name),
                             'result_equal_excluding_listed_metadata': equal}
        if old.get('preregistration_sha256') != new.get('preregistration_sha256'):
            comparisons[name]['preregistration_hash_difference'] = {
                'original': old.get('preregistration_sha256'),
                'replay': new.get('preregistration_sha256')}
        assert equal, name
        shutil.copyfile(evidence/name, args.work_dir/name)
    out = {'schema': 'padua-3d-independent-computation-v1', 'source_commit': PIN,
           'checker_sha256': sha(__file__), 'source_root': str(args.source_root),
           'versions': {'python': platform.python_version(), 'numpy': numpy.__version__,
                        'scipy': scipy.__version__, 'sympy': sympy.__version__, 'mpmath': mpmath.__version__},
           'stage_command_template': f'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 {sys.executable} {Path(__file__).resolve()} --source-root {args.source_root} --work-dir {args.work_dir} --stage STAGE',
           'redirects': 'TMP module global; t2_generators Path factory only for original absolute scratch path',
           'comparison_ignored_fields': sorted(IGNORED), 'executed': executed,
           'code_sha256': {name+'.py': sha(args.source_root/TOPIC/'code'/(name+'.py')) for name in STAGES},
           'inherited_code_sha256': {name: sha(args.source_root/'tracks/lattice-unisolvence/code'/name)
                                     for name in ['c0_catalogue.py', 'c3_rank.py', 'c3_lebesgue.py']},
           'comparisons': comparisons,
           'H39_input_sha256': sha(evidence/'t2-n3-null-cover.json'),
           'H39': check_h39(evidence/'t2-n3-null-cover.json'), 'additional_checks': independent_math()}
    if args.addendum_root:
        out['addendum_commit'] = '7407e13a0fb7b4ddbeb846d24c765fda0bd4f13c'
        out['addendum_prose_sha256'] = {name: sha(args.addendum_root/TOPIC/'theory'/name)
                                       for name in ['t4-stack-upper.md', 't4-mesh-observations.md', 't4-quality-target.md']}
    raw = json.dumps(out, separators=(',', ':'))+'\n'
    assert len(raw.encode()) < 16384
    args.output.write_text(raw)
    print(json.dumps({'status': 'PASS', 'H39': 'discharged', 'stages': len(executed),
                      'receipts_compared': len(comparisons), 'bytes': len(raw.encode())}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--original', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--addendum-root', type=Path)
    parser.add_argument('--stage', choices=STAGES)
    args = parser.parse_args()
    if args.stage:
        stage(args)
    else:
        assert args.output is not None
        main(args)
