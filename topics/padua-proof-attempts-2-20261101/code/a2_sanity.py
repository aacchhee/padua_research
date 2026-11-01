"""Measured A2 sanity values using the positive corner formula.

Long-double arithmetic is a diagnostic, not interval arithmetic or a proof.
Small receipt only; n=2,...,64 and powers of two through1024.
"""
import hashlib
import json
import platform
from pathlib import Path

import numpy as np

LD = np.longdouble
PI = LD("3.1415926535897932384626433832795028841971693993751")
GAMMA = LD("0.57721566490153286060651209008240243104215933593992")


def evaluate(n):
    total = LD(0)
    for j in range(n + 1):
        k = np.arange(1 - j % 2, n + 1, 2, dtype=np.int64)
        a = LD(j) * PI / n
        b = k.astype(LD) * PI / (n + 1)
        ej = LD("0.5") if j in (0, n) else LD(1)
        eta = np.where(k == 0, LD("0.5"), LD(1))
        # Product form avoids subtraction of nearly equal cosines.
        f = np.cos(b / 2) ** 2 / (np.sin((a + b) / 2) * np.abs(np.sin((a - b) / 2)))
        total += np.sum(ej * eta * f, dtype=LD)
    corner = 4 * total / (LD(n) * (n + 1)) + LD(1) / (n + 1)
    r = np.arange(1, n + 1, 2, dtype=np.int64)
    d = np.where(r == n, LD("0.5"), LD(1))
    lebesgue_sum = 2 * np.sum(d / np.sin(r.astype(LD) * PI / (2 * n)), dtype=LD) / n
    logarithm = np.log(LD(n))
    bterm = 8 / PI ** 2 * (GAMMA + np.log(8 / PI))
    c1 = 2 / PI * (GAMMA + np.log(8 / PI))
    return {
        "n": n,
        "corner": str(corner),
        "same_mesh_square": str(lebesgue_sum ** 2),
        "corner_minus_square": str(corner - lebesgue_sum ** 2),
        "remainder_after_leading_and_b": str(corner - 4 / PI ** 2 * logarithm ** 2 - bterm * logarithm),
        "n_times_1d_error": str(n * (lebesgue_sum - 2 / PI * logarithm - c1)),
    }


if __name__ == "__main__":
    result = {
        "status": "MEASURED sanity only; no interval or proof claim",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "longdouble_bits": int(np.finfo(LD).nmant + 1),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "results": [evaluate(n) for n in list(range(2, 65)) + [128, 256, 512, 1024]],
    }
    print(json.dumps(result, indent=2))
