# Focused readiness support — P1, P2 and R1 diff

- Reviewer: Codex, gpt-6-astra medium (configured/inherited assignment; serving metadata not separately exposed), 2026-11-14.
- Rules/input head: `b2e47412e74d2082d2c4e5587baf89cf7b25ab3a`; read AGENTS.md, WORKFLOW, the Codex role and handoff 10. Pack/tooling candidate: `52030d1d22d6397a02c2831145a962e02105973b`.
- Scope: independent technical inspection of the two verifier fixes, their README semantics, the outcome-control harness, and this topic's three shared-record corrections. Root owns actual controls, entrypoint/CC executions, pack manifests and the reservation impact check. No Git state, manuscripts, theory, shared records, prior audits or developer receipts were changed by this worker.
- Novelty: not applicable. This check introduces no mathematical mechanism, claim, priority assertion or allocation; accepted mathematics and full registry coverage are not reopened.

## Verdict

**PASS within this bounded diff scope; no unresolved finding.** P1/P2 acceptance and entrypoint logic are corrected, and R1 removes the pending-process/AC-task clauses without changing scientific claims. Execution coverage is supplied separately by the orchestrator and is not claimed by this source-inspection record.

## P1 — required and optional outcomes

Read both complete updated shell scripts, the response, and the `9705c75..52030d1` verifier/README changes.

- The required `run` helper captures a numerical program's nonzero exit, marks the global required failure flag and returns failure. Callers compare receipts only after successful program execution. The script continues to a truthful summary rather than aborting silently under `set -e`.
- The `cmpr` helper preserves the comparator's nonzero outcome in the same required failure flag. Historical protocol checks still set that flag when their hashes disagree. Mathematical endpoints, signs and other comparator significance/ignore rules are unchanged.
- SP always performs required archived-input checks before the optional branch. Optional regeneration has its own flag. An eigensolver or exact-producer failure marks optional failure; a regenerated JSON payload or exact norm mismatch also marks it. The exact producer's displayed sign is diagnostic: archived payload identity and required certificate replay remain the certificate premises.
- Source-vector differences are explicitly NOTE-only, while exact payload/norm equality is decisive for successful optional reproduction. This correctly preserves floating proposal portability without falsely asserting that differing witness payloads reproduced.
- Final precedence is correct: a required failure gives exit 1, regardless of optional results; otherwise optional failure gives exit 2; otherwise exit 0. `ALL REQUIRED CHECKS AGREE` names required comparisons only, and a separate optional line reports reproduction or non-reproduction. The old unconditional all-checks-agree defect is removed.
- `--regenerate` is parsed independently of output-directory position. The default output directory and a relative explicit output directory are resolved before entering `repository/`.

Read the complete `tools/verify_controls.py`. It runs the unchanged shell scripts with intentionally stubbed numerical programs, copying reference receipts/files and altering only selected outcomes. The six SP scenarios cover normal success, successful optional regeneration, proposal differences alone, exact-payload differences, required disagreement and producer crash; the two CC scenarios cover success and required disagreement. Expected exit values and exact summary lines are checked, with harness failure if any expectation fails. All scenarios invoke the relative virtualenv path. These are honest outcome controls, not substituted scientific certificate executions. Actual execution of these controls belongs to the root's report.

## P2 — interpreter and invocation paths

Both scripts now distinguish absolute paths, path-like relative values and bare commands. Path-like relative `PY` is resolved against the invocation directory before the `cd repository`; absolute values are retained; bare commands still use PATH. `command -v` checks availability and emits a required-check failure for an unavailable interpreter. Program and comparator invocations now quote `"$PY"`, avoiding the former string-composed interpreter command.

The README examples explicitly start from the pack directory and retain the relative `PY=venv/bin/python` form that is now supported. SP documents the optional command, distinct outcome lines, exact-payload/norm reproduction, platform-dependent proposal NOTE and optional-only exit 2. These descriptions match the actual control flow. The plain required-only mode still has exit 0/1 semantics. No change to a numerical producer, checker, input identity or certificate premise is implied by this repair.

## R1 — shared-record cleanup

Read the complete `58697024..52030d1` diff for RESULTS.md, state/CURRENT.md and PAPER_MAP.md.

- RESULTS drops the draft heading qualifier, pending-readiness line and instructions for AC. It retains the manuscript split, exact PD-T684/685 summaries, completed audit/response links, and the reconstructed-and-independently-replayed evidence fact.
- state/CURRENT removes delivery/deposit instructions and the reserved-operational-task bullet. It retains scientific results, mathematical OPEN parts, completed audit links, evidence content and licence fact.
- PAPER_MAP replaces pending-readiness/delivery task wording by manuscript/archive facts and publication placeholders. It retains supporting-ID lists, mathematical gaps, the MZ-SP dependence on MZ-CC and the regenerated witness fact.
- No other topic's scientific content or result allocation is changed by those edits. The retained metadata-placeholder/not-submitted facts do not assert that AC has completed publication tasks.

## Additional index wording note

The root identified one MINOR index-only discrepancy, independently confirmed here: `zenodo/README.md:45` says copies of both logs and the environment are in `evidence/verify-runs/`, but `git ls-tree` shows only `ENVIRONMENT.txt` in that committed directory. Both committed pack manifests list their `VERIFICATION-2026-11-14.log`. Saying that console logs are in the packs and the environment record is committed in that directory accurately records the existing locations. That narrow index correction is eligible record/link hygiene under WORKFLOW, changes no packaged verifier/template or numerical evidence, and does not require reopening P1/P2. The root owns the correction and its disposition; this worker did not edit the index.

## Commands and limits

Used read-only `cat`, `sed`, `git diff`, `git status` and path searches for the described source inspection, plus this support-note write. No numerical code, control harness, full verifier, fresh virtualenv command or archive integrity check was executed by this worker. No external source PDF was reopened. The parent combines this report with its actual independent commands and pack/reservation checks before deciding readiness.
