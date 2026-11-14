# Readiness 02 — focused verifier and replacement-pack check

- Auditor/orchestrator: Codex, `gpt-6-astra` medium (configured assignment; serving metadata not separately exposed), 2026-11-14.
- Rules/input head: `b2e47412e74d2082d2c4e5587baf89cf7b25ab3a`; rules unchanged. Handoff 10 is the scope. Developer output `ccaf2cae3ac937a1f2b2a3dbd2c425059032e8cf`; pack source `52030d1d22d6397a02c2831145a962e02105973b`.
- Accepted science, witness identities, previous full certificate replays, final IDs, builds and licensing were not reopened. No mathematical/novelty campaign or external source reread was performed.

## Verdict

**PASS — agent work is ready for review. P1, P2 and R1 are resolved; no unresolved focused-check finding.** PR35 may be marked ready for review. Only AC merges. This is neither submission nor deposit approval, and it does not resolve AC's publication metadata, frozen-text confirmation, SIAM-file choice or subsequent companion decisions.

One MINOR index correction was made by the auditor in a separate commit, `6d3307f9`: full console logs are inside each evidence pack; Git contains `evidence/verify-runs/ENVIRONMENT.txt`. The former index sentence incorrectly said both logs were in that Git directory. Only `zenodo/README.md` changed, not a pack template, verifier, manifest, receipt or evidence file. This is a stale location/link correction within WORKFLOW's proportionate-audit limits and needs no new audit round.

## P1 — verifier outcomes: PASS

Read both corrected scripts, their exact diff from `9705c75` to `52030d1`, README descriptions and the control harness. Required-program failures set `fail`; a failed comparison also sets it. Required failure takes exit precedence and produces `REQUIRED CHECKS FAILED` / exit 1. Otherwise required agreement is explicitly reported as `ALL REQUIRED CHECKS AGREE`.

SP's optional branch follows the required checks. Platform-dependent source-vector differences are NOTEs. Regenerated payload or exact-norm mismatch, eigensolver failure or regenerated-producer failure sets the separate optional failure flag, prints `OPTIONAL REGENERATION DID NOT REPRODUCE...`, and produces exit 2 when required checks agree. Successful exact payload/norm reproduction produces its own accurate summary and exit 0. The archived-witness certificate is not made dependent on floating proposal identity. Numerical producer/checker code and comparator semantics are unchanged.

The real, unmodified shell scripts were executed on **fresh staged-pack copies** through `tools/verify_controls.py`; only the numerical programs in those copies were replaced by explicitly labelled stubs. All eight scenarios pass:

| Pack / scenario | Observed exit | Observed disposition |
|---|---:|---|
| CC agreement | 0 | all required checks agree |
| CC changed producer receipt | 1 | required checks fail |
| SP agreement | 0 | all required checks agree |
| SP agreement with regeneration | 0 | required agree; optional reproduces |
| SP three vector differences, same exact payloads | 0 | three NOTEs; optional reproduces |
| SP changed regenerated payloads | 2 | required agree; optional does not reproduce |
| SP required checker rejects, optional reproduces | 1 | required failure wins |
| SP required exact producers crash | 1 | required checks fail |

These are outcome/entrypoint controls, **not new numerical certificate executions**. Code inspection also checks the explicit exact-norm comparison and optional program-failure branches. The separate [bounded diff review](audit-support/readiness02-diff.md) found no additional functional defect.

## P2 — interpreter entrypoints: PASS

Path-like `PY` values are resolved against the invocation directory **before** `cd repository`; absolute paths are retained and bare commands remain on PATH. Every Python invocation is quoted. The relative virtualenv is used by every control scenario above, including the SP `out --regenerate` form, so both SP argument/entrypoint paths execute end to end without the old exit 127.

In addition, the orchestrator ran the **full real CC verifier** from a fresh pack copy twice:

```sh
python -m venv --system-site-packages /tmp/mz-focused-run-cc/venv
cd /tmp/mz-focused-run-cc
PY=venv/bin/python PYTHONPATH=/tmp/mz-python PYTHONDONTWRITEBYTECODE=1 bash verify.sh
PY=python3 PYTHONPATH=/tmp/mz-python PYTHONDONTWRITEBYTECODE=1 bash verify.sh /tmp/mz-focused-cc-bare
```

Both finish exit 0, with all four actual certificate/table comparisons agreeing and `ALL REQUIRED CHECKS AGREE`. The new virtualenv reused the existing system packages; no fresh pip installation is claimed by this auditor. Python is 3.12.14, with the previously recorded pinned numerical stack. The developer's fresh-pip/full-SP optional run remains its own execution, documented in the response/environment and packaged console log; this check does not relabel it as an independent rerun.

The full SP numerical suite was deliberately **not repeated**: handoff 10 makes that optional, its producer/checker/data bytes are unchanged, readiness-01 already executed all default numerical checks, and this step independently exercises the changed wrapper outcomes. No new witness or asymptotic claim is inferred.

## R1 — shared-record cleanup: PASS

Reviewed `58697024..52030d1` for this topic's RESULTS.md, state/CURRENT.md and PAPER_MAP.md sections. Draft/pending-readiness and operational AC task clauses are removed. The exact PD-T684/685 content, mathematical OPEN items, source/dependency lists, evidence facts and completed audit links remain. No other topic's section or mathematical result changes. Current publication decisions remain in LOG/handoff/PR.

## Replacement packs and provenance: PASS at the permitted reconstruction scope

Both packs were freshly staged using `zenodo_pack.py stage --rev 52030d1d22d6397a02c2831145a962e02105973b --data /tmp/mz-readiness-data --out /tmp/mz-focused-packs`, once for each `--pack mz-cc` / `--pack mz-sp`. Those data are the exact independently checked inputs retained from readiness-01, not new unpinned witnesses.

Compared every staged file against both complete committed replacement manifests and pinned Git source:

| Pack | Manifest rows | Repository members exactly matching pinned source | Staged hashes exactly matching delivered manifest |
|---|---:|---:|---:|
| CC | 377 | 368 | 375 |
| SP | 706 | 678 | 700 |

The only nonmatching/external rows are the expected fresh measurement JSON runtime metadata, three SP gzip containers, and original replacement-pack console logs. All declared non-log members are present; no extra staged file appears. Both corrected verifier files, comparator, README templates, requirements and LICENSE match the manifest's exact hashes. All manuscript-named code/dependency/evidence paths remain covered; all mathematical producer/checker and paper source bytes are unchanged from readiness-01. Exact decompressed payload/norm/vector identities and the numerical measurement results remain those independently accepted there.

**Access limit:** the replacement delivered ZIP files (`729fb953...4073`, `e8dfc5af...7166`) and their original new console logs were not available to this check. The earlier attached CC ZIP has the superseded `6aa35fc7...` identity, so it cannot establish the replacement ZIP's bytes. The SP transfer-size limit remains documented in readiness-01. Handoff 10 explicitly permits reconstruction; no byte-for-byte validation of the replacement delivered ZIPs, fresh delivery or deposit is claimed. The replacement identities/delivery statements in zenodo/README remain the developer's provenance, with content consistency checked at the stated reconstruction scope.

The auditor's index-only log-location correction changes no packed file: `zenodo/README.md` is an index, while `README-mz-cc.md` and `README-mz-sp.md` are the actual pack templates. Therefore the correction requires no new pack hash.

## Reservation freshness: prior full check remains applicable

A fresh GitHub all-state collection still contains 34 PRs: open #27/#35, 32 closed and merged, no closed unmerged. Main remains `99a9b1d161e41a80c4fd425b63022c681fbe8779`. PR27 advanced from the previous `9d3f5e0f...` to fetched `50070f520b3d5cfe9afbc75f10fdb1bc664b7b71`, but **every ledger plus all four ID registries is byte-identical between those heads**. PR35's ledgers and the same four registries are also unchanged from `9705c75` to the current input.

Under handoff 10 task 5 and WORKFLOW's limit on repeated unchanged checks, the full-union refresh is not repeated. Readiness-01's complete 65-copy/19-unique-ledger check, maxima and uncontested PD-T684–689 range remain valid; no allocation or ID change occurs here. Refresh again if relevant allocation/base content changes before merge. Only AC merges.

## Actual records and next step

Small execution evidence: [readiness02-checks.json](audit-support/readiness02-checks.json). [check_readiness02.py](audit-support/check_readiness02.py) checks the fresh control receipts, real CC logs, all staged manifest/source members and unchanged allocation boundaries before producing it; it is not itself a numerical producer. The explicit control commands were:

```sh
python topics/padua-mz-paper-20261113/tools/verify_controls.py --pack-dir /tmp/mz-focused-packs/padua-mz-cc-evidence --pack mz-cc --out /tmp/mz-focused-controls-cc.json
python topics/padua-mz-paper-20261113/tools/verify_controls.py --pack-dir /tmp/mz-focused-packs/padua-mz-sp-evidence --pack mz-sp --out /tmp/mz-focused-controls-sp.json
python topics/padua-mz-paper-20261113/audit-support/check_readiness02.py
```

No manuscripts, theories, prior audits/responses, receipts, manifests, shared registries or scientific code were edited by the auditor. Local staging/venvs/logs stay off Git. No deposit, submission, merge, force-push, tag or repository-setting change occurred. After publishing this output, close handoff 10 and record the remaining AC-controlled finalization step. No further agent audit is requested for this unchanged accepted scope.
