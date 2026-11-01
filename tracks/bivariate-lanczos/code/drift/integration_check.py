"""Integration and reservation check for padua-lanczos-drift-20261101 against main and open PRs.

Read-only: inspects committed Git objects only (no working-tree content), and runs
a disposable squash rehearsal in a temporary worktree that is removed afterwards.
Usage: python3 integration_check.py --head <sha> --main <sha> --pr PR12=<sha> --pr PR16=<sha> --output <json>
"""
import argparse, hashlib, json, re, subprocess, sys, tempfile, os, datetime

def git(*a, check=True):
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f"git {' '.join(a)} failed: {r.stderr}")
    return r.stdout

RANGES = {"PD-T": (136, 155, 3), "PD-N": (62, 71, 3), "IDEA": (246, 285, 3), "LIT": (445, 459, 3)}
def final_id_regex():
    parts = []
    for ns, (lo, hi, w) in RANGES.items():
        nums = "|".join(f"{i:0{w}d}" for i in range(lo, hi + 1))
        sep = "-" if ns in ("IDEA", "LIT") else ""
        parts.append(rf"\b{ns}{'-' if ns in ('IDEA','LIT') else ''}(?:{nums})\b")
    return re.compile("|".join(parts))

LEDGER = "topics/padua-batch-20261031/ALLOCATIONS.md"
XWALK = "ID_CROSSWALK.md"
OWN = "topics/padua-lanczos-drift-20261101/"
REQUIRED_LEDGER_TOKENS = [
    "PD-T136–PD-T155", "PD-N062–PD-N071", "IDEA-246–IDEA-285", "LIT-445–LIT-459",
    "6920ba632843597c37e1493d077c1df2e89f54cb",
    "PD-T106–PD-T135", "PD-N044–PD-N061", "IDEA-210–IDEA-245", "LIT-427–LIT-444",
    "PD-T118–135, PD-N054–061, IDEA-228–245, LIT-429–444",
    "**Integration order (AC, 2026-11-01):**",
]
REQUIRED_XWALK_TOKENS = ["| PD-N?mz2d-codex-41 | PD-N045 |", "Administrative reciprocal mapping", "PD-T110", "## Lanczos drift reservation (no final assignment)"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--head", required=True); ap.add_argument("--main", required=True)
    ap.add_argument("--pr", action="append", default=[]); ap.add_argument("--output", required=True)
    a = ap.parse_args()
    head = git("rev-parse", a.head).strip(); mainsha = git("rev-parse", a.main).strip()
    out = {"generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "code_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "head": head, "main": mainsha, "checks": {}}
    c = out["checks"]
    c["main_is_ancestor_of_head"] = subprocess.run(["git", "merge-base", "--is-ancestor", mainsha, head]).returncode == 0
    led = git("show", f"{head}:{LEDGER}"); xw = git("show", f"{head}:{XWALK}")
    c["ledger_tokens_present"] = {t: (t in led) for t in REQUIRED_LEDGER_TOKENS}
    c["crosswalk_tokens_present"] = {t: (t in xw) for t in REQUIRED_XWALK_TOKENS}
    # Every line of main's crosswalk survives; ledger changes vs main are limited to the PR15 scan-link line.
    main_xw = git("show", f"{mainsha}:{XWALK}").splitlines()
    c["crosswalk_main_lines_all_retained"] = all(l in xw.splitlines() for l in main_xw)
    d = git("diff", "--unified=0", mainsha, head, "--", LEDGER)
    removed = [l[1:] for l in d.splitlines() if l.startswith("-") and not l.startswith("---")]
    added = [l[1:] for l in d.splitlines() if l.startswith("+") and not l.startswith("+++")]
    c["ledger_lines_removed_vs_main"] = removed; c["ledger_lines_added_vs_main"] = added
    c["ledger_change_limited_to_pr15_scan_link"] = len(removed) <= 1 and all("allocation-scan.json" in l for l in removed + added)
    # Protected paths unchanged vs main.
    prot = ["state", "PROOF_STATUS.md", "PAPER_MAP.md", "literature", ".github", "AGENTS.md", "agents", "templates"]
    c["protected_paths_diff_vs_main"] = git("diff", "--name-only", mainsha, head, "--", *prot).split()
    th = git("diff", "--name-status", mainsha, head, "--", "tracks/bivariate-lanczos/theory").splitlines()
    c["theory_changes_vs_main"] = th
    c["only_drift_codex_theory_files_changed"] = all(re.search(r"theory/drift-codex-[^/]+\.md$", l) and l[0] in "AM" for l in th)
    old = [p for p in git("ls-tree", "-r", "--name-only", mainsha, "tracks/bivariate-lanczos/theory").split() if "drift-codex-" not in p]
    c["old_theory_files_count"] = len(old)
    c["old_theory_files_byte_identical"] = not git("diff", "--name-only", mainsha, head, "--", *old).strip()
    # Reserved final IDs must not be used as final IDs anywhere except reservation prose.
    rx = final_id_regex()
    refs = {"main": mainsha, "head": head}
    for spec in a.pr:
        k, v = spec.split("="); refs[k] = git("rev-parse", v).strip()
    use = {}
    for name, ref in refs.items():
        hits = {}
        for path in git("ls-tree", "-r", "--name-only", ref).split():
            if not path.endswith((".md", ".json", ".py", ".csv", ".txt")): continue
            if path.startswith(OWN) or path == LEDGER or path == XWALK: continue
            txt = git("show", f"{ref}:{path}", check=False)
            m = sorted(set(rx.findall(txt)))
            if m: hits[path] = m
        # Final assignments: registry files and record headers. Other hits are prose/validation mentions.
        assign = {}
        reg = ["PROOF_STATUS.md", "PAPER_MAP.md", "literature/INDEX.md", "state/IDEAS.md", "state/CURRENT.md"]
        for path in reg:
            txt = git("show", f"{ref}:{path}", check=False)
            m = sorted(set(rx.findall(txt)))
            if m: assign[path] = m
        xtxt = git("show", f"{ref}:{XWALK}", check=False)
        rows = sorted(set(x for l in xtxt.splitlines() if l.startswith("|") for x in rx.findall(l)))
        if rows: assign[XWALK + " (table rows)"] = rows
        for path in git("ls-tree", "-r", "--name-only", ref, "tracks").split():
            if not path.endswith(".md"): continue
            first = git("show", f"{ref}:{path}", check=False).splitlines()[:1]
            m = sorted(set(rx.findall(first[0]))) if first else []
            if m: assign[path + " (header)"] = m
        use[name] = {"ref": ref, "final_assignments_of_reserved_ids": assign,
                     "other_mentions_outside_own_topic_and_ledger": hits}
    c["reserved_range_usage"] = use
    # Conflict rehearsal of head against each open PR.
    conf = {}
    for spec in a.pr:
        k, v = spec.split("=")
        r = subprocess.run(["git", "merge-tree", "--write-tree", "--name-only", head, v], capture_output=True, text=True)
        lines = r.stdout.splitlines()
        conf[k] = {"clean": r.returncode == 0, "conflicted_files": [l for l in lines[1:] if l and not l.startswith(("Auto-merging", "CONFLICT"))]}
    c["merge_tree_vs_open_prs"] = conf
    # Disposable squash rehearsal onto main.
    with tempfile.TemporaryDirectory() as td:
        wt = os.path.join(td, "wt")
        git("worktree", "add", "--detach", wt, mainsha)
        try:
            r = subprocess.run(["git", "-C", wt, "merge", "--squash", head], capture_output=True, text=True)
            st = subprocess.run(["git", "-C", wt, "status", "--porcelain"], capture_output=True, text=True).stdout
            tree = subprocess.run(["git", "-C", wt, "write-tree"], capture_output=True, text=True).stdout.strip()
            c["squash_rehearsal"] = {"merge_squash_rc": r.returncode, "unmerged_entries": [l for l in st.splitlines() if l[:2] in ("UU", "AA", "DU", "UD")],
                                     "squashed_tree": tree, "head_tree": git("rev-parse", f"{head}^{{tree}}").strip()}
            c["squash_rehearsal"]["tree_equals_head_tree"] = c["squash_rehearsal"]["squashed_tree"] == c["squash_rehearsal"]["head_tree"]
        finally:
            git("worktree", "remove", "--force", wt)
    ok = (c["main_is_ancestor_of_head"] and all(c["ledger_tokens_present"].values()) and all(c["crosswalk_tokens_present"].values())
          and c["crosswalk_main_lines_all_retained"] and c["ledger_change_limited_to_pr15_scan_link"] and not c["protected_paths_diff_vs_main"]
          and c["only_drift_codex_theory_files_changed"] and c["old_theory_files_byte_identical"]
          and all(not v["final_assignments_of_reserved_ids"] for v in use.values())
          and c["squash_rehearsal"]["merge_squash_rc"] == 0 and c["squash_rehearsal"]["tree_equals_head_tree"])
    out["result"] = "PASS" if ok else "FAIL"
    json.dump(out, open(a.output, "w"), indent=1, ensure_ascii=False); print(out["result"])

if __name__ == "__main__":
    main()
