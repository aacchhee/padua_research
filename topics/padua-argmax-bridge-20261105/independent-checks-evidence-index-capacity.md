# Independent index-capacity review

Input HEAD: `1ebf813c73bb51025c10db5a0e6b8a5745832c6d`.
Rules AGENTS/WORKFLOW/CODEX are unchanged from the prior review at
`0768cb93c4f829faf5f38d47cdd7e33faad8bf64` (verified by Git diff).
Reviewer: distinct Codex technical reviewer; requested Astra medium, API
accepted, serving model metadata unexposed. This is utility/metadata maintenance,
not a research round or novel mathematics; the full IDEA gate does not apply.

Read the LOG's explicit ONE consolidated-index exception: strict 32KiB index
limit, unchanged strict 16KiB evidence limit and aggregate 10MB policy. Read
`capacity-change.md`, the full developer checker, and the candidate/canonical
diff. Only three conceptual changes are present: new INDEX_LIMIT and two CLI
index guards/messages. No schema, hash, file verifier, conversion or replacement
logic changes. No actual helper/index or Git mutations are authorized here.

Preregistered before execution: one independent standard-library Python run,
process hard CPU limit 2 seconds, single process, no scientific/native imports.
Verify exact three-change bytes and candidate/checker identities; independently
decode and rehash the actual 194 rows; compare APIs and nonencoding metadata;
temporary CLI main checks at index sizes 16385,32767,32768; both compaction
output bounds; declared/physical 16384-byte evidence rejection and 16383-byte
acceptance. Assert actual helper/index unchanged. This reviewer owns this report
and `code/evidence_index_capacity_review.py` only.

## Results and verdict

ACCEPT: no BLOCKING, MAJOR or MINOR findings in this capacity-only patch.
The independent run completed PASS, exit 0, in 0.082336 process CPU seconds.
Command from repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 topics/padua-argmax-bridge-20261105/code/evidence_index_capacity_review.py
```

All 194 actual files were independently decoded/rehashed. The actual index was
16086 bytes, SHA256
`8b0268fa380ece7eef8f448d38469a247c4d4df7b8245556672edc90656c604c`.
The candidate and canonical APIs produced identical decoded rows, V3/V4
conversions and nonencoding metadata. Exact byte reconstruction verifies that
every source byte outside the three intended changes is unchanged, including
all V2/V3/V4 schemas, full 32-byte SHA handling and evidence guards.

Seven isolated calls to the actual CLI main parser/action path passed:
16385- and 32767-byte indexes accepted; 32768 rejected; each compaction action
accepted exactly 32767-byte output and rejected exactly 32768-byte output while
preserving the original. Both declared-size and physical-file guards rejected
16384-byte evidence and accepted 16383 bytes. Canonical helper and actual index
were unchanged after execution. The tests make no aggregate-size-policy
implementation claim: the existing aggregate 10MB policy remains a separate
repository obligation.

Identities (SHA256):

- Candidate, 10944 bytes: `d9d4590d59f44cbfc1627a4a0cab0b6bda398f327c0e755eb0c19c48aa063e2f`.
- Developer checker, 6614 bytes: `30a80befd96e47275436f1be78425e8efe1177e96429713d53505348ed6fdbcd`.
- Independent checker: `f8ac864fe16e645b456e956cb19e3fd7a7245e6658bede325157ecb61245f791`.

Developer chronology is preserved in `capacity-change.md`: the earlier suite
stopped on its fixture-padding assertion before testing the intended compaction
behavior, then switched to schema-specific padding targeting 22000 bytes. The
record reports the earlier 0.2986-second wall time separately from the successful
0.6411 CPU-second suite. This is a metadata test-fixture correction, not a
scientific retry. I inspected that corrected checker and its recorded chronology;
I did not rerun it or independently verify its historical timing. My independent
boundary fixtures passed on their first run, without sharing its padding target.

This review does not repeat the prior V4 algorithm audit or claim general
concurrency/crash durability. Exact unchanged source establishes that those
prior limitations remain. Root owns adoption: copy the pinned candidate bytes
to the canonical helper, confirm byte identity and diff, and preserve all actual
manifest rows and metadata. The cap change itself requires no index rewrite,
evidence removal, split, archive operation, schema change or hash shortening.
The independent checker is intentionally a pre-adoption exact-diff test; after
adoption, use the developer checker with its supported canonical `--helper`
argument and verify the adopted SHA. No new approval flow is required.
