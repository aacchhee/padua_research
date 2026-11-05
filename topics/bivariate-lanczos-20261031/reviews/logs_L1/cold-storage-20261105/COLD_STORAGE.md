# Cold-storage manifest — topics/bivariate-lanczos-20261031/reviews/logs_L1

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
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/exact_checks.log` | 4550 | `423db0578c680f2ba3711a5d619d5ff19b9d095de86ba086f027d985c31b62aa` | `3c9d388946355653358bc67ab12e0a5c7d5c4e87` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/extra.log` | 2796 | `a00d8d75a3e43646ed35c27bed098e6d9b1a65e5f8fbe50b56e43aa05db53da7` | `9a2a89ffcec54db4ceeb957e2a15c612178faae9` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/prop.log` | 5160 | `d5d62cc568adee9985dd3bfebff15e3858aa5c6027641f8816634d3a650f1ec3` | `456748dff83b2f2a9877cf39ea71b81eb11c454e` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/prop_selection.log` | 1859 | `9284b565525381debc0df0ff9d4ea636f1407acf335afbfad0986b58c6122422` | `7f645724129c7a33325b62a105e9727d1dd0d9d2` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/rule_sensitivity.log` | 7962 | `a1b0ef4fa0cc855b67998d876a5e81ee39c6e22d619746f4465ce7266bdf3387` | `4af66e36df4e35ca8b69c565278417948339749f` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/sweep_M.log` | 1162 | `c68519703a6f3f25d926eecb313db4dc298b2a023a2d95701fcdf60ad8f68ab7` | `cda54d57be06a99692f74a63478c089d834172bb` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/sweep_alt.log` | 5170 | `48a7c2e7f45aab70925848179ad1c5ac853da791201475af4b2f16b978b6e0e9` | `1136281e5df3baf476af47dd996983dfbe039618` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/sweep_ritz.log` | 5585 | `3e31eda473bfed5b526baa4c3f2cf5e67162710c0432ce9344ddae91d4f86ef6` | `5bca409729836762dd4768e5e905bc282800807a` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/directions/L1/R01.md](../../../directions/L1/R01.md)
- [topics/bivariate-lanczos-20261031/directions/L1/candidates.md](../../../directions/L1/candidates.md)
- [topics/bivariate-lanczos-20261031/directions/L1/response-audit-01.md](../../../directions/L1/response-audit-01.md)
- [topics/bivariate-lanczos-20261031/directions/L1/response-recon-01.md](../../../directions/L1/response-recon-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-prior-art-01.md](../../L1-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md](../../L1-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-02.md](../../L1-reconstruction-02.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/reviews/L1-prior-art-01.md](../../L1-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md](../../L1-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-02.md](../../L1-reconstruction-02.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/reviews/logs_L1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_reviews_logs_L1_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/reviews/logs_L1/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/reviews/logs_L1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/reviews/logs_L1/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/exact_checks.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C075 | C075 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/extra.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C076 | C076 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/prop.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C077 | C077 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/prop_selection.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C078 | C078 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/rule_sensitivity.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C079 | C079 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/sweep_M.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C080 | C080 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/sweep_alt.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C081 | C081 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L1/sweep_ritz.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C082 | C082 |

### C075

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:379`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
python3 -I -u rv_exact_checks.py > L/exact_checks.log
````

### C076

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:385`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
python3 -I -u rv_extra.py > L/extra.log
````

### C077

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:384`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 python3 -I -u rv_prop.py > L/prop.log
````

### C078

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:387`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=2 python3 -I -u rv_prop_selection.py > L/prop_selection.log
````

### C079

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:386`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
python3 -I rv_rule_sensitivity.py <developer logs>/r01_{input3,rotation,swap,padua,irregular}.raw > L/rule_sensitivity.log
````

### C080

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:382`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
python3 -I -u rv_sweep.py M > L/sweep_M.log
````

### C081

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:381`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
python3 -I -u rv_sweep.py alt > L/sweep_alt.log
````

### C082

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:383`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
python3 -I -u rv_sweep.py ritz > L/sweep_ritz.log
````
