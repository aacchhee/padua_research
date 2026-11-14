#!/usr/bin/env python3
"""Compare a fresh JSON receipt with a reference receipt, ignoring run-specific fields.

Usage: compare_receipts.py FRESH REFERENCE [--ignore REGEX ...]
Fields ignored (dotted path, regex): timings, memory, commands, file paths,
interpreter/library versions, platform strings, hashes of other receipts, and
gzip-container hashes and sizes (these depend on the zlib build; the
decompressed payload hashes are compared separately). Everything else, including
exact numerators/denominators, enclosures, signs, code and payload hashes,
must be identical. Each --ignore REGEX adds a dotted-path pattern to skip; the
calling script states why (for example, a replay from an archived witness has
no source vector). Exit status 0 on agreement, 1 otherwise.
"""
import gzip, json, re, sys

IGNORE = re.compile(r'(^|\.)(seconds|elapsed_seconds|stderr|threads|cpu_seconds|wall_seconds|total_seconds|ball_table_seconds|phase_seconds|times|'
                    r'peak_rss_kib|peak_self_rss_kib|command|compile_command|compiler|environment|python|platform|dependencies|numpy|scipy|'
                    r'flint|python_flint|sympy|gmp|started_utc|finished_utc|path|scratch|bulk|binary_sha256|'
                    r'producer_receipt_sha256|producer_receipt|witness_sha256|status)(\.|$)'
                    r'|(^|\.)witness\.(sha256|bytes)$|_path$')

def load(p):
    opener = gzip.open if p.endswith('.gz') else open
    with opener(p, 'rt') as f:
        return json.load(f)

EXTRA = []

def ignored(path):
    return bool(IGNORE.search(path)) or any(re.search(x, path) for x in EXTRA)

def walk(a, b, path, diffs):
    if ignored(path):
        return
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            sub = f'{path}.{k}' if path else k
            if ignored(sub):
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
    args = sys.argv[1:]
    fresh, ref = args[0], args[1]
    rest = args[2:]
    while rest:
        if rest[0] != '--ignore' or len(rest) < 2:
            sys.exit('usage: compare_receipts.py FRESH REFERENCE [--ignore REGEX ...]')
        EXTRA.append(rest[1]); rest = rest[2:]
    diffs = []
    walk(load(fresh), load(ref), '', diffs)
    if diffs:
        print(f'DIFFER {fresh} vs {ref}')
        for d in diffs[:40]:
            print('  ', d)
        sys.exit(1)
    note = f' (also ignoring: {", ".join(EXTRA)})' if EXTRA else ''
    print(f'AGREE  {fresh} vs {ref}{note}')

if __name__ == '__main__':
    main()
