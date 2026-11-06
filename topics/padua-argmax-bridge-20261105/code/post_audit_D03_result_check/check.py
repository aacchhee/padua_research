"""Independent saved-record check only; never loads the pilot or native code."""
import collections
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
start = time.process_time()
seen = set()

def verify(obj):
    if isinstance(obj, dict):
        if {'path', 'bytes', 'sha256'} <= obj.keys() and isinstance(obj['path'], str):
            p = Path(obj['path'])
            if not p.is_absolute():
                p = ROOT / p
            if (str(p), obj['sha256']) not in seen:
                b = p.read_bytes()
                assert len(b) == obj['bytes']
                assert hashlib.sha256(b).hexdigest() == obj['sha256'], p
                seen.add((str(p), obj['sha256']))
        for x in obj.values():
            verify(x)
    elif isinstance(obj, list):
        for x in obj:
            verify(x)

receipt = json.loads((TOPIC / 'evidence/d03-near-only.json').read_text())
verify(receipt)
for key in ('raw_artifact_manifest', 'header_closure'):
    verify(json.loads((ROOT / receipt[key]['path']).read_text()))
for entry in receipt['runtime_closures']:
    verify(json.loads((ROOT / entry['path']).read_text()))

for summary in receipt['rows']:
    d = json.loads(Path(summary['detail']['path']).read_text())
    rho = F(d['rho'])
    frontier = {(i, ''): ([-rho, F(0)] if i < 2 else [F(0), rho]) +
                ([-rho, F(0)] if i % 2 == 0 else [F(0), rho]) for i in range(4)}
    native = []
    accepted = []
    for row in d['trace']:
        key = row['root'], row['path']
        b = frontier.pop(key)
        assert list(map(F, row['box'])) == b
        if row['status'] == 'split':
            i = 0 if b[1]-b[0] >= b[3]-b[2] else 2
            mid = (b[i]+b[i+1])/2
            for bit in (0, 1):
                child = b.copy()
                child[i+1 if bit == 0 else i] = mid
                frontier[(key[0], key[1]+str(bit))] = child
        else:
            accepted.append(row)
        if row['status'] == 'outside-near':
            def ma(a, z): return F(0) if a <= 0 <= z else min(abs(a), abs(z))
            assert ma(*b[:2])+ma(*b[2:]) > rho
        else:
            assert all(math.isfinite(x) for x in row['bounds'])
            native.append(row)
    assert accepted == d['leaves']
    assert frontier == {(x['root'], x['path']): list(map(F, x['box'])) for x in d['pending']}
    assert len(d['trace']) == summary['visited'] == 128
    assert len(native) == summary['native_calls']
    assert dict(collections.Counter(x['status'] for x in accepted)) == summary['leaf_counts']
    assert len(frontier) == summary['unresolved_frontier'] > 0
    assert abs(sum(x['native_cpu_seconds'] for x in native)-summary['native_calls_cpu_seconds']) < 1e-8
    assert sum(x['bounds'][3] != 0 for x in native) == summary['profile_calls']
    for status, count in summary['per_status_native_accounting'].items():
        rows = [x for x in d['trace'] if x['status'] == status]
        assert len(rows) == count['visited_boxes']
        assert sum('bounds' in x for x in rows) == count['native_calls']
        assert abs(sum(x.get('native_cpu_seconds', 0) for x in rows)-count['native_CPU_seconds']) < 1e-8
    for name, flag in [('computed', True), ('not_computed', False)]:
        rows = [x for x in native if bool(x['bounds'][3]) == flag]
        count = summary['profile_flag_accounting'][name]
        assert len(rows) == count['native_calls']
        assert abs(sum(x['native_cpu_seconds'] for x in rows)-count['native_CPU_seconds']) < 1e-8
    assert not summary['complete_float_partition'] and summary['exact_checker_cpu_seconds'] is None
    print('rho', float(rho), 'visits', len(d['trace']), 'frontier', len(frontier), 'PASS')
assert receipt['aggregate_runner_CPU_seconds'] < receipt['CPU_cap']
assert receipt['exit_status'] == 0 and receipt['retries'] == 0 and not receipt['failures']
print('Verified identities', len(seen), 'CPU seconds', time.process_time()-start)
