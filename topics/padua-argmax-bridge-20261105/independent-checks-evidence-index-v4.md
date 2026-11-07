# Independent essential-index V4 encoding review

Rules/source head: `0768cb93c4f829faf5f38d47cdd7e33faad8bf64`.
Date: 2026-11-06. Role: distinct Codex technical reviewer; requested model
`gpt-6-astra`, medium (API accepted); serving model metadata is not exposed,
so this is not an attestation of runtime model identity.

Scope: routine lossless metadata encoding only. No scientific claim, research
round, novelty claim, evidence removal, hash truncation, archive operation or
registry change. Full ideas/novelty review is inapplicable to this scope. Only
this report and `code/evidence_index_v4_review_checks.py` are reviewer-owned.
The active helper and manifest remain read-only; Git belongs to the root agent.

## Preregistered independent checks (before execution)

Run a pure standard-library Python checker with a 2-second CPU hard limit,
single process except isolated short CLI checks (combined measured CPU below
2 seconds). Independently decode all 176 current rows and rehash their files;
compare V2/V3/V4 rows and opaque metadata; reconstruct greedy prefix selection
using actual JSON byte counts on small Unicode/escaped fixtures crossing index
9/10; exercise canonical path, bool/range/full-base64 failures, outside/self
references, and temporary replacement/cleanup failure. Check active input bytes
unchanged. No native/scientific imports or jobs. Developer tests are inspected;
any executed rerun will be recorded distinctly below.

## Results

PASS within this technical scope; no BLOCKING, MAJOR or MINOR findings.
Candidate adoption is acceptable subject to the mechanical checks below.
This independent Codex check supplements, rather than claims to replace, any
separately required cross-agent workflow handoff.

Reviewed identities (SHA-256):

- Candidate, 10914 bytes: `ca6b511e4eb1282f587407cd8c2d81b542f498fcca401d7daeb075132a57025d`.
- Developer checks, 9983 bytes: `5538e96a19ded4e3ea93589a8a9a78d06a0e8705c8098542e58710f5baf250dc`.
- Existing helper: `cfa6a797978e09169b27592f34936621bc851d63b4de8a87fa2c17a4167fa9d3`.
- Existing index: `ce6a232087a886c33a389f0c56e37a5f398f1875bf03f0897718a874ca5e4167`.
- Pure V4 output: `6581abec9e9859be0e7a5aa25f6743f926f9f3900850c8655642ac137c77fafd`.
- Independent checker: `c0fdeaaa55d7ee2419f3ac648bf4ec9ad1acd1752a1db4959d330c461a0fc796`.

Executed from repository root with Python 3.12.14:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 topics/padua-argmax-bridge-20261105/code/evidence_index_v4_review_checks.py
PYTHONDONTWRITEBYTECODE=1 python3 topics/padua-argmax-bridge-20261105/code/evidence_index_v4_checks.py
```

Independent checker PASS: 176 independent file rehashes, 22 rejection cases,
18 real-data prefixes, 15 oracle-fixture prefixes, 0.248164 measured CPU seconds
including child CLI processes. Developer-checker independent rerun PASS: all
176 files rehashed, 75 rejection cases, 0.4163 measured CPU seconds including
children. Combined reported CPU 0.664464 seconds, below the 2-second review
budget. The independent checker has a 2-second process CPU hard limit; its
child-inclusive total is also asserted below 2 seconds. The developer suite
retains its own preregistered process limit and completed within this budget.
No random seeds, scientific/native code, external service calls for computation,
or heavy jobs were used. Outputs are summarized here; no bulk receipt is needed.

The current index converts from 15403 to 14554 bytes: 849 bytes saved, not 2 KiB.
The strict limit is less than 16384 bytes; the result can grow another 1829 bytes
and remain strictly below it. All decoded paths, sizes, complete 32-byte hashes,
total bytes, and nonencoding metadata agree. The actual index and existing
helper were unchanged at completion of both test runs.

## Inspection and independent coverage

Read the complete candidate/developer checker and diff against the existing
helper. V2/V3 normalization and fixed V3 dictionary remain compatible;
`compact()` still emits V3, while `compact_v4()` and `--compact-v4` are explicit.
V4 prefix validation checks unused prefixes too, permits partial canonical
components, and validates each complete concatenated path. A suffix beginning
with `/` is valid only when concatenation is canonical (tested `a` + `/x`).
Duplicate resolved row strings, bool indices/sizes, range violations, traversal,
noncanonical base64 and incomplete digests are rejected. Filesystem verification
separately rejects self references and symlink escapes.

The independent oracle reconstructs adjacent-path common prefixes without the
candidate's prefix utility, then evaluates whole serialized JSON representations
for every eligible greedy choice. It agrees on a 45-path fixture with Unicode,
quotes, tabs, dotfiles and nested prefixes, including dictionary index digit
changes. The gain calculation includes dictionary commas/quotes and row index
width; the candidate's additive string cost matches compact UTF-8 JSON costs.
This supports the stated greedy algorithm, not global optimality of compression.

Both API conversion directions preserve metadata and leave their input untouched.
Temporary CLI fixtures passed compaction/check. Injected replacement failure
leaves the original index intact and removes the temporary. The developer suite
rerun exercises both pre-replacement index-change comparisons and cleanup,
malformed input, strict no-improvement refusal, CLI argument conflict, and
changed evidence rejection.

## Verification limits and mechanical adoption

The race checks detect changes at two explicit comparisons. They do not provide
locking or compare-and-swap: another writer can change the index after the final
comparison and before `replace`, or evidence after verification. This inherited
limitation is acceptable for the instructed single-writer root-agent operation;
no general concurrency-safety claim is made. Atomic replacement is not a claim
of directory-fsync crash durability. Synthetic failure checks do not exhaust
all filesystem errors.

At this report's completion, the active helper/index have not been adopted.
The root agent must copy the exact candidate bytes to `code/evidence_index.py`,
confirm the above candidate hash and same-directory default root, and inspect
the resulting diff. It may retain the tested candidate or remove that duplicate
without changing the adopted bytes. Then transform the actual index using the
explicit V4 entry point, independently compare decoded rows and all nonencoding
metadata to the frozen pre-adoption index, and rehash every referenced file.
These are mechanical integration checks, not a new research/audit round.
Both checkers accept `--helper <canonical-helper-path>` for verifying the
adopted helper. Run the developer checker after helper adoption but before
actual index conversion: it explicitly asserts a strict size improvement and
therefore cannot pass against an already canonical V4 index. The independent
review checker can run before or after index conversion; after conversion its
old/index byte fields describe the current V4 index and savings become zero.
Neither reconstructs the pre-adoption snapshot. Root must retain that snapshot
for its before/after comparison. This test-order constraint is a NOTE, not a
candidate correctness finding. No permission flow, evidence deletion/splitting, truncation,
archival change, or scientific conclusion follows from this review.
