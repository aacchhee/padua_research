#!/usr/bin/env python3
"""Supplementary checks, not a readiness audit or an all-N computer proof.

Requires independently executed 210-dps conditioning outputs in --raw.
Writes a short JSON receipt to stdout. No developer files are modified.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import re
import zipfile
from itertools import product
from math import comb
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/nn-mop-conditioning-20261106'


def digest(path):
    data = path.read_bytes()
    return dict(path=str(path), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def replay(raw):
    mp.mp.dps = 320
    history = ROOT / 'topics/nn-mop-stability-20261105/attempts/D1.md'
    table = {}
    for line in history.read_text().splitlines():
        cells = [s.strip() for s in line.split('|')]
        if len(cells) == 7 and cells[1].isdigit():
            table[int(cells[1])] = cells[2:6]
    receipt = json.loads((TOPIC / 'm0a-receipt.json').read_text())
    for entry in receipt['inputs']:
        assert digest(Path(entry['path'])) == entry
    rows, paths = [], []
    for family, column in [('krawtchouk', 0), ('hahn', 1)]:
        runs = []
        for filename in [f'm0-{family}.json', f'm0-{family}260.json',
                         f'independent-m0-{family}.json']:
            path = raw / filename
            paths.append(digest(path))
            runs.append(json.loads(path.read_text()))
        assert [int(r['argv'][-1]) for r in runs] == [180, 260, 210]
        assert len({r['code_sha256'] for r in runs}) == 1
        assert len({r['baseline_sha256'] for r in runs}) == 1
        for run in runs:
            assert [c['N'] for c in run['cases']] == [4, 16, 32]
        for cases in zip(*(r['cases'] for r in runs)):
            assert len({c['input_sha256'] for c in cases}) == 1
            for target, col in [('NN', column), ('step_line', column + 2)]:
                vals = [mp.mpf(c[target]['mixed']['kappa']) for c in cases]
                differences = [abs(x / vals[1] - 1) for x in (vals[0], vals[2])]
                assert max(differences) < mp.mpf('1e-10')
                assert mp.mpf(mp.nstr(vals[2], 7)) == mp.mpf(table[cases[0]['N']][col])
                rows.append(dict(family=family, N=cases[0]['N'], target=target,
                                 replay_relative_difference=mp.nstr(differences[1], 10)))
    return dict(verdict='PASS within M0a; original M0 remains UNASSESSABLE',
                cases=rows, inputs=paths)


def small_derivative():
    path = ROOT / 'topics/nn-mop-stability-20261105/code/conditioning.py'
    mod = load('independent_conditioning', path)
    rows = []
    for family in ('krawtchouk', 'hahn'):
        row = mod.conditioning_case(4, family, dps=180, check=True)
        errors = row['moment_check']
        assert max(mp.mpf(x) for x in errors.values()) < mp.mpf('1e-150')
        rows.append(dict(family=family, N=4, **errors))
    return rows


def interface():
    path = TOPIC / 'code/c4_normalization.py'
    mod = load('independent_c4_interface', path)
    result = mod.check()
    # Extend the round-trip to a negative affine map and a nongeometric gauge.
    from fractions import Fraction as Q
    truth = mod.load('independent_exact_truth', ROOT / 'topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py')
    base = mod.load('independent_inputs', ROOT / 'topics/nn-mop-iep-20261103/code/c4_float_baseline.py')
    extra = []
    for family in ('krawtchouk', 'hahn'):
        N = 5
        x, w = base.inputs(N, family)
        _, c = truth.ground_truth(x, w)
        H = mod.monic_hessenberg(c, N)
        D = [Q(1), Q(7, 3), Q(-2, 11), Q(13), Q(-5, 17)]
        assert mod.make_monic(mod.similarity(H, D)) == H
        s, b = Q(-3, 7), Q(5, 11)
        _, transformed = truth.ground_truth([s * z + b for z in x], w)
        assert mod.affine_monic(H, s, b) == mod.monic_hessenberg(transformed, N)
        extra.append(dict(family=family, N=N, negative_affine_and_nonuniform_gauge=True))
    return dict(developer_cases=result['cases'], additional_cases=extra,
                scope='local exact interface only; no external IEP-MOP fidelity')


def c1_checks(raw):
    mod = load('independent_c1', TOPIC / 'code/c1_metrics.py')
    from fractions import Fraction as Q
    # Exact primal enumeration: at a vertex of a box cut by one hyperplane,
    # at most one coordinate is strictly between its bounds.
    median_cases = 0
    for weights in ([Q(1), Q(1), Q(1)], [Q(1), Q(2), Q(8)],
                    [Q(1), Q(1), Q(2), Q(3)]):
        for grad in product((-2, 0, 3), repeat=len(weights)):
            optimum = Q(0)
            for free in range(len(weights)):
                others = [j for j in range(len(weights)) if j != free]
                for signs in product((-1, 1), repeat=len(others)):
                    z = dict(zip(others, signs))
                    z[free] = -sum(weights[j]*z[j] for j in others)/weights[free]
                    if abs(z[free]) <= 1:
                        optimum = max(optimum, sum(weights[j]*grad[j]*z[j] for j in z))
            median = mod.weighted_median_support(list(grad), [int(w) for w in weights])
            assert mp.mpf(optimum.numerator)/optimum.denominator == median
            median_cases += 1
    rows, artifacts = [], []
    for family in ('krawtchouk', 'hahn'):
        for mode in ('scalar', 'terminal'):
            path = raw / f'independent-c1-{mode}-{family}.json'
            run = json.loads(path.read_text())
            assert run['code_sha256'] == digest(TOPIC / 'code/c1_metrics.py')['sha256']
            assert [c['N'] for c in run['cases']] == [4, 8, 16]
            for row in run['cases']:
                error = max(mp.mpf(r['forward_AD_max_scaled_entry_difference'])
                            for r in row.get('marginals', [row]))
                assert error < mp.mpf('1e-160')
                rows.append(dict(family=family, mode=mode, N=row['N'],
                                 maximum_scaled_derivative_difference=mp.nstr(error, 8)))
            artifacts.append(digest(path))
    return dict(exact_weighted_median_cases=median_cases, derivative_rows=rows,
                artifacts=artifacts)


def c3_checks(raw):
    own_path = raw / 'independent-c3-grid.json'
    own = json.loads(own_path.read_text())
    dev = json.loads((TOPIC / 'c3-grid-summary.json').read_text())
    table = {(r['family'], r['N']): r for r in dev['cases']}
    rows = []
    for row in own['cases']:
        expected = table[row['family'], row['N']]
        for key in ('E', 'ratio', 'c4E', 'c4ratio'):
            assert row[key] == expected[key]
        rows.append(dict(family=row['family'], N=row['N'],
                         A_LU_ratio=row['ratio'], C4_ratio=row['c4ratio']))
    return dict(cases=rows, displayed_nine_digit_cells_agree=True,
                artifacts=[digest(own_path), digest(Path(own['raw']['path']))],
                scope='six selected cases, not the full grid or a stability theorem')


def c2_checks():
    """Own rational moment differentiation and formal-series reconstruction."""
    from fractions import Fraction as Q
    def solve(A, b):
        A = [list(r)+[v] for r, v in zip(A, b)]
        n = len(b)
        for j in range(n):
            p = next(i for i in range(j, n) if A[i][j])
            A[p], A[j] = A[j], A[p]
            v = A[j][j]
            A[j] = [x/v for x in A[j]]
            for i in range(n):
                if i != j:
                    v = A[i][j]
                    A[i] = [x-v*y for x, y in zip(A[i], A[j])]
        return [r[-1] for r in A]
    def series_mul(a, b, degree):
        return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(degree+1)]
    def power(c, exponent, degree):
        return [Q(comb(exponent, j) if j <= exponent else 0)*c**j
                if exponent >= 0 else Q((-1)**j*comb(-exponent+j-1, j))*c**j
                for j in range(degree+1)]
    count = 0
    for p1, p2 in [(Q(1,5),Q(7,10)), (Q(2,5),Q(1,2)),
                   (Q(1,2),Q(3,5)), (Q(3,5),Q(4,5)), (Q(1,10),Q(1,5))]:
        for M in range(1, 8):
            weights = [[Q(comb(M,k))*p**k*(1-p)**(M-k) for k in range(M+1)] for p in (p1,p2)]
            moments = [[sum(w[k]*Q(k)**r for k in range(M+1)) for r in range(2*M+1)] for w in weights]
            dm = [sum(weights[1][k]*(-1)**k*Q(k)**r for k in range(M+1)) for r in range(2*M+1)]
            actual_sum = Q(0)
            a,b = p1/(1-p1),p2/(1-p2)
            A,B,h = (a+b)/(b-a),2*p2,1+b
            for n in range(M):
                m=M-n
                equations=[(s,r) for s,size in enumerate((n,m)) for r in range(size)]
                matrix=[[moments[s][r+j] for j in range(M)] for s,r in equations]
                coeff=solve(matrix,[-moments[s][r+M] for s,r in equations])
                forcing=[-dm[r+M]-sum(coeff[j]*dm[r+j] for j in range(M)) if s else Q(0) for s,r in equations]
                derivative=solve(matrix,forcing)[-1]
                degree=m-1
                polynomial=series_mul(power(1/(a+b),n,degree), power(1/(b-a),-n,degree),degree)
                polynomial=series_mul(polynomial,power(1/(2*b),m,degree),degree)
                R=sum((m-j)*(-h)**j*polynomial[j] for j in range(m))
                predicted=(-1)**n*A**n*B**m*R/h
                assert derivative == predicted
                actual_sum += (-1)**n*derivative
                count += 1
            # Coefficient of rational generating function (11), then /h.
            coefficients=[Q(1),2*A]
            for L in range(2,M):
                coefficients.append(2*A*coefficients[-1]-coefficients[-2])
            reduced=[coefficients[L]-(A*coefficients[L-1] if L else 0) for L in range(M)]
            predicted_sum=B/h*sum((j+1)*(B-1)**j*reduced[M-1-j] for j in range(M))
            assert actual_sum == predicted_sum
            if p2 >= Q(1,2):
                assert actual_sum >= B/h*reduced[M-1]
    return dict(exact_terminal_rows=count, exact_summed_generating_coefficients=35,
                sizes='N2..8', parameters=['1/5,7/10','2/5,1/2','1/2,3/5','3/5,4/5','1/10,1/5'],
                scope='equations (8),(11), coefficient positivity where p2>=1/2; no all-N computer proof')


def external_checks(raw):
    import numpy as np
    import struct
    from fractions import Fraction as Q
    archive = Path('/workspace/attachments/d3b8457a-2c90-4d56-a9a3-f05ea55b5826/IEP-MOP-main.zip')
    assert digest(archive)['sha256'] == 'cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145'
    inventory = []
    with zipfile.ZipFile(archive) as bundle:
        for entry in bundle.infolist():
            if entry.is_dir():
                continue
            data = bundle.read(entry)
            assert data == (Path('/tmp/c4-iep-source') / entry.filename).read_bytes()
            inventory.append([entry.filename, hashlib.sha256(data).hexdigest()])
    # Independent spectral norm calculation against exact Fraction moments.
    bridge = load('independent_m2_bridge', TOPIC/'code/c4_normalization.py')
    base = bridge.load('independent_m2_base', ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py')
    truth = bridge.load('independent_m2_truth', ROOT/'topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py')
    x,w = base.inputs(6,'krawtchouk')
    _,fields = truth.ground_truth(x,w)
    exact_fraction = bridge.affine_monic(bridge.monic_hessenberg(fields,6),Q(5,2),Q(5,2))
    exact = np.array(exact_fraction,dtype=float)
    path = raw/'independent-c4-m2.json'
    results = json.loads(path.read_text())
    def decode(bits):
        return [struct.unpack('>d',bytes.fromhex(bits[j:j+16]))[0] for j in range(0,len(bits),16)]
    def matrix(bits):
        return np.array(decode(bits)).reshape((6,6),order='F')
    shared = next(c for c in results if c['input_kind']=='shared_normalized')
    assert decode(shared['nodes_bits']) == [float(v) for v in x]
    for s,key in enumerate(('weights1_bits','weights2_bits')):
        assert decode(shared[key]) == [float(v) for v in w[s]]
    case = next(c for c in results if c['input_kind']=='archive_integer')
    norm = np.linalg.norm(exact,2)
    def distance(bits):
        got=matrix(bits)
        delta=np.array([[float(Q.from_float(got[i,j])-exact_fraction[i][j]) for j in range(6)] for i in range(6)])
        return float(np.linalg.norm(delta,2)/norm)
    reference_error = distance(case['exact_bits'])
    errors = {name:distance(info['H_bits'])
              for name,info in case['algorithms'].items()}
    assert reference_error < 1e-12 and errors['CORE'] < 1e-12
    g5 = np.loadtxt(raw/'independent-g5/ours_kravchuk.dat')
    value = float(g5[g5[:,0]==10][0,1])
    log_ratio = float(np.log10(value/6.851191e-10))
    assert abs(log_ratio) <= 1
    return dict(archive=digest(archive), archive_members_verified=len(inventory),
                extracted_inventory_sha256=hashlib.sha256(json.dumps(sorted(inventory)).encode()).hexdigest(),
                M2=dict(reference_relative=reference_error, solver_relative=errors,
                        scope='topic N6 Krawtchouk; exact generator and CORE within threshold'),
                M4=dict(paper_N=10, family='kravchuk', CORE_relative=value,
                        log10_ratio_to_paper=log_ratio),
                outputs=[digest(path),digest(raw/'independent-g5/ours_kravchuk.dat'),
                         digest(raw/'independent-g5/ours_hahn.dat')])


def gauge_fit_checks(raw):
    from decimal import Decimal
    table = {}
    historical = ROOT/'topics/nn-mop-stability-20261105/attempts/D1.md'
    for line in historical.read_text().splitlines():
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        if len(cells) == 5 and cells[0].isdigit():
            values = [Decimal(v) for v in cells[1:]]
            table[int(cells[0])] = [mp.mpf(str(v+Decimal(5).scaleb(v.as_tuple().exponent-1))) for v in values]
    summary = json.loads((TOPIC/'c1-summary.json').read_text())
    intervals = {}
    with mp.workdps(100):
        for family, offset in [('krawtchouk',0),('hahn',1)]:
            terminal = json.loads((raw/f'c1-terminal-{family}260.json').read_text())
            data = {row['N']:row for row in terminal['cases']}
            assert set(data) == set(range(4,65))
            for label, key, column in [('NN','NN_gauge_lower',offset),('step','step_gauge_lower',offset+2)]:
                for model in ('mixed','spacing','componentwise_nodes','fixed_mass'):
                    lower_slope = upper_slope = mp.mpf(0)
                    denominator = sum((n-48)**2 for n in range(32,65))
                    for n in range(32,65):
                        lo, hi = mp.log(mp.mpf(data[n][key][model])),mp.log(table[n][column])
                        assert lo <= hi
                        weight = mp.mpf(n-48)/denominator
                        lower_slope += min(weight*lo,weight*hi)
                        upper_slope += max(weight*lo,weight*hi)
                    interval = [float(mp.exp(lower_slope)),float(mp.exp(upper_slope))]
                    reference = summary['gauge_bounds'][family][label]['variant_fit_intervals'][model]
                    assert max(abs(a-b) for a,b in zip(interval,reference)) < 1e-12
                    if model == 'mixed':
                        intervals[family+'_'+label] = interval
    return dict(signed_OLS_intervals=intervals, intervals_verified=16,
                scope='all integer sizes32..64; numerical endpoint evaluations, not outward enclosures')


def sharp_jet_checks():
    from fractions import Fraction as Q
    from math import factorial
    def solve(A,b):
        rows=[list(row)+[value] for row,value in zip(A,b)]
        for j in range(len(rows)):
            pivot=next(i for i in range(j,len(rows)) if rows[i][j])
            rows[j],rows[pivot]=rows[pivot],rows[j]
            divisor=rows[j][j]
            rows[j]=[v/divisor for v in rows[j]]
            for i in range(len(rows)):
                if i != j:
                    factor=rows[i][j]
                    rows[i]=[a-factor*b for a,b in zip(rows[i],rows[j])]
        return [row[-1] for row in rows]
    def evaluate(c,x,j=0):
        return sum(c[r]*Q(factorial(r),factorial(r-j))*x**(r-j) for r in range(j,len(c)))
    count=jets=0
    for M in range(1,7):
        def bernstein(values):
            return [sum(Q(comb(M,k)*comb(M-k,r-k)*(-1)**(r-k))*values[k] for k in range(r+1)) for r in range(M+1)]
        ps=(Q(2,5),Q(1,2))
        w=[[Q(comb(M,k))*p**k*(1-p)**(M-k) for k in range(M+1)] for p in ps]
        xi=[Q(M,2)*(-1)**k for k in range(M+1)]
        eta=[[Q((-1)**(k+s)) if k%3 != s else Q(0) for k in range(M+1)] for s in range(2)]
        for t in range(1,M+1):
            for n in range(t+1):
                sizes=(n,t-n)
                indices=[(s,j) for s,size in enumerate(sizes) for j in range(size)]
                moments=lambda s,r:sum(w[s][k]*Q(k)**r for k in range(M+1))
                A=[[moments(s,j+r) for r in range(t)] for s,j in indices]
                c=solve(A,[-moments(s,j+t) for s,j in indices])+[Q(1)]
                P=[evaluate(c,Q(k)) for k in range(M+1)]
                Pd=[evaluate(c,Q(k),1) for k in range(M+1)]
                rhs=[-sum(w[s][k]*(eta[s][k]*Q(k)**j*P[k]+xi[k]*(Q(k)**j*Pd[k]+(j*Q(k)**(j-1)*P[k] if j else 0))) for k in range(M+1)) for s,j in indices]
                dc=solve(A,rhs)
                R=bernstein([evaluate(dc,Q(k)) for k in range(M+1)])
                f=bernstein([P[k]*xi[k] for k in range(M+1)])
                g=bernstein([Pd[k]*xi[k] for k in range(M+1)])
                for s,j in indices:
                    p=ps[s]
                    fs=bernstein([P[k]*eta[s][k] for k in range(M+1)])
                    logjet=sum(comb(j,l)*evaluate(f,p,j-l)*factorial(l-1)*((-1)**(l-1)/p**l+1/(1-p)**l) for l in range(1,j+1))
                    assert evaluate(R,p,j)+evaluate(fs,p,j)+evaluate(g,p,j)+logjet == 0
                    jets+=1
                v=[comb(M,k)*P[k] for k in range(M+1)]
                harmonic=lambda r:sum((Q(1,j) for j in range(1,r+1)),Q(0))
                for k in range(M+1):
                    predicted=(harmonic(k)-harmonic(M-k))*v[k]+sum(Q((-1)**abs(j-k),k-j)*v[j] for j in range(M+1) if j!=k)
                    assert comb(M,k)*Pd[k] == predicted
                count+=1
    return dict(exact_polynomials=count, exact_differentiated_jets=jets,
                sizes='N2..7', scope='all indices through M; simultaneous node/weight jets (6), weighted differentiation (12)')


def final_replays(raw):
    import csv
    import numpy as np
    from fractions import Fraction as Q
    bridge=load('independent_final_bridge',TOPIC/'code/c4_normalization.py')
    base=bridge.load('independent_final_base',ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py')
    truth=bridge.load('independent_final_truth',ROOT/'topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py')
    matrices=json.loads((raw/'c1-matrix-all.json').read_text())['cases']
    for family in ('krawtchouk','hahn'):
        for N in (4,6,8):
            x,w=base.inputs(N,family)
            _,fields=truth.ground_truth(x,w)
            H=bridge.affine_monic(bridge.monic_hessenberg(fields,N),Q(N-1,2),Q(N-1,2))
            norm=float(np.linalg.norm(np.array(H,dtype=float),2))
            assert abs(norm/matrices[family][str(N)]['spectral_norm']-1) < 1e-14
    a=json.loads((raw/'independent-c4-comparison.json').read_text())
    b=json.loads(Path('/tmp/c4-comparison-bits-raw.json').read_text())
    assert a['cases']==b['cases'] and a['binary64_input_matches']==b['binary64_input_matches']
    hahn=json.loads((raw/'independent-c2-hahn.json').read_text())
    lift=json.loads((raw/'independent-c4-lift.json').read_text())
    assert lift['status']=='PASS' and hahn['normality_systems']==273
    diagnostic=json.loads((TOPIC/'c1-error-comparison.json').read_text())
    diagnostic_rows=0
    for case in diagnostic['cases']:
        family,method,kind=case['family'],case['method'],case['input_kind']
        key='integer_node_input_lower' if kind=='archive_integer' else 'normalized_node_input_lower'
        with (TOPIC/'c4-tables'/f'{family}-{method}.csv').open() as stream:
            records=[row for row in csv.DictReader(stream) if row['input_kind']==kind]
        derived=[]
        for row in records:
            N=int(row['N']); error=float(row['H_integer'])
            bounds=matrices[family][str(N)]
            lo,hi=bounds[key]*2**-53,bounds['upper_both_inputs']*2**-53
            derived.append(dict(N=N,H_relative_spectral_error=error,condition_times_u_bounds=[lo,hi],error_over_condition_u_bounds=[error/hi,error/lo]))
        assert len(derived)==29
        assert case['N16']==next(row for row in derived if row['N']==16) and case['N32']==derived[-1]
        assert case['largest_lower_error_over_condition_u']==max(derived,key=lambda row:row['error_over_condition_u_bounds'][0])
        assert case['largest_upper_error_over_condition_u']==max(derived,key=lambda row:row['error_over_condition_u_bounds'][1])
        assert case['first_N_lower_condition_u_ge_one']==next((row['N'] for row in derived if row['condition_times_u_bounds'][0]>=1),None)
        diagnostic_rows+=len(derived)
    return dict(matrix_norms_from_exact_moments=6,C4_comparison_cases=len(a['cases']),
                C1_error_diagnostic_rows=diagnostic_rows,
                C4_binary64_matches=len(a['binary64_input_matches']),
                Hahn_rerun_counts={key:hahn[key] for key in ('normality_systems','kernel_determinants','cross_expectations','terminal_derivatives')},
                H_anchor_lift_exact_cases=len(lift['cases']),
                artifacts=[digest(raw/name) for name in ('independent-c4-comparison.json','independent-c2-hahn.json','independent-c4-lift.json')])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw', type=Path, default=Path('/tmp/nn-mop-conditioning-20261106'))
    args = parser.parse_args()
    result = dict(source_sha='b4a04981d42c7cd872957facf5e3995e4096ca67',
                  role='supplementary independent checker, not final auditor',
                  python=platform.python_version(), mpmath=mp.__version__,
                  M0a=replay(args.raw), small_moment_derivative=small_derivative(),
                  C4_interface=interface(), C1=c1_checks(args.raw), C3=c3_checks(args.raw),
                  C2=c2_checks(), C4_external=external_checks(args.raw),
                  C1_fit=gauge_fit_checks(args.raw), C2_sharp_jets=sharp_jet_checks(),
                  final_replays=final_replays(args.raw))
    result['source_files'] = [digest(p) for p in [Path(__file__),
        TOPIC / 'code/replay_gate.py', TOPIC / 'code/c4_normalization.py',
        TOPIC / 'code/c1_metrics.py', TOPIC / 'code/c3_grid.py',
        TOPIC / 'code/c4_external.m',
        ROOT / 'topics/nn-mop-stability-20261105/code/conditioning.py',
        ROOT / 'topics/nn-mop-iep-20261103/code/c4_float_baseline.py',
        ROOT / 'topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py']]
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
