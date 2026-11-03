#!/usr/bin/env python3
"""Mathematical scratch: MEASURED coefficient identity diagnostic, not a certifier."""
from pathlib import Path
import sys
import numpy as np

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO / "topics/padua-argmax-alln-20261101/code"))
import maj


def diagnostic(n):
    m, total = n + 1, n * (n + 1)
    theta, phi, weights, kernel, modes = maj.setup(n)
    j, k = np.indices(weights.shape)
    signs = (-1.0) ** (n + j) * np.where(j >= k, 1.0, -1.0)
    signs[:, 0] = (-1.0) ** (n + 1)
    signs[0, 0] = (-1.0) ** n
    direct = kernel * (
        np.cos(np.outer(theta, modes)).T
        @ (weights * signs)
        @ np.cos(np.outer(phi, modes))
    ) * (-1.0) ** (modes[:, None] + modes[None, :])
    formula = np.zeros_like(direct)
    for a in range(n + 1):
        for b in range(n - a + 1):
            hb = 1 if b == 0 else 2
            if a == n:
                formula[a, b] = 1 / total
            elif a == 0:
                epsilon = (-1) ** (n + b)
                formula[a, b] = hb / total * (
                    (1 + epsilon) / (1 + np.cos(b * np.pi / m)) - n * epsilon
                )
            else:
                x, y = np.cos(a * np.pi / n), np.cos(b * np.pi / m)
                formula[a, b] = 2 * hb / total * (
                    1 + (-1) ** (n + a + b) * x
                ) / (x + y)
    error = np.max(np.abs(direct - formula))
    slope_x = -np.sum(direct * modes[:, None] ** 2) / n**2
    slope_y = -np.sum(direct * modes[None, :] ** 2) / n**2
    print(f"n={n:2d} max_error={error:.3e} A/n^2={slope_x:.12f} "
          f"B/n^2={slope_y:.12f} Lambda={direct.sum():.12f}")


if __name__ == "__main__":
    for degree in (2, 3, 4, 5, 8, 16, 32, 64):
        diagnostic(degree)
