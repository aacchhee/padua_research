# Cold-storage manifest — charter-unisolvence U0

Rules/base `d36722823441dc40c6e19d69a174459348dd309c`; developer Codex, assigned `gpt-6.1-sol xhigh`; 2026-10-31. Only actual staged files are manifested. Scientific runs use immutable original script bytes; the import fix anticipated in the plan was not needed.

All artifacts are staged under `/workspace/padua-cold/charter-unisolvence-20261031/U0/`. The complete machine-readable manifest is [evidence-manifest.json](evidence-manifest.json), byte-identical to cold `artifact-manifest.json`; it contains every manifested path, size, SHA-256, source checkpoint, generating command, source Git blob identities and retrieval notes. A matching [evidence-check.txt](evidence-check.txt) is committed as essential small checker output. No remote/off-machine delivery is claimed.

- Source commit: `5123a32774110e9290c42bc1cf3c6838ee6c3d35`.
- Canonical committed original code: `topics/charter-unisolvence-20261031/input-code/ff_padua/`.
- Script Git blobs and SHA-256: `input-code/IDENTITY.json`; all8 ff_padua scripts match actual cold-copy bytes.
- Environment: Python3.12.14; NumPy2.3.5; SymPy1.14.0; Linux6.18.57 x86_64 glibc2.41. Full environment capture is manifested; no credentials collected.
- Deterministic seeds: root generator12345; dense transform `n*1000+p`; timing `n`; HS source labelling1. Developer exact checker has no RNG.

## Frozen generating and checker commands

Commands were actually executed from `/workspace/padua_research` (absolute Python executable identity is recorded in execution JSON):

```sh
python3 -I /workspace/padua-cold/charter-unisolvence-20261031/U0/source-copy/run_all.py
python3 -I topics/charter-unisolvence-20261031/directions/U0/replay_source.py /workspace/padua-cold/charter-unisolvence-20261031/U0/source-copy /workspace/padua-cold/charter-unisolvence-20261031/U0/child-replay
python3 -I topics/charter-unisolvence-20261031/directions/U0/verify_exact.py
python3 -I topics/charter-unisolvence-20261031/directions/U0/check_evidence.py /workspace/padua-cold/charter-unisolvence-20261031/U0 topics/charter-unisolvence-20261031/input-code/ff_padua
```

Original driver stdout/stderr were captured into `run_all.stdout`/`run_all.stderr`, with rc0 and35.303704023361206 seconds recorded in execution JSON. Child wrapper output was captured into `child-replay.stdout`/`.stderr`; every individual child exited0. Exact checker stdout/stderr were captured into `verify_exact.jsonl`/`.stderr`; it exited0. The checker output below verifies the bytes and recorded successful outcomes; it is not a universal mathematical proof.

For regeneration, first copy the committed ff_padua `.py` files into a fresh cold directory, preserving bytes. Use that directory as the `source_copy` argument so source scripts' generated logs stay out of the repository. Replay outputs contain variable timings and therefore need a fresh manifest if regenerated; original hashes identify this particular run.

## Essential artifact identities

Paths below are relative to the stated absolute cold-storage root. Child logs and all8 original scripts are individually listed in the complete JSON manifest.

| File | Bytes | SHA-256 |
|---|---|---|
| `source-identities.json` | 2553 | `430bd64a8cbfe19b0f62fa0e353f4221c8e8c3b6a9ffc86821121b06624fbfe4` |
| `environment.json` | 610 | `da794059c960dcd1dcd7a25621a9f58f2570eedce740735fde6f590bbf899417` |
| `run_all.stdout` | 2369 | `422f75e8712a6a455e902dc0501dc2c79072d418c8422884066be6401257b775` |
| `run_all.stderr` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `run_all.execution.json` | 290 | `1b683e0f46787d9d3308aaf8e66b420b5081194b4567776f5cbd2ea5762d49e8` |
| `verify_exact.jsonl` | 1802 | `b8ec4733f41e1683f4c2a0dc5100a0047e416faefd4616fb73e45b02ff3ec228` |
| `verify_exact.stderr` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `child-replay/execution.json` | 3489 | `3aa1f9f3302059f538a600dae761fcaac2b6a7ac58b6d780a19fd21fa75fce2a` |

- Complete manifest: 15744 bytes; SHA-256 `92e0239d6c5b5077920714ab273f0b32c76a1a6890fcbe3551945067e64108d3`.
- Checker stdout SHA-256: `3f8f148d149d6f54a9482b79efc8ac529da63f34848d2bec9b90bfce5aa57c2a`.
- Checker result: `{"artifacts_verified": 33, "child_statuses_zero": 6, "exact_checker_rows": 10, "manifest_sha256": "92e0239d6c5b5077920714ab273f0b32c76a1a6890fcbe3551945067e64108d3", "result": "PASS", "source_scripts_verified": 8}`.

## Interpretation and independent checks

Finite claims and exact scopes are in theory records06/07; universal developer proofs are01–05; unverified universal source extensions are08. The source floating script reports discrepancies in log determinants; it is not an exact determinant certificate. The supplied driver does not retain child exit statuses; the wrapper does. No source code was repaired.

The independent adversary separately reran source children, developed its own finite checker, and independently reran `verify_exact.py`; its own evidence is under the campaign's `independent/u0/` records and corresponding separate cold directory. This developer does not call repeated developer runs independent-agent verification. Its all-code upper-bound proof was independently reviewed in [bound-review.md](bound-review.md), separate from measured attainment.

## Retention and retrieval

Retain this Padua-specific cold directory until AC chooses a retention policy; no expiry or deletion is authorized. AC/orchestrator is the custodian. Retrieve the exact local absolute paths from the JSON manifest and rerun `check_evidence.py`; verify both size and SHA-256 before using an artifact. The committed manifest/checker/output preserve identities and the observed result, but off-machine archival delivery is not confirmed. If the workspace is lost, the recorded commands and committed original code permit regeneration with newly recorded identities.

## Handoff

Bounded U0 registration is frozen. Root owns Git, moving provisional theory into the final track path, registry allocation, final audit dispositions and any final source/checker commits. No developer acceptance or merge is asserted.
