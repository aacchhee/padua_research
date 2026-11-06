# Handoff 02 — NN MOP conditioning — substantive Claude audit

- Status: done in c5f2820232885fe78504a9bae75b6da68491b1be
- Previous handoff: [01-work.md](01-work.md)
- Next agent / model / effort: Claude, Opus 5.5 xhigh
- Role: independent substantive auditor and topic orchestrator
- Branch: codex/nn-mop-conditioning-20261106
- Input head SHA: cc1edd20a27f955f2f028e988e525889ddfbc805 (completed scientific output; this handoff is published afterward)
- Main / base: 76ba4214b100c86a44941f5e9a662ce9ce48efb8
- Rules read by developer: b4a04981d42c7cd872957facf5e3995e4096ca67
- Stage: AUDIT; draft PR [32](https://github.com/aacchhee/padua_research/pull/32)
- Written by: Codex coordinator, requested gpt-6-astra high; serving identity/effort unexposed, 2026-11-06

## Assignment

Perform the single substantive independent audit of this completed bounded round. Read AGENTS.md, agents/WORKFLOW.md and your Claude role file at the branch head. Follow the current proportionate audit rules. Do not treat the supplementary Astra checks as Claude approval or reopen merged predecessor work beyond actual dependencies.

Read the complete state/IDEAS.md, including all aliases and obstruction/disposition tables, then the full nearest entries and linked dependencies. This audit is novelty-bearing: explicit gauge definitions, rate proofs and failed bound routes are new quantitative continuations, although historical priority is unclaimed. Read literature/INDEX.md before any attribution claim; primary-source coverage remains bounded exactly as external-code.md records.

## Claimed results and review priorities

1. **Krawtchouk sharp rate:** theory/c2-sharp-upper.md proves kappa_N<=3,000,000 N^13(5+2sqrt(6))^(N-1) for the complete NN map in PD-T432's mixed-input/fieldwise metric. Reconstruct the differentiated jets, exact common-node logarithmic source split, separating contours, weighted grid derivative estimate, top-three-coefficient transfer, both a fields and terminal support successor. PD-T437 supplies the matching lower. Check every constant and small-degree convention, not just the terminal weight witness.
2. **Gauge/metric statements:** C1's fixed positive gauges and differentiable local sections retain b fields and include forward coefficients. Verify fieldwise infimum bounds, the Krawtchouk squeeze, Hahn lower transfer, the scalar exact-zero convention, fixed-mass weighted-median dual and the specific monic matrix norm inequalities. Neither an arbitrary matrix-similarity infimum nor a metric-free intrinsic theorem is claimed. Finite signed-OLS envelopes bound fits of unknown gauge optima; they are MEASURED, not exact optimization or outward certificates.
3. **Hahn:** c2-hahn-normality.md proves all-N normality and exact subleading coefficients via the adjacent Cauchy kernel. Its determinant constant is product_(r=1)^t r!. The simple lower and the stronger c2-hahn-terminal-rate.md are separate results. The latter proves the terminal parity-row rate rho_H≈12.1136005841 and a full-map lower liminf, including both parities/fixed masses. Reconstruct the signs, exact positive sums, polynomial comparison, generating coefficients, finite-type entropy lower, saddle and reciprocal quartic. No matching full-map Hahn upper is claimed.
4. **Other rate claims and dispositions:** general-parameter Krawtchouk rho is a lower base, not a matching upper. The product-of-global-maxima Hahn envelope failure is a scoped PD-N, not a refutation of the full target. Preserve every failed/empty/deferred route and the original PD-T448/449 wording/status. Supporting results do not silently make original targets PARTIAL.
5. **Algorithmic scope:** C3's weak-stability target remains OPEN. Check its direct terminal chain term G_p-LM^-1H, residual dimension warning and stated nearby-input algorithm issue. Native ratio measurements are not a theorem or M3 PASS. Warnings and vacuous large-kappa*u regimes remain explicit.
6. **Authenticated comparison:** inspect the exact source archive before executing it; verify all27 members, source normalization and the bitwise input/output transport. Actual M4 and M2 pass. Final comparisons cover116 configurations/348 external calls and58 identical normalized binary64 inputs; native grid has232 cases. External full-NN fields explicitly add input-derived H+d0 high-precision moment lifting; that is not native solver output, positive-real realizability, or joint backward error. Inspect final14 CSV tables and receipts, field errors, matrix coordinates/norm, size convention and fixed input anchor. Decimal JSON transport was rejected after a1ulp mismatch; exploratory records must not masquerade as final evidence. Advanpix-only archive experiments remain unrun.

## Required inputs and reproducible checks

Read LOG, plan, rounds, gates, report, note-material, attempts/C1-C4 and C2-hard, all theory files, input-snapshot.json, evidence-manifest.json, external-code.md, runtime/source/M2/comparison receipts, and both independent-check reports. Check the results file and PR against the exact statements.

Run code/verify_evidence.py first (optional --raw only where temporary artifacts exist). Frozen repository imports are listed in the manifest; no merged source was edited. The analytic theorems have no computer-proof premise. Execute independent consequential checks rather than merely rereading receipts. Useful exact producer/checker entry points are:

- code/c2_rate_checks.py; code/c2_hahn_checks.py; code/c2_hahn_terminal.py --max-m 10; code/independent_hahn_rate.py; code/c2_hahn_upper_search.py --max-m 6.
- The complete reproducible exact Krawtchouk jet/a-field/terminal check is embedded in attempts/C2-hard.md; supporting independent formulations are in code/independent_check.py and its report.
- code/c1_metrics.py and code/c1_summarize.py, with commands and raw conventions in attempts/C1.md. Full61-size primal/adjoint/scalar runs are inexpensive compared with a full triangle Jacobian sweep.
- code/c3_grid.py, with OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1; reproduce selected consequential cases or the complete58-case-per-method grid, as your audit depth requires.
- code/c4_normalization.py and code/c4_lift.py exact finite checks; code/c4_prepare.py, c4_external.m, c4_fidelity.py and c4_compare.py for actual source replay. Full commands/runtime setup are in external-code.md. Use a new /tmp output destination, preserve committed evidence, and compare scientific payloads rather than timing/path metadata.

Archive supplied by AC in this chat: IEP-MOP-main.zip, 1,020,330 bytes, SHA256 cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145. Local developer path was /workspace/attachments/d3b8457a-2c90-4d56-a9a3-f05ea55b5826/IEP-MOP-main.zip; upload ID file_00000000a97c8211920f79c590206753. These are retrieval hints, not a guarantee your runtime has the file. Public source links/member inventory are in external-code.md and the predecessor. If unavailable, state that source execution is blocked; do not call receipt review a rerun or silently substitute a different revision. No third-party source/PDF/paper data is committed.

Raw files are temporary, regenerable and content-pinned; COLD_STORAGE.md explicitly claims no archival delivery. Essential small tables/receipts and all local generating/checking code are committed. Treat rerun platform differences honestly.

## Expected outputs and next step

Write audit-01.md with audited SHA, model/effort, coverage, independently reconstructed proofs, actual commands/results, findings BLOCKING/MAJOR/MINOR/NOTE and remaining uncertainty. Preserve development records and all earlier handoff bodies; do not silently fix material mathematics. This is the first substantive audit of this topic, so return findings under the workflow rather than inventing repeated audit loops.

If accepted or only MINOR fixes remain, set PR stage and hand off a concrete Codex preparation step: final-ID reservation refresh/allocation, shared registry application by reviewed diff, dispositions and final results section. If material findings remain, set WORK and open a bounded Codex response handoff. Final registry assignment/readiness has not happened; there is no current reserved range. Only the orchestrator holding this handoff allocates the next number.

Commit/push audit outputs first. In a following commit close this status at that output SHA and add the next numbered handoff when work remains. Do not merge, force-push, create tags or touch .github. AC explicitly approved continued connector commits under the GitHub noreply author exception; canonical authority and timing qualifications are recorded once in LOG. All repository mutations remain within this topic/results until audited PR preparation authorizes shared registries. Only AC merges.
