# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-02/L1

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
| `topics/bivariate-lanczos-20261031/audit-02/L1/developer-exact-rerun.log` | 6445 | `f4ff98a922b620c10786ee6af7071c635472ea7ce7e48c0e410f6fcb091c1377` | `8c369f43a2d8e407fc0fabf57d8e1e06513257c3` |
| `topics/bivariate-lanczos-20261031/audit-02/L1/developer-n101-reanalysis-rerun.log` | 13436 | `3b29cf2fcb1f1aec768e8fa0c7b9edc770afba717f98353ba88f6febc8bc312c` | `fe22a2ce2ffa26fd8c4c4b0481cf3ce4cbc5113c` |
| `topics/bivariate-lanczos-20261031/audit-02/L1/independent-response-checks.log` | 1721 | `ccb610f0b348a704f6c5d1370c5ae99c8f531a44243ad586239feb7606178844` | `2e009bb9adcc68668acf04f6950b1d2d79408cf7` |
| `topics/bivariate-lanczos-20261031/audit-02/L1/provenance.log` | 1214 | `9dbf09c1e371fd5d842af98ab7332618e55b0a456e2cc833967a83d5d92863cd` | `20d7040ebdc2f22e348859b14874a503414e0691` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/COLD_STORAGE.md](../../../COLD_STORAGE.md)
- [topics/bivariate-lanczos-20261031/audit-02/L1.md](../../L1.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-02/L1.md](../../L1.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-02/L1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-02_L1_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-02/L1/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-02/L1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-02/L1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
```

The archive is staged at the actual export directory above. Final migration
results/receipt hashes are in the [migration verification](../../../../padua-lebesgue-followups-20261103/preparation/cold-storage-migration.md).
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
| `topics/bivariate-lanczos-20261031/audit-02/L1/developer-exact-rerun.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C004 | C004 |
| `topics/bivariate-lanczos-20261031/audit-02/L1/developer-n101-reanalysis-rerun.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C021 | C021 |
| `topics/bivariate-lanczos-20261031/audit-02/L1/independent-response-checks.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C022 | C022 |
| `topics/bivariate-lanczos-20261031/audit-02/L1/provenance.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C023, C024 | C023, C024 |

### C004

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L1.md:73`,
Git blob `efc1b20b29d96251b0428ecc8cd794f4be7a978b` at retrieval source40347d1.

````text
python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py > topics/bivariate-lanczos-20261031/audit-02/L1/developer-exact-rerun.log
````

### C021

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L1.md:74`,
Git blob `efc1b20b29d96251b0428ecc8cd794f4be7a978b` at retrieval source40347d1.

````text
python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_n101_reanalysis.py topics/bivariate-lanczos-20261031/directions/L1/logs > topics/bivariate-lanczos-20261031/audit-02/L1/developer-n101-reanalysis-rerun.log
````

### C022

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L1.md:75`,
Git blob `efc1b20b29d96251b0428ecc8cd794f4be7a978b` at retrieval source40347d1.

````text
python3 -I topics/bivariate-lanczos-20261031/audit-02/L1/independent_response_checks.py > topics/bivariate-lanczos-20261031/audit-02/L1/independent-response-checks.log
````

### C023

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:52`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-02/L1/manifest.json` | Git blob `6c851ab37a55` at `2b52b432fe59`; AC cold storage PENDING | 72,327 | `e41b5e65f0727b9f4c4fbe2c0b7b9fe7a29ea7450e508118e0f486473c2d06c8` | `2b52b432fe59` | python3 -I topics/bivariate-lanczos-20261031/audit-02/L1/make_manifest.py > audit-02/L1/provenance.log | committed at source commit | Summary: audit-02/L1.md:68-76; audit-02/L1/provenance.log.  |
````

### C024

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L1.md:76`,
Git blob `efc1b20b29d96251b0428ecc8cd794f4be7a978b` at retrieval source40347d1.

````text
python3 -I topics/bivariate-lanczos-20261031/audit-02/L1/make_manifest.py > topics/bivariate-lanczos-20261031/audit-02/L1/provenance.log
````
