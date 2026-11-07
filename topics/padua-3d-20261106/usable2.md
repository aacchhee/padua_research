# U2 — direct point optimization

2026-11-07. Input/rules `38227202bc6908d5a5a874950145761a8ca4312f`.
Developer: Codex, assigned gpt-6.1-sol xhigh; runtime model metadata is
not independently exposed. Ownership is this new record, `code/u2_*.py`,
`evidence/u2-*.json`, and `theory/u2-*.md`. Root alone owns Git and shared
records. Budget: at most ten counted rounds, with no obligation to spend
the ceiling. No final IDs or ranges are allocated.

## Initialization and reading

Read AGENTS, WORKFLOW, CODEX, topic LOG and report-round08, templates IDEA
and THEORY, the T9 round06 protocol/gate/literature and measured theory
homes. Inspected the full `t9_maxima.py`, `t9_r06_maxima.py`,
`t9_r06_controls.py`, `t7_r06_baselines.py`, `t4_stacks.py`, and inherited
`c3_lebesgue.py`/`c3_rank.py` source chain. Consulted the complete workflow
and source-comparison rows relevant to the inherited controls.

The shared [gate](usable-gate.md) was published at
`26a4b5e3b7d74f58c862e95f51a540a9935d1240`; root then cleared candidate
generation. Before that clearance this worker only inspected existing
inputs and planned known replication. No experiment had been executed.
Additional personally read full closest records: charter U2, C3
candidates, IDEA209, the Van Barel–Humet–Sorber source record, and the
T9 interpolation-correction lemma. Source coverage remains as stated in
the shared gate; no new primary-paper inspection is claimed.

## Known controls to preserve

The primary QR rule uses unscaled product Chebyshev columns in the exact
inherited order: total degree first, then increasing first exponent,
then increasing second exponent. Candidate points are the lexicographic
Python-product ordering of Lobatto(2n+1)^3. SciPy's economic QR with column
pivoting acts on the transposed matrix; the first N=binom(n+3,3) pivots
are retained. Numerical tie behavior and library versions are recorded,
not silently replaced by a different ordering.

The Leja comparator uses inherited `discrete_leja(lobatto(n+1))`, with
the lower-set indices in the same exponent order. The one-sweep localdet
comparator is exactly `t9_r06_maxima.exchange`: four cardinal maxima
starts on the 21^3 angular mesh plus the current node, continuous
L-BFGS-B, determinant gain >1+1e-10, and one node-order sweep from QR.
This is already continuous node optimization and cardinal-based exchange.

Known direct Lebesgue optimization is also a predecessor: IDEA-027 and
LIT-336 describe greedy add/update/Gauss–Newton methods. The inspected
repository record for that source is coverage-qualified and secondary;
this worker has not inspected the original 2014 paper. No historical
novelty claim is intended.

## IDEA?padua-3d-20261106-codex-U2-01 — simultaneous sampled-norm descent

Aliases: U2-SN; smooth cardinal-row maximum; all-node L-BFGS-B.

- Question / scope: can a concrete bounded update improve the frozen
  one-sweep localdet rule's finite interpolation quality at affordable
  extra construction cost, while retaining N nodes in the cube?
- Mechanism and hypotheses: start from the unchanged one-sweep localdet
  set. Move all 3N physical coordinates simultaneously by L-BFGS-B to
  minimize a smooth sampled Lebesgue maximum. This is a known direct
  Lebesgue optimization variant, not a new general mechanism.
- Closest entries read: IDEA027/187/209; LIT336/382; the complete
  inherited T9 source chain, measured records and extraction correction.
- Separation criterion: localdet maximizes one cardinal column and
  accepts a determinant increase; U2-SN differentiates the joint row
  absolute-sum objective over all coordinates and may decrease the
  determinant. The distinction is erased if the implementation merely
  repeats cardinal-column exchange. A zero accepted coordinate change or
  no useful held-out quality change kills usefulness of this fixed rule,
  not the known direct-optimization method.
- Literature baseline / limits: greedy Lebesgue add/update/Gauss–Newton
  already appears in the coverage-qualified LIT336 record. No priority,
  exhaustive literature or original-paper reproduction claim.
- Obstructions escaped: the points are not constrained to a killed
  unshifted lattice support. This changes no cubature theorem. Finite
  conditioning, numerical rank and determinant do not bound the norm.
- Verdict: **variant with difference**, without a historical novelty claim.
- Cheapest decisive test: derive and central-difference-check the exact
  finite objective gradient at a deterministic nonsingular perturbed
  n2 set, then compare objective/update traces against localdet at n2/4.
- Kill written before testing: derivative relative error >1e-4 at the
  frozen finite-difference checks blocks optimization until corrected;
  no improvement in the training maximum by 1e-4 relative yields the
  localdet fallback. The pilot is not practically promising unless both
  n6/8 fresh refined validation values improve localdet by at least 5%,
  neither fresh value worsens, guards pass, and each extra optimization
  stays within 120 CPU seconds. Any failed component is retained.
- Discriminability: a fresh assessment cloud and local searches from its
  best points test whether training descent transfers within this finite
  scope. This is not a certified supremum or all-degree statement.
- Disposition: prospective; no result yet. Canonical measured/negative
  homes will be written after actual outcomes. No PD-N for abandonment.

## Prospective finite protocol — awaiting root publication

Round 1 is one fixed pilot over n=2,4,6,8; it includes the analytic
gradient check, historical control calibration, full matched controls,
the fixed candidate and its failures. If its practical gate passes,
round 2 applies the unchanged rule to n=10,12 as a degree holdout. If it
fails, stop this rule with a scoped MEASURED negative record; no parameter
search or renamed repeat. At most one further mathematically distinct
candidate may be proposed later, only with a new prospective registration.
Unused rounds remain unused.

For nodes X, V is the inherited unscaled product-Chebyshev matrix and
C=E V^-1 on the fixed 21^3 tensor angular Lobatto training grid. Define
s_m=sum_j sqrt(C_mj^2+epsilon^2), epsilon=1e-8, and
F=log(sum_m exp(beta*s_m))/beta, beta=40/L0, where L0 is the initial
unsmoothed training maximum. Beta remains fixed for the run. If D is the
derivative of F with respect to C, then dF/dV=-C^T D V^-T. The derivative
of each product Chebyshev row with respect to each physical coordinate
is obtained by differentiating the three-term recurrence. Thus boundary
nodes can move; angular endpoint gradients are not used.

Use one start only: the unchanged inherited one-sweep localdet output.
L-BFGS-B bounds are [-1,1] on every coordinate; maxiter150, maxfun1000,
maxls30, maxcor10, ftol1e-10, gtol1e-7. Extra optimization cap120 process
CPU seconds per degree. Retain every evaluated objective, unsmoothed
training maximum, optimizer termination, elapsed CPU, inverse failure and
best trial identity in raw output. Return the visited set with the lowest
unsmoothed training maximum, including the initial set; no assessment
result selects a node set. If improvement <1e-4 relative or the final
guards fail, return the initial set and record the failed attempt. No
restart, hidden seed or validation-based tuning is allowed.

The finite-difference check uses n2 localdet perturbed by deterministic
sinusoidal coordinates of amplitude1e-3, clipped inside [-.99,.99], ten
coordinate directions selected by linspace across the 30 variables,
central difference h=1e-6, and denominator max(1,|analytic|,|difference|).
This finite check validates implementation only; the matrix differential
is justified algebraically in the durable theory record.

Controls are inherited QR, inherited lower-set discrete Leja and unchanged
one-sweep localdet, regenerated with current library versions and the
exact ordering above. Calibrate QR n4/n8 against old mesh41/refined rows
and localdet n2; preserve any discrepancy and its node identities instead
of assuming floating QR ties transfer between versions. Record QR,
localdet and U2 construction CPU separately, plus objective evaluations,
iterations, node count, raw node hashes, unscaled/orthonormal condition2,
inverse residual and log determinant. Numerical guards are condition2<1e12
and inverse residual<=1e-7; suppress unreliable quality values. Candidate
total construction cost includes QR plus localdet plus the extra descent;
none of those initial stages is counted as free.

Assessment is frozen before optimization and never used for selection:
the 32^3 tensor first-kind Gauss angular-midpoint grid (disjoint from
training), plus8192 scrambled Sobol cube points with seed2026110702,
plus8 corners. Refine the four largest distinct Gauss points and8
corners by the inherited T9 L-BFGS-B Lebesgue search. Retain all initial
and final search values, including optimizer failures. Report the maximum
over those lower samples, not a supremum. Also report mesh21/41 values
for comparison with old results, with their training overlap explicit.

On the fixed Gauss and Sobol points report max/RMS errors separately for exp(x+y+z),
1/(1+5*(x^2+y^2+z^2)), abs(x+y+z)/3, and
cos(3*x+2*y-z). Assess deterministic additive data noise of amplitude
1e-6 using Rademacher signs from seed2026110703+n,16 trials, reporting
maximum/RMS output and worst sampled row-l1 amplification. Noise and
function comparisons remain finite MEASURED observations. Record numerical
polynomial reproduction through the nodal inverse residual. An exact
finite-field rank check at prime1000003 interprets the actual binary64
node coordinates as dyadic rationals via as_integer_ratio; try1000033
only if the first rank is deficient. A full modular rank is a positive
exact witness under its arithmetic model; deficient modular rank is not
a real singularity conclusion. Numerical rank never becomes PROVED.

Every receipt is <16KiB with all actual code/data hashes, versions,
environment, seeds, exact command, actual outcome and unrun cases. Raw
nodes and complete evaluation/refinement logs use one unique `/tmp`
directory per execution, with byte/hash identities. They are local
regenerate-only, not claimed archived. Consequential results need the
separate planned supplementary execution; no self-approval or complete
computer-assisted proof is claimed from missing committed raw evidence.

Planned runner commands (not yet executed):

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_optimize.py --degrees 2 4 6 8 --scratch <unique-raw-dir> --output topics/padua-3d-20261106/evidence/u2-pilot.json`

If and only if the pilot gate passes:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_optimize.py --degrees 10 12 --scratch <unique-raw-dir> --output topics/padua-3d-20261106/evidence/u2-holdout.json`

## Round ledger / Runs needed

No rounds counted and no mechanism run executed. Root must publish this
protocol before dependent execution. Implement/freeze the runner, execute
the pilot, preserve each failure, and send the source/node hashes and
exact command to the supplementary checker. A later code correction must
preserve the failed execution and its old source snapshot separately.
