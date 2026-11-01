"""Read-only identity/provenance checks for the frozen Lanczos audit candidate."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
TOPIC = ROOT / "topics/bivariate-lanczos-20261031"
CANDIDATE = "5ccfac223f466a9105450365d8c6c3781ff7d922"


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    result = {"candidate": CANDIDATE, "python": sys.version,
              "main_at_session_start": "07c5f5465d6de306aa81dbe8ca1f615295163864"}
    handoff = git("show", CANDIDATE + ":topics/bivariate-lanczos-20261031/audit-handoff.md").decode()
    entries = re.findall(r"\| ([0-9a-f]{64}) \| `(tracks/[^`]+)` \|", handoff)
    result["theory_manifest_entries"] = len(entries)
    checks = []
    for expected, name in entries:
        frozen = git("show", CANDIDATE + ":" + name)
        checks.append({"path": name, "sha256": digest(frozen),
                       "manifest_matches": digest(frozen) == expected,
                       "working_science_unchanged": (ROOT / name).read_bytes() == frozen})
    result["theory"] = checks
    declared = {p for _, p in entries}
    actual = set(git("ls-tree", "-r", "--name-only", CANDIDATE,
                     "tracks/bivariate-lanczos/theory").decode().splitlines())
    result["unmanifested_theory"] = sorted(actual - declared)
    inputs = (ROOT / "tracks/bivariate-lanczos/code/inputs/MANIFEST.md").read_text()
    rows = re.findall(r"\| ([\w.]+\.py) \| ([0-9a-f]{40}) \| ([0-9a-f]{64}) \| (\d+) \|", inputs)
    result["input_copies"] = []
    for name, blob, sha, size in rows:
        p = ROOT / "tracks/bivariate-lanczos/code/inputs" / name
        b = p.read_bytes()
        result["input_copies"].append({"path": str(p.relative_to(ROOT)),
            "identity_matches": digest(b) == sha and len(b) == int(size)
                and git("hash-object", str(p)).decode().strip() == blob})
    repro = (TOPIC / "repro/REPRO.md").read_text()
    result["repro_logs"] = []
    for sha, name in re.findall(r"^([0-9a-f]{64})  (\S+)$", repro, re.M):
        p = TOPIC / "repro/logs" / name
        result["repro_logs"].append({"path": str(p.relative_to(ROOT)),
                                   "identity_matches": p.exists() and digest(p.read_bytes()) == sha})
    files = git("ls-tree", "-r", "--long", CANDIDATE,
                "topics/bivariate-lanczos-20261031").decode().splitlines()
    generated = []
    for row in files:
        meta, name = row.split("\t", 1)
        if "/logs/" in name or "/logs_" in name or "/repro/analysis/" in name and name.endswith(".txt"):
            generated.append({"path": name, "bytes": int(meta.split()[3])})
    result["generated_output_inventory"] = generated
    result["generated_output_bytes"] = sum(x["bytes"] for x in generated)
    result["generated_output_files"] = len(generated)
    result["oversized_generated_files"] = [x for x in generated if x["bytes"] > 1000000]
    result["generated_inventory_limit"] = result["generated_output_bytes"] < 5000000 and not result["oversized_generated_files"]
    result["archive_retrieved_this_audit"] = False
    result["archive_limit"] = "AC's Windows cold storage is not attached; no archive re-verification claimed."
    result["actual_theory_files"] = len(actual)
    result["handoff_prose_theory_count"] = 64
    result["theory_count_prose_matches"] = len(actual) == result["handoff_prose_theory_count"]
    result["pass"] = (len(entries) == len(actual) and not result["unmanifested_theory"]
        and all(x["manifest_matches"] and x["working_science_unchanged"] for x in checks)
        and len(rows) == 12 and all(x["identity_matches"] for x in result["input_copies"])
        and all(x["identity_matches"] for x in result["repro_logs"])
        and bool(result["repro_logs"]) and result["generated_inventory_limit"])
    print(json.dumps(result, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
