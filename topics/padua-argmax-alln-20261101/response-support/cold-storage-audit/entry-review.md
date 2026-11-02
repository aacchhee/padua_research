# Per-entry command and summary review

Protocol audit at initial `6fae535df28303b27ca1d533d9afa229660a3a20`, tool impact through `b8fbb5c5be374bf658d2970681c7cac0fb40d737`. Paths below are relative to `topics/padua-argmax-alln-20261101/`. Row numbers follow the machine manifest. Every row passed source-path/blob/SHA-256/size and actual restoration comparisons; see `roundtrip.json`. `metadata.json` pins committed generator and retained summary blobs. The table is coverage, not a claim that every producer was executed anew.

## Command groups

- **A**: `audit-support/claude-audit-01/files/A/indep/padua_indep.py` is committed; accepts `--n N --dps 90 --out OUT --grid 801 --checker-compare --leaf-replay --leaf-containment`. JSON fields show these optional checker/leaf/grid outputs were used. Manifest does not supply the actual command, flags or path setup. Script lines 470/496 hard-code `/home/user/padua_research/...`; additional imports also use the old root. A reproducible invocation needs explicit relocation/setup. No fresh execution in this audit. Historical output/timings retrieved exactly instead. Finding CS3.
- **D**: committed `audit-support/claude-audit-01/files/D/t1_local.py`, with default 21 degrees n=2…201 and adjacent `padlib.py`, writes adjacent `t1_local.json`. Copy both to scratch before rerunning. Manifest's generic prose does not name the script or its default argument. Finding CS3; not freshly rerun.
- **AM**: historical audit-support inventory includes hashes of ephemeral scratch-only files. README explicitly says those files were not archived. No committed manifest-producing command is identified; the blanket “regenerable by rerunning the named sub-auditor script” is inaccurate for this historical inventory. Retrieve the pinned blob; do not promise exact regeneration. Finding CS3.
- **EM**: `code/part3/check_evidence.py --refresh` is committed, but requires the historical evidence tree/output boundary specified in the row. Refresh at the current head is a different inventory. Retrieval preserves the original inventory; the response's current inventory is separate work.
- **IS**: explicitly non-scripted historical input provenance. Retrieval, not regeneration, is the documented method; audit-01/F retains 236/236 blob verification summary.
- **G1**: `code/gated/d1_screen_r01.py OUT/d1_screen_r01.json > OUT/d1_screen_r01.out`, OPENBLAS/OMP=1; stdout and JSON agree with the script interface. `gzip -n -9` is a packaging step after generation. Timing/argv/environment or completed-note hash can differ on rerun; retained receipt specifies comparison exclusions. Source gzip remains retrievable exactly.
- **G2**: `code/gated/d2_screen_r01.py OUT/d2_screen_r01.json > OUT/d2_screen_r01.out`, OPENBLAS/OMP=1; arguments match the committed interface. Retained receipt describes exact scientific equality with timing/argv exclusions.
- **G3**: `code/gated/d3_edge_generate.py --output OUT/d3_edge_certificate.json --ep-output OUT/d3_ep_screen.json`. Executed here from pinned sources: E-P JSON byte-identical, SHA-256 `3215523e1a768ce7e81c76283ac18bf476f8162bdcd84e579a7b93388707d14c`. Certificate produced as a by-product; its mathematics was not reaudited.
- **T2/T3**: `code/part3/tests_T2_T3.py T2|T3 OUT/name.json`, OPENBLAS/OMP=1. Positional test selector and destination are correct. Separate independent outputs use the same code; existing summaries disclose this.
- **P**: `code/part3/pairing_screens.py --output OUT/pairing_screens.json`, OPENBLAS/OMP=1; interface correct. Existing measured summary and exact-comparison receipt retain their different scopes.
- **T1**: `code/part3/tests_T1.py OUT/tests_T1.json`, then `code/part3/tests_analyze.py OUT`. Scripts are committed, but analyzer first reads T2/T3/T4 JSONs before processing T1; those prerequisite files are not stated in the T1 rows. A fresh OUT containing only the first producer result fails. Finding CS3. The analyzer splits profile cells and adds comparisons; it does not leave the raw unsplit producer output unchanged. Existing audit-01/raw-replay hash and comparisons remain historical evidence; this audit did not redo T1.
- **TS**: `code/part3/tests_analyze.py OUT` with T1/T2/T3/T4 prerequisites stated in this row. The command is a postprocessor, not a new measurement.

## Retained summary groups

- **SA**: `audit-support/claude-audit-01/subaudit-reports/A.md` and audit-01 executions: direct-cardinal numerical agreement, tested degrees, grid scope and rigorous checks distinguished.
- **SD**: corresponding `subaudit-reports/D.md`: measured local inequality, n=2…201, ratio <=0.447, scope and float limitations.
- **SF**: support README, `subaudit-reports/F.md`, audit-01 provenance and execution counts. These are compact provenance summaries; exact inventory details require retrieval.
- **SG1/SG2/SG3**: `outputs/gated/check_d1_r01_receipt.json`, `check_d2_r01_receipt.json` plus `d2_screen_r01_weighted.json`, and `check_d3_r01_receipt.json` plus `d3_edge_certificate.json`, respectively. All remain committed and below 16 KiB per generated file. Receipts preserve identities, commands, exclusions and measured/exact distinctions.
- **ST1**: `attempts/T1-T5.md`, `outputs/part3/tests_summary.out`, `independent-checks-part3.md`, audit-01 measured replays. They retain literal KILL / dated noncorner RETAIN, tested range, missing general-beta series and raw replay hash. Full cell profiles require retrieval.
- **ST2/ST3**: `outputs/part3/tests_T2.out` / `tests_T3.out`, or `independent_T2.out` / `independent_T3.out` for independent artifacts; `attempts/T1-T5.md` and audit-01 distinguish the finite measured kills from general mathematical claims.
- **SP**: `theory/argmax-alln-codex-06-measured-pairing.md`, `outputs/part3/pairing_exact_check.json` and audit-01 replay summary. The exact checker concerns its scoped list comparison, not certification of the entire measured screen.
- **STS**: `outputs/part3/tests_summary.out`, `attempts/T1-T5.md`, audit-01; complete fit arrays are retrievable, while conclusions remain in short records.

## Complete entry matrix

| # | Manifest artifact | Command group / assessment | Retained summary |
|---|---|---|---|
| 1 | `audit-support/claude-audit-01/files/A/indep/out/indep_n10.json` | A / incomplete invocation | SA |
| 2 | `audit-support/claude-audit-01/files/A/indep/out/indep_n11.json` | A / incomplete invocation | SA |
| 3 | `audit-support/claude-audit-01/files/A/indep/out/indep_n12.json` | A / incomplete invocation | SA |
| 4 | `audit-support/claude-audit-01/files/A/indep/out/indep_n13.json` | A / incomplete invocation | SA |
| 5 | `audit-support/claude-audit-01/files/A/indep/out/indep_n14.json` | A / incomplete invocation | SA |
| 6 | `audit-support/claude-audit-01/files/A/indep/out/indep_n15.json` | A / incomplete invocation | SA |
| 7 | `audit-support/claude-audit-01/files/A/indep/out/indep_n16.json` | A / incomplete invocation | SA |
| 8 | `audit-support/claude-audit-01/files/A/indep/out/indep_n9.json` | A / incomplete invocation | SA |
| 9 | `audit-support/claude-audit-01/files/A/indep/run_8_12.log` | A / exact historical stdout command absent | SA |
| 10 | `audit-support/claude-audit-01/files/D/t1_local.json` | D / generic manifest prose | SD |
| 11 | `audit-support/claude-audit-01/manifest.json` | AM / retrieval-only inventory not accurately classified | SF |
| 12 | `evidence-manifest.json` | EM / historical tree required | SF |
| 13 | `input-snapshot.json` | IS / retrieval-only explicitly disclosed | SF |
| 14 | `outputs/gated/d1_screen_r01.json.gz` | G1 / interface and comparison supported | SG1 |
| 15 | `outputs/gated/d1_screen_r01.out` | G1 / stdout, timing-dependent | SG1 |
| 16 | `outputs/gated/d2_screen_r01.json` | G2 / interface supported | SG2 |
| 17 | `outputs/gated/d2_screen_r01.out` | G2 / stdout, timing-dependent | SG2 |
| 18 | `outputs/gated/d3_ep_screen.json` | G3 / freshly regenerated byte-identically | SG3 |
| 19 | `outputs/part3/independent_T2.json` | T2 / interface supported | ST2 independent |
| 20 | `outputs/part3/independent_T3.json` | T3 / interface supported | ST3 independent |
| 21 | `outputs/part3/pairing_screens.json` | P / interface supported | SP |
| 22 | `outputs/part3/tests_T1.json` | T1 / missing analyzer prerequisites | ST1 |
| 23 | `outputs/part3/tests_T1_n100.json` | T1 / missing analyzer prerequisites | ST1 |
| 24 | `outputs/part3/tests_T1_n101.json` | T1 / missing analyzer prerequisites | ST1 |
| 25 | `outputs/part3/tests_T1_n128.json` | T1 / missing analyzer prerequisites | ST1 |
| 26 | `outputs/part3/tests_T1_n199.json` | T1 / missing analyzer prerequisites | ST1 |
| 27 | `outputs/part3/tests_T1_n200.json` | T1 / missing analyzer prerequisites | ST1 |
| 28 | `outputs/part3/tests_T1_n24.json` | T1 / missing analyzer prerequisites | ST1 |
| 29 | `outputs/part3/tests_T1_n256.json` | T1 / missing analyzer prerequisites | ST1 |
| 30 | `outputs/part3/tests_T1_n399.json` | T1 / missing analyzer prerequisites | ST1 |
| 31 | `outputs/part3/tests_T1_n400.json` | T1 / missing analyzer prerequisites | ST1 |
| 32 | `outputs/part3/tests_T1_n48.json` | T1 / missing analyzer prerequisites | ST1 |
| 33 | `outputs/part3/tests_T1_n96.json` | T1 / missing analyzer prerequisites | ST1 |
| 34 | `outputs/part3/tests_T2.json` | T2 / interface supported | ST2 |
| 35 | `outputs/part3/tests_T3.json` | T3 / interface supported | ST3 |
| 36 | `outputs/part3/tests_summary.json` | TS / prerequisites documented | STS |

All entries retain a relevant short summary or receipt; the summaries do not substitute for raw arrays or historical inventories. No general claim was independently recertified here. The existing audit verdicts remain the authority for mathematics.
