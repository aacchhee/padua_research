#!/usr/bin/env python3
"""Claude audit-01: ONE monolithic original Verifier.run on a closed-square n=8 artifact.

Auditor-written.  Builds a literal join of (archived interior proposal, auditor-
regenerated boundary proposal) and then calls the UNCHANGED frozen
a5_checker_n8.main() without --allow-partial, i.e. the complete original run
(interior leaves/roots/nodes, Verifier.boundaries, and every final summary
predicate in one process).  The only runtime substitution is the frozen,
previously controlled, bit-identical cached interval evaluator
(a5_checker_n8_staged_cached.cached_evaluate), installed exactly as that frozen
module does.  No acceptance predicate is touched.  The summary edge/corner/total
fields are copied from the boundary PROPOSAL, never from expected counts.
"""
import argparse, copy, gzip, hashlib, json, sys, time
from pathlib import Path

if not __debug__:
    raise RuntimeError('refuses optimized Python')

def sha(b): return hashlib.sha256(b).hexdigest()

def unique(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ValueError('duplicate key ' + k)
        out[k] = v
    return out

def load(path):
    raw = Path(path).read_bytes()
    data = gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw
    return raw, json.loads(data, object_pairs_hook=unique)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--interior', required=True); ap.add_argument('--interior-sha256', required=True)
    ap.add_argument('--boundary', required=True)
    ap.add_argument('--joined-out', required=True); ap.add_argument('--receipt', required=True)
    a = ap.parse_args()
    frozen = Path(a.repo) / 'topics/padua-proof-attempts-2-20261101/code'
    iraw, interior = load(a.interior)
    assert sha(iraw) == a.interior_sha256, 'interior hash'
    braw, boundary = load(a.boundary)
    assert not any(k in interior for k in ('edges', 'corners', 'boundary_summary'))
    joined = copy.deepcopy(interior)
    joined['edges'] = boundary['edges']; joined['corners'] = boundary['corners']
    joined['boundary_summary'] = boundary['summary']
    bs = boundary['summary']
    joined['summary'].update(edge=bs['edge'], corner=bs['corner'],
                             total=interior['summary']['interior'] + bs['edge'] + bs['corner'], complete=True)
    payload = gzip.compress(json.dumps(joined, separators=(',', ':'), sort_keys=True).encode(), mtime=0)
    Path(a.joined_out).write_bytes(payload)
    sys.path.insert(0, str(frozen))
    import a5_checker_n8_staged_cached as cached          # verifies frozen staged/main hashes on import
    check = cached.check
    assert check.evaluate is cached.ORIGINAL_EVALUATE
    check.evaluate = cached.cached_evaluate                # same substitution as cached.install()
    sources = {p: sha((frozen / p).read_bytes()) for p in
               ('a5_checker_n8.py', 'a5_checker_n8_staged.py', 'a5_checker_n8_staged_cached.py')}
    own = sha(Path(__file__).read_bytes())
    t0 = time.monotonic()
    sys.argv = ['a5_checker_n8.py', a.joined_out, '--output', a.receipt + '.checker.json']
    code = check.main()
    after = {p: sha((frozen / p).read_bytes()) for p in sources}
    res = json.loads(Path(a.receipt + '.checker.json').read_text())
    receipt = dict(format='claude-audit-01-monolithic-n8-v1', checker_exit=code,
                   wrapper_sha256=own, wrapper_sha256_after=sha(Path(__file__).read_bytes()),
                   frozen_sources_before=sources, frozen_sources_after=after,
                   evaluator='frozen a5_checker_n8_staged_cached.cached_evaluate (bit-identical cached monomials)',
                   interior_input_sha256=sha(iraw), interior_input_bytes=len(iraw),
                   boundary_input_sha256=sha(braw), boundary_input_bytes=len(braw),
                   joined_sha256=sha(payload), joined_bytes=len(payload),
                   allow_partial=False, wall_seconds=time.monotonic() - t0,
                   checker_result={k: res.get(k) for k in (
                       'accepted', 'count_certified', 'interior_complete', 'boundary_complete',
                       'complete_prefix_partition', 'verified_leaves', 'verified_patterns',
                       'verified_interior_maxima_enclosures', 'verified_edge_maxima_enclosures',
                       'verified_corner_maxima', 'verified_edge_patterns', 'corner_active_patterns',
                       'edge_dispositions', 'total_maxima', 'dispositions', 'verified_node_leaves',
                       'verified_node_records', 'verified_direction_breakpoints', 'checker_sha256',
                       'checker_source_unchanged', 'python', 'sympy', 'python_flint', 'FLINT', 'error', 'seconds')})
    Path(a.receipt).write_text(json.dumps(receipt, indent=1, sort_keys=True) + '\n')
    print(json.dumps(receipt, sort_keys=True), flush=True)
    return code

if __name__ == '__main__':
    sys.exit(main())
