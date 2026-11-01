"""Honest new staged entry with bit-identical cached interval evaluation."""
from functools import lru_cache
import hashlib
from pathlib import Path
import a5_checker_n8_staged as staged

HERE = Path(__file__).resolve()
ENTRY_SHA_AT_IMPORT = hashlib.sha256(HERE.read_bytes()).hexdigest()
BASE_SHA = '82385dd392513c476e83ed7c5a59c63e602e77d50279fb51a3976ac5857021ef'
require = staged.require
check = staged.check
require(staged.DRIVER_SHA_AT_IMPORT == BASE_SHA and staged.sha(staged.HERE.read_bytes()) == BASE_SHA,
        'cached entry has wrong staged base')
ORIGINAL_EVALUATE = check.evaluate
ORIGINAL_GUARD = staged.guard_sources
ORIGINAL_ATOMIC = staged.atomic_json
CONTROL_PATH = HERE.with_name('a5_checker_n8_staged_cached_controls.py')
CONTROL_SHA_AT_IMPORT = staged.sha(CONTROL_PATH.read_bytes()) if CONTROL_PATH.exists() else None

@lru_cache(maxsize=512)
def monomials(xlo, xhi, ylo, yhi, precision):
    require(precision == 160 and check.PRECISION == 160 and check.UNIT == 1 << 160,
            'cached precision changed')
    require(all(type(n) is int for n in (xlo, xhi, ylo, yhi)), 'noninteger cached endpoints')
    xx, yy = check.Interval(xlo, xhi), check.Interval(ylo, yhi)
    xp = tuple(xx.power(i) for i in range(9))
    yp = tuple(yy.power(j) for j in range(9))
    return tuple(tuple(a*b for b in yp) for a in xp)

def cached_evaluate(terms, box):
    """Same ordered per-term products and rounding as frozen evaluate."""
    xx, yy = box
    table = monomials(xx.lo, xx.hi, yy.lo, yy.hi, check.PRECISION)
    lo = hi = 0
    unit = check.UNIT
    for i, j, c in terms:
        m = table[i][j]
        products = (c.lo*m.lo, c.lo*m.hi, c.hi*m.lo, c.hi*m.hi)
        lo += min(products)//unit
        hi += check.ceil_div(max(products), unit)
    return check.Interval(lo, hi)

def guard_entry():
    ORIGINAL_GUARD()
    require(staged.sha(HERE.read_bytes()) == ENTRY_SHA_AT_IMPORT, 'cached execution entry changed')
    require(CONTROL_SHA_AT_IMPORT is not None and
            staged.sha(CONTROL_PATH.read_bytes()) == CONTROL_SHA_AT_IMPORT,
            'cached controls source changed')
    require(check.evaluate is cached_evaluate, 'cached runtime evaluator changed')

def tagged_atomic(path, value):
    guard_entry()
    # Metadata is added to the original result, never to any proof input.
    value.update(execution_entry_sha256=ENTRY_SHA_AT_IMPORT,
                 execution_entry_sha256_after=staged.sha(HERE.read_bytes()),
                 execution_entry_source_unchanged=True,
                 execution_cache_controls_sha256=CONTROL_SHA_AT_IMPORT,
                 base_staged_driver_sha256=BASE_SHA,
                 runtime_evaluate_replaced=True,
                 runtime_evaluate_backend='bit-identical cached monomials and per-term endpoint rounding',
                 runtime_evaluate_cache=monomials.cache_info()._asdict())
    return ORIGINAL_ATOMIC(path, value)

def install():
    require(check.evaluate is ORIGINAL_EVALUATE, 'unexpected evaluator before cache install')
    check.evaluate = cached_evaluate
    staged.guard_sources = guard_entry
    staged.atomic_json = tagged_atomic
    guard_entry()

if __name__ == '__main__':
    install()
    raise SystemExit(staged.main())
