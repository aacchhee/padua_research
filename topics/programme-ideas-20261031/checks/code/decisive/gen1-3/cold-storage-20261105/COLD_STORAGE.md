# Cold-storage manifest — topics/programme-ideas-20261031/checks/code/decisive/gen1-3

2026-11-05. AC instructed: “generated outputs should go to cold storage.”
Raw transcripts/generated analysis captures are archived without changing their bytes.
Small essential receipts, scientific summaries, mathematics and all code remain tracked.

Exact retrieval source: pushed `40347d11071c81c1c633a2578cb52325bb92584a`. [Machine manifest](cold-storage.json)
records every path, SHA-256, size and Git blob. The source is a retrieval snapshot,
not a relabelling of historical execution provenance. No artifact was split; this
manifest belongs to an existing logical experiment/audit component.

## Artifact identities

| Repository path | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/T1b.out` | 4786 | `8c77635738262d8946727d46e781223815ceb9f9c8c10cac02937e66528b7da3` | `c11fafce3acd87aa014023e8606c2fb3fe0c3a69` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/T2.out` | 15041 | `a60324a7d4f684bb777b2e37e9130986b2a0a9c63b58f2c268b7c33b56e555fe` | `3205061d27ab2eb9cd2f4a07a3100c7447395275` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/T2c.out` | 7312 | `67bf0363656ed7af8b6be82bbecc85b1e7c6c4994ef2430bca11792df8df9a78` | `a5c9082f1ffe364c4da653b540fc8e9d966e7e66` |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/window_exact.out` | 15138 | `8354313abf496f9d62550daade12d5b148ff653b20ad1266c4e48d62cbc6a1e4` | `e7b47cc6875fe7b018bc7131dde5eb0010305e2d` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/programme-ideas-20261031/checks/decisive-gen1-3.md](../../../../decisive-gen1-3.md)
- [topics/programme-ideas-20261031/theory/programme-ideas-claude-N02-windowed-rational-lanczos-instability.md](../../../../../theory/programme-ideas-claude-N02-windowed-rational-lanczos-instability.md)

Short scientific summaries:
- [topics/programme-ideas-20261031/checks/decisive-gen1-3.md](../../../../decisive-gen1-3.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/programme-ideas-20261031/checks/code/decisive/gen1-3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_programme-ideas-20261031_checks_code_decisive_gen1-3_cold-storage-20261105 --manifest topics/programme-ideas-20261031/checks/code/decisive/gen1-3/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/programme-ideas-20261031/checks/code/decisive/gen1-3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/programme-ideas-20261031/checks/code/decisive/gen1-3/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
```

The archive is staged at the actual export directory above. Final migration
results/receipt hashes are in the [migration verification](../../../../../../padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md).
Source and destination SHA/size verification is required before removing tracked
copies. The receipt describes export-time readback; re-run verify-archive when
relying on the archive later. No Git history is rewritten.

## Retention and physical delivery

Physical delivery to AC’s `Downloads/padua/cold_storage` is **PENDING**;
that destination is not mounted/accessible in this session. The local stage has
no promised retention period and is not a substitute claim of delivery.
Pinned source blobs remain reachable through the pushed branch history; they
provide cloud retrieval if staging is lost. Keep staging while available.
No purge or deletion of historical Git objects is authorized.

## Frozen command records

These are verbatim historical records, not new executions. Direct named-output
invocations are distinguished from partial argv, checker/input mentions and
script/output mappings. Preserve the original record’s working directory,
environment, source revision and placeholders; do not treat an abbreviated
line as a newly reconstructed runnable command. For missing capture details,
exact-byte retrieval from the pinned blob is the supported archival route.

| Artifact | Status | Command record IDs | Direct output IDs |
|---|---|---|---|
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/T1b.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/T2.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/T2c.out` | Partial argv/generator/input/script mapping only; exact output command not recovered. | none recovered | none recovered |
| `topics/programme-ideas-20261031/checks/code/decisive/gen1-3/window_exact.out` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/checks/decisive-gen1-3.md:35`,
blob `363e03e2c7a9af8cce4d9c23c558a79cfb699eef`:

````text
All numbers MEASURED within the stated scopes; scripts and outputs under `checks/code/decisive/gen1-3/` (`orf2d.py` library; `window_exact.py/.out`; `run_T1_T3.py` → `T1_T3.out`, 351 s; `run_T1b.py` → `T1b.out`, 368 s; `run_T2.py` → `T2.out`, 142 s; `run_T2c.py` → `T2c.out`, 72 s). Total wall time ≈ 16 min, dominated by eight 80-bit reference runs of ≈ 50 s each; every double-precision method runs in ≈ 1 s at M = 4096, N = 325 (L3c 1.0 s, LF 1.4–1.6 s, R1 0.11 s, R2 0.13 s, R3 0.26–0.50 s: no runtime difference worth reporting at this size).
````

Documented mapping only (not exact invocation): `topics/programme-ideas-20261031/theory/programme-ideas-claude-N02-windowed-rational-lanczos-instability.md:49`,
blob `fcfde6bd3e62252f6343022132fb52924f093364`:

````text
`checks/code/decisive/gen1-3/` (frozen at `614709d`): `window_exact.py/.out`, `run_T1_T3.py`/`T1_T3.out`, `run_T1b.py`/`T1b.out`, `orf2d.py`. Pre-registration at `a8364b9332e651c4e64115667b0411d38234fcd0`. Audit replay as in the table.
````
