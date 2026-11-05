"""Strict certificate parser and independent compiled GMP replay driver.

No reference/producer arithmetic modules are imported. The original v1
provenance convention is checked against read-only repository source bytes.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import time

REPO = Path(__file__).resolve().parents[4]
REF = REPO / 'topics/padua-argmax-alln-20261101/code/part3'
DEPENDENCY = REPO / 'topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md'
PIN = '328be35e55143013047ec03a70e9906e82b95353'


def need(value, message):
    if not value:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pairs(items):
    result = {}
    for key, value in items:
        need(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def load(path):
    payload = Path(path).read_bytes()
    if str(path).endswith('.gz'):
        payload = gzip.decompress(payload)
    return json.loads(payload, object_pairs_hook=pairs,
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite JSON')))


def provenance(data):
    need(data['format'] == 'padua-part3-general-certificate-v1', 'format')
    need(data['source_head'] == PIN, 'source head')
    names = ('finite_bernstein.py', 'finite_general.py', 'finite_general_run.py', 'finite_n2_exact.py')
    actual = {name: digest(REF/name) for name in names}
    historical = dict(actual)
    guard = ('if not __debug__:\n    raise RuntimeError("Scientific verification requires Python assertions; '
             'do not use -O or PYTHONOPTIMIZE.")\n\n').encode()
    raw = (REF/'finite_n2_exact.py').read_bytes()
    need(raw.count(guard) == 1, 'n2 historical compatibility guard')
    historical['finite_n2_exact.py'] = hashlib.sha256(raw.replace(guard, b'', 1)).hexdigest()
    need(data['source_sha256'] in (actual, historical), 'source hashes')
    need(data['dependency_sha256'] == digest(DEPENDENCY), 'dependency hash')
    need(data['cardinal_constructor'] == 'PD-T101 corrected kernel; rigorous rational cosine intervals', 'constructor')


def check(data, binary, cache=None):
    need(type(data) is dict, 'object required')
    provenance(data)
    n = data['n']
    need(type(n) is int and 2 <= n <= 100, 'degree')
    need(type(data['leaves']) is list and type(data['pending']) is list, 'frontier lists')
    leaves = {}
    pending = set()
    def path(p):
        need(type(p) is str and len(p) <= 100 and set(p) <= {'0', '1'}, 'path')
        return p
    for row in data['leaves']:
        need(type(row) is dict, 'leaf object')
        p = path(row['path'])
        need(p not in leaves, 'duplicate leaf')
        need(row.get('kind') in ('bound', 'corner'), 'leaf kind')
        key = 'upper' if row['kind'] == 'bound' else 'upper_away_from_vertex'
        need(type(row.get(key)) is int, 'integer bound')
        if row['kind'] == 'corner':
            need(type(row.get('corner')) is list and len(row['corner']) == 2
                 and all(type(x) is int for x in row['corner']), 'corner coordinates')
        leaves[p] = row
    for p in data['pending']:
        p = path(p)
        need(p not in pending and p not in leaves, 'overlap')
        pending.add(p)
    frontier = set(leaves) | pending
    need(frontier, 'empty frontier')
    ancestors = {p[:i] for p in frontier for i in range(len(p))}
    need(not (ancestors & frontier), 'ancestor overlap')
    # Tree cardinality plus prefix-free paths implies a full binary prefix cover.
    need(len(frontier) == len(ancestors)+1, 'uncovered partition')
    key = (n, tuple(sorted(frontier)))
    if cache is None or key not in cache:
        proc = subprocess.run([str(binary), str(n)], input=''.join((p or '-')+'\n' for p in sorted(frontier)),
                              text=True, capture_output=True, check=True)
        rows = [json.loads(line) for line in proc.stdout.splitlines()]
        replay = rows[0], {row['path']: row for row in rows[1:]}
        if cache is not None:
            cache[key] = replay
    else:
        replay = cache[key]
    metadata, verified = replay
    for k, v in metadata.items():
        # Python equality aliases bool/int; require matching structural types.
        need(json.dumps(data[k], sort_keys=True) == json.dumps(v, sort_keys=True), 'metadata '+k)
    corners = [[-1, -1], [1, -1] if n % 2 == 0 else [-1, 1]]
    need(data['corners'] == corners and all(type(x) is int for e in data['corners'] for x in e), 'corners')
    need(set(verified) == frontier, 'reached frontier')
    counts = Counter()
    for p, row in leaves.items():
        need(row == verified[p], 'leaf verdict '+p)
        counts[row['kind']] += 1
    counts['splits'] = len(ancestors)
    if pending:
        counts['pending'] = len(pending)
    need(type(data['complete']) is bool and data['complete'] == (not pending), 'complete flag')
    need(data['accepted'] is False, 'producer approval')
    need(type(data['statistics']) is dict, 'statistics')
    for k in ('bound', 'corner', 'splits'):
        value = data['statistics'].get(k, 0)
        need(type(value) is int and value == counts[k], 'counter '+k)
    if not pending:
        need({tuple(row['corner']) for row in leaves.values() if row['kind']=='corner'} == set(map(tuple,corners)), 'corner coverage')
    return dict(n=n, accepted=not pending, complete_partition=True,
                all_supplied_bounds_verified=True, counts=dict(counts))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--binary', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    result = check(load(args.certificate), args.binary)
    result.update(format='padua-native-independent-check-v1', certificate_sha256=digest(args.certificate),
                  checker_sha256=digest(__file__), kernel_sha256=digest(Path(__file__).with_name('kernel.cpp')),
                  binary_sha256=digest(args.binary), seconds=time.monotonic()-started)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, sort_keys=True))

if __name__ == '__main__':
    main()
