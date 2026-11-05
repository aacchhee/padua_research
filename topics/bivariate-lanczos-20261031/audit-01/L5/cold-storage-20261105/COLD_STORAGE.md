# Cold-storage manifest — topics/bivariate-lanczos-20261031/audit-01/L5

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
| `topics/bivariate-lanczos-20261031/audit-01/L5/diagnostics.jsonl` | 4843 | `bf4923d64e41d32b5cb10a5222d50d342e3655ed480a1e1d474276db3b196d1f` | `c30637eb0a61faec64b67d5395102b64825bd919` |
| `topics/bivariate-lanczos-20261031/audit-01/L5/dual.jsonl` | 5860 | `7beac82e5a37e7d8d9f00814b3cb0af38a6b3073510a10ce36c3a750f7288776` | `cfa38813e8af50d8ca7d9eff80728cf5e6efc663` |
| `topics/bivariate-lanczos-20261031/audit-01/L5/kill-rerun.jsonl` | 1956 | `5457b948e2ed1dcc4e6ab43f3b1b9113b8145f689d1ed4910d4a05dc5a78110b` | `654eb02d3520cc43cd17371af644fc2db1a40293` |
| `topics/bivariate-lanczos-20261031/audit-01/L5/random-fit.jsonl` | 2145 | `a94650083d2fca2d878000892f63e7c2e53f434235efc8163991bd053ad4a56f` | `4896cbb69902fc409d3d488a9836fa20ec0afe98` |
| `topics/bivariate-lanczos-20261031/audit-01/L5/random-rerun.log` | 3785 | `d3f899ece79cfa595b600625c460e2a1a5f44e2c1714d9028d2067c34d35e4d3` | `9981cc2e89ef39de731316ba03dc9b6ee04af854` |
| `topics/bivariate-lanczos-20261031/audit-01/L5/rules-rerun.jsonl` | 4980 | `5078ac7808b054a23461d2ad085a5c06f5a813f2de8fa1896cf5208df32c56cd` | `90e3ef5eaf791adf4f637d3989f527d690e57715` |
| `topics/bivariate-lanczos-20261031/audit-01/L5/slopes-reanalysis.txt` | 12452 | `aea83efe51cca3d5b2213f4e8e57edd283304a8a18ebe9ae13050c0254242e98` | `b6398939cd939a84eedb4e729cc74583567acbfe` |
| `topics/bivariate-lanczos-20261031/audit-01/L5/small-rerun.log` | 2663 | `d00344ad3c0e35ee3c00e981150872eab0c5ced9c6b905368dee2a3bbd3510ba` | `8924815d6777c2f056b10224b37e443adb2deda7` |

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
- [topics/bivariate-lanczos-20261031/audit-01/L5.md](../../L5.md)
- [topics/bivariate-lanczos-20261031/directions/L5/R02.md](../../../directions/L5/R02.md)
- [topics/bivariate-lanczos-20261031/directions/L5/response-audit-01.md](../../../directions/L5/response-audit-01.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/audit-01/L5.md](../../L5.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/audit-01/L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_audit-01_L5_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/audit-01/L5/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/audit-01/L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/audit-01/L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/audit-01/L5/diagnostics.jsonl` | Recorded output invocation; preserve original cwd/env/placeholders. | C012 | C012 |
| `topics/bivariate-lanczos-20261031/audit-01/L5/dual.jsonl` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C013 | none recovered |
| `topics/bivariate-lanczos-20261031/audit-01/L5/kill-rerun.jsonl` | Recorded output invocation; preserve original cwd/env/placeholders. | C014 | C014 |
| `topics/bivariate-lanczos-20261031/audit-01/L5/random-fit.jsonl` | Recorded output invocation; preserve original cwd/env/placeholders. | C015, C016 | C016 |
| `topics/bivariate-lanczos-20261031/audit-01/L5/random-rerun.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C017 | C017 |
| `topics/bivariate-lanczos-20261031/audit-01/L5/rules-rerun.jsonl` | Recorded output invocation; preserve original cwd/env/placeholders. | C018 | C018 |
| `topics/bivariate-lanczos-20261031/audit-01/L5/slopes-reanalysis.txt` | Recorded output invocation; preserve original cwd/env/placeholders. | C019 | C019 |
| `topics/bivariate-lanczos-20261031/audit-01/L5/small-rerun.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C020 | C020 |

### C012

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L5.md:88`,
Git blob `4d68a52c51ae232e8acacf8b248bf36e887d76a0` at retrieval source40347d1.

````text
python3 -I $A/check_l5.py diagnostics > $A/diagnostics.jsonl
````

### C013

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/directions/L5/R02.md:40`,
Git blob `ee628559e4e257aca8c9749cde41cee42853fcd1` at retrieval source40347d1.

````text
python3 -I exp_r02_dual.py logs/r02_dual.jsonl padua_cub 15 20 30 40
````

### C014

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L5.md:87`,
Git blob `4d68a52c51ae232e8acacf8b248bf36e887d76a0` at retrieval source40347d1.

````text
python3 -I $A/check_l5.py kill > $A/kill-rerun.jsonl
````

### C015

Status: documented_command_with_placeholders. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:49`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `audit-01/L5/random-rerun.jsonl` | Git blob `2a915f1f8df9` at `2b52b432fe59`; AC cold storage PENDING | 18,424 | `49339cc43d1ab9b08ddc1cf9b9f695431d2c2e45ed5ba3ffb2664eed09b50e69` | `2b52b432fe59` | OPENBLAS_NUM_THREADS=1 python3 -I topics/bivariate-lanczos-20261031/audit-01/L5/check_l5.py setup; then OPENBLAS_NUM_THREADS=1 python3 -I <setup>/L5/exp_r01.py random <out> 66 136 231 496 861 1326 2016 | committed at source commit | Summary: audit-01/L5.md:89,99; audit-01/L5/random-fit.jsonl. Seeds 7000*k+M. |
````

### C016

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L5.md:90`,
Git blob `4d68a52c51ae232e8acacf8b248bf36e887d76a0` at retrieval source40347d1.

````text
python3 -I $A/check_l5.py fresh_analysis > $A/random-fit.jsonl
````

### C017

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L5.md:89`,
Git blob `4d68a52c51ae232e8acacf8b248bf36e887d76a0` at retrieval source40347d1.

````text
python3 -I /tmp/padua-l5-audit-3a9063b/L5/exp_r01.py random /workspace/padua_research/$A/random-rerun.jsonl 66 136 231 496 861 1326 2016 > $A/random-rerun.log
````

### C018

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L5.md:86`,
Git blob `4d68a52c51ae232e8acacf8b248bf36e887d76a0` at retrieval source40347d1.

````text
python3 -I $A/check_l5.py rules > $A/rules-rerun.jsonl
````

### C019

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L5.md:84`,
Git blob `4d68a52c51ae232e8acacf8b248bf36e887d76a0` at retrieval source40347d1.

````text
python3 -I $A/check_l5.py analysis > $A/slopes-reanalysis.txt
````

### C020

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L5.md:85`,
Git blob `4d68a52c51ae232e8acacf8b248bf36e887d76a0` at retrieval source40347d1.

````text
python3 -I $A/check_l5.py small > $A/small-rerun.log
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L5.md:33`,
blob `4d68a52c51ae232e8acacf8b248bf36e887d76a0`:

````text
With the same size weights, the slope difference is unchanged by this normalization. Positive separate ratio slopes are not a confidence interval for their difference. Independent reanalysis of the committed uniform-family data, using the record's own per-size means and t interval (seven sizes, df = 5), gives the paired Givens/HL slope **0.5953256, 95% interval [-0.1106994, 1.3013506]**. The corresponding Givens/CGS2 difference is **1.3020027 [0.6202911, 1.9837143]**. These calculations are in `L5/diagnostics.jsonl` and the `diagnostics` mode of `check_l5.py`.
````
