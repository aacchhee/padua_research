#!/usr/bin/env python3
"""Mechanical audit-response guards. No scientific execution or proof check.

Run at repository root after staging final response files. Read Git index bytes;
write a fresh small receipt, then stage it and regenerate the evidence manifest.
The accepted candidate and immutable auditor delivery remain separate pins.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
TOPIC = "topics/padua-proof-attempts-2-20261101/"
CANDIDATE = "4265bb94f987ce77d89cd5e15a8c435cbd1411d0"
DELIVERY = "0dd4a6df2db4a2019541604bb97c05926ab3c22b"
MAIN = "28aaa20861d08074b77efc74eaef75cdcb36234d"
BLOCK = r"Target: `([^`]+)`\s+Pinned commit: `([0-9a-f]{40})`\s+Old:\s+```text\n(.*?)\n```\s+New:\s+```text\n(.*?)\n```"
OLD_CHAIN = "where the last inequality follows from delta_t<2t and1/80>1/100."
NEW_CHAIN = "where `(h/2)^2=t/40=2t*(1/80)>2t/100>delta_t/100`, using `delta_t<2t`."


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def blob(revision, path):
    return git("show", revision + ":" + path)


def paths(revision):
    return git("ls-tree", "-r", "--name-only", revision, "--", TOPIC).decode().splitlines()


def main():
    errors = []

    def check(ok, message):
        if not ok:
            errors.append(message)

    original_paths = paths(CANDIDATE)
    indexed = git("ls-files", "--", TOPIC).decode().splitlines()
    # Every pre-existing source and scientific generated output stays frozen.
    frozen = [p for p in original_paths if p.startswith(TOPIC + "code/")
              or (p.startswith(TOPIC + "outputs/") and not p.endswith(".md"))]
    for p in frozen:
        check(blob(CANDIDATE, p) == blob("", p), "frozen source/output changed: " + p)
    auditor = [p for p in paths(DELIVERY) if p == TOPIC + "audit-01.md"
               or p.startswith(TOPIC + "audit-support/")]
    for p in auditor:
        check(blob(DELIVERY, p) == blob("", p), "auditor delivery changed: " + p)

    proof_sections = 0
    for p in original_paths:
        if not p.startswith(TOPIC + "theory/") or not p.endswith(".md"):
            continue
        before = blob(CANDIDATE, p).decode()
        after = blob("", p).decode()
        if "-N01-" in p:
            check(before.count(OLD_CHAIN) == 1 and after.count(NEW_CHAIN) == 1,
                  "negative01 arithmetic clarification not exact")
            before = before.replace(OLD_CHAIN, NEW_CHAIN)
        pattern = r"^## Proof[^\n]*\n.*?(?=^## |\Z)"
        old_sections = re.findall(pattern, before, re.M | re.S)
        new_sections = re.findall(pattern, after, re.M | re.S)
        proof_sections += len(old_sections)
        check(old_sections == new_sections, "proof section changed: " + p)

    original_blocks = re.findall(BLOCK, blob(CANDIDATE, TOPIC + "proposed-record-changes.md").decode(), re.S)
    current_blocks = re.findall(BLOCK, blob("", TOPIC + "proposed-record-changes.md").decode(), re.S)
    check(len(original_blocks) == len(current_blocks) == 10, "ten literal proposals required")
    for old_row, row in zip(original_blocks, current_blocks):
        target, pin, old, new = row
        check(old_row[:3] == row[:3], "proposal target/pin/Old changed: " + target)
        if old:
            check(blob(pin, target).decode().count(old) == 1, "Old not unique at pin: " + target)
            check(blob(MAIN, target).decode().count(old) == 1, "Old not unique at main: " + target)
            check(old in new, "Old not retained in New: " + target)
        else:
            check(target not in git("ls-tree", "-r", "--name-only", MAIN).decode().splitlines(),
                  "new-file target already exists")
        for phrase in ["PROVEDandREFUTES", "EVERYfixedpositive", "Part2Claudeaudit", "N8at least44interior"]:
            check(phrase not in new, "uncorrected run-together proposal words: " + phrase)

    old_handoff = blob(DELIVERY, TOPIC + "handoffs/03-response.md").decode()
    new_handoff = blob("", TOPIC + "handoffs/03-response.md").decode()
    check(re.sub(r"^- Status:.*$", "- Status: <publication>", old_handoff, flags=re.M)
          == re.sub(r"^- Status:.*$", "- Status: <publication>", new_handoff, flags=re.M),
          "handoff03 instruction body changed")
    outside = [p for p in git("diff", "--cached", "--name-only", MAIN).decode().splitlines()
               if not p.startswith(TOPIC)]
    check(not outside, "outside-topic staged tree differs from pinned main")
    check(not git("diff", "--name-only").strip(), "unstaged tracked edits")

    for p in indexed:
        if not p.endswith(".md"):
            continue
        text = blob("", p).decode()
        text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
        for target in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", text):
            target = unquote(target.split("#")[0])
            if not target or re.match(r"[a-zA-Z][\w+.-]*:", target):
                continue
            check(((ROOT / p).parent / target).exists(), "broken local Markdown link: " + p + " -> " + target)

    generated = [(p, len(blob("", p))) for p in indexed if not p.endswith((".md", ".py", ".sh"))]
    total = sum(n for _, n in generated)
    maximum = max(n for _, n in generated)
    check(total <= 5_000_000 and maximum <= 1_000_000, "generated evidence budget exceeded")
    result = {
        "purpose": "mechanical response guards only; no scientific execution or audit claim",
        "accepted_scientific_candidate": CANDIDATE,
        "immutable_audit_delivery": DELIVERY,
        "main": MAIN,
        "source": "Git index for final response; immutable Git objects for baselines",
        "frozen_source_and_scientific_output_files": len(frozen),
        "immutable_auditor_files": len(auditor),
        "unchanged_proof_sections_except_exact_authorized_chain": proof_sections,
        "literal_proposals_checked": len(current_blocks),
        "generated_bytes_at_check": total,
        "largest_generated_bytes": maximum,
        "receipt_excludes_its_own_new_bytes_until_final_manifest_budget_check": True,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "errors": errors,
        "passed": not errors,
    }
    destination = ROOT / TOPIC / "response-support/verification.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
