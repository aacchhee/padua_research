"""Data-only complete-return checks using separately trusted released local code.
No archive code, compiler, native oracle, or scientific producer is executed.
"""
import argparse
from pathlib import Path
import sys
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import digest, encoded, manifest, strict
from plans import SMALL, LARGE, plan
from evidence import Access, require, safe, validate_attempt, validate_run_state

def verify(archive, package, expected_manifest_sha, partial=False):
    package = Path(package).resolve()
    frozen = (package / 'runtime_manifest.json').read_bytes()
    require(digest(frozen) == expected_manifest_sha, 'trusted released manifest SHA mismatch')
    m = manifest(package)
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        require(len(set(names)) == len(names), 'duplicate ZIP member')
        for name in names: safe(name)
        from archive_io import bounded_inventory, verify_payloads
        collection = bounded_inventory(z)
        verify_payloads(z, collection)
        require(collection['schema'] == 'padua-quiescent-return-v1' and collection['quiescent'] is True, 'collection schema/quiescence')
        require(collection['manifest_sha256'] == expected_manifest_sha, 'return source manifest mismatch')
        require(set(names) == set(collection['files']) | {'COLLECTION.json'}, 'incomplete/unmanifested return')
        for name, row in m['files'].items():
            data = z.read(name)
            require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'returned frozen bytes differ: ' + name)
        require(z.read('runtime_manifest.json') == frozen, 'returned manifest differs')
        groups = [r['group'] for r in collection['runs']]
        require(len(groups) == len(set(groups)) and set(groups) <= {'all', 'small', 'large', 'rehearsal'}, 'registered unique groups')
        if not partial:
            require(sorted(groups) in (['all'], ['large', 'small']), 'exact all OR disjoint small+large groups required')
        planned = set()
        seen = set(); completed = []; incomplete = []; never_started = []
        for record in collection['runs']:
            group = record['group']; prefix = 'outputs/' + group + '/'
            run = strict(z.read(prefix + 'run.json')); summary = strict(z.read(prefix + 'summary.json')); p = plan(group)
            require(run['plan'] == p and run['manifest'] == m, 'run plan/source mismatch')
            expected = digest(encoded({'manifest': m, 'plan': p, 'workers': run['workers'], 'writer_domain': run['writer_domain']}))
            require(run['identity'] == expected == record['identity'] == summary['identity'], 'run identity mismatch')
            require(summary.get('quiescent') is True and summary.get('ECHILD') is True, 'run not quiescent')
            if not partial:
                require(summary.get('first_failure') is None and summary.get('never_started') == [] and summary.get('cleanup_killed') == [], 'run incomplete/failed')
            actual = {int(name[len(prefix + 'jobs/'):].split('/')[0]) for name in names if name.startswith(prefix + 'jobs/')}
            require(actual <= set(p['degrees']), 'unregistered case')
            require(not planned.intersection(p['degrees']), 'overlapping registered plans')
            planned.update(p['degrees'])
            from archive_io import verify_admissions
            admitted = verify_admissions(z, prefix, actual)
            require(admitted <= set(p['degrees']), 'unregistered admission')
            missing = sorted(set(p['degrees']) - admitted)
            require(summary.get('never_started') == missing, 'exact never-started coverage')
            never_started.extend(missing)
            if not partial: require(not missing, 'exact case coverage')
            access = Access(package, run['package_root'], z.read)
            require(collection['writer_domain'] == run['writer_domain'] == access.json('outputs/writer-domain.json'), 'collection original writer domain')
            validate_run_state(run, summary, group, m, run['writer_domain'], run['package_root'])
            for n in sorted(admitted):
                require(n not in seen, 'duplicate degree'); seen.add(n)
                attempt_path = prefix + 'jobs/' + str(n) + '/attempt.json'
                candidate = strict(z.read(attempt_path)) if attempt_path in names else {}
                if partial and candidate.get('status') != 'awaits_independent_result_review':
                    incomplete.append(n); continue
                validate_attempt(access, group, n, run); completed.append(n)
            # Captured preflight/compiler-tool identities also require payloads.
            access.closure(run['provenance'])
            from archive_io import verify_history
            verify_history(z, prefix, access, run)
        if not partial: require(seen == set(SMALL + LARGE), 'exact280 coverage required')
    return {'validated_attempt_pairs': len(completed), 'completed_subset': sorted(completed), 'failed_or_interrupted': sorted(incomplete), 'never_started': sorted(never_started), 'complete280': not partial, 'known_portability': SMALL, 'residual_degrees': LARGE,
            'scope': 'data checks passed; distinct final result review remains required'}

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('archive')
    ap.add_argument('--package', required=True); ap.add_argument('--manifest-sha', required=True)
    ap.add_argument('--partial', action='store_true')
    a = ap.parse_args(); print(encoded(verify(a.archive, a.package, a.manifest_sha, a.partial)).decode())
