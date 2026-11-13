"""Finite runtime probes; these do not establish universal IEEE conformance.

Supplement to frozen I25 code, not a change to its historical execution.
Run with python3 -E -B; no certificate input or native engine is used.
"""
import json
import sys

import numpy as np

from controls import arithmetic_controls


def main():
    if sys.flags.optimize:
        raise SystemExit('optimization is not permitted for runtime probes')
    a = np.array([1.0])
    half = np.array([2.0**-53])
    tiny = np.array([2.0**-1022])
    checks = {
        'ties_even_down': bool((a + half)[0] == 1.0),
        'ties_even_up': bool(((a + 2*half) + half)[0] == 1 + 2.0**-51),
        # Compare integer encodings: DAZ can make zero and a subnormal
        # compare equal in floating-point even when FTZ erased the result.
        'gradual_underflow': int((tiny/2).view(np.uint64)[0]) == 0x0008000000000000,
        'smallest_subnormal': int(np.nextafter(np.float64(0), np.float64(1))
                                  .view(np.uint64)) == 0x0000000000000001,
    }
    if not all(checks.values()):
        raise SystemExit('runtime probe failed: ' + repr(checks))
    controls = arithmetic_controls()
    print(json.dumps({'python': sys.version, 'numpy': np.__version__,
                      'arithmetic_controls': len(controls), 'runtime_probes': checks,
                      'scope': 'finite runtime probes; no witness replay'}, indent=2))


if __name__ == '__main__':
    main()
