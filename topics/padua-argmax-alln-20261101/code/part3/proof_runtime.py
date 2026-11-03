"""Narrow source compatibility for adding an optimization refusal to n2.

The frozen general/D3 certificates pin finite_n2_exact.py as a producer
dependency. Its arithmetic is unchanged: the only admitted historical
source identity is the exact current file with this one guard removed.
The D3 certificate also pins its checker. For that one key, reverse only
the enumerated guard/import/metadata-call edits below. All other entries
must remain exactly equal. This is metadata compatibility, never permission
to ignore a mathematical source change.
"""
import hashlib
from pathlib import Path

N2_OPTIMIZATION_GUARD = (
    'if not __debug__:\n'
    '    raise RuntimeError("Scientific verification requires Python assertions; '
    'do not use -O or PYTHONOPTIMIZE.")\n\n'
).encode()

D3_COMPAT_IMPORT = b'from proof_runtime import guard_compatible_sources\n'
D3_CURRENT_SOURCE_CHECK = (
    "    assert guard_compatible_sources(data['source_sha256'], c.source_hashes(),\n"
    "                                    Path(c.b.__file__).with_name('finite_n2_exact.py'),\n"
    "                                    'code/part3/finite_n2_exact.py',\n"
    "                                    d3_checker_path=Path(__file__))\n"
).encode()
D3_HISTORICAL_SOURCE_CHECK = b"    assert data['source_sha256'] == c.source_hashes()\n"


def guard_compatible_sources(recorded, actual, n2_path, n2_key,
                             d3_checker_path=None):
    if recorded == actual:
        return True
    current = Path(n2_path).read_bytes()
    if (current.count(N2_OPTIMIZATION_GUARD) != 1
            or actual.get(n2_key) != hashlib.sha256(current).hexdigest()):
        return False
    historical = dict(actual)
    historical[n2_key] = hashlib.sha256(
        current.replace(N2_OPTIMIZATION_GUARD, b'', 1)).hexdigest()
    if d3_checker_path is not None:
        checker = Path(d3_checker_path).read_bytes()
        key = 'code/gated/d3_edge_check.py'
        if (actual.get(key) != hashlib.sha256(checker).hexdigest()
                or any(checker.count(block) != 1 for block in
                       (N2_OPTIMIZATION_GUARD, D3_COMPAT_IMPORT,
                        D3_CURRENT_SOURCE_CHECK))):
            return False
        checker = checker.replace(N2_OPTIMIZATION_GUARD, b'', 1)
        checker = checker.replace(D3_COMPAT_IMPORT, b'', 1)
        checker = checker.replace(D3_CURRENT_SOURCE_CHECK,
                                  D3_HISTORICAL_SOURCE_CHECK, 1)
        historical[key] = hashlib.sha256(checker).hexdigest()
    return recorded == historical
