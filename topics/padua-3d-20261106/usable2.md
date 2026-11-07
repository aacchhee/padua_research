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
- Initial disposition: prospective; actual R1 disposition is
  **REJECTED: failed** within the finite extension gate, with the
  isolated n4 improvement retained. Canonical homes are the measured
  and negative records linked in R1 below. No PD-N for abandonment.

## Prospective finite protocol — published before execution

Root published this protocol at
`fe23e002f25912b2ca2a09b225e385f596f824fe` before implementation or
scientific execution. The prepublication supplementary review clarified
numerical reproduction wording, separate assessment measures and total
construction cost; those changes are included above and below.

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

Runner commands as planned at registration (actual executions below):

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_optimize.py --degrees 2 4 6 8 --scratch <unique-raw-dir> --output topics/padua-3d-20261106/evidence/u2-pilot.json`

If and only if the pilot gate passes:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_optimize.py --degrees 10 12 --scratch <unique-raw-dir> --output topics/padua-3d-20261106/evidence/u2-holdout.json`

## Round 1 — completed pilot, fixed U2-SN rule fails its extension gate

The first execution stopped at the receipt-size guard after13/16
assessments. Its16689-byte partial output and exact source snapshots are
preserved and hash-identified in [diagnosis](evidence/u2-diagnosis.json).
The failed runner's exact original bytes are also retained in
[u2_failed_size_source.py](code/u2_failed_size_source.py), SHA256
`64151b0c6647fb3cdfe164f4a60fa9bcac075fb86d8313c65e93bb3e4420c3d1`,
so its source does not depend on keeping temporary storage.
Only serialization changed: row arrays with a declared schema and nine
significant display digits; raw output retains full precision. The whole
unchanged mathematical pilot was rerun in a fresh directory. This repair
is not a new research round.

Completed command:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_optimize.py --degrees 2 4 6 8 --scratch /tmp/padua-u2-pilot-20261107-a2 --output topics/padua-3d-20261106/evidence/u2-pilot.json`

The [15050-byte receipt](evidence/u2-pilot.json) pins actual source/data,
raw inventory and environment. Gradient-check maximum normalized error
is5.838e-10. All three historical overlap controls reproduce node hashes,
mesh41 and historical refined values exactly. All16 assessed sets have
the required N distinct nodes, valid numerical guards and full dyadic
rank modulo1000003. This is not a complete committed computer proof:
large raw trials/nodes are local regenerate-only and the independent
execution is separate.

| n | localdet fresh refined | joint-norm fresh refined | ratio | extra descent CPU seconds |
|---:|---:|---:|---:|---:|
|2|4.153630836|4.153630836|1.000000|0.00494|
|4|11.140116090|5.434721017|0.487851|0.87645|
|6|17.669649678|17.669649678|1.000000|0.04493|
|8|24.124150806|24.124150806|1.000000|0.11678|

The n4 determinant falls45.5801→44.8092 while unscaled condition2 falls
9.07936→4.25938, establishing observable objective/update separation.
Its candidate total construction cost is1.02663 CPU seconds including
QR/localdet. Its Gauss noise maximum falls5.827e-6→3.409e-6, but the
absolute-value function's Gauss RMS worsens0.0566234→0.0601125; the
set is not uniformly better for every function. All errors/noise appear
in the receipt, without selecting by them.

The n6/8 five-percent requirements fail, so **U2-SN is REJECTED: failed
within this finite operational gate**. Its n10/12 holdout was not run.
The n4 isolated gain survives as a measured finite result, not a claim
of a degree-uniform quality improvement. See the scoped
[negative home](theory/u2-negative-unrestricted-step.md) and
[measured home](theory/u2-sampled-norm.md).

The [executed diagnosis](evidence/u2-diagnosis.json) explains why the
reported optimizer success is uninformative at n2/6/8. Its initial
projected gradient infinity norms are1,2,2, respectively. The next trial
has exact node collisions (unique counts9/10,68/84,129/165), producing
`Singular matrix`; the penalty has zero gradient. The third evaluation
returns to the initial point, and SciPy terminates by relative function
reduction after one iteration. This is a failure of the specified
unrestricted-step/penalty combination, not evidence of stationarity.

## IDEA?padua-3d-20261106-codex-U2-02 — admissible projected backtracking

Aliases: U2-AB; separation-scaled projected gradient; Neumann-safe trial.

- Question / scope: does an explicit bounded projected-gradient update
  avoid the observed first-trial collision failure while improving the
  same frozen sampled-norm objective?
- Mechanism and hypotheses: identical localdet start, smooth objective,
  training/assessment data and quality/cost gates; change the update to
  projected-gradient steps with a geometric cap, explicit invertibility
  guard and Armijo backtracking. This is an established optimization
  variant, with no historical novelty claim.
- Closest entries read: U2-01 and its preserved trace, IDEA027 and
  LIT336 direct Lebesgue optimization; all other gate comparisons apply.
- Separation criterion: every attempted physical step has coordinate
  displacement at most r/(8*sqrt(3)), where r is the current minimum
  Euclidean node separation, and a trial is inverted only after
  rho=||(V_trial-V_current)*V_current^-1||_infinity<=1/2. U2-01 has
  neither invariant; its initial n6/8 displacements were2 and collided.
  A replay that reproduces an unguarded collision erases the claimed
  implementation distinction. This update is not a renamed localdet
  determinant exchange or a repeat of the failed unrestricted rule.
- Applicable obstructions: the old quality failure remains valid.
  Distinct nodes alone do not prove unisolvence; the Neumann condition
  provides an exact-arithmetic sufficient condition, while its floating
  implementation is a safeguard and not an interval certificate.
- Cheapest decisive test: frozen pilot n2/4/6/8, first checking the step
  displacement, separation and Neumann inequalities in its actual trace.
- Kill criterion before tests: same five-percent fresh refined improvement
  over localdet at both n6/8 and120 CPU-second per-degree cap; failure
  stops this candidate without tuning. Any violation of the declared
  update invariants blocks quality interpretation until corrected.
- Discriminability: the new rule is motivated by training-trace collision,
  not by adjusting against assessment values. Changed update acceptance
  and invariant traces distinguish it even if it later fails quality.
- Initial disposition: prospective; actual R2/R3 results below retain
  this known variant as a useful finite improvement. No measured failure
  of its registered quality gates occurred; no new PD-N is created.

## Round 2 prospective protocol — published before execution

Root published this complete update protocol, including the reused-pilot
disclosure, separate new driver and conditional n10/12 transfer criterion,
at `86b9e26920272bcb6a9a55b3eaf2d41bd63d2d58` before dependent work.

Run U2-AB at n=2,4,6,8. If its unchanged five-percent/cost/guard gate
passes, run round3 n=10,12 unchanged; otherwise stop it with a scoped
negative home. This is the sole additional candidate contemplated by
the original protocol. No other objective, start, parameter or quality
measure is selected from pilot assessment results.

The n2/4/6/8 assessment clouds and their R1 results are already known and
are deliberately reused for this second pilot. They are independent of
the training mesh, but are **not an unseen R2 assessment holdout**.
The changed update is motivated by the preserved training-trial collision
diagnosis, with the original quality criteria unchanged. Degrees10/12
remain unseen and conditionally reserved for the unchanged R2 rule.
For that conditional degree holdout, a successful finite transfer means
the same >=5% fresh refined gain over localdet at both n10/12, with the
same guards and per-degree120 CPU-second cap. Failure retains the actual
values and a scoped failed-transfer statement; it does not trigger tuning.

At each accepted iterate x, compute F,g from the existing frozen smooth
objective. Set d=clip(x-g,-1,1)-x. Stop if ||d||_infinity<1e-7. Let r
be the minimum pairwise Euclidean node distance and
delta=r/(8*sqrt(3)); replace d by d*min(1,delta/||d||_infinity).
Try x+alpha*d for alpha=1,1/2,...,2^-24. Reject without inversion if
rho=||(V_trial-V_current)*V_current^-1||_infinity>1/2 or nonfinite.
Otherwise evaluate F_trial and its gradient and accept only if
F_trial<=F+1e-4*alpha*(g dot d). Stop after25 failed backtracks,
200 accepted steps,120 process CPU seconds, or relative accepted
function decrease<=1e-10. Keep the accepted iterate with the lowest
unsmoothed training maximum, including the initial set. Apply the original
1e-4 relative improvement and final numerical guard fallback. No restart.

The geometric cap implies a single trial moves each node by at most r/8
in Euclidean distance, so every pair remains separated by at least3r/4.
In exact arithmetic the Neumann guard makes the trial Vandermonde
invertible. These are elementary sufficient safeguards, not claims that
the floating implementation encloses an inverse. Record actual observed
displacement, minimum separation, rho, Armijo values, every rejected
trial and stopping reason, with raw coordinate arrays and hashes.

All initial-stage costs, modular checks, separate Gauss/Sobol assessment,
functions, noise, seeds, local starts, source/data pinning, unique raw
policy and independent-check requirements remain those of round1.
The new driver `u2_admissible_run.py` preserves the old runner/source
unchanged and explicitly records its update choice. Planned pilot command:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_admissible_run.py --degrees 2 4 6 8 --scratch <unique-raw-dir> --output topics/padua-3d-20261106/evidence/u2-admissible.json`

## Round 2 and round 3 — completed admissible pilot and unseen-degree holdout

Actual commands, both with unchanged frozen new modules:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_admissible_run.py --degrees 2 4 6 8 --scratch /tmp/padua-u2-admissible-20261107-a1 --output topics/padua-3d-20261106/evidence/u2-admissible.json`

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_admissible_run.py --degrees 10 12 --scratch /tmp/padua-u2-admissible-holdout-20261107-a1 --output topics/padua-3d-20261106/evidence/u2-admissible-holdout.json`

The pilot gate was actually checked before the holdout execution. The
unchanged rule then passed both unseen degree requirements. The new
[summary checker](code/u2_summarize.py) explicitly distinguishes the
n6/8 pilot gate from the n10/12 transfer gate, which the driver itself
does not interpret. It reads actual full-precision raw results and every
trial trace; the [5705-byte receipt](evidence/u2-admissible-gates.json)
reports both gates true and all geometric, accepted Neumann and Armijo
checks passing. No assessment-based tuning occurred.

Terminology clarification: “unseen degree holdout” refers to the new
U2-AB outputs and their quality at n10/12. Historical QR/localdet values
through16 were already known, and the assessment design was already
specified. It does not mean every baseline datum or assessment design
was new at those degrees.

| n | N | localdet fresh refined | U2-AB fresh refined | ratio | extra / total construction CPU seconds |
|---:|---:|---:|---:|---:|---:|
|2|10|4.153631|3.155869|0.759786|1.46 / 1.50|
|4|35|11.140116|5.544014|0.497662|1.26 / 1.41|
|6|84|17.669650|8.222854|0.465366|3.62 / 4.19|
|8|165|24.124151|12.299585|0.509845|10.71 / 12.41|
|10|286|34.870367|17.265295|0.495128|26.60 / 31.01|
|12|455|55.677884|26.007323|0.467103|60.48 / 73.17|

Every run reaches the registered200 accepted-step cap and reports
success=false, so this is a bounded algorithm rather than a convergence
claim. All outputs have the expected N distinct nodes, pass the numerical
guards and have full dyadic rank modulo1000003. At n12, unscaled/ortho
conditions fall33.8341/24.9675→11.0750/8.24010; log determinant falls
1019.588→998.211, again separating norm improvement from determinant
ascent. Pilot+holdout total CPU including all assessments/calibrations
is22.5913+113.5608 seconds. Dense per-objective work is O(MN^2+N^3),
M=21^3, with O(MN+N^2) working storage, plus retained raw trial arrays;
this is not proposed as a cheap all-degree construction.

Function/noise comparisons remain mixed. At n10 all four frozen
function RMS values improve on both assessment measures. At n12 the
absolute-value function's Sobol RMS worsens by2.15%, while the other
seven measure/function combinations improve. Pilot n2 has worse
exponential RMS and some worse noise outcomes; n8 absolute-value RMS
also worsens. The n12 Gauss noise max/RMS fall8.056e-6/1.444e-6 to
6.203e-6/1.255e-6. All outcomes remain in the two receipts. A sampled
norm gain does not promise improvement for every function/noise draw.

Concrete representative: [u2-degree12-nodes.json](evidence/u2-degree12-nodes.json)
contains the actual455-node highest registered degree set, losslessly
encoded as10920 little-endian binary64 bytes in a14853-byte JSON file.
It avoids requiring optimizer replay to use that set and was selected
by degree, not by assessment quality. Coordinates are interpreted as
exact dyadic rationals; no rounding or node movement is introduced.

Executed export and developer check:

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_node_payload.py --receipt topics/padua-3d-20261106/evidence/u2-admissible-holdout.json --n 12 --output topics/padua-3d-20261106/evidence/u2-degree12-nodes.json`

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/u2_node_payload.py --check topics/padua-3d-20261106/evidence/u2-degree12-nodes.json`

The developer check reconstructs the payload hash/shape/cube, distinct
coordinates and rank455 modulo1000003. The independent
[standard-library-only checker](code/uc12_payload_check.py) actually
decodes the IEEE754 integer bits, checks455 distinct exact dyadic points
in the cube and returns determinant residue318086 at freshly checked
prime1000037. Its [exact receipt](evidence/uc12-u2-payload.json) pins the
essential payload and checker source. The separately split
[PD-T?U2-03 finite theorem](theory/u2-degree12-unisolvence.md) supplies
the written Z[1/2] modular reduction and claims **computer-assisted
PROVED unisolvence for this one stored455-point degree12 set**.
All quality and algorithm-wide observations remain **MEASURED** in
[U2-02](theory/u2-admissible-norm.md).
The independent [byte-link check](evidence/uc12-u2-payload-link.json)
also establishes that this essential payload is byte-identical to the
actual n12 coordinate array used in the measured holdout, with NPY
header/type/order and all source hashes checked without NumPy.

The [independent U2-AB replay](evidence/uc12-u2-ab-replay.json) actually
reproduces24/24 scientific rows and6/6 optimization traces, checks all
trial safeguards with maximum reconstructed rho delta2.31e-14, and
checks the returned dyadic ranks in an alternate monomial basis.
The [separate assessment](evidence/uc12-u2-ab-fresh.json) preserves
finite quality gains and mixed function/noise outcomes. This supplements
the required Claude audit, without claiming that audit has occurred.

## Round ledger / Runs needed

R1 completed: unrestricted U2-SN fails its finite extension gate, with
n4 isolated gain retained; its n10/12 holdout was not run.
R2 completed: U2-AB pilot passes at n6/8, with reused assessment disclosed.
R3 completed: unchanged U2-AB unseen-degree transfer passes at n10/12.
Three of at most ten rounds used. No additional candidate, tuning or
degree extension is proposed merely to spend the ceiling.

U2 development and supplementary checks are complete. Required Claude
audit remains root's separate handoff. The broad target
of a stable minimal-node polylogarithmic family remains OPEN.

Final executed validation: all six owned JSON receipts parse and remain
below16KiB; every owned Python source parses and remains below16KiB;
36 actual source/input pins,117 raw-inventory entries and45 owned local
links pass. A focused stale-wording search found no remaining pending
independent-execution claim. R1 source bytes remain unchanged; the exact
pre-serialization-fix runner is additionally retained as noted above.
No Git, shared registry, audit or old handoff file was edited by this worker.
