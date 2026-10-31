"""Independent allocation/registry and manuscript transcription checks.

Run from the repository root. This does not prove the analytic theorems, rerun
spectral calculations, compile TeX, or certify historical novelty.
"""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
EV = ROOT / "tracks/mz-constants/evidence"


def read(path):
    return (ROOT / path).read_text()


def identity(path):
    b = (ROOT / path).read_bytes()
    return {"path": path, "sha256": hashlib.sha256(b).hexdigest(), "bytes": len(b)}


def dump(name, value):
    (EV / name).write_text(json.dumps(value, indent=2) + "\n")


mapping = json.loads(read("topics/mz-constants/final-id-map.json"))
pairs = mapping["mappings"]
crosswalk = read("ID_CROSSWALK.md")
proofs = read("PROOF_STATUS.md")
literature = read("literature/INDEX.md")
ideas = read("state/IDEAS.md")
failures = []
claims = []
for old, final in pairs.items():
    rows = [line for line in crosswalk.splitlines()
            if line.startswith("| " + old + " | " + final + " |")]
    if len(rows) != 1:
        failures.append("crosswalk row: " + final)
        continue
    target = re.search(r"\]\(([^)]+)\)", rows[0]).group(1)
    if not (ROOT / target).is_file():
        failures.append("canonical path: " + final)
        continue
    canonical = read(target)
    if final not in canonical:
        failures.append("canonical identifier: " + final)
    if final.startswith("PD-"):
        status = "OPEN" if final in {"PD-T020", "PD-T027", "PD-T028"} else (
            "MEASURED" if final == "PD-T026" else "PROVED")
        r = [s for s in proofs.splitlines() if s.startswith("| " + final + " |")]
        if len(r) != 1 or "| " + status + " |" not in r[0]:
            failures.append("result status: " + final)
        if not canonical.splitlines()[0].startswith("# " + final):
            failures.append("theory heading: " + final)
        claims.append({"id": final, "path": target, "status": status})
    elif final.startswith("LIT-"):
        if len([s for s in literature.splitlines() if s.startswith("| " + final + " |")]) != 1:
            failures.append("literature row: " + final)
    elif not re.search(r"^#{2,3} " + re.escape(final) + r"(?:\s|$)", ideas, re.M):
        failures.append("idea heading: " + final)

registry_paths = ["ID_CROSSWALK.md", "PROOF_STATUS.md", "literature/INDEX.md",
                  "state/IDEAS.md", "topics/padua-batch-20261031/ALLOCATIONS.md"]
registry = {
    "method": "verify every mapping/crosswalk row, canonical heading/path, result status, literature row and IDEA heading",
    "command": "python tracks/mz-constants/evidence/astra-final-check.py",
    "scientific_checkpoint": mapping["scientific_checkpoint"],
    "mapping_count": len(pairs), "results": claims,
    "failures": failures, "outcome": "FAIL" if failures else "PASS",
    "registry_sha256": {p: identity(p)["sha256"] for p in registry_paths},
}
dump("astra-registry-check.json", registry)

tex_path = "tracks/mz-constants/paper/manuscript.tex"
bib_path = "tracks/mz-constants/paper/refs.bib"
tex, bib = read(tex_path), read(bib_path)
data_path = "tracks/mz-constants/evidence/astra-reproduction.json"
replay = json.loads(read(data_path))["results"]
tables = re.findall(r"\\begin\{tabular\}.*?\\end\{tabular\}", tex, re.S)
rows = []
for table in tables:
    rows.append([[float(s.strip()) for s in line.split(r"\\")[0].split("&")]
                 for line in table.splitlines() if re.match(r"^\d+\s*&", line)])
assert len(rows) == 2 and [len(x) for x in rows] == [6, 4], rows
differences = []
table_checks = []
for row in rows[0]:
    n = int(row[0])
    reference = next(r for r in replay["cc_Nminus1"] if r["N"] == n)
    delta = [abs(a - reference[k]) for a, k in zip(row[1:], ["lmin", "lmax", "eta"])]
    differences.extend(delta)
    table_checks.append({"rule": "CC", "N": n, "max_rounding_error": max(delta)})
for row in rows[1]:
    n = int(row[0])
    reference = next(r for r in replay["padua"] if r["m"] == n)
    expected = [float(n)] + reference["out"][0][0] + [float(reference["out"][1])]
    assert row[:2] == expected[:2] and row[-1] == expected[-1], (row, expected)
    delta = [abs(a - b) for a, b in zip(row[2:5], expected[2:5])]
    differences.extend(delta)
    table_checks.append({"rule": "Padua", "N": n, "max_rounding_error": max(delta),
                         "degree_and_negative_weight_count_match": True})
assert max(differences) < 5.1e-10
cites = {key.strip() for block in re.findall(r"\\cite[pt]?(?:\[[^]]*\])?\{([^}]+)\}", tex)
         for key in block.split(",")}
bibkeys = set(re.findall(r"@\w+\{([^,]+),", bib))
assert cites == bibkeys and len(cites) == 12, (cites, bibkeys)
ids = set(re.findall(r"(?:PD-[TN]\d{3}|LIT-\d{3})", tex + bib))
assert ids <= set(pairs.values())
assert "?mz-constants" not in tex + bib
inputs = [tex_path, bib_path, "tracks/mz-constants/paper/README.md",
          "topics/mz-constants/directions/M7/manuscript-record.md", data_path,
          "topics/mz-constants/final-id-map.json"]
manuscript = {
    "auditor": "gpt-6-astra xhigh", "date": "2026-10-31",
    "command": "python tracks/mz-constants/evidence/astra-final-check.py",
    "inputs": [identity(p) for p in inputs],
    "scope": "Full TeX and bibliography read; analytic translation and source limits reviewed separately in independent-astra-01.md. This check uses the auditor's actual earlier spectral replay, not the developer table check.",
    "table_rows": table_checks, "float_entries_compared": len(differences),
    "maximum_rounding_error": max(differences), "citations": sorted(cites),
    "all_citation_keys_match_bibliography": True,
    "all_final_ids_allocated": True, "provisional_ids_present": False,
    "outcome": "PASS", "own_TeX_compilation": False, "own_PDF_visual_review": False,
    "limits": "No new spectral execution in this check; no novelty clearance, Claude completion, submission or publication approval.",
}
dump("astra-manuscript-check.json", manuscript)
assert not failures, failures
print(json.dumps({"registry": registry["outcome"], "mappings": len(pairs),
                  "manuscript": "PASS", "table_rows": len(table_checks),
                  "float_entries": len(differences), "max_error": max(differences)}))
