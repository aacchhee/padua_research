# U1/U2 supplementary independent verification

Rules/input head: `38227202bc6908d5a5a874950145761a8ca4312f`.
Role: independent supplementary checker, assigned Codex Sol xhigh; runtime
model/effort is not independently exposed. This is not the required Claude
audit. Ownership is this file, `code/uc12_*.py`, and `evidence/uc12-*.json`.
Only the orchestrator controls Git and shared records.

## Scope and execution boundary

U1 concerns positive oversampled weighted least squares; U2 concerns direct
optimization of exactly N interpolation nodes. This verification adds no
novel mathematical mechanism and makes no novelty claim. The shared gate
owns predecessor coverage. Until the orchestrator supplies the published
gate and prospective protocols, this checker only reads existing inputs and
prepares verification requirements. No new experiment has been executed.

Rules read: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`;
topic LOG read through its existing handoff08 completion. Existing inputs
read include `code/t10_lattices.py`, `code/t10_extract.py`,
`code/t9_r06_controls.py`, `code/t9_r06_maxima.py`, `code/t9_maxima.py`,
the inherited `tracks/lattice-unisolvence/code/c3_lebesgue.py`,
`audit-03/code/T10/gram.py`, `theory/t10-parity-log4.md`,
`theory/t10-quality.md`, `theory/t9-projection-extraction.md`, and
`preregistration-T9-round06.md`. Reading is not an executed rerun.

## Prospective verification requirements

1. Freeze executable/data identities before execution: checker source,
   producer source and helpers, node/weight data, input receipts, commands,
   versions, thread settings, seeds, stopping limits, and raw-output paths.
   Require unchanged identities after execution. Do not pin prose as an
   executable acceptance condition. Use a distinct scratch directory for
   each independent run, and compact receipts below 16 KiB. Larger arrays
   remain local regenerate-only, with actual byte counts and SHA-256.
2. Reconstruct the mathematical object independently. Check n, N=binom(n+3,3),
   M, distinct finite nodes in the cube, positive normalized U1 weights,
   exact node/weight enumeration and canonical order, and every registered
   family/restart/failure. U2 must contain exactly N distinct nodes.
3. State both exponent order and normalization. Reconstruct Chebyshev tables
   independently, form the weighted design A=diag(sqrt(w)) Phi, and use an
   independent QR/SVD solve rather than trusting a producer normal-equation
   inverse. Report singular values and condition of A and of its Gram
   separately. For U2 report condition in the frozen basis and an
   orthonormal Chebyshev basis, so basis scaling is visible.
4. Check the complete coefficient reproduction matrix C Phi against I,
   constant reproduction, the weighted normal equations, and agreement of
   independent predictions with the producer. Test a deterministic
   coefficient combination as well as all basis columns. The known
   anisotropic parity identity G=I+ee^T and equal-order G=I provide strong
   controls; a raw degree-(2n-1) cubature operator is not automatically a
   degree-n projection. A floating residual supplies MEASURED evidence.
5. Preserve inherited controls exactly: tensor Lobatto(2n+1),
   `itertools.product` point order, degree-ordered inherited exponents,
   SciPy economic pivoted QR; lower-set discrete Leja starts at index 0 and
   breaks ties by the smaller original index. The frozen T9 localdet is
   one sweep with registered starts, gain threshold and stopping limits.
   Report original and optimized nodes, every initialization/restart,
   objective evaluations, acceptances, CPU/wall costs and all failures.
   Do not select whichever QR basis/order has a favorable result.
6. Training objective meshes must be separate from final assessment data.
   Retain initial and final local optimizer values, failed termination and
   the best observed initial value. Denser or fresh sampled maxima are
   lower bounds on the continuous norm, including a local refinement.
   If a holdout informed selection or retuning, call it reused and obtain
   a fresh assessment before drawing a generalization conclusion.
7. Freeze the full approximation function suite, noise model, scaling and
   metric before final node selection. Report all functions/degrees and
   all competitors, including poor results. Use both a deterministic
   smooth/non-smooth approximation suite and polynomial reproduction.
   Quantify random-noise variability; a favorable single draw or function
   does not establish a family-wide advantage. A deterministic adversarial
   sign-noise example is an operator stress test, not an iid-noise draw.
8. Separate same-degree behavior from equal-evaluation cost. U1 uses M>N
   function evaluations, whereas U2 uses N. Report M/N and construction,
   factorization and prediction cost. With independent per-observation
   equal variance, coefficient risk is sigma^2 tr(CC^T). The quantity
   M tr(CC^T) has a fixed-total-budget replication interpretation only
   when noise variance scales as M/B under B total observations; state
   that model explicitly. It is not automatically a fair-cost guarantee
   for deterministic function error. Compare feasible evaluation budgets
   without hiding the extra samples.
9. Stop at the published gate/round limits. A finite negative result kills
   only the registered family/objective/stopping rule. Numerical
   ineligibility does not prove exact singularity. Better finite scores
   do not prove a degree-uniform bound or an asymptotic growth law.

## Existing-control observations (inspection only)

- `t10_lattices.operator` applies the continuous orthogonality scaling in
  its raw mode and solves the Gram system for LS. The anisotropic parity
  theorem supplies a rank-one Gram correction. Confusing these modes
  would change polynomial reproduction and noise risk.
- T10's primary global QR explicitly uses the inherited degree-ordered
  basis; restricted extraction uses a lexicographic basis. Earlier work
  records actual tie-dependent node differences. U2 should keep the
  inherited baseline unchanged and identify any different optimizer
  initialization as a separate rule.
- T9 refinement retains both initial and final values because the
  absolute-value objective is nonsmooth. Optimizer success is distinct
  from the largest observed score. Its meshes/refinements are lower
  samples, not certified suprema.
- The existing `t9_r06_controls.py` checks two stored QR values plus an
  actual n2 legacy two-sweep run. Reading it does not reproduce those
  executions, and its legacy control is not the new one-sweep localdet.

## Runs needed

Published shared gate/protocol, frozen producer code/data, then separately
executed producer replays and fresh-code reconstruction under the above
requirements. Exact commands and measured discrepancies will be recorded
after the executable inputs exist. No PROVED status is claimed here.

## Gate/protocol chronology

The orchestrator reports shared-gate publication in
`26a4b5e3b7d74f58c862e95f51a540a9935d1240`. Producers are released to
register protocols only; dependent checks still await their publication.
The v5 `code/artifact_manifest.py` compression change was inspected at
the orchestrator's request: it losslessly compresses the existing identity
map in a single JSON and preserves recursive code/data and inherited-helper
verification. No discrepancy was found by inspection. This checker did not
rerun the orchestrator's mutation controls, and that inspection is separate
from mathematical verification.

## Prospective fresh-code assessment supplement

Registration only, awaiting the orchestrator's protocol publication. Use
no producer objective values to select these checks or their output nodes.
For every published U1/U2 candidate and matched comparator, independently
rebuild the coefficient map using an SVD of the weighted orthonormal
Chebyshev design; use uniform weights for square interpolation. Compare
the producer's coefficient map/predictions with this reconstruction when
the producer exposes them, and always record full reproduction residuals,
design and Gram conditions, M, N and coefficient noise trace.

The fresh evaluation data are the tensor angular midpoint grid of length
28 per axis and 4096 scrambled Halton physical-cube points with seed
2026110712, generated once and never used for node optimization or choosing
the returned set. Record max and RMS separately for the two clouds. The
following complete additional function suite is fixed before outcomes:

- `exp((x+2*y-z)/4)`;
- `1/(1+9*(x+y/2-z/3)^2)`;
- `(abs(x)+abs(y)+abs(z))/3`;
- `cos(5*x-3*y+2*z)`.

Report every function, degree and comparator without an aggregate winner
chosen after seeing results. Also reproduce the producer's own suite using
its frozen definitions. Use 32 independent Rademacher perturbation columns
of amplitude 1e-6, seed `2026110713+n`, in the raw node order. Report sampled
max/RMS amplification and empirical coefficient energy alongside exact
linear-algebra expectation `tr(CC^T)` (computed in binary64, MEASURED).
These noise trials model equal variance per node; fixed-total-budget risk
is a separate explicitly modeled statistic. A shared draw stream may
correlate competitor trials and is not a claim that their ordered nodes
represent the same observation.

These are additional finite stress checks, not extra candidate searches.
Any consequential disagreement is returned to development and root before
rerunning changed producer code. No silent repair or adaptive new function
selection is permitted.
