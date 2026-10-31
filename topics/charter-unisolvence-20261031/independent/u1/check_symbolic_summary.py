#!/usr/bin/env python3
"""Compare the producer's prose factor tables with its independently rerun JSON."""
import hashlib
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
raw_path = HERE / "producer-final-symbolic.json"
raw = json.loads(raw_path.read_text())


def C(H):
    return s.prod(H[i] - H[j] for i in range(len(H)) for j in range(i + 1, len(H)) if (i + j) % 2)


def A(H):
    return sum(H[::2]) - sum(H[1::2])


def B(H):
    E, O = H[::2], H[1::2]
    a, b = sum(E), sum(E[i] * E[j] for i in range(len(E)) for j in range(i + 1, len(E)))
    u, v = sum(O), s.prod(O)
    return s.expand(u * a - b - u * u + v)


def Q(H):
    E, O = H[::2], H[1::2]
    a, b, c = sum(E), sum(E[i] * E[j] for i in range(3) for j in range(i + 1, 3)), s.prod(E)
    u, v, w = sum(O), sum(O[i] * O[j] for i in range(3) for j in range(i + 1, 3)), s.prod(O)
    alpha, beta, gamma = a - u, v - b, c - w
    return s.expand(-(beta**2 + alpha * a * beta - alpha * gamma + alpha**2 * b))


def minor(H, r):
    numerators = {(3, 1): lambda: s.Integer(1), (4, 1): lambda: A(H),
                  (5, 1): lambda: B(H), (5, 2): lambda: s.Integer(1),
                  (6, 1): lambda: Q(H), (6, 2): lambda: A(H)}
    return numerators[len(H), r]() / C(H)


def differences(H, pairs, power):
    return s.prod((H[int(pair[0])] - H[int(pair[1])])**power for pair in pairs.split())


print("source_sha256", hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print("input_sha256", hashlib.sha256(raw_path.read_bytes()).hexdigest())
print("sympy", s.__version__)
for rec in raw["records"]:
    m, e = rec["m"], rec["parity"]
    X, Y = s.symbols(f"x0:{m + 1}"), s.symbols(f"y0:{m + 2}")
    env = {str(z): z for z in X + Y}
    for item in rec["axis_minors"]:
        H = X if item["axis"] == "X" else Y
        observed = s.sympify(item["minor"], locals=env)
        assert s.factor(observed - minor(H, item["r"])) == 0, (m, e, item)
    if m == 2:
        expected = (-1 if e == 0 else 1) * differences(X, "01 12", 1) * differences(X, "02", 2)
        expected *= differences(Y, "02", 2 - e) * differences(Y, "13", 1 + e) * A(Y)
    elif m == 3:
        expected = (-1)**e * differences(X, "01 03 12 23", 1)
        expected *= differences(X, "02", 3 - e) * differences(X, "13", 2 + e)
        expected *= differences(Y, "02 04 13 24", 2) * A(X) * B(Y)
    elif m == 4:
        expected = (-1)**e * differences(X, "01 03 12 14 23 34", 1)
        expected *= differences(X, "02 04 13 24", 3)
        expected *= differences(Y, "02 04 24", 3 - e) * differences(Y, "13 15 35", 2 + e)
        expected *= B(X) * A(Y) * Q(Y)
    observed = s.sympify(rec["determinant"], locals=env)
    assert s.factor(observed / expected) == 1, (m, e, "prose determinant table")
    print("PASS", "m", m, "parity", e, "compact axis minors and signed difference-factor table")
print("PASS all 6 symbolic summary cases")
