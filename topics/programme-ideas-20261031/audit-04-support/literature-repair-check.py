"""Working-tree repair recheck, read-only integration checks; no source-reading or mathematical claims.

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
SHA = sys.argv[1] if len(sys.argv) > 1 else "WORKTREE"
ORIGINAL = "37820a528c863e5cfe2dc2f1f8879b4fd40cf210"
MAIN = "21e620b"
TOPIC = "topics/programme-ideas-20261031/"
inputs = {}


def read(path, rev=SHA):
    data = (ROOT / path).read_bytes() if rev == "WORKTREE" else subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT)
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
# Additional repair acceptance checks; never edit the original audit receipt.
def markdown_cells(line):
    # A literal pipe delimits a cell unless preceded by an odd backslash run.
    pieces, start = [], 0
    for i, char in enumerate(line):
        if char != "|":
            continue
        j = i - 1
        while j >= 0 and line[j] == chr(92):
            j -= 1
        if (i - j - 1) % 2 == 0:
            pieces.append(line[start:i].strip())
            start = i + 1
    pieces.append(line[start:].strip())
    assert pieces[0] == pieces[-1] == ""
    return pieces[1:-1]

malformed = []
coverage_missing = []
for provisional, final in programme.items():
    n, row, raw = index_rows[final]
    rendered = markdown_cells(raw)
    if len(rendered) != 7:
        malformed.append({"final": final, "line": n, "cells": len(rendered)})
    if base_rows[provisional][5] not in row[6]:
        coverage_missing.append(final)
unchanged_paths = [TOPIC + "lit/baseline.md", TOPIC + "lit/integration-map.json",
                   TOPIC + "lit/integration-map-pr10.json", TOPIC + "pr-prep/id-map.json"]
unchanged = {p: read(p) == read(p, ORIGINAL) for p in unchanged_paths}
old_corpus = read("literature/CORPUS.md", ORIGINAL)
old_corpus_rows = {cells(l)[0]: cells(l) for l in old_corpus.splitlines() if l.startswith("| ")}
new_corpus_rows = {cells(l)[0]: cells(l) for l in corpus.splitlines() if l.startswith("| ")}
removed_keys = sorted(old_corpus_rows.keys() - new_corpus_rows.keys())
added_keys = sorted(new_corpus_rows.keys() - old_corpus_rows.keys())
allowed_gap_before = "full citation to be completed at final allocation"
allowed_gap_after = "citation completion pending source verification; final IDs do not clear this gap"
corpus_unexpected = []
corpus_gap_clarifications = 0
for key in old_corpus_rows.keys() & new_corpus_rows.keys():
    old, new = old_corpus_rows[key], new_corpus_rows[key]
    if old != new:
        if old[:-1] == new[:-1] and old[-1] == allowed_gap_before and new[-1] == allowed_gap_after:
            corpus_gap_clarifications += 1
        else:
            corpus_unexpected.append(key)
original_artifacts = {}
for name, wanted in [("literature-check.py", "6e5a19ce8774791ace443242cb104a09eb9ed72ffdbd5684400b8873c425f479"),
                     ("literature-check.json", "a26b8fed0dcf392dcdf0c4556d35acd47855546afadf6954ad44718a950f8ed3")]:
    data = (ROOT / TOPIC / "audit-04-support" / name).read_bytes()
    original_artifacts[name] = hashlib.sha256(data).hexdigest() == wanted
row73 = index_rows["LIT-389"][2]
row58 = index_rows["LIT-375"][2]
repair_checks = {
    "markdown_nonseven_column_rows": malformed,
    "reading_coverage_missing": coverage_missing,
    "unchanged_baseline_maps_allocation": unchanged,
    "removed_corpus_keys": removed_keys,
    "added_corpus_keys": added_keys,
    "unexpected_corpus_row_edits": corpus_unexpected,
    "corpus_gap_clarifications": corpus_gap_clarifications,
    "original_audit_artifacts_unchanged": original_artifacts,
    "row73_attribution_flag_retained": "attribution flag retained: arXiv paper/book conflation" in row73,
    "row58_unchanged": row58 in read("literature/INDEX.md", ORIGINAL).splitlines(),
}

result = {
    "repair_checks": repair_checks,
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
assert not malformed and not coverage_missing and all(unchanged.values())
assert removed_keys == ["Y", "c", "x±y"] and not added_keys and not corpus_unexpected
assert all(original_artifacts.values()) and repair_checks["row73_attribution_flag_retained"] and repair_checks["row58_unchanged"]
# An audit finding is recorded in the receipt rather than suppressed by a
# premature assertion. Exit 1 means integration retention needs repair.
sys.exit(1 if mismatches or result["bogus_corpus_rows"] else 0)
