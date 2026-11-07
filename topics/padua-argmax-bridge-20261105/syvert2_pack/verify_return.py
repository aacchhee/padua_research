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
from evidence import Access, require, safe, validate_attempt

def verify(archive, package, expected_manifest_sha):
    package = Path(package).resolve()
    frozen = (package / 'runtime_manifest.json').read_bytes()
    require(digest(frozen) == expected_manifest_sha, 'trusted released manifest SHA mismatch')
    m = manifest(package)
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        require(len(set(names)) == len(names), 'duplicate ZIP member')
        for name in names: safe(name)
        collection = strict(z.read('COLLECTION.json'))
        require(collection['schema'] == 'padua-quiescent-return-v1' and collection['quiescent'] is True, 'collection schema/quiescence')
        require(collection['manifest_sha256'] == expected_manifest_sha, 'return source manifest mismatch')
        require(set(names) == set(collection['files']) | {'COLLECTION.json'}, 'incomplete/unmanifested return')
        for name, row in collection['files'].items():
            data = z.read(name)
            require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'return bytes differ: ' + name)
        for name, row in m['files'].items():
            data = z.read(name)
            require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'returned frozen bytes differ: ' + name)
        require(z.read('runtime_manifest.json') == frozen, 'returned manifest differs')
        groups = [r['group'] for r in collection['runs']]
        require(sorted(groups) in (['all'], ['large', 'small']), 'exact all OR disjoint small+large groups required')
        seen = set()
        for record in collection['runs']:
            group = record['group']; prefix = 'outputs/' + group + '/'
            run = strict(z.read(prefix + 'run.json')); summary = strict(z.read(prefix + 'summary.json')); p = plan(group)
            require(run['plan'] == p and run['manifest'] == m, 'run plan/source mismatch')
            expected = digest(encoded({'manifest': m, 'plan': p, 'workers': run['workers']}))
            require(run['identity'] == expected == record['identity'] == summary['identity'], 'run identity mismatch')
            require(summary.get('first_failure') is None and summary.get('never_started') == [] and
                    summary.get('quiescent') is True and summary.get('ECHILD') is True and summary.get('cleanup_killed') == [], 'run incomplete/failed')
            actual = {int(name[len(prefix + 'jobs/'):].split('/')[0]) for name in names if name.startswith(prefix + 'jobs/')}
            require(actual == set(p['degrees']), 'exact case coverage')
            access = Access(package, run['package_root'], z.read)
            for n in p['degrees']:
                require(n not in seen, 'duplicate degree'); seen.add(n)
                validate_attempt(access, group, n, run)
            # Captured preflight/compiler-tool identities also require payloads.
            access.closure(run['provenance'])
        require(seen == set(SMALL + LARGE), 'exact280 coverage required')
    return {'validated_attempt_pairs': len(seen), 'known_portability': SMALL, 'residual_degrees': LARGE,
            'scope': 'data checks passed; distinct final result review remains required'}

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('archive')
    ap.add_argument('--package', required=True); ap.add_argument('--manifest-sha', required=True)
    a = ap.parse_args(); print(encoded(verify(a.archive, a.package, a.manifest_sha)).decode())
