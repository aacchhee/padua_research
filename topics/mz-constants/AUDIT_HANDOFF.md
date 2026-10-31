# Audit handoff for Claude

- Stage: AUDIT.
- Next: `Claude (Opus 5.5 xhigh): Continue codex/mz-constants-20261031.`
- Rules/base: d36722823441dc40c6e19d69a174459348dd309c. Original scientific checkpoint: 2dc9264333cdf8372947448f4b9bdd3bb577d0e1. Final-ID map and administrative impact records preserve the original labels and audited hashes.
- Developer: Codex orchestrator (runtime model/effort metadata unexposed); explicitly assigned gpt-6.1-sol xhigh mathematics/manuscript, high literature, medium reproduction. Separate gpt-6-astra xhigh mathematical reconstruction and medium protocol check supplement this required cross-agent audit; they do not replace it.
- Final candidate: current branch HEAD together with audit-targets.json once final packaging is pinned. Inspect the manifest and actual HEAD rather than assuming the earlier scientific SHA includes later registry/paper metadata.

## Exact audit scope

Read complete state/IDEAS.md and all obstruction/disposition tables, all shortlisted full candidate records in directions/M1,M2,M3, the M0 baseline and literature/INDEX.md, all21 MZ theory files, report.md, final manuscript and bibliography, independent Astra/protocol reports and their evidence. Check each canonical result's exact hypotheses/status against PROOF_STATUS.md; numerical measurements remain MEASURED.

Central claims: PD-T014 upper<2 through degreeN−1; PD-T017/018 matching logarithmic endpoint order; PD-T022/023/024 explicit strong fixed-ratio constants; PD-T019 exact U identity; PD-N004 finite512 counterexample; PD-T025 upper-Gram hyperinterpolation application; PD-T021 signed-Padua marginal compression. All statements have independent mathematical reconstruction. PD-T020/027/028 remain OPEN; no administrative reclassification hides them.

The mathematical proofs are analytic. The exact finite checkers supplement them; they are not finite extrapolation proofs or interval-spectrum certification. Trust assumptions are the written elementary identities/inequalities and standard finite-dimensional variational principles, not private results or floating-point libraries.

## Reproducible commands

From repository root, with Python3.12, NumPy2.3.5 and SciPy1.17.0 (exact versions in evidence):

```sh
python tracks/mz-constants/code/m1_exact_check.py --max-n 40 --float 2 3 4 5 6 10 20 40 80 160 320
python tracks/mz-constants/code/m2_endpoint.py --exact 512 --measure 8 16 32 64 128 256 512 1024
python tracks/mz-constants/code/m3_exact_check.py --max-n 25 --measure 20 40 80 160
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python tracks/mz-constants/code/reproduce.py --suite all --max-N 1280 --output /tmp/mz-claude-reproduction.json
python tracks/mz-constants/evidence/protocol-check.py
```

The exact executed M1 invocation and outputs are in directions/M1/RUNS.md. Astra's own independent check/replays and comparisons are under tracks/mz-constants/evidence/astra-*. Re-executed numerical JSON has new timestamps/timings; compare numerical fields and source hashes, not full-file timestamps.

For manuscript compilation use the exact commands and destination in tracks/mz-constants/paper/README.md. The PDF is a local deliverable outside Git; TeX and bibliography are committed. No PDF/source fulltext belonging to third parties is committed.

## Findings to challenge

1. Degree/node/ADE conventions and the even-N parity improvement; full-degreeT_N exceeds2.
2. Defect entry signs versus PSD; Z-matrix comparison and all factors in the coefficient floor.
3. All-N CC weight/cardinal bounds; rectangular Schur row and column normalizations.
4. Harmonic-U witness admissibility, endpoint cancellation, uniform sine/cosine bounds and L≥128/small-N extension.
5. Fejér Fourier plateau, no-alias range, n0 convention, torus shell counts and half-circle factors.
6. An–Wu conditionality, finite512 applicability obstruction, known upper-Gram mechanism and precise reproduction degree. No unverified journal erratum or true logarithmic hyperinterpolation norm is claimed.
7. etaCC→1 does not prove its deficiency has logarithmic order; Padua compression gives onlyliminf eta≥1 and no signed-form positivity.
8. Historical novelty is unresolved, particularly Lobatto interpolation norm theorems; fulltext gaps are pending-reference rather than concealed clearances. The source's stale private D1′ description supplies no public proof dependency.
9. Batch ledger preserves PR2's existing IDs; its member acknowledgement and future shared-registry update remain pending before merge readiness. This topic does not author the charter. Review the actual squash rehearsal/repair artifact and refresh main if PR2 merges.

## Decision and limits

Write your own audit-NN.md with exact candidate SHA/hashes, inspected scope, actual commands and severity-ranked findings. Do not edit the independent audit reports to resolve them; developer responses belong in response-NN.md. A clean scoped audit may advance the topic to PR only after its documented findings are disposed of. Keep the PR draft while required audit or batch coordination remains pending. Only AC merges; no merge is requested at this handoff.

No scientific producer run remains necessary for the stated analytic results. Sharp asymptotics, higherN measurements and2D extensions are future work. Windows archival delivery is pending; locally staged files and actual identities are in cold-storage.md.
