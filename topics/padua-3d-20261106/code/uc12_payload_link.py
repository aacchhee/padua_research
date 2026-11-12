#!/usr/bin/env python3
"""Link essential exact coordinates to measured NPY bytes using stdlib only."""
import argparse
import ast
import base64
import hashlib
import json
from pathlib import Path
import struct
import sys


def identity(path):
    raw = Path(path).read_bytes()
    return {"path": str(Path(path).resolve()), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--payload", type=Path, required=True)
    p.add_argument("--receipt", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    data = json.loads(a.payload.read_text())
    receipt = json.loads(a.receipt.read_text())
    n = data["n"]
    row = next(dict(zip(receipt["row_columns"], values)) for values in receipt["rows"]
               if dict(zip(receipt["row_columns"], values))["n"] == n
               and dict(zip(receipt["row_columns"], values))["family"] == "joint_norm")
    node_path = Path(receipt["scratch"])/f"n{n}-joint_norm-nodes.npy"
    paths = [Path(__file__), a.payload, a.receipt, node_path]
    pins = [identity(path) for path in paths]
    assert pins[3]["sha256"] == row["node_sha256"] == data["source_nodes"]["sha256"]
    assert pins[2]["sha256"] == data["source_receipt"]["sha256"]
    raw = node_path.read_bytes()
    assert raw[:6] == b"\x93NUMPY"
    version = tuple(raw[6:8])
    assert version in ((1, 0), (2, 0), (3, 0))
    length_bytes = 2 if version == (1, 0) else 4
    length = struct.unpack("<H" if length_bytes == 2 else "<I", raw[8:8+length_bytes])[0]
    offset = 8+length_bytes
    header = ast.literal_eval(raw[offset:offset+length].decode("utf8" if version == (3, 0) else "latin1"))
    assert header == {"descr": "<f8", "fortran_order": False, "shape": (455, 3)}
    coordinate_bytes = raw[offset+length:]
    essential_bytes = base64.b85decode(data["coordinates_base85"])
    assert len(coordinate_bytes) == 455*3*8 and coordinate_bytes == essential_bytes
    assert hashlib.sha256(coordinate_bytes).hexdigest() == data["coordinates_sha256"]
    assert pins == [identity(path) for path in paths]
    result = {"status": "VERIFIED exact byte linkage, separate from norm measurement",
              "command": sys.argv, "inputs": pins, "n": 12, "N": 455,
              "coordinate_bytes": len(coordinate_bytes),
              "coordinate_sha256": hashlib.sha256(coordinate_bytes).hexdigest(),
              "statement": "The essential exact payload and the measured holdout joint_norm NPY contain identical C-order little-endian binary64 coordinate bytes."}
    a.output.write_text(json.dumps(result, separators=(",", ":"))+"\n")


if __name__ == "__main__":
    main()
