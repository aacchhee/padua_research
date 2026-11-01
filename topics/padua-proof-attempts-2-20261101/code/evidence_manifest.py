#!/usr/bin/env python3
"""Mechanical provenance only; reads inputs from immutable Git objects.

Run from any directory. Re-run after final output edits. No scientific code is run.
"""
import hashlib
import json
from pathlib import Path
import platform
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = "topics/padua-proof-attempts-2-20261101"
PINS = {
    "main_b3_b1_context": "28aaa20861d08074b77efc74eaef75cdcb36234d",
    "main_results_tracking_rule": "28aaa20861d08074b77efc74eaef75cdcb36234d",
    "main_mz_registry_update": "e0d9e3d08ee26c3b82a295f33b6ff99d928f22b9",
    "part1_and_rules": "a09d910ae7d5526b1e216066421a0bee7fc20da4",
    "part1_audit_arrived": "95279b833bca5967fcf47c1b71a56ff622185b4e",
    "main_part1_merged": "806cc7b4509fd93bae652f9545d32d95529f8281",
    "part1_final_branch": "752ba068589683afe644b505d673f8da1529cbf0",
    "part1_main_sync_arrived": "93da3be26dbddf9ec2446af578fe8015bb4eeada",
    "part1_response_arrived": "7b8884a2f98518784ff3698dd2f3f9c49c9cdd62",
    "literature_index_update": "cf89b140530d5838bdb208a8c28f3e7aa676ace3",
    "current_main_and_rules": "e24b21fe43cdd090f6dfac269147e75185f04c5b",
    "programme_final": "b46b4dea18ce2c933489a211b0b6819dfd32ca70",
    "main_observed": "9739a0c56b7a3976422ce60a8441bfbbfd6554df",
    "programme": "9bd14a6d2c4da69139a10107d8a787f2be0c5c9e",
    "part1_programme": "cadb35066160e466cb1704b9791ad6f374446422",
    "lanczos": "a2dd845b8a231e1b00733e1361e2a9ad3bad222f",
}
PG = "topics/programme-ideas-20261031/"
P1 = "topics/padua-proof-attempts-20261101/"
RULES = ["AGENTS.md", "agents/WORKFLOW.md", "agents/codex/CODEX.md"]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def tree(pin):
    return git("ls-tree", "-r", "--name-only", pin).decode().splitlines()


def identity(data):
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def main():
    requested = {}

    def add(label, paths):
        for path in paths:
            requested[(PINS[label], path)] = label

    add("main_b3_b1_context", [PG + x for x in ["OPEN_TARGETS.md",
        "theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md",
        "theory/programme-ideas-claude-N01-symmetrised-product-inertia-count.md",
        "theory/programme-ideas-claude-N02-windowed-rational-lanczos-instability.md",
        "checks/decisive-gen1-3.md", "checks/adversarial-gen1-3.md",
        "checks/code/decisive/gen1-3/orf2d.py", "checks/code/decisive/gen1-3/window_exact.py"]] + [
        "tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-301-truncated-favard-sections.md",
        "tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-N304-compression-model-insufficient.md",
        "tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-316-square-case-first-order-commutator-isomorphism.md",
        "topics/bivariate-lanczos-20261031/directions/L3/candidates.md"])
    add("main_results_tracking_rule", RULES + ["results/README.md", "RESULTS.md"])
    add("main_mz_registry_update", RULES + ["state/IDEAS.md", "literature/INDEX.md",
        "PROOF_STATUS.md", "ID_CROSSWALK.md", "PAPER_MAP.md", "state/CURRENT.md"] +
        [p for p in tree(PINS["main_mz_registry_update"]) if
         p.startswith("tracks/mz-constants/theory/") and p.endswith(".md")])
    add("part1_and_rules", RULES + [p for p in tree(PINS["part1_and_rules"]) if p.startswith(P1)])
    add("part1_audit_arrived", [p for p in tree(PINS["part1_audit_arrived"])
        if p == P1 + "audit-01.md" or p.startswith(P1 + "audit-support/claude-audit-01/")])
    response_paths = git("diff", "--name-only", "--diff-filter=ACMRT",
                         PINS["part1_audit_arrived"], PINS["part1_response_arrived"],
                         "--", P1).decode().splitlines()
    add("part1_response_arrived", response_paths)
    sync_paths = git("diff", "--name-only", "--diff-filter=ACMRT",
                     PINS["part1_response_arrived"], PINS["part1_main_sync_arrived"],
                     "--", P1).decode().splitlines()
    add("part1_main_sync_arrived", sync_paths)
    merged_p1_paths = git("diff", "--name-only", "--diff-filter=ACMRT",
                         PINS["part1_main_sync_arrived"], PINS["main_part1_merged"],
                         "--", P1).decode().splitlines()
    merged_pg_paths = git("diff", "--name-only", "--diff-filter=ACMRT",
                         PINS["literature_index_update"], PINS["main_part1_merged"],
                         "--", PG).decode().splitlines()
    add("main_part1_merged", merged_p1_paths + merged_pg_paths +
        ["PROOF_STATUS.md", "ID_CROSSWALK.md", "state/IDEAS.md", "state/CURRENT.md",
         "PAPER_MAP.md", "topics/padua-batch-20261031/ALLOCATIONS.md"])
    pg_paths = tree(PINS["programme"])
    add("programme", [p for p in pg_paths if
        p in [PG + x for x in ["OPEN_TARGETS.md", "checks/decisive-gen4-2.md",
            "checks/decisive-gen1-3.md", "checks/adversarial-gen1-3.md",
            "ideas/candidates.md", "gate-rejected.md", "lit/baseline.md",
            "response-02.md", "audit-03.md"]]
        or p.startswith(PG + "theory/")
        or p.startswith(PG + "checks/code/decisive/gen4-2/")
        or p.startswith(PG + "checks/code/decisive/gen1-3/")
        or p in ["state/IDEAS.md", "literature/INDEX.md", "literature/CORPUS.md",
            "literature/lattice-unisolvence/records/padua-2006.md",
            "literature/lattice-unisolvence/baseline.md"]])
    add("lanczos", ["tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-304-square-case-commutator-bounds.md"])
    add("current_main_and_rules", RULES + ["templates/HANDOFF.md", "templates/THEORY.md",
        "state/IDEAS.md", "literature/INDEX.md", "PROOF_STATUS.md", "ID_CROSSWALK.md"])
    add("literature_index_update", ["literature/INDEX.md", "literature/CORPUS.md"])
    add("programme_final", [p for p in pg_paths if p.startswith(PG + "theory/")
        or p == PG + "OPEN_TARGETS.md"])
    # Retain both versions of changed authoritative inputs and unchanged rules.
    compare_paths = RULES + [p for (sha, p) in requested if sha == PINS["programme"]]
    old_paths = set(tree(PINS["part1_programme"]))
    add("part1_programme", [p for p in compare_paths if p in old_paths])
    inputs = []
    for (sha, path), label in sorted(requested.items()):
        data = git("show", f"{sha}:{path}")
        inputs.append({"source": label, "commit": sha, "path": path,
                       "git_blob": git("rev-parse", f"{sha}:{path}").decode().strip(),
                       **identity(data)})
    changes = []
    for path in sorted(set(compare_paths)):
        if path in old_paths:
            old = git("rev-parse", f"{PINS['part1_programme']}:{path}").decode().strip()
            new = git("rev-parse", f"{PINS['programme']}:{path}").decode().strip()
            if old != new:
                changes.append({"path": path, "old_git_blob": old, "new_git_blob": new})
    outputs = []
    # Checkpoint identities cover files available from the index/repository.
    # Untracked prototypes may change during parallel development; stage each
    # durable artifact before regenerating this manifest.
    indexed_paths = set(git("ls-files", "--", TOPIC).decode().splitlines())
    for relative in sorted(indexed_paths):
        path = Path(relative)
        if (path.name != "evidence-manifest.json" and "__pycache__" not in path.parts
                and not relative.startswith(TOPIC + "/handoffs/")):
            # Hash the index bytes that this checkpoint will commit. Parallel
            # workers may be editing tracked working files not yet staged.
            data = git("show", f":{relative}")
            outputs.append({"path": relative, **identity(data)})
    result = {"schema": 1, "purpose": "mechanical provenance; no scientific execution or verification",
              "pins": PINS, "python": platform.python_version(),
              "command": f"python {TOPIC}/code/evidence_manifest.py",
              "input_source": "local immutable Git objects via git show COMMIT:PATH; no files fetched remotely by this script",
              "inputs": inputs, "changed_compared_inputs": changes,
              "output_source": "Git index snapshot via git show :PATH; stage durable changes before generation; unstaged edits are excluded",
              "outputs": outputs,
              "exclusions": ["evidence-manifest.json excludes itself to avoid a recursive hash",
                             "numbered handoffs are Git-pinned publication metadata, excluded because required post-candidate status closure/addition occurs in the following commit",
                             "untracked prototypes and unstaged tracked edits are excluded until staged for a checkpoint",
                             "__pycache__ files are interpreter cache, not evidence"]}
    dest = ROOT / TOPIC / "evidence-manifest.json"
    dest.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"inputs": len(inputs), "outputs": len(outputs), "manifest_bytes": dest.stat().st_size,
                      "changed_compared_inputs": len(changes)}))


if __name__ == "__main__":
    main()
