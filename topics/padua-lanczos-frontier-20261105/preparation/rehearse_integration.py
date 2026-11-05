#!/usr/bin/env python3
"""Root-only mechanical squash rehearsal; no commits, fetches or scientific runs.

Run at the topic repository root with full --base (origin/main) and --head
SHAs. --output must be a new path outside the repository. Raw command logs
remain under /tmp/padua-lanczos-frontier-preparation, including on failure.
Only the unique branch/worktree created by this invocation is cleaned up.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import uuid


TOPIC = "codex/padua-lanczos-frontier-20261105"
STORAGE = Path("/tmp/padua-lanczos-frontier-preparation")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(all(re.fullmatch(r"[0-9a-f]{40}", s) for s in (args.base, args.head)),
            "--base and --head must be full lowercase SHA-1 commit IDs")
    root = Path.cwd().resolve()
    output = args.output.absolute()
    require(not output.exists(), "Receipt output already exists")
    require(output.parent.is_dir(), "Receipt output parent must exist")
    require(not output.resolve().is_relative_to(root), "Receipt output must be outside repository")
    STORAGE.mkdir(parents=True, exist_ok=True)
    require(STORAGE.resolve() == STORAGE, "Temporary storage must not be a symlink")
    logs = Path(tempfile.mkdtemp(prefix="rehearsal-logs-", dir=STORAGE))
    token = uuid.uuid4().hex
    worktree = STORAGE / ("rehearsal-" + token)
    branch = "codex/pr24-integration-rehearsal-" + token
    commands = []
    env = os.environ.copy()
    # Do not inherit alternate indexes, repositories, worktrees or object stores.
    for key in list(env):
        if key.startswith("GIT_"):
            del env[key]
    env.update(GIT_TERMINAL_PROMPT="0", GIT_OPTIONAL_LOCKS="0", LC_ALL="C")

    def git(cwd, *argv, allowed=(0,), trim=True):
        cmd = ["git", "-c", "core.hooksPath=/dev/null", *argv]
        done = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, check=False)
        index = len(commands)
        stem = f"{index:02d}"
        (logs / (stem + ".stdout")).write_bytes(done.stdout)
        (logs / (stem + ".stderr")).write_bytes(done.stderr)
        commands.append({"cwd": str(cwd), "argv": cmd, "returncode": done.returncode,
                         "log": stem})
        require(done.returncode in allowed,
                f"Command {index} failed ({done.returncode}); see {logs / (stem + '.stderr')}")
        decoded = done.stdout.decode("utf-8", errors="surrogateescape")
        return decoded.strip() if trim else decoded

    def refs():
        return {name: git(root, "rev-parse", "--verify", "--quiet", name, allowed=(0, 1))
                for name in ("refs/heads/main", "refs/remotes/origin/main")}

    def snapshot():
        # Hash full status and diffs instead of embedding potentially large root edits.
        data = {"branch": git(root, "symbolic-ref", "--short", "HEAD"),
                "head": git(root, "rev-parse", "HEAD"), "main_refs": refs()}
        for name, argv in (("status", ("status", "--porcelain=v1", "-z", "--untracked-files=all")),
                           ("unstaged", ("diff", "--binary", "--no-ext-diff", "--no-textconv")),
                           ("staged", ("diff", "--cached", "--binary", "--no-ext-diff", "--no-textconv"))):
            value = git(root, *argv, trim=False)
            data[name + "_sha256"] = hashlib.sha256(value.encode("utf-8", "surrogateescape")).hexdigest()
        return data

    def inventory_logs():
        # Freeze only after the final Git/snapshot command. The index identifies
        # itself through the receipt, avoiding an impossible self-hash entry.
        index_path = logs / "file-inventory.json"
        files = []
        for path in sorted(logs.iterdir()):
            if path == index_path:
                continue
            require(path.is_file() and not path.is_symlink(), "Unexpected log entry: " + str(path))
            content = path.read_bytes()
            files.append({"filename": path.relative_to(logs).as_posix(),
                          "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()})
        index = {"schema": 1, "scope": "All files in this log directory except this inventory",
                 "count": len(files), "files": files}
        content = (json.dumps(index, separators=(",", ":")) + "\n").encode()
        index_path.write_bytes(content)
        return {"path": str(index_path), "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(), "count": len(files),
                "retention": "Local temporary files; no archival or lifetime guarantee. "
                             "Regenerate by rerunning this helper at the recorded base/head; "
                             "unique paths and resulting log bytes may differ."}

    before = None
    branch_owned = False
    wt_owned = False
    tree = None
    error = None
    cleanup_errors = []
    try:
        require(Path(git(root, "rev-parse", "--show-toplevel")).resolve() == root,
                "Execute from the repository root")
        require((root / "agents/WORKFLOW.md").is_file(), "Not the Padua research repository")
        before = snapshot()
        require(before["branch"] == TOPIC, "Unexpected root branch")
        require(before["head"] == args.head, "Root HEAD differs from --head")
        require(before["main_refs"]["refs/remotes/origin/main"] == args.base,
                "origin/main differs from --base; refresh/reconcile explicitly first")
        for sha in (args.base, args.head):
            require(git(root, "rev-parse", "--verify", sha + "^{commit}") == sha,
                    "Input does not resolve to its exact commit")
        git(root, "merge-base", "--is-ancestor", args.base, args.head)
        base_tree = git(root, "rev-parse", args.base + "^{tree}")
        head_tree = git(root, "rev-parse", args.head + "^{tree}")
        require(not worktree.exists(), "Unique worktree path unexpectedly exists")
        require(not git(root, "rev-parse", "--verify", "--quiet", "refs/heads/" + branch,
                        allowed=(0, 1)), "Unique branch unexpectedly exists")
        git(root, "branch", branch, args.base)
        branch_owned = True
        # Mark before add so a partial registration can be inspected and removed.
        wt_owned = True
        git(root, "worktree", "add", str(worktree), branch)
        require(git(worktree, "symbolic-ref", "--short", "HEAD") == branch,
                "Disposable worktree branch differs")
        require(git(worktree, "rev-parse", "HEAD") == args.base, "Disposable HEAD differs from base")
        require(not git(worktree, "status", "--porcelain=v1", "--untracked-files=all"),
                "Disposable worktree starts dirty")
        git(worktree, "merge", "--squash", "--no-commit", args.head)
        require(git(worktree, "rev-parse", "HEAD") == args.base, "Squash unexpectedly moved HEAD")
        tree = git(worktree, "write-tree")
        require(tree == head_tree, "Squash index tree differs from head tree")
        require(not git(worktree, "diff", "--name-only", "--diff-filter=U"), "Unmerged entries remain")
    except Exception as exc:
        error = str(exc)
    finally:
        if wt_owned and worktree.exists():
            try:
                require(git(worktree, "symbolic-ref", "--short", "HEAD") == branch,
                        "Refuse cleanup: disposable branch changed")
                require(git(worktree, "rev-parse", "HEAD") == args.base,
                        "Refuse cleanup: disposable HEAD changed")
                git(worktree, "reset", "--hard", args.base)
                git(root, "worktree", "remove", str(worktree))
            except Exception as exc:
                cleanup_errors.append(str(exc))
        if branch_owned and not worktree.exists() and not cleanup_errors:
            try:
                require(git(root, "rev-parse", "refs/heads/" + branch) == args.base,
                        "Refuse deletion: disposable branch moved")
                git(root, "branch", "-D", branch)
            except Exception as exc:
                cleanup_errors.append(str(exc))
    try:
        after = snapshot() if before is not None else None
        require(before is not None and after == before, "Root branch/HEAD/main refs/status/diffs changed")
        require(not cleanup_errors, "Cleanup failed: " + "; ".join(cleanup_errors))
        require(error is None, error or "Rehearsal failed")
        require(not worktree.exists(), "Disposable worktree remains")
        require(not git(root, "rev-parse", "--verify", "--quiet", "refs/heads/" + branch,
                        allowed=(0, 1)), "Disposable branch remains")
        log_inventory = inventory_logs()
        receipt = {"result": "PASS", "base": args.base, "head": args.head,
                   "base_tree": base_tree, "head_tree": head_tree, "squash_tree": tree,
                   "base_is_ancestor": True, "root_before": before, "root_after": after,
                   "root_unchanged": True, "cleanup": "PASS", "disposable_branch": branch,
                   "disposable_worktree": str(worktree), "logs": str(logs), "commands": commands,
                   "log_inventory": log_inventory,
                   "scope": "Mechanical squash/tree equivalence only; no scientific validation"}
        payload = (json.dumps(receipt, separators=(",", ":")) + "\n").encode()
        require(len(payload) < 16384, "Receipt exceeds 16 KiB")
        with output.open("xb") as stream:
            stream.write(payload)
        print(f"PASS: {output} ({len(payload)} bytes); logs {logs}")
        return 0
    except Exception as exc:
        # Failure details are deliberately off-repository and never a PASS receipt.
        failure = {"result": "FAIL", "error": error, "validation_error": str(exc),
                   "cleanup_errors": cleanup_errors, "commands": commands}
        (logs / "failure.json").write_text(json.dumps(failure, indent=2) + "\n")
        inventory_logs()
        print(f"FAIL: {exc}; raw logs and failure.json: {logs}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"FAIL before rehearsal: {exc}", file=sys.stderr)
        sys.exit(1)
