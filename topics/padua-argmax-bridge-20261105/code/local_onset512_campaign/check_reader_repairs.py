"""Synthetic regression for E4-01..04 and E5-01; no native campaign or real-proof claim.

Run python3 -E -B .../check_reader_repairs.py. Temporary ZIPs are rehashed after
mutations. The positive fixture uses a marked checker/closure adapter because the
canonical ZIP is absent. A real storage/export roundtrip uses synthetic data.
Only trust/checker arithmetic and sampled closure verification use marked adapters.
"""
import contextlib
import copy
import io
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile
from types import SimpleNamespace
from unittest.mock import patch
import warnings
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import return_bundle as B
from storage import deduplicate
import verify_compact as V


def require(value, message):
    if not value: raise RuntimeError(message)


def rejects(call, reason):
    try: call()
    except (ValueError, KeyError, RuntimeError) as error:
        require(reason in str(error), 'wrong rejection: ' + str(error) + '; expected ' + reason)
        return
    raise RuntimeError('unexpected acceptance: ' + reason)


def fixture(root='/recorded', assets=None):
    root = str(root); prefix = 'out'; docs = {}; frozen = {'path': '/frozen', 'bytes': 1, 'sha256': B.sha(b'f')}
    pins = {'source': [], 'arithmetic_files': {}, 'freeze': frozen, 'asset_provenance': frozen}
    helper = b'# synthetic helper\n'
    helper_pin = {'path': '/original/evidence.py', 'bytes': len(helper), 'sha256': B.sha(helper), 'input_head_equal': True}
    if assets is not None:
        assets.mkdir()
        (assets / 'frozen').write_bytes(b'f')
        (assets / 'python').write_bytes(b'p')
        (assets / 'evidence.py').write_bytes(helper)
        frozen = B.R.identity(assets / 'frozen')
        pins.update(freeze=frozen, asset_provenance=frozen)
        helper_pin.update(B.R.identity(assets / 'evidence.py'))
    reg = {'degrees': list(range(320, 511)), 'pins': pins, 'runner': {'sha256': B.CAMPAIGN_RUNNER_SHA},
           'compact_evidence': helper_pin, 'python': (B.R.identity(assets / 'python') if assets is not None
                                                           else {'path': '/python', 'bytes': 1, 'sha256': 'p'})}
    def put(name, value):
        data = B.encoded(value); docs[name] = data
        return {'path': root + '/' + name, 'bytes': len(data), 'sha256': B.sha(data)}
    pre = put(prefix + '/preregistration.json', reg)
    selection = {'eligible': reg['degrees'], 'seed_hex': '00',
                 'selected': random.Random(b'\0').sample(reg['degrees'], 2), 'preregistration': pre}
    put(prefix + '/compact-selection.json', selection)
    put(prefix + '/return-provenance.json', {'python_invocation': '/python'})
    put(prefix + '/helper-source-pins.json', {'files': [helper_pin]})
    docs[prefix + '/helper-source/evidence.py'] = helper
    wrappers = []
    for n in reg['degrees']:
        case = prefix + '/jobs/' + str(n); exits = []
        primary = None
        for mode in ('produce', 'verify'):
            target = case + '/' + mode
            raw = put(target + '/raw-evidence.json', {'runtime_before': {'all_file_mappings': [reg['python']]}})
            config = {'n': n, 'mode': mode, 'output': root + '/' + target, 'certificate': None, 'certificate_identity': None}
            if mode == 'verify':
                config.update(certificate=primary['path'], certificate_identity=primary)
                docs[target + '/original-certificate.json'] = docs[case + '/produce/essential-receipt.json']
            proof = {k: [] for k in B.COMPARE}
            proof.update(n=n, freeze=frozen, whole_raw_evidence=raw, verification={'synthetic': True}, CPU_stages=[])
            receipt = put(target + '/essential-receipt.json', proof)
            if mode == 'produce': primary = receipt
            put(target + '/preregistration.json', {'engine_config': config, 'freeze': frozen})
            put(target + '/summary.json', {'result': 'PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING', 'first_failure': None,
                'engine_config': config, 'whole_raw_evidence': raw, 'essential_receipt': receipt, 'freeze': frozen, 'stages': []})
            put(target + '/final-accounting.json', {'complete': True, 'first_failure': None, 'hard_aggregate_cap': 120,
                'engine_config': config, 'result': B.LABELS[mode], 'total_CPU_through_summary': 1,
                'final_self_limit': {'no_live_children': True, 'waited_child_CPU': 1, 'absolute_self_CPU_hard': 1}})
            put(target + '/local-validation.json', {'receipt': receipt, 'raw': raw})
            command = [reg['python']['path'], '-E', '-S', '-B', root + '/topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/engine.py',
                       '--mode', mode, '--n', str(n), '--output', config['output'], '--run-once']
            if mode == 'verify': command += ['--certificate', primary['path']]
            ex = {'observed_returncode': 0, 'ECHILD': True, 'timeout': False, 'cleanup_killed': [], 'command': command}
            put(case + '/' + mode + '-exit.json', ex); exits.append(ex)
        put(case + '/attempt.json', {'n': n, 'failure': None, 'ECHILD': True, 'cleanup_killed': [], 'terminal': True,
                                    'status': 'awaits_independent_result_review', 'passes': exits})
        put(case + '/admitted.json', {'n': n, 'preregistration': pre})
        wrapper = {'n': n, 'observed_returncode': 0}; wrappers.append(wrapper)
        put(case + '/wrapper-exit.json', wrapper)
    for stage, degrees in [('pilot', [320]), ('remaining', list(range(321, 511)))]:
        put(prefix + '/' + stage + '-admitted.json', {'degrees': degrees, 'preregistration': pre})
        put(prefix + '/' + stage + '-summary.json', {'ECHILD': True, 'quiescent': True, 'failed': False,
            'unstarted': [], 'cleanup_killed': [], 'results': [row for row in wrappers if row['n'] in degrees]})
    return docs, {'format': 'PADUA-local-onset512-compact-v1', 'root': root, 'output': prefix,
                  'degrees': reg['degrees'], 'selection': selection}, pins


def producer_roundtrip(temp, release, manifest, controls):
    """Run real completed/export/deduplicate; adapt only trust and proof arithmetic.

    This is synthetic data, never an engine invocation. Build artifacts are tiny
    inert bytes; the real storage helper authenticates and hardlinks them.
    """
    tree = temp / 'producer-tree'; tree.mkdir()
    output = tree / 'out'
    docs, _, pins = fixture(tree, temp / 'producer-assets')
    for name, data in docs.items():
        if name in ('out/return-provenance.json', 'out/compact-selection.json'): continue
        path = tree / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(data)
    # Export includes both trusted script identities; preserve their real names
    # relative to the synthetic package instead of bypassing export's add().
    scripts = []
    for source in (Path(B.__file__), Path(B.R.__file__)):
        target = tree / source.relative_to(B.R.ROOT)
        target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(source.read_bytes()); scripts.append(target)
    examined = relinked = 0
    for n in range(320, 511):
        for mode in ('produce', 'verify'):
            target = output / 'jobs' / str(n) / mode
            work = target / 'check-synthetic'; work.mkdir()
            build = {'workdir': str(work), 'linked_dependency_closure': []}
            for key in ('source_snapshot', 'preprocessed_translation_unit', 'checker_binary'):
                path = work / key; path.write_bytes(b'inert synthetic build bytes\n')
                build[key] = B.R.identity(path)
            B.R.save(target / 'S-build.json', build)
            receipt = deduplicate(output, target)
            examined += receipt['immutable_paths_examined']; relinked += receipt['paths_relinked']
    require(examined == 1146 and relinked > 0, 'real storage paths were not deduplicated')
    require((output / '.preserve.lock').read_bytes() == b'', 'producer lock')
    events = []; sampled = []
    class ArithmeticAdapter:
        def __init__(self, *args, read_bytes=None):
            if read_bytes is not None:
                events.append('checker'); require(events[-2:] == ['pins', 'checker'], 'roundtrip import order')
            self.reader = read_bytes
            self.checker = SimpleNamespace(verify_essential=lambda proof, freeze: proof['verification'])
        def data(self, name): return self.reader(name)
    def checked_pins(): events.append('pins'); return pins
    archive = temp / 'producer-roundtrip.zip'
    with patch.object(B.R, 'ROOT', tree), patch.object(B.R, 'RELEASE', release), \
         patch.object(B.R, '__file__', str(scripts[1])), patch.object(B, '__file__', str(scripts[0])), \
         patch.object(B.R, 'pins', checked_pins), patch.object(B.R, 'LocalAccess', ArithmeticAdapter), \
         patch.object(B, 'Access', ArithmeticAdapter), patch.object(B, 'MANIFEST_SHA', B.sha(manifest)), \
         patch.object(B, 'validate_pass', lambda a, target, n, mode, m: sampled.append((n, mode))):
        exported = B.export(output, archive)
        with zipfile.ZipFile(archive) as bundle:
            require(bundle.read('out/.preserve.lock') == b'', 'export omitted produced lock')
            receipts = [name for name in bundle.namelist() if name.endswith('/storage-dedup.json')]
            require(len(receipts) == 382, 'export omitted produced storage receipts')
            for name in receipts:
                require(bundle.read(name) == (tree / name).read_bytes(), 'produced receipt bytes changed')
        with contextlib.redirect_stdout(io.StringIO()) as captured:
            B.verify(archive, B.sha(archive.read_bytes()))
        result = json.loads(captured.getvalue())
        require(result['pairs'] == 191 and result['proofs'] == 382 and len(sampled) == 4,
                'roundtrip reader coverage')
        require(exported['selection']['selected'] == result['sample'], 'roundtrip sample')
    controls.append('real deduplicate/completed/export/reader roundtrip: 382 produced receipts and empty lock')


def main():
    controls = []
    with tempfile.TemporaryDirectory(prefix='reader-repairs-') as temp:
        temp = Path(temp); release = temp / 'release'; release.mkdir()
        asset = b'{}'; manifest = B.encoded({'files': {'asset_provenance.json': {'bytes': 2, 'sha256': B.sha(asset)}}})
        (release / 'asset_provenance.json').write_bytes(asset)
        (release / 'runtime_manifest.json').write_bytes(manifest)
        producer_roundtrip(temp, release, manifest, controls)
        docs, inventory, pins = fixture()
        docs['TRUSTED_RUNTIME_MANIFEST.json'] = manifest; docs['TRUSTED_ASSET_PROVENANCE.json'] = asset
        inventory['trusted_manifest'] = B.R.identity(release / 'runtime_manifest.json')
        events = []; sampled = []
        class SyntheticAccess:
            def __init__(self, package, root, read_bytes):
                events.append('checker'); require(events[-2:] == ['pins', 'checker'], 'checker loaded before pins')
                self.reader = read_bytes
                self.checker = SimpleNamespace(verify_essential=lambda proof, freeze: proof['verification'])
            def data(self, name): return self.reader(name)
            # Match real Access.json: the repaired local subclass must supply validation.
            def json(self, name): return json.loads(self.reader(name))
        def checked_pins(): events.append('pins'); return pins
        def archive(files, inv=inventory, members=None):
            path = temp / 'case.zip'
            inv = copy.deepcopy(inv)
            inv['files'] = {n: {'bytes': len(d), 'sha256': B.sha(d)} for n, d in files.items()}
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                with zipfile.ZipFile(path, 'w') as z:
                    for n, data in (list(files.items()) if members is None else members): z.writestr(n, data)
                    z.writestr('COMPACT.json', B.encoded(inv))
            return path
        def run(files, inv=inventory, members=None):
            path = archive(files, inv, members)
            with contextlib.redirect_stdout(io.StringIO()) as output:
                B.verify(path, B.sha(path.read_bytes()))
            return json.loads(output.getvalue())
        def mutate(name, key, value):
            files = dict(docs); doc = json.loads(files[name]); doc[key] = value; files[name] = B.encoded(doc); return files
        with patch.object(B.R, 'RELEASE', release), patch.object(B, 'MANIFEST_SHA', B.sha(manifest)), \
             patch.object(B.R, 'pins', checked_pins), patch.object(B, 'Access', SyntheticAccess), \
             patch.object(B, 'validate_pass', lambda a, target, n, mode, m: sampled.append((n, mode))):
            result = run(docs)
            require(result['pairs'] == 191 and result['proofs'] == 382 and result['reader']['sha256'] == B.R.identity(B.__file__)['sha256'], 'verified counts/reader SHA')
            require(len(sampled) == 4, 'sample closure calls'); controls.append('positive adapted 191-pair baseline')
            dedup = {'immutable_paths_examined': 3, 'paths_relinked': 2, 'logical_bytes_relinked': 4,
                     'scope': 'identical bytes and paths retained; logs/JSON untouched'}
            produced = dict(docs); produced['out/.preserve.lock'] = b''
            member = 'out/jobs/320/produce/storage-dedup.json'
            produced[member] = B.encoded(dedup)
            run(produced); controls.append('allowlisted storage receipt and empty lock')
            bad = dict(produced); bad['out/.preserve.lock'] = b'x'
            rejects(lambda: run(bad), 'preserve lock must be empty'); controls.append('nonempty preserve lock')
            for label, value, reason in [
                ('missing key', {k: v for k, v in dedup.items() if k != 'scope'}, 'receipt schema'),
                ('extra key', dict(dedup, extra=1), 'receipt schema'),
                ('nonobject', [], 'receipt schema'),
                ('boolean count', dict(dedup, paths_relinked=True), 'integer counts'),
                ('float count', dict(dedup, paths_relinked=1.0), 'integer counts'),
                ('negative count', dict(dedup, logical_bytes_relinked=-1), 'integer counts'),
                ('too many relinks', dict(dedup, paths_relinked=4), 'consistent counts'),
                ('bytes without relinks', dict(dedup, paths_relinked=0), 'consistent counts'),
                ('scope', dict(dedup, scope='forged'), 'dedup scope')]:
                bad = dict(produced); bad[member] = B.encoded(value)
                rejects(lambda bad=bad: run(bad), reason); controls.append('storage dedup ' + label)
            for label, data, reason in [
                ('duplicate key', B.encoded(dedup).replace(b'"paths_relinked": 2', b'"paths_relinked": 2, "paths_relinked": 2'), 'duplicate JSON key'),
                ('NaN', B.encoded(dedup).replace(b'"paths_relinked": 2', b'"paths_relinked": NaN'), 'nonfinite JSON')]:
                bad = dict(produced); bad[member] = data
                rejects(lambda bad=bad: run(bad), reason); controls.append('storage dedup ' + label)
            for name in ('../x', '/x', './x', 'a//b'):
                rejects(lambda name=name: run({}, members=[(name, b'1')]), 'required: not path.is_absolute()'); controls.append('unsafe ' + name)
            rejects(lambda: run({}, members=[('dir/', b'')]), 'required: not path.is_absolute()'); controls.append('directory')
            rejects(lambda: run({}, members=[('a', b'1'), ('a', b'2')]), 'required: not path.is_absolute()'); controls.append('duplicate member')
            rejects(lambda: B.verify(archive(docs)), 'external archive SHA256'); controls.append('external archive pin')
            with patch.object(B, 'MANIFEST_SHA', '0' * 64):
                before = len(events); rejects(lambda: run(docs), 'external trusted manifest'); require(len(events) == before, 'checker ran on bad manifest')
            controls.append('external manifest pin before checker')
            before = len(events)
            with patch.object(B.R, 'pins', side_effect=ValueError('synthetic frozen source mismatch')):
                rejects(lambda: run(docs), 'synthetic frozen source mismatch')
            require(len(events) == before, 'checker ran on failed source pins')
            controls.append('source pins authenticated before checker')
            shadow = dict(docs); shadow['asset_provenance.json'] = asset
            rejects(lambda: run(shadow), 'archive shadows trusted package'); controls.append('trusted shadow')
            for member, reason in [('out/jobs/999/attempt.json', 'unregistered job'), ('out/jobs/320/failure.txt', 'unexpected failure'),
                                   ('out/jobs/320/produce/evil.json', 'unregistered pass'), ('arbitrary', 'unregistered archive')]:
                files = dict(docs); files[member] = b'{}'; rejects(lambda: run(files), reason); controls.append(member)
            for name, key, value, reason in [
                ('out/jobs/320/attempt.json', 'status', 'failed', 'completed attempt status'),
                ('out/jobs/320/produce/summary.json', 'essential_receipt', {}, 'summary receipt identity'),
                ('out/jobs/320/verify/final-accounting.json', 'engine_config', {'n': 320}, 'account'),
                ('out/jobs/320/produce-exit.json', 'observed_returncode', False, 'integer field'),
                ('out/jobs/320/wrapper-exit.json', 'observed_returncode', 0.0, 'integer field'),
                ('out/jobs/320/attempt.json', 'terminal', 1, 'boolean field'),
                ('out/jobs/320/produce-exit.json', 'ECHILD', 1, 'boolean field'),
                ('out/jobs/320/produce-exit.json', 'cleanup_killed', False, 'cleanup_killed'),
            ]:
                rejects(lambda: run(mutate(name, key, value)), reason); controls.append(name + ':' + key)
            for label, member, data, reason in [
                ('unsampled native history', 'out/jobs/404/produce/check-abc/deps/libx.so', b'x', 'unsampled native history'),
                ('wrong preserved hash', 'preserved-sha256/' + B.sha(b'other'), b'not-other', 'preserved object hash'),
                ('extra helper', 'out/helper-source/extra.py', b'# extra', 'unregistered helper source'),
                ('changed original certificate', 'out/jobs/403/verify/original-certificate.json',
                 docs['out/jobs/403/verify/original-certificate.json'] + b' ', 'original-certificate'),
                ('duplicate attempt key', 'out/jobs/335/attempt.json',
                 docs['out/jobs/335/attempt.json'].replace(b'"terminal": true', b'"terminal": true, "terminal": true'), 'duplicate JSON key')]:
                bad = dict(docs); bad[member] = data
                rejects(lambda bad=bad: run(bad), reason); controls.append(label)
            rejects(lambda: run(mutate('out/jobs/333/produce-exit.json', 'observed_returncode', '0')), 'integer field')
            controls.append('string exit code')
            bad_runner = mutate('out/preregistration.json', 'runner', {'sha256': '0' * 64})
            rejects(lambda: run(bad_runner), 'preregistered campaign runner')
            controls.append('historical preregistered runner SHA')
            fresh = dict(docs)
            for name in ('final-accounting.json', 'summary.json', 'preregistration.json'):
                key = 'out/jobs/320/verify/' + name
                doc = json.loads(fresh[key]); doc['engine_config']['certificate_identity']['path'] = '/wrong'
                fresh[key] = B.encoded(doc)
            rejects(lambda: run(fresh), 'fresh input primary linkage')
            controls.append('fresh certificate identity on unsampled pair')
            # Retain the original transport negatives without multi-GiB allocations.
            original_infos = zipfile.ZipFile.infolist
            for sizes, reason in [([513 * 1024**2], 'member.file_size'), ([450 * 1024**2] * 5, 'total<=')]:
                def declared_infos(bundle):
                    infos = original_infos(bundle)
                    for info, size in zip(infos, sizes): info.file_size = size
                    return infos
                reads = []
                def observed_read(bundle, member, pwd=None):
                    reads.append(member.filename)
                    # Marked metadata adapter: declared sizes test pre-read guards;
                    # bytes are deliberately tiny and not an actual giant ZIP.
                    return b'x'
                with patch.object(zipfile.ZipFile, 'infolist', declared_infos), patch.object(zipfile.ZipFile, 'read', observed_read):
                    rejects(lambda: run({}, members=[('p' + str(i), b'x') for i in range(len(sizes))]), reason)
                require(len(reads) == (0 if len(sizes) == 1 else 4), 'size bound happened after read')
                controls.append('pre-read size bound ' + str(len(sizes)))
            missing = temp / 'missing.zip'
            with zipfile.ZipFile(missing, 'w') as z: z.writestr('a', b'x')
            rejects(lambda: B.verify(missing, B.sha(missing.read_bytes())), 'COMPACT.json')
            controls.append('missing COMPACT.json')
            invalid = archive(docs)
            with zipfile.ZipFile(invalid) as z: pairs = [(i.filename, z.read(i)) for i in z.infolist()]
            bad_inventory = json.loads(pairs[-1][1]); bad_inventory['files']['TRUSTED_ASSET_PROVENANCE.json']['sha256'] = '0' * 64
            with zipfile.ZipFile(invalid, 'w') as z:
                for name, data in pairs[:-1]: z.writestr(name, data)
                z.writestr('COMPACT.json', B.encoded(bad_inventory))
            rejects(lambda: B.verify(invalid, B.sha(invalid.read_bytes())), "row==")
            controls.append('inventory hash mismatch')
            symlink = zipfile.ZipInfo('out/jobs/320/produce/evil.json'); symlink.external_attr = 0o120777 << 16
            rejects(lambda: run(docs, members=[*docs.items(), (symlink, b'/etc/passwd')]), 'inventory')
            controls.append('symlink typed member remains data/inventory checked')
            inv = copy.deepcopy(inventory); inv['degrees'] = []
            rejects(lambda: run(docs, inv), 'degrees'); controls.append('forged empty degree inventory')
            # A zero-certificate archive must be refused before imports, even with -O/env optimization.
            forged = archive({}, {'root': '/forged', 'output': 'out', 'degrees': [], 'selection': {}})
            for flags, env in [(['-O', '-B'], None), (['-B'], {'PYTHONOPTIMIZE': '1'})]:
                import os
                child_env = dict(os.environ); child_env.update(env or {})
                for script, args in [(B.__file__, ['verify', str(forged)]), (B.R.__file__, ['preregister', str(temp / 'never-created')])]:
                    proc = subprocess.run([sys.executable, *flags, script, *args], env=child_env, capture_output=True, text=True)
                    require(proc.returncode != 0 and 'optimized Python is unsupported' in proc.stderr and 'accepted_pending' not in proc.stdout, 'optimization refusal')
                    controls.append('optimization refusal ' + Path(script).name + ' ' + str(flags))
            require(not (temp / 'never-created').exists(), 'optimized runner mutated output')
            for script in (B.__file__, B.R.__file__):
                proc = subprocess.run([sys.executable, '-E', '-B', script, '--help'], env=child_env, capture_output=True, text=True)
                require(proc.returncode == 0, '-E must ignore PYTHONOPTIMIZE')
                controls.append('-E ignores optimization environment ' + Path(script).name)
            # Check the real wrapper/pass check sites of the repaired compact verifier.
            for mode in ('wrapper', 'pass'):
                class ExitAccess:
                    absolute = Path('/recorded')
                    def data(self, name):
                        if name.endswith('/FREEZE.json'): return b'f'
                        return B.encoded(self.json(name))
                    checker = SimpleNamespace(verify_essential=lambda proof, freeze: proof['verification'])
                    def json(self, name):
                        if name.endswith('/started.json'): return {'n': 320, 'identity': 'id', 'core': 0}
                        mapped = name.replace('outputs/g/', 'out/')
                        value = json.loads(docs[mapped].replace(b'/recorded/out/', b'/recorded/outputs/g/'))
                        if name.endswith('/summary.json'):
                            data = self.data(name.rsplit('/', 1)[0] + '/essential-receipt.json')
                            value['essential_receipt'].update(bytes=len(data), sha256=B.sha(data))
                        if mapped.endswith('/wrapper-exit.json') and mode == 'wrapper': value['observed_returncode'] = False
                        if mapped.endswith('/produce-exit.json'):
                            value.update(mode='produce', observed_returncode=False)
                        return value
                rejects(lambda: V.check_pair(ExitAccess(), 'g', 320, {'identity': 'id', 'provenance': {'selected_cores': [0]}}),
                        'observed wrapper EXIT0' if mode == 'wrapper' else 'observed pass EXIT0')
                controls.append('compact boolean exit ' + mode)
            receipt = {'schema': 'padua-compact-return-v1', 'manifest_sha256': 'pin', 'files': {'runtime_manifest.json': {'bytes': 2, 'sha256': V.digest(b'{}')}},
                       'completed_degrees': [], 'runs': [], 'validation_hashes': [],
                       'selection': {'coverage': {'eligible_residual': [], 'completed': []}, 'seed_hex': '00', 'sampled_residual_degrees': []}}
            payload = {'runtime_manifest.json': b'{}', 'COMPACT.json': B.encoded(receipt)}
            result = V.verify_payloads(payload, temp, {'files': {}}, b'{}', 'pin')
            require(result['expect_plan'] is None and result['coverage_mode'] == 'completed_subset', 'subset mode reporting')
            rejects(lambda: V.verify_payloads(payload, temp, {'files': {}}, b'{}', 'pin', 'all'), 'expected complete plan coverage')
            with patch.object(V, 'plan', lambda label: {'degrees': []}):
                result = V.verify_payloads(payload, temp, {'files': {}}, b'{}', 'pin', 'all')
            require(result['expect_plan'] == 'all' and result['coverage_mode'] == 'complete_plan', 'complete mode reporting')
            controls.append('compact coverage reporting and incomplete plan rejection')
    print(json.dumps({'status': 'PASS', 'controls': len(controls), 'cases': controls,
                      'scope': 'synthetic linkage/transport controls with explicit checker/closure adapter; real synthetic storage/export roundtrip; no canonical archive or arithmetic rerun'}))

if __name__ == '__main__': main()
