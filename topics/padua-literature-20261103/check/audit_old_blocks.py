"""Check literal Old blocks against a pinned base without applying proposals.

Usage: python3 -I audit_old_blocks.py --repo /path/to/clone --proposal file
No network, writes, final-ID assignment, or scientific validation.
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--repo", type=Path, required=True)
parser.add_argument("--proposal", type=Path, required=True)
parser.add_argument("--base", default="440d1079e42c3ef21c40d1cf8870f5b206410c6a")
args = parser.parse_args()

def git(*argv):
    return subprocess.check_output(["git", "-C", str(args.repo), *argv])

names = git("ls-tree", "-r", "--name-only", args.base).decode().splitlines()
base = {p: git("show", args.base + ":" + p) for p in names
        if p.endswith((".md", ".bib", ".py"))}
proposal = args.proposal.read_text()
pattern = r"(?im)^Old[^\n]*\n(?:\s*\n)*```[^\n]*\n(.*?)\n```"
rows = []
for m in re.finditer(pattern, proposal, re.S):
    old = m.group(1).encode()
    matches = [[p, body.count(old)] for p, body in base.items() if old in body]
    rows.append({"line": proposal[:m.start()].count("\n") + 1, "matches": matches})
missing = [r["line"] for r in rows if not r["matches"]]
print(json.dumps({"base": args.base, "old_blocks": len(rows),
                  "missing": missing, "rows": rows}, separators=(",", ":")))
if not rows or missing:
    raise SystemExit(1)
