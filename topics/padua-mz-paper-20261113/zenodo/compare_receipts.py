#!/usr/bin/env python3
"""Compare a fresh JSON receipt with a reference receipt, ignoring run-specific fields.

Usage: compare_receipts.py FRESH REFERENCE
Fields ignored (dotted path, regex): timings, memory, commands, file paths,
interpreter/library versions, platform strings, hashes of other receipts, and
gzip-container hashes and sizes (these depend on the zlib build; the
decompressed payload hashes are compared separately). Everything else, including
exact numerators/denominators, enclosures, signs, code and payload hashes,
must be identical. Exit status 0 on agreement, 1 otherwise.
"""
import gzip, json, re, sys

IGNORE = re.compile(r'(^|\.)(seconds|elapsed_seconds|stderr|cpu_seconds|wall_seconds|total_seconds|ball_table_seconds|phase_seconds|times|'
                    r'peak_rss_kib|peak_self_rss_kib|command|compile_command|python|platform|dependencies|numpy|scipy|'
                    r'flint|python_flint|sympy|gmp|started_utc|finished_utc|path|scratch|bulk|binary_sha256|'
                    r'producer_receipt_sha256|producer_receipt|witness_sha256|status)(\.|$)'
                    r'|(^|\.)witness\.(sha256|bytes)$')

def load(p):
    opener = gzip.open if p.endswith('.gz') else open
    with opener(p, 'rt') as f:
        return json.load(f)

def walk(a, b, path, diffs):
    if IGNORE.search(path):
        return
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            sub = f'{path}.{k}' if path else k
            if IGNORE.search(sub):
                continue
            if k not in a or k not in b:
                diffs.append(f'{sub}: present only in {"reference" if k not in a else "fresh"}')
            else:
                walk(a[k], b[k], sub, diffs)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            diffs.append(f'{path}: list length {len(a)} != {len(b)}')
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f'{path}[{i}]', diffs)
    elif a != b:
        diffs.append(f'{path}: {str(a)[:80]!r} != {str(b)[:80]!r}')

def main():
    fresh, ref = sys.argv[1], sys.argv[2]
    diffs = []
    walk(load(fresh), load(ref), '', diffs)
    if diffs:
        print(f'DIFFER {fresh} vs {ref}')
        for d in diffs[:40]:
            print('  ', d)
        sys.exit(1)
    print(f'AGREE  {fresh} vs {ref}')

if __name__ == '__main__':
    main()
