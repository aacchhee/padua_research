# Cold-storage manifest — topics/bivariate-lanczos-20261031/reviews/logs_L5

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
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/analysis_review.txt` | 13420 | `3f2eb534049f6dab27b8e96d572529df890aefc1c37ca69c791580ca44addd90` | `d4ace38d91d56ce78e1e26970ca43823c367f122` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/b_kill.jsonl` | 7607 | `8ce3f38506bf858997a9fc1822b3c5780ced59b6580d807ea6d8967736d50a4a` | `32ebd3ccb21427e654a77e27a4ac3bcdb4adf555` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/b_kill.log` | 6200 | `efb51392f76063acb0f07da88edadf835dfa91362b163b8a521496e1f5500fec` | `a41890b9db4e54a070ed4447286256396b41d487` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/c_repro60.jsonl` | 1136 | `159ceb5d12b38020aa58fcf13f596a28e7fcae7e80e96e5ea8f26dce146b065e` | `1fbea833f41774b6e145b1265c770a9e6504cb6a` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/c_repro60.log` | 1090 | `4e65d69a6e91230e564860efcc646154a010bdb0cc6a4b65d39153195f321595` | `de12ed44dcfb11d9216a101362ad62e49eb24cdd` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/checks.log` | 2658 | `bc9ad826a779baae9f81827be46b667800a2883513eee75155dc3f313a119730` | `a0173b233da9ad69f20bc1045dc62e830a4c7bb3` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/d_unif.jsonl` | 4622 | `7a2573155a0c634f1f43a45c01558c6e9637a6c674aaea5db6fa44edfc2013ed` | `ec82f0f0c9ab32ebcfdcb04dcaadec1f56455a25` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/d_unif.log` | 4153 | `a968ec6aa6d73ca08f8bcb581ea61a3370526d2cb08bd15e97bed49cafd271eb` | `fd58d38da163b3ebdca497355e41617f888b04d3` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/reanalysis_dev_r01.txt` | 10593 | `498870118ac14fdbb0f0b8a61787475ac9dc344193162d966aa7dd46d69e849c` | `c03c2bc918a8df1abbd2861ef8ec3757932fab72` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/stage_check.log` | 76 | `cc176cc487a34cb83727e9863411a64ebca8a49e1e414a0b719de97d042f13e9` | `4a41a784db1028ca6470ebe60715b433c462022d` |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/unif_slopes.txt` | 247 | `b9ed68fa6a6b561871e36a0851704c974da2eb9f47ca25e359a9f0d49e6c124c` | `33cc6645864d9b2327572d98fc9169baca687649` |

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
- [topics/bivariate-lanczos-20261031/audit-01/L1-later.md](../../../audit-01/L1-later.md)
- [topics/bivariate-lanczos-20261031/audit-01/L3-framework.md](../../../audit-01/L3-framework.md)
- [topics/bivariate-lanczos-20261031/audit-02/L1.md](../../../audit-02/L1.md)
- [topics/bivariate-lanczos-20261031/audit-02/L2.md](../../../audit-02/L2.md)
- [topics/bivariate-lanczos-20261031/directions/L1/response-audit-01.md](../../../directions/L1/response-audit-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md](../../L1-reconstruction-01.md)
- [topics/bivariate-lanczos-20261031/reviews/L5-reconstruction-01.md](../../L5-reconstruction-01.md)

Short scientific summaries:
- [topics/bivariate-lanczos-20261031/reviews/L5-reconstruction-01.md](../../L5-reconstruction-01.md)

## Export and restoration

From repository root:

```sh
python tools/cold_storage.py export topics/bivariate-lanczos-20261031/reviews/logs_L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-storage-20261105-v2
python tools/cold_storage.py verify-archive /workspace/scratch/padua-cold-storage-20261105-v2/topics_bivariate-lanczos-20261031_reviews_logs_L5_cold-storage-20261105 --manifest topics/bivariate-lanczos-20261031/reviews/logs_L5/cold-storage-20261105/cold-storage.json
python tools/cold_storage.py restore topics/bivariate-lanczos-20261031/reviews/logs_L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
python tools/cold_storage.py verify topics/bivariate-lanczos-20261031/reviews/logs_L5/cold-storage-20261105 --dest /workspace/scratch/padua-cold-restore-20261105
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
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/analysis_review.txt` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C094 | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/b_kill.jsonl` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C095, A05 | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/b_kill.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | A06 | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/c_repro60.jsonl` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C096, A07 | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/c_repro60.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | A08 | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/checks.log` | Recorded output invocation; preserve original cwd/env/placeholders. | C009, C022, C075 | C009, C022, C075 |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/d_unif.jsonl` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C097, A09 | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/d_unif.log` | Partial argv/generator/input/script mapping only; exact output command not recovered. | A10 | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/reanalysis_dev_r01.txt` | Partial argv/generator/input/script mapping only; exact output command not recovered. | C094 | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/stage_check.log` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |
| `topics/bivariate-lanczos-20261031/reviews/logs_L5/unif_slopes.txt` | Original command not recovered; exact-byte retrieval only. | none recovered | none recovered |

### A05

Status: original argv recorded in output metadata; interpreter invocation/flags not recovered from argv alone. Source `topics/bivariate-lanczos-20261031/reviews/logs_L5/b_kill.jsonl:1`,
Git blob `32ebd3ccb21427e654a77e27a4ac3bcdb4adf555` at retrieval source40347d1.

````text
{"meta": true, "mode": "kill", "argv": ["exp_review.py", "kill", "/home/claude/padua_research/topics/bivariate-lanczos-20261031/reviews/logs_L5/b_kill.jsonl", "30", "40", "50"], "start": "2026-10-31T22:47:14Z", "numpy": "2.5.3", "python": "3.13.18", "blas": "1", "sha_exp": "ccac2697dbc1675b", "sha_lib": "01139ca2e7ceec3f", "sha_c": "fe12b714c7f06d48"}
````

### A06

Status: original argv recorded in output metadata; interpreter invocation/flags not recovered from argv alone. Source `topics/bivariate-lanczos-20261031/reviews/logs_L5/b_kill.log:1`,
Git blob `a41890b9db4e54a070ed4447286256396b41d487` at retrieval source40347d1.

````text
{"meta": true, "mode": "kill", "argv": ["exp_review.py", "kill", "/home/claude/padua_research/topics/bivariate-lanczos-20261031/reviews/logs_L5/b_kill.jsonl", "30", "40", "50"], "start": "2026-10-31T22:47:14Z", "numpy": "2.5.3", "python": "3.13.18", "blas": "1", "sha_exp": "ccac2697dbc1675b", "sha_lib": "01139ca2e7ceec3f", "sha_c": "fe12b714c7f06d48"}
````

### A07

Status: original argv recorded in output metadata; interpreter invocation/flags not recovered from argv alone. Source `topics/bivariate-lanczos-20261031/reviews/logs_L5/c_repro60.jsonl:1`,
Git blob `1fbea833f41774b6e145b1265c770a9e6504cb6a` at retrieval source40347d1.

````text
{"meta": true, "mode": "repro60", "argv": ["exp_review.py", "repro60", "/home/claude/padua_research/topics/bivariate-lanczos-20261031/reviews/logs_L5/c_repro60.jsonl"], "start": "2026-10-31T22:52:10Z", "numpy": "2.5.3", "python": "3.13.18", "blas": "1", "sha_exp": "ccac2697dbc1675b", "sha_lib": "01139ca2e7ceec3f", "sha_c": "fe12b714c7f06d48"}
````

### A08

Status: original argv recorded in output metadata; interpreter invocation/flags not recovered from argv alone. Source `topics/bivariate-lanczos-20261031/reviews/logs_L5/c_repro60.log:1`,
Git blob `de12ed44dcfb11d9216a101362ad62e49eb24cdd` at retrieval source40347d1.

````text
{"meta": true, "mode": "repro60", "argv": ["exp_review.py", "repro60", "/home/claude/padua_research/topics/bivariate-lanczos-20261031/reviews/logs_L5/c_repro60.jsonl"], "start": "2026-10-31T22:52:10Z", "numpy": "2.5.3", "python": "3.13.18", "blas": "1", "sha_exp": "ccac2697dbc1675b", "sha_lib": "01139ca2e7ceec3f", "sha_c": "fe12b714c7f06d48"}
````

### A09

Status: original argv recorded in output metadata; interpreter invocation/flags not recovered from argv alone. Source `topics/bivariate-lanczos-20261031/reviews/logs_L5/d_unif.jsonl:1`,
Git blob `ec82f0f0c9ab32ebcfdcb04dcaadec1f56455a25` at retrieval source40347d1.

````text
{"meta": true, "mode": "unif", "argv": ["exp_review.py", "unif", "/home/claude/padua_research/topics/bivariate-lanczos-20261031/reviews/logs_L5/d_unif.jsonl", "66", "136", "231", "496"], "start": "2026-10-31T22:54:20Z", "numpy": "2.5.3", "python": "3.13.18", "blas": "1", "sha_exp": "ccac2697dbc1675b", "sha_lib": "01139ca2e7ceec3f", "sha_c": "fe12b714c7f06d48"}
````

### A10

Status: original argv recorded in output metadata; interpreter invocation/flags not recovered from argv alone. Source `topics/bivariate-lanczos-20261031/reviews/logs_L5/d_unif.log:1`,
Git blob `fd58d38da163b3ebdca497355e41617f888b04d3` at retrieval source40347d1.

````text
{"meta": true, "mode": "unif", "argv": ["exp_review.py", "unif", "/home/claude/padua_research/topics/bivariate-lanczos-20261031/reviews/logs_L5/d_unif.jsonl", "66", "136", "231", "496"], "start": "2026-10-31T22:54:20Z", "numpy": "2.5.3", "python": "3.13.18", "blas": "1", "sha_exp": "ccac2697dbc1675b", "sha_lib": "01139ca2e7ceec3f", "sha_c": "fe12b714c7f06d48"}
````

### C009

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:66`,
Git blob `9cd80e0b73871b639dbbf6c216531d3babb399a2` at retrieval source40347d1.

````text
python3 -I topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.py > topics/bivariate-lanczos-20261031/audit-01/L3-framework/exact_framework_checks.log 2>&1
````

### C022

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/audit-02/L1.md:75`,
Git blob `efc1b20b29d96251b0428ecc8cd794f4be7a978b` at retrieval source40347d1.

````text
python3 -I topics/bivariate-lanczos-20261031/audit-02/L1/independent_response_checks.py > topics/bivariate-lanczos-20261031/audit-02/L1/independent-response-checks.log
````

### C075

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L1-reconstruction-01.md:379`,
Git blob `7fb2d501095639893096dcabe1119defc54c0514` at retrieval source40347d1.

````text
python3 -I -u rv_exact_checks.py > L/exact_checks.log
````

### C094

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:87`,
Git blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6` at retrieval source40347d1.

````text
| `reviews/logs_L5/a_slopes.jsonl` | Git blob `9a68042250a1` at `2b52b432fe59`; AC cold storage PENDING | 23,713 | `f714f1b8100415581984674c98acdd54a5b3ac290216751163960ef45322e6a3` | `2b52b432fe59` | cd tracks/bivariate-lanczos/code/review_L5 && OPENBLAS_NUM_THREADS=1 AG_BUILD=<build> python3 -I exp_review.py slopes a_slopes.jsonl 10 15 20 25 30 35 40 44 (about 6 min; needs agivens.c built) | committed at source commit | Summary: reviews/L5-reconstruction-01.md:63; reviews/logs_L5/analysis_review.txt; reanalysis_dev_r01.txt.  |
````

### C095

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L5-reconstruction-01.md:64`,
Git blob `5a8dad674f92d4b742668c31fdaafdd4aa20c773` at retrieval source40347d1.

````text
python3 -I exp_review.py kill b_kill.jsonl 30 40 50
````

### C096

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L5-reconstruction-01.md:65`,
Git blob `5a8dad674f92d4b742668c31fdaafdd4aa20c773` at retrieval source40347d1.

````text
python3 -I exp_review.py repro60 c_repro60.jsonl
````

### C097

Status: exact_named_output_command. Source `topics/bivariate-lanczos-20261031/reviews/L5-reconstruction-01.md:66`,
Git blob `5a8dad674f92d4b742668c31fdaafdd4aa20c773` at retrieval source40347d1.

````text
python3 -I exp_review.py unif d_unif.jsonl 66 136 231 496
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/COLD_STORAGE.md:88`,
blob `13e468d63b19cb25699bbbaa4a2e83d2ef9023f6`:

````text
| `reviews/logs_L5/a_slopes.log` | Git blob `86195134ba10` at `2b52b432fe59`; AC cold storage PENDING | 21,429 | `42599678051f9fe23c5d075e65f68b736b130bd6ddea6c9c915005b588473879` | `2b52b432fe59` | stdout of the same exp_review.py slopes run | committed at source commit | Summary: reviews/L5-reconstruction-01.md:63; reviews/logs_L5/analysis_review.txt.  |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L1-later.md:102`,
blob `5637d6c6d55499fb36cb09c48cbdc07967b93685`:

````text
| `topics/bivariate-lanczos-20261031/audit-01/L1-later/independent_checks.py` | `independent_checks.log` |
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-01/L3-framework.md:21`,
blob `9cd80e0b73871b639dbbf6c216531d3babb399a2`:

````text
An exact counterexample is implemented in [exact_framework_checks.py](L3-framework/exact_framework_checks.py), output [exact_framework_checks.log](L3-framework/exact_framework_checks.log):
````

Documented mapping only (not exact invocation): `topics/bivariate-lanczos-20261031/audit-02/L2.md:31`,
blob `a5903820c70a0f1e8e3c9aa5127054eb804cb332`:

````text
Required correction: retain the universal unnormalised inequality, restrict the quotient implication to `||A||>0`, or explicitly set a zero operator's normalized defect contribution to zero. Under U(n), n≥1, the operators are nonzero and the intended part(c) applications are unaffected. [qualification_checks.py](L2/qualification_checks.py) checks this simple construction; [log](L2/qualification-checks.log). This is a domain omission, not a counterexample to the drift inequality.
````
