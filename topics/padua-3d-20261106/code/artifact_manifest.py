#!/usr/bin/env python3
"""Create or verify the topic's code/data identities; never pin prose."""
import argparse
import base64
import hashlib
import json
import zlib
from pathlib import Path

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def identity(path, base=TOP):
    raw = path.read_bytes()
    return {"path": path.relative_to(base).as_posix(), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def artifacts():
    # Recursive, suffix-independent coverage, excluding Python bytecode caches.
    return sorted(path for directory in ("code", "evidence")
                  for path in TOP.joinpath(directory).rglob("*")
                  if path.is_file() and "__pycache__" not in path.parts
                  and path.suffix != ".pyc")


def packed(rows):
    """Lossless compact identities: SHA-256 bytes in RFC1924 base85."""
    result = {"code": {}, "evidence": {}, "other": {}}
    for row in rows:
        path = Path(row["path"])
        expected = ".py" if path.parts[0] == "code" else ".json"
        if path.suffix == expected:
            group = path.parts[0]
            key = path.relative_to(group).with_suffix("").as_posix()
        else:
            group, key = "other", path.as_posix()
        result[group][key] = [row["bytes"], base64.b85encode(
            bytes.fromhex(row["sha256"])).decode("ascii")]
    return result



SCHEMA = "padua-3d-code-data-manifest-v6"
MAGIC = b"P3M6\x00"


def varint(value):
    """Canonical unsigned base-128 integer."""
    if type(value) is not int or value < 0:
        raise ValueError("invalid unsigned integer")
    out = bytearray()
    while value >= 128:
        out.append((value & 127) | 128)
        value >>= 7
    out.append(value)
    return bytes(out)


def encode_rows(rows):
    """P3M6 NUL, count; sorted path prefix/suffix lengths, suffix, size;
    then concatenated raw32 digests in matching order. Integers are varints.
    Paths are UTF-8; compression is zlib9 followed by RFC1924 base85.
    """
    out = bytearray(MAGIC + varint(len(rows)))
    digests = bytearray()
    previous = b""
    for row in sorted(rows, key=lambda row: row["path"].encode("utf-8")):
        path = row["path"].encode("utf-8")
        validate_path(path.decode("utf-8"))
        if path <= previous:
            raise ValueError("duplicate or unordered path")
        prefix = 0
        while prefix < min(len(path), len(previous)) and path[prefix] == previous[prefix]:
            prefix += 1
        suffix = path[prefix:]
        digest = bytes.fromhex(row["sha256"])
        if len(digest) != 32:
            raise ValueError("invalid SHA-256 length")
        out.extend(varint(prefix) + varint(len(suffix)) + suffix
                   + varint(row["bytes"]))
        digests.extend(digest)
        previous = path
    return bytes(out + digests)


def validate_path(path):
    parts = path.split("/")
    if (parts[0] not in ("code", "evidence") or len(parts) < 2
            or any(part in ("", ".", "..", "__pycache__") for part in parts)
            or "\\" in path or "\x00" in path or path.endswith(".pyc")):
        raise ValueError("invalid artifact path")


def decode_rows(raw):
    if not raw.startswith(MAGIC):
        raise ValueError("invalid v6 magic/version")
    offset = len(MAGIC)

    def integer():
        nonlocal offset
        start, value, shift = offset, 0, 0
        while True:
            if offset >= len(raw) or shift > 63:
                raise ValueError("truncated or oversized varint")
            byte = raw[offset]
            offset += 1
            value |= (byte & 127) << shift
            if not byte & 128:
                if raw[start:offset] != varint(value):
                    raise ValueError("noncanonical varint")
                return value
            shift += 7

    count = integer()
    if count > len(raw) // 35:
        raise ValueError("impossible entry count")
    rows, previous = [], b""
    for _ in range(count):
        prefix, length = integer(), integer()
        if prefix > len(previous) or not length or offset + length > len(raw):
            raise ValueError("invalid path prefix or truncated path")
        path = previous[:prefix] + raw[offset:offset + length]
        offset += length
        if path <= previous:
            raise ValueError("duplicate or unordered path")
        name = path.decode("utf-8")
        validate_path(name)
        size = integer()
        rows.append({"path": name, "bytes": size})
        previous = path
    if len(raw) - offset != 32 * count:
        raise ValueError("truncated or trailing SHA-256 data")
    for row in rows:
        row["sha256"] = raw[offset:offset + 32].hex()
        offset += 32
    return rows


def decode_manifest(saved):
    schema = saved.get("schema")
    if schema == "padua-3d-code-data-manifest-v4":
        return saved["artifacts"]
    if schema not in ("padua-3d-code-data-manifest-v5", SCHEMA):
        raise ValueError("unsupported manifest schema")
    compressed = base64.b85decode(saved["artifacts_payload"])
    inflater = zlib.decompressobj()
    raw = inflater.decompress(compressed) + inflater.flush()
    if not inflater.eof or inflater.unused_data or inflater.unconsumed_tail:
        raise ValueError("truncated or trailing compressed payload")
    return (packed(decode_rows(raw)) if schema == SCHEMA else json.loads(raw))


def verify_manifest(saved, observed, inherited):
    if decode_manifest(saved) != packed(observed) or saved.get("inherited_inputs") != inherited:
        raise ValueError("code/data set or identities changed")


def render_manifest(output):
    raw = json.dumps(output, indent=2) + "\n"
    if len(raw.encode()) >= 16384:
        raw = json.dumps(output, separators=(",", ":"), ensure_ascii=False) + "\n"
    if len(raw.encode()) >= 16384:
        raise ValueError("compact manifest limit exceeded")
    return raw


def make_manifest(observed, inherited):
    return {
        "schema": SCHEMA,
        "rules_input_sha": "38227202bc6908d5a5a874950145761a8ca4312f",
        "historical_rules_input_sha": "ccd9e905d19c0c625c196c4a3f3e707058ed042a",
        "generate": "python topics/padua-3d-20261106/code/artifact_manifest.py",
        "verify": "python topics/padua-3d-20261106/code/artifact_manifest.py --verify",
        "format": "--list: v4 map; scope: recursive code/evidence excluding __pycache__ and .pyc.",
        "artifacts_codec": "P3M6-prefix-varint-sha256-columns+zlib9+RFC1924-base85; see code",
        "artifacts_payload": base64.b85encode(zlib.compress(
            encode_rows(observed), 9)).decode(),
        "inherited_inputs": inherited,
        "limits": [
            "Identities only; no mathematical verification.",
            "Prose: audit commit only.",
            "Scope/inputs: receipts and attempts.",
            "Large catalogues: regeneration only; COLD_STORAGE.md.",
            "No archival delivery or independent Claude audit implied."
        ]
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--list", action="store_true", help="Print the losslessly decoded identity map")
    args = parser.parse_args()
    target = TOP / "evidence-manifest.json"
    observed = [identity(path) for path in artifacts()]
    inherited = [identity(ROOT / "tracks/lattice-unisolvence/code" / name, ROOT)
                 for name in ("c3_lebesgue.py", "c3_rank.py")]
    if args.verify or args.list:
        saved = json.loads(target.read_text())
        decoded = decode_manifest(saved)
        if args.list:
            print(json.dumps(decoded, indent=2))
            return
        if decoded != packed(observed) or saved.get("inherited_inputs") != inherited:
            raise SystemExit("FAIL: code/data set or identities changed")
        print(json.dumps({"verdict": "PASS", "artifacts": len(observed),
                          "bytes": sum(row["bytes"] for row in observed)}))
        return
    output = make_manifest(observed, inherited)
    raw = render_manifest(output)
    target.write_text(raw)
    print(json.dumps({"manifest": str(target), "artifacts": len(observed),
                      "bytes": len(raw.encode())}))


if __name__ == "__main__":
    main()
