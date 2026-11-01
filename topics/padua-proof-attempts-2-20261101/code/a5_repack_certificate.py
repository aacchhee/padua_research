#!/usr/bin/env python3
"""Losslessly pack one count JSON as XZ; rebind only its global raw-file hash.

This is mechanical packaging, not certificate verification. The independent
checker must verify the resulting matching count/global pair in full. Existing
files are reused only when their bytes are identical; no force option exists.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import lzma
import os
from pathlib import Path
import platform
import sys


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def identity(path: Path, data: bytes) -> dict:
    return {"path": str(path.resolve()), "bytes": len(data), "sha256": sha256(data)}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def decode(raw: bytes) -> bytes:
    if raw.startswith(b"\x1f\x8b"):
        return gzip.decompress(raw)
    if raw.startswith(b"\xfd7zXZ\x00"):
        return lzma.decompress(raw)
    return raw


def compatible_destination(path: Path, data: bytes) -> None:
    if path.exists() and path.read_bytes() != data:
        raise ValueError(f"destination already has different bytes; choose a new path: {path}")


def atomic_write_new_or_identical(path: Path, data: bytes) -> None:
    if path.exists():
        compatible_destination(path, data)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".tmp-{os.getpid()}")
    try:
        with temporary.open("xb") as stream:
            stream.write(data)
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--global-file", type=Path)
    parser.add_argument("--global-output", type=Path)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    if bool(args.global_file) != bool(args.global_output):
        parser.error("--global-file and --global-output must be supplied together")
    paths = [args.certificate, args.output, args.receipt]
    if args.global_file:
        paths += [args.global_file, args.global_output]
    if len({path.resolve() for path in paths}) != len(paths):
        parser.error("input, output and receipt paths must all be distinct")

    source_path = Path(__file__).resolve()
    source_before = source_path.read_bytes()
    raw = args.certificate.read_bytes()
    decoded = decode(raw)
    document = json.loads(decoded, object_pairs_hook=unique_object)
    if not isinstance(document, dict):
        raise ValueError("count certificate must be a JSON object")
    packed = lzma.compress(decoded, format=lzma.FORMAT_XZ,
                           check=lzma.CHECK_SHA256,
                           preset=9 | lzma.PRESET_EXTREME)
    if lzma.decompress(packed) != decoded:
        raise ValueError("lossless roundtrip failed")
    if len(packed) > 1_000_000:
        raise ValueError(f"single XZ archive is {len(packed)} bytes, over the 1 MB limit")

    receipt = {
        "format": "a5-mechanical-xz-repack-v1",
        "scope": "lossless packaging only; no count or global verification",
        "python": platform.python_version(),
        "python_executable": sys.executable,
        "program_argv": sys.argv,
        "dont_write_bytecode": bool(sys.dont_write_bytecode),
        "compression": {"container": "XZ", "filter": "LZMA2",
                        "preset": 9, "extreme": True, "check": "SHA256"},
        "source": identity(source_path, source_before),
        "input": identity(args.certificate, raw),
        "output": identity(args.output, packed),
        "decoded_bytes": len(decoded),
        "decoded_sha256": sha256(decoded),
        "decoded_bytes_identical": True,
        "input_claimed_complete": document.get("summary", {}).get("complete") is True,
        "source_unchanged": True,
    }
    writes = [(args.output, packed)]
    global_raw = None
    if args.global_file:
        global_raw = args.global_file.read_bytes()
        old_global = json.loads(global_raw, object_pairs_hook=unique_object)
        if not isinstance(old_global, dict) or old_global.get("certificate_sha256") != sha256(raw):
            raise ValueError("input global object is not bound to the input raw certificate")
        new_global = dict(old_global)
        new_global["certificate_sha256"] = sha256(packed)
        if {k: v for k, v in old_global.items() if k != "certificate_sha256"} != \
                {k: v for k, v in new_global.items() if k != "certificate_sha256"}:
            raise ValueError("a nonbinding global field changed")
        global_packed = (json.dumps(new_global, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":"), allow_nan=False) + "\n").encode()
        receipt.update({"global_input": identity(args.global_file, global_raw),
                        "global_output": identity(args.global_output, global_packed),
                        "global_only_binding_field_changed": True})
        writes.append((args.global_output, global_packed))

    if args.certificate.read_bytes() != raw or source_path.read_bytes() != source_before:
        raise ValueError("input certificate or repacker source changed during packaging")
    if global_raw is not None and args.global_file.read_bytes() != global_raw:
        raise ValueError("input global object changed during packaging")
    receipt_bytes = (json.dumps(receipt, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()
    writes.append((args.receipt, receipt_bytes))
    for path, data in writes:
        compatible_destination(path, data)
    for path, data in writes:
        atomic_write_new_or_identical(path, data)
    print(json.dumps({"output_bytes": len(packed), "output_sha256": sha256(packed),
                      "decoded_bytes_identical": True,
                      "global_only_binding_field_changed": global_raw is not None,
                      "receipt": str(args.receipt.resolve())}, sort_keys=True))


if __name__ == "__main__":
    main()
