# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-02/L5

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
| `topics/bivariate-lanczos-20261031/audit-02/L5/analysis_r01d_rerun.txt` | 7992 | `d295f49b523ea0d81f8cee017186ce7e615d66bbf38fa917bce1aa1a36ff8604` | `ab7e04e1e6d5030dd4845149989f1d865f64945f` |
| `topics/bivariate-lanczos-20261031/audit-02/L5/check_response.log` | 848 | `af08dcae208424fde9a8df28c75bf0d0e2fb40a3a52d87f3969aa72a62114202` | `4397a43f22efee9d41499fa58d79c23dff6dda2d` |

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
- [topics/bivariate-lanczos-20261031/audit-02/L5.md](../../L5.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-02/L5.md](../../L5.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-02/L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-02_L5_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-02/L5/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-02/L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-02/L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-02/L5/analysis_r01d_rerun.txt` | Recorded output invocation; preserve original cwd/env/placeholders. | C027 | C027 |
| `topics/bivariate-lanczos-20261031/audit-02/L5/check_response.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C028, C029 | C028, C029 |

### C027

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L5.md:101`,
Git blob `b35b7bb5ac8735a3c43797d4f1be025f7e6285da` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 python3 -B -I tracks/bivariate-lanczos/code/L5/analyze_r01d.py topics/bivariate-lanczos-20261031/directions/L5/logs > topics/bivariate-lanczos-20261031/audit-02/L5/analysis_r01d_rerun.txt
````

### C028

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:58`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-02/L5/input_manifest.json` | Git blob `68fc8fbf6b42` at `2b52b432fe59`; AC cold storage PENDING | 22,156 | `271a57ce030291298b1d71183a8c82dfdf772d078af3ed9c37c4e1fa4d02ebe2` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 python3 -B -I topics/bivariate-lanczos-20261031/audit-02/L5/check_response.py > audit-02/L5/check_response.log | committed at source commit | Summary: audit-02/L5.md:19,108; audit-02/L5/SHA256SUMS; check_response.log.  |
````

### C029

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L5.md:103`,
Git blob `b35b7bb5ac8735a3c43797d4f1be025f7e6285da` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 python3 -B -I topics/bivariate-lanczos-20261031/audit-02/L5/check_response.py > topics/bivariate-lanczos-20261031/audit-02/L5/check_response.log
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-02/L5.md:108`,
blob `b35b7bb5ac8735a3c43797d4f1be025f7e6285da`:

````text
Artifacts: [checker](L5/check_response.py), [checker log](L5/check_response.log), [full paired/checkpoint results](../COLD_STORAGE.md), [driver rerun](L5/analysis_r01d_rerun.txt), [input identities](../COLD_STORAGE.md), [artifact checksums](L5/SHA256SUMS). No experimental data beyond the unchanged log families were independently regenerated in this focused round. The full Padua slope runs, all 54 prefix scans, n=60 sequence and exact/interval certification remain outside this execution scope, as already disclosed in audit-01 and the response.
````
