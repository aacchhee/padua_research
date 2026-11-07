"""Verify all histories locally; return all proofs and two sampled histories."""
from datetime import datetime, timezone
import io
import os
from pathlib import Path
import random
import socket
import sys
import tarfile
from common import HERE, digest, encoded, exclusive, lock, manifest, read
from evidence import Access, safe, validate_attempt, validate_run_state, require
from plans import SMALL, LARGE, plan
from storage import sha


def collect(destination, root=HERE):
    root = Path(root).resolve(); destination = Path(destination).resolve()
    require(destination != root and root not in destination.parents, 'return destination must be outside package')
    with lock(root / 'outputs'):
        m = manifest(root); manifest_bytes = (root / 'runtime_manifest.json').read_bytes()
        domain = read(root / 'outputs/writer-domain.json')
        needed = {'runtime_manifest.json', 'outputs/writer-domain.json', 'SOURCE_CUSTODY.json'}
        runs = []; completed = []; unfinished = []; validations = []; locations = {}
        for directory in sorted((root / 'outputs').iterdir()):
            if not directory.is_dir(): continue
            group = directory.name
            require(group in ('all', 'small', 'large', 'rehearsal'), 'unknown output group')
            run = read(directory / 'run.json'); summary = read(directory / 'summary.json')
            # No invented ECHILD attestation or hard-kill recovery. An unclean
            # campaign may be rerun fresh after its writers have stopped.
            require(summary.get('quiescent') is True and summary.get('ECHILD') is True,
                    'Campaign did not stop cleanly: stop writers and rerun the cheap cohort fresh')
            validate_run_state(run, summary, group, m, domain, run['package_root'])
            require(not summary.get('cleanup_error'), 'unclean campaign: stop writers and rerun fresh')
            runs.append({'group': group, 'identity': run['identity'], 'original_summary': summary})
            needed.update(p.relative_to(root).as_posix() for p in directory.rglob('*')
                          if p.is_file() and '/jobs/' not in p.relative_to(root).as_posix())
            access = Access(root, run['package_root'])
            for n in plan(group)['degrees']:
                case = directory / 'jobs' / str(n)
                if not case.exists(): continue
                prefix = case.relative_to(root).as_posix()
                try: status = read(case / 'attempt.json').get('status')
                except (OSError, ValueError): status = 'in_progress/incomplete'
                if status != 'awaits_independent_result_review':
                    needed.update(p.relative_to(root).as_posix() for p in case.glob('*.json') if p.is_file())
                    unfinished.append({'group': group, 'n': n, 'status': status}); continue
                require(n not in locations, 'duplicate completed degree')
                validate_attempt(access, group, n, run)
                completed.append(n); locations[n] = (group, run)
                for name in ('started.json', 'wrapper-exit.json', 'attempt.json', 'produce-exit.json', 'verify-exit.json'):
                    needed.add(prefix + '/' + name)
                hashes = {'n': n, 'group': group, 'full_history_validated_on_server': True}
                for mode in ('produce', 'verify'):
                    for name in ('essential-receipt.json', 'final-accounting.json', 'summary.json', 'preregistration.json'):
                        needed.add(prefix + '/' + mode + '/' + name)
                    hashes[mode + '_receipt_sha256'] = sha(case / mode / 'essential-receipt.json')
                    hashes[mode + '_raw_sha256'] = sha(case / mode / 'raw-evidence.json')
                hashes['attempt_sha256'] = sha(case / 'attempt.json'); validations.append(hashes)
            print('Server checked', group, 'completed pairs:', len(completed), flush=True)
        require(runs, 'no campaign outputs')
        eligible = sorted(n for n in completed if n in LARGE)
        coverage = {'manifest_sha256': digest(manifest_bytes), 'runs': runs,
                    'completed': sorted(completed), 'eligible_residual': eligible}
        selection_root = root / 'compact-selections'; selection_root.mkdir(exist_ok=True)
        selection_file = selection_root / (digest(encoded(coverage)) + '.json')
        if not selection_file.exists():
            seed = os.urandom(32)
            selected = random.Random(seed).sample(eligible, min(2, len(eligible)))
            exclusive(selection_file, {'coverage': coverage, 'seed_hex': seed.hex(),
                       'algorithm': 'random.Random(bytes.fromhex(seed_hex)).sample(sorted_eligible,min(2,len))',
                       'python': sys.version, 'sampled_residual_degrees': selected})
        selection = read(selection_file)
        require(selection['coverage'] == coverage, 'persisted sample coverage mismatch')
        selected = selection['sampled_residual_degrees']
        require(selected == random.Random(bytes.fromhex(selection['seed_hex'])).sample(eligible, min(2, len(eligible))), 'sample draw mismatch')
        needed.add(selection_file.relative_to(root).as_posix())
        # Track actual full-validator reads, including out-of-job immutable
        # builds and external SHA objects. Known frozen files resolve from the
        # separately trusted delivered package instead of being retransmitted.
        for n in selected:
            group, run = locations[n]
            case = root / 'outputs' / group / 'jobs' / str(n)
            needed.update(p.relative_to(root).as_posix() for p in case.rglob('*') if p.is_file())
            for file in case.glob('*/*-build.json'):
                work = Path(read(file)['workdir'])
                relative = work.relative_to(Path(run['package_root']))
                needed.update(p.relative_to(root).as_posix() for p in (root / relative).rglob('*') if p.is_file())
            def tracking_read(name):
                safe(name)
                if name not in m['files']: needed.add(name)
                return (root / name).read_bytes()
            access = Access(root, run['package_root'], tracking_read)
            validate_attempt(access, group, n, run); access.closure(run['provenance'])
        inventory = {name: {'bytes': (root / safe(name)).stat().st_size, 'sha256': sha(root / name)} for name in sorted(needed)}
        receipt = {'schema': 'padua-compact-return-v1', 'manifest_sha256': digest(manifest_bytes),
                   'runs': runs, 'completed_degrees': sorted(completed), 'unfinished': unfinished,
                   'full280_data_validated_on_server': set(completed) == set(SMALL + LARGE),
                   'never_started': {r['group']: sorted(set(plan(r['group'])['degrees']) -
                                     {int(p.name) for p in (root / 'outputs' / r['group'] / 'jobs').glob('*') if p.is_dir()}) for r in runs},
                   'validation_hashes': validations, 'selection': selection, 'files': inventory,
                   'full_history_scope': 'all completed pairs validated on producing server; only sampled full histories returned; other histories remain on Syvert',
                   'source_regeneration': 'released source manifest plus pinned offline packages and unchanged engine CLI; no unsampled cold-storage claim'}
        destination.mkdir(parents=True, exist_ok=True)
        archive = destination / (socket.gethostname().split('.')[0] + '-padua-compact-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ') + '.tar.gz')
        aliases = {}
        with tarfile.open(archive, 'x:gz', dereference=True) as tar:
            for name, row in inventory.items():
                path = root / name
                require(path.resolve().is_relative_to(root), 'external payload symlink')
                info = tar.gettarinfo(str(path.resolve()), arcname=name)
                require(info.isfile(), 'bundle requires regular payload files')
                key = (row['bytes'], row['sha256'])
                if key in aliases:
                    info.type = tarfile.LNKTYPE; info.linkname = aliases[key]; info.size = 0
                    tar.addfile(info)
                else:
                    aliases[key] = name
                    with path.open('rb') as stream: tar.addfile(info, stream)
                require(sha(path) == row['sha256'], 'payload changed during collection')
            data = encoded(receipt); info = tarfile.TarInfo('COMPACT.json'); info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
        size = archive.stat().st_size
        print('Compact return:', archive, 'bytes:', size, 'sampled residual:', selected,
              '(over preferred25MB)' if size > 25_000_000 else '', flush=True)
        return archive
