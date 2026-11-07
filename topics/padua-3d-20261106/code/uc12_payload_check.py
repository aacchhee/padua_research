#!/usr/bin/env python3
"""Exact standalone degree12 dyadic unisolvence checker; no NumPy or producer import."""
import argparse
import base64
import hashlib
import json
import math
from pathlib import Path
import platform
import struct
import sys
import time


def identity(path):
    data = Path(path).read_bytes()
    return {"path": str(Path(path).resolve()), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    began = time.monotonic()
    pins = [identity(__file__), identity(args.payload)]
    data = json.loads(args.payload.read_text())
    assert data["schema"] == "u2-essential-node-payload-v1"
    assert data["n"] == 12 and data["N"] == math.comb(15, 3) == 455
    assert data["shape"] == [455, 3]
    raw = base64.b85decode(data["coordinates_base85"].encode("ascii"))
    assert len(raw) == 455*3*8
    assert hashlib.sha256(raw).hexdigest() == data["coordinates_sha256"]
    # Decode IEEE754 bits directly, independently of float.as_integer_ratio.
    words = struct.unpack("<"+str(455*3)+"Q", raw)
    rational = []
    for word in words:
        exponent = (word >> 52) & 2047
        fraction = word & ((1 << 52)-1)
        assert exponent != 2047, "NaN or infinity"
        mantissa = fraction if exponent == 0 else (1 << 52)+fraction
        power = -1074 if exponent == 0 else exponent-1023-52
        numerator = -mantissa if word >> 63 else mantissa
        if power >= 0:
            numerator, denominator = numerator << power, 1
        else:
            denominator = 1 << (-power)
        divisor = math.gcd(numerator, denominator)
        numerator, denominator = numerator//divisor, denominator//divisor
        assert denominator > 0 and denominator & (denominator-1) == 0
        assert -denominator <= numerator <= denominator
        rational.append((numerator, denominator))
    points = [tuple(rational[i:i+3]) for i in range(0, len(rational), 3)]
    assert len(set(points)) == 455
    prime = 1000037
    assert all(prime % divisor for divisor in range(2, math.isqrt(prime)+1))
    exponents = [(a, b, c) for a in range(13) for b in range(13-a)
                 for c in range(13-a-b)]
    assert len(exponents) == 455
    matrix = []
    for point in points:
        values = [numerator % prime*pow(denominator, prime-2, prime) % prime
                  for numerator, denominator in point]
        powers = [[pow(x, a, prime) for a in range(13)] for x in values]
        matrix.append([powers[0][a]*powers[1][b]*powers[2][c] % prime
                       for a, b, c in exponents])
    determinant = 1
    swaps = 0
    for column in range(455):
        pivot = next((row for row in range(column, 455) if matrix[row][column]), None)
        assert pivot is not None, f"rank deficient at column {column}"
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant = -determinant % prime
            swaps += 1
        pivot_value = matrix[column][column]
        determinant = determinant*pivot_value % prime
        inverse = pow(pivot_value, prime-2, prime)
        row = matrix[column]
        for k in range(column, 455):
            row[k] = row[k]*inverse % prime
        for i in range(column+1, 455):
            multiplier = matrix[i][column]
            if multiplier:
                matrix[i][column:] = [(x-multiplier*y) % prime
                                     for x, y in zip(matrix[i][column:], row[column:])]
    assert determinant != 0
    assert pins == [identity(__file__), identity(args.payload)]
    result = {"status": "EXACT finite checker execution; theorem needs the stated modular reduction",
              "command": sys.argv, "inputs": pins,
              "versions": {"python": platform.python_version(), "stdlib_only": True},
              "arithmetic": "manual IEEE754 integer-bit decoding; unbounded Python integers; prime verified by complete trial division through isqrt(p); Fermat inverses",
              "n": 12, "N": 455, "shape": [455, 3], "coordinate_bytes": len(raw),
              "coordinate_sha256": hashlib.sha256(raw).hexdigest(),
              "all_exact_rational_coordinates_in_closed_cube": True,
              "all_coordinates_dyadic": True, "distinct_exact_nodes": len(set(points)),
              "basis": "total-degree monomials, increasing a then b then c", "prime": prime,
              "rank": 455, "determinant_residue": determinant, "row_swaps": swaps,
              "seconds": time.monotonic()-began,
              "scope": "Only the essential serialized dyadic node set. No cosine-family, norm, optimizer optimality or all-degree theorem follows."}
    payload = json.dumps(result, separators=(",", ":"))+"\n"
    assert len(payload.encode()) < 16384
    args.output.write_text(payload)
    print(json.dumps({"rank": 455, "prime": prime, "determinant_residue": determinant,
                      "payload_sha256": pins[1]["sha256"]}), flush=True)


if __name__ == "__main__":
    main()
