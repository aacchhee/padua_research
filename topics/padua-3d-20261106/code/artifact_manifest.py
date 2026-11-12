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



SCHEMA = "padua-3d-code-data-manifest-v7"
MAGIC = b"P3M7\x00"
V6_MAGIC = b"P3M6\x00"
MAX_RAW = 16 * 1024 * 1024


def varint(value):
    """Canonical unsigned base-128 integer."""
    if type(value) is not int or not 0 <= value < (1 << 63):
        raise ValueError("invalid unsigned integer")
    out = bytearray()
    while value >= 128:
        out.append((value & 127) | 128)
        value >>= 7
    out.append(value)
    return bytes(out)


def encode_v6_rows(rows):
    """P3M6 NUL, count; sorted path prefix/suffix lengths, suffix, size;
    then concatenated raw32 digests in matching order. Integers are varints.
    Paths are UTF-8; compression is zlib9 followed by RFC1924 base85.
    """
    out = bytearray(V6_MAGIC + varint(len(rows)))
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


def decode_v6_rows(raw):
    if not raw.startswith(V6_MAGIC):
        raise ValueError("invalid v6 magic/version")
    offset = len(V6_MAGIC)

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


def inflate(compressed):
    """Accept exactly one bounded zlib stream, with no trailing bytes."""
    inflater = zlib.decompressobj()
    raw = inflater.decompress(compressed, MAX_RAW + 1)
    if len(raw) > MAX_RAW or not inflater.eof or inflater.unused_data or inflater.unconsumed_tail:
        raise ValueError("oversized, truncated or trailing compressed payload")
    return raw


def read_integer(raw, offset):
    start, value, shift = offset, 0, 0
    while offset < len(raw) and shift <= 63:
        byte = raw[offset]
        offset += 1
        value |= (byte & 127) << shift
        if not byte & 128:
            if value > (1 << 63) - 1 or raw[start:offset] != varint(value):
                raise ValueError("oversized or noncanonical varint")
            return value, offset
        shift += 7
    raise ValueError("truncated or oversized varint")


def encode_rows(rows):
    """One P3M7 frame: count, path/size compressed lengths, zlib paths,
    zlib sizes, then count raw32 digests. All lengths/counts are varints.
    """
    ordered = sorted(rows, key=lambda row: row["path"].encode("utf-8"))
    paths, sizes, digests, previous = bytearray(), bytearray(), bytearray(), b""
    for row in ordered:
        name = row["path"].encode("utf-8")
        validate_path(row["path"])
        if name <= previous:
            raise ValueError("duplicate or unordered path")
        digest = bytes.fromhex(row["sha256"])
        if len(digest) != 32:
            raise ValueError("invalid SHA-256 length")
        paths.extend(name + b"\x00")
        sizes.extend(varint(row["bytes"]))
        digests.extend(digest)
        previous = name
    paths, sizes = zlib.compress(paths, 9), zlib.compress(sizes, 9)
    return (MAGIC + varint(len(rows)) + varint(len(paths)) + varint(len(sizes))
            + paths + sizes + digests)


def decode_rows(raw):
    if not raw.startswith(MAGIC):
        raise ValueError("invalid v7 magic/version")
    count, offset = read_integer(raw, len(MAGIC))
    path_length, offset = read_integer(raw, offset)
    size_length, offset = read_integer(raw, offset)
    if count > MAX_RAW // 35 or not path_length or not size_length:
        raise ValueError("invalid count or metadata length")
    end_paths, end_sizes = offset + path_length, offset + path_length + size_length
    if end_sizes > len(raw) or len(raw) - end_sizes != 32 * count:
        raise ValueError("truncated or trailing frame data")
    paths = inflate(raw[offset:end_paths])
    sizes = inflate(raw[end_paths:end_sizes])
    names = paths.split(b"\x00")
    if names[-1] != b"" or len(names) != count + 1:
        raise ValueError("invalid path count or terminator")
    rows, previous, size_offset = [], b"", 0
    for i, path in enumerate(names[:-1]):
        if path <= previous:
            raise ValueError("duplicate or unordered path")
        name = path.decode("utf-8")
        validate_path(name)
        size, size_offset = read_integer(sizes, size_offset)
        rows.append({"path": name, "bytes": size,
                     "sha256": raw[end_sizes + 32*i:end_sizes + 32*(i+1)].hex()})
        previous = path
    if size_offset != len(sizes):
        raise ValueError("trailing size data")
    return rows


def decode_manifest(saved):
    schema = saved.get("schema")
    if schema == "padua-3d-code-data-manifest-v4":
        return saved["artifacts"]
    if schema not in ("padua-3d-code-data-manifest-v5",
                       "padua-3d-code-data-manifest-v6", SCHEMA):
        raise ValueError("unsupported manifest schema")
    payload = saved["artifacts_payload"]
    raw = base64.b85decode(payload)
    if base64.b85encode(raw).decode() != payload:
        raise ValueError("noncanonical base85")
    if schema == SCHEMA:
        return packed(decode_rows(raw))
    raw = inflate(raw)
    return (packed(decode_v6_rows(raw)) if schema.endswith("-v6") else json.loads(raw))


def verify_manifest(saved, observed, inherited):
    if decode_manifest(saved) != packed(observed) or saved.get("inherited_inputs") != inherited:
        raise ValueError("code/data set or identities changed")


def render_manifest(output):
    # Topic-specific allowance approved by AC, 2026-11-08; handoff 19.
    raw = json.dumps(output, indent=2) + "\n"
    if len(raw.encode()) >= 32768:
        raw = json.dumps(output, separators=(",", ":"), ensure_ascii=False) + "\n"
    if len(raw.encode()) >= 32768:
        raise ValueError("compact manifest limit exceeded")
    return raw


def make_manifest(observed, inherited):
    return {
        "schema": SCHEMA,
        "rules_input_sha": "38227202bc6908d5a5a874950145761a8ca4312f",
        "historical_rules_input_sha": "ccd9e905d19c0c625c196c4a3f3e707058ed042a",
        "generate": "python topics/padua-3d-20261106/code/artifact_manifest.py",
        "verify": "python topics/padua-3d-20261106/code/artifact_manifest.py --verify",
        "format": "--list: v4 map.",
        "artifacts_codec": "P3M7+zlib9(paths,sizes)+raw32+base85",
        "artifacts_payload": base64.b85encode(encode_rows(observed)).decode(),
        "inherited_inputs": inherited,
        "limits": "Identities only; no proof, archival delivery or independent audit. See pruning-manifest.md."
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
