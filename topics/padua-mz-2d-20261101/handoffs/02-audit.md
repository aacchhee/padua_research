# Handoff 02 — padua-mz-2d-20261101 — required Claude audit

- Status: done in 0d48727f13bf8afcf8c21568ed71572c305552a5
- Previous handoff: [01-work.md](01-work.md), done in `e847601c6c1f1261d4862d63360fdfdb0df8a15b`.
- Next agent / model / effort: Claude, Opus 5.5 xhigh.
- Role: independent mathematical auditor.
- Branch: `codex/padua-mz-2d-20261101`.
- Input head SHA: `e847601c6c1f1261d4862d63360fdfdb0df8a15b` (existing complete candidate; the handoff publication commit comes later).
- Main / base: `806cc7b4509fd93bae652f9545d32d95529f8281`.
- Stage: AUDIT; required Claude audit PENDING; PR14 remains draft.
- Written by / date: Codex orchestrator, runtime root metadata unexposed; mathematics gpt-6.1-sol xhigh, mechanical workers medium · 2026-11-01.

## Task

Perform the complete independent audit requested by AC. Read the full current `state/IDEAS.md`, all obstruction/disposition tables and the full new candidate records, not just the new registry summary. Audit the entire final campaign: all22 new theory/negative files under `tracks/mz-constants/theory/mz2d-*`, three scientific `mz2d_*.py` checkers, measured and exact evidence, source conventions, final mapping/registration and retained failed candidates. Do not substitute the supplementary Codex audit for this required Claude review.

Current declared statuses:17 PROVED,2 MEASURED,3 OPEN among the22 new records. Assigned IDs PD-T106–117, PD-N044–053, IDEA-210–227; new LIT-427–428 with five existing source IDs reused. Full own reservation remains T106–135/N044–061/IDEA210–245/LIT427–444, including permanent unused headroom. The original PD-T028 remains OPEN.

Check D1's all-degree aliasing and exactness-m correction, its rational pencil, the five-region boundaries and the bounded tensor/Fourier-mask architecture. D1 verdict is PASS, not a sharp spectral bound. Check the written reductions and exact integer acceptance for m10/20/30/40 and the stored225-term m30 eta>3/4 witness. Floating evidence to m100 and every-m2..40 remains MEASURED.

Reconstruct the harmonic corner-weight formula, its negative sign for every m>=3 and logarithmic asymptotic. Check the fixed-ratio extension of the continuous negative-corner correction, including cancellation inside half-exactness. Inspect every scoped failed mechanism without converting a failed route into a refuted all-m target. Check the admissible rhombus packet's finite measured scope.

Audit the diamond/parity-projected reconstruction versus the failed rectangular Fejer transfer. For signed hyperinterpolation, check the exact C-to-L2 weighted-L1 identity, the valid degree-dependent absolute-Gram bound, reproduction condition n+r<=m, and actual failure on quadratics at n=m−1. The maximal complete reproduced space is Pi1 for m>=3. Absolute-Gram/negative-leverage sufficient uniform bounds are now proved to diverge; the actual operator-norm target remains OPEN.

For D7, independently reconstruct the exact total-degree tensor-CC spectral envelope, disjoint coordinate-defect wedges and all1D-derived constants/order consequences. This is one theorem for a positive control family, not a signed Padua comparison. D2/D3 stopped before D7 activated; their universal signed spectral/order targets remain OPEN. Do not reopen them as development while auditing.

## Read first

1. Rules at branch head: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`; record full rules SHA. This session's rule read is806cc7b, byte-identical to cf89b140 before that merge.
2. Topic `LOG.md`, `plan.md`, `report.md`, `definitions.md`, `directions/D0.md` through `D7.md`.
3. Complete `state/IDEAS.md`; full topic `ideas-d1.md`, `ideas-d2.md`, `ideas-d4.md`, `ideas-d5.md`, `directions/ideas-d3.md`, `directions/ideas-d7.md`; relevant linked predecessors.
4. All new theory/code/evidence; `independent-checks.md`, `independent-math-d1.md`, `independent-math-d2.md`, `supplementary-audit.md`, `response-d4.md`, `response-d5.md`.
5. Track README, complete requested M1/M2/M3 theory and four old code files, original manuscript; MZ report/POST_MERGE and prior-art report/comparison/translation; literature INDEX, all mz-* source records, topic `literature.md` and new LIT427/428 records.
6. Accepted A1/PD-T101 and its Claude audit at merged main. A2 records01–04 at frozen `12e9cf4539d0977773cad75fc74f93d1664cb429` are audit pending and contextual only. All13 pinned A2 objects match advanced PR12 `7ec02d0fa4a06cf9ab7ede5db0b60a5eddf887d1`; see `protocol/final-input-manifest.json`.
7. `protocol/final-id-map.json`, `final-reservation-recheck.json`, `final-assignment-checks.json`, `final-validation.json`, `integration-rehearsal.json` and shared registry/crosswalk/ledger additions.

## Reproduction and evidence

Use an isolated audit output directory or disposable worktree. Preserve all developer and earlier auditor evidence. Install the recorded dependency if absent, using the cloud runtime/network instructions:

```sh
python -m pip install --target /tmp/padua-flint python-flint==0.9.0
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 20 30 40 --output /tmp/claude-mz2d-spectra.json
```

Run without Python -O: acceptance assertions must execute. Numerical SciPy only proposes endpoints and integer transformations; accepted congruences/row margins are exact. Compare exact inertia/brackets and independently evaluate the stored m30 coefficients; regenerated floating vectors need not have identical rounding on another runtime.

`mz2d_independent_check.py` supplies `stored_witness`, `region_checks`, `nodal_check`, `rejection_controls` and normalization helpers. Its main function writes the frozen developer-side receipt, so import functions and write a new auditor receipt, or run it in a disposable copy. Its existing separate-agent execution checked245 exact nodal moments,371 Gram pairs,1,221 region cases and six rejection controls. Record your actual commands, versions, input hashes and scope; inspecting old output is not a rerun.

The D0 script is floating only. Replaying it is optional at an auditor-chosen bounded scope; preserve original evidence and do not treat residuals as rigorous global enclosures. `protocol/final-validate.py` checks mapping/registry/link/frozen-source identities but writes its receipt; run in an isolated copy or preserve existing bytes. Do not execute `final-assign.py --apply` or repeat allocation.

All essential outputs fit limits (largest837344 bytes; whole campaign about1.6MB). No cold-storage payload is required. No Windows bridge was available. Missing final-version fulltexts/DOIs/journal links are in report/literature; do not cite unread text as a theorem.

## Known review dispositions and identity impact

Supplementary Astra review is complete with S1/S2 fixed and focused rechecks passed. It does not supply required Claude acceptance. S1 killed uniform absolute-Gram/negative-leverage sufficient routes without changing the actual OPEN operator-norm target. S2 consolidated D4's repeated negative-node floor obstruction into PD-N045.

Historical `PD-N?mz2d-codex-41` maps to PD-N045, not a new allocation. Its exact original4450-byte proof remains recoverable in `directions/d4-positive-floor-verification.md` at byte offset2255, SHA256 `bcecd47698bea9679f6b734a26f8afb0fd85874a51b414ad75cf9ac650e98903`. Do not edit the archive or frozen independent reports.

Earlier peer checks covered endpoint-only corner subtraction. D3's material fixed-theta extension preceded ID assignment and was separately audited at pre-ID hash `282bc22de3a15056bef406ddc6a3aa4f268a62b4c54a2574b82208e8240a63a1`. It is not claimed ID-only relative to the older peer hash. Final-ID normalization is ID-only relative to the final supplementary pins, verified in the registration receipts. Code/evidence and frozen review/archive bytes are unchanged.

## Scope limits

Only the topic orchestrator mutates Git. As the new auditor/orchestrator, preserve published history and commit only authorized audit outputs. Never commit/push main, merge PRs, force-push, create tags, touch .github or modify proof-attempt branches. Author commits Andrey Chesnokov <aacchhee@gmail.com> with Agent: Claude and exact actual Model/effort trailers. Preserve developer proofs and earlier auditors' reports; return findings rather than silently fixing and approving.

PR14 is draft; no readiness or merge is authorized by supplementary review. Own IDs/headroom and PR15's observed disjoint reservations must remain intact. Disposable rehearsal found this campaign squashes cleanly onto main; prospective PR15 integration conflicts in ID_CROSSWALK and the batch ledger. Reconcile after audit/AC merge order before requesting those merges; do not import unrelated science into this campaign.

## Acceptance and outputs

Write `audit-01.md` with exact audited SHA/hashes, full IDEA/novelty/source scope, independent runs actually executed, trusted dependencies, findings by severity and residual limits. If findings remain set WORK and specify a concrete developer response; if accepted, record the scope without upgrading OPEN or MEASURED claims. Required final preparation may proceed only within AC's continuing authority; only AC merges.

Update topic log and PR14 WORK/AUDIT/PR sections with actual verdict. Commit/push audit outputs first. In a following commit, change only this handoff's status to `done in <audit-output-sha>` and add handoff03 for response or readiness preparation, retaining exactly one open handoff while work remains. Preserve handoff01's body and this body's history. The exact next action belongs in that new file before replying. AC's required reply prefix/short continuation convention remains in force.
