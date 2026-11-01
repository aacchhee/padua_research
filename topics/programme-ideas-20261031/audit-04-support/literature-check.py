"""Pinned, read-only integration checks; no source-reading or mathematical claims.

Run from repository root; stdout is the deterministic audit receipt. Delimiters
are the baseline's literal space-pipe-space boundaries, preserving inner math
pipes. This is intentionally not a general Markdown parser.
"""
import collections
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
SHA = sys.argv[1] if len(sys.argv) > 1 else "37820a528c863e5cfe2dc2f1f8879b4fd40cf210"
MAIN = "21e620b"
TOPIC = "topics/programme-ideas-20261031/"
inputs = {}


def read(path, rev=SHA):
    data = subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT)
    inputs[f"{rev}:{path}"] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    return data.decode()


def cells(line):
    return line.removeprefix("| ").removesuffix(" |").split(" | ")


baseline = read(TOPIC + "lit/baseline.md")
index = read("literature/INDEX.md")
corpus = read("literature/CORPUS.md")
crosswalk = read("ID_CROSSWALK.md")
first = json.loads(read(TOPIC + "lit/integration-map.json"))
second = json.loads(read(TOPIC + "lit/integration-map-pr10.json"))
read(TOPIC + "lit/integration-map.md")
read(TOPIC + "lit/integration-map-pr10.md")
allocation = json.loads(read(TOPIC + "pr-prep/id-map.json"))
base_rows = {cells(l)[0]: cells(l) for l in baseline.splitlines() if l.startswith("| LIT?programme-ideas-claude-")}
index_rows = {re.match(r"\| (LIT-\d+)", l)[1]: (n, cells(l), l)
              for n, l in enumerate(index.splitlines(), 1) if re.match(r"\| LIT-\d+", l)}
aliases = dict(allocation["map"])
for final, (_, _, row) in index_rows.items():
    alias = re.match(r"\| LIT-\d+ \((LIT\?[^)]+)\)", row)
    if alias:
        aliases[alias[1]] = final
programme = {k: v for k, v in allocation["map"].items() if k.startswith("LIT?programme-ideas-")}
lattice = {k: v for k, v in allocation["map"].items() if k.startswith("LIT?lattice-")}
merged = allocation["merged_without_new_id"]
expected_merges = {r["id"]: r["existing_ids"][0] for r in first if r["relation"] == "same"}
expected_merges.update({r["id"]: r["pr10_ids"][0] for r in second if r["relation_vs_pr10"] == "same"})
mismatches = []
for provisional, final in programme.items():
    n, target, _ = index_rows[final]
    original = base_rows[provisional]
    for position, name in [(2, "statement"), (3, "source_key"), (4, "locator")]:
        if target[position].replace("\\|", "|") != original[position].replace("\\|", "|"):
            mismatches.append({"provisional": provisional, "final": final, "line": n,
                               "field": name, "baseline": original[position], "index": target[position]})
    if original[6] not in target[6]:
        # Final allocation can rewrite IDs inside provenance labels.
        normalized = original[6]
        for old, new in aliases.items():
            normalized = normalized.replace(old, new)
        if normalized not in target[6]:
            mismatches.append({"provisional": provisional, "final": final, "line": n,
                               "field": "verification", "baseline": original[6], "index": target[6]})
main_index = read("literature/INDEX.md", MAIN)
main_rows = {re.match(r"\| (LIT-\d+)", l)[1]: l for l in main_index.splitlines() if re.match(r"\| LIT-\d+", l)}
changed_main = [k for k, row in main_rows.items() if index_rows[k][2] != row]
cleanup_line = next(l for l in corpus.splitlines() if l.startswith("After PR #10 merged"))
cleanup_keys = re.findall(r"`([^`]+)`", cleanup_line)[1:]
main_corpus = read("literature/CORPUS.md", MAIN)
cleanup = {}
for key in cleanup_keys:
    rows = [l for l in corpus.splitlines() if l.startswith("| " + key + " |")]
    inherited = [l for l in main_corpus.splitlines() if l.startswith("| " + key + " |")]
    cleanup[key] = {"count": len(rows), "matches_main": rows == inherited}
flags = [r["id"] for r in second if r["conflict"]]
flag_checks = {}
for provisional in flags:
    if provisional in merged:
        flag_checks[provisional] = "merged; conflict retained in map"
    else:
        final = programme[provisional]
        flag_checks[provisional] = "flag in integration-map-pr10" in index_rows[final][2]
for p in ["bos-dmv-xu-2007", "li-sun-xu-2009", "vanbarel-chesnokov-2010", "egk-1991",
          "bartels-jezioranski-1985", "huhtanen-larsen-bit-2002", "huhtanen-larsen-simax-2002",
          "brubeck-nakatsukasa-trefethen-2021", "sauer-2007", "xu-pitman-1994"]:
    read("literature/records/" + p + ".md")
result = {
    "candidate_sha": SHA, "main_sha": subprocess.check_output(["git", "rev-parse", MAIN], cwd=ROOT, text=True).strip(),
    "scope": "Integration inventory, statement/locator/coverage retention; no mathematics or fulltext rerun",
    "python": sys.version.split()[0],
    "baseline_rows": len(base_rows), "programme_rows": len(programme), "lattice_rows": len(lattice),
    "first_relations": dict(collections.Counter(r["relation"] for r in first)),
    "second_relations": dict(collections.Counter(r["relation_vs_pr10"] for r in second)),
    "merges": merged, "merge_map_matches": merged == expected_merges,
    "crosswalk_merges_match": all(f"| {old} | Merged into {new}" in crosswalk for old, new in merged.items()),
    "programme_range_matches": set(programme.values()) == {f"LIT-{n}" for n in range(332, 427)},
    "lattice_range_matches": set(lattice.values()) == {f"LIT-{n}" for n in range(300, 332)},
    "all_provisional_rows_retained": set(programme) | set(merged) == set(base_rows),
    "changed_inherited_index_rows": changed_main,
    "retention_mismatches": mismatches,
    "flag_count": len(flags), "flag_retention": flag_checks,
    "row58_relation": next(r for r in second if r["id"].endswith("-58")),
    "cleanup_keys": cleanup,
    "bogus_corpus_rows": [{"line": n, "text": l} for n, l in enumerate(corpus.splitlines(), 1)
                           if any(l.startswith("| " + key + " |") for key in ["c", "Y", "x±y"])],
    "inputs": inputs,
}
print(json.dumps(result, indent=2, ensure_ascii=False))
assert result["merge_map_matches"] and result["crosswalk_merges_match"]
assert result["programme_range_matches"] and result["lattice_range_matches"]
assert result["all_provisional_rows_retained"] and not changed_main
assert len(flags) == 20 and all(flag_checks.values())
assert len(cleanup) == 34 and all(v == {"count": 1, "matches_main": True} for v in cleanup.values())
# An audit finding is recorded in the receipt rather than suppressed by a
# premature assertion. Exit 1 means integration retention needs repair.
sys.exit(1 if mismatches or result["bogus_corpus_rows"] else 0)
