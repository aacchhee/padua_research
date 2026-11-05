# Handoff 02 — resolve G0 before resuming Lanczos frontier

- Status: done in aab7bbe97899b0216d60a015c1a0d2cb2d7cbd99
- Previous handoff: [01-work.md](01-work.md), stopped at its mandatory G0 kill; L1–L7 remain unfinished.
- Next agent / model / effort: Codex, gpt-6.1-sol xhigh for numerical reasoning; gpt-6.1-sol medium for technical diagnostics; supplementary independent replay gpt-6-astra high. Required later scientific/protocol audit: Claude Opus 5.5 xhigh, still pending.
- Role: orchestrator/developer; only orchestrator mutates Git.
- Branch: codex/padua-lanczos-frontier-20261105.
- Input head SHA: 0574c47c697a63d76d6222393d3521c145870d03 (output commit, distinct from the later handoff publication).
- Base/main at checkpoint: 440d1079e42c3ef21c40d1cf8870f5b206410c6a.
- Stage: WORK, G0 blocked.
- Date: 2026-11-05.

## Read first

Rules at current branch head; LOG, report, plan, gates, independent-checks-g0.md, evidence/g0-summary.json, evidence/g0-kernel-probes.json, code/g0_replay.py, evidence-manifest.json and COLD_STORAGE.md. Read original handoff01 in full: its seven-target scientific scope and prospective gates remain binding once G0 is resolved. Read source drift README/e6-provenance/e6-frozen-grids12 and checks/audit-02/E6.md at frozen source8359bf7. Earlier handoff status denotes this stop-rule boundary, not completion of the campaign.

## Concrete blocker

Both E1 degree12 exact witness regenerations, scalar certificate arithmetic and E5 symbolic checks pass. Fresh E6 T24 n12 M325/N91 input and producer/upstream hashes match frozen evidence, but dev gap2.7558694937e-10 differs from2.4812027023e-10 and alt1.3027152070e-12 differs from7.3010222490e-12. Upstream xy differs too. Orthogonality remains near machine precision, reference rank91/kappa9.13376 trusted, and yx/dev matrices agree entrywise. Repeated processes and fresh NumPy2.3.5/SciPy1.17 wheels reproduce current bytes. Supported BLAS kernel changes vary gaps substantially but none in the bounded probe reproduced historical numbers. Historical runtime CPU dispatch/library bytes are not pinned.

The README explicitly permits operation/library variation; G0 does not impose universal bit equality. The independent checker conservatively considered the historical discrepancy unresolved and applied handoff01's exact criterion: "any unexplained mismatch stops the campaign until it is explained." The harness reports numerical identity/difference separately from that dated judgment. Do not turn its byte-difference flag into a new acceptance criterion or claim an algorithm/theorem is refuted.

## Required work

1. Refresh main/topic and reconcile base under WORKFLOW without rewriting published history. Scope remains topic directory and its results file; no shared scientific registry edits or writes to other branches.
2. Diagnose the G0 discrepancy with pinned provenance or a justified independent numerical analysis. Distinguish variation in the computed recurrence from error in the reference-span diagnostic. An arithmetic sensitivity/error-propagation analysis may explain a class of variation without recovering the historical CPU, but it must support the actual observed scales and preserve the residual uncertainty. Do not fish kernels indefinitely or dismiss the differences solely because they are small in absolute units.
3. Preserve original receipts and dated FAIL. Write an additive G0 disposition with commands, source hashes, actually executed results, what explanation is established and what remains unknown. Seek a distinct independent check of any consequential resolution.
4. If original G0 cannot be resolved, retain STOP. Do not silently broaden tolerances, waive the gate or run new scientific experiments. If a criterion change is necessary, present a concrete proposed change and ask AC explicitly, citing original handoff01; elapsed time is not approval.
5. Only after a documented resolved G0 verdict, resume handoff01. Complete mandatory novelty/source reads before pursuing saved candidates. Current candidate drafts contain a disclosed prospective novelty-gate timing deviation: some formulas were generated before all mandatory shortlisted reading was finished. Later reading does not retroactively cure it; retain the disclosure and request Claude's explicit protocol disposition during the later audit. No draft has proved status.
6. G1/G2/G3/G4 were NOT RUN. G2 needs an exact degree12 decision before all-degree L2 proof. L7's code is an unvalidated skeleton (syntax checked only), not a completed producer: validate training replay, reference screens and agreement with frozen implementations; G4 must replay both PD-T146 high-degree rows before new fits. Keep its preregistration unchanged, append any justified correction prospectively.

## Reproduction and storage

code/g0_replay.py uses a frozen read-only git archive8359bf7 and restores four historical blobs after SHA/size assertions. Install pinned dependencies and source outside Git exactly as independent-checks-g0.md says. Example after setup:

```sh
PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps OPENBLAS_NUM_THREADS=1 python -B topics/padua-lanczos-frontier-20261105/code/g0_replay.py --output-dir /tmp/padua-lanczos-frontier-g0-next --external /tmp/padua-lanczos-frontier-g0/polyrat --pythonpath /tmp/padua-lanczos-frontier-g0/deps --diagnostics --fresh-pythonpath /tmp/padua-lanczos-frontier-g0/fresh-numeric:/tmp/padua-lanczos-frontier-g0/deps
```

The output directory must be new and outside the repository. Paths may no longer exist in a new sandbox; restore setup without reading credentials. Full harness arithmetic was validated; final output-label-only change has separate recorded hashes. A current diagnostic difference exit1 is an intentional disposition-needed outcome, not an execution crash. No optional full comparator-upper regeneration or G4 is claimed. Raw local outputs are manifested but no Windows delivery/retention is promised. Code/short receipts only in Git, normally under16KiB per evidence file; third-party code/PDF/HTML remains external.

## Reservations, PR and acceptance

Draft [PR24](https://github.com/aacchhee/padua_research/pull/24). Permanent reservation T324–363/N116–131/IDEA414–453/LIT582–593, first pushed40b3eb645c1dc066a8e646b79c67eaa00f4fa181. Parallel MZ reservation T294–323/N104–115/IDEA384–413/LIT574–581 is preserved. No final IDs assigned. Refresh every active/retired reservation before assignment/readiness. Keep PR WORK/AUDIT/PR honest and draft; only AC merges.

Acceptance for this focused step: either an independently checked evidence-based G0 resolution under the unchanged criterion, followed by resumed target work; or a precise unresolved diagnosis with a concrete AC decision required. Preserve all original results and limits. Update log/results/report and manifest for actual changes; commit outputs first, then close this handoff and add the next in a separate commit. Push before final reply. No Claude audit request until there is completed scientific work to audit; preparatory drafts alone are not completed L1–L7.
