"""Metadata-only completion of the preserved D12 independent replay.

No native loader, compiler, subprocess, point oracle or author checker import.
The prior worker executed run.py; this helper only validates retained records.
"""
import hashlib
import json
import pathlib
import resource
import sys

sys.dont_write_bytecode = True
from verify import strict_json, geometry, endpoints, corner, predicates, Q

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
TOPIC = HERE.parents[1]
EVIDENCE = TOPIC / 'evidence'
SOURCE = HERE.parent / 'post_audit_D11_point_cover'
RAW = ROOT / 'local-output/argmax-bridge-20261105/post-audit-D12/result-review'
PRIMARY = ROOT / 'local-output/argmax-bridge-20261105/post-audit-D11/point-cover'
OUTPUT = EVIDENCE / 'd12-review-point-cover.json'
cache = {}
checked_rows = 0


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def encoded(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode()


def identity(path):
    p = pathlib.Path(path)
    p = (p if p.is_absolute() else ROOT / p).resolve()
    if p not in cache:
        b = p.read_bytes()
        cache[p] = dict(path=str(p), bytes=len(b), sha256=hashlib.sha256(b).hexdigest())
    return cache[p]


def compact(path):
    r = identity(path)
    p = pathlib.Path(r['path'])
    return [str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p), r['bytes'], r['sha256']]


def check(row):
    global checked_rows
    got = identity(row['path'])
    assert (got['bytes'], got['sha256']) == (row['bytes'], row['sha256']), row['path']
    checked_rows += 1


def all_identities(value):
    if isinstance(value, dict):
        if {'path', 'bytes', 'sha256'} <= value.keys():
            check(value)
        for item in value.values():
            all_identities(item)
    elif isinstance(value, list):
        for item in value:
            all_identities(item)


def read(path):
    return strict_json(path, limit=1048576)


def pinned(path, digest):
    assert identity(path)['sha256'] == digest, str(path)
    return read(path)


def mapping_paths(path):
    paths = set()
    for line in path.read_text().splitlines():
        parts = line.split(maxsplit=5)
        if len(parts) == 6 and parts[5].startswith('/'):
            assert not parts[5].endswith(' (deleted)')
            paths.add(str(pathlib.Path(parts[5]).resolve()))
    return paths


def runtime(build, before, after, before_maps, after_maps, mapped_key, linked_key):
    all_identities(build)
    all_identities(before)
    all_identities(after)
    assert before[mapped_key] == after[mapped_key]
    assert before[linked_key] == after[linked_key]
    mapped = {r['path']: r for r in before[mapped_key]}
    assert len(mapped) == len(before[mapped_key])
    assert set(mapped) == mapping_paths(before_maps) == mapping_paths(after_maps)
    for expected in build['linked_dependency_closure']:
        matches = [r for p, r in mapped.items() if pathlib.Path(p).name == pathlib.Path(expected['path']).name]
        assert matches
        assert all((r['bytes'], r['sha256']) == (expected['bytes'], expected['sha256']) for r in matches)
    assert all(r['path'] in mapped for r in before[linked_key])
    return dict(mapped_files=len(mapped), linked_files=len(before[linked_key]),
                toolchain=len(build['toolchain']), tool_dependencies=len(build['toolchain_dependency_closure']),
                headers=len(build['headers']), dependency_inputs=len(build.get('dependency_inputs', [])))


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
    assert sys.argv[1:] == ['--metadata-once']
    assert not OUTPUT.exists(), 'essential review receipt already exists'
    freeze = pinned(HERE/'FREEZE.json', '8590610974cfdc5d2f7c78e85329028f4537e66be07f93724d4577482e060305')
    all_identities(freeze['files'])
    author_freeze = pinned(SOURCE/'FREEZE.json', '3c361e44db34babd168cdca0c785fe101abb80c5441cbf9e1c7314e52c73c8c1')
    all_identities(author_freeze['code_data'])
    all_identities(read(SOURCE/'SOURCES.json')['immutable_code_data_dependencies'])
    author = pinned(EVIDENCE/'d12-point-cover.json', '5404f0b9679db125640ece212c85f86dfa7cfac13a41a9956c290e2804fe33c4')
    all_identities(author)
    tree = pinned(EVIDENCE/'d12-point-cover-tree.json', '62a0f35a51730ab57b0a0931122b9cab7c6ca1d113ea38dc779a059ade3eda2e')
    registration = read(RAW/'registration.json')
    assert registration['freeze'] == identity(HERE/'FREEZE.json')
    assert registration['cap_cpu'] == 120 and registration['no_retry'] is True and registration['subreaper'] == 1
    state, accounting = read(RAW/'checkpoint.json'), read(RAW/'final-accounting.json')
    assert state['status'] == 'COMPLETE' and state['active_call'] is None and 'first_failure' not in state
    assert accounting['passed'] is True and accounting['accounting_complete'] is True
    assert accounting['returncode'] == 0 and accounting['first_failure'] is None
    assert accounting['inclusive_cpu_through_sample'] == 41.464729
    assert accounting['wall_seconds'] < registration['wall_cap']
    assert (RAW/'stdout').stat().st_size == (RAW/'stderr').stat().st_size == 0
    lower, witness = corner(read(EVIDENCE/'d09-threepoint.json'))
    assert str(lower) == '7112277937770225/281474976710656'
    assert str(lower) == state['lower'] and witness == state['witness']
    leaves, points, depth = geometry(tree)
    assert (len(tree['preorder']), len(leaves), len(points), depth) == (83, 42, 53, 12)
    rows = []
    for entry in state['completed']:
        assert entry['returncode'] == 0 and 0 <= entry['cpu'] <= registration['completed_call']
        row = entry['row']
        assert len(row) == 4 and len(row[3]) == 6
        assert all(type(x) is int and x >= 0 for x in row[3])
        assert all(str(Q(x)) == x for x in row[:2])
        assert endpoints(row[2])[0] >= 0
        rows.append(row)
    assert [(Q(r[0]), Q(r[1])) for r in rows] == points
    summary, details = predicates(leaves, rows, lower)
    assert summary == state['summary']
    assert details == read(RAW/'leaves.json')
    assert summary['leaf_counts'] == {'NEAR': 8, 'FAR': 31, 'OUTSIDE': 3}
    assert summary['minimum_margin'] == {
        'FAR': '935713367702180327/453712364894045601792',
        'NEAR': '19706796211663228105/3629698919152364814336'}
    av = author['verification']
    assert summary['leaf_counts'] == av['leaf_counts']
    assert summary['minimum_margin'] == av['minimum_strict_margin_by_required_predicate']
    assert av['nodes'] == 83 and av['leaves'] == 42 and av['distinct_canonical_vertices'] == 53 and av['max_depth'] == 12
    sums = [sum(row[3][i] for row in rows) for i in range(6)]
    maxima = [max(row[3][i] for row in rows) for i in range(6)]
    assert sums == av['native_count_sums'] and maxima == av['native_count_maxima']
    old = read(PRIMARY/'checker-checkpoint.json')
    assert old['status'] == 'COMPLETE' and old['active_call'] is None
    oldrows = {r['key']: r['native'] for r in old['completed_calls']}
    assert len(oldrows) == len(old['completed_calls']) == 53
    for row in rows:
        prior = oldrows[row[0]+','+row[1]]
        assert (row[2], row[3], 0) == (prior['raw_hex'], prior['counts'], prior['returncode'])
    assert state['author_comparison'] == 'all 53 endpoint/radius hex triples and six-counter vectors exactly equal'
    build = read(RAW/'build.json')
    closure_counts = {'review': runtime(build, read(RAW/'runtime-before.json'), read(RAW/'runtime-after.json'),
                                      RAW/'before.maps', RAW/'after.maps', 'mapped', 'linked')}
    for stage in ('producer', 'checker'):
        b = read(PRIMARY/(stage+'-build.json'))
        closure_counts[stage] = runtime(b, read(PRIMARY/(stage+'-runtime-before.json')),
                                       read(PRIMARY/(stage+'-runtime-after.json')),
                                       PRIMARY/(stage+'-loaded-before.maps'), PRIMARY/(stage+'-loaded-after.maps'),
                                       'all_file_mappings', 'loaded')
        supervisor = read(PRIMARY/(stage+'-supervisor.json'))
        assert supervisor['returncode'] == 0 and supervisor['stop'] is None
        assert supervisor['accounting_complete'] is True and supervisor['complete'] is True
        assert supervisor['inclusive_CPU_with_supervision'] == author['CPU'][stage+'_inclusive']
    primary_accounting = read(PRIMARY/'final-accounting.json')
    assert primary_accounting['complete'] is True
    assert primary_accounting['total_CPU_through_summary'] == author['CPU']['primary_through_summary_sample']
    author_build = read(PRIMARY/'checker-build.json')
    assert build['checker_binary']['path'] != author_build['checker_binary']['path']
    assert build['checker_binary']['sha256'] != author_build['checker_binary']['sha256']
    assert build['source_snapshot']['sha256'] == author_build['source_snapshot']['sha256']
    raw_names = ['registration.json', 'checkpoint.json', 'build.json', 'runtime-before.json', 'runtime-after.json',
                 'final-accounting.json', 'leaves.json', 'before.maps', 'after.maps', 'stdout', 'stderr']
    raw_records = [[name, *compact(RAW/name)[1:]] for name in raw_names]
    identity(HERE/'summarize.py')
    unique = sorted((str(p), r['bytes'], r['sha256']) for p, r in cache.items())
    result = dict(
        status='PASS saved-data completion of successful independent fresh native replay; theorem accepted in companion report',
        release_commit=freeze['source_commit'],
        provenance=dict(native_worker='/root/d12_cover_result_review', native_model_requested='gpt-6-astra xhigh',
                        completion_worker='/root/d12_review_finish', serving_metadata='independently unexposed',
                        completion_scope='metadata/source/exact-arithmetic review only; zero new native calls',
                        native_command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D12_result_review/run.py --released-once',
                        completion_command='PYTHONDONTWRITEBYTECODE=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D12_result_review/summarize.py --metadata-once'),
        identities={key: compact(path) for key, path in [
            ('review_freeze', HERE/'FREEZE.json'), ('review_run', HERE/'run.py'), ('review_verify', HERE/'verify.py'),
            ('postprocessor', HERE/'summarize.py'), ('author_freeze', SOURCE/'FREEZE.json'),
            ('author_sources', SOURCE/'SOURCES.json'), ('author_receipt', EVIDENCE/'d12-point-cover.json'),
            ('tree', EVIDENCE/'d12-point-cover-tree.json'), ('D09_corner', EVIDENCE/'d09-threepoint.json')]},
        native_build={key: build[key] for key in ['compiler_version', 'source_snapshot', 'preprocessed_translation_unit', 'checker_binary']},
        verification=dict(nodes=83, internal_nodes=41, leaves=42, max_depth=depth, distinct_points=53,
                          **summary, corner_lower=str(lower), corner_epsilon_lower=witness['epsilon_lower'],
                          author_comparison='all 53 complete interval/radius hex triples and six-counter vectors equal',
                          count_columns=av['native_count_columns'], count_sums=sums, count_maxima=maxima,
                          maximum_native_call_cpu=max(e['cpu'] for e in state['completed']),
                          identity_records_checked=checked_rows, unique_files_read=len(cache),
                          enumerated_identity_digest=hashlib.sha256(encoded(unique)).hexdigest(),
                          closure_counts=closure_counts),
        CPU=dict(prior_replay_through_sample=accounting['inclusive_cpu_through_sample'], prior_wall=accounting['wall_seconds'],
                 prior_accounting_complete=True, metadata_hard_cap=2, aggregate_allocation=120,
                 primary_producer=author['CPU']['producer_inclusive'], primary_checker=author['CPU']['checker_inclusive'],
                 primary_through_summary=author['CPU']['primary_through_summary_sample'],
                 note='CPU samples precede final tiny writes; native supervisor/metadata hard limits remain explicit'),
        row_format=['alpha_over_pi', 'beta_over_pi', ['lower_hex', 'upper_hex', 'radius_hex'], av['native_count_columns']],
        rows=rows, raw_directory=str(RAW.relative_to(ROOT)), raw_artifacts=raw_records,
        limits='Observed compiler/header/linked/mapped closure only; no hermeticity. Native trust inherits accepted C11/D07 arithmetic and Arb/FLINT/GMP/MPFR. Full raw retained locally, permanent cold-storage pending. Frozen primary/replay commands consumed; no retry. Final Claude audit separate.')
    result['CPU']['metadata_before_serialization'] = cpu()
    assert accounting['inclusive_cpu_through_sample'] + 2 < 120
    data = encoded(result)
    assert len(data) < 16384, len(data)
    assert cpu() < 1.9, 'metadata reserve'
    with OUTPUT.open('xb') as stream:
        stream.write(data)
    print(json.dumps(dict(status='PASS', bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                          metadata_cpu_through_write=cpu(), identity_records_checked=checked_rows,
                          unique_files_read=len(cache), closure_counts=closure_counts)))


if __name__ == '__main__':
    main()
