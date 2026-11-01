#!/usr/bin/env python3
"""Independent receipt/check of freshly regenerated formal-CGS2 artifacts.

Does not implement the CGS2 map. It checks exact equality with committed
developer certificates, all stored rational enclosures, and exact decisions.
The generator and primitive/projection checker executions are recorded by
their own output artifacts, rather than being claimed as new implementations.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)


def identity(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def check_enclosures(value):
    count = 0
    if isinstance(value, dict):
        if 'sqrt_rational_interval' in value:
            x = Fraction(value['exact'])
            lo, hi = map(Fraction, value['sqrt_rational_interval'])
            assert 0 <= lo <= hi and lo*lo <= x <= hi*hi
            count += 1
        count += sum(check_enclosures(v) for v in value.values())
    elif isinstance(value, list):
        count += sum(map(check_enclosures, value))
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--independent-root', required=True)
    parser.add_argument('--developer-root', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[4]
    evidence = root/'topics/padua-lanczos-drift-20261101/evidence'
    independent, developer = map(Path, [args.independent_root, args.developer_root])
    scalarpath = evidence/'e1-scalar-cgs2.json'
    compactpath = evidence/'e1-multinode-certificates.json'
    scalar = json.loads(scalarpath.read_text())
    compact = json.loads(compactpath.read_text())
    output = {
        'role': 'independent supplementary mathematical checker',
        'rules_sha': '6920ba632843597c37e1493d077c1df2e89f54cb',
        'generated_utc': datetime.now(timezone.utc).isoformat(),
        'model': 'specified scalar CGS2, exact q0, fixed choices, formal independent relative-operation errors',
        'input_norm': 'l-infinity over all formal scalar-operation parameters',
        'output_norm': 'spectral norm of the final orthonormal-basis normal derivative',
        'execution_scope': 'Independent executions of inspected developer generators, primitive and projection checkers; this receipt checker is independently authored. No own full normalized trajectory implementation or actual IEEE claim.',
        'commands': [], 'upper_runs': [], 'coherent_node_runs': [],
        'multinode_runs': [], 'endpoint_identity': [], 'exact_decisions': [],
        'local_artifact_manifest': [], 'inputs': [],
    }
    enclosure_count = 0
    for name, rule in [('triangle', 'pivot'), ('rotated', 'alt')]:
        upperpath = independent/f'cgs2-{name}-n12-{rule}.json'
        onepath = independent/f'cgs2-witness-{name}-n12-bj.json'
        multipath = independent/f'cgs2-multinode-{name}-n12-bj.json'
        upper, one, multi = [json.loads(p.read_text()) for p in
                             [upperpath, onepath, multipath]]
        expected_upper = next(r for r in scalar['full_graph_upper_runs'] if r['set'] == name)
        expected_one = next(r for r in scalar['full_graph_sign_witness_runs'] if r['set'] == name)
        expected_multi = next(r for r in compact['witnesses'] if r['set'] == name)
        fields = [
            (upper, expected_upper, ['set', 'degree', 'rule', 'source_count', 'upper_squared', 'input_norm', 'output_norm', 'rho', 'graph']),
            (one, expected_one, ['set', 'degree', 'rule', 'lower_squared', 'selected_nodes', 'input_norm', 'sign_rule']),
            (multi, expected_multi, ['set', 'degree', 'rule', 'target_column', 'expected_random_sign_lower_squared', 'explicit_greedy_sign_lower_squared', 'node_signs', 'input_norm', 'operation_sign_rule', 'greedy_rule']),
        ]
        for actual, expected, keys in fields:
            for key in keys:
                assert actual[key] == expected[key], (name, key)
            output['endpoint_identity'].append({'set': name, 'producer': actual['code_sha256'], 'compared_keys': keys, 'result': 'IDENTICAL'})
        # The large working artifacts are also compared in full mathematical
        # content. They are not necessary hidden inputs: the generator derives
        # all capacities from explicit nodes, rules, and the retained target.
        localdev = json.loads((developer/multipath.name).read_text())
        for key in ['target_column', 'node_signs', 'target_capacity_exact',
                    'expected_random_sign_lower_squared', 'explicit_greedy_sign_lower_squared']:
            assert multi[key] == localdev[key], (name, key)
        output['endpoint_identity'].append({'set': name, 'all_regenerated_capacities_and_node_signs_vs_developer_working_record': 'IDENTICAL'})
        enclosure_count += sum(check_enclosures(v) for v in [upper, one, multi])
        output['upper_runs'].append(upper)
        output['coherent_node_runs'].append(one)
        compressed = {k: v for k, v in multi.items() if k != 'target_capacity_exact'}
        compressed['regenerated_capacity_count'] = len(multi['target_capacity_exact'])
        compressed['target_capacity_canonical_json_sha256'] = canonical_hash(multi['target_capacity_exact'])
        compressed['working_artifact'] = identity(multipath)
        output['multinode_runs'].append(compressed)
        lower = Fraction(multi['explicit_greedy_sign_lower_squared']['exact'])
        upperq = Fraction(upper['upper_squared']['exact'])
        coherent = Fraction(one['lower_squared']['exact'])
        ratio = lower/upperq
        expected_ratio = Fraction(multi['expected_random_sign_lower_squared']['exact'])/upperq
        assert lower >= Fraction(multi['expected_random_sign_lower_squared']['exact'])
        assert (ratio > 100) == (name == 'triangle')
        assert ratio > 49
        if name == 'triangle':
            assert ratio > 640000 and coherent/upperq > 100000
        output['exact_decisions'].append({
            'set': name, 'squared_greedy_lower_over_full_upper_exact': str(ratio),
            'squared_greedy_lower_over_full_upper_display': float(ratio),
            'squared_expected_lower_over_full_upper_display': float(expected_ratio),
            'greater_than_100': ratio > 100, 'greater_than_49': ratio > 49,
            'greater_than_640000': ratio > 640000,
            'coherent_node_squared_ratio_display': float(coherent/upperq),
            'decisions_use_exact_rational_cross_comparison': True,
        })
        for path, item in [(upperpath, upper), (onepath, one), (multipath, multi)]:
            output['commands'].append('PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python ' + item['command'])
            output['local_artifact_manifest'].append(identity(path))
        signpath = independent/f'cgs2-sign-check-{name}.json'
        sign = json.loads(signpath.read_text())
        assert sign['result'] == 'PASS'
        assert sign['input_sha256'] == identity(multipath)['sha256']
        output.setdefault('independently_executed_projection_checks', []).append(sign)
        output['commands'].append(f'PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e1_sign_check.py --input {multipath} --output {signpath}')
        output['local_artifact_manifest'].append(identity(signpath))
    graphpath = independent/'cgs2-localgraph-verify.json'
    graph = json.loads(graphpath.read_text())
    developergraphpath = evidence/'e1-cgs2-graph-verification.json'
    assert graph['checks'] == json.loads(developergraphpath.read_text())['checks']
    assert all(row['result'] == 'PASS' for row in graph['checks'])
    output['independently_executed_local_primitive_check'] = graph
    output['local_primitive_check_label_correction'] = 'Producer raw status is fixed developer wording. This artifact was freshly executed by the independent agent, covering local primitive gradients only, not the complete normalized trajectory.'
    output['commands'].append(f'PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python tracks/bivariate-lanczos/code/drift/e1_cgs2_verify.py --output {graphpath}')
    output['local_artifact_manifest'].append(identity(graphpath))
    output['rational_square_root_enclosures_checked'] = enclosure_count
    output['verdict'] = 'Full scalar-model factor-ten comparison remains INCONCLUSIVE; triangle certified, rotated lower/upper ratio <100 is no refutation. Post-hoc >7 bothsets and >800 triangle endpoints reproduce.'
    code = root/'tracks/bivariate-lanczos/code/drift'
    theory = root/'tracks/bivariate-lanczos/theory'
    paths = [code/n for n in ['e1_exact.py', 'e1_cgs2.py', 'e1_cgs2_witness.py', 'e1_cgs2_multinode.py', 'e1_cgs2_verify.py', 'e1_sign_check.py', 'e1_reproduce.py', 'check_independent_scalar.py']]
    paths += [scalarpath, compactpath, developergraphpath]
    paths += sorted(theory.glob('drift-codex-*.md'))
    paths += [root/'topics/padua-lanczos-drift-20261101/directions/E1.md']
    for path in paths:
        output['inputs'].append(identity(path))
    output['cold_storage'] = 'Working artifact paths are temporary; essential exact endpoints, source definitions and sign vectors are retained here. Full capacities are reproducible from committed code and identified by their canonical content hash; no permanent archive claim.'
    Path(args.output).write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({'result': 'PASS', 'output': args.output,
                      'bytes': Path(args.output).stat().st_size,
                      'enclosures_checked': enclosure_count,
                      'verdict': output['verdict']}))


if __name__ == '__main__':
    main()
