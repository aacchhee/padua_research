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
prepares verification requirements. That was the pre-gate boundary; the
subsequent executed scope and outcomes are recorded below.

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

## Initial runs needed (historical, completed below)

Published shared gate/protocol, frozen producer code/data, then separately
executed producer replays and fresh-code reconstruction under the above
requirements. Exact commands and measured discrepancies will be recorded
after the executable inputs exist. No PROVED status is claimed here.

## Gate/protocol chronology

The orchestrator reports shared-gate publication in
`26a4b5e3b7d74f58c862e95f51a540a9935d1240`. At that boundary producers
were released to register protocols only; dependent checks awaited
publication. The later published/executed boundary is recorded below.
The v5 `code/artifact_manifest.py` compression change was inspected at
the orchestrator's request: it losslessly compresses the existing identity
map in a single JSON and preserves recursive code/data and inherited-helper
verification. No discrepancy was found by inspection. This checker did not
rerun the orchestrator's mutation controls, and that inspection is separate
from mathematical verification.

## Prospective fresh-code assessment supplement

Registered before outcomes, then published by the orchestrator in
`fe23e002f25912b2ca2a09b225e385f596f824fe`. Use no producer objective
values to select these checks or their output nodes.
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

## Executed U1 and U2 round1 checks — 2026-11-07

The shared gate was published in `26a4b5e3b7d74f58c862e95f51a540a9935d1240`;
U1/U2 and this checker's assessment protocol were then published in
`fe23e002f25912b2ca2a09b225e385f596f824fe` before dependent execution.
No producer code was repaired by this checker. Heavy checks were deferred
while U2's cap-sensitive pilot ran. Every final fresh-code case used a
separate process with a supervised120-second wall limit; none hit it.

| Actual execution | Scope | Outcome / evidence |
|---|---|---|
| U1 producer replay | Round1 n4/8/12/16, four families; Round2 both parity OLS families |24/24 cases match, including saved nodes/operators/noise; [receipt](evidence/uc12-u1-replay.json) |
| U1 independent reconstruction | All24 cases, recurrence basis and weighted SVD; canonical parity indices/multiplicities; public one/multiple-RHS API; two fresh clouds, eight functions and32 noise trials | All pass; [receipt](evidence/uc12-u1-fresh.json) |
| U2 producer replay | n2/4/6/8, QR/Leja/localdet/joint-norm; complete objective/fallback traces |16/16 cases and all4 optimization traces match; [receipt](evidence/uc12-u2-replay.json) |
| U2 alternative exact rank execution | All16 returned binary64 sets,13 distinct arrays; monomial basis, Python integers, separately checked prime1000037 | Every rank is N; same replay receipt. This is only dyadic-input finite verification, not exact cosine rank or a uniform theorem. |
| U2 independent reconstruction | All16 sets, recurrence basis and weighted SVD; two clouds, eight functions and32 noise trials | All pass; [receipt](evidence/uc12-u2-fresh.json) |
| U2 independent gradient check | Frozen n2 perturbation/ten directions; independent recurrence, transposed solve and stable scalar objective | Maximum relative central-difference discrepancy5.84e-10; [receipt](evidence/uc12-u2-gradient.json) |

The replay scripts are [U1](code/uc12_replay_u1.py) and
[U2](code/uc12_replay_u2.py). The independent array checker is
[uc12_assess.py](code/uc12_assess.py), with its data-only
[inventory builder](code/uc12_inventory.py); the gradient check is
[uc12_u2_gradient.py](code/uc12_u2_gradient.py). Exact commands, full
source/data hashes, versions, raw identities and tolerances are in the
receipts. Every executable/data pin was rechecked after its execution.
No checker pins prose.

U1's frozen producer is `u1_usable.py`, SHA-256
`50da9061b5ec4a5a0735664450d62e7e8e2f19675eed66aca0eb463ff193b0d4`.
For U2 round1, `u2_core.py` is
`b6d75a34cf45b28b89c3e1196efb28101b881b9952f31108fc01bdbccfa97b6e`
and the final compact-display driver is
`69e24c620b0aba0f7d477c05700b1cfe8279a82d3522223a536d52ebe9c48c32`.
Both final fresh assessments actually ran with checker hash
`9a5cc9b3bf34a3c9538a4a6ec2ba89257569190403e77ce7d83376c3d5aca14a`.

### Findings and interpretation

No unresolved producer discrepancy was found within this scope. The
pre-execution phrase "exact polynomial reproduction through the nodal
inverse residual" was returned to development and corrected to numerical
reproduction. Fresh U1's maximum reproduction residual is1.30e-12,
maximum saved-operator difference is4.16e-15, and public parity API
one-/multiple-RHS differences are at most1.43e-15. U2's maximum fresh
reproduction residual is1.67e-13. These remain floating measurements.

Independently reconstructed U1 n16 values illustrate the cost distinction:

| Family | M | iid coefficient risk tr(CC^T) | Equal-budget factor M tr(CC^T) |
|---|---:|---:|---:|
| Anisotropic Haar |1377|0.706314|972.594|
| Equal Haar |1458|0.667504|973.221|
| Global QR |969|6.193240|6001.249|
| Lower-set Leja |969|35.173323|34082.950|
| Anisotropic OLS |1377|0.688839|948.532|
| Equal OLS |1458|0.648984|946.219|

The last column has only the registered replication interpretation;
deterministic errors are not divided by M. OLS reduces same-node iid
variance but need not improve approximation: for the extra ridge function,
n16 anisotropic Halton RMS increases0.0145003→0.0148613, and the extra
cosine RMS increases9.101e-5→1.011e-4. Every function and both clouds are
retained in the identified full raw output.

For U2 n4, midpoint28 row-l1 lower samples improve11.1255643→5.3750140
and Halton samples10.8601039→5.2051484; coefficient noise risk falls
1.43533145→0.99805730. This is a real isolated finite improvement.
It does not imply every function improves: the producer's nonsmooth
`abs(x+y+z)/3` RMS increases0.0566131→0.0601031 on midpoint28 and
0.0668285→0.0679696 on Halton. At n2/6/8 the output equals localdet's
fallback. Inspection and replay of the n6/8 event logs show initial
evaluation, a singular trial, and return to the identical initial set.
Thus the failed original pilot gate concerns that registered update and
penalty rule, and supplies no stationary-point or whole-class obstruction.

The U1 recipe/count/L2-contraction proof, iid risk bound and OLS covariance
identity were reconstructed algebraically from their explicit hypotheses.
No gap was found: the covariance cross term vanishes from (C−C0)V=0;
positive W gives W²<=w_max W; and G>=I yields the stated L2 contraction.
These analytic checks do not promote finite errors or norm samples to
PROVED. All measured norm/error maxima here are lower samples.

### Checker serialization correction and raw boundary

The first fresh U1 execution completed all24 scientific cases, then failed
the final16-KiB receipt-size assertion. Its full-precision output and
executed source are preserved in `/tmp/uc12-u1-fresh-20261107-a1/`.
The corresponding old source is also preserved in the first U2 fresh
directory. Only compact display rounding to nine significant figures
changed; the scientific functions, arrays, seeds and calculations did
not. Both entire fresh assessments were actually rerun at the final hash
above, using `/tmp/uc12-u1-fresh-20261107-a2/` and
`/tmp/uc12-u2-fresh-20261107-a2/`. Full precision stays in the single
identified raw result per assessment; outputs were not split to evade
the receipt limit. Final receipts are14782 and14753 bytes.

All raw arrays, inventories and logs are local regenerate-only output;
no cold-storage delivery or retained-raw availability is claimed. The
committed code and receipts support rerunning the checks. The exact
integer rank execution is explicitly limited by that raw-input boundary;
no computer-assisted PROVED upgrade is claimed here. This supplementary
check does not replace Claude's substantive audit.

## Subsequent U2 scope

Root reports publication of the collision-safe U2 round2 protocol in
`86b9e26920272bcb6a9a55b3eaf2d41bd63d2d58`. The original source/receipt
pins above remain unchanged. This checker has read the new projected-step,
separation and Neumann safeguards; their exact-arithmetic sufficient
arguments are sound under the stated norm bounds, while floating guards
are not interval certificates. The subsequent completed scope is below. The own
midpoint28/Halton/function/noise assessments will be explicitly reused,
since their round1 results are already known; no unseen-holdout claim
will be made for those repeated points or functions.

## Completed collision-safe U2 pilot and degree holdout

The unchanged new driver/module were independently replayed at n2/4/6/8
and at the registered previously unseen degrees10/12. All24 scientific
case rows and all6 optimization traces match. Both registered target gates
pass. [Actual replay receipt](evidence/uc12-u2-ab-replay.json) and
[checker](code/uc12_ab_replay.py) identify the exact sources, data and
commands. Full-rank monomial checks at prime1000037 also passed for every
returned dyadic array in these two batches; the raw-only ranks have the
same scope/retention boundary as the earlier generic rank checks.

Every recorded trial's coordinates were independently associated with its
hash. The checker rebuilt its recurrence evaluation matrix, coordinate
displacement, old/new minimum Euclidean separation and Neumann row norm.
It checked all geometric bounds and accepted recorded Armijo inequalities;
the largest difference from reported rho is2.31e-14. This is binary64
trace reconstruction, not an interval or exact inverse enclosure. It
also checked that the returned node array is exactly the registered best
accepted trial. The scalar objective gradient had already passed the
separate independent finite-difference check above.

| Target degree | Refined candidate/localdet ratio | Producer extra optimization CPU seconds | Registered gate |
|---:|---:|---:|---|
|6|0.465366|3.623|PASS|
|8|0.509845|10.711|PASS|
|10|0.495128|26.600|PASS|
|12|0.467103|60.484|PASS|

Times are measurements under the recorded single-thread setup, not a
complexity theorem. Total candidate construction costs include QR and
localdet initialization. The independent replay has its own timing in
its receipt. The new pilot uses previously known assessment data; the
reported n10/12 transfer concerns held-out degrees under the unchanged
rule. No result states an asymptotic rate or a certified supremum.

The complete reused assessment was separately executed for all24 sets
using the unchanged own checker and published functions/seeds:
[fresh-code receipt](evidence/uc12-u2-ab-fresh.json). "Fresh-code" means
an independent reconstruction; these repeated clouds/functions are not
an unseen round2 holdout. At n12 the own midpoint28 norm lower samples
are54.0668171 (localdet) and25.2485179 (candidate); continuous-orthonormal
coefficient noise risks are2.09767467 and1.61708653. The maximum
reproduction residual across these24 cases is5.30e-13.

All function/noise regressions remain. In particular the n2 candidate's
coefficient noise risk increases0.81731246→0.91638588 even though its
sampled norm improves. At n8 the producer nonsmooth function's own
Halton RMS increases0.0297303→0.0324021, and at n12 it increases
0.0188794→0.0193909. None of these cases is removed from the raw
assessment or recast as universal approximation/noise dominance.

### Essential degree12 exact statement

The later essential payload is a deliberate exception to the generic
raw-only boundary above. Its14853-byte file is
[u2-degree12-nodes.json](evidence/u2-degree12-nodes.json), SHA-256
`ade51c2e459b2d3161eddab564e1ada2233d2f841b5dd64bf808b2e607f7140f`.
The actual standalone independent
[checker](code/uc12_payload_check.py) imports only Python's standard
library. It decodes the IEEE754 integer bit fields directly, without
NumPy, a producer import or float.as_integer_ratio, and verifies the
10920 coordinate bytes and their hash,455 exact distinct dyadic triples
in the closed cube, and all455 monomial pivots modulo1000037. That prime
was checked by complete integer trial division. The determinant residue
is318086; [actual receipt](evidence/uc12-u2-payload.json). The frozen
checker hash is
`c7a2d190758cc246b9037b13065115ae5ec63312d5a811de4c429cc4f452b3a0`.

The separate [exact-unisolvence theory](theory/u2-degree12-unisolvence.md)
was read and its modular reduction reconstructed: all entries lie in
Z[1/2]; reduction to the odd-prime field commutes with the determinant;
a nonzero residue excludes a zero rational determinant. This establishes
the stated finite unisolvence claim once the essential payload, checker
and receipt are published together. No proof gap was found in that
narrow computer-assisted statement. It uses no raw optimization log or
floating norm premise and does not promote numerical quality to PROVED.

A second stdlib-only [byte-link checker](code/uc12_payload_link.py)
independently parses the measured NPY header and verifies that its
coordinate bytes equal the essential payload exactly; it also verifies
the source node and holdout-receipt hashes:
[link receipt](evidence/uc12-u2-payload-link.json). Thus the exact stored
set is the set receiving the measured n12 assessments. This linkage is
separate from the modular proof and gives no norm enclosure.

## Final assigned-scope status

Completed: U1's two registered rounds; U2's failed original rule, its
collision-safe pilot and unchanged n10/12 extension; independent
conditioning/reproduction/API/approximation/noise checks; all-trial
geometric/Neumann reconstruction; and the essential n12 exact data check.
No unresolved discrepancy remains in that declared scope. The scoped
limitations and mixed practical outcomes above remain. Claude's required
substantive audit, root publication/integration and all-degree questions
are separate from this supplementary check.

Final owned-scope validation actually checked265 current code/data
identities, parsed all9 own receipts (1363–14782 bytes), and checked all19
owned report links. All8 own checker/generator sources are frozen at the
identities in those receipts/raw maps; no additional evidence JSON was
created for this integration check. Raw data are regenerable as described
above, while the essential degree12 payload is separate finite-proof data.
