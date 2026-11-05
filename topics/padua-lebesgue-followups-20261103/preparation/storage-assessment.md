# Storage assessment — PR20 preparation

2026-11-05. Rules/input head `e8ba6f90a7421fd6dad231586843a4870bdcaf15`.
Mechanical inspection only, configured Codex gpt-6.1-sol medium; serving
metadata is unexposed. **The measured bucket remains below 5,000,000 bytes,
but this assessment does not certify “well below 5 MB.”** The narrow source
classification correction does not provide a comfortable margin. No waiver
is inferred. This is a constraint for the independent preparation reviewer.

## Exact inventories

I reproduced response-01's conservative classifier using complete
`git ls-tree -r -l e8ba6f90a7421fd6dad231586843a4870bdcaf15` output. Excluded
extensions are exactly `md, py, sh, tex, bib, svg, gitignore`; every other blob
is counted, including C/C++ source and JSON metadata. The current prospective
commit inventory uses the union of `git ls-files -z --cached --others
--exclude-standard`, counts each existing regular path once at its present
worktree size, and applies the same extension rule. This includes the two
new JSON files without accidentally counting ignored scratch outputs or Git
history. No files were staged, removed, exported or otherwise changed by this
inspection.

| Snapshot | Non-record files | Exact bytes | Margin below 5,000,000 |
|---|---:|---:|---:|
| Published input e8ba6f9 | 1,252 | 4,839,525 | 160,475 |
| Current worktree snapshot, including new JSON | 1,254 | 4,851,736 | 148,264 |

The current count is **97.03472%** of 5,000,000, leaving **2.96528%**.
The exact increase is 12,211 bytes: preparation/reservation-recheck.json
11,343 and preparation/final-id-map.json 868. Both are below 16,384 bytes.
The existing evidence-manifest.json is still 15,764 bytes; its content changes
have not changed its size at this snapshot. There is no other non-record size
delta. New Markdown documentation adds no bytes to this particular bucket.

For reproducible inventory identities, SHA-256 of sorted lines
`<decimal-size>\t<path>\n` for the complete non-record inventory is:

- Input: `518d5f41b9f2a1b7097e0da740043ac87c00dd251b01508303e24ec37d525bb9`.
- Worktree snapshot: `5e6e24793be5f1b7a821425a3945943e3d1f94e5f7fa9708e0e7c26a131a7052`.

These identities pin path/size lists, not contents. They must be recomputed
at the final head, especially if further machine-readable check receipts are
added. The Markdown assessment itself does not affect either total.

## What the classifier means

The workflow's wording is “Committed generated outputs of the whole repository
together stay well below 5 MB.” The extension bucket is a deliberately broad
operational proxy, not an exact semantic census of generated outputs.
`tools/cold_storage.py` uses the same RECORD_EXT set in its planning command,
additionally excludes names beginning `cold-storage`, and applies a per-file
size threshold. Its `plan` output does not certify the whole-repository budget
or automatically decide whether every JSON is generated evidence.

There is a defensible source correction of exactly **37,326 bytes in seven
files**. These files are committed C/C++ programs, identifiable from their
code paths and content, rather than executed output:

| Path | Bytes |
|---|---:|
| tracks/bivariate-lanczos/code/L5/givens_core.c | 7,651 |
| tracks/bivariate-lanczos/code/L5/givens_dual.c | 3,952 |
| tracks/bivariate-lanczos/code/review_L5/agivens.c | 4,145 |
| topics/padua-argmax-effective-20261103/code/native_checker/kernel.cpp | 6,752 |
| topics/padua-argmax-effective-20261103/code/native_checker/unit.cpp | 1,678 |
| topics/padua-argmax-effective-20261103/code/native_producer/producer.c | 9,360 |
| topics/padua-lebesgue-followups-20261103/code/t1_native.c | 3,788 |

Removing only those source bytes yields **4,814,410 bytes**, leaving
**185,590 bytes (3.7118%)**. This is a classified remainder, still counting
metadata and administrative JSON; it is not an independently established exact
generated-evidence total. Source files and all regeneration/checking code stay
preserved.

The following disjoint metadata categories are also inside the conservative
count; their sizes are unchanged between input and current snapshot:

| Metadata path classification | Files | Bytes |
|---|---:|---:|
| Basename begins `cold-storage` | 12 | 217,961 |
| Basename exactly `evidence-manifest.json` | 6 | 170,389 |
| Other basenames containing `manifest` | 37 | 220,333 |

These 608,683 bytes are hash/size/path inventories or related metadata, not
all mathematical measurement payloads. However, they include generated hashes
and mixed handwritten status/provenance with generated entry tables. Their
being called manifests does not establish that they are wholly handwritten
records or exempt generated outputs. I have therefore retained them in the
conservative total rather than subtracting all metadata to manufacture a
larger margin. Likewise, the new final-ID map is an authored registration
record, while the reservation receipt contains machine-collected hashes and
counts; both remain counted. Logs, receipts, compressed certificates, checker
outputs and measured JSON across all topics remain counted.

Executing `python tools/cold_storage.py plan . --threshold 16384` identified
one above-threshold non-record/non-cold-manifest file: the existing PR17
evidence-manifest.json, 109,206 bytes. Its own content explicitly records the
handoff07 integrity-manifest exception and says it contains hashes/paths,
not split measurement payloads. This inherited exception does not waive the
aggregate budget and does not apply to new PR20 outputs. No unrelated repair
or cleanup is proposed or performed.

## Disposition and retention

The classification establishes a small source correction; it does **not**
establish an actual generated-output total sufficiently smaller to resolve
“well below” by measurement alone. There is no numerical definition of “well
below” in the workflow. A purely “less than 5,000,000” test would pass, but it
is weaker than the written requirement. Record the narrow margin and this
unresolved aggregate-budget interpretation explicitly for Astra and the
orchestrator's readiness decision. No approval or waiver has been supplied by
this assessment.

The large regenerable T1 certificates and logs remain outside the prospective
commit inventory. COLD_STORAGE.md still records actual artifact identities,
regeneration/retrieval paths and **pending physical delivery** to AC's Padua
cold storage; this inspection makes no delivery claim. Original executed
sources, audited receipts and all necessary producer/checker code are retained.
No evidence was rewritten, split or removed to reduce the count.
