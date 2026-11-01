"""Two-stage execution of the immutable N8 verifier; no new math predicate."""
import argparse
import ast
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import signal
import tempfile
import time

MAIN_SHA = 'a9cff5748d6c40ee41ac76e4e8a0035e0d5dab95f4de1233dfcc26902cb085a2'
CONTROLS_SHA = '7f57ed9ba5ad864391aa2e309834d9b61c33f673a6854247d44594cb10ec71d2'
TAIL_AST_SHA = '14ec9c77c3afef4d585b3017a0d3b2f32f6cf0b705ff73c188fea92f4c2be7a5'
HERE = Path(__file__).resolve()
MAIN_PATH = HERE.with_name('a5_checker_n8.py')
CONTROLS_PATH = HERE.with_name('a5_checker_n8_controls.py')

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

DRIVER_SHA_AT_IMPORT = sha(HERE.read_bytes())
if sha(MAIN_PATH.read_bytes()) != MAIN_SHA:
    raise RuntimeError('frozen main changed before import')
import a5_checker_n8 as check

require = check.require
BOUNDARY_KEYS = {'edges', 'corners', 'boundary_summary'}
SUMMARY_CHANGES = {'complete', 'edge', 'corner', 'total'}
NODE_RESULT_KEYS = ('node_status_counts', 'verified_node_records',
                    'verified_direction_breakpoints', 'accepted_node_cones')
READY_KEYS = {'format', 'interior_sha256', 'certificate_path',
              'certificate_sha256', 'global_path', 'global_sha256'}

def canonical(value):
    # Typed JSON equality: unlike Python ==, this separates true/1 and 1/1.0.
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      allow_nan=False).encode()

def guard_sources():
    require(sha(MAIN_PATH.read_bytes()) == MAIN_SHA == check.SOURCE_SHA_AT_IMPORT,
            'frozen main source changed')
    require(sha(CONTROLS_PATH.read_bytes()) == CONTROLS_SHA, 'frozen controls changed')
    require(sha(HERE.read_bytes()) == DRIVER_SHA_AT_IMPORT, 'staged driver source changed')

def extracted_tail(source=None):
    """Compile the literally unchanged original run tail, with explicit locals."""
    raw = MAIN_PATH.read_bytes() if source is None else source
    require(sha(raw) == MAIN_SHA, 'tail source is not the frozen main')
    module = ast.parse(raw)
    cls = next(n for n in module.body if isinstance(n, ast.ClassDef) and n.name == 'Verifier')
    run = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == 'run')
    start = next(i for i, n in enumerate(run.body) if isinstance(n, ast.Assign) and
                 any(isinstance(t, ast.Name) and t.id == 'no_unresolved' for t in n.targets))
    body = copy.deepcopy(run.body[start:])
    tree = ast.Module(body=body, type_ignores=[])
    require(sha(ast.dump(tree, include_attributes=False).encode()) == TAIL_AST_SHA,
            'original run tail AST changed')
    wrapper = ast.parse('def frozen_run_tail(self, certificate, allow_partial, node_result, leaves, complete_partition):\n pass\n').body[0]
    wrapper.body = body
    program = ast.fix_missing_locations(ast.Module(body=[wrapper], type_ignores=[]))
    namespace = dict(vars(check))
    exec(compile(program, '<unchanged-a5-n8-run-tail>', 'exec'), namespace)
    return namespace['frozen_run_tail']

def validate_interior_input(data):
    require(not BOUNDARY_KEYS.intersection(data), 'stage1 already contains boundary data')
    require(data.get('pending_paths') == [] and data.get('unresolved') == [],
            'stage1 has pending or unresolved regions')
    require(data['summary'].get('complete') is False and
            data['summary'].get('interior_complete') is True, 'wrong stage1 completeness')
    require(isinstance(data.get('metadata'), dict) and
            'mechanical_join' not in data['metadata'], 'wrong original interior metadata')

def validate_final_interior(original, final, interior_sha, interior_bytes):
    require(set(final) == set(original) | BOUNDARY_KEYS, 'final top-level fields changed')
    for key in original:
        if key not in {'summary', 'metadata'}:
            require(canonical(original[key]) == canonical(final[key]),
                    'interior field changed: ' + key)
    old, new = original['summary'], final['summary']
    require(set(new) == set(old) | {'edge', 'corner', 'total'}, 'final summary keys changed')
    require(new.get('complete') is True, 'final complete flag absent')
    for key in old:
        if key not in SUMMARY_CHANGES:
            require(canonical(old[key]) == canonical(new[key]), 'interior summary changed: ' + key)
    old, new = original['metadata'], final['metadata']
    require(set(new) == set(old) | {'mechanical_join'}, 'metadata keys changed beyond join provenance')
    for key in old:
        if key != 'source_sha256':
            require(canonical(old[key]) == canonical(new[key]), 'interior metadata changed: ' + key)
    require(valid_sha(new['source_sha256']), 'invalid join source identity')
    join = new['mechanical_join']
    required = {'interior_input_sha256', 'interior_input_bytes', 'boundary_input_sha256',
                'boundary_input_bytes', 'interior_source_sha256', 'boundary_source_sha256', 'scope'}
    require(isinstance(join, dict) and required <= set(join) <= required | {'base_joiner_sha256'},
            'unsupported join provenance fields')
    require(join['interior_input_sha256'] == interior_sha and
            type(join['interior_input_bytes']) is int and join['interior_input_bytes'] == interior_bytes and
            join['interior_source_sha256'] == old['source_sha256'], 'join interior binding failed')
    require(all(valid_sha(join[k]) for k in join if k.endswith('sha256')) and
            type(join['boundary_input_bytes']) is int and join['boundary_input_bytes'] > 0 and
            isinstance(join['scope'], str), 'malformed join provenance')

def valid_sha(value):
    return isinstance(value, str) and len(value) == 64 and set(value) <= set('0123456789abcdef')

def load_json(raw):
    return json.loads(check.decode_payload(raw), object_pairs_hook=check.unique_object)

def load_ready(path, interior_sha):
    require(Path(path).is_file(), 'READY marker missing')
    ready_raw = Path(path).read_bytes()
    ready = load_json(ready_raw)
    require(isinstance(ready, dict) and set(ready) == READY_KEYS and
            ready['format'] == 'a5-n8-staged-ready-v1', 'invalid READY schema')
    require(ready['interior_sha256'] == interior_sha, 'READY binds a different interior')
    for key in ('certificate_sha256', 'global_sha256'):
        require(valid_sha(ready[key]), 'invalid READY hash')
    require(all(isinstance(ready[k], str) and ready[k] for k in ('certificate_path', 'global_path')),
            'invalid READY paths')
    cert_raw = Path(ready['certificate_path']).read_bytes()
    global_raw = Path(ready['global_path']).read_bytes()
    require(sha(cert_raw) == ready['certificate_sha256'] and
            sha(global_raw) == ready['global_sha256'], 'READY raw pair hash mismatch')
    return ready, ready_raw, cert_raw, global_raw

def atomic_json(path, value):
    path = Path(path)
    payload = json.dumps(value, indent=2, sort_keys=True, allow_nan=False).encode() + b'\n'
    if path.exists():
        require(path.read_bytes() == payload, 'refusing to replace an existing different receipt')
        return
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.resolve().parent, prefix=path.name + '.',
                                         suffix='.tmp', delete=False) as stream:
            temporary = stream.name
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            os.unlink(temporary)

def check_deadline(deadline):
    require(datetime.now(timezone.utc) < deadline, 'staged deadline reached')

def interrupted(signum, frame):
    raise TimeoutError('staged execution interrupted or deadline reached')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for option in ('interior', 'interior-sha256', 'ready-file', 'interior-output', 'output', 'deadline-utc'):
        parser.add_argument('--' + option, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    result = {'format': 'a5-n8-staged-result-v1', 'stage': 'starting', 'accepted': False,
              'count_certified': False, 'driver_sha256': DRIVER_SHA_AT_IMPORT,
              'checker_sha256': MAIN_SHA, 'controls_sha256': CONTROLS_SHA,
              'tail_ast_sha256': TAIL_AST_SHA, 'python': check.platform.python_version(),
              'sympy': check.sp.__version__, 'python_flint': check.flint.__version__,
              'FLINT': check.flint.__FLINT_VERSION__, 'precision': check.PRECISION,
              'trusted_dependencies': ['frozen independent N8 Verifier', 'CPython exact integers/Fraction',
                                       'SymPy exact algebra', 'python-flint exact arithmetic']}
    try:
        guard_sources()
        tail = extracted_tail()
        require(Path(args.output).resolve() != Path(args.interior_output).resolve(), 'stage receipt paths coincide')
        deadline = datetime.fromisoformat(args.deadline_utc.replace('Z', '+00:00'))
        require(deadline.tzinfo is not None, 'deadline must include UTC offset')
        check_deadline(deadline)
        signal.signal(signal.SIGALRM, interrupted)
        signal.signal(signal.SIGTERM, interrupted)
        signal.setitimer(signal.ITIMER_REAL, (deadline - datetime.now(timezone.utc)).total_seconds())
        raw = Path(args.interior).read_bytes()
        require(valid_sha(args.interior_sha256) and sha(raw) == args.interior_sha256, 'wrong interior raw hash')
        original = load_json(raw)
        validate_interior_input(original)
        result.update(interior_path=args.interior, interior_sha256=sha(raw), interior_bytes=len(raw))
        verifier = check.Verifier(original['field_embedding'])
        interior_result = verifier.run(original, allow_partial=True)
        require(interior_result['complete_prefix_partition'] is True and
                interior_result['interior_complete'] is True and
                interior_result['count_certified'] is False and interior_result['boundary_complete'] is False,
                'stage1 did not verify a complete interior-only partition')
        require(interior_result['verified_interior_maxima_enclosures'] == len(original['interior_roots']) ==
                original['summary']['interior'], 'stage1 root accounting mismatch')
        node_result = {key: interior_result[key] for key in NODE_RESULT_KEYS}
        guard_sources()
        result.update(interior_result)
        result.update(stage='interior_verified', scope='interior-only; boundary/global pending',
                      seconds=time.monotonic() - started, driver_source_unchanged=True,
                      checker_source_unchanged=True, controls_source_unchanged=True)
        atomic_json(args.interior_output, result)
        print(json.dumps({'stage': 'interior_verified', 'interior_output': args.interior_output,
                          'verified_leaves': interior_result['verified_leaves'],
                          'verified_interior_roots': len(verifier.roots), 'count_certified': False}), flush=True)
        while not Path(args.ready_file).is_file():
            check_deadline(deadline)
            guard_sources()
            time.sleep(1)
        check_deadline(deadline)
        ready, ready_raw, cert_raw, global_raw = load_ready(args.ready_file, sha(raw))
        final, global_data = load_json(cert_raw), load_json(global_raw)
        validate_final_interior(original, final, sha(raw), len(raw))
        guard_sources()
        # EXACT original tail; all preceding mathematical state was verified
        # by the original run and all reused input fields are typed-identical.
        complete_result = tail(verifier, final, False, node_result, final['leaves'], True)
        global_result = verifier.global_values(final, global_data, sha(cert_raw), complete_result)
        require(complete_result['count_certified'] is True, 'original tail did not certify full coverage')
        require(sha(Path(ready['certificate_path']).read_bytes()) == sha(cert_raw) and
                sha(Path(ready['global_path']).read_bytes()) == sha(global_raw) and
                sha(Path(args.interior).read_bytes()) == sha(raw), 'verified input files changed during execution')
        check_deadline(deadline)
        guard_sources()
        result.update(complete_result)
        result.update(global_result)
        result.update(stage='complete', scope='complete count/global via exact original staged predicates',
                      certificate_sha256=sha(cert_raw), certificate_bytes=len(cert_raw),
                      global_certificate_sha256=sha(global_raw), global_certificate_bytes=len(global_raw),
                      ready_sha256=sha(ready_raw), ready=ready, seconds=time.monotonic() - started,
                      driver_sha256_after=sha(HERE.read_bytes()), checker_sha256_after=sha(MAIN_PATH.read_bytes()),
                      controls_sha256_after=sha(CONTROLS_PATH.read_bytes()))
        signal.setitimer(signal.ITIMER_REAL, 0)
        atomic_json(args.output, result)
        print(json.dumps(result, sort_keys=True), flush=True)
        return 0
    except Exception as error:
        signal.setitimer(signal.ITIMER_REAL, 0)
        result.update(accepted=False, count_certified=False, stage='failed', error=str(error),
                      scope='no complete count/global acceptance', seconds=time.monotonic() - started,
                      driver_sha256_after=sha(HERE.read_bytes()), checker_sha256_after=sha(MAIN_PATH.read_bytes()),
                      controls_sha256_after=sha(CONTROLS_PATH.read_bytes()))
        atomic_json(args.output, result)
        print(json.dumps(result, sort_keys=True), flush=True)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
