"""Full-history data-only export/readback for the new 2026-11-14 campaign.

Never imports or executes archive code, extracts paths, or changes scientific
receipts. Every pass receives the separately trusted compact validate_pass.
"""
import argparse
import hashlib
from collections import OrderedDict
import json
import os
import stat
from pathlib import Path
import sys
import zipfile

import campaign as C
R = C.R
PYTHON_INVOCATION = '/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3'
from evidence import Access, identities, safe, validate_pass

COMPARE = ('tree', 'S_upper_rows', 'lambda_upper_rows', 'norm', 'verification',
           'floor', 'corner', 'analytic_far', 'origin_lower_hex')


def digest(data): return hashlib.sha256(data).hexdigest()
def row(data): return {'bytes': len(data), 'sha256': digest(data)}
def encoded(value): return (json.dumps(value, indent=2, allow_nan=False) + '\n').encode()
def need(condition, message): R.require(condition, message)


def validate(reader, root, prefix, frozen):
    """Validate all histories and numerical receipts using only trusted code."""
    prereg_name = prefix + '/preregistration.json'
    registration_bytes = reader(prereg_name)
    prereg = R.strict(registration_bytes)
    prereg_id = {'path': root + '/' + prereg_name, **row(registration_bytes)}
    need(prereg_id == frozen['preregistration'], 'committed preregistration identity')
    need(prereg['campaign_id'] == 'padua-argmax-paper-regeneration-20261114', 'new campaign ID')
    need(prereg['runner'] == frozen['runner'] and prereg['campaign_wrapper'] == frozen['campaign_wrapper'], 'committed campaign code')
    need(prereg['degrees'] == list(range(320, 511)) and prereg['passes'] == ['produce', 'verify'], 'exact new campaign scope')
    need(prereg['output'] == root + '/' + prefix, 'registered campaign root')
    local_pins = R.pins()
    need(prereg['pins']['source'] == local_pins['source'] and prereg['pins']['arithmetic_files'] == local_pins['arithmetic_files'], 'trusted frozen source and arithmetic pins')
    for key in ('freeze', 'asset_provenance'):
        need(all(prereg['pins'][key][k] == local_pins[key][k] for k in ('bytes', 'sha256')), 'trusted source/provenance identity')
    need(all(R.identity(R.RELEASE / 'runtime_manifest.json')[k] == prereg['trusted_manifest'][k] for k in ('bytes', 'sha256')), 'trusted manifest pin')
    for helper in prereg['helper_sources']:
        path = R.ROOT / Path(helper['path']).relative_to(root)
        need(all(R.identity(path)[k] == helper[k] for k in ('bytes', 'sha256')), 'trusted compact helper source pin')
    class DataAccess(Access):
        def json(self, name): return R.strict(self.data(name))
    access = DataAccess(R.ROOT, root, read_bytes=reader)
    manifest = R.read(R.RELEASE / 'runtime_manifest.json')
    controls = R.strict(reader(prefix + '-controls/controls.json'))
    need(controls['pins'] == prereg['pins'] and controls['external_reap_refused'] is True and controls['ignored_SIGCHLD_refused'] is True, 'operational controls and source pins')
    need(controls['exit7']['observed_returncode'] == 7 and controls['exit7']['ECHILD'] is True and controls['exit7']['cleanup_killed'] == [], 'observed control EXIT7')
    need(type(controls['exit7']['waitstatus']) is int and os.waitstatus_to_exitcode(controls['exit7']['waitstatus']) == controls['exit7']['observed_returncode'], 'control raw waitstatus linkage')
    inventory = []
    wrappers = {}
    def get(name): return R.strict(reader(name))
    def identity(name): return {'path': root + '/' + name, **row(reader(name))}
    for n in prereg['degrees']:
        case = prefix + '/jobs/' + str(n)
        proofs = []; exits = []
        for mode in ('produce', 'verify'):
            target = case + '/' + mode
            receipt = validate_pass(access, target, n, mode, manifest)
            proof = R.strict(receipt); proofs.append(proof)
            ex = get(case + '/' + mode + '-exit.json'); exits.append(ex)
            need(type(ex['observed_returncode']) is int and ex['observed_returncode'] == 0 and ex['ECHILD'] is True and ex['timeout'] is False and ex['cleanup_killed'] == [], 'observed pass terminal EXIT0')
            need(type(ex['waitstatus']) is int and os.waitstatus_to_exitcode(ex['waitstatus']) == ex['observed_returncode'], 'pass raw waitstatus linkage')
            command = [PYTHON_INVOCATION, '-E', '-S', '-B', root + '/topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/engine.py', '--mode', mode, '--n', str(n), '--output', root + '/' + target, '--run-once']
            if mode == 'verify': command += ['--certificate', root + '/' + case + '/produce/essential-receipt.json']
            need(ex['command'] == command, 'exact observed engine command')
            local = get(target + '/local-validation.json')
            need(local['receipt'] == identity(target + '/essential-receipt.json') and local['raw'] == identity(target + '/raw-evidence.json'), 'original local validation identities')
            raw = get(target + '/raw-evidence.json')
            need(prereg['python'] in raw['runtime_before']['all_file_mappings'], 'preregistered Python runtime actually mapped')
            summary = get(target + '/summary.json')
            need(summary['essential_receipt'] == identity(target + '/essential-receipt.json'), 'summary receipt identity')
            inventory.append({'n': n, 'mode': mode, 'receipt': identity(target + '/essential-receipt.json'),
                'raw': identity(target + '/raw-evidence.json'), 'account': identity(target + '/final-accounting.json'),
                'exit': identity(case + '/' + mode + '-exit.json')})
        need(all(proofs[0][key] == proofs[1][key] for key in COMPARE), 'fresh retained proof equality')
        need(reader(case + '/produce/essential-receipt.json') == reader(case + '/verify/original-certificate.json'), 'fresh original certificate byte equality')
        config = get(case + '/verify/final-accounting.json')['engine_config']
        need(config['certificate'] == root + '/' + case + '/produce/essential-receipt.json', 'fresh registered primary certificate path')
        attempt = get(case + '/attempt.json')
        need(attempt['n'] == n and attempt['terminal'] is True and attempt['ECHILD'] is True and attempt['failure'] is None and attempt['cleanup_killed'] == [] and attempt['status'] == 'awaits_independent_result_review' and attempt['passes'] == exits, 'complete attempt/pass linkage')
        admission = get(case + '/admitted.json')
        need(admission['n'] == n and admission['preregistration'] == prereg_id and admission['core'] in prereg['environment']['selected_cores'], 'case admission binding')
        wrapper = get(case + '/wrapper-exit.json')
        need(type(wrapper['observed_returncode']) is int and wrapper['observed_returncode'] == 0 and wrapper['n'] == n, 'observed wrapper EXIT0')
        wrappers[n] = wrapper
    for stage, degrees in [('pilot', [320]), ('remaining', list(range(321, 511)))]:
        admission = get(prefix + '/' + stage + '-admitted.json')
        need(admission['degrees'] == degrees and admission['preregistration'] == prereg_id, 'stage preregistration admission')
        summary = get(prefix + '/' + stage + '-summary.json')
        need(summary['ECHILD'] is True and summary['quiescent'] is True and summary['failed'] is False and summary['cleanup_killed'] == [] and summary['unstarted'] == [], 'terminal stage accounting')
        need(sorted(r['n'] for r in summary['results']) == degrees and len(summary['results']) == len(degrees), 'exact stage coverage')
        need(all(r == wrappers[r['n']] for r in summary['results']), 'stage/wrapper result equality')
    return {'format': 'paper-regeneration-full-inventory-v1', 'campaign_id': prereg['campaign_id'],
        'preregistration': prereg_id, 'pairs': 191, 'proofs': 382, 'passes': inventory,
        'status': 'accepted_pending_independent_I25_and_audit'}


def export(archive):
    reg = C.checked(); prefix = C.OUTPUT.relative_to(R.ROOT).as_posix()
    manifest = R.read(R.RELEASE / 'runtime_manifest.json')['files']
    files = {}; sources = {}; seen_blobs = set()
    def add(name, path):
        safe(name); path = Path(path)
        need(path.is_file() and not path.is_symlink(), 'regular retained file: ' + str(path))
        data = path.read_bytes(); value = row(data)
        if name in files: need(files[name] == value, 'consistent retained identity')
        files[name] = value; sources[value['sha256']] = path
        return data
    for directory in (C.OUTPUT, C.CONTROL):
        for path in sorted(directory.rglob('*')):
            if path.is_file(): add(path.relative_to(R.ROOT).as_posix(), path)
    # Preserve every referenced dependency that is not already supplied by the
    # separately authenticated trusted release, including all external files.
    json_names = [name for name in files if name.endswith('.json')]
    verified_dependencies = {}
    for name in json_names:
        for identity in identities(R.strict(sources[files[name]['sha256']].read_bytes())):
            path = Path(identity['path'])
            if not path.is_absolute():
                safe(path.as_posix()); path = R.ROOT / path
            identity = {**identity, 'path': str(path)}
            if str(path) in verified_dependencies:
                need(verified_dependencies[str(path)] == identity, 'consistent repeated dependency identity')
                continue
            actual = R.identity(path)
            need(actual == identity, 'referenced dependency identity unchanged')
            verified_dependencies[str(path)] = identity
            relative = path.relative_to(R.ROOT).as_posix() if path.is_relative_to(R.ROOT) else 'preserved-sha256/' + identity['sha256']
            if relative in manifest:
                need(manifest[relative] == {k: identity[k] for k in ('bytes', 'sha256')}, 'trusted dependency equality')
            else: add(relative, path)
    def reader(name):
        safe(name)
        if name in manifest:
            path = R.RELEASE / name if name == 'asset_provenance.json' else R.ROOT / name
            data = path.read_bytes(); need(row(data) == manifest[name], 'trusted source identity'); return data
        value = files[name]; data = sources[value['sha256']].read_bytes()
        need(row(data) == value, 'retained export bytes'); return data
    result = validate(reader, str(R.ROOT), prefix, R.read(C.SNAPSHOT))
    result_path = C.OUTPUT / 'evidence-inventory.json'
    R.save(result_path, result); add(result_path.relative_to(R.ROOT).as_posix(), result_path)
    essential = C.OUTPUT.with_name(C.OUTPUT.name + '-essentials'); essential.mkdir(exist_ok=False)
    essential_rows = []
    for item in result['passes']:
        path = Path(item['receipt']['path']); name = 'n' + str(item['n']) + '-' + item['mode'] + '.json'
        data = path.read_bytes(); need(R.identity(path) == item['receipt'], 'essential source authenticated')
        with (essential / name).open('xb') as stream: stream.write(data)
        essential_rows.append({'name': name, **row(data), 'origin': str(path)})
    R.save(essential.with_name(essential.name + '-inventory.json'), {'files': essential_rows})
    inventory = {'format': 'paper-regeneration-full-return-v1', 'root': str(R.ROOT), 'output': prefix,
        'preregistration': reg['campaign_id'], 'frozen_config': R.read(C.SNAPSHOT),
        'files': files, 'retention': 'All campaign and controls files; all referenced nonrelease dependencies; unique byte blobs, no history sampling or pruning.'}
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        bundle.writestr('INVENTORY.json', encoded(inventory))
        for value in files.values():
            sha = value['sha256']
            if sha in seen_blobs: continue
            data = sources[sha].read_bytes(); need(row(data) == value, 'final export identity')
            bundle.writestr('sha256/' + sha, data); seen_blobs.add(sha)
    R.save(archive.with_suffix(archive.suffix + '.receipt.json'), {'archive': R.identity(archive),
        'evidence_inventory': R.identity(result_path), 'files': len(files), 'unique_blobs': len(seen_blobs)})
    print(json.dumps({'archive': R.identity(archive), 'evidence_inventory': R.identity(result_path)}), flush=True)


def verify(archive, archive_sha):
    need(R.identity(archive)['sha256'] == archive_sha, 'external return archive SHA256')
    manifest = R.read(R.RELEASE / 'runtime_manifest.json')['files']
    with zipfile.ZipFile(archive) as bundle:
        names = bundle.namelist()
        need(len(names) == len(set(names)) and len(names) < 200000, 'unique bounded archive members')
        need(all(not m.is_dir() and stat.S_IFMT(m.external_attr >> 16) in (0, stat.S_IFREG) and m.file_size <= 512*1024**2 for m in bundle.infolist()), 'bounded regular data blobs')
        need(sum(m.file_size for m in bundle.infolist()) <= 8*1024**3, 'bounded total uncompressed return')
        inventory = R.strict(bundle.read('INVENTORY.json'))
        need(inventory['format'] == 'paper-regeneration-full-return-v1' and inventory['frozen_config'] == R.read(C.SNAPSHOT), 'trusted new return profile')
        files = inventory['files']
        need(set(names) == {'INVENTORY.json'} | {'sha256/' + v['sha256'] for v in files.values()}, 'exact byte object inventory')
        for name, value in files.items():
            safe(name)
            need(set(value) == {'bytes', 'sha256'} and type(value['bytes']) is int and value['bytes'] >= 0 and len(value['sha256']) == 64 and all(c in '0123456789abcdef' for c in value['sha256']), 'inventory identity shape')
        need(all(files[name] == manifest[name] for name in set(files) & set(manifest)), 'no archive trusted-source shadowing')
        for value in files.values():
            need(bundle.getinfo('sha256/' + value['sha256']).file_size == value['bytes'], 'every retained file byte count')
        cache = OrderedDict(); cache_bytes = 0; budget = 128*1024**2
        def blob(sha):
            nonlocal cache_bytes
            if sha in cache:
                data = cache.pop(sha); cache[sha] = data; return data
            data = bundle.read('sha256/' + sha)
            need(len(data) == bundle.getinfo('sha256/' + sha).file_size and digest(data) == sha, 'archived object identity')
            if len(data) <= budget:
                while cache and cache_bytes + len(data) > budget:
                    cache_bytes -= len(cache.popitem(last=False)[1])
                cache[sha] = data; cache_bytes += len(data)
            return data
        # Authenticate every archive object, even files unused by proof parsing.
        for sha in {v['sha256'] for v in files.values()}: blob(sha)
        def reader(name):
            safe(name)
            if name in manifest:
                need(name not in files or files[name] == manifest[name], 'no trusted source shadowing')
                path = R.RELEASE / name if name == 'asset_provenance.json' else R.ROOT / name
                data = path.read_bytes(); need(row(data) == manifest[name], 'trusted release identity'); return data
            value = files[name]; data = blob(value['sha256'])
            need(len(data) == value['bytes'], 'archive retained byte count'); return data
        result = validate(reader, inventory['root'], inventory['output'], R.read(C.SNAPSHOT))
        need(result == R.strict(reader(inventory['output'] + '/evidence-inventory.json')), 'readback full validation inventory equality')
    print(json.dumps({'status': 'accepted_full_raw_readback_pending_independent_I25_and_audit',
        'pairs': result['pairs'], 'proofs': result['proofs'], 'archive': R.identity(archive), 'reader': R.identity(__file__)}), flush=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('action', choices=['export', 'verify'])
    ap.add_argument('archive', type=Path); ap.add_argument('--archive-sha')
    args = ap.parse_args()
    if args.action == 'export': export(args.archive.resolve())
    else:
        need(args.archive_sha is not None, 'explicit new archive SHA required')
        verify(args.archive.resolve(), args.archive_sha)
