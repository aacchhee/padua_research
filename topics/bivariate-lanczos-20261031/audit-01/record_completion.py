"""Validate the frozen science and inventory the small final audit artifacts."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
TARGET = HERE / "artifact-manifest.json"
CANDIDATE = "5ccfac223f466a9105450365d8c6c3781ff7d922"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    subprocess.run(["python3", str(HERE / "check_inventory.py")],
                   stdout=subprocess.DEVNULL, check=True)
    required = ["L1-foundations", "L1-later", "L2", "L3-framework", "L3-certificates", "L5", "protocol"]
    reports = [HERE / (name + ".md") for name in required]
    assert all(p.exists() for p in reports)
    reports.append(TOPIC / "audit-01.md")
    missing = []
    for p in reports:
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", p.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            path = target.split("#")[0]
            if path and not (p.parent / path).resolve().exists():
                missing.append({"source": str(p.relative_to(ROOT)), "target": target})
    assert not missing, missing
    artifacts = []
    for p in sorted(HERE.rglob("*")) + [TOPIC / "audit-01.md"]:
        if not p.is_file() or p == TARGET or "__pycache__" in p.parts:
            continue
        assert p.suffix in {".py", ".md", ".json", ".jsonl", ".log", ".txt"}, p
        artifacts.append({"path": str(p.relative_to(ROOT)),
                          "bytes": p.stat().st_size, "sha256": sha(p)})
    assert all(x["bytes"] <= 1000000 for x in artifacts)
    inventory = json.loads((HERE / "inventory.json").read_text())
    total = sum(x["bytes"] for x in artifacts)
    # Conservatively count every audit source/report as output for this budget.
    assert total + inventory["generated_output_bytes"] < 5000000
    result = {"candidate": CANDIDATE,
              "rules_read_at": "3a9063b84d14ca0a5998378371e27643fde50a29",
              "main_at_audit": "07c5f5465d6de306aa81dbe8ca1f615295163864",
              "theory_files_unchanged": inventory["actual_theory_files"],
              "scope_reports": required, "local_report_links_valid": True,
              "artifact_count": len(artifacts), "audit_bytes": total,
              "candidate_output_plus_inventoried_audit_bytes": total + inventory["generated_output_bytes"],
              "manifest_excludes_itself": True,
              "regeneration_command": "python3 topics/bivariate-lanczos-20261031/audit-01/record_completion.py",
              "retention": "Small necessary committed audit evidence; no external archive created.",
              "artifacts": artifacts}
    TARGET.write_text(json.dumps(result, indent=2) + "\n")
    assert total + inventory["generated_output_bytes"] + TARGET.stat().st_size < 5000000
    print(json.dumps({k: v for k, v in result.items() if k != "artifacts"}, indent=2))


if __name__ == "__main__":
    main()
