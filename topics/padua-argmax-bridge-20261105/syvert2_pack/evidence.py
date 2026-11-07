"""Shared data-only validation of one pass/attempt, including portable raw closure.
Local execution may capture already identified external bytes into SHA objects.
Return validation uses only trusted local checker code and archived payload bytes.
"""
import importlib.util
import fcntl
import os
from pathlib import Path, PurePosixPath
from common import digest, strict, encoded
from plans import ENGINE, plan
from ownership import validate_domain
LABELS = {'produce': 'EXACT_SINGLE_DEGREE_PRIMARY_ACCEPTED_PENDING_FRESH_VERIFY',
          'verify': 'FRESH_RETAINED_PROOF_VERIFY_ACCEPTED_PENDING_RESULT_REVIEW'}

def require(condition, message):
    if not condition: raise ValueError(message)

def safe(name):
    p = PurePosixPath(name)
    require(not p.is_absolute() and '..' not in p.parts and str(p) == name, 'unsafe portable payload path')
    return name

def identities(value):
    if isinstance(value, dict):
        if {'path', 'bytes', 'sha256'} <= set(value): yield {k: value[k] for k in ('path', 'bytes', 'sha256')}
        for child in value.values(): yield from identities(child)
    elif isinstance(value, list):
        for child in value: yield from identities(child)

class Access:
    def __init__(self, package, root_absolute, read_bytes=None, capture=False):
        self.package = Path(package).resolve(); self.absolute = PurePosixPath(root_absolute)
        require(self.absolute.is_absolute() and '..' not in self.absolute.parts, 'registered absolute package root')
        self.reader = read_bytes or (lambda name: (self.package / safe(name)).read_bytes())
        self.capture = capture
        spec = importlib.util.spec_from_file_location('released_data_checker', self.package / ENGINE / 'checker.py')
        self.checker = importlib.util.module_from_spec(spec); spec.loader.exec_module(self.checker)
    def data(self, name): return self.reader(safe(name))
    def json(self, name): return strict(self.data(name))
    def identity(self, row):
        require(type(row.get('bytes')) is int and row['bytes'] > 0 and isinstance(row.get('sha256'), str) and
                len(row['sha256']) == 64 and all(c in '0123456789abcdef' for c in row['sha256']), 'artifact identity shape')
        p = PurePosixPath(row['path'])
        require(p.is_absolute() and '..' not in p.parts, 'artifact absolute source path')
        if p.is_relative_to(self.absolute):
            name = safe(p.relative_to(self.absolute).as_posix())
        else:
            name = 'preserved-sha256/' + row['sha256']
            if self.capture:
                destination = self.package / name
                with (self.package / '.preserve.lock').open('a+b') as lease:
                    fcntl.flock(lease, fcntl.LOCK_EX)
                    self._capture(row, destination)
            name = safe(name)
        data = self.data(name)
        require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'required retained artifact missing/changed: ' + name)
        return data
    def _capture(self, row, destination):
        if not destination.exists():
            data = Path(row['path']).read_bytes()
            require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'external bytes changed before capture')
            destination.parent.mkdir(parents=True, exist_ok=True)
            temp = destination.with_name(destination.name + '.tmp-' + str(os.getpid()))
            with temp.open('xb') as f: f.write(data); f.flush(); os.fsync(f.fileno())
            temp.replace(destination)
    def closure(self, value):
        for row in identities(value): self.identity(row)

def validate_pass(a, prefix, n, mode, manifest):
    summary = a.json(prefix + '/summary.json'); account = a.json(prefix + '/final-accounting.json')
    receipt_bytes = a.data(prefix + '/essential-receipt.json'); receipt = strict(receipt_bytes)
    require(len(receipt_bytes) < 16384, 'receipt cap')
    require(account.get('result') == LABELS[mode] and account.get('complete') is True and account.get('first_failure') is None,
            'complete final accounting required')
    config = account['engine_config']
    require(config['n'] == n and config['mode'] == mode and config == summary['engine_config'], 'account/summary configuration')
    require(config['output'] == str(a.absolute / prefix), 'registered output path mismatch')
    require(account.get('hard_aggregate_cap') == 120 and 0 <= account['total_CPU_through_summary'] < 120, 'whole accounting cap')
    limit = account['final_self_limit']
    require(limit['no_live_children'] is True and limit['waited_child_CPU'] + limit['absolute_self_CPU_hard'] <= 119, 'final whole descendant bound')
    require(summary['result'] == 'PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING' and summary.get('first_failure') is None, 'provisional summary')
    registration = a.json(prefix + '/preregistration.json')
    require(registration['engine_config'] == config and registration['freeze'] == receipt['freeze'] == summary['freeze'], 'registered frozen inputs')
    freeze = a.data(ENGINE + '/FREEZE.json')
    require(receipt['freeze']['sha256'] == digest(freeze) and receipt['freeze']['bytes'] == len(freeze), 'released numerical source')
    require(receipt['n'] == n and a.checker.verify_essential(receipt, receipt['freeze']) == receipt['verification'], 'exact rational proof reconstruction')
    require(receipt['whole_raw_evidence'] == summary['whole_raw_evidence'], 'receipt/summary raw linkage')
    raw = strict(a.identity(summary['whole_raw_evidence']))
    require(raw['format'] == 'FINAL-HYBRID-whole-raw-evidence-v1' and raw['engine_config'] == config and raw['freeze'] == receipt['freeze'], 'raw source/configuration')
    checkpoint = a.json(prefix + '/checker-checkpoint.json')
    require(raw['checkpoint'] == checkpoint and checkpoint['n'] == n and checkpoint['status'] == 'COMPLETE' and checkpoint['active_call'] is None, 'raw checkpoint closure')
    for rkey, ckey in [('tree', 'certificate'), ('S_upper_rows', 'retained_S_upper_rows'), ('origin_lower_hex', 'origin_lower_hex'), ('verification', 'verification')]:
        require(receipt[rkey] == checkpoint[ckey], 'receipt/checkpoint ' + rkey)
    require(receipt['lambda_upper_rows'] == [[*r['key'], r['upper_hex']] for r in checkpoint['actual_points']], 'actual retained linkage')
    require(receipt['norm'] == {'method': checkpoint['norm_selection']['selected'], 'M': checkpoint['norm_selection']['M']}, 'norm linkage')
    require(receipt['CPU_stages'] == summary['stages'] == raw['stages'] and [r['stage'] for r in summary['stages']] == ['controls', 'checker'], 'whole stage linkage')
    for stage, cap in [('controls', 2), ('checker', 100)]:
        row = next(r for r in summary['stages'] if r['stage'] == stage)
        require(row == a.json(prefix + '/' + stage + '-supervisor.json') and row['returncode'] == 0 and row['stop'] is None and
                row['complete'] is True and row['accounting_complete'] is True and row.get('first_failure') is None and
                0 <= row['inclusive_CPU_with_supervision'] <= cap, 'stage accounting')
        stage_checkpoint = a.json(prefix + '/' + stage + '-checkpoint.json')
        require(a.identity(row['checkpoint']) == a.data(prefix + '/' + stage + '-checkpoint.json'), 'stage checkpoint identity')
        if stage == 'controls': require(raw['controls_checkpoint'] == stage_checkpoint, 'controls raw linkage')
        require(a.json(prefix + '/' + stage + '-descendants.json')['complete'] is True, 'stage descendant reap')
        a.data(prefix + '/' + stage + '.stdout'); a.data(prefix + '/' + stage + '.stderr')
        entry = a.json(prefix + '/' + stage + '-entry.json')
        require(entry['engine_config'] == config, 'stage entry configuration'); a.closure(entry)
    calls = checkpoint['completed_calls']; by_key = {}
    for row in calls:
        key = (row['api'], tuple(row['key']))
        require(key not in by_key and row['n'] == n and row['native']['returncode'] == 0 and 'point' in row, 'native call closure')
        require(a.checker.exact_hex(row['native']['raw_hex'][0]) == a.checker.rational(row['point']['lower']) and
                a.checker.exact_hex(row['native']['raw_hex'][1]) == a.checker.rational(row['point']['upper']), 'native endpoint linkage')
        by_key[key] = row
    for x, y, upper in receipt['S_upper_rows']:
        require(by_key['S', (x, y)]['native']['raw_hex'][1] == upper, 'retained S/native linkage')
    require(by_key['S', ('0', '0')]['native']['raw_hex'][0] == receipt['origin_lower_hex'], 'origin/native linkage')
    for x, y, upper in receipt['lambda_upper_rows']:
        require(by_key['lambda', (x, y)]['native']['raw_hex'][1] == upper, 'retained actual/native linkage')
    expected_apis = ['S', 'lambda'] if n < 256 else ['S']
    require(set(raw['builds']) == {'S', 'lambda'}, 'raw build selector schema')
    for api in expected_apis:
        build = a.json(prefix + '/' + api + '-build.json')
        require(raw['builds'][api] == build and build['kernel_variant'] == api, 'raw/build linkage')
        origin = PurePosixPath(build['source_origin'])
        require(origin.is_relative_to(a.absolute), 'native source origin outside package')
        source_row = manifest['files'][origin.relative_to(a.absolute).as_posix()]
        require(all(build['source_snapshot'][k] == source_row[k] for k in ['bytes', 'sha256']), 'native compiled source/released bytes')
        for k in ['source_snapshot', 'preprocessed_translation_unit', 'checker_binary']:
            require(k in build, 'mandatory native artifact'); a.identity(build[k])
        for k in ['toolchain', 'toolchain_dependency_closure', 'headers', 'dependency_inputs', 'linked_dependency_closure']:
            require(isinstance(build.get(k), list) and build[k], 'mandatory compiler/header/loader closure')
    if n >= 256: require(raw['builds']['lambda'] is None, 'analytic corner no lambda build')
    before = a.json(prefix + '/runtime-before.json'); after = a.json(prefix + '/runtime-after.json')
    require(raw['runtime_before'] == before and raw['runtime_after'] == after and before['loaded'] == after['loaded'] and
            before['all_file_mappings'] == after['all_file_mappings'] and set(before['loaded']) == set(expected_apis), 'runtime loaded closure')
    for label in ['before', 'after']:
        maps = a.data(prefix + '/loaded-' + label + '.maps').decode()
        require(raw['maps_' + label] == maps, 'maps raw linkage')
        mapped = {r['path'] for r in before['all_file_mappings']}
        for line in maps.splitlines():
            fields = line.split(maxsplit=5)
            if len(fields) == 6 and fields[5].startswith('/'):
                require(not fields[5].endswith(' (deleted)') and fields[5] in mapped, 'all mapped files have preserved identities')
    # Recursively require every identity in raw/build/runtime/preregistration,
    # including compiler, headers, native TU/binary/deps, mapped Python and libc.
    for doc in [raw, summary, account, registration, receipt]: a.closure(doc)
    if mode == 'produce':
        require(config['certificate'] is None and config['certificate_identity'] is None and raw['original_certificate'] is None, 'primary has no old input')
    if mode == 'verify':
        original = a.data(prefix + '/original-certificate.json')
        require(raw['original_certificate'] == strict(original), 'raw original certificate linkage')
        require(a.identity(config['certificate_identity']) == original, 'registered original certificate identity')
    return receipt_bytes

def validate_attempt(a, group, n, run):
    domain = a.json('outputs/writer-domain.json')
    validate_domain(domain, run['package_root'], digest(a.data('runtime_manifest.json')))
    require(run.get('writer_domain') == domain and run['plan'] == plan(group), 'immutable writer domain/run plan binding')
    expected_identity = digest(encoded({'manifest': run['manifest'], 'plan': run['plan'],
                                       'workers': run['workers'], 'writer_domain': domain}))
    require(run['identity'] == expected_identity, 'writer-domain run identity')
    require(run['plan']['group'] == group and n in run['plan']['degrees'] and 1 <= run['workers'] <= 40, 'attempt frozen scope/profile')
    selected = run['provenance']['selected_cores']
    require(len(selected) == run['workers'] and len(set(selected)) == len(selected) and
            set(selected) <= set(run['provenance']['inherited_affinity']), 'inherited core plan')
    prefix = 'outputs/' + group + '/jobs/' + str(n)
    started = a.json(prefix + '/started.json'); wrapper = a.json(prefix + '/wrapper-exit.json'); attempt = a.json(prefix + '/attempt.json')
    require(started['n'] == n and started['identity'] == run['identity'] and started['core'] in run['provenance']['selected_cores'], 'started run identity')
    require(wrapper.get('observed_returncode') == 0 and not wrapper.get('timeout') and not wrapper.get('supervisor_cleanup'), 'direct wrapper EXIT0')
    require(attempt.get('n') == n and attempt.get('terminal') is True and attempt.get('failure') is None and
            attempt.get('ECHILD') is True and attempt.get('cleanup_killed') == [] and attempt.get('status') == 'awaits_independent_result_review', 'terminal attempt closure')
    records = []
    for mode in ['produce', 'verify']:
        exit_record = a.json(prefix + '/' + mode + '-exit.json'); records.append(exit_record)
        require(exit_record.get('mode') == mode and exit_record.get('observed_returncode') == 0 and
                exit_record.get('cleanup_killed') == [] and exit_record.get('ECHILD') is True, 'direct pass EXIT0')
        expected_command = [exit_record['command'][0], '-E', '-S', '-B', str(a.absolute / ENGINE / 'engine.py'),
                            '--mode', mode, '--n', str(n), '--output', str(a.absolute / prefix / mode), '--run-once']
        if mode == 'verify': expected_command += ['--certificate', str(a.absolute / prefix / 'produce/essential-receipt.json')]
        require(exit_record['command'] == expected_command, 'direct observed command identity')
        receipt = validate_pass(a, prefix + '/' + mode, n, mode, run['manifest'])
        if mode == 'produce': primary = receipt
        else: require(a.data(prefix + '/verify/original-certificate.json') == primary, 'fresh replay exact primary linkage')
    require(attempt['passes'] == records, 'attempt/pass-exit linkage')
    return n
