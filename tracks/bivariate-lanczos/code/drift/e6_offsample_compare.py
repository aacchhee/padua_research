"""Response-02 (A02-L5): leaf-by-leaf comparison of the response-02 rerun of e6_offsample.py with the
frozen response-01 evidence. The rerun exists because the comments of e6_offsample.py were corrected
(midpoint-law wording) and its sha256 is pinned in the frozen response-01 evidence/manifest.

Run from the repository root:
  python3 -I tracks/bivariate-lanczos/code/drift/e6_offsample_compare.py [--embed]

Compares every JSON leaf (exact equality, no tolerance); only the listed provenance fields are masked.
With --embed the result is stored under the key 'response02_comparison_to_response01' of the rerun file
(a post-run addition; the rest of the file is the unmodified script output).
"""
import hashlib, json, pathlib, sys

EV = pathlib.Path('topics/padua-lanczos-drift-20261101/evidence')
OLD, NEW = EV / 'response-01-e6-offsample.json', EV / 'response-02-e6-offsample-rerun.json'
MASK = ['/command', '/python', '/elapsed_seconds', '/code_sha256/e6_offsample.py']


def leaves(o, p=''):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from leaves(v, p + '/' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from leaves(v, p + '/' + str(i))
    else:
        yield p, o


def main():
    a = json.loads(OLD.read_text())
    b = json.loads(NEW.read_text())
    b.pop('response02_comparison_to_response01', None)
    A, B = dict(leaves(a)), dict(leaves(b))
    assert set(A) == set(B), 'leaf sets differ'
    cmp_keys = [k for k in A if k not in MASK]
    unequal = [k for k in cmp_keys if A[k] != B[k]]
    isnum = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)
    num = [k for k in cmp_keys if isnum(A[k])]
    res = {'old_file': str(OLD), 'old_sha256': hashlib.sha256(OLD.read_bytes()).hexdigest(),
           'masked_fields': MASK, 'total_leaves': len(A), 'compared_leaves': len(cmp_keys),
           'compared_numeric_leaves': len(num), 'unequal_compared_leaves': unequal,
           'all_compared_equal': not unequal,
           'masked_values_old': {k: A[k] for k in MASK}, 'masked_values_new': {k: B[k] for k in MASK},
           'note': 'python/numpy/scipy versions are identical (numpy and scipy are compared, not masked); '
                   'masked: command (output path differs), code hash (comments edited), elapsed time.'}
    print(json.dumps({k: v for k, v in res.items() if not k.startswith('masked_values')}, indent=1))
    if '--embed' in sys.argv:
        raw = json.loads(NEW.read_text())
        raw['response02_comparison_to_response01'] = res
        NEW.write_text(json.dumps(raw, indent=1) + '\n')
    return 0 if not unequal else 1


if __name__ == '__main__':
    sys.exit(main())
