# M2 work and verification log

Rules/base d36722823441dc40c6e19d69a174459348dd309c, read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md at assignment. Developer: Codex gpt-6.1-sol xhigh, explicit orchestrator assignment. No Git or shared-registry mutations. Files owned are this direction folder, tracks/mz-constants/theory/m2-*.md and tracks/mz-constants/code/m2_*.py (code destination corrected per orchestrator).

Frozen question: direct cardinal lower estimate and an explicit parity-constrained matching upper vector. Supplied private C4 material is not a dependency, and no private text was copied. Source code used for comparison was read in full; recorded hashes below. Full initial IDEA and literature indexes were read; novelty coverage limits in candidates.md.

## Conceptual rounds

| Round | Changed mechanism / decisive test | Outcome |
|---|---|---|
| 1 | Try ordinary Lebesgue constant plus relative cardinal L1 columns | Exact ∫|ℓ_0|=1/N refutes required uniform endpoint column bound; retained candidate 25 / PD-N25 |
| 2 | Replace by angular cells and weighted Schur kernel | All-N cardinal bound and weight floor give explicit log-squared lower bound, PD-T21 |
| 3 | Check supplied full-space alternating vector and simpler U witness | Alternating vector violates degree condition (PD-N26); exact U norm reconstructed (PD-T23), only reciprocal-log quotient |
| 4 | Construct harmonic same-parity U combination with both endpoints cancelled | Exact admissibility, Q=OlogN and continuous norm²≳log³N; matching upper proved with explicit loose constants, PD-T22 |
| 5 | Exact endpoint eta ceiling kill test at N=512 | U quotient<1/4, hence eta>3/4; analytical finite certificate PD-N24 |

Five rounds used, below the ten-round cap. Sharp leading constant left separately OPEN (PD-T27); no attempt to infer it from fits. All considered candidates retained in candidates.md. This direction need not be exhausted to stop: its frozen order target has a complete development proof pending acceptance.

## Completed developer run

Command executed from repository root, 2026-10-31:

```sh
python tracks/mz-constants/code/m2_endpoint.py --exact 512 --measure 8 16 32 64 128 256 512 1024 > topics/mz-constants/directions/M2/developer-run.jsonl
```

Environment: Python 3.12.14; NumPy 2.3.5; SciPy 1.17.0. No random seed (deterministic). Input is the integer list in command and explicit formulas in the checker. No supplied numeric output consumed by this run. Measurements are diagnostics only; theorem proofs are analytic and not computer-assisted.

- Producer code SHA-256: `71f516a44e4d1e46731b0e596b36ba8796577f823c11a267efaf6b71746142c0`.
- Output SHA-256: `df076812f88c19e8e6a71b58ac1eb46cacb506541cccd09a92441fd9356ae6a8`.
- Supplied B2 source SHA-256: `0f9f602c351cd4b8cc816042d529a3c665f6dda4f0884d2d017283ac52231e23`.
- Supplied B2b source SHA-256: `34b1dbc0a08a2a7095241ae35407196b4510bf996cd0eb2716b1803374341d0c`.
- Exact check N=512: U_Q=524288/262143, U_RQ≈0.24384880648700108; exact `RQ_lt_1_4=true`.
- Harmonic witness diagnostics N=8,…,1024: RQ decreases 0.760525 to0.208428, and RQ·log²N increases 3.289 to10.014. No asymptotic inference made.
- Weight floor ratios in that scope are at least1. This does not replace the analytic all-N floor proof.

Generated output is small necessary evidence (under1MB) and retained locally in this folder; orchestrator decides final evidence inclusion or archival to AC-selected Windows cold storage. No claim of transfer to that path.

## Acceptance / audit

Independent Astra adversarial reviewer was sent the mechanisms before acceptance and flagged both inadmissible full-space transfer and ordinary L1-column obstruction independently. Reviewer subsequently reported the two main analytic drafts appeared gap-free, but final pinned-file audit and own execution were still pending at this log entry. Such discussion is not an accepted audit and does not replace the required Claude handoff.

## Runs needed

- Final file-hash pin and independent Astra execution/audit.
- Full historical prior-art disposition from literature worker.
- Required Claude audit handoff via orchestrator.

## Exact next step

Send all final M2 file hashes and the above deterministic command to Astra; preserve acceptance PENDING until its written report. Orchestrator may open M3 because M2 development has reached its frozen target; no third mathematical direction is launched here.
