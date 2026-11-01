#!/usr/bin/env python3
"""Read-only, pinned literature integration checks; no paper retrieval or Git writes."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
PINS = {
    "head": "a2dd845b8a231e1b00733e1361e2a9ad3bad222f",
    "baseline": "cf01449fc96233c9074ce25efcb056535414aa1d",
    "main": "9739a0c56b7a3976422ce60a8441bfbbfd6554df",
    "consolidation": "ae36ec013630c939fb1b2c1cdddb2cf12cc80cf0",
    "pre_consolidation": "9a77f2b10d42bb43aea01cacfcea86469c87c5dc",
    "merge": "1167c33e71e2b0677e569f5fbae7ed97160fa8e9",
    "allocation": "896afd6c6befee3bc05f74d178cab9400baab31a",
}
TOPIC = "topics/bivariate-lanczos-20261031/"

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def get(ref, path):
    return git("show", f"{ref}:{path}").decode()

def paths(ref):
    return git("ls-tree", "-r", "--name-only", ref, "literature/records/").decode().splitlines()

def rows(text):
    return [[cell.strip() for cell in line.strip().strip("|").split(" | ")] for line in text.splitlines() if line.startswith("| ")]

def norm(s):
    return s.strip()

def field(block, name):
    m = re.search(r"^- " + re.escape(name) + r": (.*)$", block, re.M)
    return m[1] if m else None

H, B, M = (PINS[x] for x in ("head", "baseline", "main"))
hp, bp, mp = (paths(x) for x in (H, B, M))
records = {p: get(H, p) for p in hp}
checks = {"pins": PINS, "head_matches_pin": git("rev-parse", "HEAD").decode().strip() == H}
changes = [line.split("\t") for line in git("diff", "--name-status", PINS["pre_consolidation"], PINS["consolidation"], "--", "literature/records/").decode().splitlines()]
checks["consolidation_record_changes"] = dict(Counter(status for status, path in changes))
changed = [p for _, p in changes]
checks["consolidation_added"] = [p for status, p in changes if status == "A"]
checks["consolidation_updated"] = [p for status, p in changes if status == "M"]

shared = sorted((set(bp) & set(mp)) - {"literature/records/README.md"})
checks["shared_sources"] = {}
checks["shared_source_count"] = len(shared)
checks["accepted_main_record_file_count_including_readme"] = len(mp)
for p in shared:
    before, after = get(M, p), records[p]
    missing = [line for line in before.splitlines() if line.strip() and not any(line in current for current in after.splitlines())]
    headings = re.findall(r"^#{2,4} LIT-[^\n]+", before, re.M)
    checks["shared_sources"][p] = {"whole_main_text_literal_substring": before.strip() in after,
        "missing_nonblank_lines_even_as_extended_line": missing,
        "main_statement_headings_preserved": all(x in after for x in headings)}
checks["all_main_records_preserved_nonblank_lines"] = [p for p in mp if any(
    line.strip() and not any(line in current for current in records.get(p, "").splitlines())
    for line in get(M, p).splitlines())]
main_index, index = get(M, "literature/INDEX.md"), get(H, "literature/INDEX.md")
checks["missing_main_index_nonblank_lines"] = [s for s in main_index.splitlines() if s.strip() and s not in index]
main_rows = {r[0]: r for r in rows(get(M, "literature/CORPUS.md"))}
head_rows = {r[0]: r for r in rows(get(H, "literature/CORPUS.md"))}
checks["main_corpus_field_preservation_failures"] = []
for key, row in main_rows.items():
    if key in ("Key", "---") or key.startswith("-"): continue
    now = head_rows.get(key, [])
    for i, value in enumerate(row):
        if i >= len(now) or value not in now[i]:
            checks["main_corpus_field_preservation_failures"].append([key, i, value, now[i] if i < len(now) else None])

aliases = json.loads(get(H, TOPIC + "pr-prep/id-map.json"))["map"]
lit_map = {k: v for k, v in aliases.items() if k.startswith("LIT?")}
heads, blocks = {}, {}
for p, text in records.items():
    matches = list(re.finditer(r"^#{2,4} (LIT-\d+) \((LIT\?bivariate-lanczos-claude-\d+)\)[^\n]*", text, re.M))
    for i, match in enumerate(matches):
        fid, alias = match[1], match[2]
        heads.setdefault(alias, []).append([fid, p])
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        blocks[alias] = text[match.start():end]
index_rows = {}
for row in rows(index):
    m = re.fullmatch(r"(LIT-\d+) \((LIT\?bivariate-lanczos-claude-\d+)\)", row[0])
    if m: index_rows.setdefault(m[2], []).append([m[1], row])
checks["final_mapping_count"] = len(lit_map)
checks["final_mapping_range"] = [min(int(v[4:]) for v in lit_map.values()), max(int(v[4:]) for v in lit_map.values())]
checks["final_mapping_failures"] = []
checks["new_statement_field_failures"] = []
checks["new_statement_coverage"] = []
for alias, fid in lit_map.items():
    hs, irs = heads.get(alias, []), index_rows.get(alias, [])
    if len(hs) != 1 or len(irs) != 1:
        checks["final_mapping_failures"].append([alias, "multiplicity", hs, irs]); continue
    got_fid, p = hs[0]
    row_fid, row = irs[0]
    path = re.search(r"\]\((records/[^)]+)\)", row[5])
    target = path[1] if path else row[5]
    if got_fid != fid or row_fid != fid or p != "literature/" + target or row[3] != Path(p).stem:
        checks["final_mapping_failures"].append([alias, "record/id/key disagreement", hs, row])
    if int(alias.rsplit("-",1)[1]) < 401: continue
    block = blocks[alias]
    statement = field(block, "Statement in faithful paraphrase")
    hypo = field(block, "Hypotheses and notation")
    locator = field(block, "Page / theorem / equation")
    if row[2] != statement + " Hypotheses: " + hypo or row[4] != locator:
        checks["new_statement_field_failures"].append([alias, "statement/hypotheses/locator differs", row[2], statement, hypo, row[4], locator])
    checks["new_statement_coverage"].append({"id": fid, "alias": alias, "record": p,
        "verification": field(block, "Verification"), "reading": field(block, "Reading evidence and limitations"),
        "index_coverage": row[6]})

# A preservation comparison of every old topic statement field, independent of ID allocation.
checks["baseline_statement_field_changes"] = []
baseline_count = 0
for p in bp:
    text = get(B, p)
    ms = list(re.finditer(r"^#{2,4} (LIT\?bivariate-lanczos-claude-\d+)[^\n]*", text, re.M))
    for i, m in enumerate(ms):
        alias = m[1]; baseline_count += 1
        before = text[m.start():ms[i+1].start() if i+1 < len(ms) else len(text)]
        after = blocks.get(alias, "")
        for name in ("Verification", "Statement in faithful paraphrase", "Hypotheses and notation", "Page / theorem / equation", "Reading evidence and limitations"):
            a, b = field(before, name), field(after, name)
            if a is not None and a != b:
                checks["baseline_statement_field_changes"].append([alias, p, name, a, b])
checks["baseline_statement_count"] = baseline_count

# Exact canonical identifiers, restricted to metadata, reveal source duplication, not merely ID duplication.
identities = defaultdict(set)
for p, text in records.items():
    if len(Path(p).parts) != 3: continue
    loc = field(text, "DOI / URL / supplied location") or ""
    for arxiv in re.findall(r"arxiv\.org/(?:abs|pdf)/([\w./-]+)", loc):
        identities["arxiv:" + arxiv.removesuffix(".pdf")].add(p)
checks["duplicate_arxiv_sources"] = {k: sorted(v) for k,v in identities.items() if len(v)>1}

inputs = sorted(set(hp + ["AGENTS.md", "agents/WORKFLOW.md", "agents/codex/CODEX.md", "state/IDEAS.md", "literature/INDEX.md", "literature/CORPUS.md", TOPIC + "pr-prep/id-map.json", TOPIC + "lit/search-log.md", TOPIC + "audit-01/protocol.md"] + [TOPIC + f"reviews/L{i}-prior-art-01.md" for i in (1,2,3)]))
manifest = []
for p in inputs:
    blob = git("show", f"{H}:{p}")
    manifest.append({"path": p, "bytes": len(blob), "sha256": hashlib.sha256(blob).hexdigest(), "worktree_matches_head": (ROOT/p).read_bytes() == blob})
checks["input_worktree_mismatches"] = [x["path"] for x in manifest if not x["worktree_matches_head"]]
checks["new_statement_count"] = len(checks["new_statement_coverage"])
checks["new_statements_missing_explicit_unverified_label"] = [x["id"] for x in checks["new_statement_coverage"] if "UNVERIFIED" not in (x["verification"] or "")]
checks["frozen_prior_reviews_unchanged_from_baseline"] = {TOPIC + f"reviews/L{i}-prior-art-01.md": get(B, TOPIC + f"reviews/L{i}-prior-art-01.md") == get(H, TOPIC + f"reviews/L{i}-prior-art-01.md") for i in (1,2,3)}
(OUT/"checks.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2)+"\n")
(OUT/"input-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({k:v for k,v in checks.items() if k not in ("new_statement_coverage", "consolidation_added", "consolidation_updated", "shared_sources")},ensure_ascii=False,indent=2))
