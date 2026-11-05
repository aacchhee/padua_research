# Cold-storage manifest — topics/bivariate-lanczos-20261031/reviews/logs_L2

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
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/adapt_C.log` | 872 | `4c61f915291f1bb5ff29bf255629def53e2cc0c398dbd641fee62fada2f083a3` | `1eb2f8b8b1d72b4706179d643993179d1442bd0a` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/cycles.log` | 1314 | `72d3aa36b45910b850c907d7872f6bce20a0a330df3519c923dfb50607c2c588` | `cb3c2750a46fa104ab25f52b9329dfcdef215bbb` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/dev_r01_omega_rerun.raw` | 12460 | `0fa16b87eedacad624ac2dedd470bd0b9925fee836d84dba776f0c64934a2b31` | `fb9f2ed99be2752fec7f0123a763c881ebaacfae` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/dev_r02_proJ_rerun.raw` | 9620 | `d85db4841bb6bfb8c529a272bb3e042e0ec0c2e2b89b6a727496a15034c410d9` | `52ad71493bfe9ba5b0f3e7ccb573831bcc59e590` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/dev_r02_pro_rerun.raw` | 5801 | `61f15ce43eae537d08f6caf9cc588b74c701cc19cac9f75397662495de55519d` | `11b6ead2a24a27d31af3a0604d563163c0ebcc6a` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/dev_r03_dots_rerun.raw` | 14441 | `d5e4e5bcdd4bd4cb5178fd218be7737405138427187f05b9b9b61d3232a59ae1` | `703bf4d36f4020c82b34e6e2c94ab819a275cd1e` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/drift_C.log` | 3547 | `13905c7c72a7faceeca89abe3e8c0845d0338ecedbd49a591877fea175e42f60` | `567822276e4ff4ac0ef9e4bd1f4755d94af12120` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/drift_D.log` | 845 | `53b1d3e1e52054c1d13cf26193bf587911d0955199d8ed85fdfc940aa2f0979c` | `7918e6279f9369b778364420e2a53f0cec2e67a8` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/exact.log` | 3540 | `eeb9f64b4539fda7de8d7f819464a365650eb4ca02f3861a254869951142149d` | `6309890186e325e25337325b865ca4ec925487e8` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/omega.log` | 13178 | `b79452c3bd5eae3d193512543a4769d90dab996d6528affe08e092131dd37766` | `e4a2bef5b27fd815c16ee642337725e417d90928` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/sections.log` | 1106 | `09327de47edfef48f8cd7907a99501f6e9f44ef77c554445f25b01d55e3bee77` | `59fc6462da8ffe623722bdc9eb2a620273d5d469` |

## Retrieval, generation records and checks

Exact frozen byte-reconstruction command for each row:
`git cat-file blob <Git-blob> > <external-destination>/<repository-path>`.
Fetch the source commit if needed. This reproduces historical bytes, including
timing/diagnostic fields, without claiming a fresh mathematical run.
Original generating/checker commands and their execution scope remain in the
retained records below; they are not uniformly reconstructed by this migration.
Where historical command details are absent, retrieval is the supported route.

Retained provenance records:
- [topics/bivariate-lanczos-20261031/audit-01/L1-foundations.md](../../../audit-01/L1-foundations.md)
- [topics/bivariate-lanczos-20261031/audit-01/L3-certificates.md](../../../audit-01/L3-certificates.md)
- [topics/bivariate-lanczos-20261031/directions/L1/response-audit-01.md](../../../directions/L1/response-audit-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L2-prior-art-01.md](../../L2-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md](../../L2-reconstruction-01.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/reviews/L2-prior-art-01.md](../../L2-prior-art-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md](../../L2-reconstruction-01.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/reviews/logs_L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_reviews_logs_L2_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/reviews/logs_L2/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/reviews/logs_L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/reviews/logs_L2/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/adapt_C.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C083 | C083 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/cycles.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C084 | C084 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/dev_r01_omega_rerun.raw` | Recorded output invocation; preserve original cwd/env/placeholders. | C085 | C085 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/dev_r02_proJ_rerun.raw` | Recorded output invocation; preserve original cwd/env/placeholders. | C086 | C086 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/dev_r02_pro_rerun.raw` | Recorded output invocation; preserve original cwd/env/placeholders. | C087 | C087 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/dev_r03_dots_rerun.raw` | Recorded output invocation; preserve original cwd/env/placeholders. | C088 | C088 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/drift_C.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C089 | C089 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/drift_D.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C090 | C090 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/exact.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C002, C091 | C002, C091 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/omega.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C092 | C092 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L2/sections.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C093 | C093 |

### C002

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L1-foundations.md:76`,
Git blob `394d35d2f63008adba3a18e4ab07fbdd23f1c7ff` at retrieval source40347d1.

````text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I topics/bivariate-lanczos-20261031/audit-01/L1-foundations/check_foundations.py > topics/bivariate-lanczos-20261031/audit-01/L1-foundations/independent_exact.log 2>&1
````

### C083

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:380`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I rl2_adapt_C.py     > logs_L2/adapt_C.log     # adapt selections vs (C)
````

### C084

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:379`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I rl2_cycles.py      > logs_L2/cycles.log      # 205 well-definedness vs condition (C)
````

### C085

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:384`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I l2_r01_omega.py rotpi4 triangle              > logs_L2/dev_r01_omega_rerun.raw
````

### C086

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:385`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I l2_r02_pro.py --jmeasure rotpi4 triangle cb_cubic > logs_L2/dev_r02_proJ_rerun.raw
````

### C087

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:386`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I l2_r02_pro.py rotpi4 triangle                > logs_L2/dev_r02_pro_rerun.raw
````

### C088

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:387`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I l2_r03_dots.py cb_cubic rotpi4               > logs_L2/dev_r03_dots_rerun.raw
````

### C089

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:375`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
OMP_NUM_THREADS=1 python3 -I rl2_drift.py C > logs_L2/drift_C.log    # M = 1681, 1e4, 1e5 (≈ 3 min)
````

### C090

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:376`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I rl2_drift_D.py     > logs_L2/drift_D.log     # L-shape, annulus, LD reference (≈ 1.5 min)
````

### C091

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:378`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I rl2_exact.py       > logs_L2/exact.log       # 202 / 205 exact checks + structural search
````

### C092

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:381`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
OMP_NUM_THREADS=1 python3 -I rl2_omega.py > logs_L2/omega.log        # own E1/E1D and PRO-2D-J
````

### C093

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L2-reconstruction-01.md:382`,
Git blob `51d0205bb75dcdbe808b9b26ac5847665a16316e` at retrieval source40347d1.

````text
python3 -I rl2_sections.py    > logs_L2/sections.log    # e_H, e_tau, e_F in LD; tensor control
````
