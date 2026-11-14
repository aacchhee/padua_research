"""Synthetic records for operational validation; no scientific source imported."""
import hashlib
import json
from pathlib import Path
import sys

ENGINE = 'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine'
def blob(data): return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
def put(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True) + '\n')
    return ident(path)
def ident(path): return dict(path=str(Path(path).resolve()), **blob(Path(path).read_bytes()))
def make_pass(root, group, n, mode, manifest):
    root = Path(root); base = root / 'outputs' / group / 'jobs' / str(n) / mode
    base.mkdir(parents=True)
    original = base.parent / 'produce/essential-receipt.json'
    config = {'n': n, 'mode': mode, 'output': str(base), 'certificate': str(original) if mode == 'verify' else None,
              'certificate_identity': ident(original) if mode == 'verify' else None}
    if mode == 'verify': (base / 'original-certificate.json').write_bytes(original.read_bytes())
    frozen = ident(root / ENGINE / 'FREEZE.json')
    check = {'n': n, 'status': 'COMPLETE', 'active_call': None, 'certificate': {'fixture': 'NO_SCIENCE'},
             'retained_S_upper_rows': [['0', '0', '0x1.0000000000000p+1']],
             'origin_lower_hex': '0x1.0000000000000p+0', 'verification': {'fixture': 'NO_SCIENCE'},
             'norm_selection': {'selected': 'GRID', 'M': '2'}, 'actual_points': [], 'completed_calls': []}
    for api, keys in [('S', [('0', '0')]), ('lambda', [('1', '0'), ('0', '1'), ('1', '1')] if n < 256 else [])]:
        for key in keys:
            check['completed_calls'].append({'n': n, 'api': api, 'key': list(key),
                 'native': {'returncode': 0, 'raw_hex': ['0x1.0000000000000p+0', '0x1.0000000000000p+1', '0x0.0p+0']},
                 'point': {'lower': '1', 'upper': '2'}})
            if api == 'lambda': check['actual_points'].append({'key': list(key), 'upper_hex': '0x1.0000000000000p+1'})
    checkpoints = {'checker': check, 'controls': {'status': 'COMPLETE', 'fixture': 'NO_SCIENCE'}}
    stages = []
    for stage in ['controls', 'checker']:
        cid = put(base / (stage + '-checkpoint.json'), checkpoints[stage])
        row = {'stage': stage, 'checkpoint': cid, 'returncode': 0, 'stop': None, 'complete': True,
               'accounting_complete': True, 'first_failure': None, 'inclusive_CPU_with_supervision': 0.001}
        stages.append(row); put(base / (stage + '-supervisor.json'), row)
        put(base / (stage + '-descendants.json'), {'complete': True})
        put(base / (stage + '-entry.json'), {'engine_config': config})
        (base / (stage + '.stdout')).write_bytes(b''); (base / (stage + '.stderr')).write_bytes(b'')
    native = root / 'fixture-native-source'; source = ident(native)
    builds = {'S': None, 'lambda': None}; loaded = {}
    for api in (['S', 'lambda'] if n < 256 else ['S']):
        tu = base / (api + '.ii'); tu.write_bytes(b'NO_SCIENCE_TU\n')
        binary = base / (api + '.so'); binary.write_bytes(b'NOT_AN_EXECUTABLE\n')
        build = {'kernel_variant': api, 'source_origin': str(native), 'source_snapshot': source,
                 'preprocessed_translation_unit': ident(tu), 'checker_binary': ident(binary)}
        for key in ['toolchain', 'toolchain_dependency_closure', 'headers', 'dependency_inputs', 'linked_dependency_closure']:
            build[key] = [source]
        builds[api] = build; put(base / (api + '-build.json'), build); loaded[api] = [source]
    runtime = {'loaded': loaded, 'all_file_mappings': []}
    for label in ['before', 'after']:
        put(base / ('runtime-' + label + '.json'), runtime); (base / ('loaded-' + label + '.maps')).write_bytes(b'')
    raw = {'format': 'FINAL-HYBRID-whole-raw-evidence-v1', 'engine_config': config, 'freeze': frozen,
           'checkpoint': check, 'controls_checkpoint': checkpoints['controls'], 'stages': stages,
           'builds': builds, 'runtime_before': runtime, 'runtime_after': runtime, 'maps_before': '', 'maps_after': '',
           'original_certificate': json.loads(original.read_bytes()) if mode == 'verify' else None}
    raw_id = put(base / 'raw-evidence.json', raw)
    receipt = {'fixture': 'NO_SCIENCE', 'freeze': frozen, 'n': n, 'verification': check['verification'],
               'whole_raw_evidence': raw_id, 'tree': check['certificate'], 'S_upper_rows': check['retained_S_upper_rows'],
               'origin_lower_hex': check['origin_lower_hex'], 'lambda_upper_rows': [[*r['key'], r['upper_hex']] for r in check['actual_points']],
               'norm': {'method': 'GRID', 'M': '2'}, 'CPU_stages': stages}
    put(base / 'essential-receipt.json', receipt)
    put(base / 'preregistration.json', {'engine_config': config, 'freeze': frozen})
    put(base / 'summary.json', {'engine_config': config, 'result': 'PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING',
         'first_failure': None, 'freeze': frozen, 'whole_raw_evidence': raw_id, 'stages': stages})
    labels = {'produce': 'EXACT_SINGLE_DEGREE_PRIMARY_ACCEPTED_PENDING_FRESH_VERIFY',
              'verify': 'FRESH_RETAINED_PROOF_VERIFY_ACCEPTED_PENDING_RESULT_REVIEW'}
    put(base / 'final-accounting.json', {'engine_config': config, 'result': labels[mode], 'complete': True,
         'first_failure': None, 'hard_aggregate_cap': 120, 'total_CPU_through_summary': 0.01,
         'final_self_limit': {'no_live_children': True, 'waited_child_CPU': 0.001, 'absolute_self_CPU_hard': 118}})
    command = [sys.executable, '-E', '-S', '-B', str(root / ENGINE / 'engine.py'), '--mode', mode, '--n', str(n), '--output', str(base), '--run-once']
    if mode == 'verify': command += ['--certificate', str(original)]
    record = {'mode': mode, 'command': command, 'observed_returncode': 0, 'cleanup_killed': [], 'ECHILD': True}
    put(base.parent / (mode + '-exit.json'), record)
    return record

def make_attempt(root, group, n, run, started=True):
    base = Path(root) / 'outputs' / group / 'jobs' / str(n); base.mkdir(parents=True, exist_ok=True)
    if started: put(base / 'started.json', {'n': n, 'identity': run['identity'], 'core': run['provenance']['selected_cores'][0]})
    records = [make_pass(root, group, n, mode, run['manifest']) for mode in ['produce', 'verify']]
    put(base / 'attempt.json', {'n': n, 'terminal': True, 'failure': None, 'ECHILD': True, 'cleanup_killed': [],
                             'status': 'awaits_independent_result_review', 'passes': records})
    put(base / 'wrapper-exit.json', {'observed_returncode': 0})
